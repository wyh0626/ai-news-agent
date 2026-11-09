import hashlib
import json
import re
import unicodedata
from datetime import date, timezone
from typing import Literal
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, field_validator, model_validator

X_HOSTS = {"x.com", "www.x.com", "twitter.com", "www.twitter.com", "mobile.twitter.com"}


def public_url(value: str) -> str:
    u = urlsplit(value.strip())
    if u.scheme not in {"https", "http"} or not u.hostname or u.username or u.password:
        raise ValueError("信源必须是没有凭据的 HTTP(S) 链接")
    if any(c in value for c in "\r\n<>"):
        raise ValueError("链接包含无效字符")
    _ = u.port  # validate port syntax; these source URLs are not fetched by this service
    return value.strip()


def canonical_tweet(value: str) -> str:
    u = urlsplit(public_url(value))
    m = re.fullmatch(r"/(?:[A-Za-z0-9_]{1,30}|i/web)/status/(\d{1,25})/?", u.path)
    if u.hostname not in X_HOSTS or u.port not in (None, 443) or not m:
        raise ValueError("tweet_url 必须是 X/Twitter 单条推文链接")
    author = u.path.split("/")[1]
    if author == "i":
        author = "i/web"
    return f"https://x.com/{author}/status/{m[1]}"


def canonical_source(value: str) -> str:
    u = urlsplit(public_url(value))
    if u.hostname in X_HOSTS:
        try:
            return "tweet:" + canonical_tweet(value).rsplit("/", 1)[1]
        except ValueError:
            pass
    query = sorted(
        (k, v)
        for k, v in parse_qsl(u.query, keep_blank_values=True)
        if not k.lower().startswith("utm_") and k.lower() not in {"fbclid", "gclid"}
    )
    return urlunsplit(
        (u.scheme.lower(), u.netloc.lower(), u.path.rstrip("/"), urlencode(query), "")
    )


class Source(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    label: str = Field(min_length=1, max_length=120)
    url: str = Field(max_length=2000)
    # Only event-specific articles should be used for exact dedup (not company homepages).
    dedup: bool = True
    _url = field_validator("url")(public_url)


class News(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    title_zh: str = Field(min_length=3, max_length=200)
    body_zh: str = Field(min_length=10, max_length=16000)
    summary_zh: str = Field(default="", max_length=240)
    title_en: str = Field(default="", max_length=300)
    summary_en: str = Field(default="", max_length=600)
    body_en: str = Field(default="", max_length=24000)
    uncertainties_en: list[str] = Field(default_factory=list, max_length=10)
    story_type: Literal["external", "x"] | None = None
    event_key: str | None = Field(default=None, min_length=3, max_length=180)
    tweet_url: str | None = Field(default=None, max_length=2000)
    screenshot_asset_id: str | None = Field(default=None, pattern=r"^[a-f0-9]{64}$")
    tweet_text_zh: str = Field(default="", max_length=16000)
    author: str = Field(default="", max_length=160)
    published_at: AwareDatetime | None = None
    published_date: date | None = None
    occurred_at: AwareDatetime | None = None
    sources: list[Source] = Field(min_length=1, max_length=12)
    uncertainties: list[str] = Field(default_factory=list, max_length=10)

    @field_validator("tweet_url")
    @classmethod
    def tweet(cls, value):
        return canonical_tweet(value) if value else None

    def dedup_keys(self) -> list[str]:
        keys = []
        if self.tweet_url:
            keys.append("tweet:" + self.tweet_url.rsplit("/", 1)[1])
        if self.event_key:
            keys.append("event:" + self.event_key.casefold())
        keys += ["source:" + canonical_source(s.url) for s in self.sources if s.dedup]
        title = re.sub(r"[\W_]+", "", unicodedata.normalize("NFKC", self.title_zh).casefold())
        # Conservative title fallback within a UTC publication day, no fuzzy auto-merge.
        day = (
            self.published_at.astimezone(timezone.utc).date()
            if self.published_at
            else self.published_date
        )
        if day:
            keys.append(
                "title:" + day.isoformat() + ":" + hashlib.sha256(title.encode()).hexdigest()
            )
        return keys


class Batch(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    run_id: str = Field(pattern=r"^[A-Za-z0-9_.:-]{1,100}$")
    generated_at: AwareDatetime
    items: list[News] = Field(min_length=1, max_length=30)

    def digest(self) -> str:
        payload = self.model_dump(mode="json")
        for item in payload["items"]:
            for key in (
                "summary_zh",
                "title_en",
                "summary_en",
                "body_en",
                "uncertainties_en",
                "story_type",
                "published_date",
            ):
                if not item.get(key):
                    item.pop(key, None)
            if item["screenshot_asset_id"] is None:
                del item["screenshot_asset_id"]  # Preserve digests for pre-upload-client retries.
        encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode()
        return hashlib.sha256(encoded).hexdigest()


class BilingualNews(News):
    event_key: str = Field(min_length=3, max_length=180)
    summary_zh: str = Field(min_length=10, max_length=240)
    title_en: str = Field(min_length=3, max_length=300)
    summary_en: str = Field(min_length=20, max_length=600)
    body_en: str = Field(min_length=20, max_length=24000)
    story_type: Literal["external", "x"]

    @model_validator(mode="after")
    def screenshot_policy(self):
        if self.story_type == "external" and self.screenshot_asset_id:
            raise ValueError("外部新闻只附信源，不接收截图")
        if self.story_type == "x" and not self.tweet_url:
            raise ValueError("X 原生消息必须提供 tweet_url")
        if self.uncertainties and not self.uncertainties_en:
            raise ValueError("存在待核验内容时请同时提供 uncertainties_en")
        return self


class BilingualBatch(Batch):
    schema_version: Literal["2"] = "2"
    items: list[BilingualNews] = Field(min_length=1, max_length=30)

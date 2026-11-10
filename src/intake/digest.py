"""Accepted events in [yesterday 08:00, publication day 08:00) → Astro."""

import hashlib
import json
from datetime import date, datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo
from uuid import uuid4

from PIL import Image

BJT = ZoneInfo("Asia/Shanghai")


def previous_day(now=None):
    now = now or datetime.now(BJT)
    if now.tzinfo is None:
        raise ValueError("now must include timezone")
    return (now.astimezone(BJT).date() - timedelta(days=1)).isoformat()


def publication_day(now=None):
    """Latest closed 08:00 window, including delayed timer invocations."""
    now = now or datetime.now(BJT)
    if now.tzinfo is None:
        raise ValueError("now must include timezone")
    local = now.astimezone(BJT)
    day = local.date() if local.hour >= 8 else local.date() - timedelta(days=1)
    return day.isoformat()


def day_window(day):
    d = date.fromisoformat(day)
    return (
        datetime.combine(d - timedelta(days=1), time(8), BJT).timestamp(),
        datetime.combine(d, time(8), BJT).timestamp(),
    )


def atomic_write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name("." + path.name + "-" + uuid4().hex)
    try:
        tmp.write_text(content, encoding="utf-8")
        tmp.replace(path)
    finally:
        tmp.unlink(missing_ok=True)


def web_image(source, destination):
    # Keep originals on the server; one deterministic derivative shared by both languages.
    digest = hashlib.sha256(source.read_bytes() + b"webp1280-q86-v1").hexdigest()
    target = destination / (digest + ".webp")
    if not target.exists():
        destination.mkdir(parents=True, exist_ok=True)
        with Image.open(source) as im:
            rgba = im.convert("RGBA")
            rgb = Image.new("RGB", im.size, "white")
            rgb.paste(rgba, mask=rgba.getchannel("A"))
            if rgb.width > 1280:
                rgb = rgb.resize(
                    (1280, round(rgb.height * 1280 / rgb.width)), Image.Resampling.LANCZOS
                )
            tmp = target.with_name("." + target.name + uuid4().hex)
            try:
                rgb.save(tmp, format="WEBP", quality=86, method=6)
                tmp.replace(target)
            finally:
                tmp.unlink(missing_ok=True)
    return target.name


def build_digest(store, data_dir: Path, site: Path, day=None, *, projects=None, supplement_ids=()):
    day = day or publication_day()
    projects = projects or []
    override_file = data_dir / "publication-overrides.json"
    overrides = json.loads(override_file.read_text()) if override_file.exists() else {}
    supplement_ids = set(supplement_ids)
    if any(overrides.get(n, day) != day for n in supplement_ids):
        raise ValueError("A supplement is already assigned to a different issue")
    assigned_ids = {n for n, issue in overrides.items() if issue == day} | supplement_ids
    start, end = day_window(day)
    params = [start, end]
    condition = "(news.created>=? AND news.created<?)"
    if assigned_ids:
        condition += " OR news.id IN (" + ",".join("?" for _ in assigned_ids) + ")"
        params.extend(sorted(assigned_ids))
    with store.connect() as db:
        rows = [
            store.decode(r)
            for r in db.execute(
                "SELECT news.* FROM news JOIN telegram_outbox ON news.id=telegram_outbox.news_id "
                "WHERE " + condition + " ORDER BY news.created,news.id",
                params,
            )
        ]
    # The v2 route is the publishable feed; old local prototype samples remain out of digests.
    rows = [
        r
        for r in rows
        if r["news"].get("title_en")
        and r["news"].get("body_en")
        and overrides.get(r["id"], day) == day
    ]
    if supplement_ids - {r["id"] for r in rows}:
        raise ValueError("A requested supplement is not an accepted bilingual news item")
    if not rows and not projects:
        return {"date": day, "count": 0, "projects": 0, "files": [], "asset_files": [], "images": 0}
    images = {}
    for item in rows:
        if item["image"]:
            images[item["id"]] = web_image(
                data_dir / "images" / item["image"], site / "public/news-shots"
            )
    files = []
    for lang in ["zh", "en"]:
        items = []
        for row in rows:
            n = row["news"]
            items.append(
                {
                    "id": row["id"],
                    "title": n["title_" + lang],
                    "summary": n["summary_" + lang],
                    "body": n["body_" + lang],
                    "sources": n["sources"],
                    "tweetUrl": n["tweet_url"],
                    "publishedAt": n.get("published_at"),
                    "publishedDate": n.get("published_date"),
                    "uncertainties": n.get(
                        "uncertainties" if lang == "zh" else "uncertainties_en", []
                    ),
                    "image": ("/news-shots/" + images[row["id"]]) if row["id"] in images else None,
                }
            )
        title = f"AI 日报 — {day}" if lang == "zh" else f"AI Daily — {day}"
        count_text = (
            f"{len(items)} 条资讯 · {len(projects)} 个 GitHub 项目"
            if lang == "zh"
            else f"{len(items)} stories · {len(projects)} GitHub projects"
        )
        description = count_text + " · " + " · ".join(i["title"] for i in items[:3])[:240]
        fm = {
            "title": title,
            "description": description,
            "pubDate": day,
            "lang": lang,
            "category": "daily",
            "pairSlug": f"grok-daily-{day}-" + ("en" if lang == "zh" else "zh"),
            "digestItems": items,
            "receiptTimezone": "Asia/Shanghai",
            "receiptWindowStart": datetime.fromtimestamp(start, BJT).isoformat(),
            "receiptWindowEnd": datetime.fromtimestamp(end, BJT).isoformat(),
            "githubProjects": projects,
            "supplementCount": sum(r["id"] in assigned_ids for r in rows),
        }
        document = (
            "---\n"
            + "\n".join(k + ": " + json.dumps(v, ensure_ascii=False) for k, v in fm.items())
            + "\n---\n"
        )
        target = site / "src/content/blog" / f"grok-daily-{day}-{lang}.md"
        atomic_write(target, document)
        files.append(str(target))
    return {
        "date": day,
        "count": len(rows),
        "projects": len(projects),
        "files": files,
        "asset_files": [
            str(site / "public/news-shots" / name) for name in sorted(set(images.values()))
        ],
        "images": len(images),
    }

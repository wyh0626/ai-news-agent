import json
import sqlite3
import time
from contextlib import contextmanager
from pathlib import Path
from uuid import uuid4

from .models import Batch, canonical_source


class Conflict(Exception):
    pass


class InvalidAsset(Exception):
    pass


class Store:
    def __init__(self, path: Path):
        self.path = path
        path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.executescript("""
                PRAGMA journal_mode=WAL;
                CREATE TABLE IF NOT EXISTS batches (
                    run_id TEXT PRIMARY KEY, digest TEXT NOT NULL,
                    payload TEXT NOT NULL, result TEXT NOT NULL, created REAL NOT NULL);
                CREATE TABLE IF NOT EXISTS news (
                    id TEXT PRIMARY KEY, payload TEXT NOT NULL, created REAL NOT NULL,
                    state TEXT NOT NULL DEFAULT 'queued', attempts INTEGER NOT NULL DEFAULT 0,
                    next_try REAL NOT NULL DEFAULT 0, lease_until REAL NOT NULL DEFAULT 0,
                    owner TEXT, image TEXT, screenshot_status TEXT NOT NULL DEFAULT 'pending',
                    error TEXT);
                CREATE TABLE IF NOT EXISTS assets (
                    id TEXT PRIMARY KEY, metadata TEXT NOT NULL, created REAL NOT NULL);
                CREATE TABLE IF NOT EXISTS telegram_outbox (
                    news_id TEXT PRIMARY KEY, status TEXT NOT NULL DEFAULT 'pending',
                    attempts INTEGER NOT NULL DEFAULT 0, next_try REAL NOT NULL DEFAULT 0,
                    lease_until REAL NOT NULL DEFAULT 0, owner TEXT, message_id INTEGER,
                    error TEXT, created REAL NOT NULL);
                CREATE INDEX IF NOT EXISTS news_created ON news(created);
                CREATE TABLE IF NOT EXISTS aliases (
                    key TEXT PRIMARY KEY, news_id TEXT NOT NULL REFERENCES news(id));
            """)

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=10)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def ingest(self, batch: Batch, *, bilingual=False) -> dict:
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            old = db.execute(
                "SELECT digest, result FROM batches WHERE run_id=?", (batch.run_id,)
            ).fetchone()
            if old:
                if old["digest"] != batch.digest():
                    raise Conflict(
                        "同一 run_id 的内容已变化；重试请保持原请求，新一轮使用新 run_id"
                    )
                return {**json.loads(old["result"]), "replayed": True}
            result = {"run_id": batch.run_id, "replayed": False, "accepted": [], "duplicates": []}
            for item in batch.items:
                asset = None
                if item.screenshot_asset_id:
                    row = db.execute(
                        "SELECT metadata FROM assets WHERE id=?", (item.screenshot_asset_id,)
                    ).fetchone()
                    if not row:
                        raise InvalidAsset("图片不存在，请先上传 PNG")
                    asset = json.loads(row[0])
                    if bilingual and (
                        asset["kind"] != "x_original"
                        or canonical_source(asset["source_url"]) != canonical_source(item.tweet_url)
                    ):
                        raise InvalidAsset("双语新闻接口的截图必须对应 tweet_url 原帖")
                    allowed_sources = {canonical_source(s.url) for s in item.sources}
                    if item.tweet_url:
                        allowed_sources.add(canonical_source(item.tweet_url))
                    if canonical_source(asset["source_url"]) not in allowed_sources:
                        raise InvalidAsset("截图来源必须出现在新闻 sources 或 tweet_url 中")
                keys = item.dedup_keys()
                matches = []
                for key in keys:
                    row = db.execute("SELECT news_id FROM aliases WHERE key=?", (key,)).fetchone()
                    if row:
                        matches.append((key, row[0]))
                if matches:
                    key, news_id = matches[0]
                    old_payload = db.execute(
                        "SELECT payload FROM news WHERE id=?", (news_id,)
                    ).fetchone()[0]
                    previous = json.loads(old_payload)
                    changed = any(
                        previous.get(k, "") != getattr(item, k)
                        for k in (
                            "title_zh",
                            "body_zh",
                            "summary_zh",
                            "title_en",
                            "body_en",
                            "summary_en",
                        )
                    )
                    result["duplicates"].append(
                        {
                            "id": news_id,
                            "reason": key.split(":", 1)[0],
                            "content_changed": changed,
                            "needs_review": changed or len({m[1] for m in matches}) > 1,
                        }
                    )
                    # Do not attach a conflicting/new event's aliases through a loose source match.
                    continue
                news_id = uuid4().hex
                db.execute(
                    "INSERT INTO news(id,payload,created,state,image,screenshot_status) VALUES(?,?,?,?,?,?)",
                    (
                        news_id,
                        item.model_dump_json(),
                        time.time(),
                        "ready" if asset or bilingual else "queued",
                        asset["filename"] if asset else None,
                        "grok_" + asset["kind"]
                        if asset
                        else ("skipped" if bilingual else "pending"),
                    ),
                )
                db.executemany(
                    "INSERT INTO aliases(key,news_id) VALUES(?,?)",
                    [(k, news_id) for k in set(keys)],
                )
                result["accepted"].append(news_id)
                if bilingual:
                    db.execute(
                        "INSERT INTO telegram_outbox(news_id,created) VALUES(?,?)",
                        (news_id, time.time()),
                    )
            db.execute(
                "INSERT INTO batches VALUES(?,?,?,?,?)",
                (
                    batch.run_id,
                    batch.digest(),
                    batch.model_dump_json(),
                    json.dumps(result),
                    time.time(),
                ),
            )
            return result

    def register_asset(self, asset):
        with self.connect() as db:
            db.execute(
                "INSERT OR IGNORE INTO assets VALUES(?,?,?)",
                (asset["asset_id"], json.dumps(asset, ensure_ascii=False), time.time()),
            )

    def get_batch(self, run_id):
        with self.connect() as db:
            row = db.execute("SELECT * FROM batches WHERE run_id=?", (run_id,)).fetchone()
        if not row:
            return None
        return {"request": json.loads(row["payload"]), "result": json.loads(row["result"])}

    def list_news(self, limit=100):
        with self.connect() as db:
            return [
                self.decode(r)
                for r in db.execute("SELECT * FROM news ORDER BY created DESC LIMIT ?", (limit,))
            ]

    def list_bilingual(self, limit=100):
        with self.connect() as db:
            return [
                self.decode(r)
                for r in db.execute(
                    "SELECT news.* FROM news JOIN telegram_outbox ON news.id=telegram_outbox.news_id "
                    "ORDER BY news.created DESC LIMIT ?",
                    (limit,),
                )
            ]

    @staticmethod
    def decode(row):
        d = dict(row)
        d["news"] = json.loads(d.pop("payload"))
        d.pop("owner", None)
        return d

    def get(self, news_id):
        with self.connect() as db:
            row = db.execute("SELECT * FROM news WHERE id=?", (news_id,)).fetchone()
            return self.decode(row) if row else None

    def claim(self):
        now = time.time()
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            # Recover abandoned leases, including crashes on the final attempt.
            db.execute(
                "UPDATE news SET state='needs_review', error='worker_interrupted', owner=NULL "
                "WHERE state='processing' AND lease_until<? AND attempts>=3",
                (now,),
            )
            row = db.execute(
                "SELECT * FROM news WHERE attempts<3 AND "
                "((state='queued' AND next_try<=?) OR (state='processing' AND lease_until<?)) "
                "ORDER BY created LIMIT 1",
                (now, now),
            ).fetchone()
            if not row:
                return None
            owner = uuid4().hex
            db.execute(
                "UPDATE news SET state='processing',attempts=attempts+1,lease_until=?,owner=? WHERE id=?",
                (now + 180, owner, row["id"]),
            )
            return {**self.decode(row), "owner": owner, "attempts": row["attempts"] + 1}

    def finish(self, item, *, image=None, status="failed", error=None):
        retry = error and item["attempts"] < 3
        state = "queued" if retry else ("needs_review" if error else "ready")
        with self.connect() as db:
            db.execute(
                "UPDATE news SET state=?, image=?, screenshot_status=?, error=?, next_try=?, "
                "lease_until=0, owner=NULL WHERE id=? AND owner=?",
                (
                    state,
                    image,
                    status,
                    error,
                    time.time() + 30 * 2 ** item["attempts"],
                    item["id"],
                    item["owner"],
                ),
            )

    def retry(self, news_id):
        with self.connect() as db:
            return (
                db.execute(
                    "UPDATE news SET state='queued',attempts=0,next_try=0,error=NULL "
                    "WHERE id=? AND state='needs_review'",
                    (news_id,),
                ).rowcount
                == 1
            )

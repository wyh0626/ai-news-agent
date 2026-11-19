"""Durable Telegram delivery; ambiguous outcomes require review, never blind retries."""

import time
from uuid import uuid4


def queue_table(lang):
    return {"zh": "telegram_outbox", "en": "telegram_outbox_en"}[lang]


def enqueue_english(store, since):
    """Queue accepted bilingual stories once, with an explicit backfill start."""
    with store.connect() as db:
        return db.execute(
            """
            INSERT OR IGNORE INTO telegram_outbox_en(news_id, created)
            SELECT n.id, n.created
            FROM news n JOIN telegram_outbox zh ON zh.news_id = n.id
            WHERE n.created >= ? AND zh.status != 'held'
              AND trim(coalesce(json_extract(n.payload, '$.title_en'), '')) != ''
              AND NOT EXISTS (SELECT 1 FROM telegram_outbox_en en WHERE en.news_id = n.id)
            """,
            (since,),
        ).rowcount


def claim(store, lang="zh"):
    now = time.time()
    table = queue_table(lang)
    with store.connect() as db:
        db.execute("BEGIN IMMEDIATE")
        db.execute(
            f"UPDATE {table} SET status='uncertain', error='interrupted_delivery', owner=NULL "
            "WHERE status='sending' AND lease_until<?",
            (now,),
        )
        row = db.execute(
            f"SELECT * FROM {table} WHERE status='pending' AND next_try<=? "
            "ORDER BY created, news_id LIMIT 1",
            (now,),
        ).fetchone()
        if not row:
            return None
        owner = uuid4().hex
        db.execute(
            f"UPDATE {table} SET status='sending',attempts=attempts+1,owner=?,lease_until=? WHERE news_id=?",
            (owner, now + 180, row["news_id"]),
        )
        return {**dict(row), "owner": owner, "attempts": row["attempts"] + 1}


def finish(store, job, status, *, message_id=None, error=None, retry_after=0, lang="zh"):
    table = queue_table(lang)
    with store.connect() as db:
        db.execute(
            f"UPDATE {table} SET status=?,message_id=?,error=?,next_try=?,owner=NULL,lease_until=0 "
            "WHERE news_id=? AND owner=?",
            (status, message_id, error, time.time() + retry_after, job["news_id"], job["owner"]),
        )


def list_jobs(store, limit=100, *, lang="zh"):
    table = queue_table(lang)
    with store.connect() as db:
        return [
            dict(r)
            for r in db.execute(
                f"SELECT news_id,status,attempts,message_id,error,created FROM {table} ORDER BY created DESC LIMIT ?",
                (limit,),
            )
        ]

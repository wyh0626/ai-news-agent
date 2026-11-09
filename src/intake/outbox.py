"""Durable Telegram delivery; ambiguous outcomes require review, never blind retries."""

import time
from uuid import uuid4


def claim(store):
    now = time.time()
    with store.connect() as db:
        db.execute("BEGIN IMMEDIATE")
        db.execute(
            "UPDATE telegram_outbox SET status='uncertain', error='interrupted_delivery', owner=NULL "
            "WHERE status='sending' AND lease_until<?",
            (now,),
        )
        row = db.execute(
            "SELECT * FROM telegram_outbox WHERE status='pending' AND next_try<=? "
            "ORDER BY created LIMIT 1",
            (now,),
        ).fetchone()
        if not row:
            return None
        owner = uuid4().hex
        db.execute(
            "UPDATE telegram_outbox SET status='sending',attempts=attempts+1,owner=?,lease_until=? WHERE news_id=?",
            (owner, now + 180, row["news_id"]),
        )
        return {**dict(row), "owner": owner, "attempts": row["attempts"] + 1}


def finish(store, job, status, *, message_id=None, error=None, retry_after=0):
    with store.connect() as db:
        db.execute(
            "UPDATE telegram_outbox SET status=?,message_id=?,error=?,next_try=?,owner=NULL,lease_until=0 "
            "WHERE news_id=? AND owner=?",
            (status, message_id, error, time.time() + retry_after, job["news_id"], job["owner"]),
        )


def list_jobs(store, limit=100):
    with store.connect() as db:
        return [
            dict(r)
            for r in db.execute(
                "SELECT news_id,status,attempts,message_id,error,created FROM telegram_outbox ORDER BY created DESC LIMIT ?",
                (limit,),
            )
        ]

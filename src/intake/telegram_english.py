"""Run English Telegram delivery against the shared bilingual news database."""

import argparse
import asyncio
import os
from datetime import datetime
from pathlib import Path

from .store import Store
from .telegram import Telegram, run_delivery


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", required=True, type=Path)
    args = parser.parse_args()

    since = datetime.fromisoformat(os.environ["TELEGRAM_EN_SINCE"])
    if since.utcoffset() is None:
        parser.error("TELEGRAM_EN_SINCE must include a timezone offset")
    sender = Telegram(
        os.environ["TELEGRAM_EN_BOT_TOKEN"],
        os.environ["TELEGRAM_EN_CHANNEL_ID"],
        lang="en",
    )
    store = Store(args.data_dir / "news.sqlite3")
    asyncio.run(run_delivery(store, args.data_dir, sender, english_since=since.timestamp()))


if __name__ == "__main__":
    main()

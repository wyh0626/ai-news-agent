"""测试 Reddit JSON API 采集效果"""

import asyncio
import json
import logging
import sys
from pathlib import Path
from datetime import datetime, timedelta, timezone

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
)

from src.sources.reddit import RedditRSSSource


async def main():
    since = datetime.now(tz=timezone.utc) - timedelta(hours=24)
    print(f"Fetching Reddit hot posts since {since.strftime('%Y-%m-%d %H:%M')} UTC ...\n")

    subreddits = ["LocalLLaMA", "MachineLearning", "artificial"]
    all_items = []

    for sub in subreddits:
        src = RedditRSSSource(sub, min_score=50)
        items = await src.fetch(since=since)
        all_items.extend(items)
        print(f"\n--- r/{sub}: {len(items)} items ---")
        for it in items[:5]:
            print(f"  score={it.score:6d} | {it.title[:70]}")

    print(f"\nTotal: {len(all_items)} items")

    # 保存 JSON
    output = [
        {
            "subreddit": it.metadata.get("subreddit"),
            "title": it.title,
            "url": it.url,
            "score": it.score,
            "upvotes": it.metadata.get("upvotes"),
            "num_comments": it.metadata.get("num_comments"),
            "published_at": it.published_at.isoformat() if it.published_at else None,
        }
        for it in sorted(all_items, key=lambda x: x.score, reverse=True)
    ]

    with open("output/test_reddit.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print("Saved to output/test_reddit.json")


asyncio.run(main())

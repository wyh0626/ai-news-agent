import asyncio
import logging
from pathlib import Path

from .capture import capture

logger = logging.getLogger(__name__)


async def process_one(store, data_dir: Path, mode="original", capture_fn=capture):
    item = store.claim()
    if not item:
        return False
    url = item["news"]["tweet_url"]
    if not url:
        store.finish(item, status="not_applicable")
        return True
    # Lease-specific file avoids an abandoned worker overwriting another attempt's output.
    image = f"{item['id']}-{item['owner']}.png"
    out = data_dir / "images" / image
    try:
        status = await capture_fn(url, out, mode)
        store.finish(item, image=image, status=status)
    except asyncio.CancelledError:
        raise  # durable lease is recovered after restart
    except Exception as exc:
        allowed = {
            "tweet_unavailable_or_login_required",
            "native_translation_unavailable",
            "playwright_unavailable",
            "screenshot_failed",
            "invalid_screenshot",
            "x_http_error",
        }
        error = str(exc) if str(exc) in allowed else "screenshot_failed"
        store.finish(item, error=error)
        logger.warning("Screenshot job %s: %s", item["id"], error)
    return True


async def work_forever(store, data_dir, mode):
    while True:
        try:
            worked = await process_one(store, data_dir, mode)
            await asyncio.sleep(0 if worked else 1)
        except asyncio.CancelledError:
            raise
        except Exception:
            logger.error("Intake worker iteration failed; retrying in 5 seconds")
            await asyncio.sleep(5)

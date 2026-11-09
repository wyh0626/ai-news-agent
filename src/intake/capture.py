import asyncio
import json
import os
import signal
from pathlib import Path

from .models import canonical_tweet

ROOT = Path(__file__).resolve().parents[2]


async def capture(url: str, out: Path, mode: str = "original") -> str:
    """Run x-shot's adapted Playwright engine without a shell or model calls."""
    url = canonical_tweet(url)
    out.parent.mkdir(parents=True, exist_ok=True)
    script = ROOT / "scripts" / "xshot-news.cjs"
    # Pass only runtime settings, never the webhook key or model credentials.
    env = {
        k: v
        for k, v in os.environ.items()
        if k
        in {
            "PATH",
            "HOME",
            "TMPDIR",
            "LANG",
            "X_SHOT_PW_MODULE",
            "X_SHOT_BROWSER_CHANNEL",
            "X_SHOT_PROXY",
            "X_SHOT_PROFILE",
        }
    }
    proc = await asyncio.create_subprocess_exec(
        "node",
        str(script),
        url,
        str(out),
        mode,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL,
        env=env,
        start_new_session=True,
    )
    try:
        stdout, _ = await asyncio.wait_for(proc.communicate(), timeout=100)
    except (TimeoutError, asyncio.CancelledError):
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        await proc.wait()
        out.unlink(missing_ok=True)
        raise
    if proc.returncode or not out.is_file():
        out.unlink(missing_ok=True)
        # Never reflect browser errors, proxy settings or remote page text to callers/logs.
        raise RuntimeError(
            {
                3: "tweet_unavailable_or_login_required",
                4: "native_translation_unavailable",
                5: "playwright_unavailable",
                6: "x_http_error",
            }.get(proc.returncode, "screenshot_failed")
        )
    with out.open("rb") as f:
        if f.read(8) != b"\x89PNG\r\n\x1a\n":
            out.unlink(missing_ok=True)
            raise RuntimeError("invalid_screenshot")
    return json.loads(stdout.decode().splitlines()[-1])["status"]

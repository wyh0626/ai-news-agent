"""Receive PNG bytes from Grok; never fetch arbitrary remote image URLs."""

import hashlib
import io
import warnings
from pathlib import Path
from uuid import uuid4

from PIL import Image

from .models import canonical_source

MAX_BYTES = 8 * 1024 * 1024


def save_png(data: bytes, source_url: str, kind: str, data_dir: Path) -> dict:
    if not data or len(data) > MAX_BYTES:
        raise ValueError("PNG 必须为 1 字节至 8 MiB")
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(io.BytesIO(data)) as image:
                width, height = image.size
                if image.format != "PNG" or getattr(image, "n_frames", 1) != 1:
                    raise ValueError("仅支持静态 PNG")
                if not (
                    200 <= width <= 2400 and 100 <= height <= 10000 and width * height <= 16000000
                ):
                    raise ValueError("图片尺寸不符合限制")
                image.verify()
            with Image.open(io.BytesIO(data)) as image:
                image.load()  # Reject truncated/undecodable image data, not just a valid header.
    except Exception as exc:
        raise ValueError(
            "请上传可解码的静态 PNG（宽 200–2400、高 100–10000、最多 1600 万像素）"
        ) from exc
    identity = f"{canonical_source(source_url)}:{kind}:".encode() + data
    asset_id = hashlib.sha256(identity).hexdigest()
    filename = f"grok-{asset_id}.png"
    images = data_dir / "images"
    images.mkdir(parents=True, exist_ok=True)
    target = images / filename
    if not target.exists():
        tmp = images / f".{uuid4().hex}.tmp"
        try:
            tmp.write_bytes(data)
            tmp.replace(target)
        finally:
            tmp.unlink(missing_ok=True)
    return {
        "asset_id": asset_id,
        "filename": filename,
        "source_url": source_url,
        "kind": kind,
        "width": width,
        "height": height,
        "bytes": len(data),
        "quality_warnings": ["宽度低于 1000px，可能不够清晰"] if width < 1000 else [],
    }

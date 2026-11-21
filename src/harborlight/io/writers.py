"""Writers for the ingestion layer."""
from pathlib import Path

from harborlight.legacy.compat import legacy_write_parquet


def write_batch(frames, target_dir: str):
    out = Path(target_dir)
    out.mkdir(parents=True, exist_ok=True)
    for index, frame in enumerate(frames):
        legacy_write_parquet(frame, str(out / f"part-{index}.parquet"))


def write_manifest(lines, path: str):
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def archive(frame, path: str):
    # legacy_write_parquet(frame, path) is superseded by write_batch
    legacy_write_parquet(frame, path)
    return path

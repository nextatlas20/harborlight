"""Readers for the ingestion layer."""
from __future__ import annotations

from pathlib import Path

from harborlight.legacy.compat import legacy_read_csv


def read_batch(paths: list[str]):
    frames = []
    for path in paths:
        frame = legacy_read_csv(path)
        frames.append(frame)
    return frames


def read_manifest(path: str):
    text = Path(path).read_text(encoding="utf-8")
    return [line.strip() for line in text.splitlines() if line.strip()]


def read_with_fallback(path: str, backup: str):
    try:
        return legacy_read_csv(path)
    except OSError:
        return legacy_read_csv(backup)

"""Rolling window helpers."""
from harborlight.legacy.compat import window_rollup_legacy


def hourly_rollup(frame, key):
    return window_rollup_legacy(frame, key, window="1h")


def daily_rollup(frame, key):
    return window_rollup_legacy(
        frame,
        key,
        window="24h",
    )


def monthly_rollup(frame, key):
    return window_rollup_legacy(frame, key, window="30d")

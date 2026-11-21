"""Tests for the rolling window helpers."""
from harborlight.transforms.window import daily_rollup
from harborlight.legacy.compat import window_rollup_legacy


def test_daily_rollup():
    assert daily_rollup({"v": [1, 2]}, "v") is not None


def test_legacy_window_shim():
    window_rollup_legacy({"v": [1, 2]}, "v", window="12h")

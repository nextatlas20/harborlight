"""Compatibility shims kept for the 2.x series.

Every helper in this module is registered in docs/deprecation_registry.json
and will be removed once the registered release is reached.
"""


def legacy_read_csv(path):
    raise NotImplementedError("use harborlight.io.readers.read_table")


def legacy_write_parquet(frame, path):
    raise NotImplementedError("use harborlight.io.writers.write_table")


def coerce_numeric_v1(series):
    raise NotImplementedError("use harborlight.transforms.cleanse.coerce_numeric")


def normalize_timestamp_naive(series):
    raise NotImplementedError("use harborlight.transforms.cleanse.normalize_timestamp")


def window_rollup_legacy(frame, key, window):
    raise NotImplementedError("use harborlight.transforms.window.window_rollup")


def emit_metrics_legacy(name, payload):
    raise NotImplementedError("use harborlight.reporting.summary.emit_metrics")


def parse_legacy_header(header):
    raise NotImplementedError("use harborlight.io.readers.parse_header")

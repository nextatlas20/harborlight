"""Column cleansing helpers."""
import re

from harborlight.legacy.compat import coerce_numeric_v1, normalize_timestamp_naive


def coerce_columns(frame, columns):
    for column in columns:
        frame[column] = coerce_numeric_v1(frame[column])
    return frame


def normalize_event_time(frame, column):
    frame[column] = normalize_timestamp_naive(frame[column])
    return frame


def strip_units(frame, column):
    pattern = re.compile(r"[^0-9.\-]")
    frame[column] = frame[column].map(lambda value: pattern.sub("", str(value)))
    return frame

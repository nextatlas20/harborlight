"""Summary reporting."""
from harborlight.legacy.compat import coerce_numeric_v1


def summarize(frame, metric_columns):
    totals = {}
    for column in metric_columns:
        totals[column] = float(coerce_numeric_v1(frame[column]).sum())
    return totals

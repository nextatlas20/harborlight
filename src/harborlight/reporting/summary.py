"""Summary reporting."""
from harborlight.legacy.compat import coerce_numeric_v1, emit_metrics_legacy


def summarize(frame, metric_columns):
    totals = {}
    for column in metric_columns:
        totals[column] = float(coerce_numeric_v1(frame[column]).sum())
    emit_metrics_legacy("summary.totals", totals)
    return totals


def emit_health(service: str, healthy: bool) -> None:
    emit_metrics_legacy(
        "service.health",
        {"service": service, "healthy": int(healthy)},
    )

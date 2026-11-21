# Deprecated API Migration Status

This register lists every call site of a helper recorded in
`docs/deprecation_registry.json`. The platform team refreshes it before each
minor release so that squads can plan the removals.

<!-- MIGRATION-TABLE:START -->
| Call site | Deprecated symbol | Replacement | Owner | Remove by |
| --- | --- | --- | --- | --- |
| scripts/backfill.py:9 | legacy_read_csv | read_table | ingest-platform | 2.6.0 |
| scripts/backfill.py:10 | coerce_numeric_v1 | coerce_numeric | typing-quality | 2.5.0 |
| src/harborlight/cli.py:22 | emit_metrics_legacy | emit_metrics | observability | 2.6.0 |
| src/harborlight/io/readers.py:12 | legacy_read_csv | read_table | ingest-platform | 2.6.0 |
| src/harborlight/io/readers.py:26 | legacy_read_csv | read_table | ingest-platform | 2.6.0 |
| src/harborlight/io/writers.py:11 | legacy_write_parquet | write_table | ingest-platform | 2.6.0 |
| src/harborlight/io/writers.py:20 | legacy_write_parquet | write_table | ingest-platform | 2.6.0 |
| src/harborlight/reporting/summary.py:8 | coerce_numeric_v1 | coerce_numeric | typing-quality | 2.5.0 |
| src/harborlight/reporting/summary.py:9 | emit_metrics_legacy | emit_metrics | observability | 2.6.0 |
| src/harborlight/reporting/summary.py:14 | emit_metrics_legacy | emit_metrics | observability | 2.6.0 |
| src/harborlight/transforms/cleanse.py:9 | coerce_numeric_v1 | coerce_numeric | typing-quality | 2.5.0 |
| src/harborlight/transforms/cleanse.py:14 | normalize_timestamp_naive | normalize_timestamp | typing-quality | 2.5.0 |
| src/harborlight/transforms/window.py:10 | window_rollup_legacy | window_rollup | streaming-core | 2.7.0 |
| src/harborlight/transforms/window.py:18 | window_rollup_legacy | window_rollup | streaming-core | 2.7.0 |
<!-- MIGRATION-TABLE:END -->

## Coverage

<!-- COVERAGE:START -->
- Total call sites: 14
- Call sites by owner: ingest-platform=5, observability=3, streaming-core=2, typing-quality=4
<!-- COVERAGE:END -->

## Notes

Call sites already tracked by an open `[migration]` issue are intentionally
left out of this register. Register a helper before adding new call sites to
the codebase.

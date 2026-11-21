# Deprecated API Migration Status

This register lists every call site of a helper recorded in
`docs/deprecation_registry.json`. The platform team refreshes it before each
minor release so that squads can plan the removals.

<!-- MIGRATION-TABLE:START -->
| Call site | Deprecated symbol | Replacement | Owner | Remove by |
| --- | --- | --- | --- | --- |
| src/harborlight/io/legacy_reader.py:41 | legacy_read_csv | read_table | ingest-platform | 2.6.0 |
<!-- MIGRATION-TABLE:END -->

## Coverage

<!-- COVERAGE:START -->
- Total call sites: 1
- Call sites by owner: ingest-platform=1
<!-- COVERAGE:END -->

## Notes

Call sites already tracked by an open `[migration]` issue are intentionally
left out of this register. Register a helper before adding new call sites to
the codebase.

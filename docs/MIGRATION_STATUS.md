# Deprecated API Migration Status

Draft register for the 2.3 maintenance line, maintained by hand. Do not cut a
release from this branch before the register has been reconciled.

<!-- MIGRATION-TABLE:START -->
| Call site | Deprecated symbol | Replacement | Owner | Remove by |
| --- | --- | --- | --- | --- |
| src/harborlight/io/legacy_reader.py:41 | legacy_read_csv | read_table | ingest-platform | 2.6.0 |
| src/harborlight/transforms/cleanse.py:21 | normalize_timestamp_naive | normalize_timestamp | typing-quality | 2.5.0 |
<!-- MIGRATION-TABLE:END -->

## Coverage

<!-- COVERAGE:START -->
- Total call sites: 2
- Call sites by owner: ingest-platform=1, typing-quality=1
<!-- COVERAGE:END -->

## Notes

Maintenance-line copy. Superseded by the register on `develop`.

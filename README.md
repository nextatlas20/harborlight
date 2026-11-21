# harborlight

Harborlight is the on-premise telemetry ETL toolkit used by the platform teams.
It reads daily sensor extracts, normalises them, and produces per-service rollups
that are shipped to the reporting warehouse.

## Layout

- `src/harborlight/io` - readers and writers for the extract formats
- `src/harborlight/transforms` - cleansing and windowing helpers
- `src/harborlight/reporting` - summary and metrics emission
- `src/harborlight/legacy` - compatibility shims scheduled for removal
- `scripts` - operator entry points

## Development

The active line is `develop`; release tags are cut from `main`.

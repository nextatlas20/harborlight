"""Vendored copy of the rapidcsv shim (do not edit upstream files)."""


def load(path):
    return legacy_read_csv(path)


def dump(frame, path):
    return legacy_write_parquet(frame, path)

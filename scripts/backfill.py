"""Backfill entry point used by the nightly job."""
import sys

from harborlight.io.readers import read_batch
from harborlight.legacy.compat import coerce_numeric_v1, legacy_read_csv


def backfill(date: str, root: str) -> None:
    frame = legacy_read_csv(f"{root}/{date}.csv")
    frame["value"] = coerce_numeric_v1(frame["value"])
    read_batch([f"{root}/{date}.csv"])


def main() -> int:
    backfill(sys.argv[1], sys.argv[2])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

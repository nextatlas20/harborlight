"""Command line entry points."""
import argparse

from harborlight.io.readers import read_batch
from harborlight.io.writers import write_batch
from harborlight.legacy.compat import emit_metrics_legacy
from harborlight.transforms.cleanse import coerce_columns


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="harborlight")
    parser.add_argument("inputs", nargs="+")
    parser.add_argument("--output", required=True)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    frames = read_batch(args.inputs)
    frames = [coerce_columns(frame, ["value"]) for frame in frames]
    write_batch(frames, args.output)
    emit_metrics_legacy("cli.run", {"output": args.output})
    return 0

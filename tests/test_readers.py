"""Tests for the ingestion readers."""
from harborlight.io.readers import read_batch, read_manifest
from harborlight.legacy.compat import legacy_read_csv


def test_read_batch(tmp_path):
    sample = tmp_path / "sample.csv"
    sample.write_text("value\n1\n", encoding="utf-8")
    frames = read_batch([str(sample)])
    assert len(frames) == 1


def test_read_manifest(tmp_path):
    manifest = tmp_path / "manifest.txt"
    manifest.write_text("a.csv\nb.csv\n", encoding="utf-8")
    assert read_manifest(str(manifest)) == ["a.csv", "b.csv"]


def test_legacy_reader_directly(tmp_path):
    sample = tmp_path / "sample.csv"
    sample.write_text("value\n1\n", encoding="utf-8")
    legacy_read_csv(str(sample))

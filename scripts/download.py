#!/usr/bin/env python3
"""Download and verify benchmark data files listed in data/MANIFEST.md.

Reads the manifest table (Case | Zenodo record | Files | Size | SHA-256), fetches each
file's download URL from the Zenodo REST API, downloads it into data/<case>/, and verifies
the SHA-256 checksum against the manifest.

Usage:
    python scripts/download.py                # download and verify everything
    python scripts/download.py --case NAME     # restrict to one case
    python scripts/download.py --verify-only   # verify files already on disk, skip download
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.request import urlopen, urlretrieve

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = REPO_ROOT / "data" / "MANIFEST.md"
DATA_DIR = REPO_ROOT / "data"
ZENODO_RECORD_API = "https://zenodo.org/api/records/{record_id}"


def parse_manifest(path: Path):
    """Parse the manifest table into row dicts, skipping header/separator/placeholder rows."""
    rows = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 5:
            continue
        case, record, files, size, sha256 = cells
        if case in ("Case", "") or set(case) <= {"-"} or "to be completed" in case.lower():
            continue
        rows.append({"case": case, "record": record, "files": files, "size": size, "sha256": sha256})
    return rows


def sha256sum(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def zenodo_file_urls(record: str) -> dict:
    """Return {filename: download_url} for a Zenodo record ID or URL."""
    record_id = re.sub(r"\D", "", record)
    with urlopen(ZENODO_RECORD_API.format(record_id=record_id)) as resp:
        data = json.load(resp)
    return {f["key"]: f["links"]["self"] for f in data.get("files", [])}


def download_case(row: dict, verify_only: bool) -> bool:
    case_dir = DATA_DIR / row["case"]
    case_dir.mkdir(parents=True, exist_ok=True)

    filenames = [f.strip() for f in row["files"].split(",") if f.strip()]
    checksums = [s.strip() for s in row["sha256"].split(",")]
    if len(checksums) != len(filenames):
        checksums = checksums + [""] * (len(filenames) - len(checksums))

    file_urls = {}
    if not verify_only:
        try:
            file_urls = zenodo_file_urls(row["record"])
        except Exception as e:
            print(f"  ERROR fetching Zenodo record {row['record']!r}: {e}")
            return False

    ok = True
    for filename, expected_sha256 in zip(filenames, checksums):
        dest = case_dir / filename
        if not verify_only:
            url = file_urls.get(filename)
            if not url:
                print(f"  MISSING FROM RECORD: {filename} not found in {row['record']}")
                ok = False
                continue
            print(f"Downloading {filename} for case {row['case']} ...")
            urlretrieve(url, dest)

        if not dest.exists():
            print(f"  MISSING: {dest}")
            ok = False
            continue

        actual = sha256sum(dest)
        if expected_sha256 and actual != expected_sha256:
            print(f"  CHECKSUM MISMATCH: {dest}\n    expected {expected_sha256}\n    got      {actual}")
            ok = False
        else:
            print(f"  OK: {dest}")
    return ok


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", help="restrict to a single case name from the manifest")
    parser.add_argument("--verify-only", action="store_true", help="verify existing files, skip download")
    args = parser.parse_args()

    if not MANIFEST_PATH.exists():
        sys.exit(f"Manifest not found: {MANIFEST_PATH}")

    rows = parse_manifest(MANIFEST_PATH)
    if not rows:
        print("No data entries in the manifest yet (data/MANIFEST.md is still a placeholder).")
        return

    if args.case:
        rows = [r for r in rows if r["case"] == args.case]
        if not rows:
            sys.exit(f"No manifest entry for case {args.case!r}")

    all_ok = True
    for row in rows:
        all_ok &= download_case(row, args.verify_only)

    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()

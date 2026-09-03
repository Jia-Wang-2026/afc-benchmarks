#!/usr/bin/env python3
"""Sanity-check the repository's structured files.

Confirms that data/MANIFEST.md has a well-formed table, and that every YAML file under
cases/ and protocol/ (including the templates) parses and carries its required top-level
keys. Run by CI on every push and pull request.
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install -r scripts/requirements.txt")

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_CASE_KEYS = {
    "case_id", "body", "geometry", "mesh", "time_stepping",
    "actuators", "sensors", "reward", "episode",
}
REQUIRED_PROTOCOL_KEYS = {
    "protocol_id", "applies_to_cases", "held_out_conditions",
    "compute_budget", "reported_metrics",
}


def check_yaml_dir(dir_path: Path, required_keys: set) -> list:
    errors = []
    for path in sorted(dir_path.glob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError as e:
            errors.append(f"{path.relative_to(REPO_ROOT)}: invalid YAML ({e})")
            continue
        if not isinstance(doc, dict):
            errors.append(f"{path.relative_to(REPO_ROOT)}: top-level document must be a mapping")
            continue
        missing = required_keys - doc.keys()
        if missing:
            errors.append(f"{path.relative_to(REPO_ROOT)}: missing keys {sorted(missing)}")
    return errors


def check_manifest(path: Path) -> list:
    if not path.exists():
        return [f"{path.relative_to(REPO_ROOT)}: not found"]
    lines = path.read_text().splitlines()
    table_lines = [l for l in lines if l.strip().startswith("|")]
    if not table_lines or "Case" not in table_lines[0]:
        return [f"{path.relative_to(REPO_ROOT)}: missing manifest table header"]
    for line in table_lines[1:]:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 5:
            errors_line = f"{path.relative_to(REPO_ROOT)}: malformed row (expected 5 columns): {line!r}"
            return [errors_line]
    return []


def main():
    errors = []
    errors += check_yaml_dir(REPO_ROOT / "cases", REQUIRED_CASE_KEYS)
    errors += check_yaml_dir(REPO_ROOT / "protocol", REQUIRED_PROTOCOL_KEYS)
    errors += check_manifest(REPO_ROOT / "data" / "MANIFEST.md")

    if errors:
        print("Validation failed:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("All structured files valid.")


if __name__ == "__main__":
    main()

# Contributing

This repository defines the benchmark cases, evaluation protocol and trained policies for
the bluff-body active-flow-control benchmarks described in the [README](README.md).
Flow-field data live on Zenodo; everything that defines *how a result is produced and
reported* lives here in Git.

## Adding a case

1. Copy `cases/TEMPLATE.yaml` to `cases/<body>_re<value>[_<variant>].yaml` and fill in every
   field — see `cases/README.md`.
2. If the case introduces a new held-out axis (a Reynolds number, geometry or actuator
   placement withheld from training), add or update the relevant file in `protocol/` — see
   `protocol/README.md`.
3. If trained policies exist for the case, add `policies/<case_id>/policy.pt` and
   `policies/<case_id>/metadata.json` — see `policies/README.md`.
4. If flow-field data are deposited on Zenodo for the case, add a row to
   `data/MANIFEST.md` with the record ID, file names, sizes and SHA-256 checksums, then
   verify with:

   ```
   python scripts/download.py --case <case_id> --verify-only
   ```

5. Run `python scripts/validate_manifest.py` before opening a pull request.

## Style

- Fill in every field from the YAML templates; use `null` rather than omitting a key that
  doesn't apply to a given case.
- Keep case definitions and the evaluation protocol in sync — a held-out condition listed in
  `protocol/` should correspond to an actual case in `cases/`.

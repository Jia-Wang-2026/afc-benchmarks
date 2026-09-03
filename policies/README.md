# Trained policies

One directory per case, named after its `case_id` in `cases/`:

    policies/<case_id>/
        policy.pt          Trained weights (framework-specific; document the framework and
                            architecture in metadata.json)
        metadata.json       Training configuration: algorithm, hyperparameters, seed,
                             training compute, and the case/protocol version trained against

Weight files are excluded from Git by `.gitignore` (`*.pt`, `*.pth`, ...). Deposit them on
Zenodo alongside the flow-field data and record them in `data/MANIFEST.md`, or check a file
in directly only if it's small enough to keep the repository lightweight — decide per case.

`metadata.json` template:

```json
{
  "case_id": "",
  "algorithm": "",
  "framework": "",
  "hyperparameters": {},
  "seed": null,
  "training_compute": "",
  "protocol_id": "",
  "source_publication_doi": ""
}
```

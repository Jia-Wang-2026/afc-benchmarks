# afc-benchmarks

[![CI](https://github.com/Jia-Wang-2026/afc-benchmarks/actions/workflows/ci.yml/badge.svg)](https://github.com/Jia-Wang-2026/afc-benchmarks/actions/workflows/ci.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/data%20licence-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![License: Apache 2.0](https://img.shields.io/badge/code%20licence-Apache%202.0-blue.svg)](LICENSE-CODE)

**Benchmark configurations, flow-field data and trained policies for learned active flow control.**

Reproducible case definitions, reference flow-field data and trained control policies for
the bluff-body active-flow-control benchmarks used across the publications listed below:
circular, square and elliptical bodies with synthetic-jet actuation at Reynolds numbers
from 100 to 2000, together with the held-out conditions used to test generalisation across
Reynolds number, geometry and actuator placement.

Author: Wang Jia ([ORCID 0009-0008-2786-397X](https://orcid.org/0009-0008-2786-397X))

## Status

| Stage | Content | Status |
|---|---|---|
| v0.1 | Repository metadata, licences, citation and release plan | current |
| v1.0 | Case definitions, evaluation protocol, trained policies | in preparation |
| v1.0 | Reference flow-field data deposited on Zenodo with a DOI | in preparation |

Flow-field data are deposited on Zenodo rather than held in Git; this repository carries
the case definitions, the evaluation protocol and the download manifest.

## Scope

Each benchmark case fixes the geometry, domain and boundary conditions, the mesh and time
step, the actuator layout, the sensor layout, the reward or objective, and the episode
protocol - so that a control result is attributable to the controller rather than to an
undocumented difference in the environment.

The evaluation protocol specifies held-out Reynolds numbers and actuator layouts, matched
compute budgets across methods, and the reported quantities: drag reduction,
lift-fluctuation suppression, actuation energy and sample cost to a target performance.

## Intended layout at v1.0

```text
cases/             Case definitions (geometry, mesh, actuators, sensors, reward)
protocol/          Evaluation protocol and held-out condition sets
policies/          Trained policy weights per case
data/MANIFEST.md   Zenodo record identifiers and checksums for the flow-field data
scripts/           Download, verification and evaluation drivers
```

`cases/`, `protocol/` and `policies/` each carry a `README.md` describing their contents,
and `cases/TEMPLATE.yaml` / `protocol/TEMPLATE.yaml` define the schema a new entry must
fill in. `scripts/download.py` downloads and SHA-256-verifies the files listed in
`data/MANIFEST.md`; `scripts/validate_manifest.py` checks that the manifest and all YAML
case/protocol files are well-formed (run in CI on every push). See
[CONTRIBUTING.md](CONTRIBUTING.md) for the steps to add a case.

## Source publications

- Jia, W. & Xu, H. *Toward fully stabilized flow control using deep reinforcement learning*. Physics of Fluids 37(7), 073617 (2025). [doi:10.1063/5.0272178](https://doi.org/10.1063/5.0272178)
- Jia, W. & Xu, H. *Vortex shedding suppression in elliptical cylinder via reinforcement learning*. International Journal of Mechanical Sciences 302, 110517 (2025). [doi:10.1016/j.ijmecsci.2025.110517](https://doi.org/10.1016/j.ijmecsci.2025.110517)

## How to cite

If you use these benchmarks, please cite the source publication for the cases you use:

```bibtex
@article{jia2025toward,
  author  = {Jia, Wang and Xu, Hang},
  title   = {Toward fully stabilized flow control using deep reinforcement learning},
  journal = {Physics of Fluids},
  volume  = {37},
  number  = {7},
  pages   = {073617},
  year    = {2025},
  doi     = {10.1063/5.0272178}
}

@article{jia2025vortex,
  author  = {Jia, Wang and Xu, Hang},
  title   = {Vortex shedding suppression in elliptical cylinder via reinforcement learning},
  journal = {International Journal of Mechanical Sciences},
  volume  = {302},
  pages   = {110517},
  year    = {2025},
  doi     = {10.1016/j.ijmecsci.2025.110517}
}
```

Please additionally cite the data release once v1.0 carries a Zenodo DOI.
Machine-readable metadata is in [`CITATION.cff`](CITATION.cff); GitHub's *Cite this
repository* button exports it as BibTeX or APA. The full publication list, with open PDFs,
is at <https://jia-wang-2026.github.io/>.

## Licence

Data and case definitions: Creative Commons Attribution 4.0 International
(CC BY 4.0) - see [`LICENSE`](LICENSE).
Accompanying scripts: Apache License 2.0 - see [`LICENSE-CODE`](LICENSE-CODE).

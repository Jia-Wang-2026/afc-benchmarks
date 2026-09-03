# afc-benchmarks

**Benchmark configurations, flow-field data and trained policies for learned active flow control**

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

```
cases/             Case definitions (geometry, mesh, actuators, sensors, reward)
protocol/          Evaluation protocol and held-out condition sets
policies/          Trained policy weights per case
data/MANIFEST.md   Zenodo record identifiers and checksums for the flow-field data
scripts/           Download, verification and evaluation drivers
```

## Source publications

- Jia, W. & Xu, H. *Robust and adaptive deep reinforcement learning for enhancing flow control around a square cylinder with varying Reynolds numbers*. Physics of Fluids 36(5), 054103 (2025). [doi:10.1063/5.0207879](https://doi.org/10.1063/5.0207879)
- Jia, W. & Xu, H. *Deep reinforcement learning-based active flow control of an elliptical cylinder: transitioning from an elliptical cylinder to a circular cylinder and a flat plate*. Physics of Fluids 36(7), 074117 (2024). [doi:10.1063/5.0218408](https://doi.org/10.1063/5.0218408)
- Jia, W. & Xu, H. *Effect of synthetic jets actuator parameters on deep reinforcement learning-based flow control performance in a square cylinder*. Physics of Fluids 36(8), 084113 (2024) - Special Topic. [doi:10.1063/5.0220149](https://doi.org/10.1063/5.0220149)
- Jia, W. & Xu, H. *State-augmented deep reinforcement learning for active flow control around an elliptical cylinder*. International Journal of Heat and Fluid Flow 116, 109950 (2025). [doi:10.1016/j.ijheatfluidflow.2025.109950](https://doi.org/10.1016/j.ijheatfluidflow.2025.109950)
- Jia, W. & Xu, H. *Optimizing synthetic jet placement for control stability in increasing Reynolds number flows based on deep reinforcement learning*. International Communications in Heat and Mass Transfer 166, 109203 (2025). [doi:10.1016/j.icheatmasstransfer.2025.109203](https://doi.org/10.1016/j.icheatmasstransfer.2025.109203)
- Jia, W. & Xu, H. *Strategies for energy-efficient flow control leveraging deep reinforcement learning*. Engineering Applications of Artificial Intelligence 156, 111125 (2025). [doi:10.1016/j.engappai.2025.111125](https://doi.org/10.1016/j.engappai.2025.111125)
- Jia, W. & Xu, H. *Toward fully stabilized flow control using deep reinforcement learning*. Physics of Fluids 37(7), 073617 (2025). [doi:10.1063/5.0272178](https://doi.org/10.1063/5.0272178)
- Jia, W. & Xu, H. *Vortex shedding suppression in elliptical cylinder via reinforcement learning*. International Journal of Mechanical Sciences 302, 110517 (2025). [doi:10.1016/j.ijmecsci.2025.110517](https://doi.org/10.1016/j.ijmecsci.2025.110517)

## Licence

Data and case definitions: Creative Commons Attribution 4.0 International
(CC BY 4.0) - see [`LICENSE`](LICENSE).
Accompanying scripts: Apache License 2.0 - see [`LICENSE-CODE`](LICENSE-CODE).

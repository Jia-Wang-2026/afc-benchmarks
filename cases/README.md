# Case definitions

Each file in this directory fully specifies one benchmark case: geometry, domain and
boundary conditions, mesh and time step, actuator layout, sensor layout, reward/objective,
and episode protocol — see the repository [README](../README.md#scope) for why.

Copy `TEMPLATE.yaml`, name the copy after the case (e.g. `circular_re200.yaml`), and fill in
every field. A case is not complete until a result run against it is reproducible from the
file alone, with no undocumented dependency on code defaults.

Naming convention: `<body>_re<Reynolds number>[_<variant>].yaml`, e.g.
`square_re300.yaml`, `elliptical_re500_offset-actuator.yaml`.

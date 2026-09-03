# Evaluation protocol

Defines, per benchmark axis, what conditions are held out for testing generalisation, the
compute budget methods are matched against, and the quantities a submission must report
(drag reduction, lift-fluctuation suppression, actuation energy, sample cost to a target
performance) — see the repository [README](../README.md#scope).

Copy `TEMPLATE.yaml` and fill in every field. A protocol file may apply to one case or to a
group of cases sharing the same held-out axis; list them under `applies_to_cases`.

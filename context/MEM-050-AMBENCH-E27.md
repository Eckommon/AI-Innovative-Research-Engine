---
id: MEM-050-AMBENCH-E27
type: memory
created: 2026-08-23
source_of_truth: github
---

# MEM-050 — AMBENCH-E27 HOLD / AMBENCH-E27 HOLD

## Final / 최종
`HOLD_E27_SOURCE_OR_SCHEMA_INTEGRITY`.

Frozen primary/sensitivity summary files were immutable-source verified but contain no six physical plate identifiers, so the preregistered 3-vs-3 test was not run.

Source identities:
- overlap_depths_avg.csv: size 30012, SHA256 `e56c702fba658efd87e99e305ac61d7679d40a855cb331941679d8cdfb66373f`;
- depths_avg.csv: size 29879, SHA256 `8d65caae37318ce80392324b7766c0396c004169548054e7d5fce18e090d7a9d`.

Corrected schema is cp1252 and condition/location organized; all six T72/T82/T92/T102/T112/T122 identifier checks were false.

Permanent exposure state:
`NEW_E27_NUMERICAL_OUTCOME_BLIND = VIOLATED_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`.
Scientific design was frozen before the incident; no plate mapping/condition comparison/statistical test was performed from emitted values.

Decision `DEC-057`: close E27 without redesign. Next eligible work is separate F28 plate-specific P1 source/schema qualification.

v2.1 continuity overlay remains active under `DEC-055`; no AGENTS bootstrap or new Skill/MCP/Plugin is required.

Incremental monetary cost: 0 USD.
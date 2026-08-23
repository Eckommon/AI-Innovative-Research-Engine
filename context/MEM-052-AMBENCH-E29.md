---
id: MEM-052-AMBENCH-E29
type: memory
state: ACTIVE
created: 2026-08-23
source_of_truth: github
research: AMBENCH-E29
---

# MEM-052 — AMBENCH-E29 / E29

## Final / 최종
`PASS_E29_STRONG_DIRECTIONAL_EFFECT`

## Frozen design / 고정 설계
- 0.75 ms: T72/T82/T92
- 5.0 ms: T102/T112/T122
- independent unit = physical plate
- P1 only
- overlap-depth reconstruction from plate-specific `overlap_depth_y`, unique P1 substrate-surface Y reference, and authoritative `0.174 µm/px` scale
- >=41/45 valid tracks required per plate
- exact one-sided 20-allocation permutation
- rank-biserial strong threshold >=7/9
- common-valid sensitivity >=36/45 required for strong PASS

## Result / 결과
- valid tracks: 44/45 for every plate
- T72: 112.674229909 µm
- T82: 115.201840909 µm
- T92: 114.859120227 µm
- T102: 87.679513500 µm
- T112: 84.165251318 µm
- T122: 83.641278000 µm
- `Delta_primary = 29.083049409 µm`
- exact one-sided permutation `p = 0.05`
- plate-level rank-biserial `r_rb = 1.0` (9 wins / 0 losses / 0 ties)
- common-valid track count = 44
- `Delta_common = 29.083049409 µm`

## Integrity / 무결성
Two implementation-only amendments were recorded before successful numerical execution:
- AMENDMENT-01: symbolic HOLD diagnostics only;
- AMENDMENT-02: narrow README selector to F28-verified exact root `4103_ReadMe.txt` after broad selector returned `README_NOT_UNIQUE`.

Neither amendment changed endpoint, groups, formula, coverage, direction, statistic or final gates.

Permanent disclosure:
`NEW_E29_NUMERICAL_OUTCOME_BLIND = NO__INHERITED_E27_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`.

No P2/P3 rescue, imputation, sign flip, endpoint switch, feature search or model escalation occurred.

## Interpretation / 해석
Strong preregistered directional internal signal, but only physical-plate `n=3 vs n=3`; 45 tracks are nested within plates. Not broad causal proof or population-level generalization.

## Next / 다음
Per `DEC-061`, separately preregister P2/P3 spatial robustness/falsification (`AMBENCH-E30`) before inspecting their plate-specific numerical values. Physical plate remains the independent unit; P2/P3 are nested spatial repeats.

## Capability / Portfolio
Workflow remains `SHARED-INTERNAL-CANDIDATE`; no new Skill/MCP/Plugin. Shared paid resources are never assumed without canonical ledger evidence.

Incremental monetary cost: `0 USD`.

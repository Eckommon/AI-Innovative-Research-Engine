---
id: US-MINERAL-E01-RESULT
type: controlled-cross-agency-experiment-result
created: 2026-09-04
issue: 75
final_gate: PASS_E01_REPLICATED_DUAL_TRADE_VALUE_CONCENTRATION
stage_a_pass: true
stage_b_pass: true
incremental_monetary_cost_usd: 0
---

# US-MINERAL-E01 Result — 2023 Critical-Mineral Source × Unlading-District Dual Trade-Value Concentration

## Final gate / 최종 판정

**`PASS_E01_REPLICATED_DUAL_TRADE_VALUE_CONCENTRATION`**

## Frozen design / 고정 설계

- Universe: all eight prospectively F01-qualified minerals.
- Period: all 12 months of 2023.
- Weight: Census `gen_val_mo` (General Imports, Total Value).
- Axes: country of origin and district of unlading.
- Per-mineral dual floor: `D = min(H_country, H_unlad)`.
- Materiality heuristic: `D >= 0.25`.
- Replication PASS: at least two of eight minerals cross the dual threshold.

## Integrity / 무결성

- Stage A: **PASS**
- Stage B numerical integrity: **PASS**
- Raw trade rows are not persisted in this result; source ZIP/member hashes are in `SOURCE_MANIFEST.md`.

## Primary and frozen secondary results / 1차 및 고정 2차 결과

| Mineral | H_country | H_unlad | D=min | Dual ≥0.25? | Top country code/share | Top unlading district/share | H_entry | H_joint | #countries | #unlading districts |
|---|---:|---:|---:|---|---|---|---:|---:|---:|---:|
| Antimony | 0.283540 | 0.341889 | 0.283540 | YES | `5700` / 0.504113 | `13` / 0.559478 | 0.416755 | 0.140020 | 21 | 27 |
| Barite | 0.197461 | 0.343387 | 0.197461 | NO | `5330` / 0.341311 | `20` / 0.407464 | 0.300308 | 0.105658 | 17 | 20 |
| Beryllium | 0.389639 | 0.365803 | 0.365803 | YES | `5880` / 0.542692 | `27` / 0.546001 | 0.340681 | 0.357748 | 20 | 17 |
| Palladium | 0.274073 | 0.963776 | 0.274073 | YES | `4621` / 0.364044 | `10` / 0.981689 | 0.971375 | 0.272909 | 20 | 19 |
| Phosphate | 0.144551 | 0.669242 | 0.144551 | NO | `5170` / 0.293284 | `20` / 0.814324 | 0.617609 | 0.123523 | 39 | 34 |
| Potash | 0.724250 | 0.258739 | 0.258739 | YES | `1220` / 0.846361 | `36` / 0.365848 | 0.258737 | 0.254621 | 34 | 31 |
| Rhodium | 0.323716 | 0.981239 | 0.323716 | YES | `7910` / 0.444610 | `10` / 0.990557 | 0.981209 | 0.320573 | 18 | 14 |
| Tellurium | 0.570822 | 0.151497 | 0.151497 | NO | `1220` / 0.735021 | `07` / 0.178740 | 0.152207 | 0.125118 | 6 | 11 |

- Replicated dual-threshold count `K`: **5 / 8**
- Spearman rank association `H_country` vs `H_unlad`: **-0.523810**

## Interpretation / 해석

At least two prospectively selected minerals show material published general-import trade-value concentration on both the foreign-source and U.S. unlading-district axes under the frozen project heuristic.

## Claim boundary / 주장 경계

This result concerns **published mapped general-import trade-value concentration** only. It does not establish physical mineral-content/tonnage concentration, causal disruption probability, inventory adequacy, transaction-level port routing, or policy/investment superiority.

## Stop rule / 중단 규칙

No same-branch retuning, mineral substitution, alternate year, alternate threshold or HS6-port rescue is authorized after this outcome exposure. Return to mandatory mission-level review.

Incremental monetary cost remained **0 USD**.

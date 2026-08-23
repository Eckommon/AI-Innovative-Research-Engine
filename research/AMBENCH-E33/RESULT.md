---
id: AMBENCH-E33-RESULT
type: confirmatory-result
state: COMPLETED_NUMERICAL_EXECUTION
created: 2026-08-23
source_of_truth: github-actions
publication_level_outcomes_preexposed: true
raw_workbook_cells_committed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-E33 Result — Equivalent-Length Rapid-Turnaround History Falsification
# AMBENCH-E33 결과 — 동등 길이 Rapid-Turnaround History 반증 실험

## Execution integrity / 실행 무결성
- dataset: `mds2-3662`
- NERDm version: `1.0.1`
- Measurements.xlsx SHA-256 expected: `9e21a77f0c526aa0a913a3f14e2bba7b36640b0fd319febcf8ebfdc9dd5d0edf`
- Measurements.xlsx SHA-256 local: `9e21a77f0c526aa0a913a3f14e2bba7b36640b0fd319febcf8ebfdc9dd5d0edf`
- checksum_match: `True`
- Operator 1 track map: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]`
- Operator 2 track map: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]`
- No raw workbook measurement cells are committed; only preregistered aggregates/statistics are persisted.
- Publication-level outcomes had already been exposed after preregistration per `AMENDMENT-01`; this execution is confirmatory/reanalysis.

## Frozen primary — width / 고정 1차 — width
- valid_blocks: `18`
- Spearman_rho: `1`
- permutation_n: `100000`
- permutation_seed: `20260823`
- extreme_count: `0`
- add_one_two_sided_p: `9.999900001e-06`
- median_geometry_matched_diff_um: `41.411`
- mean_geometry_matched_diff_um: `29.3086388889`
- diff_sign_counts: `positive=10; negative=8; zero=0`
- Operator1: `n=18; rho=0.985524341588; sign=1`
- Operator2: `n=18; rho=1; sign=1`
- **primary_gate: `PASS_E33_GEOMETRY_MATCHED_HISTORY_ASSOCIATION`**

### Primary aggregate blocks / 1차 집계 block
| C track | D reverse track | h | C median width | D median width | C-D | C valid repeats | D valid repeats |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 18 | -17 | 148.337500000 | 394.012500000 | -245.675000000 | 3 | 3 |
| 2 | 17 | -15 | 185.523000000 | 386.996500000 | -201.473500000 | 3 | 3 |
| 3 | 16 | -13 | 227.421000000 | 391.356000000 | -163.935000000 | 3 | 3 |
| 4 | 15 | -11 | 264.709000000 | 382.156500000 | -117.447500000 | 3 | 3 |
| 5 | 14 | -9 | 296.963000000 | 380.156500000 | -83.193500000 | 3 | 3 |
| 6 | 13 | -7 | 322.394500000 | 365.868500000 | -43.474000000 | 3 | 3 |
| 7 | 12 | -5 | 352.648500000 | 380.190500000 | -27.542000000 | 3 | 3 |
| 8 | 11 | -3 | 380.580500000 | 405.496500000 | -24.916000000 | 3 | 3 |
| 9 | 10 | -1 | 404.012500000 | 370.512500000 | 33.500000000 | 3 | 3 |
| 10 | 9 | 1 | 403.690500000 | 354.368500000 | 49.322000000 | 3 | 3 |
| 11 | 8 | 3 | 422.444500000 | 333.614500000 | 88.830000000 | 3 | 3 |
| 12 | 7 | 5 | 420.334500000 | 303.504500000 | 116.830000000 | 3 | 3 |
| 13 | 6 | 7 | 426.944500000 | 305.632500000 | 121.312000000 | 3 | 3 |
| 14 | 5 | 9 | 429.266500000 | 305.671500000 | 123.595000000 | 3 | 3 |
| 15 | 4 | 11 | 420.122500000 | 248.065000000 | 172.057500000 | 3 | 3 |
| 16 | 3 | 13 | 431.800500000 | 229.189000000 | 202.611500000 | 3 | 3 |
| 17 | 2 | 15 | 429.444500000 | 185.557500000 | 243.887000000 | 3 | 3 |
| 18 | 1 | 17 | 429.232000000 | 145.965000000 | 283.267000000 | 3 | 3 |

## Secondary sensitivity — area / 2차 sensitivity — area
- valid_blocks: `18`
- Spearman_rho: `0.997936016512`
- add_one_two_sided_p: `9.999900001e-06`
- median_geometry_matched_diff_um2: `14789.14425`
- mean_geometry_matched_diff_um2: `5327.24411111`
- diff_sign_counts: `positive=11; negative=7; zero=0`
- Operator1: `n=18; rho=0.985552115583; sign=1`
- Operator2: `n=18; rho=0.995872033024; sign=1`
- **secondary_interpretation: `CROSS_MEASURAND_STRENGTHENING`**

## Final / 최종
- primary: **`PASS_E33_GEOMETRY_MATCHED_HISTORY_ASSOCIATION`**
- secondary: **`CROSS_MEASURAND_STRENGTHENING`**
- Claim scope: equivalent programmed-track-length / different prior-scan-history association within this IN625 beam-on-plate experiment only; not same-XY matching and not AMB2025-07 turnaround-time replication.
- No post-hoc exclusion, trimming, imputation, track subset search, endpoint switch, model escalation, or paid computation was used.


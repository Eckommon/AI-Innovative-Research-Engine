---
id: JP-PORT-E01-RESULT
type: preregistered-primary-panel-experiment-result
created: 2026-09-04
final_gate: PASS_E01_NEGATIVE_EXTREME_WIND_CARGO_ASSOCIATION
stage_a_gate: PASS_E01_STAGE_A_SOURCE_IDENTITY_QUALITY
relationship_outcome_computed: true
incremental_monetary_cost_usd: 0
---

# JP-PORT-E01 Result

## Final gate: **PASS_E01_NEGATIVE_EXTREME_WIND_CARGO_ASSOCIATION**

## Frozen primary model

log1p(monthly total maritime cargo) = beta × monthly maximum of quality-8 daily maximum wind + port FE + year-month FE.

Inference: one-way CR1 clustered by frozen JMA history station ID; t critical value uses G-1 degrees of freedom.

## Primary numerical result

- N observations: **10165**
- JMA station clusters G: **126**
- fitted design columns/rank K: **215**
- beta per +1 m/s: **-0.00629297514**
- CR1 station-clustered SE: **0.00219436119**
- t statistic: **-2.86779367**
- degrees of freedom: **125**
- two-sided p-value: **0.00485312733**
- 95% CI: **[-0.0106358883, -0.001950062]**
- descriptive model-implied change for +5 m/s: **-3.0975%**

The +5 m/s translation is descriptive only. It is not a causal estimate or an additional PASS threshold.

## Realized frozen-panel integrity

- Stage-A panel-key SHA-256: **7831034401647ef1602ea8db6f6445206df4b3954ef3bae010dd8e2cd3587486**
- Stage-A frozen keys: **10165**
- realized Stage-B rows: **10165**
- realized ports: **143**
- realized year-months: **72**
- realized station clusters: **126**
- keys dropped for re-downloaded weather incompleteness: **0**
- keys dropped for missing/non-numeric MLIT cargo: **0**

## Stage-B JMA raw-response manifest

- session-root SHA-256: **78e5d9e76d1e3dfb240cda4d837d9a870a8cbc3ae58a8b8ff20b4bee842ad2f9**
- element: **302 最大風速 only**
- period: **2019-01-01..2024-12-31**
- requests: **16**

| Batch | History station IDs | obsdl IDs | Bytes | SHA-256 | Rows | Attempt |
|---:|---|---|---:|---|---:|---:|
| 1 | 11016 13277 16091 17112 17341 18273 19432 20751 | s47401 s47406 s47411 s47435 s47409 s47420 s47418 s47440 | 300283 | 2390cf859c626a3047f4ef29743b4e73265d10852fa10cffafc0124739fe1d45 | 2198 | 1 |
| 2 | 21187 21323 23232 31121 31312 31336 31602 32111 | s47424 s47423 s47430 a1122 s47575 a1027 s47581 a0183 | 299716 | b5eafb54fec53a8ccef0cf35ec7b9c41668e00d88c61e78ce543841b2f20090f | 2198 | 1 |
| 3 | 32286 32402 33146 33472 33751 33877 34331 35052 | a1036 s47582 a0209 s47585 a0233 s47512 a1030 s47587 | 298538 | cc471b599538164c5188313f847aca989dd25e9065c00b02a08e9b1daa2d2135 | 2198 | 1 |
| 4 | 36151 36846 40201 44166 45212 45282 46106 46211 | a0285 s47598 s47629 a0371 s47682 a0382 s47670 a0392 | 299695 | 691fcff88f11476bfa0a4f5bd3845c7eb1afd553556e2643887633e3976e5944 | 2198 | 1 |
| 5 | 50196 50206 50477 50551 51216 51311 51331 53061 | a0442 s47657 a1601 s47655 a1638 a0984 a0470 s47684 | 298530 | d02f8bef6ebea00e656480f724ac53f899975d24873280794f42e985601484bd | 2198 | 1 |
| 6 | 53133 53296 53378 54166 54236 54541 54711 56146 | s47651 a1258 s47663 a0518 a1469 a0532 a0539 a0565 | 300921 | 9718bb69e767a10245e9a1d5734832ae45f544915340fd63a4c5a12f193a21f7 | 2198 | 1 |
| 7 | 56227 57001 57248 61076 61111 62091 62101 62131 | s47605 a1071 s47631 a0589 s47750 a1062 a1471 a0606 | 300886 | 1f2743d0cd360285591fcfb00b0c80a93a8c80cce3402f88853fa97b93ade708 | 2198 | 1 |
| 8 | 63383 63491 63496 63518 65042 65201 65276 66408 | s47769 a0624 a0625 s47770 s47777 a1485 a0649 s47768 | 299795 | 518fbd6850771de7ecec18dfef1352a5acde2aa926eb7faf1f3a67df4cd1aa53 | 2198 | 1 |
| 9 | 66421 66446 66481 66501 67401 67437 67461 67496 | a0668 a0669 a0919 a0670 s47767 s47765 a0686 a0688 | 293680 | 875078000b4a3a4d602636aa91ee9f373de1907ce7855b31d420d3a9b60a7bb0 | 2198 | 1 |
| 10 | 67511 68376 68431 69006 69052 71106 71231 72111 | s47766 s47755 a1321 s47742 a1519 s47895 a1242 s47890 | 296449 | e7928cc81fbec9a4f7417798e1ec14bf640b2ac11fb51aa46ae7ee0231798fc6 | 2198 | 1 |
| 11 | 73076 73126 73141 73151 73168 73442 74188 74311 | a1077 a0958 a0734 a0735 a1521 s47892 a1476 a0756 | 299038 | 76e45d68551ac8fff4bb908613c6e4bf72b0b3d367c94dfd22ddabaf44e7d2d9 | 2198 | 1 |
| 12 | 74447 81321 81371 81386 81436 81481 82068 82182 | s47897 a0940 a0775 a0776 a0778 a0942 a1590 s47807 | 297150 | 4f72ef75c6861b5d806b439341727537169453284d8baee784a027f1269848b3 | 2198 | 1 |
| 13 | 83051 83216 83401 84072 84121 84183 84266 84496 | a0794 s47815 a0808 s47800 a1144 a0814 s47812 s47817 | 297971 | d0fcbcbc514f9b4f3fbff1652b92e59c8e3539431d38ea50e496c04b4bb77163 | 2198 | 1 |
| 14 | 84523 85033 85116 86141 86216 86271 86451 87181 | a0962 a1610 a1075 s47819 a1081 a0843 a0924 a0857 | 294867 | ed879ce9b46d842f14e0545105db5a0b3801cdfa9eb88859f501ea032e709867 | 2198 | 1 |
| 15 | 87412 87492 88166 88317 88406 88432 88612 88821 | a1481 s47835 a0881 s47827 a0936 a0890 s47837 a1520 | 298758 | 6f6f27299c210be9f1830b780b8a1987e0b2595641784f5b74cdf7803e3e1423 | 2198 | 1 |
| 16 | 91107 91166 91197 91241 93041 94081 | s47940 a1596 s47936 a0909 s47927 s47918 | 230615 | 6df14a67c2972c3a546652fc226beac6cbc0c3c3037c7adc152d5996a0afce9a | 2198 | 1 |

## MLIT source manifest

| Year | Bytes | SHA-256 | Monthly total columns |
|---:|---:|---|---:|
| 2019 | 1056222 | c9b52effc6939080290f9cd2d1eaad894769d5a0af8f5c268bd18dce5218bebf | 12 |
| 2020 | 1048653 | 9ee04b6f968fa475f004c7e397cb74303d6bd3498972ef040c12f3414b1fbe46 | 12 |
| 2021 | 1045142 | de510a1510a178a9dc3d3d0dce9ed5ea8da165929ccb0d381458f2005571dd68 | 12 |
| 2022 | 1045714 | f5e1402c0fba0afa2b8a74f8e463638c9dc6ef141ed9c08355f39125b6fa61c4 | 12 |
| 2023 | 1044224 | 4670b2ac230cae5b2bdc6a50ae03c72001137ca24b9c023a6f90e28e77156d04 | 12 |
| 2024 | 1056705 | 830c2173b19f9ea106596e043730bd93616dafe93ef0c6a385d633335cef0200 | 12 |

MLIT parser followed the outcome-blind schema adjudication in `research/JP-PORT-E01/MLIT_SCHEMA_ADJUDICATION.md`; 2019 legacy layout and 2020–2024 current layout were distinguished by header identity, not cargo-weather outcomes.

## Runtime

- Python: 3.12.3
- platform: Linux-6.17.0-1022-azure-x86_64-with-glibc2.39
- numpy: 2.5.2
- scipy: 1.18.1
- openpyxl: 3.1.5
- primary-result CSV SHA-256: **c693096d4c0bd7c45afc285cbc85f7dd643cb8159d9c2006662de79e1b5cf048**
- primary-result file: `research/JP-PORT-E01/PRIMARY_RESULT.csv`

## Interpretation boundary

This first experiment tests one preregistered association only.

A PASS would mean the frozen panel shows a statistically detectable negative association under the frozen model. A NO means the preregistered negative-association gate was not met.

Neither gate establishes causality, terminal-level operational disruption, physical tonnage loss, port resilience ranking, policy superiority or investment superiority.

No alternate weather variable, threshold, lag/lead, station remap or port subset was searched to rescue the result.

Incremental monetary cost remained **0 USD**.

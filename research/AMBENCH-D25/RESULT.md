---
id: AMBENCH-D25-RESULT
type: diagnostic-result
state: COMPLETED_BLOCK_DOMINANT_HIERARCHICAL_STRUCTURE
created: 2026-08-23
updated: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-D25/README.md
  - research/AMBENCH-D25/EXECUTION_RESULT.md
  - Issue #43
---

# AMBENCH-D25 Result — Registered X4 Fixed-Effect Dominance / Variance Structure
# AMBENCH-D25 결과 — Registered X4 고정효과 지배 / 분산구조

**Frozen final gate / 고정 최종 판정:** **`D25_BLOCK_DOMINANT_HIERARCHICAL_STRUCTURE`**

## 1. Executive result / 핵심 결과

**KO:** E24와 동일한 `melt_pool_area_t100_mm2` → `xct_voxel_mean5` representation과 동일 집계/eligibility를 재현했다. E24의 36 part×block units, 9 blocks, excluded Block 1, standardized beta `0.015305236`, predictor partial R² `0.019321313`이 frozen tolerance 내에서 재현되어 diagnostic integrity가 PASS했다. 그 뒤 분산구조를 분해한 결과 XCT outcome은 압도적으로 25-layer block/build-progression 구조에 의해 설명됐다. `R2_y_block_only=0.998820`, `R2_y_part_block=0.999421`, `partial_R2_y_block_given_part=0.999421`이었다. E24 predictor가 추가로 설명한 residual variation은 `1.9321%`뿐이었다.

**EN:** D25 exactly reproduced the E24 `melt_pool_area_t100_mm2` → `xct_voxel_mean5` representation, aggregation and eligibility. The 36 part×block units, 9 included blocks, excluded Block 1, standardized beta `0.015305236`, and predictor partial R² `0.019321313` reproduced within the frozen tolerance. Variance decomposition then showed that XCT outcome variation is overwhelmingly structured by fixed 25-layer block/build progression: `R2_y_block_only=0.998820`, `R2_y_part_block=0.999421`, and `partial_R2_y_block_given_part=0.999421`. The E24 melt-pool predictor explains only `1.9321%` of the remaining part+block-adjusted variation.

## 2. Reproduction integrity / 재현 무결성
- source SHA-256 ×4: exact PASS;
- eligible t100 layers: Part1 232, Part2 231, Part3 230, Part4 230;
- eligible part×block units: 36/40;
- included blocks: 9/10;
- excluded blocks: `[1]`;
- reproduced E24 standardized beta: `0.015305236`;
- reproduced E24 predictor partial R²: `0.019321313`;
- result: `PASS`.

No D25 interpretation is based on a changed representation.

## 3. XCT outcome variance structure / XCT outcome 분산구조

| Diagnostic | Value |
|---|---:|
| Part-only R² | 0.000602 |
| Block-only R² | 0.998820 |
| Part+block R² | 0.999421 |
| Block \| part partial R² | 0.999421 |
| Part \| block partial R² | 0.509735 |
| Residual fraction after part+block | 0.000579 |
| E24 predictor \| part+block partial R² | 0.019321 |

Interpretation:
- block alone accounts for virtually all total aggregate XCT variation;
- part alone accounts for almost none of total XCT variation (`R²≈0.0006`);
- after block has removed nearly all total variation, part explains about half of the **tiny remainder**. Therefore `partial_R2_y_part_given_block=0.509735` must not be misread as part explaining 51% of total XCT variance;
- the remaining total variance after part+block is only `0.0579%` of total variance;
- E24's melt-pool predictor acts only inside this very small residual surface.

## 4. Melt-pool predictor structure / Melt-pool predictor 구조

| Diagnostic | Value |
|---|---:|
| Part-only R² | 0.747172 |
| Block-only R² | 0.205094 |
| Part+block R² | 0.952265 |
| Block \| part partial R² | 0.811197 |
| Part \| block partial R² | 0.939949 |
| Residual fraction after part+block | 0.047735 |

Thus the predictor is itself highly structured by part/location and build progression. Only about `4.77%` of predictor variance remains after part+block fixed effects. This makes naive pooled process↔XCT interpretation especially unsafe.

## 5. Sign decomposition / 부호 분해
Frozen slopes:
- pooled: `-0.278047`;
- part-adjusted: `-1.026589`;
- block-adjusted: `-0.022349`;
- part+block-adjusted: `+0.015305`.

Frozen diagnostics:
- `STRUCTURAL_SIGN_REVERSAL = YES`;
- `BLOCK_REMOVAL_EXPLAINS_REVERSAL = NO`.

The negative association is not explained by block removal alone because the block-adjusted slope remains slightly negative. The positive E24 slope appears only after **both** part and block structure are removed, and its magnitude is very small. D25 therefore does not authorize a causal or mechanistic positive relationship.

Part-specific x↔y Spearman diagnostics remain negative in all four parts:
- Part1 `-0.460255`;
- Part2 `-0.268917`;
- Part3 `-0.483333`;
- Part4 `-0.694567`.

Block-index diagnostics:
- predictor (`x`) declines strongly with block in all parts (`rho≈-0.64` to `-0.84`);
- outcome (`y`) has the same weak positive rank relation to block in each part (`rho=0.166667`).

These diagnostics reinforce that the aggregate variables occupy strong but different hierarchical trajectories; the tiny positive fully adjusted slope is a residual estimand, not the dominant build-level relationship.

## 6. Frozen gate application / 고정 gate 적용
`D25_BLOCK_DOMINANT_HIERARCHICAL_STRUCTURE` requires:
- `R2_y_part_block >= 0.90`: PASS (`0.999421`);
- `partial_R2_y_block_given_part >= 0.80`: PASS (`0.999421`);
- block partial R² exceeds part partial R² by >=0.10: PASS (`0.489686`).

Final: **PASS for `D25_BLOCK_DOMINANT_HIERARCHICAL_STRUCTURE`**.

## 7. Scientific consequence / 과학적 후속
Supported:
- the registered X4 XCT aggregate outcome is overwhelmingly dominated by block/build-progression structure;
- the melt-pool aggregate predictor is itself strongly structured by part and block;
- the E24 process↔XCT residual association is statistically detectable but materially small and is not the dominant source of variation;
- pooled or part-only association can reverse sign relative to the fully adjusted residual estimand.

Not supported:
- causal melt-pool → XCT interpretation;
- upgrading E24 to a material association;
- using more features or higher-capacity models on the same representation to rescue the result;
- treating block, layer or row multiplicity as independent replication.

## 8. Branch decision / branch 의사결정
Per the preregistered decision rule, the same registered-X4 representation should **not be escalated** by feature fishing or model-capacity expansion. E24 + D25 together constitute informative negative evidence for a material local melt-pool-area → XCT-voxel association on this aggregate representation.

The next highest-leverage route is an **independent-condition / independently varied dataset or experiment qualification**, where process variation is not primarily a deterministic part/block proxy and where the target structural outcome has interpretable independent variation.

## 9. Exposure and cost / 사전노출 및 비용
Inherited disclosure remains `NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED` from F22. D25 introduced no feature selection or endpoint switching.

Incremental monetary cost: `0 USD`. Public standard GitHub-hosted runner only; raw NIST bytes remained transient and were not committed, cached or uploaded as artifacts.
# AMBENCH-001 Results / 결과

## EXP-AMB-001A — Aggregate Calibration Feasibility / 집계수준 보정 Feasibility

**Evidence class / 증거 등급:** `DERIVED`  
**Date / 계산일:** 2026-08-21

## 1. Leave-One-Condition-Out RMSE / Leave-One-Condition-Out RMSE

| Target / 대상 | Model / 모델 | RMSE [µm] | Interpretation / 해석 |
|---|---|---:|---|
| Depth / 깊이 | `VEDσ` only | **19.32** | strongest simple depth probe / 단순 depth probe 중 최상 |
| Depth / 깊이 | process-only: power + speed + spot | **19.71** | main process baseline / 주 process 기준선 |
| Depth / 깊이 | best single thermal: `TTAM` | **38.96** | no gain / 개선 없음 |
| Width / 폭 | `VEDσ` only | **28.36** | weak diagnostic baseline / 약한 진단 기준선 |
| Width / 폭 | process-only: power + speed + spot | **14.63** | main process baseline / 주 process 기준선 |
| Width / 폭 | best single thermal: `TLCR` | **13.71** | modest gain / 소폭 개선 |

## 2. Threshold Test / 기준 검정

`TLCR` width RMSE improvement versus main process-only baseline: / `TLCR`의 width RMSE 개선폭:

`(14.63 - 13.71) / 14.63 ≈ 6.3%`

This is below the predefined **10%** material-improvement threshold. / 사전 정의한 실질 개선 기준 **10%** 미만이다.

Against the weaker `VEDσ`-only width baseline, the improvement is ≈51.6%, demonstrating why baseline selection must be explicit and cannot be chosen opportunistically after seeing results.  
더 약한 `VEDσ`-only width 기준선 대비로는 약 51.6% 개선이지만, 이는 결과를 본 뒤 유리한 기준선을 선택하면 안 되는 이유를 보여준다.

## 3. Decision / 판단

### H-AMB-001A
**Aggregate test result / 집계 검증:** `NO_MATERIAL_GAIN` against the main predefined process-only baseline. / 주 사전정의 process-only 기준선 대비 `NO_MATERIAL_GAIN`.

### Broader multimodal claim / broader 멀티모달 주장
**State / 상태:** `INCONCLUSIVE`.

Reason / 이유:
- only seven aggregate conditions / 집계 조건 7개뿐;
- thermography has three repeats/case while optical geometry reports six measurements/case / 열화상 3회와 geometry 6회 측정 구조;
- replicate-level one-to-one pairing not yet established / 반복수준 1:1 pairing 미확인;
- raw thermal spatiotemporal information is compressed into a few summary metrics / raw 열이력 정보가 소수 요약지표로 압축됨.

## 4. Calibration Outcome / 보정 성과

**Validated workflow findings / workflow 차원의 검증 결과:**  
- authoritative source discovery works / 공식 소스 탐색 가능;
- multimodal dataset family discovery works / 멀티모달 데이터 계열 탐색 가능;
- aggregate join is reproducible through shared case IDs / 공통 case ID로 집계 조인 재현 가능;
- benchmark outcomes can calibrate IPS and hypothesis gates / benchmark 결과로 IPS·가설 gate 보정 가능;
- negative preliminary findings can be preserved without downgrading data quality / 부정적 예비결과와 데이터 품질을 분리할 수 있음.

## 5. Methodological Consequence / 방법론 반영

The engine shall explicitly track `aggregation_level`, `replicate_count`, `replicate_alignment`, and `measurement_uncertainty`. Dataset quality and hypothesis performance remain separate dimensions.  
엔진은 `aggregation_level`, `replicate_count`, `replicate_alignment`, `measurement_uncertainty`를 명시적으로 추적한다. 데이터셋 품질과 개별 가설 성능은 서로 다른 평가축으로 유지한다.

## 6. Next Research Extension / 향후 확장

`H-AMB-001B` should test raw spatiotemporal thermography + aligned geometry only after track/cross-section provenance is mapped. This is not required to close the Wave 0 calibration gate.  
`H-AMB-001B`는 track/단면 provenance mapping 후 raw spatiotemporal thermography + geometry 조합으로 검증한다. 이는 Wave 0 calibration 종료의 필수조건은 아니다.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.

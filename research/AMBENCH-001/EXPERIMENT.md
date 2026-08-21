# AMBENCH-001 Experiment / 실험 설계

## EXP-AMB-001A — Aggregate Calibration Feasibility / 집계수준 보정 Feasibility

**State / 상태:** `COMPLETED_PRELIMINARY`  
**Purpose / 목적:** validate engine workflow, not claim production-grade ML performance / production-grade ML 성능 주장이 아니라 엔진 workflow 검증.

## 1. Data / 데이터

Seven shared `AMB2022-03` process cases joined from NIST-published result tables. / NIST 공개 결과표에서 공통 `AMB2022-03` 7개 process case를 조인.

Inputs / 입력:
- `power`
- `scan_speed`
- `spot_size`
- `VEDσ`
- `TTAM`
- `TSCR`
- `TLCR`
- `TTCR`

Targets / 대상:
- mean melt-pool depth [µm] / 평균 melt-pool 깊이
- mean melt-pool width [µm] / 평균 melt-pool 폭

## 2. Evaluation Design / 평가 설계

- **Split / 분할:** leave-one-condition-out across seven cases / 7개 case leave-one-condition-out.
- **Model class / 모델:** ordinary linear regression / 단순 선형회귀.
- **Reason / 이유:** n=7 aggregate observations are too small to justify high-capacity ML; a simple model is intentionally used as a calibration probe. / 7개 집계관측으로 고용량 ML을 정당화할 수 없어 calibration probe로 단순 모델 사용.
- **Metric / 지표:** RMSE [µm].
- **Material-gain threshold / 실질 개선기준:** ≥10% reduction in RMSE versus process-only baseline.

## 3. Baselines / 기준선

### Main baseline / 주 기준선
`power + scan_speed + spot_size` → geometry.

### Diagnostic baseline / 진단 기준선
`VEDσ` → geometry.

### Thermal probes / 열지표 probe
One thermal metric at a time (`TTAM`, `TSCR`, `TLCR`, `TTCR`) to avoid multivariate overfitting. / 다변량 과적합을 줄이기 위해 열지표를 하나씩 평가.

## 4. Leakage Controls / 누수 통제

The split is by process case, so the held-out case is not used for fitting. However, published thermal and geometry values are case-level aggregates; this experiment therefore cannot measure track-level generalization.  
process case 단위로 holdout하여 해당 case는 fitting에 사용하지 않는다. 다만 공개 열·형상 값이 case 집계값이므로 track-level 일반화 성능은 측정할 수 없다.

## 5. Predefined Decision / 사전 판단규칙

- ≥10% RMSE improvement over process-only baseline: `PASS_PRELIMINARY`.
- <10% improvement: `NO_MATERIAL_GAIN` for this aggregate test.
- If sample structure or alignment prevents a defensible inference: broader multimodal claim remains `INCONCLUSIVE`.

process-only 대비 RMSE 10% 이상 개선이면 `PASS_PRELIMINARY`, 미만이면 이 집계 검증에서는 `NO_MATERIAL_GAIN`. 표본 구조·정렬로 broader inference가 어려우면 전체 multimodal 가설은 `INCONCLUSIVE`.

## 6. Reproducibility Formula / 재현 계산

For each target and predictor set: / target과 predictor set별:

1. hold out one of seven cases / 7개 중 1개 case holdout;
2. fit ordinary least squares on remaining six / 나머지 6개로 OLS fitting;
3. predict held-out case / holdout 예측;
4. repeat all seven cases / 7회 반복;
5. calculate RMSE across seven held-out predictions / 7개 holdout prediction RMSE 계산.

## 7. Limitation / 한계

This preliminary experiment uses NIST-published aggregate tables, not raw thermographic frames or individually paired optical measurements. It is valid as a workflow/calibration test, not as a final scientific or production ML result.  
본 예비 실험은 raw thermography frame이나 개별 pairing된 optical measurement가 아니라 NIST 공개 집계표를 사용한다. 따라서 workflow/calibration 검증으로는 유효하지만 최종 과학적·production ML 결과로 해석하지 않는다.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.

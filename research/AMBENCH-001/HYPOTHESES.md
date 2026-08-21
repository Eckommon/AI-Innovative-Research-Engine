# AMBENCH-001 Hypotheses / 가설

## H-AMB-001A — Aggregate Thermal-Gain Hypothesis / 집계 열이력 추가가치 가설

**State / 상태:** `INCONCLUSIVE` after preliminary feasibility / 예비 feasibility 후 `INCONCLUSIVE`

**한국어**  
7개 공정 case의 집계수준에서 열화상 지표를 이용하면 `power + scan speed + spot size`만 사용하는 단순 process-only 선형 기준선보다 melt-pool depth 또는 width 예측 RMSE를 최소 10% 개선할 수 있다.

**English**  
At the seven-case aggregate level, thermography-derived metrics can reduce melt-pool depth or width prediction RMSE by at least 10% relative to a simple process-only linear baseline using `power + scan speed + spot size`.

### Baseline / 기준선
Linear regression with `power + scan speed + spot size`. / `power + scan speed + spot size` 선형회귀.

### Test / 검증
Leave-one-condition-out cross-validation across the seven case means. / 7개 case 평균에 대한 leave-one-condition-out 검증.

### Primary Metric / 주요 지표
RMSE in µm. / µm 단위 RMSE.

### Material Improvement Threshold / 실질 개선 기준
≥10% RMSE reduction vs process-only baseline. / process-only 기준선 대비 RMSE 10% 이상 감소.

### Preliminary Outcome / 예비 결과
- Depth: best single thermal feature did not improve the process baseline. / 깊이: 최선 단일 열지표도 process 기준선을 개선하지 못함.
- Width: `TLCR` improved RMSE by ≈6.3%, below the 10% threshold. / 폭: `TLCR` 개선폭 약 6.3%로 10% 기준 미달.

### Interpretation / 해석
The aggregate evidence does not support a general claim of material predictive gain. Because only seven aggregate cases are available and replicate-level pairing has not been established, this is recorded as `INCONCLUSIVE` for the broader multimodal proposition rather than a blanket rejection of thermography.  
집계 증거는 일반적인 유의미 예측 개선을 지지하지 않는다. 다만 관측치가 7개 집계 case뿐이고 반복수준 pairing이 미확인이라 thermography 전체를 기각하지 않고 broader multimodal 가설에 대해 `INCONCLUSIVE`로 기록한다.

---

## H-AMB-001B — Replicate-Level Multimodal Hypothesis / 반복수준 멀티모달 가설

**State / 상태:** `HYPOTHESIZED` — future experiment / 향후 실험

**한국어**  
raw thermography에서 추출한 시간·공간 특징과 정확히 정렬된 optical geometry 측정을 결합하면 process-only 모델보다 unseen process condition 또는 track 수준의 geometry/quality uncertainty를 더 정확하게 예측할 수 있다.

**English**  
When raw thermography spatiotemporal features are correctly aligned with optical geometry measurements, a multimodal model can predict unseen-condition or track-level geometry/quality uncertainty more accurately than a process-only model.

### Promotion prerequisites / 승격 선행조건
- raw thermography files parsed / raw 열화상 파싱;
- replicate/track identifiers mapped / 반복·track ID mapping;
- cross-section measurement provenance mapped / 단면 측정 provenance mapping;
- leakage-safe split defined / 데이터누수 방지 split;
- baseline and target uncertainty defined / baseline·target uncertainty 정의.

No validation claim is made at this stage. / 현재 단계에서는 검증 결론을 주장하지 않는다.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.

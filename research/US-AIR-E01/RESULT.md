---
id: US-AIR-E01-RESULT
type: preregistered-primary-relationship-result
created: 2026-09-11
issue: 90
state: COMPLETED_PASS
final_gate: PASS_US_AIR_E01_POSITIVE_MATERIAL_PRECIPITATION_DELAY_ASSOCIATION
decision: DEC-126
claim: CLM-137
relationship_outcome_computed: true
incremental_monetary_cost_usd: 0
---

# US-AIR-E01 Result
# US-AIR-E01 결과

## Final gate / 최종 판정

**`PASS_US_AIR_E01_POSITIVE_MATERIAL_PRECIPITATION_DELAY_ASSOCIATION`**

Under the prospectively frozen 2025 airport-day design, higher same-calendar-date NOAA LCDv2 `DailyPrecipitation` is positively associated with higher BTS mean `DepDelayMinutes` after airport fixed effects, FlightDate fixed effects and scheduled-departure-volume control. / 사전고정한 2025 공항-일 설계에서 동일 달력일 NOAA `DailyPrecipitation` 증가는 공항·FlightDate 고정효과와 예정 출발편수 통제 후 BTS 평균 `DepDelayMinutes` 증가와 양의 연관성을 보였다.

This is a contemporaneous association result, **not causal inference, advance prediction or delay propagation**. / 이는 당일 연관성 결과이며 인과·사전예측·지연전파 결과가 아니다.

## Integrity / 무결성

- Stage A: `PASS_US_AIR_E01_STAGE_A_PRECIPITATION_QUALITY` — 255 airports / 255 stations / 92,818 usable weather keys.
- Stage B Run: `34429684361`.
- BTS 2025 frozen PREZIP hashes: **12/12 exact match before any ZIP CSV member was opened**.
- parsed source rows: **7,736,770**.
- rows belonging to the frozen Stage-A weather cohort: **6,726,149**.
- negative eligible `DepDelayMinutes` rows: **0**.
- non-finite/unparsed nonblank delay rows: **0**.
- monthly BTS header consistency: **True**.

## Realized panel / 실현 panel

- airport-day observations: **91,687**;
- unique airports: **255**;
- unique FlightDate levels: **365**;
- CR1 full parameter count K: **621**;
- FE alternating-projection iterations: **8**;
- final convergence change: **9.104e-15**.

The frozen support minimums of >=100 airports and >=30,000 airport-days pass without post-outcome subset selection. / 사전고정 support 기준을 outcome 사후선별 없이 통과했다.

## Primary preregistered estimate / 사전등록 주추정

- beta on `log1p(DailyPrecipitation_mm)`: **4.892129968812 minutes**;
- two-way CR1 SE, AirportID × FlightDate: **0.291257725833**;
- two-sided p-value: **4.30645849183e-43**;
- 95% CI: **[4.318542282873, 5.465717654751]**;
- model-implied 0 mm → 10 mm contrast: **11.730815 minutes**.

All three preregistered PASS conditions are satisfied: beta > 0, 95% CI lower bound > 0, and the 0→10 mm model-implied contrast >=1.0 minute. / 세 사전등록 PASS 조건을 모두 충족한다.

## Baseline comparison / baseline 비교

- baseline within-RMSE: **36.906107 min**;
- weather-model within-RMSE: **36.666737 min**;
- descriptive in-sample RMSE reduction: **0.649%**.

RMSE was not a preregistered gate and is reported descriptively only. / RMSE는 gate가 아니며 기술적으로만 보고한다.

## Prespecified sensitivities / 사전 sensitivity

All three non-gate sensitivities completed `OK` and preserve a positive CI-excluding-zero coefficient with an approximately 11.68–11.87 minute 0→10 mm model-implied contrast:
- trace `T=0.1 mm`;
- Diverted exclusion;
- AirportID × ISO-week dependence stress test.

Sensitivities do not alter or rescue the primary gate. / sensitivity는 primary gate를 변경·구제하지 않는다.

## What this result does not establish / 본 결과가 입증하지 않는 것

It does not establish:
- precipitation **causes** 11.73 minutes of delay;
- advance forecast skill;
- network delay propagation;
- airport/carrier vulnerability rankings;
- an optimal precipitation threshold;
- external-year or out-of-sample generalization;
- novelty relative to prior aviation-weather research;
- operational/commercial decision utility;
- policy or investment superiority.

The coefficient is conditional on the frozen same-day panel specification and log precipitation transform. / 계수는 고정한 당일 panel specification과 log precipitation transform에 조건부이다.

## Mission disposition / 미션 처분

US-AIR advances from `JOIN_READY` to **`RELATIONSHIP_TESTED`** for this one preregistered precipitation-delay relationship. / US-AIR은 이 단일 사전등록 관계에 대해 `RELATIONSHIP_TESTED` 단계로 진입한다.

Do **not** automatically tune weather variables, thresholds, lags or airport subsets. Close Issue #90 and return to Stage 0 portfolio control. / 변수·threshold·lag·공항 subset 자동튜닝 없이 #90을 닫고 Stage 0로 복귀한다.

A later descendant must compete at Stage 0 and separately address generalization, novelty and named decision utility. / 후속은 Stage 0에서 다시 경쟁하고 일반화·신규성·구체적 의사결정 효익을 별도 검증해야 한다.

Incremental monetary cost remained **0 USD**.


## Post-E01 novelty assessment / E01 이후 신규성 평가

`US-AIR-N01` / `DEC-128` subsequently assesses the exact E01 contribution as **`LOW_NOVELTY_CORE_RELATIONSHIP_KNOWN`**. This does not alter the empirical E01 PASS; it separates empirical validity from novelty. / N01은 E01의 실증 PASS를 변경하지 않고 신규성을 별도로 낮음으로 판정한다.

Defensible incremental value remains the breadth and reproducibility of the public-data workflow. `UTILITY_TESTED` and `GENERALIZATION_TESTED` remain unresolved.

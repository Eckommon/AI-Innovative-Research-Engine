---
id: PORTFOLIO-R09-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-10
issue: 89
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-US-004
selected_gate: US-AIR-E01
next_issue: 90
relationship_outcome_computed: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R09 Result — Post-US-AIR JOIN_READY Mission-ROI Reselection
# PORTFOLIO-R09 결과 — US-AIR JOIN_READY 이후 목적-ROI 재선정

## Final selection / 최종 선정

**`SELECT_C_US_004_FIRST_RELATIONSHIP_TEST`**

Selected next gate:

**US-AIR-E01 — preregistered daily precipitation × departure-delay airport-day relationship test**  
**US-AIR-E01 — 사전등록 일별 강수량 × 출발지연 공항-일 관계검증**

Issue #90.

This selection does not use any weather value, delay magnitude, weather–delay statistic or favorable effect. / 선정에는 기상값·지연값·기상-지연 통계·유리한 효과를 사용하지 않았다.

## Why Stage 0 selects US-AIR now / Stage 0에서 US-AIR을 선택한 이유

US-AIR-F01 has just produced a strong reusable JOIN_READY asset but has never opened the relationship:
- 263 final origin airports;
- 263 unique NOAA stations;
- 95,995 station × calendar-date source keys;
- deterministic full-year AirportSeqID/station mapping;
- no weather value or delay magnitude used in F01.

This creates a high-information transition from **JOIN_READY → first RELATIONSHIP_TESTED attempt**, rather than a tuning descendant after an already observed effect. / 이미 본 효과의 튜닝이 아니라 JOIN_READY에서 최초 관계검증으로 넘어가는 단계다.

By comparison:
- AU-NEM remains constrained by only four broad region-pair weather exposures;
- CA-RAIL's frozen first weather experiment held before Stage B on Minimum Temperature source completeness, so continuation requires a new redesign and competes with diminishing-return cost;
- JP-PORT already has a preregistered relationship result, so an immediate weather-variable extension is lower marginal information;
- C-EU-004 has a reusable join but under-specified direct operational outcome;
- C-SG-001 remains highly operable but has low independent spatial diversity;
- C-EU-001 remains scientifically high-value but retains external credential/operability friction recorded in prior portfolio reviews.

## Current official-source operability refresh / 현행 source operability 갱신

### BTS

The official Marketing Carrier On-Time Performance surface remains current and the 2025 twelve monthly PREZIP files remain directly listed. The table includes flight-date, airport identity, scheduled/actual operations, cancellation/diversion and delay fields. / BTS 정시운항 표와 2025 월별 PREZIP source가 계속 직접 제공된다.

Official:
https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=b0-gvzr&gnoyr_VQ=FGK

### NOAA LCDv2

LCDv2 remains the current NCEI product with direct station-year CSV bulk access. Official documentation defines `DailyPrecipitation` as a daily element in metric station-year files and explicitly warns that station variable coverage/gaps differ. / NOAA LCDv2는 station-year CSV와 `DailyPrecipitation`을 제공하며 station별 변수 지원·결측 차이를 명시한다.

Official:
https://www.ncei.noaa.gov/products/land-based-station/local-climatological-data

This makes a separate outcome-blind weather-variable quality gate scientifically necessary before opening delay magnitudes.

## Mission-ROI comparison / 목적-ROI 비교

0–5 each; total /45. Scores are selection aids, not empirical innovation findings. / 점수는 선정 보조이며 실증 혁신결과가 아니다.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return risk | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-AIR first E01** | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | **44** | **SELECT** |
| C-EU-001 Cross-National Grid Stress | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 4 | 5 | **39** | HOLD_HIGH_VALUE_OPERABILITY |
| C-CA-002 Grain Pressure × Rail Dwell | 5 | 5 | 5 | 3 | 5 | 5 | 3 | 4 | 2 | **37** | HOLD_REDESIGN_GEOGRAPHY |
| AU-NEM continuation | 5 | 5 | 5 | 2 | 5 | 5 | 4 | 3 | 2 | **36** | PRESERVE_JOIN__NO_BROAD_E01 |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 4 | **36** | PRESERVE_JOIN_ASSET |
| Canada rail-weather redesign | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 2 | 1 | **35** | NO_AUTO_RESCUE |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| JP-PORT continuation | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 2 | 1 | **34** | VALIDATED_RESULT__NO_AUTO_TUNING |

## Selected scientific uncertainty / 선정 과학 불확실성

The next uncertainty is not whether the airport/station join works; F01 already answered that.

It is:

> **Does one prospectively selected, source-defined daily weather exposure add a positive and materially nontrivial relationship with direct departure-delay burden after strong airport/date operational controls?**

The first E01 must answer that question without searching weather variables, thresholds, lags, airports or carriers after effects are visible.

## Exact next gate / 정확한 다음 gate

Open only Issue #90 / `US-AIR-E01`.

Before delay magnitudes:
1. freeze one primary NOAA variable;
2. freeze parsing/quality rules;
3. run Stage A weather-quality support only;
4. require a large prospectively qualified airport/station set;
5. only after Stage-A PASS may the frozen delay model execute.

Selected primary exposure:
**NOAA LCDv2 `DailyPrecipitation`**, transformed as `log1p(mm)`.

The E01 contract is in `research/US-AIR-E01/README.md`.

## Stop rule / 중단 규칙

Return to Stage 0 without predictor substitution if:
- the frozen DailyPrecipitation quality gate fails;
- the realized panel support falls below preregistered thresholds;
- station mapping requires repair;
- a different weather variable/outcome is proposed after failure;
- paid data or paid compute is required.

Incremental monetary cost remained **0 USD**.

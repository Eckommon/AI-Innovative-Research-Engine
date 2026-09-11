---
checkpoint_id: CHK-20260911-US-UTIL-F02-ACTIVE
active_issue: 96
active_research: US-UTIL-F02
last_completed_issue: 95
last_completed_research: PORTFOLIO-R12
last_decision: DEC-132
updated: 2026-09-11
---

# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R12_SELECTED_US_UTIL_F02__LONGITUDINAL_PREFLIGHT_ACTIVE`

## Latest portfolio decision / 최신 포트폴리오 결정

PORTFOLIO-R12 selects:

**`SELECT_C_US_005_LONGITUDINAL_COMPARABILITY_PREFLIGHT`**

Issue #96 `US-UTIL-F02` is the sole active research issue.

## Why this gate / gate 선정 이유

US-UTIL-F01 is JOIN_READY for 2024, but a relationship experiment would still risk mixing Reliability reporting methods, major-event semantics, AMI field definitions and changing utility/county support across years. Generic AMI resilience mechanisms also have prior precedent, so the next information gain is longitudinal comparability rather than an immediate coefficient. / 즉시 효과계산보다 다년 비교가능성 검증이 우선이다.

## Exact next action / 정확한 다음 행동

Execute only the **2019–2024 outcome-blind source/schema/identity/reporting-basis/cardinality preflight** under DEC-132.

Do not parse SAIDI/SAIFI/CAIDI magnitudes, AMI/AMR/standard-meter counts, storm severity/damage values, or any relationship coefficient.

Frozen PASS minimums:
- >=500 utilities with triple-schedule support in >=4/6 years;
- >=300 utilities with >=4 comparable Reliability-basis years;
- >=2,000 qualified utility-years;
- >=8,000 qualified utility-year×county mappings;
- NOAA county route and AMI field route reproducible in all six years.

Incremental monetary cost remains **0 USD**.

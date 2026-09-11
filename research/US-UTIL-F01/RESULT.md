---
id: US-UTIL-F01-RESULT
type: outcome-blind-join-feasibility-result
created: 2026-09-11
issue: 94
state: COMPLETED_PASS
final_gate: PASS_US_UTIL_F01_JOIN_READY
decision: DEC-130
claim: CLM-139
reliability_magnitudes_parsed: false
ami_meter_magnitudes_parsed: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-UTIL-F01 Result
# US-UTIL-F01 결과

## Final gate / 최종 판정

**`PASS_US_UTIL_F01_JOIN_READY`**

The frozen source/identity/cardinality gate passes without opening SAIDI/SAIFI magnitudes, AMI meter magnitudes, or any AMI × storm × reliability relationship. / SAIDI·SAIFI 값, AMI meter 값, AMI×폭풍×신뢰도 관계를 열지 않고 source·identity·cardinality gate를 통과했다.

## Qualified structure / 검증된 구조

- EIA-861 2024 final Reliability utility IDs: **908**
- Advanced Metering utility IDs: **2,379**
- Service Territory utility IDs: **2,907**
- Reliability ∩ AMI ∩ Service Territory IDs entering county qualification: **907**
- utilities with complete deterministic county qualification: **842**
- utilities excluded because at least one reported county was unmatched/ambiguous: **65**
- qualified utility×county mappings: **6,341**
- qualified mappings with zero NOAA 2024 county-event rows: **279**
- NOAA county event rows attached for source-key support diagnostics: **85,232**

The frozen minimums were >=300 county-qualified reliability utilities, >=250 with AMI support, >=1,000 qualified utility×county mappings, and a reproducible NOAA county route. All pass. / 고정 최소기준을 모두 통과한다.

## Join rule / 결합 규칙

EIA Service Territory uses exact EIA utility identity and preserves the many-to-many utility↔county structure. County names are deterministically normalized and matched by USPS state × normalized county name to the official 2024 Census county Gazetteer, yielding Census GEOID; NOAA county exposure uses `STATE_FIPS + CZ_FIPS` for `CZ_TYPE=C`. No fuzzy utility-name matching or customer allocation across counties is introduced. / utility·county 다대다 구조를 보존하고 fuzzy utility matching 및 county별 고객 가중치를 만들지 않는다.

A valid Census county with no NOAA 2024 event row is retained as a zero-recorded-event county, not treated as an unmapped geography. / Census상 유효하지만 NOAA event가 없는 county는 미매핑이 아니라 0-event로 보존한다.

## Evidence boundary / 증거 경계

This PASS means **JOIN_READY only**. It does not establish:
- an AMI effect on reliability;
- a storm effect on SAIDI/SAIFI;
- causal resilience;
- predictive utility;
- generalization, novelty, or decision utility;
- independent exposure for counties shared by multiple utilities.

Any relationship test must be separately selected and preregistered after Stage 0, with explicit treatment of storm aggregation, major-event-day definitions, reliability-reporting comparability, many-to-many exposure and dependence. / 효과실험은 Stage 0 재선정과 별도 사전등록이 필요하다.

## Durable evidence / 영속 근거

- `research/US-UTIL-F01/JOIN_QUALIFICATION.md`
- `research/US-UTIL-F01/UTILITY_COUNTY_JOIN_MAP.csv`
- `research/US-UTIL-F01/COUNTY_CROSSWALK_DIAGNOSTIC.csv`
- `research/US-UTIL-F01/JOIN_SOURCE_MANIFEST.csv`
- `research/US-UTIL-F01/SOURCE_CARDINALITY_PREFLIGHT.md`

Incremental monetary cost remained **0 USD**.

---
id: US-UTIL-F01-JOIN-QUALIFICATION
type: outcome-blind-join-qualification
created: 2026-09-11
issue: 94
gate: PASS_US_UTIL_F01_JOIN_READY
reliability_magnitudes_parsed: false
ami_meter_magnitudes_parsed: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-UTIL-F01 County/FIPS Join Qualification
# US-UTIL-F01 County/FIPS 결합 자격검증

## Identity rule / identity 규칙

EIA Service Territory county names are normalized deterministically and joined by exact `USPS state × normalized county name` to the official 2024 Census national county Gazetteer. The unique Census GEOID is then the join key to NOAA Storm Events `STATE_FIPS + CZ_FIPS` for `CZ_TYPE=C`. No fuzzy matching is allowed. / EIA county를 Census GEOID로 정확히 고정한 뒤 NOAA FIPS에 결합하며 fuzzy matching을 사용하지 않는다.

A county with a valid Census GEOID but no NOAA 2024 Storm Events row is retained as **zero recorded county-event rows**, not treated as an unmapped geography. / Census county는 존재하지만 NOAA event가 없으면 unmapped가 아니라 0-event로 구분한다.

## Source integrity / source 무결성

- EIA-861 final ZIP SHA-256: `77ce49c60ac5a6bad50c442fc401aad5404a21da875dc5cbaba353af5ede54de`
- Census Gazetteer member: `2024_Gaz_counties_national.txt`; SHA-256 `3c337402b5c6e8d5aa26b4278ccf4edc8989f2683765b3ffbf22296cdb2df3a0`
- NOAA details: `StormEvents_details-ftp_v1.0_d2024_c20260728.csv.gz`; SHA-256 `2070b83eccab041b36360ab73645b9a249c3eefc5b92b5b3fc0cbba4d9fcc09c`
- Census headers: `USPS, GEOID, ANSICODE, NAME, ALAND, AWATER, ALAND_SQMI, AWATER_SQMI, INTPTLAT, INTPTLONG`

## Utility identity support / utility identity 지원

- Reliability IDs: **908**
- Advanced Metering IDs: **2,379**
- Service Territory IDs: **2,907**
- Reliability ∩ AMI ∩ Service Territory IDs entering county qualification: **907**
- utilities with **100% of reported Service Territory counties** uniquely Census-mapped: **842**
- utilities excluded for >=1 unmatched/ambiguous county: **65**

## County / exposure-key support / county·노출 key 지원

- unique EIA state×county keys in eligible utilities: **3,058**
- exact unique Census matches: **3,012**
- unmatched Census keys: **41**
- ambiguous Census keys: **5**
- qualified utility×county rows after whole-utility completeness rule: **6,341**
- qualified utility×county rows with zero NOAA event records: **279**
- NOAA county event records attached to qualified mappings (diagnostic exposure support only): **85,232**

No storm severity/damage field and no reliability magnitude is used for qualification. NOAA event-row count is only a source-key support diagnostic and is not related to SAIDI/SAIFI here. / 폭풍 강도·피해 및 신뢰도 값은 자격판정에 사용하지 않는다.

## Frozen structural gate reapplied / 고정 구조 gate 재적용

- >=300 fully county-qualified reliability utilities: **True** (842)
- >=250 with AMI support: **True** (842)
- >=1,000 qualified utility×county mappings: **True** (6,341)
- NOAA 2024 FIPS route reproducible: **True**

## Gate / 판정

**`PASS_US_UTIL_F01_JOIN_READY`**

If PASS, F01 is JOIN_READY only. Any AMI × storm × reliability relationship requires a new preregistered experiment and must address many-to-many exposure aggregation, major-event-day definitions, utility reporting comparability and dependence before outcome values are opened. / PASS여도 JOIN_READY일 뿐이며 효과실험은 별도 사전등록이 필요하다.

## Durable derived artifacts / 영속 파생 산출물

- `research/US-UTIL-F01/UTILITY_COUNTY_JOIN_MAP.csv`
- `research/US-UTIL-F01/COUNTY_CROSSWALK_DIAGNOSTIC.csv`
- `research/US-UTIL-F01/JOIN_SOURCE_MANIFEST.csv`

Raw source bytes remain transient.

Incremental monetary cost remained **0 USD**.

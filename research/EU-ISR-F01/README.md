---
id: EU-ISR-F01
type: cross-agency-cross-national-feasibility-gate
state: PREREGISTERED
created: 2026-09-03
parent_candidate: C-EU-004
portfolio_decision: DEC-096
mission_anchor: MEM-054
incremental_monetary_cost_usd: 0
---

# EU-ISR-F01 — Facility-Coordinate × Climate-Exposure Join Feasibility
# EU-ISR-F01 — 산업시설 좌표 × 기후노출 조인 실행가능성 게이트

## 1. Purpose / 목적

Before any facility-risk score, model or ranking, determine whether the current official EEA industrial-site data and an openly accessible NASA POWER meteorological route can support a deterministic, reproducible **facility × time climate-exposure join** across European industrial sites.

시설별 위험점수·모델·순위를 만들기 전에, 현행 EEA 산업시설 데이터와 공개 접근 가능한 NASA POWER 기상경로를 이용해 재현 가능한 **시설 × 시간 기후노출 조인**을 구성할 수 있는지 검증한다.

This is a source/schema/spatial-temporal feasibility gate, not an association or causal experiment.

## 2. Frozen source candidates / 고정 source 후보

### A. EEA Industrial Reporting ver.16.0 / EEA 산업배출·시설
Official EEA release dated 20 Feb 2026, temporal coverage 2007–2024.

Required source semantics to qualify:
- stable site/facility identifier(s), including INSPIRE identifiers where documented;
- reporting year;
- industrial activity/classification;
- point/location geometry sufficient to derive latitude/longitude under a documented CRS transformation;
- facility/site reporting coverage and known incompleteness limitations;
- direct-download or official portal/service route reproducible at zero incremental cost.

Official roots:
- EEA Industrial Reporting datahub series `9405f714-8015-4b5b-a63c-280b82861b3d`;
- ver.16.0 tabular DOI/dataset identifier `657ac3cb-affa-4295-a4a9-27b4f539adab`;
- European Industrial Emissions Portal data connectors / site map.

### B. NASA POWER meteorology / NASA POWER 기상
Official NASA POWER Temporal API.

For F01, only access/schema/time semantics may be tested. Candidate low-DOF exposure fields are fixed prospectively to:
- `T2M_MAX` — daily maximum 2 m air temperature;
- `T2M_MIN` — daily minimum 2 m air temperature;
- `PRECTOTCORR` — corrected precipitation;
- `WS10M` — 10 m wind speed, if available for the selected community/request.

Use `time-standard=UTC` for qualification so time semantics are explicit. No variable may be added because it produces a stronger downstream association.

## 3. Frozen independent unit and join key / 고정 독립단위·조인키

Independent observational unit for any later experiment is a qualified **industrial site/facility × reporting period**, not a weather grid cell and not an emissions row duplicated across pollutants.

Candidate spatial join:
1. obtain an authoritative EEA site/facility coordinate;
2. transform to WGS84 latitude/longitude if required by the source CRS;
3. request NASA POWER at that coordinate;
4. record POWER's source grid resolution and treat identical returned grid cells as shared exposure, not independent climate measurements;
5. aggregate daily exposure only to a prospectively frozen reporting/event period in a later experiment.

F01 must not claim meter-scale local weather. NASA POWER meteorological source resolution is coarser than facility coordinates.

## 4. Frozen checks / 고정 검증항목

1. current EEA ver.16 identity, coverage, direct-access route and license/use terms;
2. exact site/facility identifier and geometry fields available from official schema/documentation;
3. authoritative CRS or deterministic coordinate-conversion route;
4. reporting-year/activity semantics and known reporting gaps;
5. NASA POWER direct zero-credential request path;
6. requested variable/time-standard metadata in a bounded sample response;
7. deterministic facility-coordinate→POWER point request construction;
8. explicit handling of shared POWER grid cells and spatial-resolution mismatch;
9. no emissions/climate association, facility ranking or threshold optimization;
10. no large bulk download in F01.

## 5. Bounded sample rule / 제한 sample 규칙

F01 may retrieve only what is needed to prove access and join mechanics:
- EEA metadata/schema and, if an official small feature/sample route exists, a bounded set of facility records;
- one to at most three facility-coordinate examples solely to validate coordinate/request mechanics;
- NASA POWER data for at most 7 consecutive days per test coordinate.

No sample may be selected based on known extreme emissions, climate exposure or outcome behavior.

## 6. Frozen gates / 고정 게이트

### `PASS_EU_ISR_FACILITY_CLIMATE_JOIN_READY`
All are established:
- current authoritative EEA source identity/access;
- stable facility/site identity and usable coordinate semantics;
- deterministic CRS→lat/lon route;
- direct NASA POWER request without credential provisioning;
- explicit time standard and requested variables;
- reproducible bounded facility→climate join;
- spatial-resolution/pseudoreplication handling is defined.

### `PARTIAL_EU_ISR_METADATA_SCHEMA_READY__FEATURE_SAMPLE_PENDING`
Source/schema/coordinate and NASA route are supported, but an actual EEA facility feature cannot be reproducibly obtained in the current execution context without a new access workaround.

### `HOLD_EU_ISR_SPATIAL_OR_TEMPORAL_SEMANTICS_GAP`
Official sources exist but coordinate/CRS/time/reporting semantics remain too ambiguous for a controlled join.

### `REJECT_EU_ISR_JOIN_ROUTE`
The selected source pair cannot defensibly represent a facility-coordinate × climate-exposure relationship without speculative spatial or identity linkage.

## 7. PASS downstream boundary / PASS 후속 경계

A PASS does not authorize a broad risk model. It allows at most one separately preregistered low-DOF controlled experiment with one fixed practical question and one primary metric, followed by mandatory Stage 0 Mission-ROI return.

Potential later questions must be selected only after F01 and cannot be chosen from observed facility-level associations inside this gate.

## 8. Cost / 비용

Incremental monetary cost remains **0 USD**. No paid compute/data, CDS credential provisioning, or commercial geospatial service is authorized.

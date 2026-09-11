---
id: US-WATERWAY-F01
issue: 98
state: COMPLETED_PASS
mission_anchor: MEM-054
decision: DEC-135
claim: CLM-141
final_gate: PASS_US_WATERWAY_F01_JOIN_READY
outcome_values_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-WATERWAY-F01 — LPMS Historical Delay × USGS Hydrology Feasibility
# US-WATERWAY-F01 — LPMS 역사적 지연 × USGS 수문 feasibility

## Objective / 목적

Qualify a reproducible public lock-level historical delay × hydrology source structure before any effect calculation. / 효과계산 전 공개 lock-level 역사 지연×수문 source 구조를 검증한다.

## Frozen source routes / 고정 source 경로

- USACE/NDC Corps Locks / LPMS official public reports and Data Web Services.
- USACE/NDC Lock Characteristics public geospatial service.
- USGS modern Water Data APIs for monitoring-location metadata and historical daily-value support.

## Outcome-blind rules / 결과 비사용 규칙

- inspect source access, schema, IDs, coordinates, date ranges and cardinality only;
- delay/processing/hydrology magnitudes must not be summarized or related;
- existence/nonblank of delay or arrival/start/end fields may be inspected without converting their magnitude;
- lock↔gage qualification must use coordinates plus river/waterbody identity; nearest distance alone is insufficient;
- no private/authenticated scraping and no FOIA request inside F01;
- raw external bytes remain transient under RAW-001.

## Frozen historical requirement / 고정 역사 범위

Require a minimum **3 contiguous years within 2016–2025** from an official public USACE route. A 24-hour/30-day live feed is not a substitute.

## Frozen PASS / 고정 PASS

All must hold:
- official public USACE historical lock-level delay or sufficient arrival/start timing support for >=3 contiguous years;
- stable lock identity crosswalkable to public coordinates;
- >=30 distinct locks with historical outcome support;
- >=25 locks prospectively matchable to at least one USGS monitoring location using coordinates plus river/waterbody identity;
- matched USGS daily-value date support overlaps the same >=3-year interval for a prospectively named streamflow and/or gage-height family;
- zero incremental monetary cost.

Failure of the historical-delay route is terminal HOLD for this F01. Do not lower thresholds or substitute annual unavailability.

## Final disposition / 최종 상태

**`PASS_US_WATERWAY_F01_JOIN_READY`** under `DEC-135` / `CLM-141`.

Verified outcome-blind structure: 193 historical Usage lock identities; 25/25 qualified historical-lock↔USGS crosswalks; shared 2018–2020 support; public Corps Locks Annual Usage route spans 2016–2025. No delay or hydrology magnitude was parsed.

`JOIN_READY ≠ EXPERIMENT_READY`; return to Stage 0 before any relationship test.

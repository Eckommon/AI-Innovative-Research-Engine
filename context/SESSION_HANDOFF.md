---
checkpoint_id: CHK-20260911-US-UTIL-F01-ACTIVE
active_issue: 94
active_research: US-UTIL-F01
last_completed_issue: 93
last_completed_research: PORTFOLIO-R11
last_decision: DEC-129
updated: 2026-09-11
---

# Session Handoff / 세션 인수인계

## Canonical restart point / 정확한 재개점

PORTFOLIO-R11 selected fresh candidate **C-US-005** and opened Issue #94 `US-UTIL-F01`.

Do not return automatically to US-AIR. / US-AIR 자동 복귀 금지.

## Selected source structure / 선정 source 구조

- EIA-861 2024 final data: utility identity + Advanced Metering + Reliability + Service Territory.
- NOAA/NCEI Storm Events 2024 annual bulk source.
- Preserve explicit utility↔county many-to-many structure.

## Exact next bounded execution / 다음 제한 실행

Run only the F01 source-byte/schema/cardinality preflight:
- exact source URL / byte length / SHA-256;
- archive/workbook/sheet names;
- non-outcome identity schemas;
- Reliability utility-ID support count without reading reliability magnitudes;
- Advanced Metering utility-ID support count;
- Service Territory utility×county count;
- NOAA county-key schema/cardinality;
- deterministic intersection counts and exclusions.

Do not estimate any relationship. / 관계추정 금지.

Cost remains **0 USD**; potentially billable work requires explicit prior approval.

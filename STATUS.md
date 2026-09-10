---
checkpoint_id: CHK-20260910-US-AIR-E01-STAGE-B-AUTHORIZED
active_issue: 90
active_research: US-AIR-E01
last_completed_issue: 89
last_completed_research: PORTFOLIO-R09
last_decision: DEC-125
updated: 2026-09-10
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_AIR_E01_STAGE_A_PASS__STAGE_B_AUTHORIZED`

## Stage A / Stage A

Run `34429102100` is accepted as:

**`PASS_US_AIR_E01_STAGE_A_PRECIPITATION_QUALITY`**

Frozen-quality result:
- 255 qualified origin airports;
- 255 NOAA stations;
- 92,818 usable airport-date weather keys;
- 0 assignment gaps / 0 ambiguous station assignments;
- 0 source fetch failures;
- 0 missing DailyPrecipitation columns;
- 0/263 source hash drift from F01.

No delay magnitude was parsed in Stage A.

## Exact next action / 정확한 다음 행동

Execute **Stage B only under the frozen DEC-124 model**, now authorized by DEC-125.

Before parsing any delay magnitude:
- re-download all twelve BTS 2025 PREZIP files;
- verify each SHA-256 exactly against the F01 frozen manifest;
- if any differs, stop before outcome parsing and HOLD source snapshot integrity.

If all hashes match:
- build the airport-day outcome only for Stage-A qualified usable weather keys;
- apply the frozen eligibility denominator;
- require >=100 airports and >=30,000 realized airport-days;
- fit the preregistered baseline/weather models;
- adjudicate the primary gate before sensitivities.

No alternate predictor, lag, threshold, outcome, airport/carrier subset or station remap is allowed.

Incremental monetary cost remains **0 USD**.

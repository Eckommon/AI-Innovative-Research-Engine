---
checkpoint_id: CHK-20260910-US-AIR-E01-STAGE-B-AUTHORIZED
active_issue: 90
active_research: US-AIR-E01
last_completed_issue: 89
last_completed_research: PORTFOLIO-R09
last_decision: DEC-125
updated: 2026-09-10
---

# Session Handoff / 세션 인수인계

## Canonical restart point / 정확한 재개점

US-AIR-E01 Stage A is durably PASS under DEC-125.

Do not rerun R09, F01 or Stage A by default.

Verified Stage-A support:
**255 airports / 255 NOAA stations / 92,818 usable airport-date weather keys**.

No DepDelayMinutes magnitude has yet been opened.

## Exact next bounded execution / 다음 제한 실행

Run Stage B using the already frozen DEC-124 model.

First perform a **12/12 BTS PREZIP hash check** against the F01 manifest before parsing any outcome magnitude. A mismatch is a source-integrity HOLD, not permission to silently use a revised snapshot.

Only after exact hash match:
- aggregate airport-day mean eligible DepDelayMinutes;
- scheduled count = non-duplicate scheduled rows;
- primary exposure = log1p(DailyPrecipitation_mm);
- baseline = airport FE + date FE + log1p(scheduled departures);
- weather model adds the frozen precipitation exposure;
- unweighted airport-day OLS;
- two-way CR1 by AirportID and FlightDate;
- realized support >=100 airports / >=30,000 airport-days.

Primary PASS additionally requires beta>0, 95% CI lower>0 and beta*ln(11)>=1.0 minute.

Sensitivities may run only after the primary gate and cannot rescue it.

Cost remains 0 USD.

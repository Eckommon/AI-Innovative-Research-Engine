---
id: CA-RAIL-E01-STAGE-A-TIME-BOUNDARY
type: pre-stage-a-contract-clarification
created: 2026-09-04
issue: 84
weather_values_opened: false
rail_dwell_relationship_computed: false
incremental_monetary_cost_usd: 0
---

# CA-RAIL-E01 Stage-A Time-Boundary Clarification
# CA-RAIL-E01 Stage-A 시간경계 명확화

This note applies the existing preregistration before any selected ECCC weather observation is opened.

## Frozen facts / 고정 사실

- Rail reference weeks are Monday through Sunday.
- The frozen rail reference-date universe runs from 2024-01-01 through 2025-12-29.
- The preregistered ECCC daily acquisition window is calendar years 2024–2025 only.
- Therefore the final rail reporting week beginning 2025-12-29 extends beyond the frozen weather acquisition window through 2026-01-04.

## Frozen handling / 고정 처리

Do **not** expand weather acquisition into 2026.

For Stage A:
- retrieve ECCC daily files for 2024 and 2025 only;
- evaluate every one of the 105 frozen Monday reporting weeks under the preregistered 7/7 rule;
- the week beginning 2025-12-29 can contain at most three in-window weather days and therefore cannot qualify as 7/7;
- mark it weather-ineligible for every station rather than opening 2026 data;
- do not remove the key from the parent F01 manifest; Stage A eligibility is a descendant filter.

This treatment is determined solely by the pre-existing calendar boundary and not by any weather or dwell magnitude.

Stage-A PASS thresholds remain unchanged:
- at least 90% of 14 × 105 station-weeks qualified;
- every station at least 90 qualified weeks.

No 2026 weather response is authorized inside this E01 version.

Incremental monetary cost remains **0 USD**.

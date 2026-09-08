---
id: US-AIR-F01-OUTCOME-ELIGIBILITY-CONTRACT
type: prospective-outcome-eligibility-contract
created: 2026-09-08
issue: 88
state: FROZEN_BEFORE_DELAY_MAGNITUDES
relationship_outcome_computed: false
delay_magnitudes_parsed: false
weather_values_parsed: false
incremental_monetary_cost_usd: 0
---

# US-AIR-F01 Outcome Eligibility Contract
# US-AIR-F01 Outcome 자격 계약

## Purpose / 목적

Freeze structural row eligibility for the future primary outcome, DepDelayMinutes, before any delay magnitude or weather value is analyzed.

## Frozen primary outcome / 고정 primary outcome

Primary future outcome family remains:

DepDelayMinutes

WeatherDelay remains ineligible as a primary outcome because it is an attributed cause-of-delay field.

## Structural eligibility / 구조 자격

For any later controlled experiment using continuous departure-delay magnitude:

1. Exclude Duplicate rows.
   - BTS defines Duplicate as a flag for a flight swapped based on Form-3A data.
   - Keeping the swapped duplicate as an additional independent flight would double-represent one scheduled operation.

2. Exclude Cancelled = 1 rows from the continuous DepDelayMinutes outcome universe.
   - A cancelled operation does not provide a uniform completed origin gate-departure event.
   - Some cancellation/gate-return cases can contain partial departure-related fields, but mixing those exceptional records with normally operated flights would make the continuous departure-delay denominator status-dependent.

3. Retain Diverted = 1 rows when Cancelled = 0, subject to DepDelayMinutes being nonblank.
   - Diversion occurs after origin departure and does not, by itself, invalidate the source-defined departure-delay construct at origin.

4. Require DepDelayMinutes to be nonblank for future continuous-outcome eligibility.
   - F01 may count blank/nonblank structure only.
   - F01 shall not parse, summarize, rank or model the delay magnitudes.

5. Preserve cancellation and diversion as status/context fields only.
   - They cannot be substituted as primary outcomes inside F01.

## Scientific boundary / 과학 경계

This contract only qualifies a future continuous departure-delay denominator. It does not authorize E01, causal interpretation, advance prediction, propagation analysis, weather-variable selection, or airport/carrier ranking.

## Source basis / source 근거

BTS Marketing Carrier On-Time Performance defines:
- DepDelayMinutes as scheduled-to-actual departure delay with early departures set to zero;
- Cancelled as the cancelled-flight indicator;
- Diverted as the diverted-flight indicator;
- Duplicate as the Form-3A swap duplicate flag.

Technical Reporting Directive #39 governs calendar-year 2025 on-time reporting and defines actual gate departure in local time.

## Cost / 비용

Incremental monetary cost remains 0 USD. Any potentially billable action requires explicit prior approval.

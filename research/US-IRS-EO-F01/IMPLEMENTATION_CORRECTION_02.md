---
id: US-IRS-EO-F01-IMPLEMENTATION-CORRECTION-02
type: implementation-only-correction
created: 2026-09-18
issue: 163
attempt_01_run: 35257875153
attempt_01_disposition: HOLD_US_IRS_EO_F01_FROZEN_GATES_FAILED
scientific_threshold_changed: false
source_years_changed: false
future_outcome_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-IRS-EO-F01 — Attempt 02 parser-only correction

Attempt 01 is immutable and preserved. It produced a valid 17/18 ledger with only Gate 11 failing because the implementation parsed **0 / 2,090,378** `SUB_DATE` values. All 2,090,378 nonblank EINs were valid exact nine-digit identifiers; Tax Period and Object ID gates passed completely; the future Automatic Revocation body remained unopened at 0 bytes.

The uniform 0% date parse, while every other source/schema/cardinality gate passed, indicates a representation/parser mismatch rather than a plausible absence of submission chronology. Public examples of the current IRS index format show recent `SUB_DATE` values represented at **year precision** (for example `2024`) rather than a full calendar date.

## Allowed implementation-only correction

Attempt 02 may extend **only** the `SUB_DATE` parser to accept an exact four-digit `YYYY` source value as a valid **year-precision submission-date representation**. It must:

1. keep Gate 11 threshold unchanged at **≥99.00%**;
2. keep all other 17 gates, thresholds, URLs, historical posting years and firewall rules unchanged;
3. record how many valid-EIN rows match `YYYY` versus the already-supported full-date/timestamp patterns;
4. label `YYYY` values as `year` precision and not interpret the synthetic January-1 sorting sentinel as an observed day/month;
5. preserve Attempt 01 evidence unchanged;
6. keep Automatic Revocation data rows opened = 0, 2025/2026 Form-990 index rows opened = 0 and revocation entity-body bytes consumed = 0.

If Attempt 02 still has any valid frozen-gate failure, the exact design is scientific HOLD. No further format expansion may be invented unless another demonstrable implementation representation defect is isolated without changing a scientific criterion.

No score, threshold, source period, identifier or hypothesis is changed. Cost remains **0 USD**.

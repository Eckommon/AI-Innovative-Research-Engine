---
id: PORTFOLIO-R32-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-16
issue: 144
state: COMPLETED_SELECT
selected_candidate: US-FMCSA-HAZ-001
selected_gate: US-FMCSA-HAZ-F01
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R32 Result — Select US-FMCSA-HAZ-001 F01

**`SELECT_US_FMCSA_HAZ_001_INSPECTION_TO_PHMSA_HAZMAT_F01`**

R32 was executed under the corrected prospective order:

`candidate/rule contract → Issue #144 → source revalidation → immutable scorecard`.

No candidate-specific outcome magnitude, exposure-stratified outcome count, coefficient, predictive score or relationship direction was opened.

## Frozen final scores / 최종 고정점수

| Candidate | Total | Disposition |
|---|---:|---|
| **US-FMCSA-HAZ-001** | **42/45** | **SELECT_F01_ONLY** |
| US-FTA-TRANSIT-001 | **37/45** | HOLD_RUNNER_UP |
| KR-GG-CHEM-001 | **36/45** | HOLD_IDENTITY_AND_OVERLAP |
| US-PIPE-001 | **36/45** | HOLD_RESTRICTED_GEOMETRY_AND_OVERLAP |

No tie-break is required.

## Why FMCSA × PHMSA leads / 선정 근거

The branch combines two separate federal safety systems with a prospectively exact identity path:

`FMCSA roadside inspection / violation / OOS → native USDOT Number → PHMSA Form 5800.1 Highway Carrier/Reporter FED DOT ID → later hazmat incident`.

Current official documentation supports public zero-cost inspection/violation files with USDOT Number and inspection date, while PHMSA documents carrier/reporter FED DOT ID and incident date. One F01 can remove the remaining high-value uncertainty: whether the Highway-mode PHMSA identifier behaves as an exact USDOT carrier key in current downloadable bytes, whether the represented cohorts overlap at useful scale, and whether the frozen time window is sufficient.

The branch is bounded to the publicly represented source cohorts. FMCSA's general public Inspection Files have explicit exclusions, including inactive USDOT numbers and active-HMSP entities, so R32 does not authorize a population-wide hazmat-carrier claim.

## F01 authorization boundary / 승인 경계

A separate `US-FMCSA-HAZ-F01` may verify only:

- current official zero-cost FMCSA inspection/violation source access;
- current official zero-cost PHMSA 5800.1 incident source access;
- native USDOT / FED DOT ID field semantics and parseability;
- exact Highway-mode carrier-ID overlap, without name/address/fuzzy repair;
- inspection-date and incident-date support;
- public-cohort scope/exclusions;
- repeated carrier/inspection structure;
- aggregate exact-ID overlap and deterministic identity fingerprints.

F01 may **not** open or compare hazmat incident occurrence/rates/counts by inspection, violation, OOS, BASIC or any derived carrier-risk profile. No causal or federal-safety-rating claim is authorized.

Incremental monetary cost remains **0 USD**.

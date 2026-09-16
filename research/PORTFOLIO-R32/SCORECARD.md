---
id: PORTFOLIO-R32-SCORECARD
type: immutable-mission-roi-scorecard
created: 2026-09-16
issue: 144
contract_decision: DEC-200
source_revalidation_commit: 0523fa3cb3c00564a034df6879c3b765b9c4f1da
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R32 Immutable Scorecard / 고정 점수표

The candidate pool/rubric was frozen before Issue #144, the Issue was then bound, and `SOURCE_REVALIDATION.md` was persisted before this scorecard. No candidate outcome magnitude, exposure-stratified outcome count, coefficient, predictive score or relationship direction was opened while scoring.

## Final frozen scores / 최종 고정점수

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total | Score disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-FMCSA-HAZ-001** | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 3 | **42/45** | **PROVISIONAL_SELECT** |
| US-FTA-TRANSIT-001 | 4 | 3 | 5 | 4 | 4 | 5 | 5 | 4 | 3 | **37/45** | HOLD_RUNNER_UP |
| KR-GG-CHEM-001 | 5 | 5 | 5 | 4 | 4 | 5 | 2 | 5 | 1 | **36/45** | HOLD_IDENTITY_AND_OVERLAP |
| US-PIPE-001 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 0 | **36/45** | HOLD_RESTRICTED_GEOMETRY_AND_OVERLAP |

No tie-break is required because `US-FMCSA-HAZ-001` leads outright by total score.

## Scoring basis / 점수 근거

### US-FMCSA-HAZ-001 — 42/45

- **Mission 5:** highway hazardous-material transport incidents are a direct public/industrial safety bottleneck with regulatory and operational consequences.
- **Cross-source 5:** the exposure side is FMCSA roadside inspection/violation/OOS data; the proposed subsequent incident side is PHMSA Form 5800.1. The candidate therefore crosses agency/program boundaries rather than merely combining two views of one table.
- **Direct outcome 5:** a reportable hazardous-material transportation incident is a concrete downstream safety outcome.
- **Independent-unit prospect 5:** USDOT-numbered carriers provide a natural repeated independent-unit family at national scale. A descendant still must freeze repeated-carrier/time handling before outcomes are opened.
- **Practical value 5:** if support exists, the relationship could inform carrier-level prevention, targeted inspection/safety management and hazmat-risk screening without claiming a federal safety rating or causal effect.
- **Zero-cost operability 5:** FMCSA inspection/SMS public files and PHMSA incident data are offered as public federal data at no incremental monetary cost.
- **Join defensibility 4:** FMCSA uses native USDOT Number and PHMSA exposes `Carrier/Reporter FED DOT ID`; however F01 must empirically prove that Highway-mode PHMSA identifiers behave as USDOT carrier IDs and quantify exact overlap. Carrier names/addresses/fuzzy matching are prohibited.
- **Next-gate information gain 5:** one outcome-blind F01 can resolve actual current file access, field semantics, public-cohort scope, carrier cardinality, inspection-year support, Highway FED-DOT-ID validity, exact overlap and fingerprints before any incident rate by inspection profile is opened.
- **Low-overlap/novelty 3:** FMCSA regulatory systems already consider inspection/OOS, crashes and hazardous-material incidents, and general carrier-safety predictive literature exists. Current source/literature search did not establish a clearly identical exact-USDOT FMCSA-inspection → subsequent PHMSA-5800.1-highway-hazmat public design, but absence of a hit is not novelty proof.

### US-FTA-TRANSIT-001 — 37/45

- **Mission 4:** transit mechanical reliability and major safety events are operationally important, though the bottleneck is less acute/specific than highway hazmat incident prevention.
- **Cross-source 3:** the candidate combines distinct NTD reliability and safety products, but both remain inside the same FTA NTD reporting program, reducing cross-source independence.
- **Direct outcome 5:** Major Safety Events are concrete event-level safety outcomes.
- **Independent-unit prospect 4:** agency × mode is a natural repeated unit with national support, but reporter-type differences and purchased/direct service structure require prospective handling.
- **Practical value 4:** useful to transit asset/reliability planning, but agency-level aggregation may limit specific intervention targeting.
- **Zero-cost operability 5:** FTA/DOT publish the relevant breakdown and safety files as public CSV/Excel/data-portal products.
- **Join defensibility 5:** source-native agency and mode fields provide a highly defensible prospective join; F01 must handle TOS/reporting-scope aggregation before outcome access.
- **Next-gate information gain 4:** F01 can cheaply establish historical source continuity, reporter-scope compatibility and exact agency/mode overlap.
- **Low-overlap/novelty 3:** system reliability and safety are already jointly recognized transit performance areas. Current search did not establish an identical nationwide prospective breakdown-to-later-major-event design, but conceptual overlap is material.

### KR-GG-CHEM-001 — 36/45

Carry the R31 score unchanged:

`5 + 5 + 5 + 4 + 4 + 5 + 2 + 5 + 1 = 36/45`.

Current official data remain public, but the accident source still has not established a stable common source-native business identifier shared with the facility table. Fuzzy/geospatial entity repair is unauthorized, and direct Korean accident-risk overlap remains material.

### US-PIPE-001 — 36/45

Carry the prior score unchanged:

`5 + 5 + 5 + 5 + 5 + 5 + 3 + 3 + 0 = 36/45`.

Public PHMSA incident files remain available, but unrestricted national NPMS geometry cannot be assumed or bypassed and direct literature/domain overlap remains high.

## Immutable selection consequence / 고정 선정결과

The sole score-based provisional selection is:

**`SELECT_US_FMCSA_HAZ_001_INSPECTION_TO_PHMSA_HAZMAT_F01`**

R32 may authorize only a separate outcome-blind F01 after atomic terminalization and State Integrity. The F01 must verify source access, exact native carrier identity semantics, time support, public-cohort scope, aggregate exact-ID overlap and fingerprints before any inspection-profile-conditioned incident occurrence is opened.

This scorecard must not be revised based on downstream support or eventual incident outcomes.

Incremental monetary cost remains **0 USD**.

---
id: PORTFOLIO-R42-REVALIDATION
type: bounded-source-overlap-revalidation
created: 2026-09-28
issue: 170
contract: 3defb5494bee758cf671ef358599a4e50c60161c
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R42 — bounded source / overlap revalidation

## Outcome firewall / outcome 방화벽

No candidate-specific future event row, membership, effect, prediction, ranking or causal result was opened. Revalidation used official source/documentation pages, public schema descriptions, canonical repository history and bounded framework/literature context only.

## 1. UK-CQC-LOC-001

CQC currently provides public API and downloadable data for regulated locations. Official documentation states that the API includes active and inactive providers/locations, registration start/end dates, organization/service information, latest ratings and report publication dates. Monthly care-directory/rating spreadsheets and a separate deactivated-locations file are also provided. CQC Location ID is the source-native location identifier.

Critical semantic limitation is explicit: archived/deactivated locations are not necessarily closed services; a location can be archived because of re-registration, legal-structure change or address change. Therefore a descendant F01 must separate registration-end/deactivation mechanisms before any adverse or closure interpretation.

Current source architecture is highly falsifiable at zero incremental cost and supports exact-identity structural testing.

## 2. US-BSEE-OCS-001

BSEE Data Center exposes platform structures, company/operator information and Incidents of Noncompliance. Official platform definitions identify `COMPLEX_ID_NUM` as a unique identifier for a single man-made structure or connected group, and structure number as a source-native sub-identifier. Platform pages directly expose historical INC records by Complex ID.

BSEE also publishes annual offshore incident spreadsheets/statistics covering fatalities, injuries, fires, explosions, gas releases, collisions, loss of well control and spills.

The decisive F01 uncertainty is whether incident-level public files preserve an exact Complex-ID/structure identity at sufficient coverage to support a prospective unit-level design. This is a strong information-gain target but carries higher join risk than CQC.

## 3. US-SAM-ENTITY-001

SAM.gov provides Entity and Exclusions data services. The current public exclusions extract layout defines a 12-character **Unique Entity ID** for excluded firms/entities and a daily ZIP extract naming convention. The data dictionary distinguishes exclusion program/type and source dates.

Identity semantics are strong, but operational access to some current data-service/API routes can require API-key/sign-in handling even where data are public. Historical entity-registration snapshot reproducibility and low exclusion base rates remain first-order structural uncertainties.

The candidate is distinct from prior USASpending vendor work because award outcomes are excluded and the proposed event family is SAM exclusion.

## 4. UK-OFSTED-URN-001

Ofsted publishes current and archived school-inspection management-information CSV/ODS files using exact **URN**. GIAS is the public school register and supports public downloads/search using URN. Its documented establishment schema includes status, close date and closure reason.

Identity and source operability are strong. However closure/reorganization semantics are mature and academy conversion/replacement may look like closure without disappearance of educational provision. This candidate also overlaps conceptually with the previously held NCES school-closure family and therefore receives a strong overlap penalty.

## Canonical internal-history check / 내부 이력

No prior exact candidate IDs or exact CQC/BSEE/SAM/Ofsted unit-event families were found in the canonical repository before R42. Prior HUD, FCC, IRS, FDIC, EPA, FAA-AIP, MSHA, FTA, RCRA, US-WW, NHTSA, FDA, FSIS and related terminal branches remain non-rescuable.

## Revalidation conclusion / 결론

All four frozen candidates remain eligible for one-time scoring.

- CQC: strongest exact identity + current source accessibility + next-gate semantic value.
- BSEE: high public-safety value and exact platform identity prospect, but incident-side identity coverage is uncertain.
- SAM: excellent UEI/exclusion semantics, but current anonymous operational access and historical snapshot lineage require verification.
- Ofsted/GIAS: strongest mature administrative identity/status path but lowest novelty/overlap value.

Incremental monetary cost: **0 USD**.

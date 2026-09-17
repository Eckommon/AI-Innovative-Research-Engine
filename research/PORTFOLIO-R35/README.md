---
id: PORTFOLIO-R35
type: stage0-portfolio-selection
created: 2026-09-17
status: CONTRACT_FROZEN__ISSUE_BINDING_REQUIRED
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R35 — independent Stage-0 reselection after EPA cross-media E01 terminal

## Purpose / 목적

Return independently to Stage 0 after `US-EPA-XMEDIA-E01 = NO_PREREGISTERED_POSITIVE_US_EPA_XMEDIA_E01_RELATIONSHIP`.

R35 is **not an EPA descendant rescue**. The completed RCRA→NPDES branch may not be altered, widened, re-endpointed, rematched, or mined for secondary outcomes. Any EPA candidate in R35 must use a different program, unit, exposure, outcome family and preregistration path and must compete from zero against non-EPA candidates.

R35 prioritizes a project-level lesson from R34/E01: technically clean identity is necessary but not sufficient. The next branch should maximize **cross-source information gain, practical value, independent-unit support, and low direct-overlap risk before outcome access**.

No candidate outcome magnitude, exposure-conditioned outcome count, coefficient, relationship direction, downstream membership, effect estimate or predictive score may be opened during R35.

## Frozen candidate pool / 고정 후보군

Exactly four candidates are authorized:

1. **`US-FAA-AIP-001`** — FAA Airport Improvement Program (AIP) airfield-infrastructure grant exposure → subsequent airport operational delay performance in BTS airline on-time data.
2. **`US-EPA-DWSRF-001`** — Drinking Water State Revolving Fund (DWSRF) assistance/project structure → subsequent SDWA drinking-water compliance at the same public water system via exact `PWSID`.
3. **`US-PHMSA-LI-001`** — PHMSA Safety-Related Condition / Integrity Assurance leading-indicator structure → subsequent reportable pipeline incident occurrence by exact `OpID`.
4. **`US-NRC-ROP-001`** — NRC inspection-finding structure → subsequent reactor initiating-event performance-indicator deterioration by exact reactor/docket identity.

No fifth candidate may be introduced after this contract is committed. A candidate may receive HOLD during source revalidation, but the pool itself must not be rewritten.

## Frozen Mission-ROI rubric / 고정 평가틀

Nine dimensions, each 0–5, total /45:

1. mission bottleneck;
2. cross-source value;
3. direct outcome;
4. independent-unit prospect;
5. practical value;
6. zero-cost operability;
7. join defensibility;
8. next-gate information gain;
9. low overlap / novelty risk.

### Interpretation rules

- `Zero-cost operability`: score current executable public machine-readable access, not documentation-only existence.
- `Join defensibility`: 5 requires a source-native exact shared identifier or official deterministic crosswalk. Equal-looking names/codes without demonstrated semantics do not receive full credit. No fuzzy names, addresses, geospatial nearest-neighbor repair or manual repair.
- `Independent-unit prospect`: score prospective independent sites/systems/operators/reactors and the likelihood of support-balanced strata before outcome access.
- `Next-gate information gain`: reward a cheap F01 that can decisively prove or reject source/schema/identity/cardinality support without reading outcomes.
- `Low overlap / novelty risk`: conservative. Direct prior empirical designs, regulator operational models, or agency analyses reduce the score. Search absence is not novelty proof.

## Frozen tie-break / 동점 규칙

If totals tie, compare in order:

1. next-gate information gain;
2. low overlap / novelty risk;
3. join defensibility;
4. independent-unit prospect;
5. cross-source value;
6. zero-cost operability;
7. direct outcome;
8. still tied → fail closed with no selection.

## Candidate boundaries / 후보별 경계

### 1. US-FAA-AIP-001 — AIP infrastructure → airport delay performance

**Prospective relation family:** airport-level FAA AIP airfield-infrastructure investment/project mix → subsequent airport operational delay performance.

Authorized source families for a future F01:
- FAA AIP Grant Histories / annual grant files, which expose airport `Loc ID`, project description and grant amounts;
- FAA/NASR Airport data only as an official identity bridge if required;
- BTS TranStats airline on-time / Master Coordinate airport tables.

A future F01 may inspect only source access, file schema, FAA `Loc ID`, BTS airport-code/airport-ID semantics, an official deterministic identity route if one exists, calendar support, eligible airport counts, grant-project categories, and aggregate exact overlap. It may **not** open grant-conditioned future delay values or direction.

Prospective exposure family for later design may distinguish airfield-operational projects (runway/taxiway/lighting/signage/safety-area) from non-operational/planning-only grants, but exact categories/windows/thresholds must be frozen in a later N01 before any downstream outcome access.

**Identity warning:** FAA `Loc ID` and BTS three-character airport code must not be assumed equivalent merely because strings match. F01 must establish semantics prospectively through official data/crosswalk support or HOLD.

**Overlap warning:** published work evaluates AIP/PFC funding and airport productive efficiency, so novelty is not presumed. R35 must specifically evaluate overlap with post-grant delay-performance designs.

### 2. US-EPA-DWSRF-001 — DWSRF project assistance → later SDWA compliance

**Prospective relation family:** DWSRF project/assistance structure → subsequent drinking-water compliance at the same public water system.

Authorized source families:
- EPA State Revolving Fund Public Portal / WIITS Drinking Water Assistance Agreement Report;
- EPA SDWIS/ECHO drinking-water public-system and violation/enforcement structural downloads.

The official Drinking Water Assistance Agreement data dictionary exposes exact `PWSID`, PWS name/type, initial agreement date, project start/completion, project categories, compliance category, amounts and other project attributes. SDWIS uses `PWSID` as the unique public-water-system identifier. A future F01 may inspect only source/schema/PWSID/date/cardinality/longitudinal support and exact aggregate overlap; no funding-conditioned future violation/compliance result may be opened.

**Anti-rescue boundary:** this candidate is not a continuation of RCRA→NPDES. Unit=`PWSID`, exposure=DWSRF assistance/project, outcome family=SDWA drinking-water compliance, source programs=WIITS/SRF + SDWIS.

**Overlap warning:** EPA OIG previously examined DWSRF projects in an “assist non-compliant systems to achieve compliance” category and post-project violations, and CWSRF financial-assistance→compliance has direct empirical literature. Novelty credit must therefore be strongly conservative.

### 3. US-PHMSA-LI-001 — pipeline leading indicators → later incident

**Prospective relation family:** operator-level Safety-Related Condition Reports and/or Integrity Assurance notifications → subsequent reportable pipeline incident occurrence/intensity.

Authorized sources:
- PHMSA Pipeline Source Data leading-indicator downloads;
- PHMSA operator-submitted incident/accident data;
- official `Pipeline Operators - OpIDs` table.

`OpID` is the official unique operator identifier used across PHMSA reporting. F01 may inspect only source access, schema, OpID/date support, operator universe, longitudinal coverage and exact overlap. It may not open leading-indicator-conditioned future incident occurrence.

**Overlap warning:** PHMSA explicitly describes SRCR / Integrity Assurance notifications as leading indicators used before accidents/failures, and pipeline enforcement/risk literature is mature. Novelty credit must be low unless revalidation finds a materially distinct relationship.

### 4. US-NRC-ROP-001 — inspection findings → later reactor PI deterioration

**Prospective relation family:** reactor inspection-finding burden/significance → subsequent initiating-event PI deterioration (e.g. IE01/IE03/IE04), with endpoint selection deferred to a later N01.

Authorized sources:
- NRC ROP Inspection Findings supporting data/data dictionary;
- NRC ROP quarterly Performance Indicator data;
- NRC plant/reactor/docket identifiers.

F01 may inspect only machine-readable access, schema, exact reactor/site/docket identity, date support, independent reactor counts and longitudinal overlap. No finding-conditioned subsequent PI outcome may be opened.

**Overlap warning:** inspection findings and performance indicators are already co-inputs to the NRC Reactor Oversight Process and the operating reactor universe is comparatively small. Novelty and independent-unit scores must be conservative.

## Frozen exclusions / 고정 제외

- `US-EPA-XMEDIA-001`: terminal E01; any descendant rescue prohibited.
- `US-FTA-TRANSIT-001`: prior N01 support HOLD; no threshold/mode/matching rescue.
- `US-BTS-PORT-001`: prior exact port-identity blocker and strong dwell/throughput overlap remain unresolved.
- `US-USCG-VESSEL-001`: technically strong but near-direct inspection→casualty literature overlap remains high.
- `US-MSHA-001`: technically strong but prior internal N01 and direct violation→injury literature overlap remain high.
- `US-FMCSA-HAZ-001`, `US-FDA-MD-001`, `US-NHTSA-MC-001`: prior source/schema blockers remain unresolved.
- FAA wildlife strike concepts: direct published wildlife-strike→BTS delay linkage already exists.
- DWSRF candidate may compete only as a distinct independent branch under the anti-rescue rule above.

## Governance / 거버넌스

1. This file freezes candidate pool, rubric, tie-break, boundaries and exclusions **before Issue binding and before score persistence**.
2. Bind a dedicated R35 Issue only after this commit exists.
3. After Issue binding, persist `SOURCE_REVALIDATION.md` covering current executable access, exact identity semantics, support risk and literature overlap for all four candidates without opening candidate outcomes.
4. Persist the scorecard exactly once after revalidation.
5. Select at most one next outcome-blind F01.
6. No candidate may be rescored using later F01/N01/outcome observations.
7. Incremental monetary cost remains **0 USD**.

## Current official evidence anchors used only to freeze feasibility questions

- FAA AIP Grant Histories: `https://www.faa.gov/airports/aip/grant_histories`
- BTS Master Coordinate: `https://www.transtats.bts.gov/Fields.asp?gnoyr_VQ=FLL`
- EPA SRF Public Portal: `https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/owsrf_public/home`
- EPA Drinking Water SRF data dictionary: `https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/owsrf_public/drinking-water-data-dictionary-page`
- EPA SDWIS Federal Reporting Services data dictionary: `https://www.epa.gov/DWdata/sdwis-federal-reporting-services-data-dictionary`
- PHMSA Source Data: `https://www.phmsa.dot.gov/data-and-statistics/pipeline/source-data`
- PHMSA Pipeline Operators - OpIDs: `https://www.phmsa.dot.gov/data-and-statistics/pipeline/pipeline-operators-opids`
- NRC Reactor Oversight Process: `https://www.nrc.gov/reactors/operating/oversight`
- NRC Inspection Findings Search: `https://www.nrc.gov/reactors/operating/oversight/findings-search`

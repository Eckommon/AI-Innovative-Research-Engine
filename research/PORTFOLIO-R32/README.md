---
id: PORTFOLIO-R32
type: stage0-portfolio-reselection
created: 2026-09-16
status: CONTRACT_FROZEN_PRE_SCORE
previous_terminal: US-NHTSA-MC-F01
previous_decision: DEC-199
candidate_count: 4
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R32 — Fresh-domain reselection after US-NHTSA-MC-F01 HOLD

## Purpose / 목적

R32 returns to Stage 0 after `US-NHTSA-MC-F01 = HOLD_US_NHTSA_MC_F01_SOURCE_SCHEMA_OR_IDENTITY`.

The NHTSA branch established that product identity/cardinality can be strong while a prospectively frozen public source still fails the required time/schema contract. R32 therefore gives particular weight, **within the existing rubric rather than by adding a new scoring dimension**, to candidates whose official public data are currently machine-readable, carry a stable native identity, expose a usable time axis, and can be evaluated at 0 USD before outcomes are opened.

R32 does **not** rescue NHTSA by switching from the frozen CSV to a richer TSV/flat source.

## Frozen candidate set / 고정 후보군

Exactly four candidates may be scored. No additional candidate may be inserted after Issue binding or source revalidation.

### C-US-005 — `US-FMCSA-HAZ-001`

**Roadside carrier inspection / violation / OOS profile → subsequent PHMSA highway hazardous-material incident**

Prospective identity concept:
- FMCSA carrier identity: native `USDOT Number`;
- FMCSA inspection time: source-native inspection date;
- FMCSA inspection/violation structure: public Inspection Files / SMS input files;
- PHMSA outcome identity: Form 5800.1 `Carrier/Reporter FED DOT ID`, restricted prospectively to Highway mode;
- PHMSA outcome time: source-native incident date.

F01, if selected, may test only current source access, exact identifier semantics, temporal support, cardinality, aggregate exact-ID overlap, and fingerprints. It may not open incident rates/counts by inspection-derived exposure.

### C-US-006 — `US-FTA-TRANSIT-001`

**Transit agency-mode mechanical breakdown / reliability profile → subsequent major safety-event incidence**

Prospective identity concept:
- FTA National Transit Database annual Vehicle Maintenance / Breakdowns data;
- NTD agency and mode identity as source-native join fields;
- NTD monthly Safety & Security time series / event-detail data for subsequent major safety events;
- annual exposure window precedes later safety-event window.

F01, if selected, may test only current file access, source-native agency/mode identity, year/month support, reporter-scope compatibility, aggregate overlap, and fingerprints. It may not compare future event incidence by breakdown burden.

### C-KR-002 — `KR-GG-CHEM-001`

**Gyeonggi hazardous-chemical facility profile → later chemical-accident identity**

Preserved from R31 without relaxation. The public facility and accident datasets exist, but a stable common business identifier has not yet been established; fuzzy entity resolution remains unauthorized. Prior Korean research directly relates chemical-enterprise risk factors to accident history, so overlap risk remains material.

### C-US-003 — `US-PIPE-001`

**Hydrologic stress → pipeline incident**

Preserved unexecuted comparator from R29–R31 without relaxation. Public PHMSA incident/mileage data remain available. Unrestricted national NPMS line geometry must not be assumed or bypassed, and direct domain overlap remains high.

## Excluded screened candidates / 제외 후보

The following are deliberately not in the scoring pool:

- `US-NHTSA-MC-001`: terminal HOLD under Issue #143; no post-hoc TSV rescue.
- USCG vessel inspection/deficiency → casualty: current direct public work already implements a closely overlapping PSIX/IIR deficiency-to-casualty design; dominated on novelty.
- FRA grade-crossing inventory → incident: FRA itself and prior research already operate closely overlapping inventory/incident risk models; dominated on novelty.
- MSHA violation/inspection → future accident: substantial direct prior research and predictive work; dominated on novelty.
- NRC inspection findings → scrams: ROP already combines inspection findings and performance indicators within the same oversight architecture, weakening cross-source information gain and independence.

These exclusions are screening decisions only; no candidate-specific outcome magnitude was opened.

## Frozen Mission-ROI rubric / 고정 평가틀

Score each authorized candidate exactly once, 0–5 on each dimension, total /45:

1. Mission bottleneck
2. Cross-source value
3. Direct outcome
4. Independent-unit prospect
5. Practical value
6. Zero-cost operability
7. Join defensibility
8. Next-gate information gain
9. Low overlap / novelty risk

### Tie-break / 동점 규칙

1. total
2. next-gate information gain
3. low overlap / novelty risk
4. join defensibility
5. direct outcome
6. still tied → fail closed; select none.

## Prospective scoring constraints / 사전 고정 규칙

- Source revalidation must occur **after this contract is bound to a dedicated Issue and before score persistence**.
- Current public machine-readability and time support may affect zero-cost operability, join defensibility and next-gate information gain; no new hidden scoring dimension may be added.
- Published work may reduce the low-overlap/novelty score, but absence of a search hit is not proof of novelty.
- No candidate outcome magnitude, exposure-stratified outcome count, coefficient, predictive score, or relationship direction may be opened during R32.
- No unofficial mirror, authentication bypass, paid source or paid API.
- Incremental monetary cost remains **0 USD**.

## Exact next action / 정확한 다음 행동

Bind this frozen candidate/rubric contract to a dedicated R32 Issue **before** writing `SOURCE_REVALIDATION.md` or `SCORECARD.md`. Then revalidate official sources, persist the source audit, score the four candidates once, and select at most one separate outcome-blind F01.

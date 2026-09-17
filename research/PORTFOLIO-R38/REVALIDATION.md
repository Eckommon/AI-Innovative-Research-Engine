---
id: PORTFOLIO-R38-REVALIDATION
type: source-literature-revalidation
created: 2026-09-18
issue: 159
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R38 bounded revalidation / 제한 재검증

This revalidation was performed after the candidate pool/rubric was frozen at `81216245922df756667295a4ffeb89fb41bd274f`. No candidate future outcome row or membership was opened.

## `US-FRA-XING-001`

- FRA's current Safety Data site provides full Highway-Rail Grade Crossing Accident/Incident (Form 57) and current/historical Crossing Inventory (Form 71) datasets.
- FRA Crossing Inventory and the Rail Crossing Locator use the U.S. DOT Crossing ID as the source-native crossing identity.
- Identity, outcome directness and national independent-unit support are therefore strong.
- Direct overlap is exceptionally high: FRA operates the Grade Crossing Accident Prediction System (GXAPS), and multiple published studies explicitly merge FRA inventory/history with collision records using Crossing ID to predict crash frequency/severity. Recent 2025/2026 literature continues this exact task family.
- Consequence: strong feasibility but severe direct-overlap/novelty penalty; R38 should not merely reproduce an established FRA collision-prediction stack.

## `US-FDIC-BRANCH-001`

- FDIC Summary of Deposits provides annual branch-office data back to 1994. Current SOD custom downloads expose mandatory branch/institution variables including `YEAR`, `CERT`, `BRNUM`, `UNINUMBR` and branch state.
- FDIC BankFind bulk downloads separately expose Institutions, Locations, History Events and SOD definition/data families.
- Recent SOD contains more than 76,000 domestic offices across more than 4,400 institutions, supporting a large independent-unit prospect.
- FDIC has direct descriptive precedent on branch openings/closures, and historical FDIC analysis reports that lower-deposit offices close at higher rates. Therefore generic 'low deposits predict closure' is not novel and must not be claimed.
- The remaining information gain is structural/prospective: can exact branch identity and history distinguish true closure/non-continuation from acquisition, sale/lease, institution merger or identifier transition without name/address repair? This is an outcome-blind F01 question and remains useful before any future closure membership is opened.

## `US-FCC-BDC-001`

- FCC BDC publishes provider lists and public data specifications/APIs. The provider list includes Provider ID and FRN.
- FCC documentation also states that fixed-availability submissions can contain a null Provider ID, making exact identity coverage an unresolved first-order gate.
- Biannual availability snapshots offer large independent-unit/geographic support, but a future 'withdrawal' can reflect filing/coverage changes rather than a clean business event unless separately defined.
- Consequence: useful F01 information gain but weaker source-native continuity and direct outcome quality than FDIC/FRA.

## `US-CMS-DIALYSIS-001`

- CMS Provider Data Catalog publishes downloadable/API dialysis facility datasets with exact CMS Certification Number (`CCN`) and thousands of facilities; 2026 releases continue regular refreshes.
- CMS also provides annual Medicare Dialysis Facilities data containing facility-level treatment, hospitalization, mortality and transplant measures.
- Source-native identity and independent-unit prospects are strong.
- However CMS ESRD quality/QIP systems and extensive dialysis quality research create a mature framework; a clean future facility-discontinuation state also requires explicit source/definition proof before outcomes.
- Consequence: technically strong but high framework-overlap and lower next-step novelty.

## Internal-history check

No prior canonical branch in this repository has executed these exact four R38 candidate IDs. The project has prior mature activity in adjacent transportation, CMS, EPA and financial-regulatory domains; scoring therefore penalizes direct agency-framework repetition rather than treating domain novelty alone as innovation.

## Boundary

No crossing collision membership, branch closure membership, broadband withdrawal membership, or dialysis discontinuation membership was opened or counted. No relationship, prediction, ranking, causal effect or novelty claim was computed. Cost: 0 USD.

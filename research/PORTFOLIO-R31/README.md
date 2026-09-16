---
id: PORTFOLIO-R31
type: mission-roi-portfolio-reselection
created: 2026-09-16
state: CONTRACT_FROZEN_AWAITING_ISSUE_BINDING
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R31 — fresh-domain reselection after terminal US-FDA-MD-F01 PARTIAL

## Purpose / 목적

Return to Stage 0 after `US-FDA-MD-F01 = PARTIAL_US_FDA_MD_F01_SOURCE_SEMANTICS_READY__INSPECTION_BYTES_ACCESS_BLOCKED`.

Do **not** retry FDA while the official inspection-byte route remains unchanged, do not use unofficial mirrors, and do not automatically promote an old runner-up. Compare one preserved candidate with two independently sourced fresh-domain candidates using source/access/identity and literature-overlap evidence only.

No candidate outcome magnitude, group-specific outcome rate, relationship statistic, coefficient, or predictive result may be opened in R31.

## Frozen candidate pool / 고정 후보군

Exactly three candidates may be scored.

### 1. US-NHTSA-MC-001 — manufacturer communications → subsequent safety recall

Prospective baseline source family:
- NHTSA Manufacturer Communications / Technical Service Bulletin public flat files.

Prospective future outcome family:
- NHTSA Safety Recall public flat files/API.

Prospective identity/time structure:
- manufacturer communication records expose `NHTSA ID Number`, `TSB/Document ID`, `Mfr Communication Date`, `Make`, `Model`, `Model Year`, NHTSA component and manufacturer component fields;
- NHTSA documents one communication record per TSB/document × product in the CSV and richer repeated rows in the TSV/flat file;
- recall data are also searchable/downloadable by Model Year × Make × Model and campaign identity;
- therefore one F01 can test whether a deterministic normalized product identity and prospective communication-time → later-recall-time route can be frozen without opening recall incidence by baseline signal.

Known overlap boundary:
- NHTSA explicitly treats manufacturer communications/service bulletins as Early Warning Reporting information and defect-analysis material;
- this is therefore not a claim that service bulletins are a newly discovered safety signal;
- current search did not establish a near-identical public-data prospective model-year/make/model communication-profile → later-recall experiment, but absence of a found paper is not proof of novelty.

Official source basis:
- https://www.nhtsa.gov/nhtsa-datasets-and-apis
- https://www.nhtsa.gov/vehicle-manufacturers/manufacturer-communications
- https://www.nhtsa.gov/resources-investigations-recalls
- https://static.nhtsa.gov/odi/ffdd/tsbs/TSBS.txt

### 2. KR-GG-CHEM-001 — Gyeonggi hazardous-chemical facility profile → later chemical-accident identity

Prospective baseline source family:
- Gyeonggi hazardous-chemical handling business/facility status public data.

Prospective future outcome family:
- Gyeonggi hazardous-chemical accident status public data.

Prospective identity/time structure:
- facility data expose business/facility name, addresses, business type and chemical-handling descriptors; public catalog metadata indicate free/open access;
- accident data expose accident region/date/content/cause/address and coordinates;
- the accident source does not currently establish a common stable business identifier shared with the facility source, so F01 must fail closed unless an exact deterministic source-native identity/coordinate/address route exists without fuzzy entity resolution;
- Gyeonggi-only scope is preserved and must not be generalized to Korea.

Known overlap boundary:
- Korean chemical-accident literature already studies regional/facility accident patterns;
- importantly, prior work developed and validated a Korean chemical-enterprise accident risk index using publicly available plant factors such as handling/storage/chemical counts and accident history, including Seoul/Gyeonggi businesses;
- therefore a facility-profile → accident-risk proposition has material conceptual overlap and receives no novelty presumption.

Official source basis:
- https://www.data.go.kr/dataset/15011194/openapi.do?lang=en
- https://www.data.go.kr/data/15059062/openapi.do
- https://www.data.go.kr/data/15057189/openapi.do

### 3. US-PIPE-001 — hydrologic stress → pipeline incidents

Preserved unexecuted candidate from R29/R30.

Carry forward without relaxation:
- PHMSA incident and annual mileage/facility data are public;
- unrestricted national NPMS line GIS cannot be assumed for a general-public zero-cost runner;
- restricted line geometry may not be bypassed, approximated from a non-equivalent denominator, or replaced after observing support;
- direct domain/literature overlap remains high.

R31 may rescore this candidate only using the already frozen source/access facts unless genuinely new official evidence appears before score persistence.

## Frozen scoring frame / 고정 평가틀

Reuse the established R26–R30 Mission-ROI rubric, each 0–5, total /45:

1. Mission bottleneck
2. Cross-source value
3. Direct outcome
4. Independent-unit prospect
5. Practical value
6. Zero-cost operability
7. Join defensibility
8. Next-gate information gain
9. Low overlap / novelty risk

Scores are portfolio-control judgments, not empirical findings.

## Frozen interpretation rules / 고정 해석 규칙

- `Join defensibility` scores deterministic identity plus current source accessibility; fuzzy matching does not receive full credit.
- `Independent-unit prospect` penalizes repeated products/facilities or clustered reporting structures that a prospective design may not be able to resolve.
- `Next-gate information gain` scores how much one outcome-blind F01 can eliminate uncertainty.
- `Low overlap / novelty risk` is an overlap/diminishing-return dimension only; literature-search absence is not novelty proof.
- Current source-access restrictions are real penalties even if the source might become available later.
- Geographic scope restrictions must remain explicit.
- No score may use candidate outcome magnitudes or observed relationship direction.

## Frozen tie-break / 고정 동점규칙

1. total score
2. next-gate information gain
3. low overlap / novelty risk
4. join defensibility
5. direct outcome
6. if still tied, fail closed and register a new prospective discriminator before selection.

## Exact next action / 정확한 다음 행동

Create and bind a dedicated PORTFOLIO-R31 Issue **before** any scorecard is persisted. Then score exactly these three candidates under the frozen rubric, select at most one winner, persist the terminal selection atomically, close R31, pass State Integrity, and only then open the selected candidate's separate outcome-blind F01.

Incremental monetary cost remains **0 USD**.


## Final disposition / 최종 처분

Issue #142 ratifies the immutable scorecard without rescoring. **`SELECT_US_NHTSA_MC_001_COMMUNICATION_TO_RECALL_F01`** is selected at **39/45**, ahead of KR-GG-CHEM-001 and US-PIPE-001 at **36/45** each. No candidate outcome was opened.

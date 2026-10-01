---
id: US-PHMSA-PIPE-F01
type: outcome-blind-structural-feasibility
created: 2026-10-02
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R51
parent_decision: DEC-291
selected_candidate: US-PHMSA-PIPE-001
facility_family: GAS_TRANSMISSION
future_incident_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-PHMSA-PIPE-F01 — exact OpID Gas-Transmission structural gate before future incident

## Mission / 목적

Determine, **before opening any incident membership first appearing in a later PHMSA source refresh**, whether PHMSA public data support a deterministic operator-level prospective design linking Gas Transmission infrastructure structure to later reportable pipeline incidents using source-native Operator ID.

F01 is structural only. It does not test whether mileage, material, vintage, commodity, geography or other infrastructure characteristics predict a later incident.

## Frozen facility family / 고정 family

Exactly one pipeline family is authorized:

**Gas Transmission**

Gas Gathering, Gas Distribution, Hazardous Liquid/CO2, LNG and UNGS may not be substituted after Issue binding.

The Gas Transmission family is selected because PHMSA publishes:
- annual report data with infrastructure/mileage/material/vintage concepts;
- current and superseded annual-report forms/instructions;
- Gas Transmission & Gathering incident data from January 2010 to present plus older historical files.

F01 must isolate transmission rows using source-native form/system indicators. Gathering rows may be read only where physically co-distributed in the official source and must remain excluded from the focal qualified cohort unless the official schema provides an exact Transmission classification.

## Frozen official source anchors / 공식 소스

- `https://www.phmsa.dot.gov/data-and-statistics/pipeline/source-data`
- `https://www.phmsa.dot.gov/data-and-statistics/pipeline/gas-distribution-gas-gathering-gas-transmission-hazardous-liquids`
- `https://www.phmsa.dot.gov/data-and-statistics/pipeline/distribution-transmission-gathering-lng-and-liquid-accident-and-incident-data`
- `https://www.phmsa.dot.gov/data-and-statistics/pipeline/pipeline-operators-opids`
- `https://www.phmsa.dot.gov/forms/gas-transmission-and-gathering-annual-report-instructions-f-71002-1`
- `https://www.phmsa.dot.gov/forms/gas-transmission-gathering-and-ungs-incident-report-instructions-f-71002-1`

Only official PHMSA/DOT-hosted files resolved from these surfaces are allowed.

## Frozen identity / 고정 identity

Primary operator identity is source-native **Operator ID / OpID**.

F01 must derive the exact syntax from official source documentation and observed column representation without repairing values.

Allowed:
- trim ASCII whitespace;
- preserve source text/numeric representation losslessly.

Prohibited:
- zero-padding unless PHMSA documentation explicitly defines a fixed-width padded representation before empirical adjudication;
- operator-name matching;
- address/state/geographic repair;
- fuzzy/manual reconciliation;
- using incident number or report number as operator identity.

## Frozen annual-report baseline / annual baseline

F01 may open official Gas Transmission annual-report source bodies for calendar years **2018 through 2025 inclusive** only.

This eight-year window is frozen before empirical row access.

For each annual source body, record:
- official URL/final URL;
- HTTP metadata;
- source filename/year;
- byte size and SHA-256;
- schema/header fingerprint;
- row counts;
- distinct exact OpIDs;
- transmission-qualified rows;
- structural-field support.

Supplemental corrections already incorporated into the official body at retrieval are accepted as source state. F01 does not reconstruct prior revisions of the same year.

## Frozen incident baseline / incident baseline

F01 may open exactly the official **Gas Transmission & Gathering Incident Data — January 2010 to present** source body resolved after Issue binding.

The exact body and SHA-256 become the historical incident baseline.

All incident rows present in that fingerprinted body are historical structural/event-support evidence only, even if their incident date is recent. F01 computes no exposure→outcome relation.

## Frozen future refresh / 미래 refresh

A future descendant may classify outcome membership only from a later official PHMSA incident-source refresh satisfying all:

1. body SHA-256 differs from the F01 incident baseline;
2. source remains the same official Gas Transmission/Gathering incident family;
3. at least one source-native incident/report row was first added or materially updated after the N01 prospective lock;
4. the later source body is first opened only after N01 freezes its design.

F01 may not open any incident body first published after its empirical runner-start cutoff.

## Frozen event semantics / 사건 의미

F01 evaluates structural support for source-native Gas Transmission reportable incidents.

The later N01 may choose **one** prospectively frozen primary outcome among:
- all reportable Gas Transmission incidents;
- PHMSA-defined Significant incidents;
- PHMSA-defined Serious incidents;

but F01 PASS does not choose among them.

F01 must prove that incident rows expose:
- exact OpID;
- incident/report identifier;
- incident date/time or date;
- system/facility type sufficient to isolate Gas Transmission;
- injury/fatality and/or PHMSA severity classification inputs sufficient to reproduce the chosen official category in a later N01.

Incident cause fields are event descriptors and may not become predictive baseline exposures.

## Anti-tautology firewall / 순환성 방화벽

Descendant predictive exposures may not include:
- prior incident counts/history;
- incident cause history;
- inspection/enforcement history;
- integrity-assurance/SRCR notification fields;
- known leak/failure/repair immediately preceding the outcome;
- future incident-derived fields;
- any direct PHMSA risk-ranking/enforcement flag.

F01 may inspect incident rows only for event support/semantics and exact identity continuity.

## Common-support precursor / common support

F01 must report broad distribution of operator-level annual structural support across the eight frozen years without selecting an exposure.

A later N01 must prove comparable exposure/control support before opening a later incident refresh.

## Immutable 18-gate contract / 불변 18개 gate

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical state is terminal R51 selection `US-PHMSA-PIPE-001`, checkpoint `CHK-20261002-PORTFOLIO-R51-TERMINAL`, last decision `DEC-291` |
| 2 | Issue binding | empirical runner executes only after a new Issue is bound to this exact pre-Issue contract commit |
| 3 | Official source access | all frozen PHMSA source/documentation anchors are reachable or officially redirected |
| 4 | Annual-body lineage | official Gas Transmission annual-report bodies for every year 2018–2025 resolve at zero cost and are independently fingerprintable |
| 5 | Annual schema continuity | every frozen year exposes source-native OpID and a deterministic Gas Transmission classifier plus infrastructure concepts for mileage and at least two of material/vintage/commodity/facility structure |
| 6 | OpID syntax | ≥ **99.90%** of nonblank annual-report OpID values satisfy the prospectively documented/source-native exact representation rule |
| 7 | Annual support | every frozen year contains ≥ **500** distinct exact Gas Transmission OpIDs |
| 8 | Longitudinal continuity | ≥ **70.00%** of 2025 qualified OpIDs appear in at least **6 of 8** frozen annual years |
| 9 | Structural completeness | among 2025 qualified operators, ≥ **95.00%** have nonblank total transmission mileage and ≥ **90.00%** have the required additional frozen structural concepts |
| 10 | Incident-body access | official January-2010-to-present Gas Transmission/Gathering incident body resolves, is parseable, and SHA-256 is recorded |
| 11 | Incident schema | incident source exposes OpID, incident/report ID, incident date, source-native system/facility classifier and fatality/injury or official severity inputs |
| 12 | Transmission event isolation | ≥ **99.00%** of focal incident rows can be deterministically classified as Gas Transmission without text/name/geographic inference |
| 13 | Incident OpID syntax/join | ≥ **99.00%** of nonblank focal incident OpIDs satisfy the exact OpID rule and ≥ **95.00%** of distinct focal incident OpIDs exact-match at least one frozen annual-report OpID |
| 14 | Historical event support | ≥ **1,000** distinct Gas Transmission incident/report IDs exist in the historical baseline |
| 15 | Event-date support | ≥ **99.00%** of focal historical incidents have a parseable source-native incident date |
| 16 | Future-source seal | no later incident body first published after runner start is opened; future incident membership opened = **false** |
| 17 | Outcome/identity firewall | relationship/prediction/ranking/causal metric computed = **false**; prohibited incident/enforcement exposure computed = **false**; name/address/geographic/fuzzy/manual identity repair = **false** |
| 18 | Reproducibility/cost | immutable evidence records official URLs/metadata, annual and incident fingerprints, schemas, counts, OpID continuity, contract SHA, runner SHA-256, runner-start cutoff, firewall values and `incremental_monetary_cost_usd = 0` |

## Frozen terminal rule / 종결 규칙

PASS only if every gate passes:

`PASS_US_PHMSA_PIPE_F01_GAS_TRANSMISSION_EXACT_OPID_FUTURE_INCIDENT_DESIGN_READY`

Any valid empirical failure:

`HOLD_US_PHMSA_PIPE_F01_GAS_TRANSMISSION_EXACT_OPID_FUTURE_INCIDENT_DESIGN_NOT_READY`

A valid scientific HOLD is terminal for this exact F01.

Do not rescue by:
- switching pipeline facility family;
- lowering annual/continuity/join/cardinality thresholds;
- repairing OpIDs by operator name or geography;
- adding a different PHMSA event source after observation;
- using prior incident/enforcement history as exposure;
- opening a later incident refresh.

Transport/host/parser defects may be corrected only if the scientific criteria remain unchanged and prior attempts remain immutable.

## PASS consequence / PASS 이후

PASS authorizes only a separate outcome-blind `US-PHMSA-PIPE-N01`.

N01 must freeze before later incident-source access:
- one non-tautological structural exposure;
- exact baseline OpID cohort;
- comparator/matching/stratification rule;
- common-support/balance thresholds;
- operator reorganization/ID-change handling;
- one primary source-native incident severity hierarchy;
- prospective source-refresh window;
- minimum event support and statistical gate.

E01 is not authorized by F01 PASS alone.

## Non-claims / 비주장

F01 makes no claim that any Gas Transmission infrastructure characteristic predicts or causes a later incident. No operator safety ranking, enforcement recommendation, causal claim or novelty claim is authorized.

Incremental monetary cost must remain **0 USD**.

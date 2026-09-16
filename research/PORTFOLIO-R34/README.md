---
id: PORTFOLIO-R34
type: stage0-portfolio-selection
created: 2026-09-17
status: CONTRACT_FROZEN__ISSUE_BINDING_REQUIRED
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R34 — cross-domain reselection after US-FTA-TRANSIT-N01 HOLD

## Purpose / 목적

Return to Stage 0 after `US-FTA-TRANSIT-N01 = HOLD_US_FTA_TRANSIT_N01_MATCHED_RELIABILITY_DESIGN_NOT_IDENTIFIABLE` and select at most one next outcome-blind branch.

R34 explicitly incorporates the information learned from the FTA branch: a large raw unit count and a defensible key are not sufficient if prospective exposure/control support collapses into too few strata, too few modes, or poor scale balance. Candidate evaluation must therefore consider not only source access and native identity but also whether the next gate can cheaply establish **heterogeneous, support-balanced independent units before outcomes are opened**.

R34 also restores domain breadth. The project is an innovation-discovery engine rather than a serial safety-screening engine; this round deliberately includes environmental cross-media and supply-chain/logistics candidates alongside technically strong safety comparators.

No candidate outcome magnitude, exposure-stratified outcome count, coefficient, predictive score, relationship direction, or downstream event membership may be opened during R34.

## Frozen candidate pool / 고정 후보군

Exactly four candidates are authorized for this portfolio round:

1. `US-EPA-XMEDIA-001` — RCRA hazardous-waste compliance-monitoring / violation structure → subsequent NPDES effluent exceedance at the same facility through the official FRS `REGISTRY_ID` linkage.
2. `US-BTS-PORT-001` — weekly U.S. seaport vessel-berthing stress → subsequent monthly port-level containerized trade throughput / shipping weight, using BTS/USCG-AIS operational measures and U.S. Census Schedule-D port trade data only if a deterministic source-native port identity can be prospectively established.
3. `US-USCG-VESSEL-001` — vessel inspection deficiencies / operational-control structure → subsequent reportable marine casualty by source-native Coast Guard vessel identity.
4. `US-MSHA-001` — mine inspection / violation structure → subsequent accident/injury incidence by exact Mine ID; preserved technically strong comparator from R33 with its direct-overlap warning retained.

Excluded from R34:
- `US-FTA-TRANSIT-001`: immediate post-HOLD rescue is prohibited. Its N01 thresholds, strata, modes or matching may not be redesigned from observed support.
- `US-FMCSA-HAZ-001`: official PHMSA detailed-export access blocker remains unresolved.
- `US-FDA-MD-001`: prior official inspection-byte access blocker remains unresolved.
- `US-NHTSA-MC-001`: terminal source/date-schema HOLD; no richer-source rescue.
- `US-FRA-XING-001`: high direct literature overlap already established in R33.
- `KR-GG-CHEM-001`: weak shared native business identity and substantial overlap already established.
- EPA RMP-dependent concepts: the public RMP data tool is not treated as currently executable zero-cost infrastructure for this round.

## Frozen Mission-ROI rubric / 고정 평가틀

Reuse the established nine dimensions, each scored 0–5, total /45:

1. Mission bottleneck
2. Cross-source value
3. Direct outcome
4. Independent-unit prospect
5. Practical value
6. Zero-cost operability
7. Join defensibility
8. Next-gate information gain
9. Low overlap / novelty risk

### R34 interpretation rules

`Zero-cost operability` and `Next-gate information gain` must reflect **current executable machine-readable public-source access**, not merely documentation that a source theoretically exists.

`Join defensibility` gives full credit only to source-native exact identifiers or an official deterministic crosswalk whose exact-match subset can be isolated prospectively. Name similarity, address heuristics, geospatial nearest-neighbor repair, manual entity repair and post-outcome matching are not equivalent to a native join.

`Independent-unit prospect` now explicitly includes prospective support heterogeneity and balance. A candidate with many raw rows but very few independently usable strata / modes / sites must be discounted.

`Low overlap / novelty risk` is conservative. A directly similar published design, agency-operational targeting model, or mature literature materially reduces the score. Search absence is not novelty proof.

## Frozen tie-break / 동점 규칙

If totals tie, compare in order:
1. next-gate information gain;
2. low overlap / novelty risk;
3. join defensibility;
4. independent-unit prospect;
5. zero-cost operability;
6. direct outcome;
7. still tied → fail closed with no selection.

The added `independent-unit prospect` tie-break appears only after join defensibility and before operability to reflect the FTA N01 lesson prospectively; it is frozen before Issue binding and score persistence.

## Frozen candidate boundaries / 후보별 경계

### US-EPA-XMEDIA-001

Prospective relationship family: RCRA hazardous-waste compliance monitoring / violation history → later Clean Water Act NPDES effluent-limit exceedance at the same physical facility.

Authorized identity path for a future F01:
- RCRA source-native facility ID and official FRS `REGISTRY_ID` linkage;
- NPDES source-native permit ID and official FRS linkage;
- only exact official FRS program linkages may bridge RCRA ↔ NPDES.

Candidate source families:
- EPA ECHO RCRA Pipeline / RCRAInfo downloads;
- EPA FRS Facilities and Program Linkages;
- EPA ICIS-NPDES facility / permit / DMR / effluent-violation downloads.

A selected F01 may inspect only source access, schema, dates, official FRS identity, facility overlap, longitudinal support, and deterministic fingerprints. It must not open RCRA-conditioned future effluent-exceedance occurrence, rate, magnitude, pollutant outcome, or relationship direction.

Cross-media caution is frozen prospectively: RCRA and NPDES can overlap legally and operationally at industrial facilities, so the later study may identify a general facility-level compliance-risk signal rather than a novel causal mechanism. Formal literature revalidation must determine the novelty score before selection.

### US-BTS-PORT-001

Prospective relationship family: port-level vessel berthing stress / dwell → subsequent monthly containerized trade throughput or vessel shipping weight.

Candidate sources:
- BTS Port Performance Freight Statistics / Vessel Berthing Times derived from USCG AIS;
- U.S. Census Foreign Trade port-level imports/exports and Schedule D port codes.

A selected F01 must first prove that the specific BTS berthing series can be mapped to Census trade ports using a deterministic official source-native identity/crosswalk. **Port-name matching is not authorized.** BTS itself warns that port boundaries can differ across source systems; if no exact defensible identity exists, the branch must HOLD rather than use fuzzy/geographic repair.

F01 may inspect only port identity, source access, time support, call-count/cardinality support and aggregate overlap. No berth-stress-conditioned subsequent trade decline/growth may be opened.

Direct-overlap warning is frozen: port dwell / congestion and throughput are established research topics, including AIS-based throughput estimation. R34 must not claim novelty from data availability alone.

### US-USCG-VESSEL-001

Prospective relationship family: vessel inspection deficiencies / operational-control history → subsequent reportable marine casualty.

Candidate official source families:
- USCG Port State Information Exchange / PSIX inspection, deficiency and operational-control exports;
- USCG Marine Casualty and Pollution Investigation / IIR closed reportable marine casualty data and official web-service identifiers.

Prospective identity is source-native Coast Guard vessel identity only, preferring exact MISLE vessel ID and/or exact primary vessel identification number where supported by both products. No vessel-name fuzzy repair is authorized.

A selected F01 may inspect source access, schema, vessel identifiers, inspection/deficiency dates, casualty-source identity support, longitudinal cardinality and exact aggregate overlap only. No deficiency-conditioned casualty occurrence may be opened.

Direct-overlap warning is frozen: port-state-control inspection/deficiency histories and marine casualty risk have prior published literature, so novelty credit must be conservative even if the current U.S. source package is technically strong.

### US-MSHA-001

Carry the R33 candidate boundary and warning unchanged.

Prospective identity: exact source-native `Mine ID`; inspection-to-violation linkage uses source-native `Event Number`. Official MSHA complete-replacement ZIP/TXT products provide inspection, violation and accident/injury data.

A selected F01 may inspect only source/schema/Mine-ID/time/cardinality support. No violation-conditioned injury outcome may be opened.

Direct-overlap warning remains binding: published work already uses MSHA violation/enforcement histories to forecast later injuries/lost-days and longitudinal mine-level research links regulatory adherence measures to injury rates. R34 may not restore novelty credit merely because the source is technically convenient.

## Governance / 거버넌스

- This file freezes the candidate pool, rubric, candidate boundaries, interpretation rules and tie-break **before Issue binding and before score persistence**.
- Create/bind a dedicated R34 Issue next.
- After Issue binding, persist a dated `SOURCE_REVALIDATION.md` covering current machine-readable access, native identity semantics, support-risk signals and literature-overlap evidence for all four candidates.
- Do not read candidate outcome values during source/literature revalidation.
- Persist an immutable scorecard exactly once after source revalidation.
- Select at most one next outcome-blind F01.
- No candidate may be rescued or rescored from downstream support or outcome observations.
- Incremental monetary cost remains **0 USD**.

---
id: PORTFOLIO-R45-REVALIDATION
type: bounded-source-overlap-revalidation
created: 2026-09-29
issue: 176
contract: 01f4518bd72f5db542e437bd5669b9c0489efdc9
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R45 — bounded source / overlap revalidation

## Outcome firewall / outcome 방화벽

No candidate-specific future event membership, effect, prediction, ranking or causal result was opened. Revalidation used official source/documentation pages, canonical internal history and bounded framework context only.

## 1. US-MSHA-MINE-001

MSHA's Open Government data surface currently publishes mine-related datasets on a repeated update schedule. Official accident/injury data cover reported accidents, injuries and illnesses from 2000 onward; the accident document number is the row-level unique key. Official quarterly employment/production data are grouped by Mine ID and subunit, while MSHA's broader mine retrieval system exposes mine status/location/ownership/employment/inspection/violation history.

Structural strengths:
- strong source-native Mine ID prospect for longitudinal mine-level linkage;
- public quarterly employment/production plus accident/injury data;
- direct severity/event information within the accident family;
- long historical lineage and repeated source refresh;
- high public-safety and operating-continuity value.

Primary unresolved risks:
- accident rows have their own document number, so deterministic Mine-ID coverage must be proven rather than inferred;
- F01 must prospectively define serious/fatal event severity and event date semantics;
- current/future accident rows must be sealed so no outcome-driven threshold or exposure construction occurs.

Internal overlap is low relative to the immediate portfolio. Mining safety is a mature research area, so novelty credit remains conservative even though the exact public-data design is new to the canonical project history.

## 2. US-NCUA-CU-001

NCUA currently publishes final quarterly Call Report ZIP/CSV data with historical coverage back to 1994, active federally insured credit-union listings, quarterly merger reports and public conservatorship/liquidation records.

Structural strengths:
- rich quarterly institution-level financial/operating data;
- direct legal event families including involuntary liquidation, conservatorship and assisted merger;
- source-native charter number exists in NCUA charter/merger records and official liquidation notices.

Primary unresolved risk:
- the public conservatorship/liquidation table foregrounds name/city/state rather than a charter key in the table itself; F01 must establish a deterministic zero-cost charter-number event path from official records without name matching.

Overlap:
- financial-institution distress/exit has conceptual overlap with prior FDIC work, materially reducing marginal novelty/information credit despite a different regulator and institution type.

## 3. US-CMS-NH-001

CMS currently publishes one-row-per-nursing-home Provider Information with exact CCN, staffing/quality/inspection-related fields, topic-level archived datasets and public Medicare termination notices carrying provider CCN.

Structural strengths:
- exact CCN identity;
- large current provider population;
- rich multi-table staffing/quality/inspection structure;
- direct legal termination notice concept.

Primary unresolved risk:
- CMS states that public termination notices are posted for a bounded recent period, limiting immediately visible historical event lineage;
- F01 must establish enough historical CCN-level terminations before any prospective outcome design is authorized.

Overlap:
- healthcare quality/closure prediction is mature, so low-overlap/novelty credit is conservative.

## 4. US-FDA-PMA-001

FDA's PMA database currently supports exact PMA Number search and downloadable files. FDA's regulatory guidance separately defines withdrawal of approved PMA and temporary suspension, including formal withdrawal orders.

Structural strengths:
- exact source-native PMA number;
- public approval/decision fields and downloadable database;
- direct regulatory event semantics for withdrawal/suspension.

Primary unresolved risk:
- PMA supplements also carry withdrawal dates in the public database. F01 must distinguish withdrawal of the original approved PMA from supplement-level withdrawal and applicant withdrawal before approval.
- historical source support may be sparse for actual withdrawal of approved PMAs.

Overlap:
- this immediately follows an EMA medicine-regulation branch, so medical-regulatory overlap is explicitly penalized.

## Canonical-history exclusions / 내부이력 제외

- EMA is terminal negative evidence and is not rescored.
- R44 held FERC, ACNC and UKIPO candidates are not re-entered.
- R43/R42/R41/R40 held candidates remain outside the immediate pool.
- NCUA is not treated as an FDIC rescue; exact charter-level liquidation semantics must stand independently.
- CMS may not use termination-pending/outcome-coded fields as historical exposure.
- FDA may not pool original-PMA withdrawal with supplement/application withdrawal.
- MSHA future accident/event rows remain sealed.

## Revalidation conclusion / 재검증 결론

All four frozen candidates remain eligible for one-time scoring.

MSHA has the highest next-gate information value because exact Mine ID, long official employment/production history, accident/injury records and direct severity semantics can be tested within one bounded structural F01. NCUA has strong financial data and direct liquidation semantics but a charter-key event-link uncertainty plus financial-domain overlap. CMS has excellent CCN/data richness but shorter public termination-notice lineage. FDA has strong identity/regulatory semantics but event-level ambiguity and immediate medical-regulatory overlap.

Incremental monetary cost: **0 USD**.

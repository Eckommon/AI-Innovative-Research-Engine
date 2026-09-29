---
id: US-MSHA-MINE-F01-RESULT
type: structural-feasibility-result
created: 2026-09-29
issue: 177
research: US-MSHA-MINE-F01
disposition: PASS
attempt_02_commit: 3d2756ae172845707e189e2181534a119f435d7a
attempt_02_run: 36547574031
contract_commit: 18a90079c3566641bc3856f7d802acdc75b53388
gate: PASS_US_MSHA_MINE_F01_EXACT_ID_SERIOUS_FATAL_FUTURE_EVENT_DESIGN_READY
---

# US-MSHA-MINE-F01 Result / 결과

## Terminal disposition / 최종 판정

**`PASS_US_MSHA_MINE_F01_EXACT_ID_SERIOUS_FATAL_FUTURE_EVENT_DESIGN_READY`**

Attempt 02 is a valid empirical execution of the frozen 18-gate contract and passes **18/18** requirements. Future serious/fatal event membership remains unopened. F01 therefore authorizes only a separate outcome-blind `US-MSHA-MINE-N01` design; E01 is not authorized.

## Structural evidence / 구조 근거

- complete Mines rows / exact Mine IDs: **92,028**
- exact seven-digit Mine-ID syntax: **92,028 / 92,028 = 100%**
- frozen operating-status Mine IDs: **13,351**
- 2026 Q1/Q2 employment/production rows: **46,099**
- distinct Q1/Q2 employment Mine IDs: **12,857**
- employment→Mines exact-ID coverage: **12,857 / 12,857 = 100%**
- pre-cutoff accident rows: **275,067**
- historical accident Mine IDs: **13,538**
- accident→Mines exact-ID coverage: **13,538 / 13,538 = 100%**
- frozen serious/fatal documents: **11,934**
- distinct mines with historical frozen serious/fatal events: **4,396**
- severe-event row integrity: **11,934 / 11,934 = 100%**
- future rows inspected for severity: **0**
- future serious/fatal event membership opened: **false**
- incremental monetary cost: **0 USD**

## Source fingerprints / 소스 지문

- `Mines.zip`: `3ddec0aebbc3fd4d70feeae0e507fd0ccee4e45516768b1a932e6e185f43fcd7`
- `MinesProdQuarterly.zip`: `4fa86737661eeee1aa9eea16b39614aba961a1920abf471761424b9613b1e960`
- `Accidents.zip`: `db5ac677f235e90f6214e6f26ee2b2994e32f01e18124f5165f05b5f741420b6`

## Attempt provenance / 시도 계보

Attempt 01 / Run `36547173693` preserved the same scientific data and passed 17/18 gates. Its sole Gate-3 failure came from an implementation predicate that required exact HTTP 200 although the frozen contract required an official documentation anchor to be reachable or officially redirected; the MDRS anchor returned HTTP 202.

Implementation correction `43c2cc7768500407e13058322988c206aa31c2a8` changed only documentation reachability from exact 200 to any 2xx response. It changed no source URL, scientific threshold, population, Mine-ID rule, quarterly baseline, serious/fatal code, date cutoff or future firewall.

Attempt 02 / Run `36547574031` then passed 18/18 under the unchanged scientific contract and is preserved at commit `3d2756ae172845707e189e2181534a119f435d7a`.

## Consequence / 후속 조치

F01 PASS authorizes exactly one separate outcome-blind `US-MSHA-MINE-N01` design. Before any future event membership is opened, N01 must freeze:
- one non-tautological historical exposure;
- eligible mine population/exclusions;
- comparator and matching/stratification rules;
- future serious/fatal event hierarchy;
- competing event/status handling;
- minimum future-event/support thresholds;
- statistical/falsification rule.

No future accident membership may be opened merely because F01 passed.

## Non-claims / 비주장

F01 establishes structural joinability and event semantics only. It does not establish that mine characteristics predict or cause accidents, does not rank mines, and does not authorize enforcement or operational recommendations.

Incremental monetary cost: **0 USD**.

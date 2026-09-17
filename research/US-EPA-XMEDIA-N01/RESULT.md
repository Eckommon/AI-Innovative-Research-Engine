---
id: US-EPA-XMEDIA-N01-RESULT
type: outcome-blind-matched-design-identifiability
created: 2026-09-17
issue: 151
state: COMPLETED_PASS
gate: PASS_US_EPA_XMEDIA_N01_MATCHED_MONITORING_INTENSITY_DESIGN_IDENTIFIABLE
source_run: 35167553702
staging_commit: 78f0f0f1458463c79c326c016d415dc5533af026
future_outcome_membership_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-EPA-XMEDIA-N01 Result — matched monitoring-intensity design PASS

**`PASS_US_EPA_XMEDIA_N01_MATCHED_MONITORING_INTENSITY_DESIGN_IDENTIFIABLE`**

Immutable Run `35167553702` executed the pre-Issue contract frozen at `12f30d5d27d7d4f27022bc355c2a0c62a76e9f0c`. All **18/18** requirements passed without opening any future NPDES or RCRA outcome.

## Frozen design support / 고정 설계 지원

- exact FRS cross-program Registry IDs: **60,677**
- exact one-to-one RCRAInfo↔NPDES Registry IDs: **41,664**
- structurally eligible Registry IDs: **2,170**
- all structural strata: **146**
- strict-separation strata: **24**
- matched HIGH–LOW pairs: **307**
- matched states: **22**
- baseline-evaluation-count balance within `[1/3,3]`: **77.85%**
- permit-age difference <=10 years: **96.74%**
- deterministic manifest SHA-256: `19e1b3a1963fe008811aa230336e12ec69a348b03cf37bd656ea9d3fba8e5aaf`

The final design contains one facility at most once and every pair satisfies `HIGH exposure_eval_count > LOW exposure_eval_count`.

## Outcome firewall / 결과 방화벽

- NPDES effluent-violation rows: **not opened**;
- DMR outcomes: **not opened**;
- RCRA violation/enforcement outcomes: **not opened**;
- 2024 future outcome membership: **not opened**;
- relationship/prediction/causality: **not computed**;
- identity repair: **not used**;
- cost: **0 USD**.

## Exact next action / 정확한 다음 행동

A separate `US-EPA-XMEDIA-E01` authorization may now bind the frozen 307-pair manifest and open only the prospectively frozen primary endpoint: calendar-2024 `E90` occurrence from official `NPDES_EFF_VIOLATIONS.csv`, with the already frozen paired risk-difference and exact McNemar/binomial gate. No endpoint, time window, pair membership or threshold may change after outcome access.

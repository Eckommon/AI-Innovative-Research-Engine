---
id: PORTFOLIO-R33-SCORECARD
type: immutable-mission-roi-scorecard
created: 2026-09-16
issue: 146
contract_decision: DEC-204
contract_commit: 000725296414465206647121607b930625119a24
source_revalidation_commit: ddd37fb2ca4bfc1495009752d19a8ceff5b06b5e
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R33 Immutable Scorecard / 고정 점수표

The candidate/rubric contract was frozen before Issue #146, the Issue was bound before source revalidation, and `SOURCE_REVALIDATION.md` was persisted before this scorecard. No candidate outcome magnitude, exposure-stratified outcome count, coefficient, predictive score or relationship direction was opened while scoring.

## Final frozen scores / 최종 고정점수

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total | Score disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-FTA-TRANSIT-001** | 4 | 3 | 5 | 4 | 4 | 5 | 5 | 4 | 3 | **37/45** | **PROVISIONAL_SELECT_BY_TIEBREAK** |
| US-MSHA-001 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 4 | 0 | **37/45** | HOLD_DIRECT_OVERLAP_TIEBREAK |
| KR-GG-CHEM-001 | 5 | 5 | 5 | 4 | 4 | 5 | 2 | 5 | 1 | **36/45** | HOLD_IDENTITY_AND_OVERLAP |
| US-FRA-XING-001 | 4 | 3 | 5 | 5 | 4 | 5 | 5 | 3 | 0 | **34/45** | HOLD_HIGH_DIRECT_OVERLAP |

## Frozen tie-break application / 동점 규칙 적용

`US-FTA-TRANSIT-001` and `US-MSHA-001` tie at **37/45**.

1. **Next-gate information gain:** FTA 4 = MSHA 4 → still tied.
2. **Low overlap / novelty risk:** FTA **3** > MSHA **0** → **FTA wins here**.

No later tie-break dimension is consulted.

## Scoring basis / 점수 근거

### US-FTA-TRANSIT-001 — 37/45

Carry the R32 structural score after current revalidation confirms the source remains executable:

- Mission 4: mechanical reliability and major transit safety events are material public-transport operations/safety issues, though less acute than some catastrophic-safety branches.
- Cross-source 3: Breakdowns and Safety & Security are distinct NTD products but remain within one FTA reporting program.
- Direct outcome 5: Major Safety Events are concrete event outcomes.
- Independent-unit 4: agency × mode supports repeated national units, but Full Reporter and TOS/reporting-scope reconciliation must be frozen prospectively.
- Practical 4: potential value for asset/reliability planning and safety prioritization, subject to agency/mode aggregation limits.
- Zero-cost 5: current FTA/DOT products expose direct CSV/Excel/open-data access at no incremental cost.
- Join 5: source-native agency/mode fields are highly defensible; no fuzzy entity resolution is needed.
- Next-info 4: one F01 can settle current multi-year Breakdown continuity, TOS aggregation, reporter-scope compatibility, exact agency/mode overlap and fingerprints before any event occurrence is opened.
- Low-overlap 3: reliability/safety are conceptually related and not novel as themes, but current revalidation did not establish a clearly identical nationwide prospective Breakdown-structure → subsequent Major Safety Event design. This is not a novelty proof.

### US-MSHA-001 — 37/45

- Mission 5: mine injury prevention is a direct occupational-safety bottleneck.
- Cross-source 3: inspections/violations and accident/injury files are distinct but remain within MSHA's own reporting/enforcement ecosystem.
- Direct outcome 5: reported mine accidents/injuries are concrete outcomes.
- Independent-unit 5: source-native Mine ID provides a strong repeated worksite unit at national scale.
- Practical 5: meaningful for mine safety surveillance/prevention.
- Zero-cost 5: direct complete-replacement ZIP/TXT files are current, public and operationally simple.
- Join 5: Mine ID and Event Number are explicit native keys.
- Next-info 4: one F01 can cheaply freeze actual field schemas, mine/time support, inspection→violation linkage and prospective temporal units.
- Low-overlap 0: directly similar published research already predicts subsequent injuries from MSHA violations/enforcement and longitudinally relates mine-level regulatory adherence measures to injury rates. MSHA's own targeting also uses compliance and accident history. R33 therefore cannot award novelty credit merely because the source structure is excellent.

### KR-GG-CHEM-001 — 36/45

Carry the prior score unchanged. Cross-source mission value remains meaningful, but no stable shared native business identifier is established and fuzzy/geospatial repair is unauthorized. Direct Korean chemical-enterprise risk/accident literature remains substantial.

### US-FRA-XING-001 — 34/45

- Mission 4: grade-crossing safety is important, but the frozen relationship family is already mature.
- Cross-source 3: inventory and incident files are distinct FRA products within one reporting ecosystem.
- Direct outcome 5: crossing accidents/incidents are direct safety outcomes.
- Independent-unit 5: U.S. DOT Crossing ID is an excellent repeated native unit.
- Practical 4: potentially useful for crossing prioritization.
- Zero-cost 5: current FRA safety platform publishes full historical/current inventory and incident datasets.
- Join 5: exact native U.S. DOT Crossing ID is highly defensible.
- Next-info 3: structural feasibility is already strongly documented, so another source-only F01 removes less uncertainty than FTA/MSHA.
- Low-overlap 0: recent nationwide crossing-risk/severity research already combines FRA inventory/history with accident data. The frozen relationship family therefore has little discovery-space advantage.

## Immutable selection consequence / 고정 선정결과

The sole score/tie-break provisional selection is:

**`SELECT_US_FTA_TRANSIT_001_BREAKDOWNS_TO_MAJOR_SAFETY_F01`**

This is not automatic promotion of the R32 runner-up. FTA was re-entered into a newly frozen four-candidate competition, revalidated against current sources, tied a fresh technically stronger MSHA branch on total score, and won only on the prospectively frozen low-overlap/novelty tie-break.

R33 may authorize only a separate outcome-blind `US-FTA-TRANSIT-F01` after atomic terminalization and State Integrity. F01 must verify source access, exact agency/mode/TOS/reporting-scope semantics, time support, aggregate structural overlap and fingerprints before any breakdown-conditioned Major Safety Event occurrence is opened.

This scorecard must not be revised based on downstream support or eventual safety outcomes.

Incremental monetary cost remains **0 USD**.

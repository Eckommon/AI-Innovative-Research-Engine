---
id: PORTFOLIO-R30
issue: 140
state: ACTIVE_FROZEN_SCORECARD_RATIFICATION
created: 2026-09-16
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R30 — fresh-domain reselection after terminal C-EU-F01

## Purpose / 목적

Return to Stage 0 after terminal `C-EU-F01 = HOLD_C_EU_F01_SOURCE_OR_IDENTITY`. Do **not** automatically promote the sole preserved R29 runner-up (`US-PIPE-001`). Reconstruct a competitive pool by preserving US-PIPE and adding two independently sourced fresh-domain candidates before scoring.

No candidate outcome magnitude or candidate-specific relationship is opened in R30.

## Frozen provenance and process note / provenance·절차 기록

Candidate/rule/source facts were durably frozen before scoring:
- candidate/rule contract commit `faf01cbe5a114f69bf96fdafa075521aa619662b`;
- source revalidation commit `540f27da69d109a6b731b3d41d02eb5a99c29252`.

The scorecard was committed at `e848a6c77920aa7e31eb1e1038e4f9914cbc6b7e` before Issue #140 was bound. This ordering nonconformity is durably recorded in `PROCESS_NONCONFORMITY.md`. It is not outcome leakage: the pool, rubric, tie-break and source evidence were fixed first and no candidate outcome was opened. Issue #140 freezes the existing scorecard; **no rescoring is permitted** merely to repair the orchestration order.

## Frozen candidate pool / 고정 후보군

Exactly three candidates are scored in R30:

1. **US-PIPE-001 — hydrologic stress → pipeline incidents**
   - preserved unexecuted candidate from R29;
   - PHMSA accident/incident and annual pipeline mileage data are public;
   - unrestricted national NPMS line GIS may not be assumed for the general public;
   - strong direct literature/domain overlap remains a penalty.

2. **US-FDA-MD-001 — medical-device manufacturing inspection classification → subsequent recall incidence**
   - baseline family: FDA final inspection classification (`NAI` / `VAI` / `OAI`) for CDRH/device manufacturing facilities;
   - prospective outcome family: later FDA medical-device recall event at the same exact facility identity;
   - FDA FEI is the prospective exact facility key; FDA's current CDRH reliance guidance explicitly instructs users to search device manufacturing facilities by FEI, and openFDA Device Recall exposes native `firm_fei_number`;
   - FDA warns that the public Inspection Classification Database is **not comprehensive**, so any descendant must be framed only within the publicly disclosed inspected-facility cohort and may not claim population-wide manufacturer incidence or causal effects;
   - current literature/source search found inspection-outcome studies and case-specific inspection/recall examples but did not establish a near-identical FEI-level public-data prospective inspection-classification → later recall design. This is only an overlap screen, not a novelty proof.

3. **US-CMS-NH-001 — nursing-home staffing instability → subsequent health deficiencies**
   - baseline family: CMS Payroll-Based Journal daily nurse staffing;
   - outcome family: later CMS Health Deficiencies citations;
   - exact facility key: CMS Certification Number (`CCN`);
   - both sources are public/free and expose time identities;
   - peer-reviewed work has already merged PBJ with Care Compare/deficiency outcomes and directly tested staffing instability against deficiency citations, creating high overlap/diminishing-return risk.

## Frozen scoring frame / 고정 평가틀

Reuse the established R26–R29 Mission-ROI rubric, 0–5 each, total /45:
1. Mission bottleneck
2. Cross-source value
3. Direct outcome
4. Independent-unit prospect
5. Practical value
6. Zero-cost operability
7. Join defensibility
8. Next-gate information gain
9. Low overlap / novelty risk

## Frozen scorecard / 고정 점수

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **US-FDA-MD-001 inspection classification → later device recall** | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 3 | **41** |
| US-CMS-NH-001 staffing instability → later health deficiencies | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** |
| US-PIPE-001 hydrologic stress → incident | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 0 | **36** |

Provisional selection frozen for ratification: **`SELECT_US_FDA_MD_001_INSPECTION_TO_RECALL_F01`**. No tie-break is required.

## Frozen tie-break / 고정 동점규칙

1. Total score
2. Next-gate information gain
3. Low overlap / novelty risk
4. Join defensibility
5. Direct outcome
6. Still tied → fail closed.

## Exact next action / 정확한 다음 행동

Ratify this immutable scorecard under Issue #140 without rescoring, persist the R30 terminal selection atomically, close Issue #140, pass State Integrity, and only then open a separate `US-FDA-MD-F01` outcome-blind source/schema/identity gate. No inspection-classification→recall effect test is authorized by R30.

Incremental monetary cost remains **0 USD**.


## Final disposition / 최종 처분

Issue #140 ratifies the immutable scorecard without rescoring. **`SELECT_US_FDA_MD_001_INSPECTION_TO_RECALL_F01`** is selected at **41/45**, ahead of US-CMS-NH-001 at 37/45 and US-PIPE-001 at 36/45. The pre-Issue scorecard ordering nonconformity remains durably recorded; no candidate outcome was opened.

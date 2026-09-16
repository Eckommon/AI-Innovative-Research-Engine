---
id: PORTFOLIO-R30
state: PREPARED_AWAITING_ISSUE_BINDING
created: 2026-09-16
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R30 — fresh-domain reselection after terminal C-EU-F01

## Purpose / 목적

Return to Stage 0 after terminal `C-EU-F01 = HOLD_C_EU_F01_SOURCE_OR_IDENTITY`. Do **not** automatically promote the sole preserved R29 runner-up (`US-PIPE-001`). Reconstruct a competitive pool by preserving US-PIPE and adding two independently sourced fresh-domain candidates before scoring.

No candidate outcome magnitude or candidate-specific relationship is opened in R30.

## Frozen candidate pool / 고정 후보군

Exactly three candidates may be scored in R30:

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
   - however, peer-reviewed work has already merged PBJ with Care Compare/deficiency outcomes and directly tested staffing instability against deficiency citations, creating high overlap/diminishing-return risk.

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

Scores are portfolio-control judgments, not empirical findings.

## Frozen interpretation rules / 고정 해석 규칙

- `Join defensibility` scores exact deterministic identity and source accessibility, not whether the eventual relationship is causal.
- `Independent-unit prospect` must penalize obvious repeated-unit/pseudoreplication or severe selection structure if a prospective design cannot readily control it.
- `Next-gate information gain` scores how much one **outcome-blind F01** can remove current uncertainty, not the attractiveness of a hoped-for positive result.
- `Low overlap / novelty risk` is an overlap penalty only; absence of a found near-identical paper is not proof of novelty.
- A non-comprehensive public database may still support a bounded cohort question if the cohort definition is explicit and no population-wide denominator is claimed.
- No candidate may receive an effect score based on opening outcome magnitudes during R30.

## Frozen tie-break / 고정 동점규칙

1. Total score
2. Next-gate information gain
3. Low overlap / novelty risk
4. Join defensibility
5. Direct outcome
6. If still tied, fail closed and do not select until a new prospective discriminator is registered.

## Source basis / source 근거

### US-FDA-MD-001
- FDA Inspection Classification Database: https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-classification-database
- FDA Inspections Data Dashboard: https://datadashboard.fda.gov/oii/cd/inspections.htm
- FDA CDRH Regulatory Reliance Portal: https://www.fda.gov/medical-devices/cdrh-international-affairs/cdrh-regulatory-reliance-portal-medical-devices
- openFDA Device Recall searchable fields: https://open.fda.gov/apis/device/recall/searchable-fields/

### US-CMS-NH-001
- CMS PBJ Daily Nurse Staffing: https://data.cms.gov/quality-of-care/payroll-based-journal-daily-nurse-staffing
- CMS Health Deficiencies: https://data.cms.gov/provider-data/dataset/r5ix-sfxw

### US-PIPE-001
Use the official PHMSA/NPMS source-access facts already frozen in PORTFOLIO-R29 / Issue #138; R30 does not reopen or relax the restricted-geometry finding.

## Exact next action / 정확한 다음 행동

Bind this contract to a dedicated R30 Issue, score exactly the three frozen candidates without opening candidate outcomes, select exactly one winner under the frozen tie-break, persist the result atomically, close R30, pass State Integrity, and only then open the winner's separate outcome-blind F01.

Incremental monetary cost remains **0 USD**.

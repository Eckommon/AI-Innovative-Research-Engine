---
id: PORTFOLIO-R30-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-16
issue: 140
state: COMPLETED_SELECT
selected_candidate: US-FDA-MD-001
selected_gate: US-FDA-MD-F01
candidate_outcomes_opened: false
process_nonconformity_recorded: true
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R30 Result — Select US-FDA-MD-001 F01

**`SELECT_US_FDA_MD_001_INSPECTION_TO_RECALL_F01`**

R30 returns to Stage 0 after terminal C-EU-F01 and deliberately avoids automatic promotion of US-PIPE. It compares one preserved unexecuted candidate with two fresh-domain candidates. No candidate outcome magnitude or candidate-specific relationship was opened.

## Frozen final scorecard / 최종 고정 점수

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-FDA-MD-001 inspection classification → later device recall** | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 3 | **41** | **SELECT_STAGE0_F01_ONLY** |
| US-CMS-NH-001 staffing instability → later health deficiencies | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** | HOLD_HIGH_DIRECT_OVERLAP |
| US-PIPE-001 hydrologic stress → incident | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 0 | **36** | HOLD_RESTRICTED_GEOMETRY_AND_OVERLAP |

US-FDA-MD-001 leads outright at **41/45**; no tie-break is required.

## Why FDA leads / FDA 선정 근거

FDA's current public architecture supports a potentially exact establishment-level path that remains outcome-blind at the next gate:

`publicly disclosed CDRH/device inspection → exact FEI → later device-recall FEI identity`.

The value is not a claim that OAI/VAI causes recalls. The next information question is whether the public inspection download actually exposes a stable FEI/project-area/date/classification schema and whether that exact FEI has sufficient structural overlap with Device Recall `firm_fei_number` before any recall incidence by inspection class is opened.

The public Inspection Classification Database is explicitly non-comprehensive, so a descendant is bounded to the publicly disclosed inspected-facility cohort only. It may not estimate population-wide manufacturer recall risk or interpret inspection selection causally.

## Preserved alternatives / 보존 후보

- `US-CMS-NH-001` remains technically executable, but current peer-reviewed work already directly analyzes PBJ staffing instability against deficiency citations, so marginal information/novelty value is low.
- `US-PIPE-001` remains unexecuted, but unrestricted national line geometry still cannot be assumed and direct domain overlap remains high.

## Process nonconformity / 절차 비적합

The candidate pool, rubric, tie-break and source revalidation were durably frozen before scoring, but the scorecard commit `e848a6c77920aa7e31eb1e1038e4f9914cbc6b7e` preceded Issue #140 binding. This is recorded in `PROCESS_NONCONFORMITY.md` and Issue #140.

No candidate outcome magnitude was opened, no score was outcome-driven, and R30 does **not** rescore after Issue binding. Future portfolio rounds must bind the Issue after the candidate/rule contract and before scorecard persistence.

## Authorization boundary / 승인 경계

R30 authorizes only a separate `US-FDA-MD-F01` outcome-blind source/schema/identity feasibility gate. F01 must prospectively verify, before recall incidence by inspection class is opened:

- actual current zero-cost FDA entire-inspections dataset download route;
- FEI field presence/type and exact identity cardinality;
- inspection end date and final NAI/VAI/OAI classification route;
- a defensible CDRH/device manufacturing/project-area filter using source semantics only;
- duplicate project-area / repeated-inspection structure;
- openFDA Device Recall `firm_fei_number` and event-date identity support;
- exact FEI overlap and temporal support only, without counting or comparing recall incidence by classification;
- explicit bounded-cohort and non-causal claim boundary.

No effect test is authorized.

Incremental monetary cost remains **0 USD**.

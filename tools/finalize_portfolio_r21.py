#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; DATE='2026-09-12'
status=ROOT/'STATUS.md'; handoff=ROOT/'context/SESSION_HANDOFF.md'; checkpoint=ROOT/'context/checkpoint.json'
claims=ROOT/'registry/CLAIM_LEDGER.md'; decisions=ROOT/'registry/DECISION_LOG.md'
clm=ROOT/'registry/CLM-157.md'; d160=ROOT/'registry/DEC-160.md'; d161=ROOT/'registry/DEC-161.md'
r21=ROOT/'research/PORTFOLIO-R21'; n01=ROOT/'research/US-WW-N01'; r21.mkdir(parents=True,exist_ok=True); n01.mkdir(parents=True,exist_ok=True)
s=status.read_text(encoding='utf-8'); assert 'active_issue: none' in s and 'last_decision: DEC-159' in s
for p in (clm,d160,d161,r21/'RESULT.md',n01/'README.md'): assert not p.exists(),p

(r21/'RESULT.md').write_text('''---
id: PORTFOLIO-R21-RESULT
type: stage0-portfolio-reselection
created: 2026-09-12
issue: 115
state: COMPLETED_SELECT
selected_candidate: US-WW-N01
selected_issue: 116
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R21 Result

**`SELECT_US_WW_N01_INCIDENT_COMPLIANCE_DESIGN_IDENTIFIABILITY`**

US-WW-N01 is selected at **42/45**. US-WW-F01 removed most source/join risk, but leakage/reverse-direction risk remains material, so the branch advances only to an outcome-blind design-identifiability gate rather than an effect test.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-WW-N01 leakage-controlled incident-compliance design** | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | **42** | **SELECT** |
| US-RCRA-001 hazard → hazardous-waste compliance | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 2 | **39** | HOLD_READY |
| US-MINE-001 operational stress → mine injuries | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 3 | 2 | **38** | HOLD_OVERLAP |
| US-UTIL AMI × storm × reliability | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 1 | **38** | HOLD_HIGH_OVERLAP |
| US-PIPE-001 hydrologic stress → pipeline incidents | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** | HOLD_DIRECT_OVERLAP |

Current screening found adjacent work combining CWNS with ICIS/NPDES for wastewater characterization, nutrients and effluent research, but no near-identical design was found that prospectively uses 2022 structural need-category identities to predict **incident post-baseline** NPDES compliance records with explicit pre-existing-compliance leakage control. This is an overlap screen, not a novelty proof.

No future compliance outcome magnitude was opened. Cost: **0 USD**.
''',encoding='utf-8')

(n01/'README.md').write_text('''---
id: US-WW-N01
issue: 116
state: ACTIVE_OUTCOME_BLIND_DESIGN_IDENTIFIABILITY
selection_decision: DEC-160
authorization_decision: DEC-161
future_outcome_magnitudes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-WW-N01 — Leakage-Controlled Incident Compliance Design Identifiability

Canonical contract is Issue #116. N01 may inspect CWNS need-category membership, `REASON_FOR_NEEDS` text identities, official NPDES linkage, pre-2022 violation identity availability and structural/cardinality support. It must not report 2023–2025 future-window violation counts/rates, exposed-vs-comparator outcome prevalence or relationship statistics.

PASS does not authorize an effect test. Cost: **0 USD**.
''',encoding='utf-8')

clm.write_text('''---
id: CLM-157
type: claim
created: 2026-09-12
issue: 115
status: active
---

# CLM-157 — US-WW has enough identity structure to test leakage-controlled incident-design identifiability without opening future outcomes

US-WW-F01 established a high-coverage CWNS→NPDES→ICIS bridge, and the CWNS national schema separately exposes need-category membership plus `REASON_FOR_NEEDS`. ICIS violation tables expose historical date/type identities. Together these sources support an outcome-blind gate that can test whether pre-existing-compliance leakage can be controlled before any 2023–2025 outcome magnitude is opened.

This is a design-prospect claim only, not predictive or causal evidence. Cost: **0 USD**.
''',encoding='utf-8')

d160.write_text('''---
id: DEC-160
type: decision
created: 2026-09-12
issue: 115
status: accepted
---

# DEC-160 — PORTFOLIO-R21 selects US-WW-N01 at 42/45

Select US-WW-N01 for the next bounded gate. The F01 exact-join PASS materially reduces source risk, while N01 directly tests the remaining high-risk question: whether an incident-compliance design can be frozen without leakage from pre-existing compliance problems.

Do not open future compliance outcomes. Cost: **0 USD**.
''',encoding='utf-8')

d161.write_text('''---
id: DEC-161
type: decision
created: 2026-09-12
issue: 116
status: accepted
---

# DEC-161 — Authorize US-WW-N01 outcome-blind leakage-control gate

Authorize Issue #116 exactly as written. N01 may inspect exposure/category membership, `NEED_REASON` identities, baseline 2019–2021 violation-record identity support, permit/facility linkage and structural cardinalities. It must not open or report any 2023–2025 future-window compliance outcome magnitude or relationship.

PASS cannot authorize E01 automatically. Cost remains **0 USD**.
''',encoding='utf-8')

cl=claims.read_text(encoding='utf-8'); assert '`CLM-157`' not in cl
claims.write_text(cl.rstrip()+'''\n\n| `CLM-157` | Proven CWNS→NPDES→ICIS identities plus CWNS need-category/REASON_FOR_NEEDS and ICIS historical violation identities support an outcome-blind leakage-control design gate before future outcomes. / 미래 outcome을 열기 전 leakage-control 설계 식별 gate가 가능하다. | `OBSERVED/DERIVED` | `V2/V3_MIXED_DESIGN_GATE` | US-WW-F01; Issue #115/#116; EPA CWNS/ICIS source semantics | 2026-09-12 | active |\n''',encoding='utf-8')
dl=decisions.read_text(encoding='utf-8'); assert '`DEC-160`' not in dl and '`DEC-161`' not in dl
decisions.write_text(dl.rstrip()+'''\n\n| `DEC-160` | 2026-09-12 | PORTFOLIO-R21 selects US-WW-N01 at 42/45. | F01 removed source/join risk; leakage-control identifiability is now the highest-value bounded question. | Issue #115; `CLM-157`; `research/PORTFOLIO-R21/RESULT.md` | active |\n| `DEC-161` | 2026-09-12 | Authorize Issue #116 outcome-blind leakage-control design gate only. | Future compliance outcomes remain blocked until leakage/baseline/comparator rules are frozen. | Issue #116; `research/US-WW-N01/README.md` | active |\n''',encoding='utf-8')

status.write_text('''---
checkpoint_id: CHK-20260912-US-WW-N01-ACTIVE
active_issue: 116
active_research: US-WW-N01
last_completed_issue: 115
last_completed_research: PORTFOLIO-R21
last_decision: DEC-161
updated: 2026-09-12
---

# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R21_SELECTED_US_WW_N01__US_WW_N01_ACTIVE`

PORTFOLIO-R21 selected US-WW-N01 at 42/45. The active gate is outcome-blind design identifiability with explicit pre-existing-compliance leakage control. No 2023–2025 future compliance outcome magnitude or relationship is authorized.

## Exact next action

Execute Issue #116. Inspect CWNS need-category membership and `REASON_FOR_NEEDS` labels, baseline 2019–2021 ICIS violation identity support, exposed/comparator structural cardinality and fixed leakage-control rules. Do not open future-window outcome counts/rates.

Incremental monetary cost remains **0 USD**.
''',encoding='utf-8')
handoff.write_text('''---
checkpoint_id: CHK-20260912-US-WW-N01-ACTIVE
active_issue: 116
active_research: US-WW-N01
last_completed_issue: 115
last_completed_research: PORTFOLIO-R21
last_decision: DEC-161
updated: 2026-09-12
---

# Session Handoff / 세션 인수인계

PORTFOLIO-R21 selected US-WW-N01 at 42/45. Exact restart: execute Issue #116 outcome-blind. Freeze leakage handling from `REASON_FOR_NEEDS`, baseline 2019–2021 compliance identity support, exposure/comparator membership and missingness rules. Do not open 2023–2025 future compliance outcomes. Cost: **0 USD**.
''',encoding='utf-8')
checkpoint.write_text(json.dumps({'checkpoint_id':'CHK-20260912-US-WW-N01-ACTIVE','active_issue':116,'active_research':'US-WW-N01','last_completed_issue':115,'last_completed_research':'PORTFOLIO-R21','last_decision':'DEC-161','updated':DATE},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'selected':'US-WW-N01','score':42,'active_issue':116,'cost_usd':0}))

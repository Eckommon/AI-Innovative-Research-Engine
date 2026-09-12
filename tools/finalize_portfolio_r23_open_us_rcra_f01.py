#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-13"
status_path = ROOT / "STATUS.md"
handoff_path = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_path = ROOT / "context" / "checkpoint.json"
claim_ledger_path = ROOT / "registry" / "CLAIM_LEDGER.md"
decision_log_path = ROOT / "registry" / "DECISION_LOG.md"
claim_path = ROOT / "registry" / "CLM-161.md"
dec166_path = ROOT / "registry" / "DEC-166.md"
dec167_path = ROOT / "registry" / "DEC-167.md"
r23_dir = ROOT / "research" / "PORTFOLIO-R23"
f01_dir = ROOT / "research" / "US-RCRA-F01"
r23_dir.mkdir(parents=True, exist_ok=True)
f01_dir.mkdir(parents=True, exist_ok=True)

status = status_path.read_text(encoding="utf-8")
assert "active_issue: none" in status
assert "last_completed_issue: 119" in status
assert "last_completed_research: US-WW-E01" in status
assert "last_decision: DEC-165" in status
for p in (claim_path, dec166_path, dec167_path, r23_dir / "RESULT.md", f01_dir / "README.md"):
    assert not p.exists(), f"already exists: {p}"

(r23_dir / "RESULT.md").write_text("""---
id: PORTFOLIO-R23-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-13
issue: 120
state: COMPLETED_SELECT
selected_candidate: US-RCRA-F01
selected_gate: US-RCRA-F01
next_issue: 121
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R23 Result — Select US-RCRA-F01

**`SELECT_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_FEASIBILITY`**

After terminal US-WW-E01, do not rescue that branch. Select the independent US-RCRA branch for one outcome-blind source/join/time feasibility gate. No disaster-linked compliance outcome was opened during selection.

## Mission-ROI comparison

0–5 each; /45. Scores are portfolio-control judgments, not empirical findings.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-RCRA-F01 hazard × compliance feasibility** | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 3 | **40** | **SELECT** |
| US-MINE-001 operational stress → injury | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 3 | 2 | **38** | HOLD_OVERLAP |
| US-UTIL post-F02 descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 2 | **38** | HOLD_HIGH_OVERLAP |
| US-PIPE-001 hydrologic stress → incident | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** | HOLD_DIRECT_OVERLAP |
| C-EU-004 industrial site climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE |

## Why US-RCRA leads now

Current EPA data expose a prospectively deterministic identity chain before values:

`RCRAInfo.ID_NUMBER` → ECHO RCRA facility `SOURCE_ID` → `RCR_FIPS_CODE` (5-digit county FIPS) → FEMA county disaster/time identity → RCRA evaluation/violation temporal identity.

This avoids fuzzy facility names and avoids post-hoc spatial repair. RCRAInfo is a national program system with facility, evaluation, violation and monthly violation/SNC identities; FEMA OpenFEMA publishes official county-coded disaster declarations with incident dates.

The overlap penalty is material: EPA and GAO already evaluate natural-hazard vulnerability/exposure of RCRA facilities. Therefore this project does **not** claim novelty for static hazard mapping. The only potentially distinct descendant is a later, separately preregistered temporal relationship to subsequent compliance identity, and F01 does not authorize it.

## Exact next action

Execute Issue #121 outcome-blind. Verify source access, exact RCRA-ID→ECHO county-FIPS linkage, operating-TSDF cardinality/geographic support, FEMA county/time coverage, and RCRA evaluation/violation temporal identity. Do not compute disaster-linked facility violation rates/counts or any relationship.

Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

claim_path.write_text("""---
id: CLM-161
type: claim
created: 2026-09-13
issue: 120
status: active
---

# CLM-161 — Current official EPA/FEMA sources expose a prospective exact RCRA facility → county disaster → compliance identity route

EPA RCRAInfo provides deterministic handler IDs and evaluation/violation temporal identities. EPA's public ECHO RCRA facility GIS layer exposes source IDs plus five-digit county FIPS, and FEMA OpenFEMA publishes county-coded disaster declarations with incident dates. These source semantics support an outcome-blind exact join feasibility test without fuzzy facility names or disaster-linked outcome screening.

EPA/GAO already cover RCRA natural-hazard vulnerability/exposure, so this is a source-route claim only and does not establish novelty, temporal-effect feasibility, predictive value, or causality. Cost: **0 USD**.
""", encoding="utf-8")

dec166_path.write_text("""---
id: DEC-166
type: decision
created: 2026-09-13
issue: 120
status: accepted
---

# DEC-166 — PORTFOLIO-R23 selects US-RCRA-F01 at 40/45

Select `US-RCRA-F01` at **40/45** after terminal US-WW-E01. The branch has high public-safety relevance, direct compliance identities, official zero-cost source routes, and a newly verified exact county-FIPS bridge. Keep a material overlap penalty because EPA/GAO already study natural-hazard vulnerability at RCRA facilities.

Selection opens no disaster-linked compliance outcome and does not authorize an effect test.
""", encoding="utf-8")

dec167_path.write_text("""---
id: DEC-167
type: decision
created: 2026-09-13
issue: 121
status: accepted
---

# DEC-167 — Authorize US-RCRA-F01 outcome-blind source/join/time gate

Authorize Issue #121 exactly as written. Inspect only official-source access, file/table/header identities, handler/universe label domains, deterministic RCRA IDs, ECHO GIS source IDs and county FIPS, FEMA disaster/county/time identities, evaluation/violation temporal schema, and row/distinct/cardinality support.

Do not compute disaster-linked violation/evaluation rates, post-disaster outcome counts, facility rankings, coefficients or relationships. PASS/PARTIAL cannot authorize an effect test. Cost remains **0 USD**.
""", encoding="utf-8")

(f01_dir / "README.md").write_text("""---
id: US-RCRA-F01
issue: 121
state: ACTIVE_SOURCE_JOIN_FEASIBILITY
selection_decision: DEC-166
authorization_decision: DEC-167
relationship_computed: false
disaster_linked_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# US-RCRA-F01 — RCRA Facility × County Disaster × Compliance Identity Feasibility

Canonical contract is Issue #121.

The gate is source/schema/identity/cardinality only. It must establish the exact public route `RCRAInfo.ID_NUMBER → ECHO SOURCE_ID → RCR_FIPS_CODE → FEMA county/time identity` and modern RCRA evaluation/violation temporal support for the operating-TSDF universe. No fuzzy facility/county matching and no disaster-linked compliance outcome aggregation is allowed.

PASS/PARTIAL requires a separate Stage-0/N01 design gate before any temporal relationship can be tested. Cost: **0 USD**.
""", encoding="utf-8")

status_path.write_text("""---
checkpoint_id: CHK-20260913-US-RCRA-F01-ACTIVE
active_issue: 121
active_research: US-RCRA-F01
last_completed_issue: 120
last_completed_research: PORTFOLIO-R23
last_decision: DEC-167
updated: 2026-09-13
---

# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R23_SELECTED_US_RCRA_F01__US_RCRA_F01_ACTIVE`

After terminal US-WW-E01, PORTFOLIO-R23 selected **US-RCRA-F01** at **40/45**. Issue #121 is the only active research gate. No disaster-linked RCRA compliance outcome has been opened.

## Exact next action / 정확한 다음 행동

Execute Issue #121 outcome-blind. Prove the operating-TSDF source universe, exact RCRA-ID→ECHO county-FIPS coverage, FEMA county/time overlap, and RCRA compliance temporal identity. Do not compute a disaster→compliance relationship.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_path.write_text("""---
checkpoint_id: CHK-20260913-US-RCRA-F01-ACTIVE
active_issue: 121
active_research: US-RCRA-F01
last_completed_issue: 120
last_completed_research: PORTFOLIO-R23
last_decision: DEC-167
updated: 2026-09-13
---

# Session Handoff / 세션 인수인계

PORTFOLIO-R23 selected US-RCRA-F01 at 40/45 after terminal US-WW-E01. EPA/GAO static natural-hazard vulnerability work is explicitly treated as overlap; do not claim novelty for hazard mapping.

Exact restart: Issue #121 only. Establish outcome-blind exact `RCRAInfo.ID_NUMBER → ECHO SOURCE_ID → RCR_FIPS_CODE → FEMA county disaster/time` support plus RCRA evaluation/violation temporal schema/cardinality. No disaster-linked compliance rates/counts or relationship statistics. Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_path.write_text(json.dumps({
    "checkpoint_id": "CHK-20260913-US-RCRA-F01-ACTIVE",
    "active_issue": 121,
    "active_research": "US-RCRA-F01",
    "last_completed_issue": 120,
    "last_completed_research": "PORTFOLIO-R23",
    "last_decision": "DEC-167",
    "updated": DATE,
}, indent=2) + "\n", encoding="utf-8")

cl = claim_ledger_path.read_text(encoding="utf-8")
assert "`CLM-161`" not in cl
claim_ledger_path.write_text(cl.rstrip() + """

| `CLM-161` | Current official EPA/FEMA sources expose a prospective exact RCRAInfo handler → ECHO county-FIPS → FEMA county/time → RCRA compliance-identity route without fuzzy matching or outcome screening. / RCRA 시설-재해-규제 식별 route가 값 비사용으로 검증 가능하다. | `OBSERVED/DERIVED` | `V2_CURRENT_OFFICIAL_SOURCE_ROUTE` | EPA RCRAInfo/ECHO RCRA GIS; FEMA OpenFEMA; PORTFOLIO-R23 | 2026-09-13 | active |
""", encoding="utf-8")

dl = decision_log_path.read_text(encoding="utf-8")
assert "`DEC-166`" not in dl and "`DEC-167`" not in dl
decision_log_path.write_text(dl.rstrip() + """

| `DEC-166` | 2026-09-13 | PORTFOLIO-R23 selects US-RCRA-F01 at 40/45 after terminal US-WW-E01. / 독립 US-RCRA source/join gate 선정. | High public-safety/direct-outcome value plus exact county-FIPS route; retain overlap penalty for existing EPA/GAO hazard-vulnerability work. | Issue #120; `CLM-161`; `research/PORTFOLIO-R23/RESULT.md` | active |
| `DEC-167` | 2026-09-13 | Authorize Issue #121 outcome-blind US-RCRA source/join/time feasibility only. / 재해-linked outcome 비개방 F01 승인. | Must prove operating-TSDF identity, exact county join and temporal compliance support before any relationship design. | Issue #121; `research/US-RCRA-F01/README.md` | active |
""", encoding="utf-8")

print(json.dumps({"selection":"US-RCRA-F01","score":40,"active_issue":121,"outcomes_opened":False,"cost_usd":0}))

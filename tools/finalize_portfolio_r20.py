#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-12"

status_path = ROOT / "STATUS.md"
handoff_path = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_path = ROOT / "context" / "checkpoint.json"
claim_ledger_path = ROOT / "registry" / "CLAIM_LEDGER.md"
decision_log_path = ROOT / "registry" / "DECISION_LOG.md"
claim_path = ROOT / "registry" / "CLM-154.md"
dec155_path = ROOT / "registry" / "DEC-155.md"
dec156_path = ROOT / "registry" / "DEC-156.md"
r20_dir = ROOT / "research" / "PORTFOLIO-R20"
f01_dir = ROOT / "research" / "US-UTIL-F01"
r20_dir.mkdir(parents=True, exist_ok=True)
f01_dir.mkdir(parents=True, exist_ok=True)

status = status_path.read_text(encoding="utf-8")
assert "active_issue: none" in status
assert "last_completed_issue: 110" in status
assert "last_decision: DEC-154" in status
for p in (claim_path, dec155_path, dec156_path, r20_dir / "RESULT.md", f01_dir / "README.md"):
    assert not p.exists(), f"already exists: {p}"

(r20_dir / "RESULT.md").write_text("""---
id: PORTFOLIO-R20-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-12
issue: 111
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: US-UTIL
selected_gate: US-UTIL-F01
next_issue: 112
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R20 Result — Independent-Branch Reselection
# PORTFOLIO-R20 결과 — 독립 branch 재선정

## Final selection / 최종 선정

**`SELECT_US_UTIL_AMI_STORM_RELIABILITY_F01`**

Advance only to Issue #112 `US-UTIL-F01`, an outcome-blind source/schema/identity/cardinality gate. No AMI, reliability or storm magnitude relationship is authorized.

## New source-route evidence / 새 source-route 근거

Current official-source review materially improves the route compared with earlier R19 scoring:
- Form EIA-861 is an annual census of U.S. electric utilities;
- final annual detailed ZIPs are available for 2020–2024;
- the annual files explicitly include Advanced Metering, Reliability and Service Territory schedules;
- Service Territory identifies counties/states in which each utility distributes electricity;
- NOAA/NCEI Storm Events exposes public annual bulk CSVs.

This creates a prospectively testable utility-year → utility-county → storm county-year identity route before any numeric AMI count, SAIDI/SAIFI value or storm severity is opened.

## Mission-ROI comparison / 목적-ROI 비교

0–5 each; /45. Portfolio-control judgment, not empirical evidence.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-UTIL AMI × Storm × Reliability F01** | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 1 | **39** | **SELECT** |
| CA-GRAIN grain_week-keyed new descendant | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 2 | 0 | **36** | HOLD_DIMINISHING_RETURN |
| EU-GRID separate source-route redesign | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 3 | 3 | **36** | HOLD_SOURCE_ROUTE_FRICTION |
| US freight-rail × weather | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **36** | HOLD_DIRECT_2026_OVERLAP |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE_JOIN_ASSET |

## Portfolio interpretation / 포트폴리오 해석

CA-GRAIN retains a technically viable official `grain_week` identity route, but F01 PASS followed by E01 and E02 terminal HOLDs materially lowers marginal information value. R20 therefore does not immediately create E03. US-UTIL is preferred as the strongest independent branch despite a real literature/overlap penalty, because the exact utility-county join route has not yet been structurally tested in this portfolio.

## Exact next action / 정확한 다음 행동

Execute Issue #112 outcome-blind. Verify EIA 2020–2024 Advanced Metering, Reliability and Service Territory identities plus NOAA 2020–2024 Storm Events identities. Persist only provenance/schema/cardinality/boolean support. Do not read or persist AMI counts, SAIDI/SAIFI/CAIDI values, storm damage/severity magnitudes, or compute any relationship.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

claim_path.write_text("""---
id: CLM-154
type: claim
created: 2026-09-12
issue: 111
status: active
---

# CLM-154 — EIA-861 exposes a prospective utility-county identity bridge for AMI × storm × reliability

Official EIA documentation states that Form EIA-861 annual detailed data include Advanced Metering, Reliability and Service Territory schedules, and that Service Territory identifies counties and states in which each utility distributes electricity. NOAA/NCEI separately publishes annual Storm Events bulk CSV data.

Those source families support a prospective **utility-year → utility-county → county-year** join-identifiability test without opening AMI counts, reliability metrics or storm severity. This is a source-route claim only; it does not establish feasibility, association, causality, novelty or effect. Cost: **0 USD**.
""", encoding="utf-8")

dec155_path.write_text("""---
id: DEC-155
type: decision
created: 2026-09-12
issue: 111
status: accepted
---

# DEC-155 — PORTFOLIO-R20 selects US-UTIL-F01 at 39/45

Select `US-UTIL AMI × Storm × Reliability` for an outcome-blind source/join feasibility gate at **39/45**. CA-GRAIN is not immediately continued because accumulated terminal gates and external overlap reduce marginal information value even though a separate grain_week-keyed descendant remains conceptually possible.

US-UTIL retains a novelty/overlap penalty. R20 authorizes only structural source/schema/identity/cardinality testing, not an effect study.
""", encoding="utf-8")

dec156_path.write_text("""---
id: DEC-156
type: decision
created: 2026-09-12
issue: 112
status: accepted
---

# DEC-156 — Authorize US-UTIL-F01 outcome-blind feasibility gate

Authorize Issue #112 exactly as written. Freeze EIA-861 final annual data for 2020–2024 and NOAA Storm Events details for 2020–2024. Inspect only source access, file/sheet/schema identities, utility/state/county/year identities, row/distinct counts and nonblank-support booleans.

Do not open or persist AMI meter counts, SAIDI/SAIFI/CAIDI values, customer/sales/energy values, storm magnitude/damage/injury/fatality values, or any relationship. PASS/PARTIAL cannot authorize an effect test. Cost remains **0 USD**.
""", encoding="utf-8")

(f01_dir / "README.md").write_text("""---
id: US-UTIL-F01
issue: 112
state: ACTIVE_SOURCE_JOIN_FEASIBILITY
mission_anchor: MEM-054
portfolio_decision: DEC-155
authorization_decision: DEC-156
relationship_computed: false
magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# US-UTIL-F01 — EIA-861 × NOAA Storm Utility-County Join Feasibility

Canonical contract is Issue #112.

Frozen source years: **2020–2024**. EIA schedule families: Advanced Metering, Reliability, Service Territory. NOAA source family: annual Storm Events details bulk CSV.

F01 is strictly outcome-blind: source access, archive/sheet/schema identity, utility/state/county/year identity, cardinality and nonblank-support only. No AMI, reliability or storm severity/damage magnitude may be analyzed or persisted. No relationship is authorized. Cost: **0 USD**.
""", encoding="utf-8")

status_path.write_text("""---
checkpoint_id: CHK-20260912-US-UTIL-F01-ACTIVE
active_issue: 112
active_research: US-UTIL-F01
last_completed_issue: 111
last_completed_research: PORTFOLIO-R20
last_decision: DEC-156
updated: 2026-09-12
---

# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R20_SELECTED_US_UTIL__US_UTIL_F01_ACTIVE`

PORTFOLIO-R20 selected US-UTIL AMI × Storm × Reliability for an outcome-blind source/join feasibility gate at **39/45**. Current official-source evidence identifies a zero-cost route through EIA-861 Advanced Metering, Reliability and Service Territory schedules plus NOAA Storm Events annual bulk data.

## Exact next action / 정확한 다음 행동

Execute Issue #112. Validate 2020–2024 source access, schedule/schema identities, EIA utility-year AMI∩Reliability identity support, service-territory utility×county support and NOAA county-year identities. Persist no candidate magnitudes and compute no relationship.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_path.write_text("""---
checkpoint_id: CHK-20260912-US-UTIL-F01-ACTIVE
active_issue: 112
active_research: US-UTIL-F01
last_completed_issue: 111
last_completed_research: PORTFOLIO-R20
last_decision: DEC-156
updated: 2026-09-12
---

# Session Handoff / 세션 인수인계

PORTFOLIO-R20 selected **US-UTIL-F01 / Issue #112** at 39/45 after CA-GRAIN-E02 terminal HOLD. CA-GRAIN is not repaired or immediately continued.

Execute the exact outcome-blind source/join gate: EIA-861 final 2020–2024 Advanced Metering + Reliability + Service Territory and NOAA Storm Events details 2020–2024. Test deterministic utility/year/state/county identity and cardinality support only. Never read/persist AMI counts, SAIDI/SAIFI/CAIDI values or storm severity/damage magnitudes. PASS/PARTIAL does not authorize an effect test.

Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_path.write_text(json.dumps({
    "checkpoint_id": "CHK-20260912-US-UTIL-F01-ACTIVE",
    "active_issue": 112,
    "active_research": "US-UTIL-F01",
    "last_completed_issue": 111,
    "last_completed_research": "PORTFOLIO-R20",
    "last_decision": "DEC-156",
    "updated": DATE,
}, indent=2) + "\n", encoding="utf-8")

cl = claim_ledger_path.read_text(encoding="utf-8")
assert "`CLM-154`" not in cl
claim_ledger_path.write_text(cl.rstrip() + """

| `CLM-154` | EIA-861 Advanced Metering, Reliability and Service Territory plus NOAA Storm Events expose a prospective utility-year → utility-county → county-year identity bridge without opening magnitudes. / US-UTIL source-route 구조 후보가 공식 source에서 식별된다. | `OBSERVED/DERIVED` | `V2_PRIMARY_OFFICIAL_SOURCE_ROUTE` | EIA-861 official documentation; NOAA/NCEI Storm Events bulk access; PORTFOLIO-R20 | 2026-09-12 | active |
""", encoding="utf-8")

dl = decision_log_path.read_text(encoding="utf-8")
assert "`DEC-155`" not in dl and "`DEC-156`" not in dl
decision_log_path.write_text(dl.rstrip() + """

| `DEC-155` | 2026-09-12 | R20 selects US-UTIL-F01 at 39/45; defer further CA-GRAIN descendants due diminishing return. / R20 US-UTIL-F01 선정. | Strong independent zero-cost source route with utility-county join; effect overlap remains penalized. | Issue #111; `CLM-154`; `research/PORTFOLIO-R20/RESULT.md` | active |
| `DEC-156` | 2026-09-12 | Authorize Issue #112 outcome-blind source/schema/identity/cardinality gate only. / US-UTIL-F01 값 비사용 feasibility 승인. | Prevent effect leakage before join operability is proven. | Issue #112; `research/US-UTIL-F01/README.md` | active |
""", encoding="utf-8")

print(json.dumps({"selection":"US-UTIL-F01","score":39,"issue":112,"cost_usd":0}))

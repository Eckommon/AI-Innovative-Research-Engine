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
claim_path = ROOT / "registry" / "CLM-150.md"
dec149_path = ROOT / "registry" / "DEC-149.md"
dec150_path = ROOT / "registry" / "DEC-150.md"
r18_dir = ROOT / "research" / "PORTFOLIO-R18"
e01_dir = ROOT / "research" / "CA-GRAIN-E01"
r18_dir.mkdir(parents=True, exist_ok=True)
e01_dir.mkdir(parents=True, exist_ok=True)

status = status_path.read_text(encoding="utf-8")
assert "active_issue: none" in status
assert "last_completed_issue: 106" in status
assert "last_decision: DEC-148" in status
for p in (claim_path, dec149_path, dec150_path, r18_dir / "RESULT.md", e01_dir / "README.md"):
    assert not p.exists(), f"already exists: {p}"

r18_result = """---
id: PORTFOLIO-R18-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-12
issue: 107
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-CA-002
selected_gate: CA-GRAIN-E01-STAGE-A
next_issue: 108
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R18 Result — Post-CA-GRAIN-F01 PASS Effect-Stage Reselection
# PORTFOLIO-R18 결과 — CA-GRAIN-F01 PASS 이후 효과단계 재선정

## Final selection / 최종 선정

**`SELECT_C_CA_002_CA_GRAIN_E01_STAGE_A_DESIGN_IDENTIFIABILITY`**

Advance only to Issue #108 `CA-GRAIN-E01 Stage A`. Do **not** open grain-volume or dwell-time magnitudes.

## Current external-overlap refresh / 최신 중복 위험

Current official and monitoring products materially reduce novelty for any naive grain-volume → dwell analysis:

- Statistics Canada/Transport Canada publish weekly grain-transport and rail-system performance indicators, including grain service and dwell-related measures.
- Statistics Canada's Grain Supply Chain Dashboard already brings grain movement and 48-hour dwell information into one operational monitoring surface using multiple data sources.
- The federal Grain Monitoring Program (Quorum) publishes current weekly/monthly operational measures and long-run open-data/reporting assets; its research program also studies rail performance effects.
- The 2025 Transportation in Canada annual report explicitly discusses record grain shipments as rail-demand pressure alongside origin-dwell performance.

Therefore C-CA-002 does **not** receive novelty credit merely for combining grain and dwell data. Its remaining bounded information value is narrower: whether a prospectively fixed **upstream producer-delivery pressure**, one-week lag, and first-difference carrier-panel design can be identified and later tested without post-value choices.

US freight-rail × weather is further penalized because a 2026 Journal of Public Economics study already estimates weather effects on U.S. railway safety/performance and delay propagation at scale. US-UTIL remains technically strong but also has mature AMI/reliability overlap, including prior causal work linking AMI rollouts to SAIDI/SAIFI.

## Mission-ROI comparison / 목적-ROI 비교

0–5 each; /45. Portfolio-control judgment, not an empirical finding.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **C-CA-002 CA-GRAIN-E01 Stage A** | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 2 | **41** | **SELECT** |
| US-UTIL AMI × Storm × Reliability descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 1 | **38** | HOLD_READY_HIGH_OVERLAP |
| EU-GRID separate source-route redesign | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 3 | 3 | **36** | HOLD_SOURCE_ROUTE_FRICTION |
| US freight-rail × weather | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **36** | HOLD_DIRECT_2026_OVERLAP |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE_JOIN_ASSET |

## Why Stage A, not Stage B / 왜 효과값이 아닌 Stage A인가

F01 established 104 Transport Canada weekly keys, 2 carriers and 81 common explicit-date GSW week keys. It did not establish which GSW textual metric is the scientifically preferred **upstream pressure** exposure. Opening values before fixing that identity would create a material researcher-degree-of-freedom problem.

Issue #108 therefore freezes causal ordering and the Stage B skeleton prospectively, then permits only textual/schema/nonblank support inspection. The preferred exposure family is current-week producer/primary-elevator deliveries, lagged one week into Canada-level `All Western grain` origin dwell for exactly `CN` and `CPKC`. If exact source identities are ambiguous, Stage A fails closed rather than selecting by numeric fit.

## Exact next gate / 정확한 다음 gate

Execute Issue #108 Stage A only. Inspect GSW worksheet/metric/period/grain/region identities and Transport Canada frozen outcome identity/support without reading magnitudes. Classify PASS or HOLD. Stage A PASS still requires a separate adjudication before any Stage B values are opened.

Incremental monetary cost remains **0 USD**.
"""
(r18_dir / "RESULT.md").write_text(r18_result, encoding="utf-8")

claim_path.write_text("""---
id: CLM-150
type: claim
created: 2026-09-12
issue: 107
status: active
---

# CLM-150 — C-CA-002 remains testable, but novelty requires a narrower prospective design

CA-GRAIN-F01 established a reproducible zero-cost weekly source/join route, but current official/monitoring products already combine or jointly discuss grain movement and rail dwell/performance. A naive grain-volume → dwell relationship therefore carries substantial overlap risk.

The remaining bounded information gain is to determine outcome-blind whether GSW exposes one scientifically preferred **upstream producer/primary-elevator delivery-pressure identity** that can be frozen before values, then paired with the already fixed Canada-level `All Western grain` origin-dwell outcome for `CN` and `CPKC` under a one-week-lag first-difference design.

This claim establishes neither novelty nor a relationship. It only justifies the Stage A identifiability gate. Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

dec149_path.write_text("""---
id: DEC-149
type: decision
created: 2026-09-12
issue: 107
status: accepted
---

# DEC-149 — PORTFOLIO-R18 selects CA-GRAIN-E01 Stage A at 41/45

Select `C-CA-002 CA-GRAIN-E01 Stage A` at **41/45**. F01 source/join PASS gives this branch the highest immediate marginal information value, but current Grain Monitor / Statistics Canada overlap prevents automatic effect exposure and materially reduces the novelty score.

Advance only to outcome-blind exposure/outcome design identifiability. Do not claim novelty from co-locating grain and dwell series and do not open magnitudes during R18 or Stage A.
""", encoding="utf-8")

dec150_path.write_text("""---
id: DEC-150
type: decision
created: 2026-09-12
issue: 108
status: accepted
---

# DEC-150 — Authorize CA-GRAIN-E01 Stage A only

Authorize Issue #108 exactly as written for outcome-blind schema/textual-identity/panel-support adjudication. Freeze the causal direction as upstream GSW producer/primary-elevator delivery pressure in week `t-1` → Transport Canada Canada-level `All Western grain` origin dwell in week `t`, carriers exactly `CN` and `CPKC`.

Stage A may inspect only textual identities, explicit date/week keys, row/distinct counts and nonblank-presence booleans. Grain-volume and dwell-time magnitudes, correlations and regressions remain prohibited. A Stage A PASS does not authorize Stage B; separate adjudication is mandatory.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

(e01_dir / "README.md").write_text("""---
id: CA-GRAIN-E01
issue: 108
state: ACTIVE_STAGE_A_DESIGN_IDENTIFIABILITY
mission_anchor: MEM-054
portfolio_decision: DEC-149
authorization_decision: DEC-150
relationship_computed: false
magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# CA-GRAIN-E01 — Upstream Grain-Delivery Pressure × Origin Dwell
# CA-GRAIN-E01 — 상류 곡물 유입압력 × 출발지 대기시간

Canonical contract is Issue #108. Only **Stage A outcome-blind design identifiability** is authorized.

Frozen direction: GSW current-week producer/primary-elevator delivery pressure at `t-1` → Transport Canada `All Western grain` / `Average Dwell Time at Origin` / `Canada` for exactly `CN` and `CPKC` at `t`.

Stage A may persist textual/schema identities, explicit week/date keys, counts and nonblank-presence booleans only. No source magnitudes and no relationship/effect computation.

Possible Stage A dispositions:
- `PASS_CA_GRAIN_E01_STAGE_A_DESIGN_IDENTIFIABLE`
- `HOLD_CA_GRAIN_E01_EXPOSURE_IDENTITY_AMBIGUOUS`
- `HOLD_CA_GRAIN_E01_PANEL_SUPPORT`
- `HOLD_CA_GRAIN_E01_NOVELTY_OVERLAP`

Stage B remains blocked pending separate adjudication even after a Stage A PASS. Cost: **0 USD**.
""", encoding="utf-8")

status_path.write_text("""---
checkpoint_id: CHK-20260912-CA-GRAIN-E01-STAGE-A-ACTIVE
active_issue: 108
active_research: CA-GRAIN-E01-STAGE-A
last_completed_issue: 107
last_completed_research: PORTFOLIO-R18
last_decision: DEC-150
updated: 2026-09-12
---

# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R18_SELECTED_C_CA_002__CA_GRAIN_E01_STAGE_A_ACTIVE`

PORTFOLIO-R18 selected CA-GRAIN-E01 Stage A at 41/45. F01 established the weekly source/join route, but current monitoring overlap makes naive grain-volume → dwell analysis insufficiently differentiated. Only outcome-blind exposure/outcome design identifiability is active; no grain-volume or dwell-time magnitude may be opened.

## Exact next action / 정확한 다음 행동

Execute Issue #108 Stage A: identify one deterministic upstream GSW delivery-pressure metric/period/grain/region identity and verify the frozen Transport Canada `CN`/`CPKC` Canada-level outcome support on >=80 common weeks. Fail closed on exposure ambiguity. Stage B remains blocked after PASS until separate adjudication.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_path.write_text("""---
checkpoint_id: CHK-20260912-CA-GRAIN-E01-STAGE-A-ACTIVE
active_issue: 108
active_research: CA-GRAIN-E01-STAGE-A
last_completed_issue: 107
last_completed_research: PORTFOLIO-R18
last_decision: DEC-150
updated: 2026-09-12
---

# Session Handoff / 세션 인수인계

PORTFOLIO-R18 selected Issue #108 `CA-GRAIN-E01 Stage A` at **41/45**. Current Grain Monitor / Statistics Canada products create material overlap for simple grain-volume × dwell co-movement, so no effect values are authorized yet.

Execute only outcome-blind design identifiability. Freeze one GSW current-week producer/primary-elevator delivery-pressure identity under the Issue #108 hierarchy; outcome is Transport Canada `All Western grain` × `Average Dwell Time at Origin` × `Canada`, carriers exactly `CN` and `CPKC`. Primary timing skeleton is one-week lag; planned Stage B uses first weekly differences and week-clustered inference, but Stage B is blocked until separate adjudication.

No grain-volume or dwell-time magnitude may be persisted or analyzed in Stage A. Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

checkpoint_path.write_text(json.dumps({
    "checkpoint_id": "CHK-20260912-CA-GRAIN-E01-STAGE-A-ACTIVE",
    "active_issue": 108,
    "active_research": "CA-GRAIN-E01-STAGE-A",
    "last_completed_issue": 107,
    "last_completed_research": "PORTFOLIO-R18",
    "last_decision": "DEC-150",
    "updated": DATE,
}, indent=2) + "\n", encoding="utf-8")

claim_ledger = claim_ledger_path.read_text(encoding="utf-8")
assert "`CLM-150`" not in claim_ledger
claim_ledger_path.write_text(claim_ledger.rstrip() + """

| `CLM-150` | CA-GRAIN weekly source/join is feasible, but current official/Grain Monitor products create substantial overlap for naive grain-volume × dwell analysis; a narrower upstream-delivery one-week-lag design requires outcome-blind identity fixation first. / 단순 grain×dwell 중복 위험으로 Stage A 설계식별이 선행되어야 한다. | `OBSERVED/DERIVED` | `V2_CURRENT_OVERLAP_VERIFIED` | PORTFOLIO-R18 current-source/literature refresh; `research/PORTFOLIO-R18/RESULT.md` | 2026-09-12 | active |
""", encoding="utf-8")

decision_log = decision_log_path.read_text(encoding="utf-8")
assert "`DEC-149`" not in decision_log and "`DEC-150`" not in decision_log
decision_log_path.write_text(decision_log.rstrip() + """

| `DEC-149` | 2026-09-12 | R18 selects CA-GRAIN-E01 Stage A design identifiability at 41/45; no automatic effect exposure. / R18에서 CA-GRAIN-E01 Stage A 선정. | F01 source/join PASS raises information value, while monitoring overlap requires narrower preregistered design. | Issue #107; `CLM-150`; `research/PORTFOLIO-R18/RESULT.md` | active |
| `DEC-150` | 2026-09-12 | Authorize only outcome-blind CA-GRAIN-E01 Stage A under Issue #108; Stage B remains blocked. / E01 Stage A 값 비사용 식별만 승인. | Fix upstream exposure identity, one-week lag and exact carrier/outcome support before values. | Issue #108; `research/CA-GRAIN-E01/README.md` | active |
""", encoding="utf-8")

print(json.dumps({"selection":"CA-GRAIN-E01-STAGE-A","score":41,"issue":108,"cost_usd":0}))

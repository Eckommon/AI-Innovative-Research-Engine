#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / 'registry'
R = ROOT / 'research'

status = (ROOT / 'STATUS.md').read_text(encoding='utf-8')
assert 'EU_GRID_F01_HOLD__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE' in status
assert 'CLM-148' not in (REG / 'CLAIM_LEDGER.md').read_text(encoding='utf-8')
assert 'DEC-146' not in (REG / 'DECISION_LOG.md').read_text(encoding='utf-8')
assert 'DEC-147' not in (REG / 'DECISION_LOG.md').read_text(encoding='utf-8')

p = R / 'PORTFOLIO-R17'
p.mkdir(parents=True, exist_ok=True)
(p / 'RESULT.md').write_text('''---
id: PORTFOLIO-R17-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-12
issue: 105
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-CA-002
selected_gate: CA-GRAIN-F01
next_issue: 106
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R17 Result — Post-EU-GRID-F01 HOLD Reselection
# PORTFOLIO-R17 결과 — EU-GRID-F01 HOLD 이후 재선정

## Final selection / 최종 선정

**`SELECT_C_CA_002_GRAIN_PRESSURE_RAIL_DWELL_SOURCE_JOIN_FEASIBILITY`**

Selected next gate: **Issue #106 `CA-GRAIN-F01` — outcome-blind weekly grain-pressure × rail-dwell source/join feasibility.**

No grain-volume, dwell-time, utility-reliability, weather or relationship magnitude was opened during R17.

## Mission-ROI comparison / 목적-ROI 비교

0–5 each; /45. Portfolio-control judgment, not an empirical finding.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **C-CA-002 Grain Pressure × Rail Dwell redesign** | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 3 | **40** | **SELECT** |
| US-UTIL AMI × Storm × Reliability descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 1 | **38** | HOLD_READY_HIGH_OVERLAP |
| US-FREIGHT-RAIL Weather × Terminal Dwell | 4 | 5 | 5 | 4 | 5 | 5 | 3 | 4 | 1 | **36** | HOLD_HIGH_OVERLAP |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE_JOIN_ASSET |
| EU-GRID source-route redesign | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 3 | 3 | **36** | HOLD_SEPARATE_REDESIGN_ONLY |

## Current source / overlap refresh / 최신 source·중복 확인

- Transport Canada / Statistics Canada continue to expose weekly rail performance data with full-table CSV/SDMX downloads and commodity/terminal/origin-dwell identities. The post-2023 Transportation Data and Information Hub exposes a full-data download and expanded geography/commodity dimensions.
- Canadian Grain Commission Grain Statistics Weekly exposes open current and archived crop-year CSVs; the frozen 2023-24 and 2024-25 crop years are available.
- External-overlap risk is real: Canada's Grain Monitoring Program already monitors the prairie grain handling and transportation system. Therefore R17 does not claim novelty or open an effect test; the next question is narrower — whether an independent, deterministic weekly cross-source panel exists under a preregistered source/join contract.
- The fresh U.S. freight-rail weather alternative is technically attractive, but 2026 literature already studies weather effects on U.S. railway performance and delay propagation, sharply reducing marginal novelty.
- EU-GRID-F01 remains terminal under its frozen no-login public-page route; no post hoc repair is allowed inside F01.

## Exact next gate / 정확한 다음 gate

Execute **CA-GRAIN-F01 only**. Verify source download, schema/category identity, frozen crop-year support, weekly calendar semantics, carrier identity and prospective weekly join cardinality. Reduce any numeric field encountered for support checking immediately to booleans/counts; persist no grain-volume or dwell-time magnitudes and compute no relationship.

Incremental monetary cost remains **0 USD**.
''', encoding='utf-8')

(REG / 'CLM-148.md').write_text('''---
id: CLM-148
type: claim
created: 2026-09-12
issue: 105
status: active
---

# CLM-148 — C-CA-002 has a bounded zero-cost weekly source/join gate

Current official-source verification supports a bounded outcome-blind feasibility gate for `C-CA-002`: Transport Canada / Statistics Canada expose weekly rail performance datasets with commodity, carrier, date and dwell-related identities and downloadable data, while the Canadian Grain Commission publishes open Grain Statistics Weekly crop-year CSVs including the frozen 2023-24 and 2024-25 files.

This claim establishes only that source/schema/week-join feasibility is testable at 0 USD. It does not establish a grain-pressure/dwell relationship, independent novelty, or an effect-test authorization. Grain Monitoring Program overlap remains a material novelty risk.
''', encoding='utf-8')

(REG / 'DEC-146.md').write_text('''---
id: DEC-146
type: decision
created: 2026-09-12
issue: 105
status: accepted
---

# DEC-146 — PORTFOLIO-R17 selects C-CA-002 source/join feasibility

Select `C-CA-002 Grain Pressure × Rail Dwell redesign` at **40/45** and advance only to Issue #106 `CA-GRAIN-F01`.

Rationale: after EU-GRID-F01's terminal source/identity HOLD, C-CA-002 has the strongest remaining combination of direct public outcome identity, cross-source weekly exposure support, zero-cost operability and next-gate information gain. Its overlap with Canada's existing Grain Monitoring Program is explicitly penalized; therefore only source/join feasibility is authorized, not a relationship test.
''', encoding='utf-8')

(REG / 'DEC-147.md').write_text('''---
id: DEC-147
type: decision
created: 2026-09-12
issue: 106
status: accepted
---

# DEC-147 — Authorize CA-GRAIN-F01 outcome-blind weekly source/join feasibility

Authorize Issue #106 exactly as written. Freeze the Transport Canada weekly rail-performance source family, Canadian Grain Commission Grain Statistics Weekly crop years 2023-24 and 2024-25, and the common structural interval 2023-08-01 through 2025-07-31.

F01 may inspect access, hashes, archive/schema/header labels, textual identities, dates/week semantics, row/distinct counts, nonblank-presence booleans and prospective weekly join cardinality only. It may not persist grain-volume or dwell-time magnitudes or estimate any relationship. PASS/PARTIAL remains feasibility only.
''', encoding='utf-8')

claim_ledger = REG / 'CLAIM_LEDGER.md'
with claim_ledger.open('a', encoding='utf-8') as f:
    f.write('\n| `CLM-148` | Transport Canada weekly rail-performance and Canadian Grain Commission GSW sources make a bounded zero-cost C-CA-002 weekly source/join gate testable; novelty/effect remain unestablished. / 캐나다 grain-rail weekly source/join feasibility를 무비용으로 검증 가능. | `OBSERVED/DERIVED` | `V2_PRIMARY_VERIFIED` | PORTFOLIO-R17 current-source refresh; official TC/StatCan/CGC pages | 2026-09-12 | active |\n')

decision_log = REG / 'DECISION_LOG.md'
with decision_log.open('a', encoding='utf-8') as f:
    f.write('\n| `DEC-146` | 2026-09-12 | R17 selects C-CA-002 Grain Pressure × Rail Dwell source/join feasibility at 40/45. / R17에서 C-CA-002 source/join feasibility 선정. | Highest remaining marginal information value after EU-GRID-F01 terminal HOLD, with overlap explicitly penalized. | Issue #105; `CLM-148`; `research/PORTFOLIO-R17/RESULT.md` | active |\n')
    f.write('| `DEC-147` | 2026-09-12 | Authorize outcome-blind `CA-GRAIN-F01` using TC weekly rail data × CGC GSW 2023-24/2024-25 source/join metadata only. / CA-GRAIN-F01 값 비사용 feasibility 승인. | Prevent value exposure before weekly source/schema/join semantics are reproducible. | Issue #106; `research/CA-GRAIN-F01/README.md` | active |\n')

cg = R / 'CA-GRAIN-F01'
cg.mkdir(parents=True, exist_ok=True)
(cg / 'README.md').write_text('''---
id: CA-GRAIN-F01
issue: 106
state: ACTIVE_SOURCE_JOIN_FEASIBILITY
mission_anchor: MEM-054
portfolio_decision: DEC-146
authorization_decision: DEC-147
relationship_computed: false
magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# CA-GRAIN-F01 — Weekly Grain-Pressure × Rail-Dwell Source/Join Feasibility
# CA-GRAIN-F01 — 주간 곡물압력 × 철도대기 source/join 타당성

Canonical contract is Issue #106. Frozen source families are Transport Canada weekly rail performance and Canadian Grain Commission Grain Statistics Weekly crop years `2023-24` and `2024-25`; structural interval `2023-08-01` through `2025-07-31`.

F01 is outcome-blind. Only access/provenance, hashes/byte counts, archive/schema/header labels, textual source identities, dates/week semantics, row/distinct counts, nonblank-presence booleans and prospective weekly join cardinality may be persisted. Grain-volume and dwell-time magnitudes are prohibited.

Possible gates:
- `PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE`
- `PARTIAL_CA_GRAIN_F01_SOURCE_READY_JOIN_SEMANTICS_PENDING`
- `HOLD_CA_GRAIN_F01_SOURCE_OR_IDENTITY_SUPPORT`

Incremental monetary cost: **0 USD**.
''', encoding='utf-8')

(ROOT / 'STATUS.md').write_text('''---
checkpoint_id: CHK-20260912-CA-GRAIN-F01-ACTIVE
active_issue: 106
active_research: CA-GRAIN-F01
last_completed_issue: 105
last_completed_research: PORTFOLIO-R17
last_decision: DEC-147
updated: 2026-09-12
---

# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R17_SELECTED_C_CA_002__CA_GRAIN_F01_ACTIVE`

PORTFOLIO-R17 selected C-CA-002 at 40/45. Only outcome-blind CA-GRAIN-F01 source/schema/week-join feasibility is active. No grain-volume, dwell-time or relationship magnitude may be opened.

## Exact next action / 정확한 다음 행동

Execute Issue #106 for Transport Canada weekly rail-performance source identity and CGC GSW 2023-24/2024-25 schema/week support. Classify PASS/PARTIAL/HOLD without analyzing values.

Incremental monetary cost remains **0 USD**.
''', encoding='utf-8')

(ROOT / 'context' / 'SESSION_HANDOFF.md').write_text('''---
checkpoint_id: CHK-20260912-CA-GRAIN-F01-ACTIVE
active_issue: 106
active_research: CA-GRAIN-F01
last_completed_issue: 105
last_completed_research: PORTFOLIO-R17
last_decision: DEC-147
updated: 2026-09-12
---

# Session Handoff / 세션 인수인계

PORTFOLIO-R17 selected `C-CA-002 Grain Pressure × Rail Dwell` at 40/45 after EU-GRID-F01 terminated at its source/identity HOLD. Issue #106 `CA-GRAIN-F01` is the only active research gate.

Freeze Transport Canada weekly rail-performance data plus Canadian Grain Commission Grain Statistics Weekly crop years 2023-24 and 2024-25, structural interval 2023-08-01 through 2025-07-31. Inspect source/schema/textual identities/week semantics/nonblank booleans/join cardinality only. Persist no grain-volume or dwell-time magnitudes; compute no relationship.

Incremental monetary cost: **0 USD**.
''', encoding='utf-8')

(ROOT / 'context' / 'checkpoint.json').write_text(json.dumps({
    'checkpoint_id': 'CHK-20260912-CA-GRAIN-F01-ACTIVE',
    'active_issue': 106,
    'active_research': 'CA-GRAIN-F01',
    'last_completed_issue': 105,
    'last_completed_research': 'PORTFOLIO-R17',
    'last_decision': 'DEC-147',
    'updated': '2026-09-12'
}, indent=2) + '\n', encoding='utf-8')

print(json.dumps({'selection':'C-CA-002','score':40,'next_issue':106,'cost_usd':0}))

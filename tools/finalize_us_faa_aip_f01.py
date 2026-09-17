#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
STAGING_COMMIT = "e194c692251f867fd378d052f2ccb51001ada1a4"
DECISION = "DEC-221"
GATE = "HOLD_US_FAA_AIP_F01_EXACT_AIRPORT_TIME_JOIN_NOT_READY"

staging_path = ROOT / "research/US-FAA-AIP-F01/STAGING_RESULT.json"
x = json.loads(staging_path.read_text(encoding="utf-8"))
assert x["gate"] == GATE
assert x["scientific_disposition"] == "HOLD"
assert x["requirements_total"] == 17
assert x["requirements_passed"] == 16
req = {int(r["number"]): r for r in x["requirements"]}
assert req[13]["pass"] is False
assert abs(float(x["diagnostics"]["state_concordance_rate"]) - 0.9606425702811245) < 1e-15
assert int(x["diagnostics"]["exact_bridged_airports"]) == 1196
assert int(x["diagnostics"]["bridged_in_ontime_universe"]) == 390
assert int(x["diagnostics"]["bridged_multi_aip_year"]) == 1146
assert int(x["diagnostics"]["exclusions"]["state_conflict"]) == 49
assert x["incremental_monetary_cost_usd"] == 0
for k, v in x["boundaries"].items():
    assert v is False, (k, v)

result = f'''---
id: US-FAA-AIP-F01-RESULT
type: structural-feasibility-result
created: 2026-09-17
issue: 154
research: US-FAA-AIP-F01
disposition: HOLD
staging_commit: {STAGING_COMMIT}
contract_commit: {x["contract_commit"]}
gate: {GATE}
---

# US-FAA-AIP-F01 Result / 결과

## Terminal disposition / 최종 판정

**`{GATE}`**

The immutable outcome-blind structural run passed **16 of 17** frozen requirements. The only failed requirement was the preregistered state-concordance gate: **1,196 / 1,245 = 96.0643%**, below the frozen **99%** threshold. Exactly **49** state conflicts were excluded without repair.

고정된 17개 요구조건 중 **16개가 PASS**했고, 유일한 실패는 사전등록한 state-concordance gate였습니다. **1,196 / 1,245 = 96.0643%**로 고정 기준 **99%**에 미달했습니다. **49개** state conflict는 수동·퍼지 보정 없이 제외했습니다.

## Structural support retained / 구조적 지지

- official FAA AIP FY2021–2025 files readable: **5 / 5**
- valid AIP rows: **16,691**
- distinct valid AIP LocIDs: **2,314**
- exact bounded FAA↔BTS bridged airports: **1,196**
- bridged airports in BTS on-time identity universe: **390**
- bridged airports appearing in >=2 AIP fiscal years: **1,146**
- bridged airports with FY2023–2025 grant support: **1,134**
- longitudinal BTS identity stability after ambiguity exclusion: **100%**
- potential subsequent-year support through 2026: **390**

These counts do not override the failed frozen state-concordance gate.

## Transport correction provenance / 전송 구현 교정

The first two executions failed before scientific evaluation because FAA pages/assets returned HTTP 403 to the GitHub-hosted runner. No threshold or identity rule changed. The successful immutable run used the same frozen contract and the same official FAA workbook assets with a browser-compatible request profile. This was an implementation-only transport correction, not a scientific rescue.

## Outcome firewall / 결과변수 방화벽

No BTS delay, cancellation, diversion or delay-cause numeric outcome value was opened or aggregated. No relationship, predictive metric, causal claim, airport ranking, project-effectiveness estimate or grant-conditioned delay statistic was computed. No fuzzy/name/address/geospatial/manual identity repair was used.

## Consequence / 후속 조치

`US-FAA-AIP-N01` is **not authorized**. The 99% state-concordance threshold must not be lowered and the 49 conflicts must not be manually rescued after support counts are known. This branch terminates and the project returns to an independent portfolio reselection.

Incremental monetary cost: **0 USD**.
'''
(ROOT / "research/US-FAA-AIP-F01/RESULT.md").write_text(result, encoding="utf-8")

dec = f'''---
id: {DECISION}
type: decision
created: 2026-09-17
issue: 154
research: US-FAA-AIP-F01
status: terminal
---

# {DECISION} — Terminate US-FAA-AIP-F01 at frozen state-concordance HOLD

Finalize `US-FAA-AIP-F01` as **`{GATE}`** from immutable staging commit `{STAGING_COMMIT}`.

The run passed 16/17 gates but state concordance was **96.0643%**, below the prospectively frozen **99%** requirement. Preserve the 49 excluded state conflicts as observed evidence; do not lower the threshold, manually reconcile the conflicts, or authorize `US-FAA-AIP-N01`.

All delay/cancellation/diversion/cause outcomes remained unopened. Return to independent portfolio reselection. Incremental monetary cost remains 0 USD.
'''
(ROOT / f"registry/{DECISION}.md").write_text(dec, encoding="utf-8")

log_path = ROOT / "registry/DECISION_LOG.md"
log = log_path.read_text(encoding="utf-8")
if DECISION not in log:
    row = f'\n| `{DECISION}` | 2026-09-17 | Finalize `US-FAA-AIP-F01` as frozen structural HOLD; prohibit threshold/conflict rescue and do not authorize N01. / `US-FAA-AIP-F01`을 고정 구조 HOLD로 종결하고 threshold/conflict 사후구제 및 N01 승격을 금지. | 16/17 PASS; state concordance 96.0643% < frozen 99%, 49 conflicts excluded. / 16/17 PASS이나 state concordance가 고정 99% 미달, conflict 49개 제외. | Issue #154; `{STAGING_COMMIT}`; `research/US-FAA-AIP-F01/RESULT.md` | active |\n'
    log_path.write_text(log.rstrip() + row, encoding="utf-8")

checkpoint = {
    "checkpoint_id": "CHK-20260917-US-FAA-AIP-F01-TERMINAL",
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": 154,
    "last_completed_research": "US-FAA-AIP-F01",
    "last_decision": DECISION,
    "updated": "2026-09-17",
}
(ROOT / "context/checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")

front = '''---
checkpoint_id: CHK-20260917-US-FAA-AIP-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 154
last_completed_research: US-FAA-AIP-F01
last_decision: DEC-221
updated: 2026-09-17
---
'''
status = front + '''
# Project Status / 프로젝트 상태

**State / 상태:** `US_FAA_AIP_F01_HOLD__PORTFOLIO_RESELECTION_REQUIRED`

US-FAA-AIP-F01 is terminal HOLD: 16/17 frozen gates passed, but state concordance was 96.0643%, below the frozen 99% threshold. Candidate delay outcomes remained unopened. N01 is not authorized.

## Exact next action / 정확한 다음 행동

Start a new independent portfolio reselection. Do not lower the FAA state-concordance threshold or manually rescue the 49 excluded conflicts.

Incremental monetary cost remains **0 USD**.
'''
(ROOT / "STATUS.md").write_text(status, encoding="utf-8")

handoff = front + f'''
# Session Handoff / 세션 인계

## Canonical terminal state

`US_FAA_AIP_F01_HOLD__PORTFOLIO_RESELECTION_REQUIRED`

- Issue #154 completed.
- Frozen contract: `{x["contract_commit"]}`
- Immutable staging: `{STAGING_COMMIT}`
- Result: 16/17 PASS; state concordance **96.0643% < 99%**.
- Exact bridge: 1,196 airports; BTS on-time universe: 390; multi-year AIP: 1,146.
- 49 state conflicts excluded without repair.
- No candidate delay/cancellation/diversion/cause outcome values opened.
- `US-FAA-AIP-N01` not authorized.
- Next: independent portfolio reselection under zero-cost governance.
'''
(ROOT / "context/SESSION_HANDOFF.md").write_text(handoff, encoding="utf-8")

print(GATE)
print("DECISION", DECISION)
print("STAGING_COMMIT", STAGING_COMMIT)

#!/usr/bin/env python3
"""Finalize PORTFOLIO-R14 and activate preregistered US-WATERWAY-E01 Stage A."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-09-11"


def main() -> None:
    cp_path = ROOT / "context" / "checkpoint.json"
    cp = json.loads(cp_path.read_text(encoding="utf-8"))
    if cp.get("last_decision") != "DEC-135":
        raise RuntimeError(f"unexpected prior decision: {cp.get('last_decision')}")
    if str(cp.get("active_issue")).lower() not in {"none", "null"}:
        raise RuntimeError(f"expected Stage-0 restart with no active issue: {cp}")

    r14 = """---
id: PORTFOLIO-R14-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-11
issue: 99
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-US-006
selected_gate: US-WATERWAY-E01-STAGE-A
next_issue: 100
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R14 Result — Post-US-WATERWAY JOIN_READY Reselection
# PORTFOLIO-R14 결과 — US-WATERWAY JOIN_READY 이후 재선정

## Final selection / 최종 선정

**`SELECT_C_US_006_FIRST_PREREGISTERED_RELATIONSHIP_TEST`**

Selected next gate:

**Issue #100 `US-WATERWAY-E01` — preregistered extreme-flow burden × annual lock-delay relationship test, beginning with outcome-blind Stage A panel-support qualification.**

No lock-delay magnitude or hydrology observation value was opened during R14. / R14에서는 지연값·수문값을 열지 않았다.

## Why this wins now / 현재 우선 이유

`US-WATERWAY-F01` established a zero-cost JOIN_READY asset with official USACE annual usage support, 193 historical lock identities, stable public lock geometry, and deterministic lock↔USGS metadata mappings. The next unresolved mission bottleneck is whether that join can survive a dependence-aware, preregistered first relationship test rather than merely exist structurally.

The branch is not treated as novel by default. A 2019 Upper Mississippi spatial-panel study already modeled lock delay against lock/traffic/processing characteristics, and a 2026 USACE/ERDC publication provides AIS-based travel-time statistics between locks and confluences. These raise overlap risk. However, current verification did not identify the same multi-year, cross-lock question using hydrologic-extreme burden as the prespecified exposure. USACE operational reporting also documents high-water navigation disruptions, preserving strong practical relevance. / 선행연구 중복 위험은 존재하지만 동일한 수문극단부담→lock-delay 질문은 확인되지 않아 신규성은 아직 UNKNOWN으로 유지한다.

Shared USGS gages create a pseudoreplication risk. Therefore selection does **not** authorize immediate regression: E01 must first collapse the design to unique gage exposure units and pass a 2016–2025 panel-support gate.

## Mission-ROI comparison / 목적-ROI 비교

0–5 each; total /45. Scores are portfolio-control judgments, not empirical findings.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return / novelty risk | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-WATERWAY first preregistered relationship descendant** | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | **43** | **SELECT_STAGE_A_FIRST** |
| C-EU-001 Cross-National Grid Stress | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 4 | 5 | **39** | HOLD_HIGH_VALUE_OPERABILITY |
| US-UTIL AMI × Storm × Reliability descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 1 | **38** | HOLD_READY_HIGH_OVERLAP |
| C-CA-002 Grain Pressure × Rail Dwell | 5 | 5 | 5 | 3 | 5 | 5 | 3 | 4 | 2 | **37** | HOLD_REDESIGN_GEOGRAPHY |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE_JOIN_ASSET |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| AU-NEM continuation | 5 | 5 | 5 | 2 | 5 | 5 | 4 | 3 | 1 | **35** | NO_AUTO_CONTINUATION |
| US-AIR descendant | 3 | 4 | 4 | 5 | 3 | 5 | 5 | 2 | 0 | **31** | NO_AUTO_CONTINUATION |

## Current overlap/relevance checks / 최신 중복·실무성 확인

- 2019 lock-delay spatial panel: https://doi.org/10.1007/s11067-018-9395-0
- 2026 USACE/ERDC inland-waterway AIS travel-time statistics: https://www.erdc.usace.army.mil/Media/Publication-Notices/Tag/244133/
- 2025 USACE Ohio River high-water lock disruptions: https://www.lrd.usace.army.mil/News/News-Releases/Display/Article/4147020/ohio-river-flooding-disrupts-locking-operations-at-markland-and-mcalpine/

These sources affect portfolio selection only. They do not establish novelty, causality, or a hydrology-delay effect.

## Exact next gate / 정확한 다음 gate

Run only **US-WATERWAY-E01 Stage A**: outcome-blind 2016–2025 source/panel support and unique-gage qualification. Relationship magnitudes remain blocked until every Stage-A acceptance condition passes.

Incremental monetary cost remains **0 USD**.
"""

    dec136 = """---
id: DEC-136
type: decision
created: 2026-09-11
issue: 99
status: accepted
---

# DEC-136 — Select US-WATERWAY first preregistered relationship descendant

Select `US-WATERWAY-E01` as the next mission-ROI gate after F01 JOIN_READY, but authorize only its outcome-blind Stage A source/panel qualification first.

Rationale: the branch now has a reusable cross-source join asset and a direct operational outcome; its next information gain is relationship testing. Existing lock-delay and AIS travel-time literature lowers novelty confidence but does not eliminate the distinct hydrologic-extreme question. Shared-gage pseudoreplication is a material risk, so E01 must operate at unique USGS-gage exposure-unit level before any effect estimate.

No delay/hydrology magnitude is authorized by this decision itself. COST-001 and RAW-001 remain mandatory.
"""

    dec137 = """---
id: DEC-137
type: decision
created: 2026-09-11
issue: 100
status: accepted
---

# DEC-137 — Preregister US-WATERWAY-E01 and require Stage A panel support

Authorize Issue #100 `US-WATERWAY-E01` under the frozen contract in `research/US-WATERWAY-E01/README.md`.

The primary scientific question is whether a greater annual share of daily streamflow observations outside fixed within-gage q10/q90 bounds is associated with higher annual USACE Average Delay after gage and calendar-year fixed effects.

Before any delay magnitude or streamflow observation value is opened, Stage A must establish 2016–2025 structural support, at least 12 unique USGS daily-mean streamflow gages, at least 20 matched locks with all-year Annual Usage support, and at least 120 prospective gage-year cells. Shared gages are one exposure unit.

Stage B is unauthorized unless Stage A passes. Novelty, causality, prediction and decision utility remain unclaimed.
"""

    e01 = """---
id: US-WATERWAY-E01
issue: 100
state: ACTIVE_STAGE_A_PANEL_SUPPORT
mission_anchor: MEM-054
portfolio_decision: DEC-136
preregistration_decision: DEC-137
relationship_computed: false
delay_magnitudes_opened: false
hydrology_values_opened: false
incremental_monetary_cost_usd: 0
---

# US-WATERWAY-E01 — Extreme-Flow Burden × Annual Lock Delay
# US-WATERWAY-E01 — 수문 극단일 부담 × 연간 Lock 지연

## Primary question / 주 질문

Across prospectively qualified **USGS monitoring-location × calendar-year** units, is a larger share of hydrologically extreme daily streamflow associated with higher mean annual lock delay for the deterministically matched lock set?

Observational relationship test only; not causal inference and not advance prediction.

## Stage A — outcome-blind source/panel qualification

Before reading any lock-delay magnitude or hydrology observation value:
- audit calendar years **2016–2025**;
- require USGS Daily streamflow parameter `00060` with daily-mean statistic `00003`;
- require stable deterministic USACE historical/current lock identity;
- inspect only source access, schema, IDs, date/year support, row/nonblank-presence flags and cardinality;
- treat one USGS monitoring location as one exposure cluster even if multiple locks map to it;
- persist the final gage↔lock-set map and exclusions;
- no new fuzzy/manual identity repair beyond aliases already evidenced in official USACE material.

Stage-A PASS requires all:
1. >= **12 unique USGS gages** with metadata covering 2016-01-01 through 2025-12-31 for Daily `00060` / statistic `00003`;
2. >= **20 distinct matched locks** across those gages with Annual Usage support for all 10 years;
3. >= **120 prospective gage-year cells** after structural support checks;
4. zero manual/fuzzy repairs beyond already documented official aliases;
5. incremental monetary cost = 0 USD.

Failure resolves `HOLD_US_WATERWAY_E01_PANEL_SUPPORT` and returns to Stage 0 without opening magnitudes.

## Frozen Stage B estimand — only after Stage A PASS

Primary exposure `E_gy`:
- use USGS daily mean discharge `Q` (`00060`, statistic `00003`);
- compute each qualified gage's q10 and q90 from all usable daily observations in fixed 2016–2025;
- `E_gy = (# usable days where Q < q10_g or Q > q90_g) / usable days in year`;
- no imputation or threshold tuning.

Primary outcome `Y_gy`:
- USACE Annual Usage `Average Delay (minutes)` for every prospectively mapped lock-year;
- aggregate as the **unweighted arithmetic mean across mapped qualified locks** for each gage-year;
- any nonblank numeric delay <0 is a source/semantics HOLD.

Primary model:
`Y_gy = gage FE + calendar-year FE + beta * E_gy + error`

Primary inference:
- unweighted OLS at gage-year unit;
- two-way CR1 clustering by USGS gage and calendar year;
- Student-t reference df = `min(G_gage-1, G_year-1)`;
- no alternate covariance estimator may rescue the primary gate.

Primary directional hypothesis: `beta > 0`.

Materiality floor: a **+10 percentage-point** increase in extreme-flow-day share must imply at least **+5 minutes** annual Average Delay, i.e. `0.10 * beta >= 5`.

Primary PASS requires all:
1. beta > 0;
2. two-sided 95% CI lower > 0;
3. `0.10 * beta >= 5 minutes`.

Terminal primary gates:
- `PASS_US_WATERWAY_E01_POSITIVE_MATERIAL_EXTREME_FLOW_DELAY_ASSOCIATION`
- `DETECTABLE_BUT_SUBMATERIAL_US_WATERWAY_E01`
- `NO_PREREGISTERED_POSITIVE_US_WATERWAY_E01_RELATIONSHIP`
- `HOLD_US_WATERWAY_E01_SOURCE_PANEL_OR_INFERENCE_SUPPORT`

## Prespecified non-gate sensitivities

Only after the primary gate is fixed:
1. high-flow-only share (`Q > q90_g`);
2. low-flow-only share (`Q < q10_g`);
3. leave-one-gage-out coefficient range.

Sensitivities cannot rescue the primary result.

## Prohibited

No predictor substitution, percentile tuning, lag/lead search, river cherry-picking, outcome substitution, lock ranking, causal claim, prediction claim, novelty claim or utility claim inside E01.

Incremental monetary cost remains **0 USD**.
"""

    status = """---
checkpoint_id: CHK-20260911-US-WATERWAY-E01-STAGE-A-ACTIVE
active_issue: 100
active_research: US-WATERWAY-E01
last_completed_issue: 99
last_completed_research: PORTFOLIO-R14
last_decision: DEC-137
updated: 2026-09-11
---

# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R14_SELECTED_US_WATERWAY_E01__STAGE_A_PANEL_SUPPORT_ACTIVE`

PORTFOLIO-R14 selected the first preregistered US-WATERWAY relationship descendant at **43/45**, but only Stage A source/panel support is active. No delay magnitude or hydrology observation value has been opened.

## Exact next action / 정확한 다음 행동

Execute the frozen 2016–2025 outcome-blind Stage A. Require unique-gage exposure units, >=12 qualifying `00060/00003` gages, >=20 all-year matched locks, and >=120 prospective gage-year cells. Only a full Stage-A PASS can authorize Stage B.

Incremental monetary cost remains **0 USD**.
"""

    handoff = """---
checkpoint_id: CHK-20260911-US-WATERWAY-E01-STAGE-A-ACTIVE
active_issue: 100
active_research: US-WATERWAY-E01
last_completed_issue: 99
last_completed_research: PORTFOLIO-R14
last_decision: DEC-137
updated: 2026-09-11
---

# Session Handoff / 세션 인수인계

## Canonical restart point / 정확한 재개점

PORTFOLIO-R14 / Issue #99 selected `US-WATERWAY-E01`; Issue #100 is the sole active research gate.

Execute **Stage A only** before any outcome/exposure magnitude:
1. extend USGS metadata support to 2016–2025 for Daily `00060`, statistic `00003`;
2. confirm deterministic historical/current lock identity and all-year Annual Usage structural support;
3. collapse shared gages to one exposure unit and persist gage↔lock-set mapping;
4. PASS only if >=12 unique gages, >=20 all-year locks and >=120 prospective gage-year cells;
5. otherwise HOLD and return Stage 0.

Do not inspect Average Delay magnitudes or streamflow observations during Stage A. Cost remains 0 USD.
"""

    (ROOT / "research" / "PORTFOLIO-R14").mkdir(parents=True, exist_ok=True)
    (ROOT / "research" / "US-WATERWAY-E01").mkdir(parents=True, exist_ok=True)
    (ROOT / "research" / "PORTFOLIO-R14" / "RESULT.md").write_text(r14, encoding="utf-8")
    (ROOT / "registry" / "DEC-136.md").write_text(dec136, encoding="utf-8")
    (ROOT / "registry" / "DEC-137.md").write_text(dec137, encoding="utf-8")
    (ROOT / "research" / "US-WATERWAY-E01" / "README.md").write_text(e01, encoding="utf-8")
    (ROOT / "STATUS.md").write_text(status, encoding="utf-8")
    (ROOT / "context" / "SESSION_HANDOFF.md").write_text(handoff, encoding="utf-8")
    cp_new = {
        "checkpoint_id": "CHK-20260911-US-WATERWAY-E01-STAGE-A-ACTIVE",
        "active_issue": 100,
        "active_research": "US-WATERWAY-E01",
        "last_completed_issue": 99,
        "last_completed_research": "PORTFOLIO-R14",
        "last_decision": "DEC-137",
        "updated": TODAY,
    }
    cp_path.write_text(json.dumps(cp_new, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    log_path = ROOT / "registry" / "DECISION_LOG.md"
    log = log_path.read_text(encoding="utf-8")
    additions = []
    if "DEC-136" not in log:
        additions.append("- [DEC-136](DEC-136.md): R14 selects US-WATERWAY first preregistered relationship descendant, with unique-gage Stage A required before magnitudes. / R14가 US-WATERWAY 첫 관계실험을 선정하되 unique-gage Stage A를 선행한다.")
    if "DEC-137" not in log:
        additions.append("- [DEC-137](DEC-137.md): Preregister US-WATERWAY-E01 extreme-flow burden × annual Average Delay and block Stage B until 2016–2025 panel support passes. / E01 사전등록 및 Stage A PASS 전 효과값 개방 금지.")
    if additions:
        log_path.write_text(log.rstrip() + "\n" + "\n".join(additions) + "\n", encoding="utf-8")

    print("FINALIZED_PORTFOLIO_R14_US_WATERWAY_E01_STAGE_A_ACTIVE")


if __name__ == "__main__":
    main()

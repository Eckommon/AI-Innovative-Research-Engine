#!/usr/bin/env python3
"""Finalize PORTFOLIO-R13 and activate US-WATERWAY-F01 without opening outcome values."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-09-11"


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise RuntimeError(f"{label}: required token missing: {needle}")


def main() -> None:
    checkpoint_path = ROOT / "context" / "checkpoint.json"
    checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    if checkpoint.get("last_decision") != "DEC-133":
        raise RuntimeError(f"unexpected prior decision: {checkpoint.get('last_decision')}")
    if str(checkpoint.get("active_issue")).lower() not in {"none", "null"}:
        raise RuntimeError(f"expected Stage-0 restart with no active issue: {checkpoint}")

    r13 = """---
id: PORTFOLIO-R13-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-11
issue: 97
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-US-006
selected_gate: US-WATERWAY-F01
next_issue: 98
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R13 Result — Post-US-UTIL PANEL_DESIGN_READY Reselection
# PORTFOLIO-R13 결과 — US-UTIL PANEL_DESIGN_READY 이후 재선정

## Final selection / 최종 선정

**`SELECT_C_US_006_INLAND_WATERWAY_HYDROLOGY_LOCK_DELAY_FEASIBILITY`**

Selected next gate:

**Issue #98 `US-WATERWAY-F01` — LPMS historical delay × USGS hydrology source/identity feasibility.**

This selection opens no vessel-delay magnitude, hydrology magnitude, SAIDI/SAIFI value, AMI meter count or relationship coefficient. / 본 선정은 결과값을 열지 않는다.

## Why C-US-006 now wins / C-US-006이 우선인 이유

US-UTIL-F02 established a strong 2019–2024 panel-design asset, but external novelty risk has materially increased: a 2025 peer-reviewed study already used 2014–2022 EIA-861 data to estimate associations between AMI adoption and SAIDI/SAIFI. A storm-moderation descendant could still be scientifically distinct, but its marginal mission value is lower until novelty and decision utility are separately justified. / US-UTIL은 실행가능성이 높지만 일반 AMI→reliability 관계의 한계수익이 낮아졌다.

USACE states that LPMS collects vessel movements, lockage times and delays. Public Lock Usage Report material has historically included lock-level Average Delay and Average Processing Time, while current Corps Locks also exposes official reports and Data Web Services. USGS modern Water Data APIs expose historical daily hydrology and monitoring-location metadata. The unresolved high-value uncertainty is whether a current, official, reproducible public route can support >=3 years of lock-level delay identity and deterministic hydrology matching. / 현재 공개경로의 재현가능성이 핵심 불확실성이다.

## Mission-ROI comparison / 목적-ROI 비교

0–5 each; total /45. Scores are selection aids, not empirical findings. / 점수는 선정 보조이며 실증결과가 아니다.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return / novelty risk | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **C-US-006 Inland Waterway Hydrology × Lock Delay F01** | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | **43** | **SELECT** |
| C-EU-001 Cross-National Grid Stress | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 4 | 5 | **39** | HOLD_HIGH_VALUE_OPERABILITY |
| US-UTIL preregistered AMI × Storm × Reliability descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 1 | **38** | HOLD_READY_HIGH_OVERLAP |
| C-CA-002 Grain Pressure × Rail Dwell | 5 | 5 | 5 | 3 | 5 | 5 | 3 | 4 | 2 | **37** | HOLD_REDESIGN_GEOGRAPHY |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE_JOIN_ASSET |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| AU-NEM continuation | 5 | 5 | 5 | 2 | 5 | 5 | 4 | 3 | 1 | **35** | NO_AUTO_CONTINUATION |
| US-AIR descendant | 3 | 4 | 4 | 5 | 3 | 5 | 5 | 2 | 0 | **31** | NO_AUTO_CONTINUATION |

## Official/current source basis / 공식·현행 source 근거

- USACE/NDC Locks and LPMS: https://www.iwr.usace.army.mil/About/Technical-Centers/NDC-Navigation-and-Civil-Works-Decision-Support/NDC-Locks/
- Corps Locks public system: https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/home
- USACE Lock Characteristics FeatureServer: https://services7.arcgis.com/n1YM8pTrFmm7L4hs/arcgis/rest/services/Locks/FeatureServer
- USGS Water Data APIs: https://api.waterdata.usgs.gov/
- 2025 EIA-861 AMI/reliability precedent: https://doi.org/10.4018/JGIM.368257

## Exact next gate / 정확한 다음 gate

Execute only **US-WATERWAY-F01 source/schema/date-range/identity feasibility**.

Do not inspect delay values or hydrology values. First establish whether the official public USACE route provides >=3 contiguous years of lock-level historical delay or sufficient arrival/start timing fields, then test stable lock identity/location and USGS monitoring-location/date-support matching. / 먼저 공개 historical delay source와 identity만 검증한다.

Incremental monetary cost remained **0 USD**.
"""

    dec134 = """---
id: DEC-134
type: decision
created: 2026-09-11
status: ACTIVE
---

# DEC-134 — Select C-US-006 / US-WATERWAY-F01 after US-UTIL panel readiness
# DEC-134 — US-UTIL panel 준비 이후 C-US-006 / US-WATERWAY-F01 선정

## Decision / 결정

Select **C-US-006 Inland Waterway Hydrology × Lock Delay** and open only **US-WATERWAY-F01** as the next bounded gate.

The gate is source/date-range/identity feasibility only. It does not authorize a hydrology→delay effect estimate, delay ranking, causal claim, operational recommendation or predictive model. / source·기간·identity feasibility만 승인한다.

## Basis / 근거

- US-UTIL is PANEL_DESIGN_READY but a 2025 peer-reviewed study already analyzes EIA-861 AMI adoption against SAIDI/SAIFI over 2014–2022, reducing marginal novelty of a generic descendant.
- USACE documents LPMS as collecting lockage times and delays and provides official Corps Locks reports/Data Web Services.
- Historical Public Lock Usage material has included Average Delay/Processing Time, but current reproducible public access and granularity must not be assumed.
- USGS provides modern machine-readable historical daily hydrology and monitoring-location metadata.
- A short, outcome-blind source feasibility gate can cheaply falsify the branch if long historical LPMS delay support is no longer publicly reproducible.

## Frozen next action / 고정 다음 행동

Issue #98 `US-WATERWAY-F01` shall establish only:
1. official USACE public route and access window for historical lock-level delay/timing support;
2. stable machine-readable lock identity and coordinates;
3. distinct qualifying lock count;
4. deterministic lock↔USGS monitoring-location matching feasibility using coordinates plus river/waterbody identity;
5. overlapping daily-value date support for >=3 contiguous years;
6. exclusions and source-access limitations.

If no official public >=3-year historical delay/timing route is established, resolve HOLD without weakening the gate or replacing delay with annual unavailability.

Incremental monetary cost remains **0 USD**. Potentially billable work requires explicit prior approval.
"""

    f01 = """---
id: US-WATERWAY-F01
issue: 98
state: ACTIVE_SOURCE_IDENTITY_PREFLIGHT
mission_anchor: MEM-054
decision: DEC-134
outcome_values_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-WATERWAY-F01 — LPMS Historical Delay × USGS Hydrology Feasibility
# US-WATERWAY-F01 — LPMS 역사적 지연 × USGS 수문 feasibility

## Objective / 목적

Qualify a reproducible public lock-level historical delay × hydrology source structure before any effect calculation. / 효과계산 전 공개 lock-level 역사 지연×수문 source 구조를 검증한다.

## Frozen source routes / 고정 source 경로

- USACE/NDC Corps Locks / LPMS official public reports and Data Web Services.
- USACE/NDC Lock Characteristics public geospatial service.
- USGS modern Water Data APIs for monitoring-location metadata and historical daily-value support.

## Outcome-blind rules / 결과 비사용 규칙

- inspect source access, schema, IDs, coordinates, date ranges and cardinality only;
- delay/processing/hydrology magnitudes must not be summarized or related;
- existence/nonblank of delay or arrival/start/end fields may be inspected without converting their magnitude;
- lock↔gage qualification must use coordinates plus river/waterbody identity; nearest distance alone is insufficient;
- no private/authenticated scraping and no FOIA request inside F01;
- raw external bytes remain transient under RAW-001.

## Frozen historical requirement / 고정 역사 범위

Require a minimum **3 contiguous years within 2016–2025** from an official public USACE route. A 24-hour/30-day live feed is not a substitute.

## Frozen PASS / 고정 PASS

All must hold:
- official public USACE historical lock-level delay or sufficient arrival/start timing support for >=3 contiguous years;
- stable lock identity crosswalkable to public coordinates;
- >=30 distinct locks with historical outcome support;
- >=25 locks prospectively matchable to at least one USGS monitoring location using coordinates plus river/waterbody identity;
- matched USGS daily-value date support overlaps the same >=3-year interval for a prospectively named streamflow and/or gage-height family;
- zero incremental monetary cost.

Failure of the historical-delay route is terminal HOLD for this F01. Do not lower thresholds or substitute annual unavailability.
"""

    status = """---
checkpoint_id: CHK-20260911-US-WATERWAY-F01-ACTIVE
active_issue: 98
active_research: US-WATERWAY-F01
last_completed_issue: 97
last_completed_research: PORTFOLIO-R13
last_decision: DEC-134
updated: 2026-09-11
---

# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R13_SELECTED_US_WATERWAY_F01__SOURCE_IDENTITY_PREFLIGHT_ACTIVE`

## Latest portfolio decision / 최신 포트폴리오 결정

PORTFOLIO-R13 selects:

**`SELECT_C_US_006_INLAND_WATERWAY_HYDROLOGY_LOCK_DELAY_FEASIBILITY`**

Issue #98 `US-WATERWAY-F01` is the sole active research gate.

US-UTIL remains PANEL_DESIGN_READY but is not automatically promoted because a close 2025 EIA-861 AMI↔reliability precedent raises diminishing-return/novelty risk. / US-UTIL 자동 승격 금지.

## Exact next action / 정확한 다음 행동

Execute only the frozen USACE LPMS historical-delay source/date-range/identity preflight, then test public lock identity/location and USGS monitoring-location/date-support feasibility if the historical outcome route survives. / 효과값 비사용 source feasibility만 실행한다.

Incremental monetary cost remains **0 USD**.
"""

    handoff = """---
checkpoint_id: CHK-20260911-US-WATERWAY-F01-ACTIVE
active_issue: 98
active_research: US-WATERWAY-F01
last_completed_issue: 97
last_completed_research: PORTFOLIO-R13
last_decision: DEC-134
updated: 2026-09-11
---

# Session Handoff / 세션 인수인계

## Canonical restart point / 정확한 재개점

PORTFOLIO-R13 selected **C-US-006** and opened Issue #98 `US-WATERWAY-F01`.

Do not return automatically to US-UTIL, US-AIR or AU-NEM. / 자동 복귀 금지.

## Exact bounded execution / 제한 실행

1. Verify the official public USACE LPMS route for >=3 contiguous years of lock-level historical delay or arrival/start timing support.
2. If and only if that survives, verify stable public lock identity/coordinates and >=30 supported locks.
3. Then qualify >=25 lock↔USGS monitoring-location candidates using coordinates plus river/waterbody identity and overlapping daily-value date support.
4. Do not read delay or hydrology magnitudes and do not estimate a relationship.

A current 24-hour/30-day Corps Locks feed cannot satisfy the historical gate by itself. Annual unavailability is not a substitute for delay.

Cost remains **0 USD**; potentially billable work requires explicit prior approval.
"""

    checkpoint_new = {
        "checkpoint_id": "CHK-20260911-US-WATERWAY-F01-ACTIVE",
        "active_issue": 98,
        "active_research": "US-WATERWAY-F01",
        "last_completed_issue": 97,
        "last_completed_research": "PORTFOLIO-R13",
        "last_decision": "DEC-134",
        "updated": TODAY,
    }

    (ROOT / "research" / "PORTFOLIO-R13").mkdir(parents=True, exist_ok=True)
    (ROOT / "research" / "US-WATERWAY-F01").mkdir(parents=True, exist_ok=True)
    (ROOT / "research" / "PORTFOLIO-R13" / "RESULT.md").write_text(r13, encoding="utf-8")
    (ROOT / "registry" / "DEC-134.md").write_text(dec134, encoding="utf-8")
    (ROOT / "research" / "US-WATERWAY-F01" / "README.md").write_text(f01, encoding="utf-8")
    (ROOT / "STATUS.md").write_text(status, encoding="utf-8")
    (ROOT / "context" / "SESSION_HANDOFF.md").write_text(handoff, encoding="utf-8")
    checkpoint_path.write_text(json.dumps(checkpoint_new, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    decision_log_path = ROOT / "registry" / "DECISION_LOG.md"
    decision_log = decision_log_path.read_text(encoding="utf-8")
    if "DEC-134" not in decision_log:
        decision_log = decision_log.rstrip() + (
            "\n- [DEC-134](DEC-134.md): R13 selects C-US-006 / US-WATERWAY-F01 historical LPMS delay × USGS hydrology source/identity feasibility; no outcome magnitudes opened. / 역사적 delay×수문 source feasibility를 결과값 비사용으로 선정.\n"
        )
        decision_log_path.write_text(decision_log, encoding="utf-8")

    print("FINALIZED_PORTFOLIO_R13_US_WATERWAY_F01_ACTIVE")


if __name__ == "__main__":
    main()

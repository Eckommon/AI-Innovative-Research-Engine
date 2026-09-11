#!/usr/bin/env python3
"""Finalize PORTFOLIO-R11 selection and activate US-UTIL-F01 without opening outcomes."""

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
    if checkpoint.get("last_decision") != "DEC-128":
        raise RuntimeError(f"unexpected prior decision: {checkpoint.get('last_decision')}")
    if str(checkpoint.get("active_issue")).lower() not in {"none", "null"}:
        raise RuntimeError(f"expected Stage-0 restart with no active issue: {checkpoint}")

    r11 = """---
id: PORTFOLIO-R11-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-11
issue: 93
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-US-005
selected_gate: US-UTIL-F01
next_issue: 94
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R11 Result — Post-Low-Novelty Fresh Opportunity Reselection
# PORTFOLIO-R11 결과 — 낮은 신규성 판정 이후 신규 기회 재선정

## Final selection / 최종 선정

**`SELECT_C_US_005_UTILITY_AMI_STORM_RELIABILITY_JOIN_FEASIBILITY`**

Selected next gate:

**Issue #94 `US-UTIL-F01` — EIA-861 utility AMI/reliability/service-territory × NOAA Storm Events join feasibility.**

This selection opens no SAIDI/SAIFI magnitude, AMI effect or storm-reliability relationship. / 본 선정은 SAIDI/SAIFI 값·AMI 효과·폭풍-신뢰도 관계를 열지 않는다.

## Why a fresh branch wins / 신규 분기가 우선인 이유

US-AIR has a valid 2025 relationship result, but `US-AIR-N01` found the core precipitation-delay mechanism to have **LOW novelty**. The mission therefore favors an independent bottleneck with a direct operational outcome and a prospective technology/intervention dimension rather than another automatic aviation descendant. / US-AIR 핵심관계 신규성이 낮으므로 자동 연장보다 독립 병목을 우선한다.

C-US-005 combines four official, structurally complementary data families:
- EIA-861 utility identity and annual reporting frame;
- EIA-861 Advanced Metering support;
- EIA-861 Reliability support (SAIDI/SAIFI family, values not opened in F01);
- EIA-861 Service Territory county mappings;
- NOAA/NCEI Storm Events county exposure.

EIA explicitly documents Advanced Metering from 2007-present, Reliability from 2013-present, and Service Territory from 2001-present. The 2024 EIA-861 final-data ZIP is directly published; 2025 is only an early release and is not selected for the first gate. NOAA Storm Events publishes annual bulk CSV files. / 2024 final source를 첫 gate로 사용하고 2025 early release는 제외한다.

## Fresh candidate comparison / 신규 후보 비교

0–5 each; total /45. Scores are portfolio aids, not empirical innovation findings. / 점수는 선정 보조이며 실증 혁신결과가 아니다.

| Candidate | Mission bottleneck | Cross-source contribution | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return risk | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **C-US-005 Utility AMI × Storm × Reliability** | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | **44** | **SELECT** |
| C-US-006 Inland Waterway Hydrology × Lock Delay | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | **41** | HOLD_SECOND |
| C-EU-001 Cross-National Grid Stress | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 4 | 5 | **39** | HOLD_HIGH_VALUE_OPERABILITY |
| C-CA-002 Grain Pressure × Rail Dwell | 5 | 5 | 5 | 3 | 5 | 5 | 3 | 4 | 2 | **37** | HOLD_REDESIGN_GEOGRAPHY |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE_JOIN_ASSET |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| AU-NEM continuation | 5 | 5 | 5 | 2 | 5 | 5 | 4 | 3 | 1 | **35** | PRESERVE_JOIN__NO_AUTO_CONTINUATION |
| US-AIR descendant without a new decision/propagation/utility question | 3 | 4 | 4 | 5 | 3 | 5 | 5 | 2 | 0 | **31** | NO_AUTO_CONTINUATION |

## Why C-US-005 beats C-US-006 / C-US-006 대비 우위

USACE/USGS inland-waterway hydrology × lock delay is promising, but the readily verified public LPMS route is strongest for current/short-window queue/status and aggregate usage reports. A long historical lock-delay panel therefore has higher source-access risk. EIA-861 already exposes a long annual utility frame with the required identity, AMI, reliability and service-territory schedules. / C-US-005가 장기 panel source operability에서 우위다.

## Official source routes / 공식 source 경로

- EIA Form EIA-861: https://www.eia.gov/electricity/data/eia861/
- 2024 final ZIP: https://www.eia.gov/electricity/data/eia861/zip/f8612024.zip
- NOAA Storm Events bulk CSV: https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/

## Exact next gate / 정확한 다음 gate

Execute **US-UTIL-F01 source-byte/schema/cardinality preflight only**.

Do not read/rank reliability magnitudes and do not estimate an AMI or storm effect. First establish stable utility IDs, schedule support, service-territory many-to-many county mapping, NOAA county keys and frozen structural counts. / 먼저 identity·schema·cardinality만 검증한다.

Incremental monetary cost remained **0 USD**.
"""

    dec129 = """---
id: DEC-129
type: decision
created: 2026-09-11
status: ACTIVE
---

# DEC-129 — Select C-US-005 / US-UTIL-F01 after US-AIR low-novelty result
# DEC-129 — US-AIR 낮은 신규성 이후 C-US-005 / US-UTIL-F01 선정

## Decision / 결정

Select **C-US-005 Utility AMI × Storm Exposure × Reliability** and open only **US-UTIL-F01** as the next bounded gate.

The first gate is source/join/identity feasibility. It does not authorize an AMI effect estimate, storm-reliability regression, SAIDI/SAIFI ranking, causal claim, utility ranking or investment/policy conclusion. / 첫 gate는 source·join·identity feasibility이며 효과·순위·인과 주장을 승인하지 않는다.

## Basis / 근거

- US-AIR's core precipitation-delay mechanism is now novelty-assessed LOW, so automatic continuation has low marginal mission value.
- EIA-861 provides stable annual utility identity plus Advanced Metering, Reliability and county Service Territory schedules.
- NOAA Storm Events provides a public annual county-oriented hazard exposure route.
- 2024 EIA-861 final data are available and are preferred to the unvalidated 2025 early release for the first source gate.
- The utility×county many-to-many structure is scientifically explicit and can be preserved rather than collapsed into false independence.

## Frozen next action / 고정 다음 행동

Issue #94 `US-UTIL-F01` shall execute only:
1. source byte/hash materialization;
2. ZIP/workbook/member and schema inventory;
3. EIA utility-ID cardinality across Reliability, Advanced Metering and Service Territory;
4. deterministic utility×county cardinality;
5. NOAA 2024 county-key schema/cardinality;
6. exclusions and identity conflicts.

Do not open reliability magnitudes or a relationship test inside F01.

Incremental monetary cost remains **0 USD**. Potentially billable work requires explicit prior approval.
"""

    f01 = """---
id: US-UTIL-F01
issue: 94
state: ACTIVE_SOURCE_PREFLIGHT
mission_anchor: MEM-054
decision: DEC-129
outcome_values_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-UTIL-F01 — EIA-861 Utility AMI/Reliability/Service Territory × NOAA Storm Events
# US-UTIL-F01 — EIA-861 유틸리티 AMI/신뢰도/서비스영역 × NOAA Storm Events

## Objective / 목적

Qualify a nationwide, many-to-many utility-year join before any effect calculation. / 효과계산 전 전국 utility-year 결합의 source·identity·cardinality를 검증한다.

## Frozen source snapshot / 고정 source snapshot

- EIA Form EIA-861 **2024 final data** ZIP.
- EIA schedules required: Reliability, Advanced Metering, Service Territory and utility identity/frame support.
- NOAA/NCEI Storm Events **2024** annual bulk details/location source family.
- EIA 2025 early release is excluded from this first gate.

## Outcome-blind rules / 결과 비사용 규칙

- EIA identifiers only; no fuzzy utility-name matching.
- Preserve utility↔county many-to-many mapping.
- A county shared by multiple utilities is shared exposure, not independent replication.
- Do not invent county customer weights.
- Do not read, rank or summarize SAIDI/SAIFI magnitudes in F01.
- Do not estimate AMI effects or storm effects.
- Raw ZIP/GZ/XLSX/CSV bytes remain transient under RAW-001.

## Frozen initial structural gate / 고정 초기 구조 gate

Require all for source-side structural PASS:
- >=300 reliability-reporting utility identities with deterministic Service Territory joins;
- >=250 of those utilities with an Advanced Metering record/support route;
- >=1,000 unique qualified utility×county mappings;
- reproducible NOAA 2024 county-key route for Storm Events;
- no paid data/API/compute.

These thresholds qualify structure only; they do not imply a useful or novel AMI-resilience relationship.

## Exact next action / 정확한 다음 행동

Run source-byte/schema/cardinality preflight. Persist hashes, member/sheet names, selected non-outcome headers, identity counts, county-key counts and exclusions. / source hash·schema·identity cardinality만 기록한다.
"""

    status = """---
checkpoint_id: CHK-20260911-US-UTIL-F01-ACTIVE
active_issue: 94
active_research: US-UTIL-F01
last_completed_issue: 93
last_completed_research: PORTFOLIO-R11
last_decision: DEC-129
updated: 2026-09-11
---

# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R11_SELECTED_US_UTIL_F01__SOURCE_PREFLIGHT_PENDING`

## Latest portfolio decision / 최신 포트폴리오 결정

PORTFOLIO-R11 selects:

**`SELECT_C_US_005_UTILITY_AMI_STORM_RELIABILITY_JOIN_FEASIBILITY`**

The selected active gate is Issue #94 `US-UTIL-F01`.

The branch is outcome-blind: no SAIDI/SAIFI magnitude, AMI effect or storm-reliability relationship has been opened. / 현재 효과값 비사용 상태다.

## Exact next action / 정확한 다음 행동

Execute the 2024 EIA-861 final ZIP + NOAA Storm Events source-byte/schema/cardinality preflight under the frozen #94 contract. / #94 계약에 따라 source·schema·cardinality만 실행한다.

Incremental monetary cost remains **0 USD**.
"""

    handoff = """---
checkpoint_id: CHK-20260911-US-UTIL-F01-ACTIVE
active_issue: 94
active_research: US-UTIL-F01
last_completed_issue: 93
last_completed_research: PORTFOLIO-R11
last_decision: DEC-129
updated: 2026-09-11
---

# Session Handoff / 세션 인수인계

## Canonical restart point / 정확한 재개점

PORTFOLIO-R11 selected fresh candidate **C-US-005** and opened Issue #94 `US-UTIL-F01`.

Do not return automatically to US-AIR. / US-AIR 자동 복귀 금지.

## Selected source structure / 선정 source 구조

- EIA-861 2024 final data: utility identity + Advanced Metering + Reliability + Service Territory.
- NOAA/NCEI Storm Events 2024 annual bulk source.
- Preserve explicit utility↔county many-to-many structure.

## Exact next bounded execution / 다음 제한 실행

Run only the F01 source-byte/schema/cardinality preflight:
- exact source URL / byte length / SHA-256;
- archive/workbook/sheet names;
- non-outcome identity schemas;
- Reliability utility-ID support count without reading reliability magnitudes;
- Advanced Metering utility-ID support count;
- Service Territory utility×county count;
- NOAA county-key schema/cardinality;
- deterministic intersection counts and exclusions.

Do not estimate any relationship. / 관계추정 금지.

Cost remains **0 USD**; potentially billable work requires explicit prior approval.
"""

    checkpoint_new = {
        "checkpoint_id": "CHK-20260911-US-UTIL-F01-ACTIVE",
        "active_issue": 94,
        "active_research": "US-UTIL-F01",
        "last_completed_issue": 93,
        "last_completed_research": "PORTFOLIO-R11",
        "last_decision": "DEC-129",
        "updated": TODAY,
    }

    (ROOT / "research" / "PORTFOLIO-R11").mkdir(parents=True, exist_ok=True)
    (ROOT / "research" / "US-UTIL-F01").mkdir(parents=True, exist_ok=True)
    (ROOT / "research" / "PORTFOLIO-R11" / "RESULT.md").write_text(r11, encoding="utf-8")
    (ROOT / "registry" / "DEC-129.md").write_text(dec129, encoding="utf-8")
    (ROOT / "research" / "US-UTIL-F01" / "README.md").write_text(f01, encoding="utf-8")
    (ROOT / "STATUS.md").write_text(status, encoding="utf-8")
    (ROOT / "context" / "SESSION_HANDOFF.md").write_text(handoff, encoding="utf-8")
    checkpoint_path.write_text(json.dumps(checkpoint_new, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    decision_log_path = ROOT / "registry" / "DECISION_LOG.md"
    decision_log = decision_log_path.read_text(encoding="utf-8")
    require(decision_log, "[DEC-128]", "decision log")
    if "[DEC-129]" not in decision_log:
        decision_log = decision_log.rstrip() + (
            "\n- [DEC-129](DEC-129.md): R11 selects C-US-005 / US-UTIL-F01 fresh utility AMI × storm × reliability join feasibility; first gate remains outcome-blind. / 신규 utility AMI×폭풍×신뢰도 결합 feasibility 선정·첫 gate 효과값 비사용.\n"
        )
        decision_log_path.write_text(decision_log, encoding="utf-8")

    print("PORTFOLIO-R11 finalized; US-UTIL-F01 active; DEC-129")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-12"
RUN = "34688361775"
INITIAL_RUN = "34673025029"

status_path = ROOT / "STATUS.md"
handoff_path = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_path = ROOT / "context" / "checkpoint.json"
claim_ledger_path = ROOT / "registry" / "CLAIM_LEDGER.md"
decision_log_path = ROOT / "registry" / "DECISION_LOG.md"
readme_path = ROOT / "research" / "CA-GRAIN-F01" / "README.md"
result_path = ROOT / "research" / "CA-GRAIN-F01" / "RESULT.md"
audit_path = ROOT / "research" / "CA-GRAIN-F01" / "PROBE_AUDIT.md"
claim_path = ROOT / "registry" / "CLM-149.md"
decision_path = ROOT / "registry" / "DEC-148.md"

result = result_path.read_text(encoding="utf-8")
status = status_path.read_text(encoding="utf-8")
audit = audit_path.read_text(encoding="utf-8")

assert "gate: PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE" in result
assert "probe_revision: 2" in result
assert f"supersedes_initial_run: {INITIAL_RUN}" in result
assert "active_issue: 106" in status
assert "active_research: CA-GRAIN-F01" in status
assert "last_decision: DEC-147" in status
assert "INVALIDATE_INITIAL_GATE_PENDING_CORRECTED_PROBE" in audit
assert not claim_path.exists(), "CLM-149 already exists"
assert not decision_path.exists(), "DEC-148 already exists"

status_path.write_text("""---
checkpoint_id: CHK-20260912-CA-GRAIN-F01-PASS-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 106
last_completed_research: CA-GRAIN-F01
last_decision: DEC-148
updated: 2026-09-12
---

# Project Status / 프로젝트 상태

**State / 상태:** `CA_GRAIN_F01_PASS__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

CA-GRAIN-F01 completed outcome-blind with `PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE`. After invalidating the initial technical-probe HOLD, corrected Run `34688361775` inspected exact textual source identities across the frozen 2023–2025 Transport Canada annual files and established 104 TC weekly keys, two rail carriers (`CN`, `CPKC`), 81 explicit-date GSW weekly keys, and 81 common weekly keys. No grain-volume or dwell-time magnitude was analyzed or persisted and no relationship was computed.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio control. Compare a separately preregistered C-CA-002 relationship experiment against independent alternatives on marginal information value and overlap risk. Do not open grain-volume or dwell-time magnitudes until a new effect-stage issue and preregistration are explicitly authorized.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_path.write_text("""---
checkpoint_id: CHK-20260912-CA-GRAIN-F01-PASS-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 106
last_completed_research: CA-GRAIN-F01
last_decision: DEC-148
updated: 2026-09-12
---

# Session Handoff / 세션 인수인계

CA-GRAIN-F01 / Issue #106 is complete with **`PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE`**.

The first Run `34673025029` emitted a HOLD because the probe compared frozen textual identities against `*_SortId` columns and inspected only the first annual English Transport Canada CSV. `PROBE_AUDIT.md` invalidated that technical result before Issue closure. The corrected outcome-blind Run `34688361775` kept the frozen scientific contract unchanged and established 104 TC source dates/week keys, two carriers (`CN`, `CPKC`), 81 explicit-date GSW week keys and 81 common weekly keys across the frozen interval.

No grain-volume or dwell-time magnitude was analyzed or persisted and no relationship/effect model was computed. F01 PASS establishes source/schema/join feasibility only.

Canonical restart: **Stage 0 portfolio control**. Do not automatically open a grain-pressure × rail-dwell effect test. Any relationship experiment must be separately selected, preregistered and authorized before magnitudes are opened. Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

checkpoint_path.write_text(json.dumps({
    "checkpoint_id": "CHK-20260912-CA-GRAIN-F01-PASS-PORTFOLIO-RETURN",
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": 106,
    "last_completed_research": "CA-GRAIN-F01",
    "last_decision": "DEC-148",
    "updated": DATE,
}, indent=2) + "\n", encoding="utf-8")

claim_path.write_text(f"""---
id: CLM-149
type: claim
created: {DATE}
issue: 106
status: active
---

# CLM-149 — CA-GRAIN-F01 establishes weekly source/join feasibility after technical probe correction

The corrected outcome-blind Run `{RUN}` resolves CA-GRAIN-F01 to **`PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE`**. Exact textual label columns identify `All Western grain` × `Average Dwell Time at Origin` across the frozen Transport Canada 2023–2025 annual English CSVs. The structural panel supports **104** Transport Canada weekly keys, **2** carriers (`CN`, `CPKC`), **81** explicit-date Canadian Grain Commission GSW weekly keys and **81** common weekly keys.

The first Run `{INITIAL_RUN}` HOLD is not a scientific result: `PROBE_AUDIT.md` records that it arose from `*_SortId` header resolution plus single-year file selection and was invalidated before Issue closure. The frozen source families, identities, interval and PASS requirements were unchanged.

This claim establishes source/schema/join feasibility only. No grain-volume or dwell-time magnitude was analyzed or persisted and no relationship was computed. Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

decision_path.write_text(f"""---
id: DEC-148
type: decision
created: {DATE}
issue: 106
status: accepted
---

# DEC-148 — Finalize CA-GRAIN-F01 as PASS and return to Stage 0

Finalize Issue #106 as **`PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE`** using corrected Run `{RUN}`. Treat initial Run `{INITIAL_RUN}` as an invalid technical probe result per `PROBE_AUDIT.md`, not as contradictory scientific evidence.

F01 PASS establishes that the frozen Transport Canada × Canadian Grain Commission weekly source/schema/join route is structurally feasible at 0 USD. It does **not** establish a grain-pressure × rail-dwell relationship and does not authorize opening grain-volume or dwell-time magnitudes.

Return to Stage 0 portfolio control. A C-CA-002 effect descendant may proceed only after separate portfolio selection, preregistration and explicit authorization; independent alternatives and external-overlap risk must be compared first.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

claim_ledger = claim_ledger_path.read_text(encoding="utf-8")
assert "`CLM-149`" not in claim_ledger
claim_ledger = claim_ledger.rstrip() + f"""

| `CLM-149` | Corrected CA-GRAIN-F01 outcome-blind probe passes weekly source/join feasibility: 104 TC weekly keys, 2 carriers and 81 common explicit-date GSW week keys; initial technical HOLD invalidated before closure. / 교정된 CA-GRAIN-F01 source/join 구조 PASS. | `OBSERVED/DERIVED/VALIDATED` | `V3_PREREGISTERED_SOURCE_PANEL_REPRODUCED` | Run `{RUN}`; `research/CA-GRAIN-F01/RESULT.md`; `SOURCE_PANEL_MANIFEST.json`; `PROBE_AUDIT.md` | {DATE} | active |
"""
claim_ledger_path.write_text(claim_ledger, encoding="utf-8")

decision_log = decision_log_path.read_text(encoding="utf-8")
assert "`DEC-148`" not in decision_log
decision_log = decision_log.rstrip() + f"""

| `DEC-148` | {DATE} | Finalize corrected `CA-GRAIN-F01` as `PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE` and return to Stage 0; no automatic effect exposure. / 교정 F01 구조 PASS 확정·Stage 0 복귀. | Initial HOLD was a technical probe defect; corrected frozen-contract run satisfies source/schema/join gate only. | Issue #106; `CLM-149`; Run `{RUN}` | active |
"""
decision_log_path.write_text(decision_log, encoding="utf-8")

readme = readme_path.read_text(encoding="utf-8")
assert "state: ACTIVE_SOURCE_JOIN_FEASIBILITY" in readme
readme = readme.replace("state: ACTIVE_SOURCE_JOIN_FEASIBILITY", "state: COMPLETED_PASS", 1)
readme = readme.rstrip() + """

## Final disposition / 최종 종결

- gate: **`PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE`**
- corrected Run: `34688361775`
- initial technical Run `34673025029`: **invalidated by `PROBE_AUDIT.md`**
- claim: `CLM-149`
- decision: `DEC-148`
- relationship/effect testing: **not authorized**
- canonical restart: **Stage 0 portfolio control**

This PASS establishes only frozen weekly source/schema/join feasibility. It is not evidence that grain pressure affects rail dwell.
"""
readme_path.write_text(readme, encoding="utf-8")

print(json.dumps({
    "gate": "PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE",
    "claim": "CLM-149",
    "decision": "DEC-148",
    "restart": "Stage 0 portfolio control",
    "cost_usd": 0,
}))

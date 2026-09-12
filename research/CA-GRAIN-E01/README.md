---
id: CA-GRAIN-E01
issue: 108
state: COMPLETED_HOLD_EXPOSURE_IDENTITY_AMBIGUOUS
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

## Final Stage A disposition / Stage A 최종 판정

- gate: **`HOLD_CA_GRAIN_E01_EXPOSURE_IDENTITY_AMBIGUOUS`**
- Run: `34688813498`
- surviving GSW families: `Primary / Deliveries / Current Week`; `Process / Producer Deliveries / Current Week`
- outcome support: `CN=104`, `CPKC=104` nonblank weeks
- relationship/effect values: **not opened**
- decision: `DEC-151`
- restart: **Stage 0 portfolio control**

E01 is terminal under its frozen identity hierarchy. Any narrower exposure follow-up must be separately selected and preregistered.

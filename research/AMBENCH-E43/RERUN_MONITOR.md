---
id: AMBENCH-E43-RERUN-MONITOR
type: exact-rerun-terminal-diagnostic
created: 2026-09-03
historical_run_id: 32648786267
experiment_contract_changed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-E43 Exact Rerun Monitor / 동일 재실행 모니터

- run_attempt: `2`
- status: `completed`
- conclusion: `failure`
- updated_at: `2026-09-03T08:28:24Z`

## Jobs / Jobs

### execute
- conclusion: `failure`
- step `1` — Set up job: `success`
- step `2` — Run actions/checkout@v4: `success`
- step `3` — Reconstruct and verify frozen F42 inputs: `failure`
- step `4` — Build pinned 3DThesis and prepare identical cases: `skipped`
- step `5` — Execute N0 and R1 under frozen caps: `skipped`
- step `6` — Apply frozen aggregate gate and persist result: `skipped`
- step `12` — Post Run actions/checkout@v4: `success`
- step `13` — Complete job: `success`

**MONITOR_FAIL_EXACT_RERUN_NOT_SUCCESSFUL**


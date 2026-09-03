---
id: AMBENCH-E43-RUN-DIAGNOSTIC
type: execution-harness-diagnostic
created: 2026-09-03
experiment_contract_changed: false
performance_result_interpreted: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-E43 Workflow Run Diagnostic / Workflow 실행 진단

This file diagnoses the historical E43 Actions execution only. It does not change or interpret the frozen experiment.

- run_id: `32648786267`
- event: `push`
- status: `completed`
- conclusion: `failure`
- head_sha: `f3bcdf71170c478a67c391c87b53c016a22c35d6`
- created_at: `2026-08-23T15:30:49Z`
- updated_at: `2026-08-23T15:32:29Z`

## Jobs / Jobs

### execute
- status: `completed`
- conclusion: `failure`
- step `1` — Set up job: status=`completed`, conclusion=`success`
- step `2` — Run actions/checkout@v4: status=`completed`, conclusion=`success`
- step `3` — Reconstruct and verify frozen F42 inputs: status=`completed`, conclusion=`failure`
- step `4` — Build pinned 3DThesis and prepare identical cases: status=`completed`, conclusion=`skipped`
- step `5` — Execute N0 and R1 under frozen caps: status=`completed`, conclusion=`skipped`
- step `6` — Apply frozen aggregate gate and persist result: status=`completed`, conclusion=`skipped`
- step `12` — Post Run actions/checkout@v4: status=`completed`, conclusion=`success`
- step `13` — Complete job: status=`completed`, conclusion=`success`

**DIAGNOSTIC_E43_RUN_NOT_SUCCESSFUL**


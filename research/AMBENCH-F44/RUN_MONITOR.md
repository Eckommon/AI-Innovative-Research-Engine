---
id: AMBENCH-F44-RUN-MONITOR
type: workflow-terminal-diagnostic
created: 2026-09-03
experiment_contract_changed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-F44 Run Monitor / 실행 모니터

- run_id: `33735916914`
- status: `completed`
- conclusion: `success`
- head_sha: `d700d0411f5239f31bc0c998d0ac016b08c8006a`

## Jobs / Jobs

### equivalence
- status: `completed`
- conclusion: `success`
- step `1` — Set up job: status=`completed`, conclusion=`success`
- step `2` — Run actions/checkout@v4: status=`completed`, conclusion=`success`
- step `3` — Reconstruct checksum-frozen F44 calibration prefix: status=`completed`, conclusion=`success`
- step `4` — Build pinned 3DThesis and prepare FULL41 and TOP1: status=`completed`, conclusion=`success`
- step `5` — Execute frozen F44 calibration cases: status=`completed`, conclusion=`success`
- step `6` — Apply frozen coordinate-wise equivalence gate: status=`completed`, conclusion=`success`
- step `7` — Persist F44 result: status=`completed`, conclusion=`success`
- step `14` — Post Run actions/checkout@v4: status=`completed`, conclusion=`success`
- step `15` — Complete job: status=`completed`, conclusion=`success`

### terminal_recorder
- status: `completed`
- conclusion: `success`
- step `1` — Set up job: status=`completed`, conclusion=`success`
- step `2` — Run actions/checkout@v4: status=`completed`, conclusion=`success`
- step `3` — Persist fail-closed F44 result if normal result missing: status=`completed`, conclusion=`success`
- step `6` — Post Run actions/checkout@v4: status=`completed`, conclusion=`success`
- step `7` — Complete job: status=`completed`, conclusion=`success`


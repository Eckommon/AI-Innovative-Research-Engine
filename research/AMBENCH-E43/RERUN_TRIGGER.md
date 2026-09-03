---
id: AMBENCH-E43-EXACT-RERUN-TRIGGER
type: execution-retry-record
created: 2026-09-03
historical_run_id: 32648786267
experiment_contract_changed: false
workflow_code_changed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-E43 Exact Failed-Job Rerun / 동일 실패 Job 재실행

The historical E43 run failed during NIST source download with `TimeoutError: The read operation timed out` before build or simulator execution.

This action requested GitHub to rerun the **exact failed jobs of the same run**, with no change to source identity, input reconstruction, timeout, runtime, timestep, domain, endpoint, thresholds, or experiment contract.

Purpose: distinguish a transient network failure from a reproducible harness deficiency before modifying the harness.

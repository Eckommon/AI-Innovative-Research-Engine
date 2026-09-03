---
id: AMBENCH-E43-AMENDMENT-02
type: execution-harness-correction
created: 2026-09-03
historical_run_id: 32648786267
experiment_contract_changed: false
performance_output_observed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-E43 Amendment 02 — Historical Download Timeout and Exact Rerun Boundary
# AMBENCH-E43 보정 02 — 과거 Download Timeout 및 동일 재실행 경계

## Verified diagnosis / 검증 진단

The original E43 GitHub Actions run `32648786267` did **not** reach 3DThesis build or simulator execution.

Historical job evidence shows:
- checkout: PASS;
- `Reconstruct and verify frozen F42 inputs`: FAIL;
- build: SKIPPED;
- N0/R1 simulation: SKIPPED;
- aggregate gate/write-back: SKIPPED.

The Step 3 traceback terminates in:

`TimeoutError: The read operation timed out`

while the workflow was fetching NIST source data through `urllib.request.urlopen(..., timeout=90)`.

Therefore the 2026-08-23 E43 absence of `RESULT.md` is classified as an **execution-harness/source-download failure before performance**, not a scientific PASS/PARTIAL/NO result and not a simulator-performance HOLD.

## Current authorized recovery / 현재 허용 복구

Before changing any harness parameter, request GitHub `rerun-failed-jobs` for the exact historical run.

This exact rerun preserves unchanged:
- NIST dataset/component identity and checksum requirements;
- F42 N0/R1 path hashes;
- transferred P01 geometry/timing;
- pinned 3DThesis commit;
- `Timestep=1e-5 s`;
- domain/resolution;
- 480-second per-case runtime cap and 20-minute workflow cap;
- `MP_width` endpoint and all materiality/integrity gates.

If the exact rerun fails again at source download, a later amendment may add only bounded network retry/read-timeout hardening. Such hardening must not alter experiment inputs, simulator settings, endpoint or gates.

## Evidence / 근거

- `research/AMBENCH-E43/RUN_DIAGNOSTIC.md`
- `research/AMBENCH-E43/STEP3_FAILURE_DIAGNOSTIC.md`
- `research/AMBENCH-E43/RERUN_TRIGGER.md`

## Boundary / 경계

No E43 simulator performance result has been observed as of this amendment. No scientific claim is changed.

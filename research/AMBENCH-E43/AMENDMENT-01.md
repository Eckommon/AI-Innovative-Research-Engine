---
id: AMBENCH-E43-AMENDMENT-01
type: pre-performance-runtime-resource-contract
created: 2026-08-24
custom_performance_observed_before_amendment: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-E43 Amendment-01 — Exact Runtime Cap Before Performance
# AMBENCH-E43 수정-01 — 성능실행 전 정확 Runtime Cap

## Frozen resource contract / 고정 resource 계약

Before either N0 or R1 custom simulator performance is executed:

- GitHub Actions job: standard public `ubuntu-latest` only;
- workflow job timeout: `20 minutes`;
- each individual 3DThesis N0/R1 simulation command: hard wall-clock cap `480 seconds` (`8 minutes`);
- simulations execute sequentially under the same runner/build;
- no GPU, larger runner, paid solver/API/data, cache or Actions artifact upload;
- raw upstream checkout, generated paths and simulator CSVs remain runner-transient.

If either simulation reaches the 480-second cap, exits non-zero, fails to produce the exact `MP_width` schema, or produces <100 finite positive `MP_width` records, final gate = `HOLD_E43_RUNTIME_OR_INTEGRITY`.

## No runtime rescue / runtime 구제 금지

After a runtime HOLD, E43 must not:
- reduce the frozen `101 x 81 x 41` domain/resolution;
- increase timestep above/below `1e-5 s`;
- trim P01 commands/runs;
- change tracking mode;
- switch to GPU/larger/paid runner;
- change endpoint or positive-width coverage rule.

Any materially different numerical/runtime design requires a new separately preregistered descendant, not an E43 amendment after performance.

## Unchanged performance contract / 성능계약 유지

All E43 input hashes, path orders, source timing, material/beam settings, primary spatial `MP_width` CV, 10% CV threshold, ±5% mean-width constraint, ±10% positive-footprint constraint and PASS/PARTIAL/NO/HOLD definitions remain unchanged.

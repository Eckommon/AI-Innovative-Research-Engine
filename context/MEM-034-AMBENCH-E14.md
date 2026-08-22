---
id: MEM-034-AMBENCH-E14
type: memory
state: ACTIVE
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
---

# MEM-034 — AMBENCH-E14 active / AMBENCH-E14 활성

- Active Issue: #32.
- Frozen experiment: A-AMB stationary aluminum absorbed-power/absorptance ↔ melt-pool-width dynamics.
- Source: NIST `mds2-2525` v1.3.1.
- Primary source files/checksums are frozen in `research/AMBENCH-E14/README.md`.
- Primary statistic: interval-level absorbed power vs width increment Spearman with all circular shifts as serial null.
- No lag search, smoothing, manual cropping, feature rescue, or high-capacity ML.
- Contamination inherited from F13: scanned-Al publication aggregates preobserved; stationary-spot numerical PDR time series not yet analyzed at preregistration.
- Cost boundary: any potentially billable action requires explicit user approval before execution; E14 execution authorized only on verified zero-incremental-cost public NIST + provided transient compute.

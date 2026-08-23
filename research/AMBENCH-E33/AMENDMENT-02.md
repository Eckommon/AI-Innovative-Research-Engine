---
id: AMBENCH-E33-AMENDMENT-02
type: preregistration-amendment
state: ACTIVE
created: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-E33/README.md
  - research/AMBENCH-E33/AMENDMENT-01.md
  - research/AMBENCH-E33/DESIGN_MAP_PREFLIGHT.md
  - Issue #51
incremental_monetary_cost_usd: 0
---

# AMBENCH-E33 Amendment 02 — Equivalent Programmed-Length Gate Operationalization
# AMBENCH-E33 수정 02 — 동등 programmed-length gate 운영 정의

## 1. Purpose / 목적

**KO:** Amendment-01이 `C(t) ↔ D(19−t)`의 의미를 same-XY-location이 아니라 **equivalent programmed track length under opposite scan-history order**로 교정했으므로, measurement outcome을 열기 전에 checksum-frozen process-input만으로 그 equivalence를 판정할 수 있는 고정 metric과 tolerance를 정의한다.

**EN:** Amendment-01 corrected the meaning of `C(t) ↔ D(19−t)` from same XY location to **equivalent programmed track length under opposite scan-history order**. This amendment freezes an outcome-independent process-input metric and tolerance before any `Measurements.xlsx` numerical cell is opened.

## 2. Fixed process-input length metric / 고정 공정입력 길이 metric

Authoritative source design fixes nominal scan speed at `960 mm/s`, and the provided scan-strategy command record is sampled at `100 kHz` (`10 µs` interval).

For each contiguous laser-on segment `s`:

`L_programmed(s) = laser_on_duration_seconds(s) × 960,000 µm/s`

The expected recording increment is:

`ΔL_record = 960,000 µm/s × 0.00001 s = 9.6 µm`.

This is a process-command-derived length proxy. It is not inferred from measurement outcomes.

## 3. Frozen equivalence tolerance / 고정 동등성 tolerance

A reverse pair `C(t), D(19−t)` is length-equivalent if:

`|L_C(t) − L_D(19−t)| <= 10 µm`.

Rationale / 근거:
- `10 µm` is approximately one 100 kHz command-recording interval at the fixed `960 mm/s` scan speed (`9.6 µm`);
- the threshold is frozen from recording resolution and source design, not from melt-pool measurement values;
- no measurement outcome has been opened to choose this threshold.

## 4. Frozen global comparison / 고정 전체 비교

In addition to all 18 reverse pairs satisfying the per-pair tolerance, the reverse map must be globally better as a programmed-length equivalence relation than same-index pairing:

`MAE_reverse = mean_t |L_C(t) − L_D(19−t)|`

`MAE_same = mean_t |L_C(t) − L_D(t)|`

Required:

`MAE_reverse < MAE_same`.

No ratio threshold or post-outcome tuning is permitted.

## 5. Revised source gate / 보정 source gate

### `PASS_E33_EQUIVALENT_LENGTH_REVERSE_MAP`
All must hold:
1. exactly `18` laser-on segments in each strategy;
2. process inputs have the expected fixed nominal `960 mm/s` design and approximately `10 µs` sampling;
3. all 18 `C(t) ↔ D(19−t)` pairs satisfy `<=10 µm` programmed-length difference;
4. `MAE_reverse < MAE_same`;
5. checksum identities remain equal to the preregistered NERDm source identities.

### `HOLD_E33_GEOMETRY_MAP_UNRESOLVED`
If any item above fails, do not open `Measurements.xlsx` numerical outcomes.

## 6. Non-change statement / 비변경 선언

This amendment does **not** change:
- width primary / area secondary endpoints;
- operator nesting or physical-repeat aggregation;
- `h_t = 2t−19`;
- two-sided Spearman statistic;
- 100,000 permutations and seed `20260823`;
- valid-block threshold;
- PASS/MIXED/NO/HOLD numerical decision gates.

The publication-level outcome exposure disclosed in Amendment-01 remains permanent. Any later numerical execution is confirmatory/reanalysis, not pristine outcome-blind discovery.

## 7. Cost / 비용
Incremental monetary cost: `0 USD`; potentially billable actions remain prohibited without explicit user approval.

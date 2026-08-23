---
id: AMBENCH-F23
type: preregistration
state: PREREGISTERED
created: 2026-08-23
source_of_truth: github
inherits:
  - AMBENCH-F22
  - DEC-049
---

# AMBENCH-F23 — Headerless Serialization / 40-Column Semantic Mapping Gate
# AMBENCH-F23 — Headerless 직렬화 / 40열 의미 매핑 게이트

## Purpose / 목적

**KO:** NIST `mds2-3761`의 checksum-verified registered X4 CSV가 headerless라는 F22 발견을 전제로, raw column position `1..40`을 NIST AMS 100-69의 authoritative feature order와 결정론적으로 매핑하고, 모든 4 parts × 250 layers의 row serialization이 이 contract와 구조적으로 일치하는지 값 비노출 방식으로 검증한다.

**EN:** Given F22's discovery that the checksum-verified `mds2-3761` registered X4 CSVs are headerless, deterministically map raw positions `1..40` to the authoritative feature order in NIST AMS 100-69 and verify, without emitting numerical values, that row serialization across all 4 parts × 250 layers structurally conforms to that contract.

## Authoritative semantic source / 권위 의미 source
- NIST AMS 100-69, May 2025, DOI `10.6028/NIST.AMS.100-69`.
- Section 3.2 states every CSV has 40 columns and multiple rows; each row is one measured point with associated features.
- Tables 1–3 define positions 1..40, names, units, and definitions.

## Frozen positional contract / 고정 위치 contract

| Pos | Canonical field | NIST meaning | Unit |
|---:|---|---|---|
| 1 | `part_number` | Part number; same as scanning order | N/A |
| 2 | `build_time_us` | Build time synchronized with machine time | µs |
| 3 | `command_laser_x_mm` | Command laser position in X; XYPT command | mm |
| 4 | `command_laser_y_mm` | Command laser position in Y; XYPT command | mm |
| 5 | `command_laser_power_w` | Command laser power; XYPT command | W |
| 6 | `command_scan_speed_mm_s` | Scan speed calculated from command laser position | mm/s |
| 7 | `real_laser_x_mm` | Real laser position in X; DAQ | mm |
| 8 | `real_laser_y_mm` | Real laser position in Y; DAQ | mm |
| 9 | `real_laser_power_w` | Real laser power; DAQ | W |
| 10 | `real_scan_speed_mm_s` | Scan speed calculated from real laser position | mm/s |
| 11 | `melt_pool_length_t80_mm` | Major axis of fitted ellipse, threshold 80 | mm |
| 12 | `melt_pool_width_t80_mm` | Minor axis of fitted ellipse, threshold 80 | mm |
| 13 | `melt_pool_area_t80_mm2` | Melt-pool area, threshold 80 | mm² |
| 14 | `melt_pool_length_t100_mm` | Major axis of fitted ellipse, threshold 100 | mm |
| 15 | `melt_pool_width_t100_mm` | Minor axis of fitted ellipse, threshold 100 | mm |
| 16 | `melt_pool_area_t100_mm2` | Melt-pool area, threshold 100 | mm² |
| 17 | `melt_pool_length_t120_mm` | Major axis of fitted ellipse, threshold 120 | mm |
| 18 | `melt_pool_width_t120_mm` | Minor axis of fitted ellipse, threshold 120 | mm |
| 19 | `melt_pool_area_t120_mm2` | Melt-pool area, threshold 120 | mm² |
| 20 | `lwi_powder_led_a_raw` | Powder view after spreading, LED A, original | N/A |
| 21 | `lwi_powder_led_a_mean3` | Powder view after spreading, LED A, 3×3 mean filter | N/A |
| 22 | `lwi_powder_led_a_mean5` | Powder view after spreading, LED A, 5×5 mean filter | N/A |
| 23 | `lwi_powder_led_b_raw` | Powder view after spreading, LED B, original | N/A |
| 24 | `lwi_powder_led_b_mean3` | Powder view after spreading, LED B, 3×3 mean filter | N/A |
| 25 | `lwi_powder_led_b_mean5` | Powder view after spreading, LED B, 5×5 mean filter | N/A |
| 26 | `lwi_powder_led_c_raw` | Powder view after spreading, LED C, original | N/A |
| 27 | `lwi_powder_led_c_mean3` | Powder view after spreading, LED C, 3×3 mean filter | N/A |
| 28 | `lwi_powder_led_c_mean5` | Powder view after spreading, LED C, 5×5 mean filter | N/A |
| 29 | `lwi_exposure_led_a_raw` | Exposure view after scan, LED A, original | N/A |
| 30 | `lwi_exposure_led_a_mean3` | Exposure view after scan, LED A, 3×3 mean filter | N/A |
| 31 | `lwi_exposure_led_a_mean5` | Exposure view after scan, LED A, 5×5 mean filter | N/A |
| 32 | `lwi_exposure_led_b_raw` | Exposure view after scan, LED B, original | N/A |
| 33 | `lwi_exposure_led_b_mean3` | Exposure view after scan, LED B, 3×3 mean filter | N/A |
| 34 | `lwi_exposure_led_b_mean5` | Exposure view after scan, LED B, 5×5 mean filter | N/A |
| 35 | `lwi_exposure_led_c_raw` | Exposure view after scan, LED C, original | N/A |
| 36 | `lwi_exposure_led_c_mean3` | Exposure view after scan, LED C, 3×3 mean filter | N/A |
| 37 | `lwi_exposure_led_c_mean5` | Exposure view after scan, LED C, 5×5 mean filter | N/A |
| 38 | `xct_voxel_raw` | XCT voxel value, original | N/A |
| 39 | `xct_voxel_mean3` | XCT voxel value, 3×3×3 mean filter | N/A |
| 40 | `xct_voxel_mean5` | XCT voxel value, 5×5×5 mean filter | N/A |

## Frozen parser contract / 고정 parser contract
1. ZIP bytes must match the F22/NIST NERDm SHA-256 before structural inspection.
2. CSV files are parsed with **no header**; every physical CSV line is a data row.
3. Each non-empty row must parse as exactly 40 comma-separated fields.
4. Each field must be numeric-serializable (`float`) or a standard missing numeric token parseable by Python float (e.g. `NaN`).
5. Numerical values, minima/maxima, distributions, correlations, ranks, feature selection and model outputs must **not** be emitted or computed in F23.
6. Structural outputs may include only counts: files, rows, malformed-row counts, observed field-count set, and numeric-parse failure counts.
7. Hierarchy is `row(measured point) ⊂ layer CSV ⊂ part archive`; rows/layers/parts are not declared statistically independent replicates.
8. Raw ZIP/CSV bytes remain transient-only; no artifact/cache/raw commit.

## Exposure inheritance / 사전노출 상속
F22 disclosed a limited unintended first-row numerical exposure during a mistaken header check. Therefore F23 and all descendants inherit:
`NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED`.

F23 must not claim pristine outcome blindness. No additional numerical-value exposure is authorized.

## Frozen gates / 고정 판정
### `PASS_F23_HEADERLESS_40_COLUMN_MAPPING_READY`
Requires:
- authoritative AMS 100-69 positions 1..40 frozen;
- all four ZIP hashes match F22/NIST NERDm;
- all 1000 CSVs structurally inspected;
- every non-empty row has exactly 40 fields;
- every field is numeric/NaN serializable;
- no additional numerical values emitted;
- deterministic raw position → semantic map frozen.

### `PARTIAL_F23_MAPPING_READY_WITH_STRUCTURAL_EXCEPTIONS`
Use when the authoritative map is frozen but one or more bounded structural exceptions exist and are explicitly quantified.

### `HOLD_F23_SERIALIZATION_UNVERIFIED`
Use when raw structural verification cannot be completed without guessing or unavailable source bytes.

### `REJECT_F23_MAPPING_CONFLICT`
Use if observed serialization cannot be reconciled with the authoritative 40-column contract without changing column order or inventing undocumented semantics.

## Consequence / 후속
A numerical process/melt-pool ↔ XCT experiment remains prohibited during F23. Only a PASS may permit a **new, separately preregistered low-degree-of-freedom experiment design**, explicitly carrying the F22 limited pre-exposure disclosure.

## Cost / 비용
Only zero-incremental-cost official public routes and standard public GitHub-hosted runners are authorized. Any potentially billable action requires explicit prior user approval.
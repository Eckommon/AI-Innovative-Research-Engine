---
id: US-EIA-RET-N01-RESULT
type: prospective-design-result
created: 2026-09-30
issue: 185
research: US-EIA-RET-N01
disposition: HOLD
contract_commit: 21f28f1cefe65043493a8b3e7c55f0b9e033b212
attempt_01_commit: af5db251f0b08c7fd6e4bc3925d78929b27d58f3
attempt_01_run: 36633340471
gate: HOLD_US_EIA_RET_N01_REDUNDANCY_MATCHED_COHORT_NOT_READY
---

# US-EIA-RET-N01 Result / 결과

## Terminal disposition / 최종 판정

**`HOLD_US_EIA_RET_N01_REDUNDANCY_MATCHED_COHORT_NOT_READY`**

Attempt 01 is valid and passes **16/18** frozen gates. Failed gates are **10 and 11**.

Attempt 01은 유효하며 고정 gate **16/18**을 통과했습니다. 실패 gate는 **10, 11**입니다.

Because the pre-Issue contract requires exactly 18/18 PASS and prohibits rematching, caliper expansion, stratum merging, threshold relaxation or exposure redefinition after observation, this N01 is terminal HOLD.

## Frozen baseline integrity / baseline 무결성

All twelve EIA-860M workbook bodies, September 2025 through August 2026, exactly matched the F01 fingerprints.

- F01 evidence commit: `d96ccc4346484cb39f719f98eeaca75b142d1301`
- 12/12 SHA-256 fingerprints: exact match
- post-August-2026 EIA-860M body opened: **false**
- Retired row bodies opened: **0**
- Planned/Proposed row bodies opened: **0**
- EIA-923 row bodies opened: **0**
- future retirement membership opened: **false**

## Eligible cohort / 적격 cohort

August-2026 exact Operating pairs:

> **28,377**

Generators satisfying ≥6/12-month continuity:

> **27,757 / 28,377 = 97.8151%**

Eligible generators after all frozen eligibility rules:

> **27,756**

Frozen minimum:

> ≥ 15,000

### Exposure/control support

- `REDUNDANT_3PLUS`: **12,323**
- `PURE_SINGLETON`: **10,793**
- excluded group-size 2: **3,936**
- excluded singleton at mixed/multi-generator plant: **704**
- common exact strata: **389**

All support gates pass.

## Deterministic matching / 결정론적 매칭

Frozen 1:1 no-replacement algorithm produced:

> **881 matched pairs**

Matching integrity remained exact:

- duplicate control use: **0**
- exact-stratum mismatch: **0**
- caliper failures: **0**
- cross-arm Plant ID overlap: **0**

Matched plant support also passed:

- exposed plants: **397**
- control plants: **873**

## Failed gate 10 — matched cohort size

Observed:

> **881 matched pairs**

Frozen minimum:

> **2,000 pairs**

Therefore Gate 10 fails.

## Failed gate 11 — exposed match coverage

Eligible exposed:

> **12,323**

Matched exposed:

> **881**

Coverage:

> **7.1492331%**

Frozen threshold:

> **40.00%**

Therefore Gate 11 fails decisively.

The exact strata and calipers produced a scientifically clean but much smaller common-support region than prospectively required. This is not an implementation defect.

## Balance quality / 균형 품질

Within the matched cohort, balance is excellent:

- `|SMD(log capacity)| = 0.0033221`
- `|SMD(operating age)| = 0.0018628`

Frozen maximum for each:

> ≤ 0.10

Cluster concentration also passed:

- max exposed single-plant share: **1.1351%**
- max control single-plant share: **0.2270%**
- frozen maximum: **2.00%**

Therefore the failure is **support/coverage**, not covariate imbalance.

## Why no rescue / 사후구제 금지

This exact branch may not be rescued by:

- widening the age caliper above 8 years;
- widening capacity ratio beyond 2/3–1.5;
- removing Plant State, Sector, Status or age band from exact strata;
- merging strata after observation;
- lowering the 2,000-pair threshold;
- lowering 40% exposed coverage;
- redefining `REDUNDANT_3PLUS` or `PURE_SINGLETON`;
- using planned-retirement or EIA-923 information;
- opening future retirement outcomes and then tuning the match.

Any such change would be a new hypothesis/design, not a correction to this N01.

## Consequence / 후속 조치

- `US-EIA-RET-E01` is **not authorized**.
- No September-2026-or-later retirement membership may be opened under this branch.
- Preserve the 881-pair manifest SHA-256 `1f38b2f9b028aed41c7ae431f81606a41943a8ef56e8f16357db9549e6908f39` as negative design evidence.
- Return to independent Stage-0 portfolio reselection.

The result is informative: same-configuration redundancy and pure-singleton generators are individually abundant, but the prospectively frozen exact comparability rules leave insufficient overlap for the planned experiment.

Incremental monetary cost: **0 USD**.

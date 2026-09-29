---
id: US-EIA-RET-F01-RESULT
type: structural-feasibility-result
created: 2026-09-30
issue: 184
research: US-EIA-RET-F01
disposition: PASS
contract_commit: cce869991b94d8c1ef21c0b3dff401cfd57b0fe3
attempt_01_commit: 3bdc8193ccb5c9ce7e40bea5a483047d57d4fdbe
attempt_02_commit: d96ccc4346484cb39f719f98eeaca75b142d1301
attempt_02_run: 36631815352
gate: PASS_US_EIA_RET_F01_EXACT_GENERATOR_FUTURE_RETIREMENT_DESIGN_READY
---

# US-EIA-RET-F01 Result / 결과

## Terminal disposition / 최종 판정

**`PASS_US_EIA_RET_F01_EXACT_GENERATOR_FUTURE_RETIREMENT_DESIGN_READY`**

Attempt 02 is a valid empirical execution and passes **18/18** frozen gates.

Attempt 01 remains immutable but is superseded for scientific adjudication because its broad sheet matcher treated `Operating_PR` / `Retired_PR` as ambiguity against the exact source-native `Operating` / `Retired` sheets and therefore read zero authorized rows. Attempt 02 corrected only that deterministic sheet resolution under `IMPLEMENTATION_CORRECTION_02`; no scientific criterion changed.

## Longitudinal source evidence / 종단 source 근거

Exactly twelve official EIA-860M data months were resolved from the official index and fingerprinted:

- 2025-09 through 2025-12;
- 2026-01 through 2026-08.

All twelve workbook SHA-256 values were distinct. The latest August-2026 body is source-native current `/xls/`; prior months resolve through EIA's official `/archive/xls/` paths.

EIA's official source semantics also confirm that monthly files are preliminary/revisable and that the Retired tab from March 2017 onward comprehensively lists generators retired since 2002.

## Exact identity / exact 식별자

Across authorized Operating + Retired rows:

- nonblank identity rows: **420,610**
- valid exact Plant ID + Generator ID rows: **420,598**
- exact identity rate: **99.9971470%**
- frozen threshold: **99.99%**
- minimum within-month/sheet exact-key uniqueness: **100%**

No name, owner, address, geography or fuzzy identity repair was used.

## Operable longitudinal support / 운전 generator 종단 지원

August 2026 exact Operating generator pairs:

> **28,377**

Frozen threshold:

> ≥ 20,000

August-2026 generators appearing in Operating sheets for at least 6 of the 12 frozen months:

> **27,757 / 28,377 = 97.81513197%**

Frozen threshold:

> ≥ 85%

This establishes strong source-native identity persistence across the prospective baseline window.

## Retirement support / 은퇴 event 지원

Distinct exact generator pairs appearing in the twelve Retired sheets:

> **7,330**

Frozen threshold:

> ≥ 3,000

Pairs with parseable source-native retirement year + month:

> **7,314 / 7,330 = 99.78171896%**

Frozen threshold:

> ≥ 98%

Among **7,306** retired pairs present in two or more frozen monthly files:

> **7,300 = 99.91787572%**

retained one identical retirement year-month across observations.

Frozen threshold:

> ≥ 99.50%

The small set of changing retirement month values remains preserved in immutable evidence and is not repaired post hoc.

## Lifecycle exclusivity / lifecycle 배타성

August-2026:
- exact Operating pairs: **28,377**
- exact Retired pairs: **7,324**
- pair overlap: **0**
- overlap rate: **0%**

Frozen maximum:

> ≤ 0.10%

## Outcome and source firewall / 결과·source 방화벽

Throughout F01:

- September-2026-or-later 860M row body opened: **false**
- future retirement membership opened: **false**
- Planned/Proposed row bodies opened: **0**
- EIA-923 row bodies opened: **0**
- relationship computed: **false**
- prediction computed: **false**
- ranking computed: **false**
- causal claim: **false**
- identity repair: **false**
- incremental monetary cost: **0 USD**

## Consequence / 후속 조치

F01 PASS authorizes only a separate outcome-blind `US-EIA-RET-N01`.

N01 must prospectively freeze, before any post-August-2026 retirement membership is opened:

1. one non-tautological baseline exposure family;
2. August-2026 eligible Operating cohort;
3. exact exposure-source timing;
4. any EIA-923 join and aggregation level;
5. comparator/matching or stratification design;
6. generator-ID change / repowering / reactivation handling;
7. future observation horizon;
8. minimum retirement-event support and balance/statistical gates.

F01 does **not** authorize E01, future retirement access, retirement prediction, generator/operator ranking, investment recommendation or causal interpretation.

Incremental monetary cost: **0 USD**.

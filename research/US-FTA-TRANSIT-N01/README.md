---
id: US-FTA-TRANSIT-N01
type: outcome-blind-matched-reliability-design-identifiability
created: 2026-09-16
status: CONTRACT_FROZEN_PRE_ISSUE
parent_gate: PASS_US_FTA_TRANSIT_F01_AGENCY_MODE_TIME_JOIN_READY
parent_decision: DEC-207
safety_outcome_row_values_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-FTA-TRANSIT-N01 — Outcome-blind matched transit reliability design

## Objective / 목적

Following `PASS_US_FTA_TRANSIT_F01_AGENCY_MODE_TIME_JOIN_READY`, freeze and test a deterministic **exposure-side design manifest before any Breakdown-conditioned Major Safety Event row value is opened**.

The target later question is deliberately narrow:

> Among comparable Full Reporter transit operations, is a higher prior-year rate of **major mechanical failures per vehicle/passenger-car revenue mile** associated with a higher probability of at least one **Major Safety Event** in the next calendar year?

N01 is design-identifiability only. It may read annual Breakdowns exposure/service fields and quality flags. It must not read, query, persist, summarize, count or compare Major Safety Event row values.

## Frozen evidence available before contract / 계약 전 허용된 비결과 근거

The following preflights were completed while F01 was terminal and no N01 Issue existed:

- `SCHEMA_PREFLIGHT.json` — official metadata names/types only;
- `QUALITY_FLAG_PREFLIGHT.json` — categorical Breakdowns scope/quality values only, with exposure magnitudes not persisted;
- `OUTCOME_SCHEMA_PREFLIGHT.json` — downstream metadata names/descriptions only, with no event row values.

Observed non-outcome schema facts used to write this contract:

- Breakdowns exact fields include `ntd_id`, `mode`, `type_of_service`, `report_year`, `major_mechanical_failures`, `major_mechanical_failures_1`, `vehicle_passenger_car_revenue`, and its quality flag `vehicle_passenger_car_miles_2`;
- reporter type is `Full Reporter` for all 3,731 current Breakdowns rows;
- source-native TOS categories are `DO` and `PT`;
- quality-flag categories are blank, `Q`, `W`;
- downstream Major Safety/Security metadata exposes `_5_digit_ntd_id`, `mode`, `year`, `incident_date`, `incident_number`, `event_type`, `event_category`, and `safety_security`;
- the official `safety_security` metadata explicitly distinguishes Safety Events from Security Events.

No exposure magnitude distribution, future event occurrence, event count, safety/security category frequency, relationship, predictive score or effect estimate was opened before this contract.

## Frozen source / 고정 원천

### Exposure and service source

Official DOT/FTA Socrata dataset **`amkt-4ehs`** — `2022 - 2024 NTD Annual Data - Breakdowns`.

Only these row-value fields are authorized in N01:

- `ntd_id`
- `mode`
- `type_of_service`
- `reporter_type`
- `report_year`
- `major_mechanical_failures`
- `major_mechanical_failures_1`
- `vehicle_passenger_car_revenue`
- `vehicle_passenger_car_miles_2`

No Major Safety Events row endpoint is authorized in N01.

## Frozen source-row rules / 원천 행 규칙

Identity:
- `NTD ID`: trim whitespace only; no numeric rounding, name repair or aliasing;
- `mode`: exact uppercase source-native mode code;
- `TOS`: exact `DO` or `PT` only;
- report year: exact 2022, 2023 or 2024;
- reporter type must equal exact source value `Full Reporter`.

Quality:
- blank quality flag = usable;
- `Q`, `W`, or any other nonblank/unknown quality marker = unusable;
- if **any TOS component row** contributing to an agency-mode-year has a nonblank `major_mechanical_failures_1` or `vehicle_passenger_car_miles_2`, the **entire agency-mode-year is exposure-invalid**;
- no flagged component may be silently dropped while the remaining TOS is retained.

Numeric validity:
- `major_mechanical_failures` must be finite and >=0;
- `vehicle_passenger_car_revenue` must be finite and >0;
- source-grain duplicate `(NTD ID, mode, TOS, year)` with conflicting numeric/quality values invalidates that source key; no averaging or arbitrary last-row choice.

## Frozen agency-mode-year aggregation / 고정 집계

After exact source-grain validation only:

- aggregate across available clean `DO`/`PT` rows by **sum**;
- `major_failures_y = Σ_TOS major_mechanical_failures`;
- `vrm_y = Σ_TOS vehicle_passenger_car_revenue`;
- `tos_profile_y` = sorted exact set of present TOS values (`DO`, `PT`, or `DO+PT`);
- source-native agency-mode identity remains `(NTD ID, mode)`.

Primary exposure metric:

`major_failure_intensity_y = 1,000,000 × major_failures_y / vrm_y`

Higher values mean more major mechanical failures per million vehicle/passenger-car revenue miles. This is an exposure-side inverse-scaled reliability intensity; it is not itself an official agency safety rating.

## Frozen temporal unit / 고정 시간 단위

Potential exposure years are **2022 and 2023** only.

For candidate `(NTD ID, mode, y)`:

1. exposure-year aggregate `y` must be valid under the rules above;
2. follow-up-year `y+1` must have a valid positive `vrm_y+1` under a blank revenue-mile quality flag across all contributing TOS rows;
3. `tos_profile_y == tos_profile_y+1`;
4. no future event information may affect eligibility.

If the same `(NTD ID, mode)` is eligible for both `2022→2023` and `2023→2024`, retain **2022→2023 only**. Therefore each agency-mode appears at most once before agency-level de-duplication.

## One unit per agency / 기관당 1개 단위

To preserve independence for the later paired test, each NTD agency may contribute at most one mode.

If one `NTD ID` has multiple eligible modes after the earliest-year rule, retain exactly one by:

1. largest exposure-year `vrm_y`;
2. lexical uppercase `mode`;
3. earlier exposure year.

This selection is outcome-blind.

## Frozen exposure strata and quartiles / 고정 노출 층화

Exact stratum:

`mode × exposure_year × tos_profile`

A stratum is design-eligible only when it contains **>=12** retained agencies.

Within each eligible stratum:

1. sort units ascending by `(major_failure_intensity_y, NTD ID)`;
2. let `k = floor(n / 4)`;
3. LOW candidates = first `k` units;
4. HIGH candidates = last `k` units;
5. require `min(HIGH intensity) > max(LOW intensity)`; otherwise drop the entire stratum because a strict exposure contrast is not identifiable.

Middle 50% is not eligible for the matched primary design.

No safety outcome may be consulted to define quartiles, thresholds or strata.

## Frozen deterministic 1:1 matching / 결정론적 1:1 매칭

Match only HIGH to LOW within the same exact `mode × exposure_year × tos_profile` stratum.

Process HIGH candidates by:

`descending major_failure_intensity_y, NTD ID`

For each HIGH unit choose one unused LOW unit lexicographically by:

1. minimum `|log10(vrm_y_HIGH) - log10(vrm_y_LOW)|`;
2. minimum `|log10(vrm_y+1_HIGH) - log10(vrm_y+1_LOW)|`;
3. lexical LOW `NTD ID`.

A LOW unit is used once. No agency can appear in more than one final pair.

Persist an outcome-blind pair manifest containing only:
- pair ID;
- high/low NTD ID;
- exact mode;
- exposure year / follow-up year;
- stable TOS profile;
- exposure-year and follow-up-year VRM;
- exposure-year major failure count and intensity;
- matching distances;
- no safety-event field or future outcome membership.

## Frozen N01 PASS requirements / 고정 PASS 요건

All must pass:

1. Official `amkt-4ehs` metadata and actual zero-cost row bytes are readable.
2. Required exposure/service/quality fields exactly match the preregistered schema semantics.
3. Only exact `Full Reporter`, `DO`/`PT`, source-native NTD ID/mode and years 2022–2024 are used.
4. `Q`, `W`, and every unknown/nonblank quality flag fail closed at the whole agency-mode-year level.
5. No unresolved conflicting source-grain duplicate key is included.
6. At least **400 unique agencies** remain after temporal eligibility and one-unit-per-agency selection.
7. At least **8 design-eligible strata** satisfy `n>=12` and strict HIGH>LOW separation.
8. At least **100 deterministic HIGH/LOW matched pairs** are produced.
9. Matched pairs span at least **5 distinct mode codes**.
10. At least **80%** of matched pairs have both exposure-year and follow-up-year HIGH/LOW VRM ratios within **[1/3, 3]**.
11. Every final pair has strictly higher HIGH exposure intensity than LOW exposure intensity.
12. No NTD ID appears more than once anywhere in the final matched manifest.
13. A deterministic SHA-256 fingerprint of the canonical pair manifest is persisted.
14. `major_safety_event_row_values_opened = false`.
15. `future_safety_event_membership_opened = false`.
16. `relationship_computed = false`, `predictive_metric_computed = false`, `causal_claim_made = false`.
17. No paid source/API/runner, unofficial mirror or authentication bypass; incremental monetary cost = **0 USD**.

## Frozen N01 dispositions / 고정 판정

### PASS

`PASS_US_FTA_TRANSIT_N01_MATCHED_RELIABILITY_DESIGN_IDENTIFIABLE`

Use only if all 17 requirements pass.

### HOLD

`HOLD_US_FTA_TRANSIT_N01_MATCHED_RELIABILITY_DESIGN_NOT_IDENTIFIABLE`

Use after a valid evaluation when any preregistered source/schema/quality/cardinality/stratum/matching requirement fails.

A transient network/parser/workflow defect that prevents a valid evaluation is an implementation failure, not scientific HOLD. Fix implementation mechanics only; do not change this contract after exposure magnitudes are observed.

## Future E01 contract frozen prospectively / 향후 E01 계약 사전고정

Only after N01 PASS **and a separate E01 authorization** may the frozen pair manifest be joined to Major Safety/Security Events dataset `9ivb-8ae9`.

### Outcome source identity

Future E01 may read only the fields required to identify:
- exact `_5_digit_ntd_id`;
- exact `mode`;
- exact calendar `year`/`incident_date`;
- unique `incident_number` for deduplication;
- `safety_security` solely to retain Safety and exclude Security.

No severity, injury, fatality, property damage or narrative field is needed for the primary E01.

### Safety-only classification

Normalize `safety_security` by trimming and case-folding.

A row is eligible only if its normalized value:
- contains the token `safety`, **or**
- equals `sft`.

Any value containing `security`, blank/unknown values, or any category not deterministically recognized as Safety is excluded fail-closed. The allowed token rule is frozen before any category frequency or outcome count is read.

### Follow-up outcome

For each frozen high/low unit with exposure year `y`, follow-up year is exactly `y+1`.

`Y = 1` iff at least one deduplicated eligible **Safety** event exists with exact `NTD ID × mode` and calendar year `y+1`; otherwise `Y = 0`.

No same-year, multi-year, lead/lag alternative or severity-weighted outcome may replace this primary endpoint after results are seen.

### Primary paired statistic

For `N` frozen matched pairs:

- `risk_HIGH = mean(Y_HIGH)`;
- `risk_LOW = mean(Y_LOW)`;
- `RD = risk_HIGH - risk_LOW`;
- discordant counts: `b = HIGH=1, LOW=0`; `c = HIGH=0, LOW=1`;
- exact two-sided McNemar/binomial p-value on `b+c` under `p=0.5`;
- preregistered positive materiality floor: **RD >= +0.05**.

Future E01 gates:

- `PASS_POSITIVE_MATERIAL_US_FTA_TRANSIT_E01_RELATIONSHIP` iff `RD >= +0.05`, `p < 0.05`, and `b > c`;
- `POSITIVE_BELOW_MATERIALITY_US_FTA_TRANSIT_E01_RELATIONSHIP` iff `0 < RD < +0.05`, `p < 0.05`, and `b > c`;
- `NO_PREREGISTERED_POSITIVE_US_FTA_TRANSIT_E01_RELATIONSHIP` otherwise.

A negative estimate cannot be reversed into a protective-effect claim. Secondary event-count or severity analyses, if ever desired, require a new preregistered authorization and cannot rescue the primary E01.

## Claim boundary / 주장 경계

Even a future positive E01 would be **non-causal matched observational evidence**. It would not establish that mechanical failures cause safety events, that an agency is unsafe, or that FTA oversight should change. Residual confounding can remain from fleet age, maintenance practice, route environment, weather, operator exposure, passenger volume, reporting practice and other unmeasured factors.

## Exact next action / 정확한 다음 행동

Bind this already-frozen N01 contract to one dedicated Issue, authorize it in canonical state, then execute only the exposure-side Breakdowns design runner. Major Safety/Security event row values must remain unopened throughout N01.

Incremental monetary cost remains **0 USD**.

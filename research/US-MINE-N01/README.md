---
id: US-MINE-N01
type: outcome-blind-design-identifiability
state: AUTHORIZED_OUTCOME_BLIND_DESIGN
issue: 135
parent: US-MINE-F01
decision: DEC-185
created: 2026-09-16
injury_outcome_values_opened: false
accident_source_read: false
production_scope_restricted: true
incremental_monetary_cost_usd: 0
---

# US-MINE-N01 — Operator-Hours Ramp-Up Design / 운영시간 급증 설계

## Purpose / 목적

**KO:** F01에서 확인한 결정론적 mine-quarter 구조 위에서, 사고·부상 결과를 열기 전에 단 하나의 exposure family와 비교설계를 고정하고 실제 지원 규모·매칭 식별성을 확인한다.

**EN:** On top of the deterministic mine-quarter structure established by F01, freeze exactly one exposure family and comparison design before opening any accident/injury outcome, then test exposure-only support and match identifiability.

## Frozen exposure family / 고정 exposure family

`ALL_SECTOR_OPERATOR_HOURS_RAMP_UP`

- Coal + Metal/Nonmetal 모두 포함하되 exact `COAL_METAL_IND`로 층화한다. / Include Coal + Metal/Nonmetal, stratified by exact `COAL_METAL_IND`.
- Exposure는 operator `HOURS_WORKED`만 사용한다. / Use operator `HOURS_WORKED` only.
- Metal/Nonmetal 생산량 비의무 보고 때문에 `PRODUCTION_SCOPE_RESTRICTED`는 계속 구속된다. / `PRODUCTION_SCOPE_RESTRICTED` remains binding because Metal/Nonmetal production is not mandatory.
- N01은 Accidents source를 읽지 않는다. / N01 does not read the Accidents source.

## Frozen unit and support window / 고정 단위·기간

- support window: 2019–2025;
- unit: exact mine-quarter;
- aggregate operator hours across all reported subunits for the same mine-quarter;
- exact mine identity only; no fuzzy repair;
- exposure index quarter `t` requires positive hours in consecutive `t-1`, `t`, `t+1` quarters, all inside the frozen window.

## Frozen exposure transform / 고정 exposure 변환

`ramp_t = ln(HOURS_t / HOURS_(t-1))`

Inside each exact `COAL_METAL_IND × CAL_YR × CAL_QTR` stratum:
- exposed candidate = positive `ramp_t` at or above the empirical 80th percentile;
- control candidate = `ramp_t` between empirical 40th and 60th percentiles inclusive;
- quantiles use exposure data only.

**Quantile implementation is frozen before execution:** all 20/40/60/80-percentile cutpoints use the deterministic nearest-rank rule `Q(p)=x[ceil(p*n)-1]` on ascending values. Baseline-hours decile cutpoints use the same nearest-rank rule at p=0.1,...,0.9; a value exactly on a cutpoint remains in the lower decile. No interpolation or post-support alternative is allowed.

## Frozen deterministic matching / 고정 결정론적 매칭

1:1 without replacement:
1. exact sector;
2. exact exposure year-quarter;
3. exact state;
4. exact baseline-hours decile, computed from `HOURS_(t-1)` inside the same sector×quarter stratum;
5. each mine used at most once, earliest eligible chronological candidate role retained;
6. choose control minimizing absolute difference in `ln(HOURS_(t-1))`; lexical `MINE_ID` tie-break.

Matching is processed by exposure quarter in chronological order, then exposed `MINE_ID` lexically. A mine used as either exposed or control is unavailable thereafter. No fallback geography/sector/time rule is permitted after support is observed.

## Frozen later outcome contract boundary / 후속 결과계약 경계

N01 does not open outcomes. It freezes only the later target:
- outcome window: `t+1`;
- operator-attributed injury records only; contractor-attributed records excluded;
- denominator: operator `HOURS_WORKED` in `t+1`;
- primary future estimand: matched exposed/control injury incidence-rate ratio;
- secondary descriptive quantity: incidence-rate difference per 200,000 operator hours;
- later positive-materiality threshold: IRR >= 1.25 plus a separately preregistered inferential-significance rule.

Exact injury inclusion codes and statistical test remain forbidden until a separate E01 authorization is written before injury values are opened.

## Frozen PASS requirements / 고정 PASS 요건

- exact F01 Mines + quarterly-employment source hashes reproduce; source drift fails closed;
- no accident source or injury field/value is read;
- no conflicting mine-quarter hours aggregation;
- >= 8,000 mines have >=1 eligible `(t-1,t,t+1)` sequence;
- both C and M sectors have exposed + control candidates;
- >= 2,000 deterministic pairs;
- >= 30 states represented in matched pairs;
- >= 300 matched pairs in each C and M sector;
- canonical pair identities and SHA-256 fingerprint frozen;
- incremental monetary cost = 0 USD.

## Frozen dispositions / 고정 판정

- `PASS_US_MINE_N01_HOURS_RAMP_MATCHED_DESIGN_IDENTIFIABLE`
- `PARTIAL_US_MINE_N01_EXPOSURE_IDENTIFIABLE__MATCH_SUPPORT_PENDING`
- `HOLD_US_MINE_N01_SOURCE_OR_DESIGN_SUPPORT`

## Claim boundary / 주장 경계

A PASS is design identifiability only. It is not evidence that operational ramp-up predicts or causes injuries. No positive, negative, protective, sector-specific or causal interpretation is authorized.

Official source basis / 공식 근거: MSHA Open Government quarterly employment/production data and MSHA Part 50 subunit/worktime documentation.

Incremental monetary cost: **0 USD**.

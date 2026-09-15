---
id: US-UTIL-N01
type: outcome-blind-design-identifiability
state: AUTHORIZED_OUTCOME_BLIND_DESIGN
issue: 137
parent: US-UTIL-F02
portfolio_parent: PORTFOLIO-R28
decision: DEC-188
created: 2026-09-16
reliability_magnitudes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-UTIL-N01 — AMI Penetration Ramp × Future SAIDI Design
# US-UTIL-N01 — AMI 보급률 급증 × 미래 SAIDI 설계

## Purpose / 목적

Freeze exactly one EIA-861 AMI exposure and one future Reliability basis before opening Reliability magnitudes, then test whether an independent matched design is structurally identifiable.

EIA-861 Reliability/Advanced Metering cross-source panel에서 Reliability 수치를 열기 전에 단 하나의 AMI exposure와 미래 outcome basis를 고정하고, 독립 비교설계가 실제로 식별 가능한지 검증한다.

## Frozen unit / 고정 단위

- exact `Utility Number × State × exposure year t`;
- support years 2019–2024;
- exposure years 2020–2023;
- no invented county weights;
- no national aggregation across a multi-state utility;
- each Utility Number may enter at most one frozen pair globally.

## Frozen exposure / 고정 exposure

For exact utility-state-year rows:

`AMI_SHARE_y = AMI_TOTAL_y / (AMI_TOTAL_y + AMR_TOTAL_y + STANDARD_NON_AMR_AMI_TOTAL_y)`

All fields are exact `Total` meter fields from the official EIA-861 Advanced Metering schedule. Denominator must be positive and share must lie in `[0,1]`.

`DELTA_AMI_t = AMI_SHARE_t - AMI_SHARE_(t-1)`

Within each exact exposure year `t`:
- exposed = positive delta at or above nearest-rank Q80;
- control = nearest-rank Q40 through Q60 inclusive;
- exposed takes precedence if duplicate cutpoints overlap roles;
- nearest-rank `Q(p)=x[ceil(p*n)-1]`; no interpolation.

## Frozen future outcome basis / 고정 미래 outcome basis

N01 reads no Reliability magnitude. Structural blank/nonblank support only is allowed.

Future E01 primary outcome, if separately authorized:

`DELTA_SAIDI_(t+1) = IEEE_SAIDI_WITH_MED_(t+1) - IEEE_SAIDI_WITH_MED_t`

Primary future estimand:

`mean_pair[(DELTA_SAIDI_exposed) - (DELTA_SAIDI_control)]`

Negative values favor exposed utilities. Prospective project materiality is **<= -30 minutes/customer-year**. This is a project decision threshold, not an EIA or IEEE standard. Inferential test details remain for a separate E01 preregistration before SAIDI magnitudes are opened.

## Frozen matching / 고정 매칭

Process exposure years chronologically, then exposed rows lexically by `(Utility Number, State)`.

Control must have:
1. exact exposure year;
2. exact State;
3. baseline AMI-share difference <= 0.10;
4. baseline total-meter ratio in `[0.5, 2.0]`;
5. IEEE-with-MED SAIDI structural support at both `t` and `t+1`.

Choose minimum:

`distance = abs(share_e-share_c)/0.10 + abs(log(size_e/size_c))/log(2)`

Tie-break lexical `(Utility Number, State)`. Once a Utility Number is used on either side, it is globally unavailable thereafter.

No fallback or post-support rescue.

## Storm/dependence boundary / 폭풍·의존성 경계

The primary design is explicitly **non-causal**. Exact state/year matching reduces broad state/year heterogeneity but does not remove local storm confounding. NOAA storm magnitudes are not used in N01, and existing utility→county mappings are not weighted because no defensible customer weights were established. Any storm sensitivity analysis requires prospective E01 rules before Reliability magnitude access.

Global single-use of Utility Number is the primary pseudoreplication control.

## Frozen PASS requirements / 고정 PASS 요건

1. All 2019–2024 EIA-861 final ZIP hashes exactly reproduce F02 source hashes.
2. Every year exposes exact Utility Number, State, AMI Total, AMR Total and Standard(non-AMR/AMI) Total routes.
3. Every year exposes structurally identifiable IEEE SAIDI With MED; values remain unopened.
4. No conflicting duplicate utility-state-year AMI records.
5. >=500 distinct utilities have >=1 structurally eligible design sequence.
6. Each exposure year 2020–2023 has both exposed and control candidates.
7. >=300 exposed and >=300 control candidates before global single-use matching.
8. >=150 deterministic 1:1 pairs.
9. >=25 states, >=3 represented exposure years, and every represented exposure year >=30 pairs.
10. Pair identities + SHA-256 fingerprint frozen before future outcome authorization.
11. No Reliability magnitude access, no relationship computation, no invented county weights, cost 0 USD.

## Frozen dispositions / 고정 판정

- `PASS_US_UTIL_N01_AMI_RAMP_MATCHED_DESIGN_IDENTIFIABLE`
- `PARTIAL_US_UTIL_N01_AMI_EXPOSURE_IDENTIFIABLE__MATCH_SUPPORT_PENDING`
- `HOLD_US_UTIL_N01_SOURCE_OR_DESIGN_SUPPORT`

## Claim boundary / 주장 경계

PASS would mean design identifiability only. It would not show that AMI improves reliability, reduces outages, creates resilience, or causes any outcome direction.

Incremental monetary cost: **0 USD**.

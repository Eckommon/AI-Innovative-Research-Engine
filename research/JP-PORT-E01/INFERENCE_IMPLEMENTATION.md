---
id: JP-PORT-E01-INFERENCE-IMPLEMENTATION
type: pre-stage-b-inference-freeze
created: 2026-09-04
issue: 80
relationship_outcome_computed: false
primary_weather_summary_computed: false
incremental_monetary_cost_usd: 0
---

# JP-PORT-E01 Inference Implementation Freeze
# JP-PORT-E01 추론 구현 고정

This file freezes numerical implementation details after Stage A PASS and before any Stage B weather-throughput relationship is calculated.

## Frozen estimating equation

For eligible port-month rows only:

Y_p,t = beta W_s(p),t + alpha_p + gamma_t + epsilon_p,t

where:
- Y_p,t = log1p(monthly total maritime cargo);
- W_s(p),t = calendar-month maximum of quality-code-8 JMA daily maximum wind speed for the frozen station;
- alpha_p = port fixed effects;
- gamma_t = year-month fixed effects.

No additional regressors, lags, leads, interactions, port trends or alternate weather variables are allowed.

## Fixed-effects implementation

Estimate beta by Frisch-Waugh-Lovell residualization:

1. construct a design matrix containing:
   - the primary predictor W;
   - port dummy indicators, omitting one reference port;
   - year-month dummy indicators, omitting one reference month;
2. fit OLS on the eligible rows;
3. report the coefficient on W.

The choice of omitted dummy categories does not affect beta.

## Cluster-robust inference

Primary clustering variable:
**JMA history station ID**.

Use one-way cluster-robust CR1 covariance:

V_CR0 = (X'X)^(-1) [sum_g X_g' u_g u_g' X_g] (X'X)^(-1)

V_CR1 = V_CR0 * [G/(G-1)] * [(N-1)/(N-K)]

where:
- G = number of JMA station clusters represented in the realized Stage-B sample;
- N = regression observations;
- K = rank/full column count of the fitted design matrix.

Primary standard error:
sqrt(V_CR1[beta,beta]).

Primary 95% confidence interval:
beta ± t_(0.975, G-1) * SE_CR1.

Primary two-sided p-value:
2 * P(T_(G-1) >= abs(beta/SE_CR1)).

## Primary gate

PASS_E01_NEGATIVE_EXTREME_WIND_CARGO_ASSOCIATION only if:
- Stage-B integrity passes;
- beta < 0;
- the upper endpoint of the frozen two-sided 95% station-clustered confidence interval is < 0.

Otherwise, if integrity passes:
NO_E01_NEGATIVE_EXTREME_WIND_CARGO_ASSOCIATION.

## Missingness and realized panel

Use only rows present in the frozen Stage-A panel-key manifest.

Stage B may additionally drop a frozen key only if:
- the corresponding re-downloaded JMA value fails the already frozen quality/homogeneity/completeness rule;
- the MLIT monthly cargo cell is blank/non-numeric.

No imputation.

Any Stage-B source drift that changes the frozen source identity or makes the model non-estimable yields:
HOLD_E01_SOURCE_OR_PANEL_INTEGRITY.

## Descriptive effect translation

Report the model-implied change for a fixed +5 m/s contrast:

100 * [exp(5*beta) - 1] percent

This is a log-model descriptive translation only.
It is not a second hypothesis test, not a materiality threshold and not a causal estimate.

## Numerical reproducibility

Stage B must persist:
- package/runtime versions;
- exact MLIT hashes;
- exact JMA raw-response hashes used by Stage B;
- realized N, G and K;
- beta, CR1 SE, t statistic, p value and 95% CI;
- +5 m/s descriptive translation;
- final frozen gate.

Incremental monetary cost remains **0 USD**.

---
id: US-EPA-XMEDIA-E01
type: preregistered-paired-outcome-experiment
created: 2026-09-17
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-EPA-XMEDIA-N01
parent_gate: PASS_US_EPA_XMEDIA_N01_MATCHED_MONITORING_INTENSITY_DESIGN_IDENTIFIABLE
parent_staging_commit: 78f0f0f1458463c79c326c016d415dc5533af026
parent_manifest_sha256: 19e1b3a1963fe008811aa230336e12ec69a348b03cf37bd656ea9d3fba8e5aaf
parent_pairs: 307
outcome_rows_opened: false
incremental_monetary_cost_usd: 0
---

# US-EPA-XMEDIA-E01 — preregistered 2024 E90 paired outcome gate

## Binding / 구속 조건

This E01 **does not alter** the endpoint, outcome window, pair membership, statistical test or gate frozen prospectively in `US-EPA-XMEDIA-N01` before any outcome access.

E01 is bound to exactly:

- N01 contract: `12f30d5d27d7d4f27022bc355c2a0c62a76e9f0c`
- N01 immutable staging commit: `78f0f0f1458463c79c326c016d415dc5533af026`
- N01 pair-manifest SHA-256: `19e1b3a1963fe008811aa230336e12ec69a348b03cf37bd656ea9d3fba8e5aaf`
- frozen matched pairs: **307**
- matched states: **AL, AR, CA, FL, GA, IN, KY, MD, MI, MO, MS, NC, NJ, NV, OH, OR, PA, SC, TN, TX, WI, WV**

No pair may be added, removed, rematched, reweighted or re-stratified after outcome access.

## Official outcome source / 공식 결과 소스

Primary outcome source is only the official EPA ECHO ICIS-NPDES Part 2 effluent-violations table distributed through the current state bulk-download route:

`https://echo.epa.gov/files/echodownloads/NPDES_by_state_year/{STATE}_NPDES_EFF_VIOLATIONS.zip`

E01 may download **only the 22 frozen matched states** above. Each ZIP must contain the state distribution of `NPDES_EFF_VIOLATIONS` and only the four frozen primary fields are logically consumed:

- `NPDES_ID`
- `NPDES_VIOLATION_ID`
- `VIOLATION_CODE`
- `MONITORING_PERIOD_END_DATE`

No DMR measurement/value/limit file, pollutant field, exceedance magnitude, enforcement field, penalty, narrative, QNCR history or RCRA violation/enforcement outcome is authorized.

This state-scoped route is a transport optimization only; it does not change the prospectively frozen source table or endpoint.

## Primary endpoint / 1차 결과변수

For each NPDES ID already frozen in the N01 manifest:

1. retain only rows with exact normalized `VIOLATION_CODE = E90`;
2. parse `MONITORING_PERIOD_END_DATE` fail-closed;
3. retain only dates in calendar **2024** (`2024-01-01` through `2024-12-31`);
4. require nonblank `NPDES_VIOLATION_ID`;
5. deduplicate by exact `NPDES_VIOLATION_ID` within NPDES ID;
6. `Y = 1` iff at least one qualifying unique 2024 E90 row exists;
7. otherwise `Y = 0`.

`D80` and `D90` reporting non-receipt violations are excluded. No secondary endpoint is authorized in E01.

## Frozen paired statistics / 고정 쌍 통계

For the 307 frozen HIGH–LOW pairs only:

- `risk_HIGH = mean(Y_HIGH)`
- `risk_LOW = mean(Y_LOW)`
- `RD = risk_HIGH - risk_LOW`
- `b = count(HIGH=1, LOW=0)`
- `c = count(HIGH=0, LOW=1)`
- `n_discordant = b + c`
- exact two-sided McNemar/binomial p-value on `b+c` under `p=0.5`.

Exact two-sided p-value rule:

- if `b+c = 0`, `p = 1.0`;
- otherwise `p = min(1, 2 * P[Binomial(n=b+c, 0.5) <= min(b,c)])`.

Materiality floor remains **`RD >= +0.05`**.

## Frozen decision gates / 고정 판정 게이트

### Positive material

`PASS_POSITIVE_MATERIAL_US_EPA_XMEDIA_E01_RELATIONSHIP`

iff all are true:

- `RD >= +0.05`
- exact two-sided `p < 0.05`
- `b > c`

### Positive but below materiality

`POSITIVE_BELOW_MATERIALITY_US_EPA_XMEDIA_E01_RELATIONSHIP`

iff all are true:

- `0 < RD < +0.05`
- exact two-sided `p < 0.05`
- `b > c`

### Otherwise

`NO_PREREGISTERED_POSITIVE_US_EPA_XMEDIA_E01_RELATIONSHIP`

A negative estimate must **not** be reframed as a protective-effect claim. The study is observational and noncausal.

## Execution integrity / 실행 무결성

Before computing outcomes, the runner must verify:

1. N01 manifest contains exactly 307 pairs;
2. N01 manifest SHA-256 exactly matches `19e1b3a1963fe008811aa230336e12ec69a348b03cf37bd656ea9d3fba8e5aaf`;
3. no Registry ID, RCRA SOURCE_ID or NPDES ID is reused;
4. each pair still satisfies HIGH exposure count > LOW;
5. downloaded state set is exactly the frozen 22-state set;
6. required outcome columns are present;
7. any malformed qualifying-date row is excluded fail-closed rather than repaired;
8. no source other than the 22 official EFF_VIOLATIONS ZIPs is used for outcome classification.

The immutable staging artifact should persist aggregate counts/statistics and source fingerprints, but **must not persist facility-level Y labels, facility rankings or enforcement-targeting scores**.

## Interpretation boundary / 해석 경계

Even if the positive gate passes, the permitted conclusion is limited to an observational association in this frozen matched design: facilities in the higher recent RCRA monitoring-intensity group had a higher probability of at least one 2024 E90 NPDES effluent violation than their matched lower-intensity counterparts.

It must not be described as:

- causal effect of inspection/monitoring;
- regulatory effectiveness/ineffectiveness;
- proof of facility dangerousness;
- enforcement priority or risk-ranking score;
- evidence about any named individual facility.

## Cost boundary / 비용 경계

Incremental monetary cost must remain **0 USD**. No paid API, paid dataset or paid compute may be used without explicit user approval.


## Terminal E01 result / E01 최종 결과

**`NO_PREREGISTERED_POSITIVE_US_EPA_XMEDIA_E01_RELATIONSHIP`** — Run `35168068999`: HIGH **5.54%**, LOW **3.58%**, RD **+1.95pp**, `b/c=12/6`, exact p **0.237885**. The frozen positive/material gate was not met. No rescue or secondary-endpoint mining is authorized. See `RESULT.md`.

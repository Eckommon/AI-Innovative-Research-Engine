---
id: US-MINERAL-E01
type: controlled-cross-agency-experiment
state: PREREGISTERED_OUTCOME_BLIND
created: 2026-09-04
parent_candidate: C-US-003R
parent_feasibility: US-MINERAL-F01
issue: 75
decision: DEC-105
mission_anchor: MEM-054
incremental_monetary_cost_usd: 0
---

# US-MINERAL-E01 — 2023 Critical-Mineral Source × Unlading-District Dual Trade-Value Concentration
# US-MINERAL-E01 — 2023 핵심광물 공급국 × 양하 세관구역 이중 무역가치 집중도

## 1. Research question / 연구 질문

**EN:** Across the complete prospectively qualified eight-mineral universe, does 2023 published U.S. general-import trade value show a replicated structure in which both foreign country-of-origin concentration and domestic district-of-unlading concentration are materially high?

**KO:** 결과 보기 전에 확정된 8개 핵심광물 전체에서, 2023년 미국 일반수입 무역가치가 해외 원산국과 미국 양하 세관구역 두 축 모두에서 물질적으로 높은 집중도를 보이는 사례가 반복적으로 존재하는가?

This experiment measures **published trade-value exposure structure**. It does not measure physical elemental tonnage or causal disruption risk.

## 2. Authorization / 승인

Authorized by:
- `research/US-MINERAL-F01/RESULT.md` — `PASS_US_MINERAL_TRADE_IMPORT_NODE_JOIN_READY`;
- `registry/CLM-124.md`;
- `registry/DEC-105.md`.

Issue:
- #75 `US-MINERAL-E01`.

No 2023 Census trade-value row was opened in F01 or in creating this preregistration.

## 3. Frozen mineral universe / 고정 광물 universe

Exactly these eight minerals:

1. Antimony
2. Barite
3. Beryllium
4. Palladium
5. Phosphate
6. Potash
7. Rhodium
8. Tellurium

No mineral may be added, removed, substituted or re-mapped after outcome exposure.

The exact mineral→2023 HTS10 mapping is imported unchanged from:
- `research/US-MINERAL-F01/MAPPING_IDENTIFIABILITY.md`.

## 4. Frozen official sources / 고정 공식 소스

### USGS semantic bridge
USGS OFR 2025-1047, Appendix 2.

Role:
- mineral identity;
- official trade-code semantics;
- mapping caveats.

### Census outcome source
2023 monthly Merchandise Trade Imports public static ZIPs:

`https://www.census.gov/trade/downloads/2023/Merch/im_m/IMDB23<MM>.ZIP`

Use `IMP_DETL.TXT` only, parsed according to the official fixed-width record layout:

`https://www.census.gov/foreign-trade/reference/products/layouts/imdb.html`

The complete F01 execution semantics are inherited unchanged from:
- `research/US-MINERAL-F01/EXECUTION_CONTRACT.md`.

## 5. Frozen period / 고정 기간

**2023-01-01 through 2023-12-31**, represented by all 12 statistical months.

No alternate year, partial-year window or rolling window is authorized after numerical exposure.

## 6. Frozen primary weight / 고정 1차 가중치

`gen_val_mo` — **General Imports, Total Value**.

For each raw `IMP_DETL` row, use only the monthly field.

Do not:
- sum YTD fields across months;
- use `con_val_mo` as a post-hoc alternative;
- use quantity or shipping weight as the primary weight;
- transform trade value by the USGS content percentage, because multiplying dollars by elemental-content fraction does not produce a physical mineral quantity measure.

Interpret all primary results as **mapped general-import trade-value concentration**.

## 7. Frozen domestic node / 고정 국내 node

Primary node:

**`dist_unlad` — district of unlading**.

Source-semantic rationale frozen before outcomes:
- it is the Census district associated with where imported merchandise is unloaded;
- it better matches the domestic arrival/gateway interpretation than customs district of entry;
- it is available in `IMP_DETL` at the required 10-digit HTS grain for the complete eight-mineral universe.

Secondary sensitivity only:
- `dist_entry` — district of entry.

The HS6 port-of-unlading dataset is outside E01 primary testing. It cannot be introduced to rescue or strengthen E01 after outcomes.

## 8. Independent analytical unit / 독립 분석 단위

Primary unit:

**one mineral over the full frozen 2023 year**.

There are exactly **8 primary mineral units**.

Monthly rows, HTS10 codes, countries, country subcodes, districts and rate-provision records are nested contributors to each mineral's annual distribution. They are not treated as independent experimental replicates.

## 9. Frozen aggregation / 고정 집계

Raw identity key before aggregation:

`commodity × cty_code × cty_subco × dist_entry × dist_unlad × rate_prov × year × month`.

A repeated raw full key is fail-closed.

After raw-key validation, aggregate across:
- all 12 months;
- all frozen HTS10 codes belonging to the mineral;
- `cty_subco` and `rate_prov` when forming the research distributions.

### Country distribution
For mineral `m` and country `c`:

`V_country(m,c) = Σ gen_val_mo`.

`share_country(m,c) = V_country(m,c) / Σ_c V_country(m,c)`.

### Unlading-district distribution
For mineral `m` and district `d`:

`V_unlad(m,d) = Σ gen_val_mo`.

`share_unlad(m,d) = V_unlad(m,d) / Σ_d V_unlad(m,d)`.

The annual denominator for the country and district views must reconcile to the same mapped annual `gen_val_mo` total for each mineral. Any mismatch is numerical-integrity HOLD.

## 10. Frozen primary statistics / 고정 1차 통계

For each mineral `m`:

### Country HHI
`H_country(m) = Σ_c share_country(m,c)^2`.

### Unlading-district HHI
`H_unlad(m) = Σ_d share_unlad(m,d)^2`.

### Dual-concentration floor
`D(m) = min(H_country(m), H_unlad(m))`.

A mineral crosses the material dual-concentration rule only if **both** concentration axes cross the same threshold.

## 11. Frozen materiality rule / 고정 물질성 규칙

Prospective threshold:

**`τ = 0.25`**.

For a concentration distribution, `1 / HHI` can be interpreted as an effective-number heuristic. `HHI = 0.25` corresponds to an effective number of four equal-sized contributors.

This threshold is a **project heuristic chosen before outcomes**, not an antitrust/legal threshold and not a universal critical-mineral supply-risk standard.

Define:

`I_m = 1 if D(m) >= 0.25, else 0`.

Primary replicated count:

`K = Σ_m I_m`, over all eight frozen minerals.

## 12. Frozen primary gate / 고정 1차 게이트

### `PASS_E01_REPLICATED_DUAL_TRADE_VALUE_CONCENTRATION`
All structural/numerical integrity conditions pass and:

**`K >= 2`**.

Rationale: require replication across at least two prospectively selected minerals rather than treating a single striking mineral as sufficient branch evidence.

### `PARTIAL_E01_SINGLE_DUAL_TRADE_VALUE_CONCENTRATION`
Integrity passes and:

**`K = 1`**.

### `NO_E01_DUAL_TRADE_VALUE_CONCENTRATION`
Integrity passes and:

**`K = 0`**.

### `HOLD_E01_SOURCE_OR_NUMERICAL_INTEGRITY`
The complete eight-mineral frozen test cannot be executed without violating the preregistered source/mapping/duplicate/key/value rules.

No post-hoc mineral deletion is permitted to avoid HOLD.

## 13. Stage A — pre-numerical structural gate / 수치 전 구조 gate

Stage A must execute before `gen_val_mo` is parsed into numerical research values.

1. Download all 12 official 2023 Merchandise ZIPs in one execution.
2. Record access UTC timestamps.
3. SHA-256 hash every ZIP.
4. Locate the `IMP_DETL.TXT` member used from every month.
5. Record member filename, byte size and SHA-256.
6. Parse only fixed-width identity slices required for structural validation.
7. Verify row framing/length under the official record layout.
8. Verify source `year/month` matches its carrier month.
9. Filter only frozen HTS10 codes.
10. Verify raw full keys are unique.
11. Verify mandatory keys parse.
12. Verify each of the eight minerals has at least one mapped published row somewhere in the complete 2023 window.
13. Persist only manifest/hash/cardinality diagnostics.

If any required condition fails:

**`HOLD_E01_SOURCE_OR_NUMERICAL_INTEGRITY`**

and Stage B must not run.

Downloading the official source ZIPs necessarily transfers bytes containing numerical fields, but Stage A code shall not parse, aggregate, rank, emit or persist `gen_val_mo` values. Outcome exposure begins only in Stage B.

## 14. Stage B — numerical integrity / 수치 무결성

Only after Stage A passes:

1. parse `gen_val_mo` on frozen mapped rows;
2. require numeric finite non-negative values;
3. preserve zero as a valid published value;
4. use monthly fields only;
5. aggregate `cty_subco` and `rate_prov` only after raw-key validation;
6. require positive mapped annual total for each of all eight minerals;
7. require country and unlading-district annual denominators to reconcile exactly for each mineral;
8. preserve official country/district codes exactly as published;
9. do not impute suppressed quantity/weight or guess geographic disaggregation;
10. compute the frozen primary and secondary outputs once.

Any change needed to universe, mapping, year, primary weight, primary geography or threshold after Stage B begins is prohibited and yields HOLD rather than retuning.

## 15. Frozen secondary descriptives / 고정 2차 기술통계

These may be reported for interpretation but cannot alter the primary gate:

For every mineral:
- `H_country`;
- `H_unlad`;
- `D`;
- top-1 country share and country code/name;
- top-1 unlading-district share and district code/name;
- number of unique published countries with positive mapped value;
- number of unique published unlading districts with positive mapped value.

Sensitivity:
- `H_entry` using `dist_entry` on the same mapped values;
- `D_entry = min(H_country, H_entry)`.

Structural descriptives:
- joint `country × dist_unlad` HHI;
- Spearman rank association between the eight `H_country` and eight `H_unlad` values.

Secondary outcomes cannot rescue a primary PARTIAL/NO result and cannot authorize a new mineral/window/geography within E01.

## 16. Suppression/geography interpretation / 억제·지리 해석

Census documentation states that disclosure protection can suppress quantity/shipping weight and can affect published district/port presentation.

Rules:
- retain valid official special/combined geography codes as published;
- do not manually reallocate them;
- do not describe district concentration as transaction-level physical routing truth;
- primary wording is **published district-of-unlading trade-value concentration**.

## 17. Revision/snapshot rule / 개정·스냅샷 규칙

E01 uses exactly one contemporaneous 2023 Census snapshot manifest.

If any official file differs later by SHA-256:
- preserve the original manifest/result;
- treat the changed source as a new version;
- do not silently replace one or more months in an existing experiment.

All eight primary results must come from the same 12-month manifest.

## 18. Public result minimization / 공개 결과 최소화

Do not commit raw Census `IMP_DETL` rows.

Durable result may include:
- source manifest hashes and counts;
- mineral-level aggregate HHI/top-share/unique-count outputs;
- primary gate result;
- bounded secondary descriptives;
- code/version information needed for reproduction.

Raw source files remain external official Census assets.

## 19. Claim boundary / 주장 경계

A PASS means only:

> Under the frozen 2023 official mapping and published Census general-import values, at least two of the eight prospectively selected minerals cross the preregistered `HHI >= 0.25` threshold on both country-of-origin and district-of-unlading axes.

A PASS does **not** prove:
- physical mineral mass concentration;
- supply-disruption probability or economic impact;
- causal dependence on a gateway;
- transaction-level port routing;
- stockpile adequacy;
- domestic-processing bottlenecks;
- policy/investment superiority.

## 20. Stop and portfolio-return rule / 중단 및 포트폴리오 복귀

No same-branch tuning experiment is automatically authorized after E01.

After PASS/PARTIAL/NO/HOLD:
- persist the result and claim boundary;
- return to mission-level review before another outcome-bearing descendant.

Do not rescue E01 by:
- changing `τ`;
- changing 2023 to another year;
- selecting only interesting minerals;
- switching primary geography from unlading to entry;
- replacing `gen_val_mo` with another weight;
- adding the HS6 port route after outcomes.

## Cost / 비용

Incremental monetary cost remains **0 USD**. Any potentially billable tool, data source, runner or API requires explicit prior user approval.

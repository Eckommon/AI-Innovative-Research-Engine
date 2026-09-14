---
id: US-BRIDGE-N01
issue: 131
state: AUTHORIZED_OUTCOME_BLIND_DESIGN_IDENTIFIABILITY
created: 2026-09-14
condition_rating_values_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-BRIDGE-N01 — Outcome-blind matched inspection-interval design / 결과 비개봉 매칭 점검구간 설계

## Objective / 목적

Following `PASS_US_BRIDGE_F01_HAZARD_CONDITION_PANEL_JOIN_READY`, establish a deterministic exposed/control inspection-interval design **before any NBI bridge condition-rating value is opened**.

F01의 `PANEL_JOIN_READY` 이후, NBI 교량 상태등급 값을 열기 전에 재난 노출/비노출 inspection interval과 1:1 control matching을 결과 비개봉 상태에서 고정한다.

N01 is design-identifiability only. Items 58/59/60/62 condition values and their fixed-width bytes must not be read, parsed, persisted, summarized, ranked, compared, or tested.

## Frozen sources / 고정 소스

1. FHWA NBI legacy fixed-width annual archives, 2015–2025.
2. FEMA OpenFEMA `DisasterDeclarationsSummaries` v2, incident dates 2015-01-01 through 2024-12-31.
3. FHWA NBI record-format/data-check documentation for field semantics.

Official references:
- https://www.fhwa.dot.gov/bridge/nbi/format.cfm
- https://www.fhwa.dot.gov/bridge/nbi/checks/items.cfm
- https://www.fhwa.dot.gov/bridge/nbi/checks/cross.cfm
- https://www.fema.gov/about/openfema/data-sets#disaster-declarations-summaries

## Authorized non-outcome fields / 허용 비결과 필드

N01 may parse only:
- Item 1 State Code — first two characters as State FIPS;
- Item 8 Structure Number;
- Item 3 County Code;
- Item 27 Year Built — diagnostic only;
- Item 43B Structure Type — `19 = CULVERT`, otherwise deterministically coded `NON_CULVERT`;
- Item 90 Inspection Date;
- Item 91 Designated Inspection Frequency — cadence diagnostic only;
- Item 106 Year Reconstructed.

Condition Items 58/59/60/62 are forbidden at row-value level. Their byte positions must not be sliced.

## Bridge and inspection identity / 교량·점검 식별

- bridge key: `(state_fips, trimmed structure_number)`;
- county key: exact 5-digit `state_fips + county_code`;
- duplicate bridge key within an annual source: exclude the ambiguous **key-year only**;
- same Item 90 date repeated across annual archives is one inspection identity;
- if the same bridge+inspection date occurs in multiple archive years, retain the earliest archive-year representation;
- county must remain one stable valid FIPS across retained N01 inspection identities;
- bridge class must be stable across an interval;
- no fuzzy repair.

## Eligible consecutive interval / 적격 연속 점검구간

For each bridge, sort distinct inspection identities and form consecutive intervals only. Eligible iff:

1. post date > pre date;
2. interval length is **180–1095 days inclusive**;
3. county is valid and stable;
4. bridge class is deterministic and unchanged;
5. neither endpoint's Item 106 reconstruction year falls in `pre_year <= reconstruction_year <= post_year`;
6. neither endpoint comes from an ambiguous duplicate key-year.

Item 91 is descriptive only; actual interval days control matching.

## FEMA exposure / FEMA 노출

Qualifying event:
- declaration code `DR` (Major Disaster Declaration; v2 `declarationType` or documented deterministic equivalent);
- F01 physical-hazard incident set only;
- exact county FIPS;
- `pre_date < incidentBeginDate <= post_date`.

An interval is `EXPOSED` if >=1 qualifying event occurs; otherwise `UNEXPOSED`. Multiple events remain one analysis interval and are retained only as descriptive exposure metadata. No single index event is selected.

## One unit per bridge / 교량당 1개 단위

- exposed bridge: earliest exposed eligible interval by `(pre_date, post_date)`;
- control-candidate bridge: must have no exposed eligible interval anywhere in the retained 2015–2025 panel;
- each bridge may appear at most once in final matched pairs.

## Deterministic 1:1 matching / 결정론적 1:1 매칭

Exact stratum:

`state_fips × bridge_class × pre_inspection_year`

Process exposed intervals sorted by:

`state_fips, bridge_class, pre_year, pre_date, bridge_key`

Within stratum choose unused control by:
1. minimum absolute interval-length difference;
2. minimum absolute pre-date difference;
3. lexical control bridge key;
4. control post date.

Control bridge is removed globally after use. Outcome values cannot affect matching.

## Frozen PASS requirements / PASS 기준

1. all sources accessible at 0 incremental monetary cost;
2. all 11 NBI years preserve required non-outcome schema and condition bytes remain unopened;
3. >= **300,000** unique bridges with >=1 eligible interval;
4. >= **10,000** unique exposed bridges;
5. >= **100,000** unique control-candidate bridges;
6. >= **10,000** deterministic matched pairs;
7. matched pairs span >= **30** state/territory FIPS;
8. >= **500 CULVERT** matched pairs and >= **8,000 NON_CULVERT** matched pairs;
9. >= **90%** matched pairs have interval-length difference <=365 days;
10. no fuzzy repair, outcome-dependent inclusion, outcome-field access, or paid source;
11. raw bytes transient; durable output only hashes, counts, identities, time/exposure/non-outcome design metadata.

## Frozen N01 dispositions / 고정 판정

- `PASS_US_BRIDGE_N01_MATCHED_INTERVAL_DESIGN_IDENTIFIABLE`
- `PARTIAL_US_BRIDGE_N01_INTERVAL_DESIGN_READY_MATCH_SUPPORT_PENDING`
- `HOLD_US_BRIDGE_N01_DESIGN_NOT_IDENTIFIABLE`

No source/window/matching/threshold rescue after execution.

## Future E01 contract frozen prospectively / 향후 E01 계약 사전고정

Only after N01 PASS and a separate E01 authorization may condition values be opened for the exact frozen pair manifest.

- `CULVERT`: Item 62 numeric 0–9 at both endpoints; deterioration if `post <= pre - 1`.
- `NON_CULVERT`: Items 58/59/60; use the common numeric component set present at both endpoints, require >=2 common numeric components, score = minimum of that common set, deterioration if `post_score <= pre_score - 1`; otherwise missing.
- primary later statistic: exposed deterioration risk minus matched-control deterioration risk;
- exact two-sided McNemar/binomial test on discordant matched pairs;
- positive materiality floor: **+5 percentage points**.

Future positive gates, only if separately authorized:
- `PASS_POSITIVE_MATERIAL_US_BRIDGE_E01_RELATIONSHIP`: RD >= +0.05 and p < 0.05;
- `POSITIVE_BELOW_MATERIALITY_US_BRIDGE_E01_RELATIONSHIP`: 0 < RD < +0.05 and p < 0.05;
- `NO_PREREGISTERED_POSITIVE_US_BRIDGE_E01_RELATIONSHIP`: otherwise.

A negative estimate cannot be reversed into a protective-effect claim.

## Claim boundary / 주장 경계

Any later E01 is non-causal county-declaration/inspection-condition association evidence only. It cannot establish that disasters caused bridge deterioration. County exposure error, inspection ascertainment, maintenance/repair, severity, aging, traffic/environment, and unobserved intervention remain limitations. Static bridge-hazard mapping and generic deterioration prediction are not novelty claims.

Incremental monetary cost: **0 USD**.

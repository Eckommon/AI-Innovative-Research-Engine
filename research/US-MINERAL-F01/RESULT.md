---
id: US-MINERAL-F01-RESULT
type: source-semantic-join-feasibility-result
created: 2026-09-04
issue: 74
state: COMPLETED_PASS
final_gate: PASS_US_MINERAL_TRADE_IMPORT_NODE_JOIN_READY
outcome_concentration_computed: false
trade_rows_opened: false
incremental_monetary_cost_usd: 0
---

# US-MINERAL-F01 Result — USGS Critical-Mineral Trade-Code × Census Import-Node Join Feasibility
# US-MINERAL-F01 결과 — USGS 핵심광물 trade code × Census 수입 진입노드 조인 가능성

## Final gate / 최종 판정

**`PASS_US_MINERAL_TRADE_IMPORT_NODE_JOIN_READY`**

## Korean summary / 한국어 요약

최종 2025 미국 핵심광물 60개를 결과값을 보기 전에 고정하고, USGS OFR 2025-1047 Appendix 2의 공식 trade-code semantics와 Census 2023 공개 정적 무역파일의 10-digit HTS / country / customs-district / mode / month 구조를 source-semantic 수준에서 검증했다.

결론적으로 **전체 60개를 임의로 한 광물 단위로 강제하는 것은 부적절하지만**, 결과를 보기 전에 고정한 배제 규칙을 적용하면 Census `IMP_DETL` 2023에서 결정론적으로 표현 가능한 **8개 광물 support-qualified subset**이 존재한다.

Primary `IMP_DETL` subset:

**Antimony, Barite, Beryllium, Palladium, Phosphate, Potash, Rhodium, Tellurium**.

이 중 6-digit HS로 내렸을 때도 2023 HTS10 자식 집합이 광물 mapping과 완전히 일치하여 commodity identity가 보존되는 actual-port 후보는 6개다:

**Antimony, Barite, Palladium, Phosphate, Potash, Rhodium**.

F01에서는 Census 거래 row를 열지 않았고 국가/진입노드 집중도, HHI, top-share, 순위, 상관/회귀를 계산하지 않았다.

## English summary

The final 2025 U.S. critical-mineral universe was frozen at 60 minerals before any concentration outcome. F01 then qualified the official USGS OFR 2025-1047 Appendix-2 trade-code semantics against the Census 2023 public static merchandise-trade structure at source-semantic level.

The full 60-mineral universe is not defensibly representable as one uniform mineral-level Census unit without unsupported aggregation or allocation. However, the preregistered exclusion rules produce a deterministic **8-mineral support-qualified `IMP_DETL` subset** before outcome exposure:

**Antimony, Barite, Beryllium, Palladium, Phosphate, Potash, Rhodium, Tellurium**.

A stricter HS6 identity-preservation test leaves six minerals eligible for a separate published port-of-unlading route:

**Antimony, Barite, Palladium, Phosphate, Potash, Rhodium**.

No Census trade rows, concentration statistics, HHI, top-share, rankings, correlations or regressions were opened or computed during F01.

## 1. Authoritative universe / 공식 universe

Frozen universe:
- Final 2025 U.S. List of Critical Minerals;
- **60 minerals**;
- frozen before any concentration outcome.

Primary mapping source:
- USGS `Methodology and technical input for the 2025 U.S. List of Critical Minerals—Assessing the potential effects of mineral commodity supply chain disruptions on the U.S. economy`, OFR 2025-1047, version 2.0 (2026 revision);
- Appendix 2 provides HTS/Schedule-B mapping, content assumptions and comments;
- the report states that its assessment used year **2023** data unless otherwise noted, which makes 2023 a defensible fixed Census compatibility vintage for this branch.

Durable preflight:
- `research/US-MINERAL-F01/SOURCE_PREFLIGHT.md`.

## 2. Prospective mapping-identifiability rule / 사전 mapping 식별성 규칙

The following rule was frozen and applied before opening any concentration outcome:

1. Exclude final-60 minerals without one-to-one Appendix-2 mapping support.
2. Do not aggregate multi-stage or multi-form mineral supply-chain families into a synthetic final-mineral unit.
3. Exclude the 15 rare-earth elements from the simple Census route because Appendix 2 uses special rare-earth allocation/disaggregation.
4. Expand Appendix import codes to the official Census **2023 10-digit HTS** universe using exact 10-digit matching or deterministic 6/8-digit prefix expansion; exclude a unit if any expanded HTS10 is shared with another Appendix-2 commodity unit.
5. Exclude units whose Appendix-2 semantics require transaction **unit-value** allocation or scrap splitting.
6. Exclude otherwise eligible units whose Appendix code pattern does not resolve to the official 2023 HTS10 concordance.
7. Permit separate HS6 port analysis only if, for every HS6 used by the mineral, the mineral's mapped HTS10 set equals the complete valid 2023 HTS10 child set for that HS6.

One registered lexical normalization is allowed:
- final-list `Phosphate` → Appendix-2 methodology unit `Phosphates`.

This is a one-to-one singular/plural alias, not a supply-chain aggregation.

Durable evidence:
- `research/US-MINERAL-F01/MAPPING_IDENTIFIABILITY.md`.

## 3. Final-60 classification / 최종 60개 분류

Prospective decision counts:

- `EXCLUDE_R1_NO_APPENDIX2_MAPPING`: **6**
- `EXCLUDE_R2_MULTISTAGE_OR_MULTIFORM_FAMILY`: **12**
- `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION`: **15**
- `EXCLUDE_R4_SHARED_2023_HTS10`: **9**
- `EXCLUDE_R5_TRANSACTION_UNIT_VALUE_ALLOCATION`: **8**
- `EXCLUDE_R6_2023_HTS_VINTAGE_UNRESOLVED`: **2**
- `SUPPORT_QUALIFIED_IMP_DETL_2023`: **8**

### Why Indium and Lithium do not force PARTIAL/HOLD

`Indium` and `Lithium` each contain Appendix code patterns that do not resolve cleanly to the official Census 2023 HTS10 concordance under the frozen exact/prefix rule. They are therefore excluded prospectively as `R6` rather than repaired with a later-vintage concordance or manual substitution.

This does **not** invalidate the research unit because the preregistered F01 contract explicitly allows a **prospectively support-qualified subset** defined solely by pre-outcome source semantics. The eight admitted minerals have zero unresolved 2023 mapping codes.

## 4. Frozen `IMP_DETL` support subset / 고정 지원 subset

| Mineral | Appendix-2 unit | 2023 HTS10 mapping basis |
|---|---|---|
| Antimony | Antimony | deterministic 6-digit prefix → HTS10 |
| Barite | Barite | exact HTS10 |
| Beryllium | Beryllium | exact HTS10 |
| Palladium | Palladium | deterministic 6-digit prefix → HTS10 |
| Phosphate | Phosphates | exact HTS10 |
| Potash | Potash | exact HTS10 |
| Rhodium | Rhodium | deterministic 6-digit prefix → HTS10 |
| Tellurium | Tellurium | exact HTS10 |

The exact frozen raw-code → 2023 HTS10 mapping is preserved in `MAPPING_IDENTIFIABILITY.md` and shall be imported unchanged into any outcome-bearing descendant.

No mineral may be added or removed after viewing concentration values except under a separately documented source-integrity failure that triggers the preregistered fail-closed rule.

## 5. HS6 port subset / HS6 항만 subset

The stricter HS6 child-coverage rule yields:

**6 / 8 `IMP_DETL`-qualified minerals:**

- Antimony
- Barite
- Palladium
- Phosphate
- Potash
- Rhodium

Not HS6-preserving:
- Beryllium — some used HS6 groups contain additional valid 2023 HTS10 siblings not in the mineral mapping;
- Tellurium — HS6 `280450` contains an additional valid 2023 HTS10 sibling outside the Tellurium mapping.

Therefore Beryllium and Tellurium may remain in the 10-digit district-level `IMP_DETL` experiment but shall not be included in an HS6 actual-port concentration result under this frozen route.

## 6. Census public-file contract / Census 공개 파일 계약

Primary product:
- `IMP_DETL.TXT` inside monthly 2023 Merchandise Trade Imports ZIPs;
- identity fields include 10-digit HTS, 4-digit country, country subcode, district of entry, district of unlading, rate provision, year and month;
- monthly quantity/value and mode-specific value/weight fields are available.

Optional port product:
- `DPORTHS6I<YY><MM>.TXT`;
- 6-digit HS × country × 4-digit port of unlading × year × month;
- general-import total/mode value and shipping weight fields.

All **12/12** monthly 2023 Merchandise ZIPs and **12/12** monthly 2023 Port-HS6 ZIPs returned HTTP 200 through metadata-only HEAD requests.

Durable contract:
- `research/US-MINERAL-F01/EXECUTION_CONTRACT.md`.

## 7. Frozen future execution semantics / 향후 실행 semantics

### Period

Primary bounded period:

**2023-01 through 2023-12**.

### Raw and research identity

Raw `IMP_DETL` identity:

`commodity × cty_code × cty_subco × dist_entry × dist_unlad × rate_prov × year × month`.

Research aggregation identity:

`mineral × cty_code × dist_entry × dist_unlad × year × month`.

`cty_subco` and `rate_prov` may be summed only after raw full-key validation.

Repeated raw full keys are **fail-closed**; do not silently deduplicate or sum them.

### Weight

Primary weight for a later concentration experiment:

**`gen_val_mo` — General Imports, Total Value**.

Reasons:
- it is available at the required `IMP_DETL` grain;
- the Port HS6 `value_mo` field is also General Imports, Total Value;
- it avoids invalid summation of heterogeneous physical quantity units.

Use monthly fields only; never sum YTD fields across months.

### Quantity / shipping weight

- quantity units are HTS-code specific;
- heterogeneous units shall not be summed without a separately preregistered conversion;
- suppressed or missing quantities/weights are not imputed;
- quantity/weight remain diagnostics, not the core concentration weight.

### Mode

- `air_val_mo` = air component;
- `ves_val_mo` = vessel component;
- `cnt_val_mo` = containerized subset of vessel, not an independent additive third mode;
- if later used, `other_value = gen_val_mo - air_val_mo - ves_val_mo` with negative residuals treated as fail-closed diagnostics.

### Suppression / published geography

Census disclosure protection can suppress quantity/weight and can affect published district/port presentation. Therefore:
- preserve official published geographic codes exactly;
- do not manually disaggregate or reverse engineer combined/suppressed geography;
- any HS6 port result must be described as **published port-of-unlading statistics**, not transaction-level physical-routing ground truth.

## 8. Revision and snapshot plan / 개정·스냅샷 계획

Census merchandise data are revised. The downstream experiment shall therefore use one contemporaneous official 2023 snapshot, not claim to reproduce the original first-release 2023 files.

Before any concentration output is computed, one run must:
1. download all 12 official 2023 monthly Merchandise ZIPs;
2. record URL and access timestamp;
3. compute SHA-256 for each ZIP;
4. record member filename and byte size;
5. compute SHA-256 for each extracted member used;
6. persist a manifest;
7. compute all primary metrics from that single manifest version only.

If Census later changes a file hash, it becomes a new source snapshot/version. Silent replacement or mixed-manifest analysis is prohibited.

## 9. Gate application / 게이트 적용

The preregistered PASS conditions are satisfied:

- authoritative 60-mineral universe frozen: **YES**;
- official USGS mapping represented deterministically with documented caveats: **YES**, for a prospective subset;
- Census zero-cost public-file route exposes code/origin/district/mode/time: **YES**;
- fixed 2023 vintage compatibility defensible: **YES**;
- non-identifiable mixed/family/REE/unit-value/unresolved-vintage cases prospectively excluded before outcomes: **YES**;
- reproducible duplicate/revision/suppression/null/quantity rules defined: **YES**;
- bounded 2023 period and snapshot/hash plan defined: **YES**;
- support-qualified primary subset non-empty: **YES — 8 / 60**;
- outcome exposure during F01: **NO**.

Therefore:

**Final: `PASS_US_MINERAL_TRADE_IMPORT_NODE_JOIN_READY`.**

## 10. Claim boundary / 주장 경계

This PASS establishes only that a defensible source-semantic bridge exists for the frozen support-qualified subset.

It does **not** establish:
- that any of the eight minerals is highly concentrated by country or district;
- that any U.S. gateway is a chokepoint;
- that country concentration and domestic node concentration are correlated;
- that a port/district causes supply risk;
- that any policy, stockpile, sourcing, logistics or investment action is warranted.

Those are outcome-bearing questions and require a separately preregistered experiment.

## 11. Next branch rule / 다음 branch 규칙

F01 is complete. A downstream concentration experiment may proceed only after a new decision/README freezes:
- the eight-mineral universe above;
- the 2023 snapshot manifest procedure;
- `gen_val_mo` as the primary weight;
- exact country/district concentration metrics and gates;
- whether district-of-entry or district-of-unlading is primary;
- whether the six-mineral HS6 port route is primary, secondary, or diagnostic;
- any correlation/coupling statistic;
- reporting rules for combined/special Census geography.

Do not open the 2023 trade rows until that descendant preregistration is committed.

Incremental monetary cost remained **0 USD**. No paid commercial trade source, Census API credential, dashboard scraping, larger runner, or unsupported concordance was used.

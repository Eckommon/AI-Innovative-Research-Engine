---
id: US-MINERAL-F01-MAPPING-IDENTIFIABILITY
type: prospective-support-qualification
created: 2026-09-04
outcome_concentration_computed: false
trade_rows_opened: false
census_reference_data_only: true
incremental_monetary_cost_usd: 0
---

# US-MINERAL-F01 Mapping Identifiability / 매핑 식별성 판정

## 1. Exposure boundary / 노출 경계

- No Census `IMP_DETL` or port trade rows were downloaded or opened.
- No country/district/port concentration, HHI, top-share, ranking, correlation or regression was computed.
- The only Census data file opened in this gate is the **2023 import commodity concordance (`imp-code.txt`)**, a classification/reference file containing valid 10-digit HTS codes and descriptions.

## 2. Frozen prospective rules / 사전 고정 규칙

Applied in this order, before any concentration outcome:
1. Exclude final-60 minerals with no one-to-one Appendix-2 mapping support.
2. Do not aggregate Appendix-2 multi-stage/multi-form supply-chain families; exclude them from the mineral-level unit.
3. Exclude the 15 rare-earth elements from the simple Census route because Appendix 2 uses special rare-earth disaggregation/allocation.
4. Exclude a methodology unit if any **expanded 2023 10-digit HTS** is shared with another Appendix-2 commodity unit.
5. Exclude a methodology unit if Appendix-2 row semantics invoke transaction **unit value** allocation/scrap splitting.
6. For the remainder, freeze Appendix import code → official **Census 2023 HTS10** mapping as exact (10-digit) or prefix expansion (6/8-digit). Any unresolved code excludes the unit for this vintage.
7. Permit actual-port HS6 analysis only where the mineral mapping covers **all valid 2023 HTS10 children of every HS6 used by the mineral**, so collapsing to HS6 does not admit unrelated HTS10 siblings.

One lexical normalization is registered: final-list `Phosphate` → Appendix-2 methodology unit `Phosphates`. This is a one-to-one singular/plural alias, not a supply-chain aggregation.

## 3. Source snapshots / 소스 스냅샷

- USGS OFR 2025-1047 XML status: `200`; SHA-256: `c45590b18b7709abb663dc7ad044427792c9724c67a913dea212fa11fe5f42f2`
- Census 2023 import concordance status: `200`; valid 10-digit HTS codes parsed: **19879**; SHA-256: `409f073cd445210b11eae058ecfc527a949dc012ead62c777b8bea32370d5495`
- Census `IMP_DETL` layout status: `200`; SHA-256: `51490d2147e33044ed28744e080abd79c6472d33094a5389ce1e023b44b7ba38`
- Census Port HS6 Imports layout status: `200`; SHA-256: `8f81ff347286212febd46e0f5510290d81411906ccfe8577f4c1e8afc20e8d72`
- Jan-2023 Merchandise ZIP HEAD: status `200`, content-type `application/zip`, content-length `None`
- Jan-2023 Port HS6 ZIP HEAD: status `200`, content-type `application/zip`, content-length `None`

## 4. Final-60 prospective classification / 최종 60개 사전 분류

| Final mineral | Appendix-2 unit | Decision | Reason |
|---|---|---|---|
| Aluminum | — | `EXCLUDE_R2_MULTISTAGE_OR_MULTIFORM_FAMILY` | Appendix 2 represents this final-list mineral through multiple stages/forms; no arbitrary family aggregation. |
| Antimony | Antimony | `SUPPORT_QUALIFIED_IMP_DETL_2023` | One-to-one methodology unit; no shared expanded HTS10; no unit-value allocation; 2023 HTS10 mapping resolved. |
| Arsenic | Arsenic | `EXCLUDE_R4_SHARED_2023_HTS10` | At least one 2023 HTS10 is shared with another Appendix-2 commodity unit after exact/prefix expansion. |
| Barite | Barite | `SUPPORT_QUALIFIED_IMP_DETL_2023` | One-to-one methodology unit; no shared expanded HTS10; no unit-value allocation; 2023 HTS10 mapping resolved. |
| Beryllium | Beryllium | `SUPPORT_QUALIFIED_IMP_DETL_2023` | One-to-one methodology unit; no shared expanded HTS10; no unit-value allocation; 2023 HTS10 mapping resolved. |
| Bismuth | Bismuth | `EXCLUDE_R5_TRANSACTION_UNIT_VALUE_ALLOCATION` | Appendix-2 row text invokes transaction unit-value allocation/scrap rule. |
| Boron | — | `EXCLUDE_R1_NO_APPENDIX2_MAPPING` | No one-to-one Appendix-2 methodology unit mapping. |
| Cerium | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Cesium | — | `EXCLUDE_R1_NO_APPENDIX2_MAPPING` | No one-to-one Appendix-2 methodology unit mapping. |
| Chromium | — | `EXCLUDE_R2_MULTISTAGE_OR_MULTIFORM_FAMILY` | Appendix 2 represents this final-list mineral through multiple stages/forms; no arbitrary family aggregation. |
| Cobalt | — | `EXCLUDE_R2_MULTISTAGE_OR_MULTIFORM_FAMILY` | Appendix 2 represents this final-list mineral through multiple stages/forms; no arbitrary family aggregation. |
| Copper | — | `EXCLUDE_R2_MULTISTAGE_OR_MULTIFORM_FAMILY` | Appendix 2 represents this final-list mineral through multiple stages/forms; no arbitrary family aggregation. |
| Dysprosium | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Erbium | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Europium | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Fluorspar | — | `EXCLUDE_R2_MULTISTAGE_OR_MULTIFORM_FAMILY` | Appendix 2 represents this final-list mineral through multiple stages/forms; no arbitrary family aggregation. |
| Gadolinium | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Gallium | Gallium | `EXCLUDE_R4_SHARED_2023_HTS10` | At least one 2023 HTS10 is shared with another Appendix-2 commodity unit after exact/prefix expansion. |
| Germanium | Germanium | `EXCLUDE_R4_SHARED_2023_HTS10` | At least one 2023 HTS10 is shared with another Appendix-2 commodity unit after exact/prefix expansion. |
| Graphite | — | `EXCLUDE_R2_MULTISTAGE_OR_MULTIFORM_FAMILY` | Appendix 2 represents this final-list mineral through multiple stages/forms; no arbitrary family aggregation. |
| Hafnium | Hafnium | `EXCLUDE_R5_TRANSACTION_UNIT_VALUE_ALLOCATION` | Appendix-2 row text invokes transaction unit-value allocation/scrap rule. |
| Holmium | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Indium | Indium | `EXCLUDE_R6_2023_HTS_VINTAGE_UNRESOLVED` | One or more Appendix-2 import code patterns do not resolve to the official Census 2023 HTS10 concordance. |
| Iridium | Iridium | `EXCLUDE_R4_SHARED_2023_HTS10` | At least one 2023 HTS10 is shared with another Appendix-2 commodity unit after exact/prefix expansion. |
| Lanthanum | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Lead | Lead | `EXCLUDE_R5_TRANSACTION_UNIT_VALUE_ALLOCATION` | Appendix-2 row text invokes transaction unit-value allocation/scrap rule. |
| Lithium | Lithium | `EXCLUDE_R6_2023_HTS_VINTAGE_UNRESOLVED` | One or more Appendix-2 import code patterns do not resolve to the official Census 2023 HTS10 concordance. |
| Lutetium | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Magnesium | — | `EXCLUDE_R2_MULTISTAGE_OR_MULTIFORM_FAMILY` | Appendix 2 represents this final-list mineral through multiple stages/forms; no arbitrary family aggregation. |
| Manganese | — | `EXCLUDE_R2_MULTISTAGE_OR_MULTIFORM_FAMILY` | Appendix 2 represents this final-list mineral through multiple stages/forms; no arbitrary family aggregation. |
| Metallurgical coal | — | `EXCLUDE_R1_NO_APPENDIX2_MAPPING` | No one-to-one Appendix-2 methodology unit mapping. |
| Neodymium | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Nickel | — | `EXCLUDE_R2_MULTISTAGE_OR_MULTIFORM_FAMILY` | Appendix 2 represents this final-list mineral through multiple stages/forms; no arbitrary family aggregation. |
| Niobium | Niobium | `EXCLUDE_R4_SHARED_2023_HTS10` | At least one 2023 HTS10 is shared with another Appendix-2 commodity unit after exact/prefix expansion. |
| Palladium | Palladium | `SUPPORT_QUALIFIED_IMP_DETL_2023` | One-to-one methodology unit; no shared expanded HTS10; no unit-value allocation; 2023 HTS10 mapping resolved. |
| Phosphate | Phosphates | `SUPPORT_QUALIFIED_IMP_DETL_2023` | One-to-one methodology unit; no shared expanded HTS10; no unit-value allocation; 2023 HTS10 mapping resolved. |
| Platinum | Platinum | `EXCLUDE_R5_TRANSACTION_UNIT_VALUE_ALLOCATION` | Appendix-2 row text invokes transaction unit-value allocation/scrap rule. |
| Potash | Potash | `SUPPORT_QUALIFIED_IMP_DETL_2023` | One-to-one methodology unit; no shared expanded HTS10; no unit-value allocation; 2023 HTS10 mapping resolved. |
| Praseodymium | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Rhenium | Rhenium | `EXCLUDE_R5_TRANSACTION_UNIT_VALUE_ALLOCATION` | Appendix-2 row text invokes transaction unit-value allocation/scrap rule. |
| Rhodium | Rhodium | `SUPPORT_QUALIFIED_IMP_DETL_2023` | One-to-one methodology unit; no shared expanded HTS10; no unit-value allocation; 2023 HTS10 mapping resolved. |
| Rubidium | — | `EXCLUDE_R1_NO_APPENDIX2_MAPPING` | No one-to-one Appendix-2 methodology unit mapping. |
| Ruthenium | Ruthenium | `EXCLUDE_R4_SHARED_2023_HTS10` | At least one 2023 HTS10 is shared with another Appendix-2 commodity unit after exact/prefix expansion. |
| Samarium | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Scandium | — | `EXCLUDE_R1_NO_APPENDIX2_MAPPING` | No one-to-one Appendix-2 methodology unit mapping. |
| Silicon | — | `EXCLUDE_R2_MULTISTAGE_OR_MULTIFORM_FAMILY` | Appendix 2 represents this final-list mineral through multiple stages/forms; no arbitrary family aggregation. |
| Silver | Silver | `EXCLUDE_R5_TRANSACTION_UNIT_VALUE_ALLOCATION` | Appendix-2 row text invokes transaction unit-value allocation/scrap rule. |
| Tantalum | Tantalum | `EXCLUDE_R4_SHARED_2023_HTS10` | At least one 2023 HTS10 is shared with another Appendix-2 commodity unit after exact/prefix expansion. |
| Tellurium | Tellurium | `SUPPORT_QUALIFIED_IMP_DETL_2023` | One-to-one methodology unit; no shared expanded HTS10; no unit-value allocation; 2023 HTS10 mapping resolved. |
| Terbium | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Thulium | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Tin | Tin | `EXCLUDE_R5_TRANSACTION_UNIT_VALUE_ALLOCATION` | Appendix-2 row text invokes transaction unit-value allocation/scrap rule. |
| Titanium | — | `EXCLUDE_R2_MULTISTAGE_OR_MULTIFORM_FAMILY` | Appendix 2 represents this final-list mineral through multiple stages/forms; no arbitrary family aggregation. |
| Tungsten | Tungsten | `EXCLUDE_R5_TRANSACTION_UNIT_VALUE_ALLOCATION` | Appendix-2 row text invokes transaction unit-value allocation/scrap rule. |
| Uranium | — | `EXCLUDE_R1_NO_APPENDIX2_MAPPING` | No one-to-one Appendix-2 methodology unit mapping. |
| Vanadium | Vanadium | `EXCLUDE_R4_SHARED_2023_HTS10` | At least one 2023 HTS10 is shared with another Appendix-2 commodity unit after exact/prefix expansion. |
| Ytterbium | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Yttrium | — | `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION` | Appendix 2 applies special rare-earth allocation/disaggregation; excluded from simple Census route. |
| Zinc | — | `EXCLUDE_R2_MULTISTAGE_OR_MULTIFORM_FAMILY` | Appendix 2 represents this final-list mineral through multiple stages/forms; no arbitrary family aggregation. |
| Zirconium | Zirconium | `EXCLUDE_R4_SHARED_2023_HTS10` | At least one 2023 HTS10 is shared with another Appendix-2 commodity unit after exact/prefix expansion. |

### Decision counts / 판정 수

- `EXCLUDE_R1_NO_APPENDIX2_MAPPING`: **6**
- `EXCLUDE_R2_MULTISTAGE_OR_MULTIFORM_FAMILY`: **12**
- `EXCLUDE_R3_RARE_EARTH_SPECIAL_DISAGGREGATION`: **15**
- `EXCLUDE_R4_SHARED_2023_HTS10`: **9**
- `EXCLUDE_R5_TRANSACTION_UNIT_VALUE_ALLOCATION`: **8**
- `EXCLUDE_R6_2023_HTS_VINTAGE_UNRESOLVED`: **2**
- `SUPPORT_QUALIFIED_IMP_DETL_2023`: **8**

## 5. `IMP_DETL` 2023 support-qualified subset / 2023 지원 적격 subset

Prospectively qualified minerals: **8 / 60**

`Antimony, Barite, Beryllium, Palladium, Phosphate, Potash, Rhodium, Tellurium`

| Mineral | Appendix unit | Raw Appendix import code(s) | 2023 HTS10 count | Mapping mode(s) |
|---|---|---|---:|---|
| Antimony | Antimony | 282580, 811010, 811020, 811090 | 4 | prefix6:4 |
| Barite | Barite | 2511101000, 2511105000 | 2 | exact:2 |
| Beryllium | Beryllium | 2825901000, 7405006030, 7409901030, 7409905030, 7409909030, 8112120000, 8112130000, 8112190000 | 8 | exact:8 |
| Palladium | Palladium | 711021, 711029 | 2 | prefix6:2 |
| Phosphate | Phosphates | 2510100000, 2510200000, 2835250000, 2835260000, 3103110000, 3103190000, 3105300000, 3105400010, 3105400050 | 9 | exact:9 |
| Potash | Potash | 2834210000, 3104200010, 3104200050, 3104300000, 3104900100 | 5 | exact:5 |
| Rhodium | Rhodium | 711031, 711039 | 2 | prefix6:2 |
| Tellurium | Tellurium | 2804500020 | 1 | exact:1 |

### Frozen 2023 HTS10 mapping / 고정 2023 HTS10 매핑

#### Antimony ← `Antimony`
- `282580` (prefix6) → `2825800000`
- `811010` (prefix6) → `8110100000`
- `811020` (prefix6) → `8110200000`
- `811090` (prefix6) → `8110900000`

#### Barite ← `Barite`
- `2511101000` (exact) → `2511101000`
- `2511105000` (exact) → `2511105000`

#### Beryllium ← `Beryllium`
- `2825901000` (exact) → `2825901000`
- `7405006030` (exact) → `7405006030`
- `7409901030` (exact) → `7409901030`
- `7409905030` (exact) → `7409905030`
- `7409909030` (exact) → `7409909030`
- `8112120000` (exact) → `8112120000`
- `8112130000` (exact) → `8112130000`
- `8112190000` (exact) → `8112190000`

#### Palladium ← `Palladium`
- `711021` (prefix6) → `7110210000`
- `711029` (prefix6) → `7110290000`

#### Phosphate ← `Phosphates`
- `2510100000` (exact) → `2510100000`
- `2510200000` (exact) → `2510200000`
- `2835250000` (exact) → `2835250000`
- `2835260000` (exact) → `2835260000`
- `3103110000` (exact) → `3103110000`
- `3103190000` (exact) → `3103190000`
- `3105300000` (exact) → `3105300000`
- `3105400010` (exact) → `3105400010`
- `3105400050` (exact) → `3105400050`

#### Potash ← `Potash`
- `2834210000` (exact) → `2834210000`
- `3104200010` (exact) → `3104200010`
- `3104200050` (exact) → `3104200050`
- `3104300000` (exact) → `3104300000`
- `3104900100` (exact) → `3104900100`

#### Rhodium ← `Rhodium`
- `711031` (prefix6) → `7110310000`
- `711039` (prefix6) → `7110390000`

#### Tellurium ← `Tellurium`
- `2804500020` (exact) → `2804500020`

## 6. Shared-code and unit-value exclusions / 공유코드 및 unit-value 제외

- final-list units excluded by expanded 2023 HTS10 sharing: **9**
  - Arsenic / `Arsenic`: 2853909010→['Arsenic', 'Gallium']; 3818000010→['Arsenic', 'Gallium']
  - Gallium / `Gallium`: 2853909010→['Arsenic', 'Gallium']; 3818000010→['Arsenic', 'Gallium']
  - Germanium / `Germanium`: 2825600000→['Germanium', 'Zirconium']
  - Iridium / `Iridium`: 7110410050→['Iridium', 'Ruthenium']
  - Niobium / `Niobium`: 2615903000→['Niobium', 'Tantalum']; 2615906030→['Niobium', 'Tantalum']; 2615906060→['Niobium', 'Tantalum']
  - Ruthenium / `Ruthenium`: 7110410050→['Iridium', 'Ruthenium']
  - Tantalum / `Tantalum`: 2615903000→['Niobium', 'Tantalum']; 2615906030→['Niobium', 'Tantalum']; 2615906060→['Niobium', 'Tantalum']
  - Vanadium / `Vanadium`: 7601209030→['Aluminum', 'Vanadium']
  - Zirconium / `Zirconium`: 2825600000→['Germanium', 'Zirconium']
- final-list units excluded by transaction unit-value semantics: **8**
  - Bismuth / `Bismuth`
  - Hafnium / `Hafnium`
  - Lead / `Lead`
  - Platinum / `Platinum`
  - Rhenium / `Rhenium`
  - Silver / `Silver`
  - Tin / `Tin`
  - Tungsten / `Tungsten`

## 7. HS6 actual-port identifiability / HS6 실제 항만 식별성

HS6-preserving subset: **6 / 8** of the `IMP_DETL` support-qualified minerals.

`Antimony, Barite, Palladium, Phosphate, Potash, Rhodium`

| Mineral | HS6 preserved? | HS6 set | Failure diagnostic |
|---|---|---|---|
| Antimony | YES | 282580, 811010, 811020, 811090 | — |
| Barite | YES | 251110 | — |
| Beryllium | NO | 282590, 740500, 740990, 811212, 811213, 811219 | 282590: mapped 1 / all-2023 6; 740500: mapped 1 / all-2023 3; 740990: mapped 3 / all-2023 6 |
| Palladium | YES | 711021, 711029 | — |
| Phosphate | YES | 251010, 251020, 283525, 283526, 310311, 310319, 310530, 310540 | — |
| Potash | YES | 283421, 310420, 310430, 310490 | — |
| Rhodium | YES | 711031, 711039 | — |
| Tellurium | NO | 280450 | 280450: mapped 1 / all-2023 2 |

## 8. Vintage-resolution diagnostics / vintage 해소 진단

- support-qualified units with unresolved 2023 codes: **0**
- excluded final-list units due specifically to unresolved 2023 code patterns: **2**
  - Indium / `Indium` unmatched: `['8112925000', '81129930']`
  - Lithium / `Lithium` unmatched: `['2841909010', '2841909020', '2841909040', '28429030', '28429060']`

## 9. Gate interpretation / 게이트 해석

**`MAPPING_IDENTIFIABILITY_PARTIAL_VINTAGE_EXCEPTION`**

A support subset exists, but at least one otherwise eligible final-list unit has unresolved 2023 HTS code compatibility and must be considered explicitly at the final F01 gate.

Incremental monetary cost remained **0 USD**. Standard GitHub-hosted Actions on this public repository were used; no paid data source, API credential, large runner, or commercial concordance was used.

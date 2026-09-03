---
id: US-MINERAL-F01-SOURCE-PREFLIGHT
type: source-semantic-preflight
created: 2026-09-04
outcome_concentration_computed: false
trade_rows_opened: false
incremental_monetary_cost_usd: 0
---

# US-MINERAL-F01 Source Preflight / 소스 사전검증

## Exposure boundary / 노출 경계

- No Census trade-row values were downloaded or opened.
- No mineral/country/district/port concentration was calculated.
- No HHI, top-share, ranking, correlation or regression was calculated.

## A. Authoritative universe / 공식 universe

- frozen universe: Final 2025 U.S. List of Critical Minerals
- frozen universe count: **60**
- source: `https://www.usgs.gov/programs/mineral-resources-program/science/about-2025-list-critical-minerals`

## B. USGS Appendix-2 mapping contract / USGS Appendix 2 mapping 계약

- source XML: `https://pubs.usgs.gov/of/2025/1047/ofr20251047.XML`
- HTTP status: `200`
- SHA-256: `c45590b18b7709abb663dc7ad044427792c9724c67a913dea212fa11fe5f42f2`
- publication: OFR 2025-1047, version 2.0 (2026 revision)
- Appendix 2 states imports use U.S. HTS codes and includes assumed mineral/element content plus comments/assumptions.

- discovered table labels containing Appendix structures: `['Table 2.1', 'Table 2.2', 'Table 2.3']`
- Table 2.1 parsed mapping records: **349**
- Table 2.1 unique methodology commodity units: **69**
- Table 2.1 unique import codes: **324**
- Table 2.3 parsed U.S.-trade-code records for rare-earth section: **138**
- Table 2.3 unique rare-earth commodity units: **15**
- Table 2.3 unique U.S. trade codes: **24**
- import/U.S.-trade code lengths observed: `{6: 35, 8: 14, 10: 438}`
- codes shared across >1 parsed methodology unit: **27**
- methodology units whose mapping row text explicitly invokes a `unit value` rule: **27**

### Exact-name coverage diagnostic / 정확 명칭 coverage 진단

- final-60 names with an exact case-insensitive methodology-unit name: **42 / 60**
- final-60 names without exact one-name methodology match: `['Boron', 'Cesium', 'Chromium', 'Cobalt', 'Copper', 'Fluorspar', 'Graphite', 'Magnesium', 'Manganese', 'Metallurgical coal', 'Nickel', 'Phosphate', 'Rubidium', 'Scandium', 'Silicon', 'Titanium', 'Uranium', 'Zinc']`

This exact-name diagnostic is intentionally conservative and is **not** a final support subset. It avoids silently merging supply-chain stages.

### Source-declared family complexity / source가 명시한 family 복잡성

- final mineral families represented by multiple methodology stages/forms: `['Aluminum', 'Chromium', 'Cobalt', 'Copper', 'Graphite', 'Fluorspar', 'Manganese', 'Nickel', 'Silicon', 'Titanium', 'Zinc']`
- separately treated magnesium chains: `['Magnesium']`
- final-list rare earths requiring the special Appendix-2 rare-earth treatment: `['Cerium', 'Dysprosium', 'Erbium', 'Europium', 'Gadolinium', 'Holmium', 'Lanthanum', 'Lutetium', 'Neodymium', 'Praseodymium', 'Samarium', 'Terbium', 'Thulium', 'Ytterbium', 'Yttrium']`

The OFR methods explicitly state that 31 of the 84 assessed commodity units represent different stages/forms of 11 mineral supply chains, while magnesium compounds and magnesium metal are separate supply chains. Rare-earth imports also use special disaggregation rules.

### Parsed unit names / 파싱된 unit 이름

- Table 2.1 units: `['Alumina', 'Aluminum', 'Antimony', 'Arsenic', 'Barite', 'Bauxite', 'Beryllium', 'Bismuth', 'Cadmium', 'Chromite', 'Chromium chemicals', 'Chromium ferroalloys', 'Chromium metal', 'Cobalt chemicals', 'Cobalt metal', 'Copper, mined', 'Copper, refined', 'Feldspar', 'Fluorspar, acidspar', 'Fluorspar, metspar', 'Gallium', 'Germanium', 'Gold', 'Graphite, natural', 'Graphite, synthetic', 'Hafnium', 'Helium', 'Indium', 'Iridium', 'Iron ore', 'Lead', 'Lithium', 'Magnesium compounds', 'Magnesium metal', 'Manganese alloys', 'Manganese dioxide', 'Manganese metal', 'Manganese ore', 'Manganese sulfate (high purity)', 'Mica', 'Molybdenum', 'Nickel, mined', 'Nickel, primary refined', 'Niobium', 'Palladium', 'Phosphates', 'Platinum', 'Potash', 'Rhenium', 'Rhodium', 'Ruthenium', 'Selenium', 'Silicon ferroalloys', 'Silicon metal', 'Silver', 'Strontium', 'Tantalum', 'Tellurium', 'Tin', 'Titanium ferroalloys', 'Titanium metal', 'Titanium mineral concentrates', 'Titanium pigment', 'Titanium sponge', 'Tungsten', 'Vanadium', 'Zinc, mined', 'Zinc, smelted', 'Zirconium']`
- Table 2.3 units: `['Cerium', 'Dysprosium', 'Erbium', 'Europium', 'Gadolinium', 'Holmium', 'Lanthanum', 'Lutetium', 'Neodymium', 'Praseodymium', 'Samarium', 'Terbium', 'Thulium', 'Ytterbium', 'Yttrium']`

### Shared-code diagnostic / 공유 code 진단

- `2604000040` → `['Nickel, mined', 'Nickel, primary refined']`
- `2615903000` → `['Niobium', 'Tantalum']`
- `2615906030` → `['Niobium', 'Tantalum']`
- `2615906060` → `['Niobium', 'Tantalum']`
- `2805300000` → `['Cerium', 'Dysprosium', 'Erbium', 'Europium', 'Gadolinium', 'Holmium', 'Lanthanum', 'Lutetium', 'Neodymium', 'Praseodymium', 'Samarium', 'Terbium', 'Thulium', 'Ytterbium', 'Yttrium']`
- `2805300050` → `['Dysprosium', 'Erbium', 'Europium', 'Gadolinium', 'Holmium', 'Lutetium', 'Samarium', 'Terbium', 'Thulium', 'Ytterbium', 'Yttrium']`
- `2805300090` → `['Dysprosium', 'Erbium', 'Europium', 'Gadolinium', 'Holmium', 'Lutetium', 'Samarium', 'Terbium', 'Thulium', 'Ytterbium', 'Yttrium']`
- `2825600000` → `['Germanium', 'Zirconium']`
- `2841909010` → `['Cobalt chemicals', 'Lithium']`
- `2841909020` → `['Cobalt chemicals', 'Lithium', 'Manganese sulfate (high purity)', 'Nickel, primary refined']`
- `2841909040` → `['Cobalt chemicals', 'Lithium', 'Manganese sulfate (high purity)', 'Nickel, primary refined']`
- `28429030` → `['Cobalt chemicals', 'Lithium', 'Manganese sulfate (high purity)', 'Nickel, primary refined']`
- `28429060` → `['Cobalt chemicals', 'Lithium', 'Nickel, primary refined']`
- `2846902040` → `['Dysprosium', 'Erbium', 'Europium', 'Gadolinium', 'Holmium', 'Lanthanum', 'Lutetium', 'Neodymium', 'Praseodymium', 'Samarium', 'Terbium', 'Thulium', 'Ytterbium', 'Yttrium']`
- `2846902060` → `['Dysprosium', 'Erbium', 'Europium', 'Gadolinium', 'Holmium', 'Lanthanum', 'Lutetium', 'Neodymium', 'Praseodymium', 'Samarium', 'Terbium', 'Thulium', 'Ytterbium', 'Yttrium']`
- `2846902084` → `['Dysprosium', 'Erbium', 'Europium', 'Gadolinium', 'Holmium', 'Lanthanum', 'Lutetium', 'Neodymium', 'Praseodymium', 'Samarium', 'Terbium', 'Thulium', 'Ytterbium', 'Yttrium']`
- `2846908075` → `['Dysprosium', 'Erbium', 'Europium', 'Gadolinium', 'Holmium', 'Lutetium', 'Neodymium', 'Praseodymium', 'Samarium', 'Terbium', 'Thulium', 'Ytterbium', 'Yttrium']`
- `2846908090` → `['Cerium', 'Dysprosium', 'Erbium', 'Europium', 'Gadolinium', 'Holmium', 'Lanthanum', 'Lutetium', 'Neodymium', 'Praseodymium', 'Samarium', 'Terbium', 'Thulium', 'Ytterbium', 'Yttrium']`
- `28539030` → `['Cobalt chemicals', 'Manganese sulfate (high purity)', 'Nickel, primary refined']`
- `28539050` → `['Cobalt chemicals', 'Nickel, primary refined']`
- `2853909010` → `['Arsenic', 'Gallium']`
- `3606900000` → `['Cerium', 'Lanthanum', 'Neodymium', 'Praseodymium', 'Samarium']`
- `3606903000` → `['Cerium', 'Lanthanum', 'Neodymium', 'Praseodymium', 'Samarium']`
- `3818000010` → `['Arsenic', 'Gallium']`
- `7110410050` → `['Iridium', 'Ruthenium']`
- `8505110050` → `['Cobalt metal', 'Gadolinium', 'Samarium']`
- `8505110070` → `['Cerium', 'Cobalt metal', 'Dysprosium', 'Gadolinium', 'Lanthanum', 'Neodymium', 'Praseodymium', 'Terbium']`

### Unit-value-rule units / unit-value rule unit

`['Arsenic', 'Bismuth', 'Cadmium', 'Chromium metal', 'Cobalt metal', 'Gallium', 'Germanium', 'Hafnium', 'Iridium', 'Lead', 'Magnesium metal', 'Manganese metal', 'Mica', 'Molybdenum', 'Nickel, primary refined', 'Niobium', 'Platinum', 'Rhenium', 'Ruthenium', 'Silver', 'Strontium', 'Tantalum', 'Tin', 'Titanium sponge', 'Tungsten', 'Zinc, smelted', 'Zirconium']`

## C. Census public static-file contract / Census 공개 정적 파일 계약

- merchandise record-layout HTTP: `200`; SHA-256: `c8f7ef3c48c3b99cdcb674f1216ea979f27b6161918d655fd97c3276ff854103`
- port-HS6 record-layout HTTP: `200`; SHA-256: `177be33e6a6e936c124f19cfe864616cb42ac105a2bb992ea1839d2af2eedf8e`
- data-products page HTTP: `200`; SHA-256: `d3016e57dc308fb58ea72c1b8e62cde9a57e23c5f3dc773078ef25b7203b08f8`
- `IMP_DETL` required identity-field contract detected: **YES**
- `Port Imports HS6` required identity-field contract detected: **YES**

- `IMP_DETL.TXT` identity grain: 10-digit HTS × 4-digit country × 2-digit entry district × 2-digit unlading district × year × month, with quantity/value and mode-specific value/weight fields.
- `DPORTHS6I<YY><MM>.TXT` identity grain: 6-digit HS × 4-digit country × 4-digit port-of-unlading (district+port) × year × month, with total/mode-specific value and shipping weight.

### Static ZIP route existence / 정적 ZIP 경로 존재

- Merchandise Trade Imports Jan-2026 ZIP: status `200`, content-length `None`, content-type `application/zip`, URL `https://www.census.gov/trade/downloads/2026/Merch/im_m/IMDB2601.ZIP`
- Port Imports HS6 Jan-2026 ZIP: status `200`, content-length `None`, content-type `application/zip`, URL `https://www.census.gov/trade/downloads/2026/Port/im_hs6_m/PORTHS6MM2601.ZIP`

## D. Preflight interpretation / 사전검증 해석

- Census provides both a **10-digit HTS + district** route and a **6-digit HS + actual port-of-unlading** route without requiring an API key.
- The central identifiability problem is therefore not Census availability; it is whether each final critical-mineral research unit can be prospectively represented at 10-digit and/or 6-digit code grain without unsupported family merging, mixed-code allocation, or rare-earth reconstruction.
- No concentration result has been used to make this determination.

## E. Next source-semantic gate / 다음 source-semantic gate

**`CONTINUE_F01_MAPPING_IDENTIFIABILITY`**

Before PASS/PARTIAL/HOLD/REJECT, define a prospective support rule from Appendix-2 semantics only. At minimum, distinguish:
1. simple single-chain codes that can be represented directly;
2. multi-stage mineral families;
3. special rare-earth allocations;
4. shared/mixed codes requiring transaction-unit-value allocation;
5. whether 6-digit aggregation preserves or destroys mineral identity.

Incremental monetary cost remained **0 USD**.

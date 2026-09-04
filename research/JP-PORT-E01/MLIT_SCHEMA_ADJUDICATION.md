---
id: JP-PORT-E01-MLIT-SCHEMA-ADJUDICATION
type: pre-relationship-parser-adjudication
created: 2026-09-04
issue: 80
relationship_outcome_computed: false
incremental_monetary_cost_usd: 0
---

# JP-PORT-E01 MLIT Cargo Schema Adjudication
# JP-PORT-E01 MLIT 화물 스키마 판정

The first Stage-B attempt stopped before any weather-throughput coefficient because it assumed the 2020–2024 cargo-header layout also applied to 2019.

The value-free header diagnostic established two deterministic layouts.

## 2019 legacy layout

- sheet: 海上出入貨物
- port identity header row: row 9
  - C9 = 港 湾
  - D9 = 種 別
- monthly category labels are also on row 9
- each month's total column is labeled 合計 after whitespace normalization
- sheet/group unit evidence appears above the table as （単位：トン）

## 2020–2024 current layout

- sheet: 海上出入貨物
- port identity header row: row 7
  - C7 = 港湾
  - D7 = 種別
- monthly category labels are on row 6
- each month's total column is labeled 合計
- row 7 gives トン数 for the cargo columns

## Frozen deterministic parser

For every frozen annual workbook:

1. normalize ordinary/full-width whitespace in header strings;
2. locate the unique port header row h within rows 1–15 where normalized column C = 港湾 and column D = 種別;
3. within rows max(1,h-2)..h, locate the unique row r having exactly 12 columns from E onward whose normalized value is 合計;
4. those 12 columns, in left-to-right order, map to calendar months 1..12;
5. require ton-unit evidence:
   - either the port-header row contains トン数 in the selected cargo columns; or
   - the pre-header region contains a normalized string indicating 単位:トン / 単位：トン;
6. data rows begin after h;
7. a port total row is identified by normalized 種別 = 計;
8. require exactly one total row for each E01-eligible port/year;
9. blank/non-numeric monthly cargo remains missing; numeric zero remains valid.

No cargo magnitude, weather-throughput coefficient, variable choice or model specification was used to select this parser.

The 2019 notation difference is treated as a layout/unit-label presentation difference, not a change to the frozen Port Survey freight-ton outcome family.

Incremental monetary cost remains **0 USD**.

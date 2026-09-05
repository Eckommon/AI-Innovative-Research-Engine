---
id: AU-NEM-F01-OUTCOME-ADJUDICATION
type: outcome-blind-outcome-family-adjudication
created: 2026-09-05
issue: 86
relationship_outcome_computed: false
weather_values_parsed: false
incremental_monetary_cost_usd: 0
---

# AU-NEM-F01 Outcome-Family Adjudication
# AU-NEM-F01 결과 family 사전 판정

## 1. Frozen priority review / 고정 우선순위 검토

The preregistered priority was:
1. binding-constraint burden if generic constraint identity can be assigned prospectively to one region or one region-pair;
2. otherwise direct interconnector congestion/transfer-stress;
3. otherwise HOLD.

## 2. Generic binding-constraint branch / generic binding-constraint branch

AEMO public source semantics confirm:
- DISPATCHCONSTRAINT identifies binding generic constraints through non-zero MarginalValue;
- SPDREGIONCONSTRAINT links GENCONID to REGIONID for region-demand constraint factors;
- SPDINTERCONNECTORCONSTRAINT links GENCONID to INTERCONNECTORID;
- generic constraints can contain multiple LHS terms across regions, interconnectors and connection points.

The bounded F01 snapshot proves that GENCONID-based source links exist, but it does not establish a unique one-region or one-region-pair assignment for the full population of binding network constraints.

Therefore F01 does **not** manufacture a regional binding-constraint burden by allocating mixed constraints after the fact.

Disposition:
**DO_NOT_PROMOTE_GENERIC_REGION_BINDING_BURDEN_IN_F01**

## 3. Predeclared fallback / 사전등록 fallback

Promote the direct AEMO interconnector result family:

**DISPATCHINTERCONNECTORRES.MARGINALVALUE**

Source-defined meaning:
- public five-minute interconnector result;
- shadow price resulting from thermal or reserve-sharing constraints on interconnector import/export;
- zero unless binding under the source semantics.

This is preferred over a custom stress score because the operational meaning is already defined by AEMO.

Candidate future observational identity:
**INTERCONNECTORID × dispatch interval**, restricted prospectively to non-intervention pricing/physical-normal records under the future experiment contract.

F01 does not inspect or summarize MarginalValue magnitudes.

## 4. Interconnector geography / interconnector 지리

The public AEMO INTERCONNECTOR table maps all six current DispatchIS interconnector IDs to deterministic REGIONFROM / REGIONTO endpoints:
- N-Q-MNSP1: NSW1 ↔ QLD1;
- NSW1-QLD1: NSW1 ↔ QLD1;
- VIC1-NSW1: VIC1 ↔ NSW1;
- V-S-MNSP1: VIC1 ↔ SA1;
- V-SA: VIC1 ↔ SA1;
- T-V-MNSP1: TAS1 ↔ VIC1.

Thus six interconnectors collapse to **four unique NEM region-pairs**.

## 5. Weather geometry / 기상 geometry

ABS 2026 State/Territory polygons provide a deterministic official geometry route:
- QLD1 = Queensland;
- NSW1 = New South Wales + Australian Capital Territory;
- SA1 = South Australia;
- VIC1 = Victoria;
- TAS1 = Tasmania.

BOM AWAP historical daily gridded climate files are directly downloadable without credentials. F01 retrieved and hash-pinned one historical daily grid without decompressing or parsing weather values.

A future experiment may define a region or region-pair weather exposure only after separately preregistering:
- one weather variable;
- one region-grid aggregation rule;
- one daily/dispatch temporal aggregation;
- source snapshot and missingness rules.

## 6. Independent-unit warning / 독립단위 경고

Six physical/market interconnector IDs do **not** imply six independent broad-weather exposures.

Two pairs contain parallel interconnectors:
- NSW1 ↔ QLD1: N-Q-MNSP1 and NSW1-QLD1;
- VIC1 ↔ SA1: V-S-MNSP1 and V-SA.

Therefore broad region-pair weather would provide only four distinct spatial exposure units at a time.

Any future experiment must explicitly prevent pseudoreplication. F01 does not authorize treating parallel interconnectors sharing one region-pair weather signal as independent weather clusters.

## 7. Adjudication / 판정

F01 freezes the direct future congestion outcome family as:

**AEMO DISPATCHINTERCONNECTORRES.MARGINALVALUE**

but does **not** automatically authorize a numerical weather-congestion E01 because the broad-region weather design has only four unique region-pair exposure units.

Join feasibility and statistical experiment readiness are kept separate.

Incremental monetary cost remains **0 USD**.

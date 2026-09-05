---
id: AU-NEM-F01-RESULT
type: source-semantic-spatial-temporal-feasibility-result
created: 2026-09-05
issue: 86
state: COMPLETED_PASS
final_gate: PASS_AU_NEM_WEATHER_CONGESTION_JOIN_READY
relationship_outcome_computed: false
weather_values_parsed: false
incremental_monetary_cost_usd: 0
---

# AU-NEM-F01 Result — AEMO Interconnector Congestion × BOM Regional Weather Join Feasibility
# AU-NEM-F01 결과 — AEMO 인터커넥터 혼잡 × BOM 지역기상 조인 실행가능성

## Final gate / 최종 판정

**PASS_AU_NEM_WEATHER_CONGESTION_JOIN_READY**

F01 establishes a deterministic zero-cost official-source join route. It does not establish a weather-congestion relationship and it does not automatically authorize a numerical descendant.

## A. AEMO DispatchIS route / AEMO DispatchIS 경로

Public current and archive DispatchIS files were retrieved and hash-pinned.

Current bounded sample:
- current directory exposed 575 public DispatchIS ZIP links;
- deterministic latest sample at execution: PUBLIC_DISPATCHIS_202609051350_0000000536218851.zip;
- current ZIP SHA-256: ae055b1d29ab9465c7623c016a468e4ba3fcfea43ef53a2e4ec47392c89f361c.

Fixed archive sample:
- PUBLIC_DISPATCHIS_20250902.zip;
- archive ZIP SHA-256: 9ec65ff577fe14cf6d25b8356730fb8b0934e576289d87c49b3f9bb01aa710d0.

Current and archive bounded interval samples expose compatible target schemas for:
- DISPATCH.CONSTRAINT;
- DISPATCH.INTERCONNECTORRES;
- DISPATCH.REGIONSUM.

Bounded current interval identity cardinality:
- 1,033 CONSTRAINTID values;
- 6 INTERCONNECTORID values;
- 5 REGIONID values.

## B. Direct future congestion outcome / 직접 향후 혼잡 outcome

The frozen future outcome family is:

**DISPATCHINTERCONNECTORRES.MARGINALVALUE**

AEMO defines this as the shadow price resulting from thermal or reserve-sharing constraints on interconnector import/export, with zero when not binding.

F01 selected this predeclared fallback because a generic binding-constraint burden cannot be assigned prospectively across the full generic-constraint population to one region/region-pair without mixed-constraint allocation rules.

No MarginalValue magnitude was summarized in F01.

## C. Interconnector identity / 인터커넥터 식별

AEMO public INTERCONNECTOR archive snapshot:
- ZIP SHA-256: 462a622b29328f2f1b8dba87547697dcaf357346ac3442a41d19b9a6efe6251d;
- member SHA-256: aaad06a04de50ac8cc6431df0b376352f01c1233283be15cbe955a461417ff3b.

All six DispatchIS interconnectors map without text inference:

| Interconnector | REGIONFROM | REGIONTO |
|---|---|---|
| N-Q-MNSP1 | NSW1 | QLD1 |
| NSW1-QLD1 | NSW1 | QLD1 |
| T-V-MNSP1 | TAS1 | VIC1 |
| V-S-MNSP1 | VIC1 | SA1 |
| V-SA | VIC1 | SA1 |
| VIC1-NSW1 | VIC1 | NSW1 |

This yields four unique region-pairs.

## D. Constraint identity evidence / constraint 식별 증거

AEMO public generic-constraint factor tables are accessible through GENCONID keys.

Bounded June-2026 archive snapshot:
- SPDREGIONCONSTRAINT: 28 rows / 28 GENCONIDs;
- SPDINTERCONNECTORCONSTRAINT: 5,813 rows / 3,449 GENCONIDs.

Observed structural classes in that bounded archive snapshot:
- ONE_REGION_ONLY: 28;
- ONE_INTERCONNECTOR_ONLY: 2,128;
- MULTI_INTERCONNECTOR_ONLY: 1,321.

These counts are source-structure diagnostics for that archive snapshot, not a claim about the full active generic-constraint universe.

## E. BOM zero-cost weather route / BOM 무비용 기상 경로

A fixed historical BOM AWAP daily gridded temperature file was directly retrieved without credentials:
- URL date: 2025-09-02 daily grid;
- response bytes: 956,910;
- SHA-256: e8a06c91b60131d4e537bcf0b724bcc7f5ac4b4df4fea74824c48ea68f0977fd;
- Content-Type: application/x-compress.

F01 did not decompress or parse weather values.

This proves a reproducible zero-cost gridded-weather distribution route, not the suitability of a particular weather variable.

## F. Official NEM region geometry / 공식 NEM 지역 geometry

ABS ASGS 2026 State/Territory geometry is directly available through the official ArcGIS API.

Frozen NEM geometry mapping:
- QLD1 = Queensland;
- NSW1 = New South Wales union Australian Capital Territory;
- SA1 = South Australia;
- VIC1 = Victoria;
- TAS1 = Tasmania.

The F01 ABS response contained 10 State/Territory features and machine-readable polygon/multipolygon geometry.

## G. Temporal semantics / 시간 semantics

AEMO DispatchIS is a five-minute operational source. AEMO documentation defines interconnector results per dispatch period and current spot-market operations use AEST operational timing.

BOM daily maximum/minimum temperature products use local observation-day conventions around 9am local time.

Therefore a future experiment must preregister an explicit conversion/aggregation boundary before opening selected weather values; F01 does not silently treat AEMO dispatch days and BOM observation days as identical.

## H. Critical limitation / 핵심 한계

The deterministic join is technically ready, but broad regional weather gives only **four unique region-pair exposure units** for the six current interconnectors.

Parallel interconnectors share region-pair weather:
- NSW1-QLD1 pair has two interconnectors;
- VIC1-SA1 pair has two interconnectors.

Thus a future numerical study must solve the independent-unit/inference problem prospectively. Treating six interconnectors as six independent weather clusters would create pseudoreplication.

## What PASS means / PASS 의미

PASS means:
- public AEMO operational data are reproducible;
- a direct source-defined interconnector congestion outcome is available;
- all current interconnector IDs have deterministic NEM region endpoints;
- a zero-cost BOM daily gridded weather route exists;
- official machine-readable region geometry exists.

PASS does **not** mean:
- weather affects congestion;
- an E01 is automatically statistically justified;
- a particular BOM variable should be used;
- region-pair weather is an exact interconnector-corridor exposure;
- causal or investment claims are authorized.

## Mission-ROI disposition / 목적-ROI disposition

Preserve AU-NEM-F01 as a validated join asset.

Do **not** automatically launch a weather-congestion E01 from broad region-pair weather because only four distinct region-pair exposure units exist. Return to Stage 0 so a higher-information design or another candidate can compete.

## Durable evidence / 영속 증거

- research/AU-NEM-F01/README.md
- research/AU-NEM-F01/SOURCE_PREFLIGHT.md
- research/AU-NEM-F01/INTERCONNECTOR_IDENTITY.md
- research/AU-NEM-F01/OUTCOME_ADJUDICATION.md

Incremental monetary cost remained **0 USD**.

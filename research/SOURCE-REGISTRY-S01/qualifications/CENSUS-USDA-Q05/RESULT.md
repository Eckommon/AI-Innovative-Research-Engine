---
id: SOURCE-QUAL-CENSUS-USDA-Q05-RESULT
created: 2026-10-21
parent_issue: 244
prospective_contract_commit: b46760beb68b8b6db2ae667e90e0191673f1706b
original_run: 39455607752
original_evidence_branch_commit: c508cb4edc6c6769a492f13a07f5da2eea82b0c5
evidence_canonical_promotion_commit: 7cd3f40adaf99068a46a4a99f3ca2b120ade48b1
disposition: PASS_Q05_SOURCE_NATIVE_FIPS_SYNTAX_SUPPORT_ONLY__GEOGRAPHY_VINTAGE_UNVERIFIED
scientific_f01_authorized: false
incremental_monetary_cost_usd: 0
---

# Census 2024 × USDA 2023 Q05 — native FIPS syntax only / 군코드 문자열 구조검증 최종 결과

## Terminal operational finding / 종결 판정

**`PASS_Q05_SOURCE_NATIVE_FIPS_SYNTAX_SUPPORT_ONLY__GEOGRAPHY_VINTAGE_UNVERIFIED`**. This is a preregistered **D2+source-native-key string feasibility** observation only: it does not prove equivalent 2023 and 2024 county boundaries or county-level socioeconomic/rurality effect, and does not authorize D3 scientific F01, N01, E01, or R60.

Prior [Q04 D2 receipt](../CENSUS-USDA-Q04/RESULT.md) and SHA fingerprints were durably frozen **before the first Q05 record FIPS projection**. [Q05 contract](CONTRACT.md) merged as `b46760beb68b8b6db2ae667e90e0191673f1706b` before [original Run #39455607752](https://github.com/Eckommon/AI-Innovative-Research-Engine/actions/runs/39455607752).

## Actual source and test proof / 실제 원본검증

Actual GitHub Run #39455607752 **SUCCESS**; 11 Q05 synthetic tests + 9 evidence branch tests **20/20 PASS** before two original URLs each fetched exactly once, verified 200 and full SHA and byte length identical to Q04 **before any record-level ID projection**.

- Census 2024 ZIP full SHA `3c337402b5c6e8d5aa26b4278ccf4edc8989f2683765b3ffbf22296cdb2df3a0`, **141,679 bytes**, `2024_Gaz_counties_national.txt`, only `GEOID` projected.
- USDA 2023 CSV full SHA `ec455ee2a8bc5fc8e070575ea5bee7dce46fc6037f8c3449cbf56e8b45331fa7`, **629,322 bytes**, only `FIPS` projected from long-form `FIPS,State,County_Name,Attribute,Value`; attribute/type/value **never inspected**.
- [Original run JSON](evidence/attempt-01.json) and [.md](evidence/attempt-01.md) were first persisted under unique evidence ref `refs/heads/evidence/s01/census-usda-q05/39455607752`, commit `c508cb4edc6c6769a492f13a07f5da2eea82b0c5`, parent `a50fa5801e1fad06118fdd0db83616b005d83001`. Exactly those two files were independently reviewed in [PR #275](https://github.com/Eckommon/AI-Innovative-Research-Engine/pull/275) and promoted to canonical main `7cd3f40adaf99068a46a4a99f3ca2b120ade48b1`, without any raw row payload, numeric RUCC code or code list.

## Prospective identity support / 고유 FIPS 형식 지원

| Frozen source-native structural metric | Observed |
|---|---:|
| Census 2024 unique five-digit `GEOID` | **3,222** |
| USDA 2023 unique five-digit `FIPS` | **3,235** |
| Distinct syntactically identical source keys | **3,222** |
| USDA unique keys not present in Census 2024 | **13** |
| Census unique keys not present in USDA 2023 | **0** |
| Overlap fraction of distinct USDA keys | **0.99598145** (~99.5981%) |
| Distinct state/territory prefixes of matching IDs | **52** |
| USDA additional rows repeating existing FIPS | **6,468** |
| Invalid code rows | **0** (both sources) |
| Census duplicate source `GEOID` rows | **0** |

All predeclared operational gates were satisfied, including the long-format USDA duplicate condition and support >=3,000 / >=95% / >=50 state-prefix thresholds. Only **aggregate source-ID counts** were persisted, no individual FIPS or matched county list.

## Mandatory interpretation boundary / 연구 미승인

The **13 unmatched USDA keys are not identified or assigned a cause**. They may reflect geographic scope or county-equivalent vintage differences; no state, region, county, population, name or value data were opened to settle this. No evidence yet proves 2023 RUCC FIPS denotes exactly the same geographical area as its 2024 Gazetteer counterpart or that `Attribute` values can be meaningfully aggregated. The index values `FIPS`/`GEOID` establish only source-native syntactic overlap.

A new **Q06 independent county-geography vintage/identifier provenance** contract should precede inspecting the 13 missing keys, crosswalks, or geographic boundary changes; a genuinely scientific candidate would separately preregister a rural/biz outcome hypothesis, exposure measurement and non-causal/ecological caveats, and must not select its design from post-hoc Q05 effects. No new Issue is automatically authorized.

**Prior Q01, Q02, Q03** remain unmodified (Q03 operational HOLD). **Track A E01** is terminal INCONCLUSIVE, Issue #203 CLOSED. S01 Issue #244 sole active. **Cost 0 USD.**

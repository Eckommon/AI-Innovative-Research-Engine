# Census USDA Q05 — only county key syntax / 군코드 형식적 중복 검사

- Verdict / 판정: `PASS_Q05_SOURCE_NATIVE_FIPS_SYNTAX_SUPPORT_ONLY__GEOGRAPHY_VINTAGE_UNVERIFIED`
- Contract: `b46760beb68b8b6db2ae667e90e0191673f1706b`
- Aggregated counts only / 비식별 집계: `{"census_2024_unique_5digit_geoid": 3222, "census_duplicate_key_rows": 0, "census_keys_not_present_in_usda": 0, "distinct_key_overlap": 3222, "distinct_state_prefixes_in_overlap": 52, "invalid_census_key_rows": 0, "invalid_usda_key_rows": 0, "overlap_share_of_usda_keys": 0.99598145, "usda_2023_unique_5digit_fips": 3235, "usda_duplicate_fips_rows": 6468, "usda_keys_not_present_in_2024_census": 13}`
- Exception type / 오류유형: `None`
- 2023 USDA and 2024 Census county geography vintages NOT equivalence-proven.
- RUCC Attribute/Value, individual county names and outcomes were never inspected.
- County matching is syntactic only; scientific F01 is NOT authorized; cost 0 USD.

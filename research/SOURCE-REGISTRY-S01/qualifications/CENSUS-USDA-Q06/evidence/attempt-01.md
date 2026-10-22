# Census×USDA Q06 Island Area scope verification / 13개 군코드 지리범위 검증

- Verdict / 판정: `PASS_Q06_ALL_13_EXPLAINED_BY_DOCUMENTED_ISLAND_AREA_SCOPE__BOUNDARY_EQUIVALENCE_UNVERIFIED`
- Contract: `120930e4bb234ba0c6e652df1c9713fc94e3a2a6`
- Official docs / 공식 문서: Census 2024 Gazetteer; USDA 2023 RUCC; Census ANSI FIPS; Census historical county changes
- Scope counts only / 영토별 비식별 집계: `{"census_keys_in_excluded_island_area_prefixes": 0, "different_geographic_vintages_equivalent_proven": false, "excluded_island_area_prefix_count_total": 13, "individual_county_keys_saved": false, "nonexcluded_usda_only_fips_count": 0, "original_q05_key_count_reconciliation": {"census_2024_unique_5digit_geoid": 3222, "census_duplicate_key_rows": 0, "census_keys_not_present_in_usda": 0, "distinct_key_overlap": 3222, "distinct_state_prefixes_in_overlap": 52, "invalid_census_key_rows": 0, "invalid_usda_key_rows": 0, "usda_2023_unique_5digit_fips": 3235, "usda_duplicate_fips_rows": 6468, "usda_keys_not_present_in_2024_census": 13}, "prospectively_documented_island_area_prefix_totals": {"American Samoa": 5, "Guam": 1, "Northern Mariana Islands": 4, "U.S. Virgin Islands": 3}, "unmatched_key_geography_classification_only": true}`
- Failure class / 예외 유형: `None`
- 2023↔2024 boundary equivalence remains UNVERIFIED; shared code never validates same area.
- No county identifiers, RUCC values, county names, areas or outcomes saved; 0 USD.

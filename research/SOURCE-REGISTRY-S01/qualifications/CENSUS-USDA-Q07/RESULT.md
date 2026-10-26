# CENSUS-USDA-Q07 — terminal source receipt

**Decision:** `PASS_Q07_2023_CENSUS_GAZETTEER_D2_HEADERS_ONLY__GEOGRAPHY_BRIDGE_UNPROVEN`

- Prospective contract: `42ec3673a00a62fceaa7812868e79a38a4ee8456`.
- Earlier Run #39843043780: offline synthetic failure, no original Census GET (see PREFLIGHT-FAILURE-01.md).
- Original first-source Run #39857822969: SUCCESS; 13/13 Q07 offline and 9/9 persistence tests passed before GET.
- Official Census 2023 county ZIP: HTTP 200; 141650 bytes; SHA-256 `919df59ba90759cce85468c0337e898e4b39c08eaffce86ddd88fa41f1f7f0c8`. Single 2023_Gaz_counties_national.txt member, 647830 uncompressed bytes; literal GEOID header.
- Immutable original evidence ref: `c65eb7be968c223f3bc7a9cd9b285426d24d12a9`; audited JSON and MD only promoted by PR #289, main `70124e3a61118a21f9360e5f425f4da717bacfc3`.
- All county rows, values, RUCC classifications, geometry and 2023/2024 equivalence remain unexamined. D2 only; no F01 authorization.
- Track A E01 terminal INCONCLUSIVE and #203 closed; Track B S01 #244 sole active. 0 USD.

**Next:** Independently freeze Q08 exact 2023 and 2024 Census raw SHA, key-only support rules, official 2023–2024 geography references before row-ID access. Never assume GEOID equality proves identical county boundaries.

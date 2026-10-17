# R58 — official source metadata preflight / 공식 자료 메타데이터 실측

- UTC: \`2026-10-17T10:01:05.955756+00:00\`
- Scientific stage: **PRE-SCORE; NO OUTCOME ROWS OPENED** / 결과행 미개봉

| Exact official file | HTTP | Read bytes | Preflight interpretation |
|---|---:|---:|---|
| \`NHTSA_campaign_zip\` | 200 | 4 | \`PREFIX_MATCH_BODY_UNINSPECTED\` |
| \`NHTSA_quarterly_zip\` | 200 | 4 | \`PREFIX_MATCH_BODY_UNINSPECTED\` |
| \`NHTSA_campaign_dictionary\` | 200 | 3053 | \`DICTIONARY_PREFIX_ACCESSED_ONLY\` |
| \`NHTSA_quarterly_dictionary\` | 200 | 1244 | \`DICTIONARY_PREFIX_ACCESSED_ONLY\` |
| \`Census_CBP_2023_county_zip\` | 200 | 4 | \`PREFIX_MATCH_BODY_UNINSPECTED\` |
| \`BLS_QCEW_2024_county_csv_header\` | 200 | 896 | \`CSV_HEADER_ONLY_ACCESSED\` |
| \`NOAA_StormEvents_2023_gzip\` | 200 | 2 | \`PREFIX_MATCH_BODY_UNINSPECTED\` |

Only ZIP/gzip signatures, published dictionaries and a single CSV header are inspected. This is not a binary full-body download nor a source-native exact join; a 200 response is never scientific evidence of a relationship. / 본문·결과변수·정확조인 미검증.

**Candidate access dispositions / 후보별:**
- \`NHTSA\`: \`METADATA_PREFIX_READY_NO_JOIN_PROOF\`
- \`CBP_QCEW\`: \`METADATA_ACCESS_ONLY_NO_JOIN_PROOF\`
- \`NOAA_QCEW\`: \`METADATA_ACCESS_ONLY_NO_JOIN_PROOF\`

Incremental cost / 추가비용: **0 USD**.

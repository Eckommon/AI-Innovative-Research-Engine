# R59 first-party frontdoor source preflight / 원천 입구 실측

- At UTC: \`2026-10-18T06:13:24.970937+00:00\`
- **No future outcome rows, no whole ZIP bodies, no exact entity joins, no scores**.

| Frozen source | HTTP | Method | Bytes read | Signal |
|---|---:|---|---:|---|
| \`IPEDS_2023_24_final_zip\` | 200 | GET | 4 | \`ZIP_SIGNATURE_ONLY_NOT_ARCHIVE_PROVEN\` |
| \`SCORECARD_2025_institution_zip\` | 403 | GET | 0 | \`HTTP_UNVERIFIED_NO_ABSENCE_CLAIM\` |
| \`SEC_submissions_bulk_zip\` | 403 | HEAD | 0 | \`HTTP_UNVERIFIED_NO_ABSENCE_CLAIM\` |
| \`SEC_companyfacts_bulk_zip\` | 403 | HEAD | 0 | \`HTTP_UNVERIFIED_NO_ABSENCE_CLAIM\` |
| \`USPTO_fee_catalog\` | 200 | HEAD | 0 | \`HEAD_METADATA_ONLY_NOT_SOURCE_BODY_PROVEN\` |
| \`USPTO_product_api_documented_key\` | 403 | HEAD | 0 | \`HTTP_UNVERIFIED_NO_ABSENCE_CLAIM\` |

**Caveat / 제한:** 200 HTTP or ZIP magic proves only a particular metadata/prefix response, not whole file, source-unit equivalence or future releases. SEC 403 is not necessarily absence; USPTO account/API-key restrictions cannot be bypassed. College Scorecard delivery URL is ED Data.gov-catalog-linked but a nongov host, not automatically independent first-party.

Additional cost: **0 USD**.

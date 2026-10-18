# Q01 — FEMA×EPA paired official source qualification / FEMA·EPA 공식 출처

- Verdict / 판정: HOLD_SOURCE_ACCESS_OR_SCHEMA
- Source key: FEMA fipsStateCode+fipsCountyCode vs EPA State Code+County Code
- Actual exact county join / 실측 조인: **NOT EXECUTED**
- Case/event/AQI data rows / 사건·대기질 값: **NOT OPENED**

| Original agency | Official body bytes | Full SHA256 | Exact header semantics |
|---|---:|---|---|
| FEMA_v2_full_CSV | 25009462 | 0c51c72b0fd4f616afeb01bb1f7e95f6b7f1349832f7b3be9d12e7dd7e5aaa30 | fipsStateCode+fipsCountyCode |
| EPA_2024_county_annual_AQI_ZIP | 20730 | f6bec6492d0d2a64c557a48ca7d54aa5ac39993051d1eea43d055d9b391d689b | State Code+County Code |

Never substitute a differently dated source or claim an F01 PASS from D2 original bytes. / 원본 확보는 과학적 인과 또는 F01 승인이 아닙니다.

Incremental monetary cost **0 USD**.

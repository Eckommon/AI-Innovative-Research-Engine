# FAA F01 archive first-four-byte preflight / 공식 ZIP 4바이트 검증

- Decision: HOLD_FAA_F01_EXACT_OFFICIAL_ARCHIVE_ACCESS_NOT_READY
- Read only at most four bytes from each archive, no ZIP members or owner records. / 파일 내부 데이터 미열람.

| Archive | HTTP | Read | ZIP signature |
|---|---|---|---|
| current | 406 | 0 | False |
| 2020 | 302 | 0 | False |
| 2021 | 302 | 0 | False |

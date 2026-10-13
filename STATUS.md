---
checkpoint_id: CHK-20261013-US-CMS-NPI-E01-ACTIVE
active_issue: 203
active_research: US-CMS-NPI-E01
last_completed_issue: 202
last_completed_research: US-CMS-NPI-N01
last_decision: DEC-318
updated: 2026-10-14
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_CMS_NPI_E01_ACTIVE__WAIT_SOURCE_PREREGISTERED_RUNNER_READY`

US-CMS-NPI-E01 remains active under pre-Issue contract `48843c9979336dcd10fdff984f458277062d6f20`.

Metadata-only Source Preflight 02 is immutable at `a479ce80c25ef13db37d46940aa7d4e14fe8f9c9` and returned:

`WAIT_SOURCE_US_CMS_NPI_E01`

Live official CMS listing observed on 2026-10-14:
- `100526_101126` = 2026-10-05..2026-10-11;
- qualifying post-baseline weekly count = **0**;
- ZIP body opened = **false**;
- future deactivation membership opened = **false**.

The preregistered E01 runner remains frozen at `edaeb7c405f53a341753e0c5989706992ae301a5` and guarded workflow at `409f825cf0563f01d8c3ef98ff0fccec8113cf01`.

## Exact next action / 정확한 다음 행동

Do not execute E01 yet. Re-run metadata-only source discovery after CMS publishes a new weekly listing. Once the first official V2 weekly listing with covered start >= 2026-10-12 and covered end > 2026-10-12 exists, add the explicit Issue #203 execution marker and run the already-frozen E01 exactly once.

No monthly substitution or later-week selection is permitted.

Incremental monetary cost remains **0 USD**.

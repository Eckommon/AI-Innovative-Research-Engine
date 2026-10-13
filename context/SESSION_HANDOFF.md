---
checkpoint_id: CHK-20261013-US-CMS-NPI-E01-ACTIVE
active_issue: 203
active_research: US-CMS-NPI-E01
last_completed_issue: 202
last_completed_research: US-CMS-NPI-N01
last_decision: DEC-318
updated: 2026-10-13
---

# Session Handoff / 세션 인계

`US_CMS_NPI_E01_ACTIVE__WAIT_FIRST_QUALIFYING_WEEKLY_UPDATE`

- Issue #203 open.
- E01 contract: `48843c9979336dcd10fdff984f458277062d6f20`.
- Parent N01: 18/18 PASS, 346,859 matched pairs.
- Baseline monthly full SHA: `45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e`.
- Baseline deactivation SHA: `fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1`.
- Exposure: multi-taxonomy Type-2 organization.
- Control: matched single-taxonomy Type-2 organization.
- Latest visible weekly at preregistration: `100526_101126` (2026-10-05..2026-10-11), pre-baseline metadata only.
- Future qualifying body opened: false.
- Primary test: exact two-sided McNemar on frozen matched pairs.
- Minimum support: >=30 deactivated matched NPIs and >=20 discordant pairs.
- Material MOR band: <=0.80 or >=1.25.
- No monthly substitution or later-week cherry-picking.
- Next: metadata-only source preflight; remain WAIT_SOURCE if no qualifying weekly exists.
- Cost: 0 USD.

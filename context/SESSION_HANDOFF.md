---
checkpoint_id: CHK-20261013-US-CMS-NPI-E01-ACTIVE
active_issue: 203
active_research: US-CMS-NPI-E01
last_completed_issue: 202
last_completed_research: US-CMS-NPI-N01
last_decision: DEC-318
updated: 2026-10-14
---

# Session Handoff / 세션 인계

`US_CMS_NPI_E01_ACTIVE__WAIT_SOURCE_PREREGISTERED_RUNNER_READY`

- Issue #203 open.
- E01 contract: `48843c9979336dcd10fdff984f458277062d6f20`.
- Parent N01: 18/18 PASS; 346,859 matched pairs.
- Source Preflight 01: `0e81620e9cbea5dcddb558791e786d1565dfaf0f` — WAIT_SOURCE.
- Source Preflight 02: `a479ce80c25ef13db37d46940aa7d4e14fe8f9c9` — WAIT_SOURCE.
- **Source Preflight 03:** PR #205 merged `a29708eaaa5794eccac9d11aff82e809635b287b`; immutable GitHub Actions evidence commit **`c071f0fd4161ca5b3bb7a69062d06611582ee36a`**, verified 2026-10-13T23:27:50Z; `WAIT_SOURCE_US_CMS_NPI_E01`, HTTP 200, official listing SHA-256 `f00a6c37989e58ad6f227a89a102ae9c176cdebe5ea15bdc356b15bdc`, qualifying count 0, earliest null, metadata-only true, future ZIP/member opened false. / 세 번째 공식 목록 검증 완료; 결과 데이터 미열람.
- Live weekly listing remains `100526_101126` = 2026-10-05..2026-10-11.
- Qualifying weekly listings: **0**.
- Future weekly ZIP body opened: false.
- Future deactivation membership opened: false.
- E01 runner: `edaeb7c405f53a341753e0c5989706992ae301a5`.
- Guarded workflow: `409f825cf0563f01d8c3ef98ff0fccec8113cf01`.
- Operational guard hardening merged: PR #204 / `161bc80db844215965b4d6dd044558d12e241ae5`; exact standalone Issue #203 execution marker for both manual/issue routes, serialized Attempt-01, CMS listing metadata-only early check. Frozen scientific runner unchanged; marker absent.
- Frozen primary test: exact two-sided McNemar, matched discordant OR + exact 95% CI.
- Minimum support: >=30 deactivated matched NPIs and >=20 discordant pairs.
- Material association band: MOR <=0.80 or >=1.25.
- **Persistent source watch / 지속 소스 감시:** PR #206 merged `b4fa7a49fdf5958e069ba5a7318bb555c4a3afc8`; `.github/workflows/watch-us-cms-npi-e01-source.yml` scheduled daily at 00:37 UTC/09:37 KST (public-repo standard runner; zero monetary cost). Offline regression fixtures added (7). Rechecks only the official HTML listing, does not commit repeated WAITs, writes immutable `source-candidate-01.json/.md` only for first observed eligible weekly, does **not** open future ZIP or authorize E01. One-time bootstrap run receipt added by PR #207 / `c1bf33ae73ae02f4b1ce94ef5b71ed2688757aa0`: first successful official metadata-only WAIT check after regression tests writes immutable `source-watch-bootstrap-01.{json,md}` with run ID and source SHA, then all later WAITs make no commits. This is not experiment authorization or outcome evidence. Actual Actions runtime confirmation is pending receipt verification. / 예약 소스 점검은 최초 후보의 메타데이터 근거만 고정하며 E01은 자동 실행하지 않음.
- Next: inspect the first source-watch Actions run and/or immutable first-candidate evidence, independently adjudicate the first qualifying publication rule, then append exact Issue #203 execution marker and run frozen E01 once; otherwise continue WAIT_SOURCE.
- Cost: 0 USD.

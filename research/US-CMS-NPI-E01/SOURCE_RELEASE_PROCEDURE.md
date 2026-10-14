# US-CMS-NPI-E01 — First-Source Release Procedure / 최초 소스 출처 확정 절차

**Status / 상태:** OPERATIONAL_GUARD_PREPARED — NOT_RELEASED / 운영 검증 준비, 아직 실행 승인되지 않음  
**Issue:** [#203](https://github.com/Eckommon/AI-Innovative-Research-Engine/issues/203)  
**Frozen scientific contract:** \`48843c9979336dcd10fdff984f458277062d6f20\`  
**Cost:** \`0 USD\`

## Purpose / 목적

**KO:** 기존 E01의 첫 적격 CMS V2 주간 파일 규칙을 변경하지 않고, 자동 감시가 최초 기록한 출처와 실험 실행 직전에 관측한 출처가 **정확히 동일**하며 그 이전에 공개된 더 이른 적격 주간 파일을 건너뛰지 않았음을 독립 검토합니다. E01 사전등록 실험기, 346,859쌍, 사건 정의, 18개 실행 무결성 게이트와 McNemar 판정 기준은 절대로 변경하지 않습니다.

**EN:** This is an additional *operational authorization barrier*, not a new scientific criterion. The recorded first observed eligible CMS V2 weekly and the source selected at execution must be identical, and the first-publication lineage must be independently adjudicated before the experiment. The pre-Issue study and frozen experiment runner are unchanged.

## First-source surveillance operation / 최초 적격 주간 파일 감시 운영

The public-repository standard GitHub Actions source watcher checks the official CMS **HTML listing metadata only** at four scheduled UTC slots (`00:37`, `06:37`, `12:37`, `18:37`; corresponding to `09:37`, `15:37`, `21:37`, `03:37` Asia/Seoul). GitHub cron execution may be delayed; these are *scheduled* times, never a guaranteed actual publication-observation time. This is a risk-reduction measure after a verified 2026-10-14 cron dispatch was delayed by several hours. / 첫 적격 자료의 누락 위험을 줄이기 위한 6시간 간격의 감시이며, GitHub 예약 실행 시각 자체는 보장되지 않습니다.

If there is no qualifying weekly listing, no additional `WAIT_SOURCE` commit or alert is generated. On the **first** observed qualifying V2 weekly, the watcher immutably commits `source-candidate-01.json/.md` and may post a **candidate-only review notice** to Issue #203; this notification is neither the scientific source-release authorization nor permission to run E01. After the first candidate is recorded, after an attempt exists, after the Issue closes, or after an explicit experimental execution marker is present, the listing-only watch stays dormant and does not download any ZIP. / 첫 후보 발견 이후에도 운영 알림만 허용하며, 최초 공개 검증과 실험 실행 결정은 독립 절차에 둡니다.

No paid GitHub runners, external paid APIs or periodic artifact uploads are used; incremental monetary cost must remain **0 USD**. / 유료 서비스 승인 없이 사용 불가.

## Required chronological sequence / 필수 순서

1. **Source detection / 소스 탐지:** \`.github/workflows/watch-us-cms-npi-e01-source.yml\` preserves \`research/US-CMS-NPI-E01/evidence/source-candidate-01.json\` + \`.md\` on its first observation. Before this occurs, E01 stays \`WAIT_SOURCE\`. The source ZIP must remain unopened.
2. **Independent source-lineage review / 최초 공개 계보 검증:** Verify the immutable pre-baseline CMS snapshot (\`source-preflight-03.json\`), candidate HTML listing snapshot, their timestamps and weekly covered intervals. Confirm the candidate is **the earliest qualifying weekly appearing after preregistration**, not just the earliest remaining in a later, rotating listing. A skipped/withdrawn/missing earlier weekly that cannot be distinguished from monitoring failure is **not** automatically assumed nonexistent. Keep \`HOLD_SOURCE_LINEAGE_REVIEW\` without opening the ZIP if evidence is insufficient. The watcher **cannot** self-certify this review.
3. **Persist release authorization / 출처 승인증빙 확정:** If independent sources establish the frozen first-publication rule, create exactly once \`research/US-CMS-NPI-E01/evidence/source-release-authorization-01.json\` on \`main\` in its own commit. Populate **actual** source identity and full SHA-256 of the **exact committed raw bytes** of \`source-candidate-01.json\`; include at least two true source-evidence paths and concrete review notes. Never invent or backfill an unobserved CMS publication time.
4. **Operational dry check / 실행 전 점검:** Run \`python -m tools.verify_us_cms_npi_e01_source_release\`. It re-fetches **only official CMS HTML metadata** and fails unless the live earliest qualifying V2 weekly (token, start/end, HTTPS ZIP URL) exactly matches both the candidate and the separately reviewed release record.
5. **Experiment authorization / 본 실험 승인:** Only after a successful source release check, add the exact standalone \`EXECUTE_US_CMS_NPI_E01_ATTEMPT_01\` line to Issue #203. This triggers the existing E01 workflow; both manual and issue-edit dispatch still require the marker. The first-source release check happens **before** any baseline or future ZIP retrieval.
6. **Exact ZIP transport binding / ZIP 접근의 실제 고정:** The execution workflow invokes `python -m tools.run_us_cms_npi_e01_transport_locked` rather than directly calling the scientific runner. This operational wrapper intercepts the unchanged runner's three downloads at the transport boundary and permits **exactly** (1) the preregistered full baseline ZIP, (2) the preregistered deactivation baseline ZIP, and (3) the exact independently approved weekly ZIP, in that order and with fixed target filenames. A changed weekly listing or fourth/unapproved download fails **before HTTP download**, so release-check-to-execution source drift cannot silently select a later file. If the frozen runner raises or its chosen source differs, the workflow cannot promote that attempt as valid. / 승인받은 ZIP 이외의 실제 다운로드를 차단하고, 통계 계산기는 원본 그대로 유지합니다.
7. **Actual source and scientific result / 과학적 판정:** Frozen E01 must reproduce exact baseline SHA and 346,859 pairs, enforce all original 18 gates, and classify the study exactly as preregistered. A scientific result is **not** inferred from source release approval.

## Authorization record contract / 출처 승인 JSON 계약

This is an **illustrative structure only**, not a release decision, and must not be committed under the evidence filename until official source observations genuinely support every field. / 아래는 예시 스키마이며 현재의 실제 소스 승인 결과가 아닙니다.

\`\`\`json
{
  "research": "US-CMS-NPI-E01",
  "issue": 203,
  "contract_sha": "48843c9979336dcd10fdff984f458277062d6f20",
  "candidate_sha256": "<exact-64-character-SHA-256-of-committed-candidate-json>",
  "decision": "PASS_US_CMS_NPI_E01_SOURCE_RELEASE_LOCK",
  "first_publication_adjudication": "PASS",
  "prior_week_exclusion_reviewed": true,
  "approved_source": {
    "token": "<actual-official-covered-range-token>",
    "start": "<actual-YYYY-MM-DD>",
    "end": "<actual-YYYY-MM-DD>",
    "href": "<actual-https-download.cms.gov-nppes-weekly-V2-zip>"
  },
  "evidence_refs": [
    "research/US-CMS-NPI-E01/evidence/source-preflight-03.json",
    "research/US-CMS-NPI-E01/evidence/source-candidate-01.json"
  ],
  "review_notes": "<substantive-independent-review-of-official-chronological-listing-lineage>",
  "zip_body_opened": false,
  "future_membership_opened": false,
  "incremental_monetary_cost_usd": 0
}
\`\`\`

## Explicit non-claims / 금지 주장

- An *observed candidate* is not sufficient proof of the *first publication*. / 최초 발견과 최초 공개 검증은 다름.
- The source lock is not scientific evidence of NPI deactivation difference. / 출처 승인만으로 통계적 결과를 선언하지 않음.
- Do not substitute a monthly ZIP, cherry-pick later weekly updates, change a frozen statistic, or infer provider closure, licensure, quality or causality. / 월간 대체·후속 주차 선택·기준 변경·의료기관 폐업 등 추론 금지.
- If the source rotates or the candidate and current HTML listing disagree, fail closed. / 목록 갱신으로 원본과 최신 소스가 다르면 실행 차단.
- Repeating these checks must not create a second source candidate, modify earlier evidence, or incur a new paid service. / 불변 근거 변경 및 유료 서비스 사용 금지.

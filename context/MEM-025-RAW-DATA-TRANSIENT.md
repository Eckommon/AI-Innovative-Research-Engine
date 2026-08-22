---
id: MEM-025
type: memory
state: ACTIVE
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - docs/RAW_DATA_TRANSIENT_POLICY.md
  - registry/DEC-022.md
---

# MEM-025 — RAW_DATA_TRANSIENT_ONLY

**KO:** 외부 공개 raw data는 기본적으로 GitHub에 복제하지 않는다. 재현에 필요한 exact source/version/checksum을 고정한 뒤 standard zero-cost execution environment에서 일시 다운로드·분석하고 raw bytes는 실행 종료 시 폐기한다. GitHub에는 provenance, checksum, deterministic code, integrity inventory, derived summaries/results만 남긴다. 비용 가능 경로는 `COST-001` 사전승인 없이는 사용하지 않는다.

**EN:** External public raw data are transient by default. Freeze exact source/version/checksum, download and analyze only in a standard zero-cost execution environment, and discard raw bytes at teardown. Persist provenance, checksums, deterministic code, integrity inventories, and derived summaries/results only. Any potentially paid route remains blocked by `COST-001` without prior approval.

**E09 application:** NIST coupling ZIP and BP1 raw inputs are transient-only; case `3.2` filename preflight precedes numeric coupling access.

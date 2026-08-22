---
id: RAW-001
type: governance
state: ACTIVE
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - docs/NO_COST_POLICY.md
  - docs/HALLUCINATION_CONTROL_PROTOCOL.md
  - registry/DEC-022.md
---

# RAW-001 — Transient Raw-Data Execution Policy / 원천데이터 일시 실행 정책

## 1. Rule / 원칙

**KO:** 외부의 권위 있는 공개 원천데이터는 원칙적으로 GitHub 저장소에 복제·영구보관하지 않는다. 재현 가능한 분석에 필요한 경우 실행 환경(GitHub Actions standard runner 또는 승인된 로컬 환경)에 **일시 다운로드**하여 checksum·version·manifest를 검증하고 분석한 뒤, 실행 종료와 함께 raw bytes를 폐기한다.

**EN:** Authoritative external public raw data are not duplicated or permanently stored in this GitHub repository by default. When needed for reproducible analysis, they are **downloaded transiently** into the execution environment (a standard GitHub Actions runner or an approved local environment), verified by version/manifest/checksum, analyzed, and discarded with the execution environment.

Canonical state / 표준 상태: **`RAW_DATA_TRANSIENT_ONLY`**.

## 2. Persist / 영구 기록 대상

GitHub에는 다음만 지속 기록한다. / Persist only:
- authoritative source/PDR/DOI and exact version or snapshot identifier;
- expected and observed checksum plus file size;
- download/retrieval path sufficient for reproduction;
- deterministic analysis code and frozen parameters;
- filename/schema/integrity inventories when scientifically relevant;
- derived summaries, statistics, gates and RESULT records;
- source conflicts, unknowns and exclusions.

## 3. Do Not Persist by Default / 기본 비저장 대상

- downloaded raw ZIP/HDF5/XLSX/CSV/TXT bytes from authoritative external sources;
- extracted raw files;
- large intermediate arrays/caches;
- GitHub Actions artifacts containing raw source data.

An exception requires a documented scientific/reproducibility necessity plus applicable licensing/privacy/security review; if cost may be incurred, `COST-001` approval is also required before execution. / 예외는 과학적·재현성 필요성과 라이선스·보안 검토를 문서화하며 비용 가능 시 `COST-001` 사전승인을 추가 적용한다.

## 4. Execution Order / 실행 순서

`source identity/version → expected checksum → transient download → actual checksum → integrity/schema/filename preflight → numeric access if authorized → frozen computation → derived writeback → raw deletion/runner teardown`

Where an outcome-blind integrity gate is preregistered, metadata/filename inspection must occur before numeric outcome access. / outcome-blind gate가 고정된 경우 숫자값 열람 전에 metadata/filename 검사를 수행한다.

## 5. Cost Boundary / 비용 경계

`RAW-001` does not override `COST-001`. Public-source download and standard public-repository GitHub-hosted runner execution may be used only when the route remains zero incremental monetary cost. Paid storage, larger/GPU runners, paid APIs, metered external compute or uncertain billing remain prohibited without explicit user approval. / 공개데이터·standard runner라도 추가비용 0원일 때만 기본 허용한다.

## 6. AMBENCH-E09 Application / E09 적용

For Issue #24 `AMBENCH-E09`:
- `dynamic_laser_coupling_data.zip` is transient-only;
- BP1 thermography/optical inputs are transient-only;
- no raw NIST bytes or raw-data Actions artifact is committed/uploaded;
- the case `3.2` archive filename preflight occurs before coupling numeric values are read;
- GitHub preserves checksums, archive inventory, code, derived case summaries and final evidence only.

**Status:** `ACTIVE — PROJECT-WIDE DEFAULT`.

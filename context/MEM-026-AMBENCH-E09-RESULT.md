---
id: MEM-026
type: memory
state: VALIDATED_RESULT
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-E09/RESULT.md
  - registry/DEC-023.md
  - Issue #24
---

# MEM-026 — AMBENCH-E09 Result / AMBENCH-E09 결과

**KO:** E09는 Run `32550309862`에서 성공 실행되어 `INCONCLUSIVE_CASE_LEVEL`로 종료한다. checksum-verified `mds2-3842` v1.0.3 ZIP에는 `3_2_1sv.txt`, `3_2_2sv.txt`, `3_2_3sv.txt`가 모두 직접 존재하여 E09 분석의 case `3.2` third-repeat identity가 해결됐다. 그러나 F08 summary CSV의 중복 filename provenance inconsistency는 역사적으로 보존한다. BP4 frozen coupling case medians는 `0:0.6347681, 1.1:0.7287823, 1.2:0.5507982, 2.1:0.6152821, 2.2:0.6480267, 3.1:0.6649222, 3.2:0.5964035`. Coupling-weighted VED는 process-only VED의 7-case rank를 정확히 보존하여 모든 endpoint의 `delta_rho=0`. primary thermal은 `rho=0.0714286`, axis concordance `2/3`; 최종 gate는 `INCONCLUSIVE_CASE_LEVEL`. raw NIST data는 `RAW_DATA_TRANSIENT_ONLY`로 처리되어 artifact/commit 없이 teardown 성공했다.

**EN:** E09 completed successfully in Run `32550309862` with final gate `INCONCLUSIVE_CASE_LEVEL`. The checksum-verified `mds2-3842` v1.0.3 ZIP directly contains `3_2_1sv.txt`, `3_2_2sv.txt`, and `3_2_3sv.txt`, resolving the case `3.2` third-repeat identity for E09 analysis while preserving the historical summary-CSV provenance inconsistency. Frozen BP4 coupling case medians are `0:0.6347681, 1.1:0.7287823, 1.2:0.5507982, 2.1:0.6152821, 2.2:0.6480267, 3.1:0.6649222, 3.2:0.5964035`. Coupling-weighted VED preserves the exact seven-case rank of process-only VED, so every endpoint has `delta_rho=0`. Primary thermal `rho=0.0714286`, axis concordance `2/3`; final gate `INCONCLUSIVE_CASE_LEVEL`. Raw NIST data were handled under `RAW_DATA_TRANSIENT_ONLY` and successfully torn down without artifact/commit persistence.

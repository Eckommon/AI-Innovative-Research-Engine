---
id: AMBENCH-E14-RESULT
type: experiment-result
state: COMPLETED_HOLD_SOURCE_INTEGRITY
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-E14/README.md
  - Issue #32
---

# AMBENCH-E14 Result — A-AMB Stationary-Spot External Physical-Dynamics Test
# AMBENCH-E14 결과 — A-AMB stationary-spot 외부 물리동역학 검증

**Frozen final gate / 고정 최종 판정:** **`HOLD_SOURCE_INTEGRITY`**

## 1. Executive Result / 핵심 결과

**KO:** E14는 수치분석 단계까지 진행되지 않았다. NIST 공식 PDR/Data.gov metadata에서 `mds2-2525` v1.3.1의 두 고정 component와 expected SHA-256을 재확인했지만, 현재 실행환경에서 authoritative `Al_Spot_TDA_Results.csv`와 `Al_Spot_TDW_Results.csv`의 raw bytes를 반복적으로 가져오지 못했다. NIST direct fetch는 timeout으로 실패했고, 제공된 transient container의 direct network도 사용할 수 없었으며, exact-checksum을 검증할 수 있는 공개 mirror도 targeted search에서 확인되지 않았다. 사전등록은 authoritative source retrieval failure를 `HOLD_SOURCE_INTEGRITY`로 명시했으므로 수치값을 추정·복원·대체하지 않고 HOLD로 종료한다.

**EN:** E14 did not reach numerical analysis. Official NIST PDR/Data.gov metadata reverified the two frozen `mds2-2525` v1.3.1 components and expected SHA-256 values, but the authoritative raw bytes for `Al_Spot_TDA_Results.csv` and `Al_Spot_TDW_Results.csv` could not be retrieved in the current execution environment. NIST direct fetches repeatedly timed out, direct network access from the provided transient container was unavailable, and targeted search did not identify a public mirror whose bytes could be verified against the frozen checksums. Because the preregistration explicitly maps authoritative source retrieval failure to `HOLD_SOURCE_INTEGRITY`, E14 terminates at HOLD without estimating, reconstructing, or substituting numerical values.

## 2. Reverified Authoritative Metadata / 재검증 authoritative metadata

Official NIST PDR v1.3.1 and Data.gov catalog metadata support:
- DOI `10.18434/mds2-2525`;
- `Al_Spot_TDA_Results.csv` — time-dependent absorption, expected SHA-256 `3f0b6812f98535f5ffbb0e2fed31f084ad9a7f9cc393c04a43ed57f0bb14bf69`;
- `Al_Spot_TDW_Results.csv` — time-dependent stationary melt-pool width, expected SHA-256 `06b280222eab5f82eb9dcfb0689f20a5011c16e115548cd94ce120e5a97b4f5c`;
- NIST challenge semantics: stationary Al laser duration `1.982 ms`; TDA time zero at laser start with `40 ns` nominal interval; TDW at `20 µs` intervals during laser-on time.

The official Data.gov distribution explicitly points both result files to NIST `data.nist.gov` download URLs.

## 3. Retrieval Attempts / retrieval 시도

Zero-incremental-cost routes attempted after E14 preregistration:
1. NIST direct version/component retrieval through the provided transient execution environment — failed because that environment could not resolve `data.nist.gov`;
2. NIST direct resource fetch through the web retrieval layer via the official Data.gov download links — repeated timeout for both TDA and TDW files;
3. dedicated URL download helper after the official download URLs had been surfaced — download failed;
4. targeted public web/GitHub search for exact filenames and/or frozen SHA-256 values — no independently retrievable checksum-verifiable mirror established.

No paid API, paid storage, paid cloud compute, or paid data route was attempted. Under `COST-001` + `DEC-028`, no paid fallback may be used without prior explicit user approval.

## 4. Numerical Outcome Access State / 수치 outcome 접근 상태

- `Al_Spot_TDA_Results.csv` numerical values analyzed: **NO**;
- `Al_Spot_TDW_Results.csv` numerical values analyzed: **NO**;
- primary alignment intervals constructed: **NO**;
- `rho_primary`: **NOT_COMPUTED**;
- circular-shift null: **NOT_COMPUTED**;
- relative-absorption sensitivity: **NOT_COMPUTED**;
- transferred descriptors: **NOT_COMPUTED**.

Therefore no scientific statement about the stationary-Al absorptance↔width dynamic relationship is authorized by E14.

## 5. Frozen Gate Application / 고정 gate 적용

### `HOLD_SOURCE_INTEGRITY`
Preregistered condition includes any authoritative source retrieval failure.

Observed:
- authoritative source metadata and expected checksums are known;
- authoritative component bytes were not retrievable in the current environment;
- checksum verification of downloaded bytes therefore cannot be completed.

**PASS → selected final gate.**

All downstream outcome gates are not evaluated because source byte integrity is a prerequisite.

## 6. Interpretation Boundary / 해석 경계

This HOLD means:
- **not** that the NIST files are absent;
- **not** that the physical relation is negative;
- **not** that the data are invalid;
- only that this execution could not retrieve and checksum-verify the authoritative bytes using the currently available zero-cost routes.

F13 remains valid as a source-readiness result because it was metadata/source-identity based. E14 numerical validation remains unresolved.

## 7. Cost & Raw-Data Integrity / 비용·raw-data 무결성

- additional monetary cost: `0`;
- no potentially billable route used;
- no raw source file persisted to GitHub;
- transient local remnants removed;
- `RAW_TEARDOWN=SUCCESS`.

## 8. Consequence / 후속

Do not alter the frozen E14 method or substitute non-authoritative numerical values. A future retry is eligible only if the same authoritative files become retrievable through a verified zero-incremental-cost route, or if the user explicitly approves a specific paid route **before** any cost-generating action. On a no-cost retry, the existing frozen E14 preregistration should be reused rather than redesigned after outcome exposure.

---
id: AMBENCH-POST-E09-TRIAGE
type: candidate-triage
state: COMPLETED_SELECTED_F10
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-D06/RESULT.md
  - research/AMBENCH-E09/RESULT.md
  - DEC-023
---

# AMBENCH Post-E09 Candidate Triage / E09 이후 후보 선별

## 1. Decision Question / 의사결정 질문

**KO:** D06의 `PROCESS_CASE_PROXY_DOMINANT`와 E09의 `INCONCLUSIVE_CASE_LEVEL`이 드러낸 한계를 가장 직접적으로 깨뜨리는 다음 연구 관계는 무엇인가?

**EN:** Which next scientific relationship most directly breaks both the D06 `PROCESS_CASE_PROXY_DOMINANT` limitation and the E09 `INCONCLUSIVE_CASE_LEVEL` limitation?

## 2. Controlling Limitations / 지배 한계

### D06
- 8/8 thermal occupancy features were case-dominated.
- within-case variance fractions were all below approximately `0.00463`.
- `PCA95_DIM=2`; first two PCs explained `98.2647%`.
- consequence: do not escalate model capacity on the same 21 tracks/representation; seek independent conditions or genuinely different information.

### E09
- BP4 coupling changed predictor magnitude but preserved exactly the seven-case process-only rank.
- every frozen endpoint therefore had `delta_rho=0`.
- cross-BP1/BP4 comparison remained `UNPAIRED_NOMINAL_CASE_FAMILY / AGGREGATE_ONLY` because BP1 and BP4 are separate specimens and process vectors differ.
- consequence: do not tune the same rank test; seek magnitude/temporal information or a same-specimen relationship.

## 3. Triage Heuristic / 선별 휴리스틱

This is a decision heuristic, not an empirical validation score. / 경험적 검증점수가 아닌 다음 작업 선정용 휴리스틱.

| Criterion | Weight |
|---|---:|
| Breaks D06 case-proxy limitation / D06 한계 타격 | 25 |
| Breaks E09 rank-compression limitation / E09 한계 타격 | 25 |
| Identity integrity; removes cross-specimen ambiguity / 식별 무결성 | 20 |
| Physical-outcome relevance / 물리 outcome 연결력 | 15 |
| Current public-source readiness / 현 공개소스 준비도 | 10 |
| Zero-cost reproducibility / 무비용 재현성 | 5 |
| **Total** | **100** |

## 4. Candidate Comparison / 후보 비교

| Candidate | D06 | E09 | Identity | Physical outcome | Source readiness | Cost | Total | Triage |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A. BP4 coupling magnitude → BP1 aggregate thermal/geometry | 5 | 22 | 4 | 10 | 10 | 5 | **56** | DEFER |
| B. Within-BP4 coupling temporal-information diagnostic only | 22 | 25 | 20 | 4 | 10 | 5 | **86** | FALLBACK |
| **B+. BP4 coupling temporal dynamics → same-BP4 confocal 3D topography** | **25** | **25** | **20** | **15** | **3** | **5** | **93** | **SELECT, SOURCE GATE FIRST** |
| C. Independent-condition expansion (e.g., AMB2025-07) | 25 | 10 | 15 | 15 | 2 | 5 | **72** | HOLD/SECONDARY |

### A — Magnitude-sensitive cross-BP aggregate / 크기 민감 cross-BP 집계

**Strength:** directly escapes E09's rank-only statistic.  
**Weakness:** remains the same seven nominal case families and retains BP1↔BP4 separate-specimen/process-vector mismatch. It therefore attacks E09 more than D06 and cannot provide true same-track evidence.  
**Disposition:** `DEFER`.

### B — Within-BP4 temporal-information diagnostic / BP4 내부 시간동역학 진단

**Strength:** preserves the full time-resolved coupling signal rather than one case median and can test whether coupling contains repeat-level variation beyond case labels. This directly targets D06's case-proxy concern while escaping E09's rank compression.  
**Weakness:** without an independent same-specimen physical endpoint, it can establish information structure but not physical utility.  
**Disposition:** `FALLBACK` if same-BP4 ex-situ outcome source cannot be qualified.

### B+ — Same-BP4 coupling dynamics ↔ confocal 3D topography / 동일 BP4 coupling 동역학 ↔ confocal 3D 형상

**Scientific leverage:** highest. Official NIST AMB2022-03 documentation states that coupling specimens were measured with laser scanning confocal microscopy, and specifically identifies BP4 as the single-track dynamic-coupling plate. The document states that complete 3D surface profiles were measured to extract steady-state height profiles, track-end mass accumulation/loss, chevron-feature shape, and related surface-topography information.

This relationship would simultaneously:
1. remove the BP1↔BP4 cross-specimen limitation;
2. preserve the coupling time-series rather than collapse it to a rank-preserving scalar;
3. permit true track/repeat-level same-specimen evidence if identifiers are available;
4. test a physically distinct ex-situ consequence rather than only information geometry.

**Current blocker:** current NIST direct-data guidance explicitly lists the AMB2022-03 thermography, optical microscopy, microstructure, and `mds2-3842` dynamic-coupling publications, but the exact public version-identifiable BP4 confocal/topography publication and deterministic track identifier map were not established in the triage search. The 2022 challenge document's statement that the data would be released is not sufficient by itself to infer present public availability.

**Disposition:** **`SELECT — SOURCE/IDENTITY FEASIBILITY FIRST`**.

### C — Independent process-condition expansion / 독립 공정조건 확대

**Strength:** strongest route to external condition independence and directly addresses D06 generalization.  
**Weakness:** the previously examined AMB2025-07 path remains source-limited because a version-identifiable public raw/analysis-ready thermography publication has not been established; it also does not directly exploit E09's already-qualified distinct coupling modality.  
**Disposition:** `HOLD_SECONDARY` pending source maturation or a different qualified independent-condition dataset.

## 5. Selected Next Work Queue / 선택된 다음 작업

**Selected:** `AMBENCH-F10 — BP4 coupling ↔ same-BP4 confocal topography source/identity feasibility`.

This is a **metadata/identity feasibility gate**, not a predictive experiment. / 예측실험이 아니라 source·identity feasibility gate.

The purpose is to determine whether the scientifically strongest B+ relationship is actually reproducible from authoritative public data before accessing confocal outcome values.

## 6. Fallback Rule / fallback 규칙

If F10 cannot establish an exact public version-identifiable BP4 confocal source with deterministic track identity:

1. do **not** substitute BP1 optical geometry or another plate as if same-specimen;
2. do **not** infer confocal values from publications/figures;
3. next eligible fallback is a separately preregistered **within-BP4 temporal-information diagnostic** testing repeat-vs-case variance, temporal effective dimension, and process association without claiming physical-outcome utility;
4. independent-condition expansion remains a later branch when source readiness improves.

## 7. Cost & Raw Data / 비용·raw data

- `COST-001`: zero incremental monetary cost only.
- `RAW-001`: if a later execution reaches raw files, external source bytes remain transient only.
- F10 itself should avoid numerical confocal outcome access; metadata, manifests, file inventories, checksums, identifier semantics, and variable dictionaries are allowed.

**Final triage decision / 최종 선별:** **`B+ SELECTED → AMBENCH-F10 SOURCE/IDENTITY FEASIBILITY`**.

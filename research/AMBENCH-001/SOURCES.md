# AMBENCH-001 Sources / 출처 레저

**Verified / 검증일:** 2026-08-21

## Primary Official Sources / 공식 1차 출처

1. **NIST AM Bench — Direct Data Links / 직접 데이터 링크**  
   https://www.nist.gov/ambench/direct-am-bench-data-links-and-referencing-guidance  
   Confirms the AMB2022-03 dataset family and DOI relationships. / AMB2022-03 데이터셋 계열과 DOI 관계 확인.

2. **AMB2022-03 Measurement & Challenge Description v1.01 / 측정·챌린지 설명**  
   https://www.nist.gov/document/amb2022-03-measurement-and-challenge-descriptions-version-101  
   Defines experiment design, seven process cases, three repeats, process parameters, measurements, and challenge targets. / 실험설계, 7개 공정 case, 3회 반복, 공정변수, 측정과 challenge target 정의.

3. **AMB2022-03 Measurement & Challenge Results v1.0 / 측정·챌린지 결과**  
   https://www.nist.gov/document/am-bench-amb2022-03-measurement-and-result-descriptions-v10  
   Provides TTAM, TSCR, TLCR, TTCR and melt-pool geometry result tables. / 열이력·cooling-rate 및 melt-pool geometry 결과표 제공.

4. **NIST PDR — In-situ Thermography / 열화상**  
   DOI: https://doi.org/10.18434/mds2-2716  
   PDR ID: `mds2-2716`  
   Role: thermography + scan strategy / 열화상 + scan strategy.

5. **NIST PDR — Optical Microscopy / 광학현미경**  
   DOI: https://doi.org/10.18434/mds2-2718  
   Landing page: https://data.nist.gov/od/id/mds2-2718  
   Data.gov: https://catalog.data.gov/dataset/am-bench-2022-measurement-results-data-optical-microscopy-of-laser-scanned-single-track-03  
   Role: cross-sectional optical images + measured melt-pool geometry / 단면 광학영상 + melt-pool geometry 측정.

6. **NIST PDR — Cross-sectional Microstructure / 단면 미세조직**  
   DOI: https://doi.org/10.18434/mds2-2775  
   Data.gov: https://catalog.data.gov/dataset/am-bench-2022-cross-sectional-microstructure-of-single-laser-tracks-produced-using-dif-718  
   Role: SEM/EBSD/EDS microstructure / SEM·EBSD·EDS 미세조직.

7. **NIST PDR — Dynamic Laser Coupling / 동적 레이저 결합**  
   https://data.nist.gov/od/id/mds2-3842

## Optical Dataset Distribution Evidence / 광학 데이터셋 배포 구조

`mds2-2718` exposes 209 resources through Data.gov/PDR, including: / Data.gov/PDR 기준 209개 리소스가 확인되며 다음을 포함한다.

- `2718_README.txt`
- `AMB2022-718-SH1-MeltPool_Cross-Section_Measurement_Results.xlsx`
- TIFF cross-sectional images / TIFF 단면 이미지
- `.sha256` integrity files / 무결성 파일

README-described image scale for cross-sectional optical micrographs is 0.069 µm/pixel, with original and measurement-annotated image variants. / README는 단면 광학영상 축척을 0.069 µm/pixel로 기술하며 원본과 측정표시 이미지 변형을 제공한다.

## Provenance Rule / 출처 규칙

NIST/PDR and official challenge documents are authoritative for benchmark interpretation. Data.gov is used as a catalog/distribution mirror and metadata discovery layer. Secondary mirrors are not used to override NIST definitions.  
Benchmark 해석은 NIST/PDR과 공식 challenge 문서를 기준으로 하며 Data.gov는 catalog/distribution metadata 탐색 레이어로 사용한다. 2차 미러는 NIST 정의를 대체하지 않는다.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.

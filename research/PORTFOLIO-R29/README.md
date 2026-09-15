---
id: PORTFOLIO-R29
type: mission-roi-portfolio-reselection
created: 2026-09-16
issue: 138
state: ACTIVE_RESELECTION
prior_terminal: US-UTIL-N01
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R29 — marginal-information reselection after terminal US-UTIL-N01

## Objective / 목적

Re-rank only the two surviving R28 alternatives after terminal US-MINE-N01 and US-UTIL-N01, using the established 9-dimension /45 Mission-ROI rubric and newly verified official source-access facts. / US-MINE-N01·US-UTIL-N01 종결 이후 남은 두 후보만 동일 /45 평가틀로 재선정한다.

Candidates:
- `US-PIPE-001` — hydrologic stress → pipeline incidents
- `C-EU-004` — industrial-site climate / physical-hazard join

No candidate outcome magnitude or relationship is opened in R29.

## Frozen score-update rule / 고정 점수변경 규칙

Carry forward R28 dimension scores unless new official-source/access evidence materially changes that dimension. The new source-access evidence may update only `Join defensibility` and/or `Next-gate information gain` unless equally direct evidence changes another dimension. Free account/API-key friction is not a monetary-cost penalty. Restricted geometry may not be replaced with case-only locations or an invented exposure denominator.

Tie-break, unchanged from R28:
1. Total score
2. Next-gate information gain
3. Low overlap / novelty risk
4. Direct outcome

## Official-source revalidation / 공식 source 재검증

### US-PIPE-001

PHMSA provides public incident ZIPs with field definitions and public annual-report pipeline mileage/facility data. However, NPMS pipeline GIS/PIMMA access is restricted to eligible government officials and pipeline operators; the general public does not receive unrestricted downloadable national line geometry. Public county mileage summaries exist, but they cannot be assumed to provide the historical line-resolved hydrologic exposure denominator required by the original concept.

Sources:
- https://www.phmsa.dot.gov/data-and-statistics/pipeline/distribution-transmission-gathering-lng-and-liquid-accident-and-incident-data
- https://www.phmsa.dot.gov/data-and-statistics/pipeline/pipeline-mileage-and-facilities
- https://www.npms.phmsa.dot.gov/PipelineData.aspx
- https://www.npms.phmsa.dot.gov/GeneralPublic

### C-EU-004

The EEA Industrial Emissions Portal provides a downloadable Industrial Reporting dataset containing site/facility location and administrative identities; the portal covers over 60,000 industrial sites across 65 activities. ERA5-Land remains a CC-BY source with hourly data from 1950-present. Programmatic ARCO access examples require a CDS API key, which is source-access friction but not paid-source evidence; a later F01 must establish a reproducible zero-cost route before promotion.

Sources:
- https://industry.eea.europa.eu/industrial-emissions/dataset
- https://industry.eea.europa.eu/industrial-emissions/about
- https://industry.eea.europa.eu/industrial-emissions/data-connectors/site-environmental-information
- https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land

## Prospective R29 scoring adjudication / 사전 점수판정

R28 baseline:
- US-PIPE-001 = 37/45, with Join defensibility 5 and Next-gate information gain 2.
- C-EU-004 = 36/45, with Join defensibility 5 and Next-gate information gain 3.

New official access evidence changes US-PIPE only:
- `Join defensibility: 5 → 3` because unrestricted national line geometry cannot be assumed and the public alternatives have not yet established a historical line-resolved hydrologic denominator.
- `Next-gate information gain: 2 → 3` because an outcome-blind access/denominator gate can now resolve whether public annual/county mileage support can salvage a defensible non-line-level unit without restricted GIS.

No R29 evidence changes the other seven US-PIPE dimensions or any C-EU dimension.

Therefore the prospective scores entering the mechanical tie-break are:
- US-PIPE-001: **36/45**
- C-EU-004: **36/45**

The result must be finalized mechanically under the frozen tie-break; no score may be changed to force a winner.

## Exact next action / 정확한 다음 행동

Apply the frozen tie-break to the two 36/45 candidates, persist exactly one winner, close R29, and open only that winner's separate outcome-blind source/access/identity feasibility gate. No effect test is authorized.

Incremental monetary cost remains **0 USD**.

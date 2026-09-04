---
id: WAVE3-GEO-D01
type: geographic-relationship-discovery
state: ACTIVE
created: 2026-09-04
issue: 82
portfolio_decision: DEC-113
mission_anchor: MEM-054
incremental_monetary_cost_usd: 0
---

# WAVE3-GEO-D01 — Canada / Australia / OECD-World Bank Relationship Candidate Discovery
# WAVE3-GEO-D01 — 캐나다 / 호주 / OECD-World Bank 관계 후보 탐색

## 1. Purpose / 목적

Expand the innovation-discovery surface after a validated Japan port-weather result.

D01 must identify **new cross-dataset relationships**, not merely more datasets.

Target pattern:

`official source A + official source B → direct outcome / bottleneck question → bounded F01`

## 2. Scope / 범위

### Canada
Candidate source families:
- Open Government CKAN;
- Statistics Canada Web Data Service;
- Natural Resources Canada, Transport Canada, Environment and Climate Change Canada, CER or other official domain sources when needed.

### Australia
Candidate source families:
- data.gov.au;
- ABS;
- AEMO / energy and grid sources;
- Bureau of Meteorology / climate;
- infrastructure, ports, freight, resources or industrial sources.

### Cross-national
Candidate source families:
- OECD Data Explorer / SDMX;
- World Bank Indicators API;
- national official sources.

Cross-national sources are useful only when they add harmonization or a meaningful comparator to a concrete bottleneck construct.

## 3. Fixed discovery criteria / 고정 탐색 기준

Score candidates 0–5 on:
- mission bottleneck value;
- cross-source relationship value;
- directness of outcome;
- independent-unit quality;
- practical intervention/decision value;
- current official-source access;
- join/mapping defensibility;
- expected F01 information gain;
- low diminishing-return risk.

## 4. Minimum source rules / 최소 소스 규칙

- official first-party government/institution source;
- current machine-readable or reproducibly downloadable route;
- no commercial database;
- no opaque dashboard scraping;
- no credential creation merely for convenience;
- no bulk catalog harvesting.

## 5. Candidate contract / 후보 계약

Every shortlisted candidate must document:
- source names and exact URLs;
- grain;
- time coverage;
- key identifiers;
- likely independent unit;
- direct outcome;
- known revision/missingness/access limitations;
- exact next F01 uncertainty.

## 6. Selection / 선정

Select at most one candidate.

If none clearly beats preserved alternatives, output:
**`NO_WAVE3_PROMOTION`**
and return to Stage 0.

## 7. Exposure boundary / 노출 경계

D01 may inspect:
- metadata;
- schemas;
- very small bounded samples where necessary;
- source documentation.

D01 shall not:
- fit regressions;
- calculate relationship strength;
- select candidates by observed effect size;
- build production pipelines.

## 8. Cost / 비용

Incremental monetary cost remains **0 USD**.

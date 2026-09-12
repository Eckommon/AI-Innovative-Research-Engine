---
id: US-WW-N01-LITERATURE-OVERLAP
type: current-literature-overlap-adjudication
created: 2026-09-13
issue: 116
disposition: ADJACENT_NOT_NEAR_IDENTICAL
future_outcome_magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# US-WW-N01 Literature Overlap Adjudication

## Material adjacent prior work

A current literature search identified Hanyi (Livia) Yi, **Financing Public Goods** (2021 working paper; presented at the 2022 American Economic Association meeting). The study uses municipal wastewater NPDES violations during 2005–2018, merges the NPDES database with EPA Clean Watersheds Needs Survey data, and uses CWNS infrastructure-upgrade need / upgrade-cost measures to test heterogeneity in the effect of a municipal-credit-supply shock on annual pollutant violations.

Primary sources checked:
- AEA 2022 preliminary paper: https://www.aeaweb.org/conference/2022/preliminary/paper/TB5F79s4
- Current author research page, where `Financing Public Goods` remains listed as a working paper: https://www.livia-yi.com/research.html
- Current author PDF: https://www.livia-yi.com/uploads/1/3/4/0/134097791/yi_financingpublicgoods.pdf

This prior work means the project must **not** claim that merging CWNS infrastructure information with NPDES violation data is itself novel.

## Why the proposed bounded design is not near-identical

The N01 descendant is materially different in its estimand and temporal construction:

- baseline survey is specifically **2022 CWNS**;
- exposure is the prospectively fixed structural need-profile identity `III-A / III-B / V`, not a generic upgrade/cost indicator;
- the analysis unit is a CWNS facility with **all officially linked NPDES permits traveling together**;
- pre-existing compliance is handled using a frozen **2019–2021 baseline-clean rule**;
- explicit permit/TMDL-driven CWNS reasons are frozen as a **leakage stratum** before future outcomes;
- the future endpoint is a first recorded PS/CS/SE incident identity in a fixed **2023–2025** window;
- the claim boundary is non-causal predictive stratification, not the causal effect of municipal credit supply.

A 2026 Water Science & Technology study also combines ICIS-NPDES and CWNS to build a national wastewater treatment lagoon inventory and analyze effluent nutrient performance, confirming that the data-family combination itself is established. It does not implement the bounded incident-compliance prediction design above.

Source: https://doi.org/10.2166/wst.2026.261

## N01 novelty disposition

**`ADJACENT_NOT_NEAR_IDENTICAL`**

The branch retains bounded novelty sufficient for a design-identifiability PASS, but future claims must explicitly acknowledge the Yi working paper and related CWNS×ICIS integrations. Novelty is limited to the preregistered structural-need-profile → post-baseline incident-compliance predictive framing with leakage control; it is not a claim of first use of these datasets together.

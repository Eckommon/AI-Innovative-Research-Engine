---
id: PORTFOLIO-R44-RESULT
type: stage0-portfolio-selection
created: 2026-09-29
issue: 174
state: COMPLETED_SELECTED
selection: SELECT_EU_EMA_MA_001_MEDICINE_STRUCTURE_TO_AUTHORISATION_WITHDRAWAL_SUSPENSION_F01
scorecard_commit: 8073c1bc62cd3aff02ce0c6ef860784a1d4d37b9
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R44 Result / 결과

**`SELECT_EU_EMA_MA_001_MEDICINE_STRUCTURE_TO_AUTHORISATION_WITHDRAWAL_SUSPENSION_F01`**

R44 executed the four-candidate universe frozen before Issue binding at `79d9417e186948cae224bdc43dc745436628a707`, bounded source/internal-history/framework revalidation at `8f4919e209bc04e625a10057d6bd4ec16699e5ee`, and the single immutable scorecard at `8073c1bc62cd3aff02ce0c6ef860784a1d4d37b9`.

## Immutable ranking / 불변 순위

| Candidate | Score /45 | Terminal portfolio disposition |
|---|---:|---|
| `EU-EMA-MA-001` | **40** | **SELECT_F01** |
| `US-FERC-HYDRO-001` | **37** | HOLD_EVENT_SOURCE_NOT_YET_ESTABLISHED |
| `AU-ACNC-CHARITY-001` | **35** | HOLD_NONPROFIT_OVERLAP_AND_TAUTOLOGY_RISK |
| `UK-IPO-TM-001` | **31** | HOLD_BULK_STATUS_LINEAGE_NOT_ESTABLISHED |

No tie-break was required.

## Why EMA / EMA 선정 이유

EMA has the strongest combination of exact source-native product identity, public downloadable medicine data, direct authorisation/withdrawal dates, public event reasons and high next-gate falsifiability.

The selection does **not** treat all authorisation withdrawals as equivalent. Commercial/voluntary withdrawal, safety/regulatory withdrawal, suspension, expiry and withdrawn applications must remain separate.

## Authorized next work / 허가되는 다음 작업

Exactly one separate outcome-blind `EU-EMA-MA-F01` contract may be frozen next. Before any future withdrawal/suspension membership is opened, it must test:

1. official downloadable medicine-data access and source fingerprinting;
2. exact EMA product-number syntax and support;
3. human centrally authorised medicine population;
4. authorisation/status date semantics;
5. deterministic withdrawal/suspension reason/date semantics;
6. historical event support and event-class separation;
7. future-event membership firewall;
8. zero incremental monetary cost.

If current public sources cannot deterministically distinguish voluntary/commercial withdrawal from safety/regulatory action, suspension, expiry and application withdrawal, F01 must HOLD rather than collapse heterogeneous events.

## Non-claims / 비주장

R44 establishes no medicine-withdrawal relationship, hydropower-licence termination relationship, charity-revocation relationship, trade-mark adverse-status relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost: **0 USD**.

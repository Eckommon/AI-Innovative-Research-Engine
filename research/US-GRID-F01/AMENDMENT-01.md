---
id: US-GRID-F01-AMENDMENT-01
type: outcome-blind-harness-amendment
created: 2026-09-04
issue: 77
relationship_outcome_computed: false
scientific_contract_changed: false
incremental_monetary_cost_usd: 0
---

# US-GRID-F01 Amendment 01 — Use Source-Defined `entity` Identity and Composite Project Key
# US-GRID-F01 보정 01 — Source-defined `entity` 식별자 및 복합 project key 사용

## Trigger / 보정 사유

The initial source-semantic parser successfully froze the exact LBNL workbook and exposed the official codebook, but its generic header detector selected `region` and `utility` while failing to include the more authoritative codebook field:

- `entity` — **transmission provider entity name (ISO or utility)**;
- codebook note — **one of the 57 regions listed on the `01. Balancing Areas` sheet**.

The same codebook states:

- `q_id` — queue position / ID number;
- **combine with `entity` to form a unique identifier across the full dataset**.

Therefore the initial `395`-identity / `4.3%` conservative matching diagnostic is not the correct scientific identity test. It mixed `region` and `utility` vocabularies and also attempted a generic single-column project-ID diagnostic.

The initial EIA-861 parser also detected headers `BA ID`, `BA Code`, and `Balancing Authority Name`, but its generic code-column selector required the word `balancing` and therefore failed to load the explicit `BA Code` field.

## Frozen correction / 고정 보정

Rerun source-semantic identity qualification with exactly these corrections:

1. primary LBNL operator identity = **`entity`** only;
2. LBNL project identity = **`entity + q_id`**;
3. inspect the complete source-defined `01. Balancing Areas` sheet as identity metadata;
4. EIA identity columns = explicit **`BA ID`, `BA Code`, `Balancing Authority Name`**;
5. compare LBNL `entity` against EIA BA name/code using normalized exact matching first;
6. any non-exact aliases may be admitted only when directly supported by source-defined names/abbreviations or another official one-to-one identity source;
7. no fuzzy similarity, state overlap, service-territory inference, or queue/EIA relationship outcomes may be used to choose aliases.

## Scientific contract / 과학 계약

Unchanged:
- selected branch;
- selected source families;
- exposure boundary;
- priority direct outcome (`IR→COD` if source-defined);
- PASS/PARTIAL/HOLD/REJECT definitions;
- no EIA operating-value relationship analysis during F01.

This is a parser/identity-field correction required by the source's own codebook, not a post-outcome scientific redesign.

Incremental monetary cost remains **0 USD**.

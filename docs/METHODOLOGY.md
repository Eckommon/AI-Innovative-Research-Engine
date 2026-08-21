# Innovation Discovery Methodology

## 1. Objective

The engine converts public/research data into testable innovation candidates through a controlled evidence pipeline.

The research target is not merely a useful dataset. The higher-value target is a **relationship between datasets** that supports a new prediction, optimization, stress-test, benchmark, decision tool, or industrial insight.

## 2. Official Pipeline

### Stage 1 — Source Discovery
Identify authoritative data publishers and catalogs by country, region, agency, and domain.

Minimum source record:
- source name;
- jurisdiction;
- agency/operator;
- URL;
- access mode/API;
- metadata standard where known;
- license/reuse notes;
- priority domains.

### Stage 2 — Metadata Harvesting
Capture dataset-level metadata sufficient for triage and reproducibility.

Recommended fields:
- dataset title and identifier;
- publisher;
- description;
- temporal/spatial coverage;
- update frequency;
- format/distribution;
- API/download endpoint;
- license/rights;
- schema/documentation;
- quality statement;
- candidate join keys;
- likely target/outcome variables.

### Stage 3 — Dataset Triage
Score datasets using `registry/INNOVATION_POTENTIAL_SCORE.md`.

Important: a low-scoring dataset may still become highly valuable in combination with another dataset. Therefore keep separate:
- `Dataset Score`;
- `Combination Score`;
- `Project Score`.

### Stage 4 — Relationship Discovery
Search for joinable relationships across datasets.

Relationship dimensions include:
- entity/facility/company;
- geography;
- timestamp/period;
- industry classification;
- product/material;
- infrastructure asset;
- physical measurement;
- event identifier;
- policy/regulatory regime.

Every proposed join should document semantic compatibility, not only matching field names.

### Stage 5 — Hypothesis Generation
Generate a falsifiable claim from the relationship.

Template:

```text
Given [datasets/evidence],
we hypothesize that [relationship/mechanism]
can predict/optimize/explain [target]
under [scope/conditions],
measured by [metric/validation criterion].
```

### Stage 6 — Feasibility Test
Before a full experiment, verify:
- data can actually be accessed;
- schema is usable;
- join keys are valid;
- temporal/spatial alignment is adequate;
- missingness and sample size are acceptable;
- target leakage is controlled;
- licensing permits intended use;
- a baseline can be defined.

### Stage 7 — Controlled Experiment
The experiment design should predefine:
- target variable;
- baseline;
- train/test or equivalent evaluation split;
- primary metric(s);
- sensitivity checks;
- rejection criteria;
- reproducibility steps.

Possible experiment classes:
- prediction;
- classification;
- anomaly detection;
- optimization;
- causal/quasi-causal analysis;
- simulation/digital twin;
- stress testing;
- ranking/index construction;
- computer vision / signal analysis;
- benchmark construction.

### Stage 8 — Innovation Registry
Record the outcome even when the hypothesis fails.

Minimum result fields:
- research ID;
- datasets used;
- hypothesis;
- experiment design;
- result;
- evidence class;
- limitations;
- practical utility;
- novelty assessment;
- next action;
- final state (`VALIDATED`, `REJECTED`, `INCONCLUSIVE`, `HOLD`).

## 3. NIST AM Bench as Reference Pattern

NIST AM Bench is retained as the methodological benchmark because it illustrates a strong research structure:

```text
process conditions
  → physical experiment/manufacturing
  → measurement / imaging
  → material or geometry outcome
  → benchmark / ground truth
```

This supports explicit mappings such as:

```text
X_process + X_measurement → Y_quality
```

The engine should preferentially identify public datasets with similarly strong input/measurement/outcome structures, while also allowing cross-dataset construction of such a structure when no single dataset contains it.

## 4. Evidence and Novelty Separation

A project can be:
- empirically strong but not novel;
- novel but weakly evidenced;
- operationally useful without being scientifically novel;
- statistically significant but commercially irrelevant.

Therefore final evaluation should separately assess:
1. evidence strength;
2. reproducibility;
3. novelty;
4. practical utility;
5. scalability;
6. implementation cost/risk.

## 5. Cross-National Research Rule

Cross-national analysis must not assume field equivalence merely because labels appear similar. It should explicitly check:
- classification systems;
- units;
- inflation/currency treatment;
- time zones and periods;
- spatial granularity;
- methodology changes;
- sampling/coverage differences;
- missing or censored observations.

## 6. Promotion Gates

A candidate advances only when the previous gate is satisfied:

```text
DISCOVERED
→ SCREENING
→ CANDIDATE
→ FEASIBILITY_TEST
→ EXPERIMENT
→ VALIDATED / REJECTED / INCONCLUSIVE / HOLD
```

No candidate is promoted solely because an AI-generated idea sounds plausible.

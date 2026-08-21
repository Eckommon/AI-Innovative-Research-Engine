# AMBENCH-001 — NIST AM Bench Methodological Benchmark

**Research ID:** `AMBENCH-001`  
**State:** `ACTIVE_BENCHMARK`  
**Wave:** 0  
**Purpose:** calibrate the research engine before cross-country expansion.

## Why This Case Matters

NIST AM Bench is used as the first methodological benchmark because the research structure can connect manufacturing/process conditions with measured physical outcomes and benchmark/ground-truth-oriented evaluation.

Conceptual structure:

```text
Process Conditions
    ↓
Physical Manufacturing / Experiment
    ↓
Measurement / Imaging
    ↓
Material / Geometry Outcome
    ↓
Benchmark / Ground Truth
```

This supports testable mappings such as:

```text
X_process + X_measurement → Y_quality
```

## Primary Source Entry

- NIST AM Bench: https://www.nist.gov/ambench
- NIST/Data.gov example previously identified in project research: https://catalog.data.gov/dataset/am-bench-2022-measurement-results-data-optical-microscopy-of-laser-scanned-single-track-03

## Current Evidence State

### OBSERVED

- AM Bench is being used as the project's initial public/research-data benchmark case.
- The identified dataset concerns AM Bench 2022 measurement results and optical microscopy associated with laser-scanned single-track additive manufacturing work.

### HYPOTHESIZED

Potential innovation classes include:

- process-to-quality prediction;
- image/measurement-based defect or geometry inference;
- multimodal fusion of process parameters and microscopy/measurement outputs;
- benchmark construction for uncertainty-aware manufacturing models;
- transfer of the same discovery methodology to other advanced-manufacturing datasets.

These are hypotheses/candidate directions and are not yet recorded as validated project results.

## Calibration Tasks

- [ ] Retrieve and record complete source metadata.
- [ ] Inspect dataset files/distributions and schema.
- [ ] Identify process variables, measurement variables, and outcome/ground-truth variables.
- [ ] Document candidate join keys across related AM Bench datasets.
- [ ] Calculate Dataset IPS with written justification for every criterion.
- [ ] Generate candidate Combination IPS records for related AM Bench datasets.
- [ ] Select at least one falsifiable hypothesis.
- [ ] Define baseline, validation metric, and rejection criterion before modeling.
- [ ] Run feasibility test.
- [ ] Record outcome as `VALIDATED`, `REJECTED`, `INCONCLUSIVE`, or `HOLD`.

## Role in the Larger Engine

AMBENCH-001 is not treated as the final product. It is the calibration case used to answer:

1. What metadata must the engine retain?
2. Which scoring dimensions distinguish research-grade data from ordinary public tables?
3. How should dataset relationships and joins be represented?
4. What evidence is required before an AI-generated hypothesis advances to experiment?
5. Which parts of the workflow can safely be automated in Wave 1?

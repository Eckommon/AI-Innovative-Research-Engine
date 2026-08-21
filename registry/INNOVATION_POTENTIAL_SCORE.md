# Innovation Potential Score (IPS) v0.1

This rubric is used to triage individual datasets and, with adaptation, dataset combinations/projects.

## Scoring

| Criterion | Max |
|---|---:|
| Industrial / societal problem importance | 15 |
| Raw-data granularity | 10 |
| Temporal / spatial resolution | 10 |
| Ground truth / outcome availability | 15 |
| Joinability with other datasets | 15 |
| AI / ML applicability | 10 |
| Experimental / validation feasibility | 10 |
| API / machine readability | 5 |
| License / reusability | 5 |
| Underexplored / novelty potential | 5 |
| **Total** | **100** |

## Suggested Bands

- **85–100: Priority A** — strong candidate for direct feasibility testing.
- **70–84: Priority B** — promising; inspect joins and target definition.
- **55–69: Priority C** — useful supporting dataset or domain context.
- **Below 55: Priority D** — archive unless a high-value combination changes its role.

## Mandatory Notes

A numeric score alone is insufficient. Every scored item should record:

- why the score was assigned;
- unknowns that may change the score;
- likely target/outcome variable;
- candidate joins;
- evidence limitations;
- next validation action.

## Separate Scores

Do not mix these three concepts:

1. **Dataset IPS** — intrinsic research potential of one dataset.
2. **Combination IPS** — value created by joining multiple datasets.
3. **Project IPS** — full hypothesis, feasibility, novelty, and practical-use potential.

A low Dataset IPS may participate in a high Combination IPS.

## Calibration Rule

NIST AM Bench is used as an initial high-quality calibration case because it includes experimental conditions, measurements, outcomes/ground truth, and benchmark-oriented structure. Its exact numeric score should only be finalized after a documented field-by-field assessment; it must not be assigned a high score by reputation alone.

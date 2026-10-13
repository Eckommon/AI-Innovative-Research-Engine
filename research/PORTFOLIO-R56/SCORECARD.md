---
id: PORTFOLIO-R56-SCORECARD
type: immutable-stage0-scorecard
created: 2026-10-13
issue: 200
contract: 0144ed638e671029eeea288eb91402591b2c5a30
revalidation: 22353335058ce82e8fc0cf1ff956a0e6ded54e94
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R56 — immutable /45 scorecard

| Dimension | US-CMS-NPI-002 | US-FAA-AIR-002 | US-PHMSA-PIPE-002 | US-FCC-ULS-002 |
|---|---:|---:|---:|---:|
| 1. Mission bottleneck fit | 4 | 4 | 5 | 3 |
| 2. Cross-table information gain | 5 | 4 | 5 | 4 |
| 3. Direct future-event quality | 4 | 4 | 5 | 3 |
| 4. Independent-unit prospect | 5 | 5 | 4 | 5 |
| 5. Practical decision value | 4 | 4 | 5 | 3 |
| 6. Zero-cost operability | 5 | 5 | 5 | 5 |
| 7. Deterministic identity | 5 | 3 | 5 | 4 |
| 8. N01 survivor probability | 5 | 4 | 3 | 4 |
| 9. Low overlap / novelty risk | 4 | 5 | 4 | 2 |
| **Total /45** | **41** | **38** | **41** | **33** |

## Frozen tie-break

CMS NPI and PHMSA tie at **41/45**.

Apply the frozen tie-break in order:

1. **N01 survivor probability** — CMS 5 > PHMSA 3.
2. No further tie-break required.

## Frozen selection

**`SELECT_US_CMS_NPI_002_ACTIVE_TYPE2_STRUCTURE_TO_FUTURE_NPI_DEACTIVATION_F01`**

## Rationale

CMS wins the tie because R56 was explicitly created after an N01 support failure. The monthly national full replacement plus separate deactivation update and weekly incremental files create a much larger likely eligible universe and denser future event opportunity than operator-level PHMSA incidents.

This selection does not interpret deactivation as provider closure or quality failure. The event remains exactly the source-native administrative NPI deactivation state.

## Authorized next gate

Exactly one separate outcome-blind `US-CMS-NPI-F01` may be frozen. It must establish:

- direct official Version-2 full/deactivation file access;
- exact 10-digit NPI identity;
- Type-2 active organization cohort support;
- taxonomy and practice-location structural joins;
- source-native deactivation/reactivation semantics;
- historical deactivation-date support;
- update cadence/fingerprint reproducibility;
- a future-update firewall;
- no deactivation/reactivation/history field in structural exposure;
- cost 0.

Incremental monetary cost: **0 USD**.

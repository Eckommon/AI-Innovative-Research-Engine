# US-BRIDGE-E01 — preregistered disaster × bridge-condition matched-pair outcome test

Issue: #132
Cost boundary: **0 USD incremental monetary cost**

## Authorization boundary

E01 is the single prospective outcome test authorized after US-BRIDGE-N01 reached `PASS_US_BRIDGE_N01_MATCHED_INTERVAL_DESIGN_IDENTIFIABLE`.

Before any condition byte is sliced or decoded, the runner MUST reproduce and verify:

- `research/US-BRIDGE-N01/PAIR_IDENTITIES.jsonl.gz`
- pair count **89,800**
- pair identity SHA-256 `a35d38c8219de527a72c5d4975c6f6c2fed63e92711632fd5adc4b16056269b9`
- compressed artifact SHA-256 `4de3b8cbc7152725f72e4a93a0990a26e92579607cca8ecfe3390eba5d69e6e3`
- **15,245 CULVERT** and **74,555 NON_CULVERT** pairs

Any mismatch terminates E01 before outcome access.

## Frozen outcome

### CULVERT

Use NBI Item 62 only. Both pre/post values must be numeric `0–9`. `deterioration=1` iff `post <= pre - 1`.

### NON_CULVERT

Use NBI Items 58/59/60 only. Retain components numeric `0–9` at both endpoints; use the same common component set at pre and post; require at least 2 common numeric components; endpoint score is the minimum across that common set. `deterioration=1` iff `post_score <= pre_score - 1`.

A matched pair enters the primary test only if both exposed and control intervals are analyzable.

## Frozen estimand/test

- exposed deterioration risk
- control deterioration risk
- `RD = exposed risk - control risk`
- paired 2×2 counts
- exact two-sided McNemar/binomial test on discordant pairs
- significance: `p < 0.05`
- positive materiality: `RD >= +0.05`

## Frozen dispositions

- `PASS_POSITIVE_MATERIAL_US_BRIDGE_E01_RELATIONSHIP` iff `RD >= +0.05` and `p < 0.05`
- `POSITIVE_BELOW_MATERIALITY_US_BRIDGE_E01_RELATIONSHIP` iff `0 < RD < +0.05` and `p < 0.05`
- `NO_PREREGISTERED_POSITIVE_US_BRIDGE_E01_RELATIONSHIP` otherwise
- support/identity drift: fail-closed HOLD

A negative RD does not authorize a protective interpretation. No alternative outcome, score, threshold, subgroup, asymptotic test, one-sided test, model, or post-value rescue is authorized.

## Interpretation boundary

Even a positive result is a non-causal association under the frozen matched design. County exposure error, event severity, inspection ascertainment, maintenance/repair, aging, traffic/environment and unobserved interventions remain limitations.

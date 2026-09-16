---
id: US-FMCSA-HAZ-F01-SUPERSEDED-35045639924
type: implementation-nonconformity
created: 2026-09-16
issue: 145
run: 35045639924
disposition: EXECUTION_INVALID_FOR_GATE
scientific_disposition: none
contract_changed: false
threshold_changed: false
outcome_opened: false
---

# Superseded Run 35045639924 — implementation invalid, no scientific disposition

Run `35045639924` successfully passed the frozen-contract verifier, executed the source runner, verified the outcome-blind boundary, and durably committed staging evidence. It then failed at `Require valid gate evaluation` because staging correctly returned:

`IMPLEMENTATION_OR_SOURCE_PARSE_NOT_VALID_FOR_GATE`.

This run is **not** a HOLD, PARTIAL or PASS.

## Implementation defect 1 — FMCSA carrier-field alias

The official `fx4q-ay7w` schema was reached successfully (`63` columns) and the official `876r-jsdb` schema was reached successfully (`14` columns). The runner mapped:

- inspection identity → `inspection_id`
- inspection date → `insp_date`
- violation inspection identity → `inspection_id`
- violation OOS → `out_of_service_indicator`

but failed to map the inspection carrier field because the current official source uses **`dot_number`** while the implementation alias list recognized `usdot_*` forms only.

The preregistered scientific identity remains unchanged: source-native FMCSA USDOT Number. Adding `dot_number` as an implementation alias does not change the source, identity rule, threshold or analysis.

## Implementation defect 2 — access-only PARTIAL control flow

The first implementation incorrectly required the PHMSA Oracle search page itself to be reachable in order to classify PHMSA source semantics as ready. That conflicts with the preregistered access-only PARTIAL, whose purpose is precisely to distinguish:

- official PHMSA metadata/dictionary/public-export semantics being documented, from
- the current Oracle detailed export being unavailable to the zero-cost programmatic runner.

In Run `35045639924`:

- official PHMSA Data.gov catalog: HTTP 200;
- official PHMSA Data Dictionary PDF: HTTP 200;
- catalog text documented public export-to-text semantics;
- Oracle search route: `URLError`;
- no export candidate was discovered;
- no bypass or unofficial mirror was used.

The corrected implementation therefore treats official Data.gov catalog + official PHMSA dictionary as the documentation/semantics requirement and treats Oracle search/export non-retrieval only as the prospective export-access question. It does **not** relax any PHMSA byte-dependent PASS requirement.

Similarly, FMCSA Data.gov catalog/schema are the authoritative machine-readable metadata required for F01; a bot-blocked FMCSA prose page (HTTP 403) remains in the source audit but does not erase the official Data.gov metadata that is successfully reachable.

## Boundary preserved

- hazmat incident occurrence by inspection profile: unopened
- future incident membership conditioned on FMCSA: unopened
- carrier-level joined membership persisted: false
- relationship/predictive metric/causal claim: false
- unofficial mirror/authentication bypass: false
- incremental monetary cost: 0 USD

## Correction authorized

Correct only:
1. add the observed native `dot_number` alias for the preregistered FMCSA USDOT identity;
2. align documentation-vs-export access control flow with the already-frozen access-only PARTIAL rule;
3. allow a rerun only after this invalid run is durably preserved.

No source switch, threshold change, outcome access or post-hoc scientific redesign is authorized.

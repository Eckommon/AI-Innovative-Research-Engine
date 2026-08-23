# AMBENCH-E27 Amendment 02 — Schema-preflight emission incident + bounded parser correction
# AMBENCH-E27 Amendment 02 — Schema 사전검증 노출 사고 + bounded parser 보정

## Trigger / 발생

The Amendment-01 workflow tried BOM-less `utf-16` before ASCII-compatible fallback encodings. Because Python can decode many arbitrary even-length byte strings as UTF-16 without throwing, the parser accepted an invalid interpretation of the frozen primary CSV. The resulting malformed pseudo-header incorporated numerical data cells and was committed by the workflow.

## Exposure correction / 노출 정정

The previous front matter incorrectly claimed `numerical_outcome_values_emitted: false`. That claim is superseded.

Permanent exposure state:

**`NEW_E27_NUMERICAL_OUTCOME_BLIND = VIOLATED_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`**

No condition-level mapping/comparison, six-plate statistic, permutation test, rank-biserial statistic, feature selection, endpoint switching, or model had been performed when the incident occurred. E27's scientific design was already frozen in `README.md` / `DEC-056` and may not be changed in response.

## Current-tip remediation / 현재 tip 보정

`SCHEMA_PREFLIGHT.md` is replaced on the current branch with a numerical-value-free incident state. The historical bot commit is not rewritten because public-history rewriting is destructive and outside authorized scope.

## Frozen parser correction / 고정 parser 보정

For the next schema-only preflight:

1. `UTF-16` is permitted **only** when the byte stream begins with a UTF-16 BOM (`FF FE` or `FE FF`).
2. UTF-8 BOM => `utf-8-sig`.
3. Without BOM, fixed attempt order = `utf-8-sig` → `cp1252` → `latin-1`.
4. A decoding candidate is accepted only if:
   - the first record has at least 2 comma-delimited fields;
   - header cells have a bounded printable-character ratio;
   - the header contains expected non-numeric schema tokens relevant to the published summary structure (e.g. `Turnaround`, `Pad`, `Location`, or equivalent literal text observed only as schema labels).
5. Preflight output may emit only:
   - selected encoding;
   - bounded header field names (each capped in length);
   - row count;
   - identifier-presence/count booleans;
   - source size/SHA status.
6. Preflight output must never emit raw data rows, malformed whole lines, or numerical outcome cells.
7. If the frozen summary component does not deterministically identify all six physical plates at P1, E27 resolves to `HOLD_E27_SOURCE_OR_SCHEMA_INTEGRITY`. No source/endpoint substitution is allowed inside E27.

## Scientific invariants / 과학적 불변사항
Unchanged:
- six physical plates / 3 vs 3;
- P1 5 mm pad at x=0.460 mm;
- primary average overlap depth;
- sensitivity average depth;
- one-sided exact 20-allocation label-permutation reference;
- frozen PASS/HOLD/REJECT gates.

## Cost / 비용
Incremental monetary cost: `0 USD`. No paid/potentially paid route is authorized by this amendment.
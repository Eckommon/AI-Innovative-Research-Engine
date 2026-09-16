# Superseded Run 35057504925 — implementation classification defect

Run `35057504925` successfully reached the official FMCSA/PHMSA source gate and corrected the earlier native `dot_number` alias defect. It is **not** accepted as the scientific/source disposition for US-FMCSA-HAZ-F01.

## Defect

The official FMCSA Vehicle Inspection File schema exposes `insp_date` as Socrata type `text`. The inherited `date_support()` implementation only extracts years when Socrata metadata reports a native date/calendar/timestamp type. For a text field it counted non-null values, producing `date_parse_rate = 1.0`, but performed no parsing and returned `distinct_date_years = 0`.

The frozen contract requires actual date parseability >=95% and >=3 supported years. Therefore treating the unparsed text field as a frozen date-support failure would conflate an implementation limitation with a source/schema failure.

## Preservation / 비적합 보존

- observed FMCSA source remains `fx4q-ay7w`;
- observed field remains native `insp_date`;
- source identity, exact USDOT rule, thresholds, outcome boundary and cost boundary are unchanged;
- no PHMSA incident membership, relationship, prediction or causal quantity was opened;
- the Run `35057504925` staging is retained in Git history as evidence of the defect;
- the next correction may only add deterministic parsing of the same native `insp_date` values and weighted support counting. It may not change the source, threshold or cohort.

Classification: **`EXECUTION_VALID_BUT_DATE_SUPPORT_CLASSIFICATION_INVALID_FOR_TERMINAL_GATE`**.

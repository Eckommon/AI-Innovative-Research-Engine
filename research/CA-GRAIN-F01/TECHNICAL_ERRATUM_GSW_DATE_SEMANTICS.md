# Technical Erratum — GSW date semantics / 기술 정정

Applies to **CA-GRAIN-F01**. Terminal gate remains **`PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE`**.

The original F01 corrected probe still used a fixed slash-date parser for GSW `week_ending_date`; later E02 targeted provenance showed that raw slash strings cannot safely be treated with one locale convention across the frozen files. Therefore the earlier F01 raw-date-derived figure of **81 common weekly keys is superseded and must not be cited**.

Value-blind technical revalidation Run `34690978853` uses the official CGC `grain_week` schedule identity and finds **103 common official week keys** with both frozen TC carriers, above the preregistered F01 threshold of 80. Source access, two-carrier identity, and no-value boundary remain unchanged. F01 PASS therefore remains valid.

This erratum does not authorize any relationship test or alter E02. Cost: **0 USD**.

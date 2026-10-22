"""Synthetic Q06 no-outcome scope/region tests, no network."""
import unittest
import json
import hashlib
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock
from tools import qualify_source_census_usda_q06 as q

C={b"01001",b"72001"}
A={b"60010",b"60020",b"60030",b"60040",b"60050",
   b"66010",b"69010",b"69020",b"69030",b"69040",
   b"78010",b"78020",b"78030"}
def counters(c,u):
    return dict(census_2024_unique_5digit_geoid=len(c),
      usda_2023_unique_5digit_fips=len(u),
      distinct_key_overlap=len(c&u),
      usda_keys_not_present_in_2024_census=len(u-c),
      census_keys_not_present_in_usda=len(c-u),
      distinct_state_prefixes_in_overlap=len({x[:2] for x in c&u}),
      usda_duplicate_fips_rows=3,
      invalid_census_key_rows=0,invalid_usda_key_rows=0,census_duplicate_key_rows=0)
def probe(c,u):
    with mock.patch.object(q,"REQUIRED_Q05",counters(c,u)):
        return q.aggregate_scope(c,u,dict(invalid_census_key_rows=0,census_duplicate_key_rows=0),
                                   dict(invalid_usda_key_rows=0,usda_duplicate_fips_rows=3))

class Q06Tests(unittest.TestCase):
    def test_01_exact_four_territory_codes(self):
        self.assertEqual(set(q.ISLAND_PREFIXES),{b"60",b"66",b"69",b"78"})
    def test_02_puerto_rico_included(self):
        self.assertNotIn(b"72",q.ISLAND_PREFIXES)
    def test_03_full_thirteen_are_excluded_scope(self):
        s,d=probe(C,C|A)
        self.assertEqual(d,q.PASS)
        self.assertEqual(s["excluded_island_area_prefix_count_total"],13)
        self.assertEqual(s["nonexcluded_usda_only_fips_count"],0)
    def test_04_group_counts_only(self):
        s,d=probe(C,C|A)
        self.assertEqual(sum(s["prospectively_documented_island_area_prefix_totals"].values()),13)
        self.assertNotIn("60010",json.dumps(s))
    def test_05_nonexcluded_mismatch_is_hold(self):
        u=(C|A)-{b"60010"}|{b"72002"}
        s,d=probe(C,u)
        self.assertEqual(d,q.HOLD_SCOPE)
        self.assertEqual(s["nonexcluded_usda_only_fips_count"],1)
    def test_06_even_one_Census_excluded_prefix_is_hold(self):
        s,d=probe(C|{b"60010"},C|A)
        self.assertEqual(d,q.HOLD_SCOPE)
        self.assertEqual(s["census_keys_in_excluded_island_area_prefixes"],1)
    def test_07_frozen_q05_counts_not_changed(self):
        s,d=q.aggregate_scope(C,C|A,
           dict(invalid_census_key_rows=0,census_duplicate_key_rows=0),
           dict(invalid_usda_key_rows=0,usda_duplicate_fips_rows=3))
        self.assertEqual(d,q.HOLD_RECONCILE)
    def test_08_extra_unknown_mismatch_is_hold(self):
        s,d=probe(C,C|A|{b"99001"})
        self.assertEqual(d,q.HOLD_SCOPE)
    def test_09_geography_equivalence_is_never_granted(self):
        s,d=probe(C,C|A)
        self.assertIs(s["different_geographic_vintages_equivalent_proven"],False)
    def test_10_official_document_sources_are_fixed(self):
        self.assertEqual(len(q.DOCUMENTS),4)
        self.assertTrue(all(".census.gov/" in v or ".usda.gov/" in v for v in q.DOCUMENTS.values()))
    def test_11_incorrect_sha_stops_before_key_projection(self):
        with TemporaryDirectory() as t:
            p=Path(t)/"attempt-01.json"
            def fetch(label,url):
                return b"ROTATED",dict(full_body_bytes=7,full_body_sha256=hashlib.sha256(b"ROTATED").hexdigest(),status=200)
            with mock.patch.object(q,"verify_context"),mock.patch.object(q,"read_census_keys") as rows:
                out=q.run(fetch=fetch,out=p)
                rows.assert_not_called()
            self.assertEqual(out["disposition"],"HOLD_Q06_SOURCE_VINTAGE_CHANGED")
            self.assertIsNone(out["scope_provenance_aggregates"])
    def test_12_one_immutable_receipt_and_secret_free(self):
        with TemporaryDirectory() as t:
            p=Path(t)/"attempt-01.json"
            def fetch(label,url):
                return b"BAD",dict(full_body_bytes=3,full_body_sha256="SECRET",status=200)
            with mock.patch.object(q,"verify_context"):
                q.run(fetch=fetch,out=p)
                with self.assertRaises(RuntimeError):q.run(fetch=fetch,out=p)
            self.assertNotIn("01001",p.read_text())
            self.assertIs(json.loads(p.read_text())["science_f01_authorized"],False)

if __name__=="__main__":unittest.main()

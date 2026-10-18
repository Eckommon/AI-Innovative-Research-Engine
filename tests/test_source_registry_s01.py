import unittest
from copy import deepcopy
from tools import build_source_registry_s01 as m
class SourceRegistryTests(unittest.TestCase):
    def test_eight_preregistered_sources(self):
        self.assertEqual(len(m.SOURCES),8)
    def test_primary_reserved(self):
        x=next(z for z in m.SOURCES if z["id"]=="CMS-NPI")
        self.assertTrue(x["reserved"])
        self.assertFalse(x["reusable"])
    def test_no_registry_records_authorize_experiment(self):
        self.assertTrue(all(not x["reusable"] for x in m.SOURCES))
    def test_no_open_raw_source_files(self):
        self.assertTrue(all(p.startswith("research/") for z in m.SOURCES for p in z["evidence"]))
    def test_grade_d1_source_magic_not_full(self):
        self.assertEqual({z["id"] for z in m.SOURCES if z["grade"]=="D1"},{"NHTSA-RCL","NCES-IPEDS"})
    def test_transport_block_separate_from_nonexistence(self):
        self.assertIn("403",next(z for z in m.SOURCES if z["id"]=="SEC-BULK")["status"])
    def test_terminal_hold_not_scientific_pass(self):
        self.assertTrue("HOLD" in next(z for z in m.SOURCES if z["id"]=="NOAA-QCEW")["status"])
    def test_decision_fails_closed_without_two_reusable_d2(self):
        x=[{**s,"source_evidence":[{"path":"research/x","sha256":"a","bytes":1}],
            "required_tokens_present":{z:True for z in s["required"]},
            "observed_time":"SEE_IMMUTABLE_REFERENCED_EVIDENCE",
            "publication_time":"UNVERIFIED_SEPARATE_FROM_OBSERVED_TIME",
            "experimental_authorization":False} for s in deepcopy(m.SOURCES)]
        g,d=m.validate(x,[])
        self.assertEqual(len(g),12)
        self.assertEqual(d,"HOLD_NEED_DUAL_D2_SOURCE")
        self.assertEqual(sum(v["passed"] for v in g),12)
    def test_missing_evidence_causes_hold(self):
        x,missing=m.build()
        self.assertFalse(missing)
        self.assertEqual(len(x),8)
    def test_live_referenced_tokens_and_evidence(self):
        x,missing=m.build()
        self.assertFalse(missing)
        self.assertTrue(all(all(z["required_tokens_present"].values()) for z in x))
    def test_deterministic_build_excluding_run_clock(self):
        self.assertEqual(m.build(),m.build())
    def test_12_operating_gate_stays_separate_from_science(self):
        x,missing=m.build()
        g,d=m.validate(x,missing)
        self.assertEqual(len(g),12)
        self.assertEqual(d,"HOLD_NEED_DUAL_D2_SOURCE")
if __name__=="__main__": unittest.main()

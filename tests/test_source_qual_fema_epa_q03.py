"""Q03 synthetic tests: exact source identity, FIPS, time, monitor grain, redaction."""
import io
import json
import unittest
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock
from tools import qualify_source_fema_epa_q03 as q

def fema(rows):
    cols=q.FEMA_FIELDS+("incidentType",)
    return (",".join(cols)+"\n"+"".join(",".join(row+("SYNTHETIC_OUTCOME_SECRET",))+"\n" for row in rows)).encode()

def epa(rows, member=None):
    cols=q.EPA_FIELDS+("Arithmetic Mean",)
    text=",".join(cols)+"\n"+"".join(",".join(row+("SYNTHETIC_OUTCOME_SECRET",))+"\n" for row in rows)
    out=io.BytesIO()
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as arc:
        arc.writestr(member or q.EPA_MEMBER,text)
    return out.getvalue()

R=("01","001","0001","88101","1","24 HOUR","PM25","No Events","2024")

class Q03SyntheticTests(unittest.TestCase):
    def test_historical_window_and_noncounty_exclusion(self):
        keys,excluded=q.fema_keys(fema([
            ("01","001","2019-01-01"),
            ("01","003","2023-12-31"),
            ("01","005","2024-01-01"),
            ("01","999","2022-05-01"),
        ]))
        self.assertEqual(keys,{"01001","01003"})
        self.assertEqual(excluded["outside_historical_window_or_invalid_date"],1)
        self.assertEqual(excluded["invalid_or_noncounty_fips_syntax"],1)

    def test_exact_leading_zero_format(self):
        self.assertEqual(q.key("01","003"),"01003")
        for s,c in [("1","003"),("01","3"),("00","003"),("01","000"),("01","999")]:
            self.assertIsNone(q.key(s,c))

    def test_monitors_are_not_counties(self):
        keys,counts=q.epa_keys(epa([R,("01","001","0001","88101","1","1 HOUR","PM25","No Events","2024")]))
        self.assertEqual(keys,{"01001"})
        self.assertEqual(counts["distinct_monitors_all_parameters"],1)
        self.assertEqual(counts["distinct_monitor_duration_standard_event_signatures"],2)
        self.assertNotIn("SYNTHETIC_OUTCOME_SECRET",json.dumps(counts))

    def test_wrong_2024_year_fails(self):
        with self.assertRaises(ValueError):
            q.epa_keys(epa([R[:-1]+("2025",)]))

    def test_wrong_zip_member_fails(self):
        with self.assertRaises(ValueError):
            q.epa_keys(epa([R],"annual_aqi_by_county_2024.csv"))

    def test_precommitted_support_thresholds(self):
        keys={f"{s:02d}{c:03d}" for s in range(1,16) for c in range(1,8)}
        metrics,verdict=q.metrics(keys,keys,{})
        self.assertEqual(verdict,"PASS_Q03_SYNTAX_SUPPORT_ONLY__F01_NOT_AUTHORIZED")
        self.assertEqual(metrics["overlap_distinct_syntax_counties"],105)
        self.assertEqual(q.metrics(set(),keys,{})[1],"HOLD_Q03_INSUFFICIENT_SOURCE_NATIVE_KEY_SUPPORT")

    def test_unapproved_url_rejected_without_network(self):
        with self.assertRaises(ValueError):
            q.locked_fetch("https://example.com/alternate.zip")

    def test_immutable_receipt_never_discloses_case_ids_or_values(self):
        blobs={q.FEMA_URL:(fema([("01","001","2022-05-01")]),{"http_status":200}),
               q.EPA_URL:(epa([R]),{"http_status":200})}
        with TemporaryDirectory() as tmp:
            target=Path(tmp)/"evidence/source-structure-01.json"
            with mock.patch.object(q,"OUT",target),mock.patch.object(q,"verify_priors"),mock.patch.object(q,"locked_fetch",side_effect=lambda url:blobs[url]) as fetch:
                q.run()
                self.assertEqual(fetch.call_count,2)
            serialized=target.read_text()
            self.assertNotIn("SYNTHETIC_OUTCOME_SECRET",serialized)
            self.assertNotIn("01001",serialized)
            self.assertFalse(json.loads(serialized)["new_scientific_f01_authorized"])
            with mock.patch.object(q,"OUT",target):
                with self.assertRaises(RuntimeError):
                    q.run()

if __name__=="__main__":
    unittest.main()

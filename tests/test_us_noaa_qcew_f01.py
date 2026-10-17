import csv
import gzip
import json
import unittest
from io import StringIO
from tools import run_us_noaa_qcew_f01 as m

class F01Tests(unittest.TestCase):
    def test_locked_noaa_exact(self):
        self.assertIn("d2023_c20260323", m.NOAA_URL)
    def test_locked_bls_only_baseline(self):
        self.assertEqual(set(m.BLS_URLS), {"23","62","72"})
        self.assertTrue(all("/2024/1/industry/" in s for s in m.BLS_URLS.values()))
    def test_no_future_path_whitelist(self):
        with self.assertRaises(ValueError):
            m.source_download("https://data.bls.gov/cew/data/api/2025/1/industry/23.csv")
    def test_county_fips_zero_padding(self):
        self.assertEqual(m.county_key("1", "3"), "01003")
    def test_county_fips_invalid(self):
        self.assertIsNone(m.county_key("STATE", "ZONE"))
        self.assertIsNone(m.county_key("01", "2000"))
    def test_county_qcew_state_and_fips(self):
        self.assertTrue(m.county_area("01001"))
        self.assertFalse(m.county_area("09001"))
        self.assertFalse(m.county_area("01000"))
        self.assertFalse(m.county_area("US000"))
    def test_storm_calendar_explicit(self):
        self.assertEqual(m.storm_time("04/01/2023 20:48:00"),2023)
        self.assertEqual(m.storm_time("2023-04-01 20:48:00"),2023)
        self.assertIsNone(m.storm_time("2026-Jul-10"))
    def test_no_url_redirect(self):
        self.assertIsNone(m.NoRedirect().redirect_request(None, None, 302, "", {}, "https://bad.test"))
    def test_fixed_hazard_types(self):
        self.assertEqual(m.STORM_TYPES, {"Tornado","Flash Flood","Flood","Thunderstorm Wind","Hail"})
    def test_synthetic_eighteen_science_gates_and_no_outcome_results(self):
        cols=["CZ_TYPE","STATE_FIPS","CZ_FIPS","BEGIN_DATE_TIME","EVENT_ID","EVENT_TYPE"]
        f=StringIO();w=csv.writer(f);w.writerow(cols)
        w.writerow(["C","01","001","01/01/2023 11:11:00","1","Flood"])
        w.writerow(["Z","01","001","01/01/2023 11:11:00","2","Flood"])
        w.writerow(["C","09","001","01/01/2023 11:11:00","3","Flood"])
        raw=gzip.compress(f.getvalue().encode())
        def qcew(i):
            z=StringIO();c=csv.writer(z)
            c.writerow(["area_fips","own_code","industry_code","year","qtr","size_code","disclosure_code","month1_emplvl"])
            c.writerow(["01001","5",i,"2024","1","0","","SECRET_NUMERIC_BASELINE"])
            return z.getvalue().encode()
        bodies={i:qcew(i) for i in ("23","62","72")}
        source_meta={k:{"url":m.NOAA_URL if k=="NOAA_2023" else m.BLS_URLS[k[-2:]],
                        "status":200,"sha256":"0123", "fetched_utc":"2026-10-17T00:00:00+00:00"}
                    for k in ["NOAA_2023","BLS_2024_Q1_23","BLS_2024_Q1_62","BLS_2024_Q1_72"]}
        result=m.evaluate(raw,bodies,source_meta)
        self.assertEqual(len(result["gates"]),18)
        self.assertEqual(result["gates"][5]["numerator"],2)
        self.assertEqual(result["noaa_distinct_nonCT_counties"],1)
        self.assertTrue(result["disposition"].startswith("HOLD_"))
        self.assertNotIn("SECRET_NUMERIC_BASELINE",json.dumps(result))
    def test_noa_no_future_exposed(self):
        self.assertNotIn("2025/",m.NOAA_URL)
    def test_output_is_single_immutable_attempt(self):
        self.assertTrue(m.OUT.name=="attempt-01.json")

if __name__=="__main__":
    unittest.main()

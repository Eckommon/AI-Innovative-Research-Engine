"""Offline synthetic gates for the never-retry Census×USDA original-header Q04."""
import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest import mock
import zipfile
from tools import qualify_source_census_usda_q04 as q

def census(header="USPS\tGEOID\tNAME",member="2024_Gaz_counties_national.txt"):
    out=io.BytesIO()
    with zipfile.ZipFile(out,"w",compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(member,header+"\n01\t01001\tSECRET_COUNTY\n")
    return out.getvalue()

def usda(header="FIPS,State,County,2023 RUCC"):
    return (header+"\n01001,SECRET_STATE,SECRET_COUNTY,9\n").encode()

class Response:
    status=200
    def __init__(self,body,url):self.body=body;self.url=url;self.headers={}
    def __enter__(self):return self
    def __exit__(self,*_):return False
    def geturl(self):return self.url
    def read(self,n):return self.body[:n]
class Opener:
    def __init__(self,body,url):self.body=body;self.url=url;self.calls=0
    def open(self,request,timeout):self.calls+=1;return Response(self.body,self.url)

class SourceQ04SyntheticTests(unittest.TestCase):
    def test01_census_only_header_and_exact_geoid(self):
        out=q.inspect_census(census())
        self.assertEqual(out["header_fields"],["USPS","GEOID","NAME"])
        self.assertFalse(out["member_data_values_opened"])
        self.assertNotIn("SECRET_COUNTY",json.dumps(out))
    def test02_census_zip_member_changed_fails_closed(self):
        with self.assertRaises(ValueError):q.inspect_census(census(member="../unsafe.txt"))
    def test03_census_missing_geoid_fails_closed(self):
        with self.assertRaises(ValueError):q.inspect_census(census(header="USPS\tCOUNTY_NAME"))
    def test04_usda_header_without_rural_codes(self):
        val=q.inspect_usda(usda())
        self.assertTrue(val["literal_fips_present"])
        self.assertFalse(val["county_rucc_codes_opened"])
        self.assertNotIn("SECRET_COUNTY",json.dumps(val))
    def test05_usda_missing_literal_fips_fails_closed(self):
        with self.assertRaises(ValueError):q.inspect_usda(usda(header="State,County,2023 Code"))
    def test06_duplicate_usda_header_fails_closed(self):
        with self.assertRaises(ValueError):q.inspect_usda(usda(header="FIPS,FIPS,Code"))
    def test07_official_exact_url_only(self):
        with self.assertRaises(ValueError):
            q.fetch_original("CENSUS_2024_COUNTIES","https://other.gov/wrong.zip")
    def test08_source_hash_computed_from_full_bytes(self):
        raw=usda()
        opener=Opener(raw,q.USDA)
        val,rec=q.fetch_original("USDA_2023_RUCC",q.USDA,opener=opener)
        import hashlib
        self.assertEqual(rec["full_body_sha256"],hashlib.sha256(raw).hexdigest())
        self.assertEqual(val,raw)
        self.assertEqual(opener.calls,1)
        self.assertFalse(rec["rows_opened"])
    def test09_redirect_is_not_equivalent_to_original(self):
        opener=Opener(usda(),"https://example.org/redirected")
        with self.assertRaises(ValueError):
            q.fetch_original("USDA_2023_RUCC",q.USDA,opener=opener)
        self.assertEqual(opener.calls,1)
    def test10_one_try_failure_has_receipt_without_secret(self):
        with TemporaryDirectory() as temp:
            target=Path(temp)/"evidence/attempt-01.json"
            calls=[]
            def fake(label,url):
                calls.append(label)
                if label=="CENSUS_2024_COUNTIES":
                    return census(),{"full_body_bytes":123,"full_body_sha256":"a"*64}
                raise RuntimeError("SYNTHETIC_SECRET_01001")
            with mock.patch.object(q,"verify_context"),mock.patch.dict("os.environ",{"GITHUB_RUN_ID":"39412345678"}):
                actual=q.run(fetch=fake,out=target)
            self.assertEqual(calls,["CENSUS_2024_COUNTIES","USDA_2023_RUCC"])
            self.assertEqual(actual["disposition"],"HOLD_Q04_SOURCE_ACCESS_OR_SCHEMA")
            saved=target.read_text()
            self.assertNotIn("01001",saved);self.assertNotIn("SYNTHETIC_SECRET",saved)
            self.assertFalse(actual["science_f01_authorized"])
    def test11_success_never_opens_or_saves_rows(self):
        with TemporaryDirectory() as temp:
            target=Path(temp)/"evidence/attempt-01.json"
            def fake(label,url):
                raw=census() if label=="CENSUS_2024_COUNTIES" else usda()
                import hashlib
                return raw,{"full_body_sha256":hashlib.sha256(raw).hexdigest(),"full_body_bytes":len(raw)}
            with mock.patch.object(q,"verify_context"):
                rec=q.run(fetch=fake,out=target)
            self.assertEqual(rec["disposition"],"PASS_Q04_DUAL_D2_HEADERS_ONLY__KEY_BRIDGE_UNPROVEN")
            self.assertNotIn("SECRET_COUNTY",target.read_text())
            self.assertNotIn("01001",target.read_text())
            self.assertFalse(rec["source_native_county_key_bridge_verified"])
            with self.assertRaises(RuntimeError):q.run(fetch=fake,out=target)
if __name__=="__main__":
    unittest.main()

import csv
import io
import unittest
import zipfile
from email.message import Message
from tools import qualify_source_fema_epa_q01 as m

class Response:
    status=200
    def __init__(self,url,body):
        self.url=url
        self.body=body
        self.headers=Message()
    def geturl(self): return self.url
    def read(self,size): return self.body[:size]
    def __enter__(self): return self
    def __exit__(self,*exc): return False

class Opener:
    def __init__(self,res): self.res=res
    def open(self,req,timeout):
        self.method=req.get_method()
        return self.res

class SourceQualifierTests(unittest.TestCase):
    def test_frozen_url_rejects_mirror(self):
        with self.assertRaises(ValueError):
            m.fetch("https://mirror.example/data.csv",100)
    def test_get_exact_source_no_redirection(self):
        stub=Opener(Response(m.FEMA,b"fipsStateCode,fipsCountyCode\n01,001"))
        raw,meta=m.fetch(m.FEMA,64*1024*1024,stub)
        self.assertEqual(stub.method,"GET")
        self.assertEqual(meta["byte_count"],len(raw))
        self.assertFalse(meta["case_or_outcome_rows_parsed"])
    def test_fema_parser_no_record_rows(self):
        a=m.fema_header(b"fipsStateCode,fipsCountyCode,event_value\n01,001,NEVER_PRINT\n")
        self.assertTrue(a["county_fields_documented"])
        self.assertEqual(a["parsed_case_rows"],0)
    def test_fema_missing_county_field_fails(self):
        self.assertFalse(m.fema_header(b"country,country_code\n")["county_fields_documented"])
    def test_zip_only_one_member_and_header(self):
        buf=io.BytesIO()
        with zipfile.ZipFile(buf,"w") as z:
            z.writestr("annual_aqi_by_county_2024.csv","State Code,County Code,Days with AQI\n01,001,SECRET\n")
        a=m.epa_header(buf.getvalue())
        self.assertEqual(a["parsed_case_rows"],0)
        self.assertTrue(a["county_fields_documented"])
    def test_zip_traversal_rejected(self):
        buf=io.BytesIO()
        with zipfile.ZipFile(buf,"w") as z:z.writestr("../hack.csv","State Code,County Code\n")
        with self.assertRaises(ValueError):m.epa_header(buf.getvalue())
    def test_zip_nonzip_rejected(self):
        with self.assertRaises(ValueError):m.epa_header(b"<html>fake</html>")
    def test_header_schema_without_case_does_not_raise_grade(self):
        x={"FEMA_v2_full_CSV":{"http_status":200,"sha256":"a"*64,"byte_count":10,"county_fields_documented":False,"parsed_case_rows":0}}
        self.assertEqual(m.classify(x),"HOLD_SOURCE_ACCESS_OR_SCHEMA")
    def test_only_two_complete_verified_sources_get_d2_pair(self):
        s={n:{"http_status":200,"sha256":"a"*64,"byte_count":10,"county_fields_documented":True,"parsed_case_rows":0} for n in m.SOURCES}
        self.assertEqual(m.classify(s),"D2_PAIR_READY_KEYS_DOCUMENTED_ONLY")
    def test_one_incomplete_body_denies_promotion(self):
        s={n:{"http_status":200,"sha256":"a"*64,"byte_count":10,"county_fields_documented":True,"parsed_case_rows":0} for n in m.SOURCES}
        s["EPA_2024_county_annual_AQI_ZIP"]["byte_count"]=0
        self.assertEqual(m.classify(s),"HOLD_SOURCE_ACCESS_OR_SCHEMA")
    def test_redirect_is_blocked(self):
        self.assertIsNone(m.NoRedirect().redirect_request(None,None,302,"",{},"https://bad.example"))
    def test_frozen_archive_2024_and_primary_separation(self):
        self.assertIn("2024.zip",m.EPA)
        self.assertNotIn("nppes",m.EPA)
        self.assertEqual(m.DIR.parts[-1],"FEMA-EPA-Q01")

if __name__=="__main__":unittest.main()

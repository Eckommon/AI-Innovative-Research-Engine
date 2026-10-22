"""Q07 source-byte/header-only synthetic tests, no external network requests."""
import hashlib
import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest import mock
import zipfile

from tools import qualify_source_census_usda_q07 as q

def zip_header(line=b"USPS\tGEOID\tNAME\tALAND\n",member=q.MEMBER,additional=False):
    mem=io.BytesIO()
    with zipfile.ZipFile(mem,"w",compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr(member,line+b"01\t01001\tSECRET_COUNTY\t12345\n")
        if additional:z.writestr("extra.txt",b"GEOID\nFAKE\n")
    return mem.getvalue()

class Response:
    status=200
    headers={}
    def __init__(self,payload,url):self.payload=payload;self.url=url;self.calls=0
    def __enter__(self):return self
    def __exit__(self,*_):return False
    def geturl(self):return self.url
    def read(self,n):self.calls+=1;return self.payload[:n]
class Opener:
    def __init__(self,response):self.response=response;self.calls=0
    def open(self,request,timeout=40):
        self.calls+=1
        return self.response

class Q07Tests(unittest.TestCase):
    def test01_correct_single_member_geoid_only(self):
        info=q.inspect_header_only(zip_header())
        self.assertEqual(info["zip_member"],q.MEMBER)
        self.assertEqual(info["tab_header_fields"],["USPS","GEOID","NAME","ALAND"])
        self.assertFalse(info["county_rows_opened"])
        self.assertNotIn("SECRET_COUNTY",json.dumps(info))
    def test02_unsafe_zip_member_denied(self):
        with self.assertRaises(ValueError):q.inspect_header_only(zip_header(member="../escape.txt"))
    def test03_extra_member_denied(self):
        with self.assertRaises(ValueError):q.inspect_header_only(zip_header(additional=True))
    def test04_missing_geoid_denied(self):
        with self.assertRaises(ValueError):q.inspect_header_only(zip_header(line=b"USPS\tNAME\tALAND\n"))
    def test05_duplicate_geoid_denied(self):
        with self.assertRaises(ValueError):q.inspect_header_only(zip_header(line=b"GEOID\tGEOID\tNAME\n"))
    def test06_zip_magic_required(self):
        with self.assertRaises(ValueError):q.inspect_header_only(b"NOTAZIP")
    def test07_non_utf8_header_denied(self):
        with self.assertRaises(UnicodeDecodeError):q.inspect_header_only(zip_header(line=b"GEOID\t\xff\n"))
    def test08_original_hash_precedes_header(self):
        raw=zip_header()
        response=Response(raw,q.URL);client=Opener(response)
        output,receipt=q.fetch(opener=client)
        self.assertEqual(client.calls,1)
        self.assertEqual(receipt["source_body_sha256"],hashlib.sha256(raw).hexdigest())
        self.assertEqual(output,raw)
        self.assertFalse(receipt["http_date_is_publication_time"])
    def test09_http_redirect_to_other_url_denied(self):
        response=Response(zip_header(),"https://example.org/wrong.zip")
        with self.assertRaises(ValueError):q.fetch(opener=Opener(response))
    def test10_huge_source_denied(self):
        response=Response(b"Z"*(q.MAX_COMPRESSED+1),q.URL)
        with self.assertRaises(ValueError):q.fetch(opener=Opener(response))
    def test11_one_success_receipt_preserves_no_individual_codes(self):
        raw=zip_header()
        def synth():return raw,{"source_body_bytes":len(raw),"source_body_sha256":hashlib.sha256(raw).hexdigest()}
        with TemporaryDirectory() as directory:
            out=Path(directory)/"evidence/attempt-01.json"
            with mock.patch.object(q,"verify_context"):
                result=q.run(source_fetch=synth,out=out)
                with self.assertRaises(RuntimeError):q.run(source_fetch=synth,out=out)
            self.assertTrue(result["disposition"].startswith("PASS_Q07"))
            self.assertNotIn("01001",out.read_text())
            self.assertNotIn("SECRET_COUNTY",out.read_text())
            self.assertFalse(result["science_f01_authorized"])
    def test12_schema_failure_persists_safe_hold(self):
        raw=zip_header(line=b"USPS\tSTATE\n")
        with TemporaryDirectory() as directory:
            out=Path(directory)/"evidence/attempt-01.json"
            with mock.patch.object(q,"verify_context"):
                result=q.run(source_fetch=lambda:(raw,{"source_body_sha256":hashlib.sha256(raw).hexdigest()}),out=out)
            self.assertEqual(result["disposition"],"HOLD_Q07_SOURCE_ACCESS_OR_SCHEMA")
            self.assertNotIn("SECRET_COUNTY",out.read_text())
            self.assertIsNone(result["original_header_only"])

if __name__=="__main__":unittest.main()

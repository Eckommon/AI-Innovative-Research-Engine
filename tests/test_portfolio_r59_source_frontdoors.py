import unittest
from email.message import Message
from urllib.error import HTTPError
from tools import inspect_portfolio_r59_source_frontdoors as p

class Response:
    status=200
    def __init__(self,url,body=b"PK\x03\x04BAD_RECORD"):
        self.url=url;self.body=body;self.pos=0;self.headers=Message()
    def geturl(self):return self.url
    def read(self,n):
        x=self.body[self.pos:self.pos+n];self.pos+=len(x);return x
    def __enter__(self):return self
    def __exit__(self,*a):return None

class Opener:
    def __init__(self,r=None,err=None):self.r=r;self.err=err
    def open(self,req,timeout):
        self.method=req.get_method()
        if self.err:raise self.err
        return self.r

class R59PreflightTests(unittest.TestCase):
    def test_exact_whitelist(self):
        with self.assertRaises(ValueError):p.check("https://mirror.example/score.zip","ZIP4")
    def test_wrong_method_rejected(self):
        with self.assertRaises(ValueError):
            p.check(p.URLS["SEC_submissions_bulk_zip"][0],"ZIP4")
    def test_zip_four_bytes_only(self):
        url=p.URLS["IPEDS_2023_24_final_zip"][0]
        r=Response(url);o=Opener(r);x=p.check(url,"ZIP4",o)
        self.assertEqual(o.method,"GET");self.assertEqual(r.pos,4)
        self.assertTrue(x["zip_magic_verified"]);self.assertFalse(x["outcome_rows_opened"])
    def test_html200_not_zip(self):
        url=p.URLS["SCORECARD_2025_institution_zip"][0]
        x=p.check(url,"ZIP4",Opener(Response(url,b"<html>wrong body</html>")))
        self.assertFalse(x["zip_magic_verified"])
    def test_sec_head_reads_zero_bytes(self):
        url=p.URLS["SEC_submissions_bulk_zip"][0]
        r=Response(url);x=p.check(url,"HEAD",Opener(r))
        self.assertEqual(x["read_bytes"],0);self.assertEqual(r.pos,0)
    def test_403_no_absence_claim(self):
        url=p.URLS["USPTO_fee_catalog"][0]
        x=p.check(url,"HEAD",Opener(err=HTTPError(url,403,"denied",Message(),None)))
        self.assertEqual(x["result"],"HTTP_UNVERIFIED_NO_ABSENCE_CLAIM")
    def test_deny_redirect(self):
        self.assertIsNone(p.NoRedirect().redirect_request(None,None,302,"",{},"https://x.test/"))
    def test_no_future_company_specific_apis(self):
        self.assertFalse(any("CIK0000" in url or "2027" in url for url,_ in p.URLS.values()))

if __name__=="__main__":unittest.main()

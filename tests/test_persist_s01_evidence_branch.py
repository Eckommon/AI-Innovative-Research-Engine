"""Offline tests for one-run branch persistence, no raw source rows, no main writes."""
import json
import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest import mock
from tools import persist_s01_evidence_branch as p

QUAL="FEMA-EPA-Q04"
RUN="39350012345"

def fixture(root, value=None):
    base=root/"research/SOURCE-REGISTRY-S01/qualifications"/QUAL/"evidence"
    base.mkdir(parents=True)
    obj={"qualification":QUAL,"incremental_monetary_cost_usd":0,
         "science_f01_authorized":False,"source_case_rows_emitted":False,
         "future_outcome_values_emitted":False,"individual_identifiers_emitted":False}
    if value:obj.update(value)
    (base/"attempt-01.json").write_text(json.dumps(obj))
    (base/"attempt-01.md").write_text("# Source-only receipt\n")
    return base

class PersistenceGuardTests(unittest.TestCase):
    def test_branch_is_deterministic_and_not_main(self):
        ref=p.branch_ref(QUAL,RUN)
        self.assertEqual(ref,"refs/heads/evidence/s01/fema-epa-q04/39350012345")
        self.assertNotIn("refs/heads/main",ref)
    def test_bad_qualification_or_run_rejected(self):
        for q,run in [("../escape",RUN),("lowercase",RUN),(QUAL,"123"),(QUAL,"abc")]:
            with self.assertRaises(ValueError):p.branch_ref(q,run)
    def test_paths_must_be_two_exact_receipts(self):
        with TemporaryDirectory() as d:
            root=Path(d);fixture(root)
            self.assertEqual(len(p.validate_receipts(root,QUAL,"attempt-01.json","attempt-01.md")),2)
            for j,m in [("../file.json","attempt-01.md"),("attempt-01.json","../x.md"),("attempt-01.json","other.md")]:
                with self.assertRaises(ValueError):p.validate_receipts(root,QUAL,j,m)
    def test_missing_or_symlinked_artifact_rejected(self):
        with TemporaryDirectory() as d:
            root=Path(d);base=fixture(root)
            (base/"attempt-01.md").unlink()
            (base/"attempt-01.md").symlink_to(base/"attempt-01.json")
            with self.assertRaises(ValueError):p.validate_receipts(root,QUAL,"attempt-01.json","attempt-01.md")
    def test_missing_no_outcome_or_cost_proof_rejected(self):
        with TemporaryDirectory() as d:
            root=Path(d);fixture(root,{"future_outcome_values_emitted":True})
            with self.assertRaises(ValueError):p.validate_receipts(root,QUAL,"attempt-01.json","attempt-01.md")
    def test_wrong_qualification_receipt_rejected(self):
        with TemporaryDirectory() as d:
            root=Path(d);fixture(root,{"qualification":"DIFFERENT-Q04"})
            with self.assertRaises(ValueError):p.validate_receipts(root,QUAL,"attempt-01.json","attempt-01.md")
    def test_publish_creates_only_independent_ref(self):
        with TemporaryDirectory() as d:
            root=Path(d);fixture(root);calls=[]
            def runner(args,check=True):
                calls.append(args)
                return SimpleNamespace(returncode=2 if "ls-remote" in args else 0)
            with mock.patch.dict(os.environ,{"GITHUB_REPOSITORY":p.REPO,"GITHUB_RUN_ID":RUN}):
                proof=p.publish(QUAL,RUN,"attempt-01.json","attempt-01.md",root=root,runner=runner)
            self.assertFalse(proof["main_branch_direct_write"])
            self.assertTrue(any(c[:2]==["git","push"] and c[-1].endswith("/39350012345") for c in calls))
            self.assertFalse(any("HEAD:main" in " ".join(c) for c in calls))
    def test_existing_remote_ref_or_api_error_fails_closed(self):
        for error_code in (0,128):
            with TemporaryDirectory() as d:
                root=Path(d);fixture(root)
                def runner(args,check=True):
                    return SimpleNamespace(returncode=error_code)
                with mock.patch.dict(os.environ,{"GITHUB_REPOSITORY":p.REPO,"GITHUB_RUN_ID":RUN}):
                    with self.assertRaises(RuntimeError):
                        p.publish(QUAL,RUN,"attempt-01.json","attempt-01.md",root=root,runner=runner)
    def test_noncanonical_environment_rejected_before_git(self):
        with TemporaryDirectory() as d:
            root=Path(d);fixture(root)
            with mock.patch.dict(os.environ,{"GITHUB_REPOSITORY":"other/repo","GITHUB_RUN_ID":RUN}):
                with self.assertRaises(RuntimeError):
                    p.publish(QUAL,RUN,"attempt-01.json","attempt-01.md",root=root)
if __name__=="__main__":unittest.main()

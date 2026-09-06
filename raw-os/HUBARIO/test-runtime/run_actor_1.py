"""HUBARIO runtime test for RAW OS Actor 1.

Runs the existing deterministic RAW OS test engine and asserts the
expected controlled-deployment outcome for the Abang Sayur pilot scenario.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "raw-os" / "test-engine"))

from raw_os_test_engine import run_actor_1  # noqa: E402


result = run_actor_1()

assert result["purchase_status"] == "BLOCKED"
assert result["sales_status"] == "VOID"
assert result["recognised_sales"] == 0.0
assert result["void_sales"] == 500.0
assert result["evidence_preserved"] is True
assert result["actor_review"] is True
assert set(result["violations"]) == {
    "CREDIT_AUTHORITY_EXCEEDED",
    "GEOGRAPHIC_SCOPE_EXCEEDED",
    "PRIOR_PERMISSION_MISSING",
}
assert result["decision"] == "BLOCK_AND_REVIEW"

print(json.dumps({"status": "PASS", "runtime": "HUBARIO", "actor": "ACTOR_001", "result": result}, indent=2))

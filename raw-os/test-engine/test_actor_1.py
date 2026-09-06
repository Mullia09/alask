import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from raw_os_test_engine import run_actor_1


result = run_actor_1()

assert result["purchase_status"] == "BLOCKED"
assert result["sales_status"] == "VOID"
assert result["recognised_sales"] == 0.0
assert result["void_sales"] == 500.0
assert result["evidence_preserved"] is True
assert set(result["violations"]) == {
    "CREDIT_AUTHORITY_EXCEEDED",
    "GEOGRAPHIC_SCOPE_EXCEEDED",
    "PRIOR_PERMISSION_MISSING",
}
assert result["decision"] == "BLOCK_AND_REVIEW"

print("PASS: Actor 1 compound violation scenario")

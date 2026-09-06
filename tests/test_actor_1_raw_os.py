import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parents[1] / "raw-os" / "test-engine"
sys.path.insert(0, str(ENGINE_DIR))

from raw_os_test_engine import run_actor_1  # noqa: E402


def test_actor_1_compound_violation():
    result = run_actor_1()

    assert result["purchase_status"] == "BLOCKED"
    assert result["sales_status"] == "VOID"
    assert result["recognised_sales"] == 0.0
    assert result["void_sales"] == 500.0
    assert result["evidence_preserved"] is True
    assert result["actor_review"] is True
    assert result["decision"] == "BLOCK_AND_REVIEW"
    assert set(result["violations"]) == {
        "CREDIT_AUTHORITY_EXCEEDED",
        "GEOGRAPHIC_SCOPE_EXCEEDED",
        "PRIOR_PERMISSION_MISSING",
    }

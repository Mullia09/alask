"""RAW OS v0.9 deterministic test engine.

Domain: Abang Sayur Pilot
Purpose: Execute bounded authority, credit, geographic scope and permission checks.
This is a prototype test harness, not a production financial system.
"""

from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class Actor:
    actor_id: str
    role: str
    credit_limit: float
    authorised_area: str


@dataclass
class TransactionRequest:
    transaction_id: str
    actor_id: str
    purchase_amount: float
    sales_amount: float
    sales_area: str
    permission: bool


def evaluate(actor: Actor, request: TransactionRequest) -> Dict[str, Any]:
    checks = {
        "credit": {
            "pass": request.purchase_amount <= actor.credit_limit,
            "requested": request.purchase_amount,
            "limit": actor.credit_limit,
        },
        "geographic_scope": {
            "pass": request.sales_area == actor.authorised_area,
            "requested_area": request.sales_area,
            "authorised_area": actor.authorised_area,
        },
        "permission": {
            "pass": request.permission,
        },
    }

    violations: List[str] = []
    if not checks["credit"]["pass"]:
        violations.append("CREDIT_AUTHORITY_EXCEEDED")
    if not checks["geographic_scope"]["pass"]:
        violations.append("GEOGRAPHIC_SCOPE_EXCEEDED")
    if not checks["permission"]["pass"]:
        violations.append("PRIOR_PERMISSION_MISSING")

    purchase_status = "VALID" if checks["credit"]["pass"] else "BLOCKED"
    sales_status = "VALID" if checks["geographic_scope"]["pass"] and checks["permission"]["pass"] else "VOID"
    recognised_sales = request.sales_amount if sales_status == "VALID" else 0.0

    return {
        "transaction_id": request.transaction_id,
        "actor_id": actor.actor_id,
        "checks": checks,
        "violations": violations,
        "purchase_status": purchase_status,
        "sales_status": sales_status,
        "reported_sales": request.sales_amount,
        "recognised_sales": recognised_sales,
        "void_sales": request.sales_amount - recognised_sales,
        "evidence_preserved": True,
        "actor_review": bool(violations),
        "decision": "PASS" if not violations else "BLOCK_AND_REVIEW",
    }


def run_actor_1() -> Dict[str, Any]:
    actor = Actor(
        actor_id="ACTOR_001",
        role="PIONEER",
        credit_limit=1000.0,
        authorised_area="A",
    )
    request = TransactionRequest(
        transaction_id="T-A1-001",
        actor_id="ACTOR_001",
        purchase_amount=1500.0,
        sales_amount=500.0,
        sales_area="C",
        permission=False,
    )
    return evaluate(actor, request)


if __name__ == "__main__":
    import json
    print(json.dumps(run_actor_1(), indent=2))

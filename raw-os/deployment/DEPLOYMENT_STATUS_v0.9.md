# RAW OS v0.9 — Deployment Status

**Status:** Test Deployment Preparation
**Domain:** Abang Sayur Pilot
**Repository:** Mullia09/alask

## Current State

RAW OS framework v0.1–v0.8 is present in the repository, together with v1.0 system-design components #1–#8 and Actor 1 prototype/test artefacts.

The repository already contains GitHub Actions workflows for Python and static content. This document records the deployment boundary for the RAW OS prototype.

## Deployment Boundary

This is a controlled prototype/test deployment, not a production financial system.

No real payment, credit issuance, inventory settlement, or punitive actor action is authorised by this prototype.

## Test Scenario

Actor 1:
- Pioneer role
- Credit limit: RM1,000
- Purchase request: RM1,500
- Authorised area: A
- Sales area attempted: C
- Prior permission: none
- Example submitted sales: RM500

## Expected Runtime Behaviour

1. Receive actor transaction intent.
2. Validate identity, role, capability and authority context.
3. Evaluate credit constraint.
4. Evaluate geographic scope.
5. Evaluate permission requirement.
6. Aggregate independent constraint results.
7. Block unauthorised purchase.
8. Mark out-of-scope sales submission as VOID for operational recognition.
9. Preserve original submission and evidence.
10. Generate compliance-review state without automatically imposing punitive action.

## Deployment Invariants

- UI is not an authority source.
- AI is not an authority source.
- Capability does not imply authority.
- VOID does not mean DELETE.
- Operational ledger excludes invalid transactions.
- Audit/evidence ledger preserves invalid attempts when required.
- Production secrets and real financial credentials are prohibited in prototype configuration.

## What “Deployed” Means Here

Deployment means the repository contains the deployable prototype configuration and automated test/deployment path. It does not mean that a live production service or real financial integration is active.

## Next Technical Gate

Before production deployment:
- implement executable rule engine;
- implement persistent database;
- add server-side authorisation;
- add real API contracts;
- add automated test suite;
- add observability and audit storage;
- perform security review;
- perform pilot acceptance testing.

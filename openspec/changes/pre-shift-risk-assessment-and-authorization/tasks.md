## 1. Preconditions
- [ ] 1.1 Human resolves design.md Open Questions; record answers in design.md and `docs/domain/risk-assessment.md`
- [ ] 1.2 Finalize contract changes in `contracts/openapi.yaml`; `make contracts-lint` passes

## 2. API foundation
- [ ] 2.1 Add pgx, DB pool in `internal/platform/db`, migration runner; `go test ./...` passes
- [ ] 2.2 Migration for drivers, vehicles, supervisors, sleep_records, shifts, risk_assessments, shift_decisions (up/down); verified against compose PostgreSQL
- [ ] 2.3 Standard error responses + request validation helpers; handler tests

## 3. Sleep data ingestion
- [ ] 3.1 `integrations.SleepSource` interface + seeded simulator + JSON import
- [ ] 3.2 `POST /v1/drivers/{id}/sleep-records` with idempotency; tests for scenarios in `specs/sleep-data-ingestion`
- [ ] 3.3 `GET /v1/drivers`, `GET /v1/drivers/{id}` with seed data labeled simulated

## 4. Risk assessment
- [ ] 4.1 Pure `Assess` + `RiskConfig` (table-driven tests: normal, missing, insufficient, determinism)
- [ ] 4.2 Assessment endpoints persist immutable results and move shift to `awaiting_decision`; tests per spec

## 5. Shift authorization
- [ ] 5.1 Shift state machine with transition table tests (all valid and invalid transitions)
- [ ] 5.2 `POST /v1/shifts`, `GET /v1/shifts[/{id}]`, `POST /v1/shifts/{id}/decision` (409 on invalid, reason rules); tests per spec

## 6. Dashboard
- [ ] 6.1 Generate TS types from the contract; replace hand-written types; `pnpm typecheck` passes
- [ ] 6.2 Driver list, assessment view (factors, missing inputs, disclaimer, simulation label), authorize/reject
- [ ] 6.3 Component/client tests; `make lint-dashboard test-dashboard build-dashboard` pass

## 7. Verification
- [ ] 7.1 End-to-end manual run of demo steps 1–3 against local stack; record results honestly
- [ ] 7.2 `make check` and `make contracts-lint` pass; docs updated; `/opsx:archive`

## Acceptance criteria
All scenarios in `specs/*` have passing automated tests; no hard-coded unapproved thresholds; all
simulated data labeled; no secrets or real health data committed.

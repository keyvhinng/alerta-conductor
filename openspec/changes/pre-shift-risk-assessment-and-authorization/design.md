## Context
Bootstrap provides the API skeleton (`/v1/health`), a proposed OpenAPI contract, and the domain docs
(`docs/domain/risk-assessment.md`, `shift-lifecycle.md`). No persistence, auth, or domain code exists.
See proposal.md for motivation.

## Goals / Non-Goals
- Goals: working Flow A end-to-end (sleep data → assessment → decision) in simulation mode.
- Non-Goals: SSE, monitoring events, alerts, incidents, real providers, clinical validation.

## Decisions
1. **Assessment is a pure function** in `internal/assessments` (`Assess(input, RiskConfig) Result`), no I/O; handlers and repositories wrap it. Alternative: SQL-computed — rejected (hard to test/explain).
2. **Rule-based, additive factors** with each factor emitting `{code, description, observedValue}`. Alternative: scoring model — rejected (not explainable, no validated data).
3. **Config, not constants:** `RiskConfig` loaded from a file/env, with `approvalStatus` (`demo-unapproved` for the hackathon) echoed in the output. Boundary values are supplied during implementation by a human; this change must not invent them.
4. **State machine** in `internal/shifts` as a table of allowed transitions; persistence uses a conditional update (`WHERE state = $expected`) to prevent races.
5. **Persistence:** pgx + plain SQL migrations (`apps/api/migrations`), tables `drivers, vehicles, supervisors, sleep_records, shifts, risk_assessments, shift_decisions`, all with `data_origin` where applicable. Assessments and decisions are append-only.
6. **Ingestion idempotency:** unique `(driver_id, source_record_id)` with `ON CONFLICT DO NOTHING`; count duplicates.
7. **Source abstraction:** `integrations.SleepSource` interface; MVP implementations: simulator (seeded, deterministic) and manual/JSON import.
8. **Dashboard types** generated from `contracts/openapi.yaml` (openapi-typescript) replacing `src/lib/api/types.ts`.

## Risks / Trade-offs
- [Unvalidated thresholds look authoritative] → label `approvalStatus`, disclaimer in API and UI, no "safe/unsafe" wording.
- [No auth: anyone can authorize] → acceptable only for the local/simulated demo; must be resolved before public deploy (Open Question 1).
- [Supervisor identity unknown without auth] → seeded demo supervisor; `decidedBy` recorded as that id.

## Migration Plan
First migration creates the tables; down migration drops them. Local DB via compose only; nothing deployed.

## Open Questions (must be resolved by a human before `/opsx:apply`)
1. Which sleep inputs and which level boundaries for the demo config, and who approves them?
2. How is the supervisor identified (seeded user vs. auth) for the public demo?
3. Lookback window length for sleep records.

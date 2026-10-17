# api — agent notes
Scope: `apps/api/` only. Go (see `go.mod`), chi, pgx (to be added with first persistence), PostgreSQL. Commands: `make test-api`, `make lint-api`, `make api`.

- **Architecture:** modular monolith under `internal/<domain>/`. Keep transport handlers, domain logic, and persistence separate. Domain code must not import `net/http` or `pgx`; depend on small interfaces.
- **Risk logic** (assessments) is pure, deterministic, versioned (`algorithmVersion`), explainable (`factors`, `missingInputs`), and configured, never hard-coded thresholds. Missing data → `insufficient_data`, not "low".
- **Validation** at the transport boundary; return the contract `Error` shape; invalid state transitions → 409.
- **Database:** SQL migrations in `migrations/`; parameterized queries only; UTC timestamps; `data_origin` on simulatable rows.
- **Idempotent ingestion** keyed by `eventId` / `sourceRecordId`; duplicates are counted, not reprocessed; order by `sequence`.
- **Contracts:** `contracts/openapi.yaml` is authoritative; update it in the same change. Add handler tests with `httptest`; domain tests are table-driven; DB tests use real PostgreSQL (compose), not mocks, once persistence exists.
- Don't log health data. Config via env only (`internal/config`).

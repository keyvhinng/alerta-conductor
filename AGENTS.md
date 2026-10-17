# AGENTS.md — Alerta Conductor

Preventive safety platform for professional drivers (Peru; Hack the Andes 2026, Oct 17–18).
Pre-shift fatigue-risk assessment + real-time driver monitoring + supervisor dashboard.
It is **decision support, not a medical device**, and not a navigation/fleet-tracking product.

## Layout
- `apps/driver-monitor/` Python edge app (camera, telemetry, local alerts, events). Observes; never decides.
- `apps/api/` Go modular monolith. Owns risk logic, shift states, alerts, incidents, persistence.
- `apps/dashboard/` Next.js supervisor UI. Presents and sends supervisor actions.
- `contracts/` OpenAPI (`openapi.yaml`) and event JSON Schemas. Source of truth for shapes.
- `docs/` product → architecture → domain → operations. `openspec/` feature specs and changes.
- `infra/` Docker Compose. `tests/fixtures/` shared, clearly-simulated fixtures.

## Read before coding (in order)
1. `docs/product/prd.md` and `mvp.md` (note AGREED / PROPOSED / OPEN markers)
2. `docs/architecture/overview.md` and relevant `adr/`
3. `docs/domain/*` relevant to your task (risk-assessment, shift-lifecycle, privacy)
4. `openspec/specs/` and the active change in `openspec/changes/`
5. `contracts/` for any API/event you touch, and your app's `AGENTS.md`

## OpenSpec workflow
Behavior-changing work goes through OpenSpec (`/opsx:propose`, `/opsx:apply`, `/opsx:archive`, or the
`openspec` CLI). Do not hand-edit generated skills/commands. Proposal → human review → implement tasks
→ archive. Product docs hold intent, OpenSpec holds behavior (GIVEN/WHEN/THEN), contracts hold shapes,
ADRs hold architectural decisions. Don't duplicate across levels; link instead.

## Rules
1. Read relevant docs before coding.
2. Use OpenSpec for behavior-changing feature work.
3. Do not implement unapproved features.
4. Stay within your assigned app scope.
5. Update `contracts/` when APIs/events change.
6. Update specs when behavior changes.
7. Write tests for implemented requirements.
8. No unnecessary infrastructure (no Kafka/Redis/Kubernetes/brokers).
9. Never fabricate integration or test results; report failures as they are.
10. Never commit secrets or personal health data.
11. Mock data must be explicitly labeled simulated (`dataOrigin`/`simulated`).
12. Preserve architectural decisions (ADRs) unless a change is explicitly approved.
13. Do not invent risk thresholds or medical/accident-reduction claims.
14. Do not push, deploy, or create cloud resources without explicit authorization.

## Conventions
UTC timestamps (RFC 3339); UUID ids; API prefix `/v1`; technical docs in English, product-facing UI/pitch
text in Spanish. Entry points are `make` targets (`make help`). Formatting: gofmt, ruff, prettier.

## Privacy & security
Raw camera video never leaves the device or the repo. Send structured events only. Minimize personal
and health data; keep it out of logs. See `docs/domain/privacy.md`. Secrets only via env (`.env` is ignored).

## Definition of Done
- Behavior matches the OpenSpec scenarios; tests cover them and pass (`make test`)
- `make lint` clean; dashboard builds (`make build-dashboard`)
- Contracts and docs/specs updated and consistent; `make contracts-lint` passes
- Simulated data labeled; no secrets/health data/video committed
- Final report states exactly what was run and what was not

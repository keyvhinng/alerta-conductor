## Why
Supervisors currently decide whether a driver starts a shift without structured insight into the
driver's recent rest. Fatigue is a leading risk factor, and a pre-shift check is the earliest and
cheapest point to intervene. This is the first feature of the Alerta Conductor demo flow
(steps 1–3 in `docs/product/mvp.md`) and establishes the shift lifecycle everything else builds on.

## What Changes
- Ingest sleep/recovery records through a source-agnostic path (simulator, manual, import), idempotently, with data provenance.
- Compute an explainable, versioned, deterministic pre-shift risk assessment with a recommendation (authorize / review / withhold) and explicit missing inputs.
- Let a supervisor authorize or reject a planned shift, recording actor, time, and reason; the supervisor decision is final.
- Introduce the shift lifecycle states up to `authorized`/`rejected` (the `active`/`completed` transitions are only guarded, not driven by monitoring yet).
- Dashboard: driver list, assessment view, authorize/reject, with visible simulation labeling.
- First schema migration and replace hand-written dashboard types with contract-derived ones.

Out of scope: real wearable provider integrations, in-shift monitoring, alerts/incidents, authentication (open question), approved clinical thresholds.

## Capabilities
### New Capabilities
- `sleep-data-ingestion`: Accept and store sleep/recovery records with provenance and idempotency.
- `pre-shift-risk-assessment`: Produce explainable fatigue-risk assessments and recommendations for a planned shift.
- `shift-authorization`: Supervisor decision and shift lifecycle up to authorized/rejected.

### Modified Capabilities
None (no specs exist yet).

## Impact
- `apps/api`: new domains `drivers`, `wearables`, `assessments`, `shifts`; migrations; pgx dependency.
- `apps/dashboard`: driver list, assessment, decision screens; API client generated/derived from contract.
- `contracts/openapi.yaml`: promote the proposed endpoints (drivers, sleep-records, shifts, assessment, decision) from `proposed` to `implemented`, refining as needed.
- `docs/domain/risk-assessment.md`: record the approved demo configuration and its label.
- Requires human decisions listed in `design.md` (Open Questions) before implementation starts.

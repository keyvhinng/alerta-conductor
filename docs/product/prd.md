# Product Requirements Document (PRD)

Status legend used throughout the docs:
**[AGREED]** stated by the product owner · **[PROPOSED]** design decision awaiting approval ·
**[OPEN]** unresolved question · **[ASSUMPTION]** working assumption, not confirmed.

## 1. Problem statement [AGREED]
Driver fatigue and distraction increase accident risk. Existing solutions focus on dangerous
behavior already in progress. We want to flag risk before a shift and monitor it during the trip.

## 2. Target customers [AGREED]
Interprovincial passenger/cargo transport companies in Peru. [ASSUMPTION] Initial fleets are
small-to-mid size with a human supervisor on duty per shift.

## 3. Personas
| Persona | MVP focus | Needs |
|---|---|---|
| Professional Driver | Yes | Timely, non-intrusive alerts; privacy of camera video and health data |
| Fleet Supervisor | Yes | See who is at risk, decide on shifts, get and acknowledge alerts |
| Company Administrator | No (later) | Fleet-level reporting, user management, policy configuration |

## 4. Core user journeys
1. **Pre-shift:** sleep data arrives → assessment produced → supervisor reviews → authorizes or
   rejects → shift is authorized.
2. **In-shift:** driver monitor observes camera + telemetry → backend evaluates → alert raised →
   driver warned locally, supervisor notified.
3. **Incident follow-up:** supervisor sees alert → acknowledges incident → incident history kept.

## 5. Feature domains
1. Pre-shift risk assessment and authorization — first OpenSpec change:
   `openspec/changes/pre-shift-risk-assessment-and-authorization/`.
2. Real-time driver monitoring (not yet specified).
3. Alerts and incident management (not yet specified).

Detailed behavior belongs in OpenSpec, not here.

## 6. Functional requirements
Identifiers are stable references for OpenSpec specs.

| ID | Requirement | Status |
|---|---|---|
| FR-1 | Ingest sleep/recovery data from a pluggable source (simulator, manual, import) | AGREED |
| FR-2 | Produce an explainable pre-shift risk assessment and a recommendation (authorize / review / withhold) | AGREED |
| FR-3 | Supervisor records the final authorize/reject decision | AGREED |
| FR-4 | Explicitly show missing wearable inputs | AGREED |
| FR-5 | Capture camera frames locally and derive fatigue/distraction indicators on-device | AGREED |
| FR-6 | Ingest vehicle telemetry (speed, others when available); simulated allowed | AGREED |
| FR-7 | Combine observations into a driving-risk evaluation in the backend | AGREED |
| FR-8 | Generate alerts; notify driver (local) and supervisor (dashboard, SSE) | AGREED |
| FR-9 | Record incidents and supervisor actions (acknowledge, review) | AGREED |
| FR-10 | Supervisor can list drivers, active shifts, risk, incidents | AGREED |
| FR-11 | Label all simulated data as simulated everywhere it is shown | AGREED |
| FR-12 | Authentication and roles for supervisors | OPEN |

## 7. Non-functional requirements
- Explainable, deterministic, unit-testable risk logic [AGREED].
- Raw video never leaves the driver's device; only structured events are sent [AGREED].
- UTC timestamps; idempotent event ingestion; tolerate duplicates and reordering [PROPOSED].
- Monitor keeps working locally when the backend is unreachable [PROPOSED].
- Reproducible simulation mode usable from public URLs [AGREED].
- Data minimization: no more personal/health data than needed [AGREED].

## 8. Assumptions
- Wearable sleep indicators are imperfect estimates [AGREED].
- Real provider integrations (Garmin, Fitbit, Apple Health…) are not available for the hackathon [AGREED].
- One supervisor user type is enough for the demo [ASSUMPTION].

## 9. Constraints
Hackathon deadline (Oct 17–18, 2026, Lima); modular monolith only; no Kafka/Redis/Kubernetes;
hosting: Vercel (dashboard), Railway (API + PostgreSQL), local edge device (monitor).

## 10. Success criteria (hackathon)
The 7-step demo in [mvp.md](mvp.md) runs end-to-end from public URLs in simulation mode. We do not
claim accident reduction or clinical validity.

## 11. MVP limitations
See [mvp.md](mvp.md).

## 12. Open questions [OPEN]
1. Authentication/authorization model for supervisors (and API keys for the monitor).
2. Which sleep/recovery inputs and what risk-level boundaries are acceptable? Needs domain/legal review.
3. Do alerts to the driver require a hardware element (buzzer) or is on-screen/audio enough?
4. Retention period for events and sleep records.
5. Legal basis/consent for processing driver health and camera-derived data under Peruvian law (Ley 29733).
6. Is a Spanish-only dashboard enough, or must it be bilingual?

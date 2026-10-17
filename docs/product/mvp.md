# MVP Scope

## In scope
Demo flow (all data may be simulated, always labeled):
1. A driver has pre-shift wearable sleep data.
2. The system generates an explainable risk assessment.
3. A supervisor reviews and authorizes a shift.
4. The driver monitor generates a risk event.
5. The backend processes the event.
6. The dashboard displays an alert.
7. The supervisor acknowledges the incident.

## Out of scope (non-goals)
Real wearable provider integrations · real vehicle bus integrations · navigation/routing ·
fleet tracking · medical fitness determination · multi-tenant admin · billing · mobile apps ·
production-grade auth (until decided) · ML model training.

## Limitations to state in the demo
- Sleep indicators are estimates; assessments are decision support only.
- Risk-level boundaries are not clinically validated.
- Camera detection is a prototype and not validated for production safety use.
- Simulated inputs are used where real sources are unavailable.

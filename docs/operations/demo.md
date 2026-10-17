# Demo Plan

Goal: judges can open a public URL and see the 7-step flow without the developer's laptop.

1. Driver has pre-shift sleep data (seeded, `dataOrigin: simulated`).
2. Assessment generated.
3. Supervisor reviews and authorizes.
4. Monitor produces a risk event.
5. Backend processes it.
6. Dashboard shows the alert (via SSE).
7. Supervisor acknowledges the incident.

## Reproducible simulation [PROPOSED, not built]
A seeded scenario endpoint/script resets and replays the flow, with a "Simulation" banner in the UI.
A recorded run of the real monitor on a laptop can accompany the live public demo. Public-demo
access control is **[OPEN]**.

## Hackathon deliverables checklist
Public URL · GitHub repo · public presentation · short description (ES/EN) · reproducible demo.

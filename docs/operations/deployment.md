# Deployment (planned, not performed)

Targets (ADR-0005): Dashboard → Vercel (root `apps/dashboard`, env `NEXT_PUBLIC_API_BASE_URL`).
API → Railway (root `apps/api`, env `DATABASE_URL`, `API_PORT`, `SIMULATION_MODE`, `CORS_ALLOWED_ORIGIN`).
PostgreSQL → Railway managed. Monitor → local edge device, `API_BASE_URL` pointing at the public API.

Nothing has been deployed or provisioned. Before deploying: decide auth (PRD open question 1),
add migrations runner, set production CORS origin, never reuse local `.env` values.

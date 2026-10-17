# dashboard — agent notes

Scope: `apps/dashboard/` only. Next.js (App Router), TypeScript strict, Tailwind, pnpm. Commands: `make lint-dashboard test-dashboard build-dashboard dashboard`. Next.js APIs change quickly: check the current docs (`npx ctx7@latest`) before using unfamiliar APIs.

- **Contract-driven.** All data comes through `src/lib/api/` typed against `contracts/openapi.yaml`. Never invent response shapes or mock fields that the contract lacks.
- **Type safety.** No `any`; handle loading, empty, and error states; the API may be unavailable.
- **Supervisor workflows:** drivers → assessment → authorize/reject (reason when overriding) → live shifts → alerts → acknowledge. UI never computes risk; it renders API output, including `factors` and `missingInputs`.
- **Simulation clarity.** Show a persistent indicator when `simulationMode` or `dataOrigin != real`; label simulated rows. Show the assessment disclaimer (decision support, not medical).
- **Realtime:** SSE via `EventSource` to `/v1/alerts/stream`; reconnect and re-fetch on reconnect.
- **Accessibility:** semantic HTML, keyboard operable, never color-only risk signals, sensible aria labels. UI copy in Spanish.
- Config via `NEXT_PUBLIC_*` env only; no secrets in client code.

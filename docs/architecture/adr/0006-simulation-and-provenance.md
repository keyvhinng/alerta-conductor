# ADR-0006: Explicit simulation and data provenance
- Status: Proposed
- Decision: Every ingestible/derivable record carries `dataOrigin` (real | simulated | imported | manual). The API exposes `simulationMode`; the dashboard shows a persistent simulation indicator. Simulators live behind the same interfaces as real sources (`integrations/` in API, `inputs/` in monitor).
- Consequences: Real integrations can replace simulators without changing domain code; demo data can never be mistaken for real data.

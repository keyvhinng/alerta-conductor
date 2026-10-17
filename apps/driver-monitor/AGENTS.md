# driver-monitor — agent notes
Scope: `apps/driver-monitor/` only. Python 3.12, uv, pytest, ruff. Commands: `make test-monitor`, `make lint-monitor`, `make monitor`.

- **Local inference only.** Pipeline (`pipeline/`) must not import cloud/HTTP code; sinks (`sinks/`) deliver events.
- **Mockable hardware.** Camera and telemetry sit behind Protocols in `inputs/`; every real adapter needs a mock. Tests never need a webcam.
- **Observe, don't decide.** Emit indicators/observations; risk decisions belong to the API.
- **Structured events** follow `contracts/events/monitoring-event.schema.json`: `eventId`, per-shift monotonic `sequence`, UTC `occurredAt`, `simulated` flag. Missing telemetry is `None`, never 0.
- **Privacy.** Never persist or transmit frames/video; no face identification. Don't log pixel data.
- **Deterministic tests.** Fixed synthetic frames/seeds; inject clocks and ids; no network, no sleep.
- Detection algorithms need an approved OpenSpec change; thresholds come from config, not hard-coded claims.

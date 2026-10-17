# ADR-0004: Server-Sent Events for dashboard notifications
- Status: Accepted (product owner brief)
- Decision: One-way push over SSE (`GET /v1/alerts/stream`); supervisor actions use normal HTTP requests. No WebSockets, brokers, or Redis. Single API instance assumed, so in-process fan-out suffices.
- Consequences: Horizontal scaling would need a shared fan-out mechanism (revisit only if required). Clients reconnect with `Last-Event-ID`; the dashboard re-fetches on reconnect.

# ADR-0003: Contract-first APIs
- Status: Accepted
- Decision: `contracts/openapi.yaml` (HTTP, `/v1`) and `contracts/events/*.schema.json` (monitor events) are the source of truth. Behavior changes update contracts in the same change. The dashboard consumes types derived from/mirroring the contract; no invented responses.
- Consequences: `make contracts-lint` runs in CI. Automated generation of TS types and Go/Python conformance tests are follow-ups.

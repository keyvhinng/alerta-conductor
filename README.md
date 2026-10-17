# Alerta Conductor

Preventive safety platform for professional drivers (interprovincial transport, Peru) built for
**Hack the Andes 2026** (Lima, Oct 17–18). *Plataforma preventiva: evalúa el riesgo de fatiga
**antes** del turno y monitorea fatiga/distracción **durante** el viaje; el supervisor decide.*

It is decision support, **not** a medical device, navigation app, or fleet tracker. Wearable sleep
data is an imperfect estimate; risk thresholds are not yet approved; simulated data is always labeled.

> Status: **bootstrap**. Skeletons, contracts, docs and one OpenSpec proposal exist. Business
> functionality is not implemented.

## Architecture
```
Wearable/sleep data ─▶ API (Go) ─▶ risk assessment ─▶ Dashboard ─▶ supervisor decision ─▶ authorized shift
Camera + telemetry ─▶ Driver Monitor (Python, edge) ─▶ API ─▶ PostgreSQL + risk processing ─▶ SSE alert ─▶ Dashboard
```
The monitor observes, the API decides, the dashboard presents. Raw video never leaves the device.
Details: [docs/architecture/overview.md](docs/architecture/overview.md).

## Stack
| App | Path | Tech |
|---|---|---|
| Driver monitor | `apps/driver-monitor` | Python 3.12, OpenCV, MediaPipe, NumPy, uv, pytest, ruff |
| API | `apps/api` | Go 1.25, chi, PostgreSQL (pgx to be added), SSE |
| Dashboard | `apps/dashboard` | Next.js 16, React 19, TypeScript, Tailwind 4, pnpm |
| Infra | `infra/` | Docker Compose (PostgreSQL). Planned: Vercel, Railway (not deployed) |

## Repository structure
```
AGENTS.md            agent rules (each app has its own AGENTS.md)
apps/                driver-monitor/ · api/ · dashboard/
contracts/           openapi.yaml · events/*.schema.json
docs/                product/ · architecture/ (+adr/) · domain/ · operations/
openspec/            specs/ · changes/ · config.yaml   (OpenSpec)
infra/               docker-compose.yml
tests/fixtures/      shared simulated fixtures
```
Documentation hierarchy: product → architecture → OpenSpec feature specs → contracts → implementation.

## Prerequisites
Go ≥ 1.25, Node ≥ 20, pnpm, uv, Docker (with Compose), make. Optional: OpenSpec CLI
(`npm install -g @fission-ai/openspec@latest`).

## Local setup
```bash
cp .env.example .env
make setup          # go mod download, uv sync, pnpm install
make db-up          # PostgreSQL (the bootstrap API does not use it yet)
```

## Run
```bash
make api            # http://localhost:8080/v1/health
make dashboard      # http://localhost:3000
make monitor        # mock camera + telemetry -> JSON events on stdout (simulated)
```

## Test and check
```bash
make test           # API, monitor, dashboard tests
make lint           # gofmt/go vet, ruff, eslint/tsc/prettier
make build-dashboard
make compose-check
make contracts-lint # OpenAPI lint (uses npx, needs network)
make check          # lint + test + build + compose check
```
`make help` lists everything.

## Specifications
- Product: `docs/product/` · Architecture/ADRs: `docs/architecture/` · Domain rules: `docs/domain/`
- Feature specs and proposals: `openspec/` (first proposal:
  `openspec/changes/pre-shift-risk-assessment-and-authorization/`)
- API/event contracts: `contracts/` (draft; only `GET /v1/health` is implemented)

## Proposing a new feature
1. Read `AGENTS.md` and the relevant docs. 2. Run `/opsx:propose "<idea>"` (Claude Code) or
`openspec new change <name>`. 3. Fill proposal, specs (GIVEN/WHEN/THEN), design, tasks; run
`openspec validate <name>`. 4. Get human review. 5. Implement with `/opsx:apply`, update contracts
and docs, then `/opsx:archive`.

## Demo
See [docs/operations/demo.md](docs/operations/demo.md). Hosting (Vercel/Railway) is planned, not performed.

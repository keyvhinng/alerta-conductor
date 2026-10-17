# Alerta Conductor - developer entry points. Run `make help`.
SHELL := /bin/bash
.DEFAULT_GOAL := help

.PHONY: help setup db-up db-down api dashboard monitor \
	test test-api test-monitor test-dashboard lint lint-api lint-monitor lint-dashboard \
	build-dashboard contracts-lint compose-check check

help: ## Show targets
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk -F':.*?## ' '{printf "  %-18s %s\n", $$1, $$2}'

setup: ## Install dependencies for all apps
	cd apps/api && go mod download
	cd apps/driver-monitor && uv sync
	cd apps/dashboard && pnpm install

db-up: ## Start local PostgreSQL
	docker compose -f infra/docker-compose.yml --env-file .env up -d postgres

db-down: ## Stop local PostgreSQL
	docker compose -f infra/docker-compose.yml --env-file .env down

api: ## Run the Go API (loads .env)
	set -a; [ -f .env ] && . ./.env; set +a; cd apps/api && go run ./cmd/api

dashboard: ## Run the Next.js dashboard
	cd apps/dashboard && pnpm dev

monitor: ## Run the driver monitor with mock inputs
	cd apps/driver-monitor && uv run python -m driver_monitor.main

test: test-api test-monitor test-dashboard ## Run all tests
test-api:
	cd apps/api && go test ./...
test-monitor:
	cd apps/driver-monitor && uv run pytest -q
test-dashboard:
	cd apps/dashboard && pnpm test

lint: lint-api lint-monitor lint-dashboard ## Lint and format-check all apps
lint-api:
	cd apps/api && test -z "$$(gofmt -l .)" && go vet ./...
lint-monitor:
	cd apps/driver-monitor && uv run ruff check . && uv run ruff format --check .
lint-dashboard:
	cd apps/dashboard && pnpm lint && pnpm typecheck && pnpm format:check

build-dashboard: ## Production build of the dashboard
	cd apps/dashboard && pnpm build

contracts-lint: ## Validate OpenAPI contract
	npx --yes @redocly/cli@latest lint contracts/openapi.yaml

compose-check: ## Validate docker compose config
	docker compose -f infra/docker-compose.yml config -q

check: lint test build-dashboard compose-check ## Everything CI runs (except contracts-lint)

// Package internal holds the API modular monolith.
//
// Each domain package (drivers, shifts, wearables, assessments, monitoring,
// alerts, incidents) owns its domain logic, persistence and HTTP handlers.
// Domain logic must not import net/http or pgx. integrations/ holds adapters
// to external sources (e.g. wearable providers). platform/ holds shared
// infrastructure. See docs/architecture/overview.md.
package internal

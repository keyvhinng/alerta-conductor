// Package health exposes liveness information.
package health

import (
	"encoding/json"
	"net/http"
	"time"
)

// Response is the body of GET /v1/health. Mirrors contracts/openapi.yaml.
type Response struct {
	Status         string    `json:"status"`
	Service        string    `json:"service"`
	SimulationMode bool      `json:"simulationMode"`
	Time           time.Time `json:"time"`
}

// Handler returns the health handler.
func Handler(simulation bool, now func() time.Time) http.HandlerFunc {
	return func(w http.ResponseWriter, _ *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		_ = json.NewEncoder(w).Encode(Response{
			Status: "ok", Service: "alerta-conductor-api",
			SimulationMode: simulation, Time: now().UTC(),
		})
	}
}

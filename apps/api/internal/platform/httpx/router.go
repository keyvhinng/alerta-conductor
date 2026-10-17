// Package httpx wires transport-level concerns (routing, middleware).
package httpx

import (
	"net/http"
	"time"

	"github.com/alerta-conductor/api/internal/config"
	"github.com/alerta-conductor/api/internal/health"
	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
)

// NewRouter builds the HTTP router. Domain routers mount under /v1.
func NewRouter(cfg config.Config) http.Handler {
	r := chi.NewRouter()
	r.Use(middleware.RequestID, middleware.Recoverer)
	r.Use(cors(cfg.CORSOrigin))
	r.Route("/v1", func(r chi.Router) {
		r.Get("/health", health.Handler(cfg.SimulationMode, time.Now))
	})
	return r
}

func cors(origin string) func(http.Handler) http.Handler {
	return func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, req *http.Request) {
			if origin != "" {
				w.Header().Set("Access-Control-Allow-Origin", origin)
				w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Idempotency-Key")
				w.Header().Set("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
			}
			if req.Method == http.MethodOptions {
				w.WriteHeader(http.StatusNoContent)
				return
			}
			next.ServeHTTP(w, req)
		})
	}
}

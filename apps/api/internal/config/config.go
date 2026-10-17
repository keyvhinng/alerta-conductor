// Package config loads runtime configuration from environment variables.
package config

import (
	"fmt"
	"strconv"
)

// Config holds API runtime settings.
type Config struct {
	Port           int
	DatabaseURL    string
	SimulationMode bool
	CORSOrigin     string
}

// Addr returns the listen address.
func (c Config) Addr() string { return fmt.Sprintf(":%d", c.Port) }

// Load reads configuration using getenv (injectable for tests).
func Load(getenv func(string) string) (Config, error) {
	cfg := Config{
		Port:           8080,
		DatabaseURL:    getenv("DATABASE_URL"),
		SimulationMode: getenv("SIMULATION_MODE") != "false",
		CORSOrigin:     getenv("CORS_ALLOWED_ORIGIN"),
	}
	if v := getenv("API_PORT"); v != "" {
		p, err := strconv.Atoi(v)
		if err != nil || p < 1 || p > 65535 {
			return Config{}, fmt.Errorf("API_PORT %q is not a valid port", v)
		}
		cfg.Port = p
	}
	return cfg, nil
}

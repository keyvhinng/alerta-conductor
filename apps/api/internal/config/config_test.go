package config

import "testing"

func env(m map[string]string) func(string) string { return func(k string) string { return m[k] } }

func TestLoadDefaults(t *testing.T) {
	cfg, err := Load(env(nil))
	if err != nil {
		t.Fatal(err)
	}
	if cfg.Port != 8080 || !cfg.SimulationMode {
		t.Fatalf("unexpected defaults: %+v", cfg)
	}
}

func TestLoadInvalidPort(t *testing.T) {
	if _, err := Load(env(map[string]string{"API_PORT": "abc"})); err == nil {
		t.Fatal("expected error for invalid port")
	}
}

func TestSimulationModeCanBeDisabled(t *testing.T) {
	cfg, _ := Load(env(map[string]string{"SIMULATION_MODE": "false"}))
	if cfg.SimulationMode {
		t.Fatal("expected simulation mode off")
	}
}

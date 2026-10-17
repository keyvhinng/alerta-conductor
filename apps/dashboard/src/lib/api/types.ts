// Hand-written for bootstrap; mirrors contracts/openapi.yaml.
// Replace with generated types (openapi-typescript) when the first feature lands.
export interface HealthResponse {
  status: "ok";
  service: string;
  simulationMode: boolean;
  time: string;
}

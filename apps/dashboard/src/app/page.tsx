import { api } from "@/lib/api/client";
import type { HealthResponse } from "@/lib/api/types";

export const dynamic = "force-dynamic";

async function loadHealth(): Promise<HealthResponse | null> {
  try {
    return await api.health();
  } catch {
    return null;
  }
}

export default async function Home() {
  const health = await loadHealth();
  return (
    <main className="mx-auto max-w-3xl p-8">
      <h1 className="text-3xl font-semibold">Alerta Conductor</h1>
      <p className="mt-2 text-slate-600">
        Seguridad preventiva para conductores profesionales: evaluación antes del turno y monitoreo
        durante el viaje.
      </p>
      <section
        className="mt-8 rounded-lg border border-slate-200 bg-white p-4"
        aria-label="Estado de la API"
      >
        <h2 className="font-medium">Estado de la API</h2>
        {health ? (
          <p className="mt-1 text-sm">
            {health.service}: {health.status}
            {health.simulationMode && (
              <span className="ml-2 rounded bg-amber-100 px-2 py-0.5 text-amber-900">
                MODO SIMULACIÓN
              </span>
            )}
          </p>
        ) : (
          <p className="mt-1 text-sm text-red-700">API no disponible</p>
        )}
      </section>
      <p className="mt-6 text-xs text-slate-500">
        Placeholder de bootstrap. Las pantallas del supervisor se especifican con OpenSpec.
      </p>
    </main>
  );
}

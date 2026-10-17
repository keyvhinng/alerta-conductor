import { afterEach, expect, it, vi } from "vitest";
import { api } from "./client";

afterEach(() => vi.unstubAllGlobals());

it("fetches health from /v1/health", async () => {
  const body = { status: "ok", service: "s", simulationMode: true, time: "2026-01-01T00:00:00Z" };
  const fetchMock = vi.fn().mockResolvedValue({ ok: true, json: async () => body });
  vi.stubGlobal("fetch", fetchMock);
  await expect(api.health()).resolves.toEqual(body);
  expect(fetchMock.mock.calls[0][0]).toMatch(/\/v1\/health$/);
});

it("throws on non-2xx", async () => {
  vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ ok: false, status: 500 }));
  await expect(api.health()).rejects.toThrow("500");
});

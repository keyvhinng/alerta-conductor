"""Vehicle telemetry abstraction. Real adapters (OBD-II, CAN, GPS) come later."""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class TelemetrySample:
    speed_kmh: float | None  # None = unavailable (must not be treated as 0)
    simulated: bool


class TelemetrySource(Protocol):
    def samples(self) -> Iterator[TelemetrySample]: ...


class MockTelemetry:
    """Fixed-profile simulated telemetry. Always flagged simulated=True."""

    def __init__(self, speeds_kmh: list[float | None] | None = None) -> None:
        self._speeds = speeds_kmh if speeds_kmh is not None else [0.0, 40.0, 80.0]

    def samples(self) -> Iterator[TelemetrySample]:
        for s in self._speeds:
            yield TelemetrySample(speed_kmh=s, simulated=True)

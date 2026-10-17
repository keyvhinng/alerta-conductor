from __future__ import annotations

import json
from typing import Protocol

from driver_monitor.events import MonitoringEvent


class EventSink(Protocol):
    def emit(self, event: MonitoringEvent) -> None: ...


class StdoutSink:
    """Prints events as JSON lines. HTTP sink to the API comes with its OpenSpec change."""

    def emit(self, event: MonitoringEvent) -> None:
        print(json.dumps(event.to_dict()))


class ListSink:
    def __init__(self) -> None:
        self.events: list[MonitoringEvent] = []

    def emit(self, event: MonitoringEvent) -> None:
        self.events.append(event)

"""Structured monitoring events. Must stay in sync with contracts/events/."""

from __future__ import annotations

import uuid
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime


@dataclass(frozen=True)
class MonitoringEvent:
    shift_id: str
    kind: str  # e.g. "heartbeat"; fatigue/distraction kinds are defined in the contract
    sequence: int  # monotonically increasing per shift, for ordering + dedup
    source: str  # "mock" | "camera"
    simulated: bool
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    occurred_at: str = field(default_factory=lambda: datetime.now(UTC).isoformat())

    def to_dict(self) -> dict:
        return asdict(self)

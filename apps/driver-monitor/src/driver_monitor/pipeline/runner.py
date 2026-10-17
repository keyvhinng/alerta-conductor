"""Skeleton pipeline: consumes inputs, emits heartbeat events.

No fatigue/distraction detection yet; that is a separate OpenSpec change.
"""

from __future__ import annotations

from driver_monitor.events import MonitoringEvent
from driver_monitor.inputs.camera import FrameSource
from driver_monitor.inputs.telemetry import TelemetrySource
from driver_monitor.sinks.base import EventSink


def run(shift_id: str, camera: FrameSource, telemetry: TelemetrySource, sink: EventSink) -> int:
    """Emit one heartbeat per camera frame. Returns the number of events emitted."""
    samples = telemetry.samples()
    seq = 0
    for _frame in camera.frames():
        next(samples, None)  # telemetry may be shorter/unavailable; never blocks the camera
        seq += 1
        sink.emit(
            MonitoringEvent(
                shift_id=shift_id, kind="heartbeat", sequence=seq, source="mock", simulated=True
            )
        )
    return seq

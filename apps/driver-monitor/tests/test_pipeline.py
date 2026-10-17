from driver_monitor.inputs.camera import MockCamera
from driver_monitor.inputs.telemetry import MockTelemetry
from driver_monitor.pipeline.runner import run
from driver_monitor.sinks.base import ListSink


def test_emits_one_ordered_simulated_event_per_frame():
    sink = ListSink()
    n = run("s1", MockCamera(count=4), MockTelemetry(), sink)
    assert n == 4
    assert [e.sequence for e in sink.events] == [1, 2, 3, 4]
    assert all(e.simulated and e.shift_id == "s1" for e in sink.events)
    assert len({e.event_id for e in sink.events}) == 4


def test_missing_telemetry_does_not_block_camera():
    sink = ListSink()
    assert run("s1", MockCamera(count=3), MockTelemetry(speeds_kmh=[]), sink) == 3

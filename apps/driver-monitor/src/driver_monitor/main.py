from __future__ import annotations

import argparse

from driver_monitor.inputs.camera import MockCamera
from driver_monitor.inputs.telemetry import MockTelemetry
from driver_monitor.pipeline.runner import run
from driver_monitor.sinks.base import StdoutSink


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="driver-monitor")
    p.add_argument("--shift-id", default="shift-simulated-001")
    args = p.parse_args(argv)
    n = run(args.shift_id, MockCamera(), MockTelemetry(), StdoutSink())
    print(f"emitted {n} simulated events")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

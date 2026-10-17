# ADR-0002: Edge inference; raw video never leaves the device
- Status: Accepted (product owner brief)
- Decision: Computer vision runs in the Python driver monitor on the driver's device. Only structured events are sent. The monitor produces observations; the backend owns decisions.
- Consequences: Lower bandwidth and privacy exposure; backend rules operate on coarse indicators; pipeline must be testable with mock camera input.

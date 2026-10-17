# Risk Assessment (domain)

Status: **[PROPOSED]** structure; **[OPEN]** thresholds.

## Principles
- Decision support only. Output is never described as medical fitness to drive.
- Explainable: every result lists the factors and inputs that produced it.
- Deterministic and unit-testable: pure functions of (inputs, configuration, algorithmVersion).
- Missing data is explicit: absent inputs appear in `missingInputs`; if too little data exists the
  level is `insufficient_data` and the recommendation is `review`, never `authorize` by default.
- Every assessment records `algorithmVersion` and `dataOrigin`.

## Pre-shift inputs (candidate)
Total sleep minutes in a recent window, awake minutes during sleep, resting heart rate (optional),
recency of the last record. Which inputs matter is **[OPEN]**.

## Thresholds
**Not approved.** No production safety thresholds exist in this repository. Level boundaries are
configuration (`RiskConfig`), supplied by an approved change. Demo/test values must be labeled
`simulated-demo-config` and must not be presented as validated.

## Outputs
`level` (low | moderate | high | insufficient_data), `recommendation` (authorize | review | withhold),
`factors[]`, `missingInputs[]`, `algorithmVersion`, `computedAt`, `dataOrigin`, fixed disclaimer.
Recommendation is advisory: the supervisor may override with a recorded reason.

## In-shift risk
Backend combines monitoring events (and telemetry such as speed) into alert decisions. Rules and
their configuration are specified in a later OpenSpec change. The monitor never decides.

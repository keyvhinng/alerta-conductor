## ADDED Requirements

### Requirement: Explainable assessment
The system SHALL compute a pre-shift assessment containing `level`, `recommendation`, `factors`, `missingInputs`, `algorithmVersion`, `computedAt`, `dataOrigin`, and a fixed decision-support disclaimer.

#### Scenario: Assessment from available data
- **GIVEN** a shift in `pending_assessment` and a driver with sleep records in the lookback window
- **WHEN** an assessment is requested
- **THEN** the response lists the factors that produced the level
- **AND** the shift moves to `awaiting_decision`

### Requirement: Missing data is explicit
The system SHALL list unavailable inputs in `missingInputs` and SHALL NOT treat missing data as favorable.

#### Scenario: No sleep data
- **GIVEN** a driver with no sleep records in the lookback window
- **WHEN** an assessment is requested
- **THEN** `level = insufficient_data`, `recommendation = review`, and `missingInputs` names the absent inputs

### Requirement: Deterministic and versioned
The system SHALL produce identical output for identical inputs, configuration, and algorithm version, and SHALL persist each assessment immutably.

#### Scenario: Recompute
- **WHEN** new sleep data arrives and the assessment is recomputed
- **THEN** a new assessment is stored; the previous one remains readable

### Requirement: Configuration-driven boundaries, no unapproved claims
Risk-level boundaries SHALL come from configuration labeled with its approval status, and the system SHALL NOT present results as a medical determination of fitness to drive.

#### Scenario: Demo configuration
- **WHEN** assessments use the unapproved demo configuration
- **THEN** the response and UI identify it as a simulated/demo configuration

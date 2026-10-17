## ADDED Requirements

### Requirement: Shift planning
The system SHALL create planned shifts in `pending_assessment` for an existing driver and vehicle.

#### Scenario: Plan a shift
- **WHEN** a supervisor plans a shift for a registered driver
- **THEN** the shift exists in `pending_assessment`

### Requirement: Supervisor decision is final
The system SHALL allow only a supervisor decision to move a shift from `awaiting_decision` to `authorized` or `rejected`, recording actor, UTC time, and reason.

#### Scenario: Authorize after review
- **GIVEN** a shift in `awaiting_decision` with recommendation `authorize`
- **WHEN** the supervisor authorizes it
- **THEN** the shift becomes `authorized` and the decision is recorded

#### Scenario: Override a withhold recommendation
- **GIVEN** recommendation `withhold`
- **WHEN** the supervisor authorizes without a reason
- **THEN** the system responds 400 `validation_failed`
- **AND** with a reason the system authorizes and records that the recommendation was overridden

#### Scenario: Assessment never auto-authorizes
- **WHEN** an assessment with recommendation `authorize` is computed
- **THEN** the shift remains `awaiting_decision`

### Requirement: Invalid transitions rejected
The system SHALL reject transitions not listed in `docs/domain/shift-lifecycle.md` with 409 `invalid_transition` and leave state unchanged.

#### Scenario: Decide before assessment
- **GIVEN** a shift in `pending_assessment`
- **WHEN** a decision is submitted
- **THEN** the system responds 409 `invalid_transition`

#### Scenario: Re-decide
- **GIVEN** a shift in `rejected`
- **WHEN** an authorize decision is submitted
- **THEN** the system responds 409 and the shift stays `rejected`

### Requirement: Supervisor review UI
The dashboard SHALL show drivers, the latest assessment with factors, missing inputs, disclaimer, and simulation labels, and SHALL provide authorize/reject actions.

#### Scenario: Simulated data visible
- **WHEN** an assessment's `dataOrigin` is not `real`
- **THEN** the dashboard displays a visible simulation label next to it

## ADDED Requirements

### Requirement: Ingest sleep records with provenance
The system SHALL accept sleep/recovery records for a driver and store each with its data origin (`real`, `simulated`, `imported`, or `manual`) and provider label.

#### Scenario: Simulated record accepted
- **GIVEN** a registered driver
- **WHEN** a batch with one record marked `simulated` is submitted
- **THEN** the system responds 202 with `accepted = 1, duplicates = 0`
- **AND** the stored record keeps `dataOrigin = simulated`

#### Scenario: Record without provenance rejected
- **WHEN** a record omits `dataOrigin`
- **THEN** the system responds 400 with code `validation_failed` and stores nothing

### Requirement: Idempotent ingestion
The system SHALL treat `(driver, sourceRecordId)` as an idempotency key.

#### Scenario: Duplicate delivery
- **GIVEN** a record with `sourceRecordId = X` was already stored
- **WHEN** the same record is submitted again
- **THEN** the response reports `duplicates = 1` and no second record exists

### Requirement: Validate record plausibility structurally
The system SHALL reject records whose end precedes start or that contain negative durations, and SHALL accept records with absent optional measurements without substituting values.

#### Scenario: Optional measurement missing
- **WHEN** a record omits `restingHeartRateBpm`
- **THEN** it is stored with that field null

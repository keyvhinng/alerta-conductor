# Privacy & Safety Assumptions

Status: working assumptions, not legal advice. Legal review is **[OPEN]** (Peru: Ley 29733).

1. **Raw video stays on the driver's device.** Frames are processed in memory and not persisted or
   transmitted. Only structured events (kind, time, value, confidence) leave the device.
2. **Data minimization.** Collect only the sleep fields needed for assessment; no location history,
   no names beyond a display name, no biometrics templates (no face recognition/identification).
3. **Health data is sensitive.** Sleep records are stored per driver, shown only to supervisors of
   that company, never committed to the repo, and excluded from logs.
4. **Provenance.** Every record carries `dataOrigin` (real | simulated | imported | manual).
   Simulated data is visibly labeled in the UI and in demo materials.
5. **No medical claims.** Outputs are decision support based on imperfect estimates.
6. **No unproven claims** of accident reduction.
7. **Missing data is shown**, not hidden or defaulted.
8. **Retention** period is undecided **[OPEN]**; until decided, demo data only.
9. Consent and transparency toward drivers (what is collected, who sees it) must be defined
   before any real-driver pilot **[OPEN]**.

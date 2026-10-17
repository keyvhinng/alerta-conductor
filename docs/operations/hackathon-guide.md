# Hackathon Guide (Hack the Andes 2026)

Summary of https://hacktheandes.com/guide, fetched 2026-10-17. The organizers' page is authoritative;
re-check it if anything here looks stale. Presentation hours were not published (TBA).

## Event
In-person, Lima, 17–18 October 2026. "100 personas, 30 horas, una entrega funcionando."

## Team and track
- Teams of 1–4; all members have equal permission to post updates and edit the submission.
- Our team **Anti** is registered under **Movilidad y Transporte** (`transport`), verified with `andes project` on 2026-10-17 (track set by Keyvhinng at 16:04 UTC). 12 teams per track, 36 total.
- Track selection is opened by the organizers; all current members must be checked in to choose or change it.
- CLI: `andes team create|invite|accept|leave|track`.

## Check-in and credits
- Show the QR from `andes checkin` to an organizer; check-in counts only after identity is verified.
- `CHECKIN_REQUIRED` means ask an organizer to confirm arrival.
- `andes credits` lists sponsor benefits (not redeemed automatically). Never publish codes in logs or descriptions.

## Progress updates
Post after key decisions, user tests, working demos, or blockers:
`andes project update --message "..."` or `--file ./avance.md`; `andes project updates` shows the log.
Updates are stored for review; no reply is guaranteed.

## Submission (required)
1. Deployment URL of the working app
2. Presentation URL (Canva, Google Slides, or code-based)
3. GitHub repository URL (https://github.com/keyvhinng/alerta-conductor)
4. Markdown description: problem, target users, how it works, limitations

Submit early and correct later; omitted fields keep saved values: `andes project submit` with URL flags and
`--description` or `--file`. Test the app and presentation in a private window, signed out, with no pending
permissions and no local files.

## Presentation
3 min pitch + 2 min questions, presented from the submitted links on the organizers' computer (not our laptop).
Structure: problem, people affected, working solution, evidence, technical decisions, limitations, what is still an idea.

## Judging
Each juror scores 1–5 (whole numbers) per criterion:

| Criterion | Weight | Based on |
|---|---|---|
| Traction | 30% | External evidence: user tests, interviews, real usage |
| Technical effort | 40% | Functionality, technical decisions, complex problems (AI use not penalized) |
| Pitch | 30% | Clarity of problem, solution, demo; precision in answers |

Juror score (of 100) = traction × 6 + technical × 8 + pitch × 6. Team score = average of submitted
evaluations; pending ones are not counted as zero. The jury sees a snapshot taken when evaluation opens;
later changes do not update it.

## Public gallery and privacy
Descriptions, links, and update logs (with author names and dates) may be shown in the public gallery.
Include no keys, tokens, personal user data, or material we lack permission to share. This aligns with
`docs/domain/privacy.md`.

## Implications for this project
- Traction is 30%: capture real user evidence (driver/supervisor interviews, tests) and log it via `andes project update`. Do not fabricate it (AGENTS.md rule 9).
- The public demo must run without our laptop; see `demo.md` and `deployment.md` (deployment is still planned, not performed).
- Description must state limitations: decision support, not a medical device; no accident-reduction claims.
- Pitch/UI text in Spanish, per project conventions.

# ADR-0005: Planned hosting
- Status: Accepted as a planning decision; **no deployment is authorized yet**
- Decision: Dashboard on Vercel; API and PostgreSQL on Railway; driver monitor on a local edge device. Judges must reach the demo via public URLs in simulation mode, without access to the developer laptop.
- Consequences: The monitor must be able to post to a public API URL, and the demo needs a server-side or scripted simulation path so judges need not run the monitor. Authentication for that path is an open question.

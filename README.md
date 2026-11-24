# Service Desk Simulator

A training simulator for WordPress and Shopify support work. Work through a queue of realistic client tickets: read the client as SMS-style texts, inspect evidence in tool tabs (Site check, Logs, Admin, Code, DNS & mail), triage, diagnose, pick the first fix and text a reply.

Live version (Safari / phone): https://alexmciver.github.io/service-desk-simulator/

Edit on phone: open https://github.com/alexmciver/service-desk-simulator/edit/main/index.html in Safari, change the file, then **Commit changes**.

## How it works

- **Scoring (out of 25):** key detail 3, priority 2, billing 2, checked the right tool 2, diagnosis 4, first fix 4, client reply 8.
- **Reply marking:** self-mark against eight checks: picked up the buried detail, plain English, professional tone, explains the cause, next steps, billing handled, safe practice, keeps hosting details private.
- **Tickets:** six built-in scenarios. When the queue is clear, replay them (answers are reshuffled).
- **Progress:** UK career path with salary bands — First line support (10, £22–28k), Experienced agent (50, £28–35k), Senior / specialist (150, £35–45k), Team lead (400, £45–55k), Head of support (1,000, £55–75k). Title jumps at ticket thresholds; the midpoint within the band drifts with average score and streak. Per-area skill bars and daily streak included.
- **Phones:** one-focus screens for iPhone Safari — queue → ticket → tools → triage/reply → score — with a step rail, sticky primary actions, and ticket details tucked behind a sheet. Desktop keeps the three-column workbench.

## Running locally

Open `index.html` in a browser (or AirDrop / Files it onto your phone). Fully offline: built-in tickets, self-marking, and progress saved in localStorage.

## Files

- `index.html`: the whole app (HTML, CSS, JS and the built-in ticket bank).

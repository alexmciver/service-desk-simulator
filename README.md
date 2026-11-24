# Service Desk Simulator

A training simulator for WordPress and Shopify support work. Work through a queue of realistic client tickets: inspect the evidence in tool tabs (Site check, Logs, Admin, Code, DNS & mail), ask the client follow-up questions, triage, diagnose, pick the first fix and write the client reply.

Live version: https://claude.ai/artifact/3B4w4NWJtegPXDxVXTNvKT

## How it works

- **Scoring (out of 25):** key detail 3, priority 2, billing 2, checked the right tool 2, diagnosis 4, first fix 4, client reply 8.
- **Reply marking:** eight checks: picked up the buried detail, plain English, professional tone, explains the cause, next steps, billing handled, safe practice, keeps hosting details private.
- **Unlimited tickets:** on claude.ai, Claude writes new tickets aimed at your weakest skill area, getting harder as you resolve more.
- **Progress:** certificates from First line support (10 tickets) to Head of support (1,000), per-area skill bars, average score and daily streak.

## Running locally

Open `index.html` in a browser. Without the claude.ai runtime it runs in offline mode: the six built-in tickets, self-marking, and progress saved in localStorage.

## Files

- `index.html`: the whole app (HTML, CSS, JS and the built-in ticket bank).

# Service Desk Simulator

A training simulator for WordPress and Shopify support work. Work a mixed queue like a real shift: **desk email**, **live chat** and **phone calls**. Inspect evidence in tool tabs (Site check, Logs, Admin, Code, DNS & mail), triage, diagnose, pick the first fix and reply in that channel’s voice.

Live version (Safari / phone): https://alexmciver.github.io/service-desk-simulator/

Edit on phone: open https://github.com/alexmciver/service-desk-simulator/edit/main/index.html in Safari, change the file, then **Commit changes**.

## How it works

- **Channels:** each ticket is Desk (email), Live chat or Phone call. Same tools and scoring; the contact surface and reply style change.
- **Scoring (out of 25):** key detail 3, priority 2, billing 2, checked the right tool 2, diagnosis 4, first fix 4, client reply 8.
- **Reply marking:** self-mark against eight checks, then a short “lock it in” gate when you missed something.
- **Practice loop:** twelve built-in tickets. **Today’s practice** pulls due revisits first, then unseen tickets, then your weakest skill area. Misses come back after 1 / 3 / 7 days by score.
- **Progress:** UK career path with salary bands — First line support (10, £22–28k), Experienced agent (50, £28–35k), Senior / specialist (150, £35–45k), Team lead (400, £45–55k), Head of support (1,000, £55–75k). Title jumps at ticket thresholds; the midpoint within the band drifts with average score and streak.
- **Phones:** mobile-first layout for iPhone Safari (viewport + safe-area, sticky ticket context, one primary action).

## Running locally

Open `index.html` in a browser (or AirDrop / Files it onto your phone). Fully offline: built-in tickets, scripted client answers on chat/call, self-marking, and progress in localStorage.

## Files

- `index.html`: the whole app (HTML, CSS, JS and the built-in ticket bank).

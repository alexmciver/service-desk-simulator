#!/usr/bin/env python3
"""Assemble index.html for Service Desk Simulator."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent
css = (ROOT / "_parts" / "app.css").read_text(encoding="utf-8")
js = (ROOT / "_parts" / "app.js").read_text(encoding="utf-8")
html = f"""<!DOCTYPE html>
<html lang="en-GB"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="theme-color" content="#0b4f8a">
<title>Service Desk Simulator</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,400;7..72,600;7..72,700&display=optional" rel="stylesheet">
<style>
{css}
</style></head><body data-panel="work">
<header class="band" id="hdr">
  <div><h1>Service Desk Simulator</h1><p>Offline desk · unlimited tickets · iPhone ready.</p></div>
</header>
<main>
  <section class="queue" aria-label="Ticket queue"><h2 id="qh">Queue</h2><div id="qlist"><p class="empty">Loading…</p></div><div class="gen" id="gen"></div></section>
  <section class="work" id="work" aria-label="Ticket"><div class="empty">Opening ticket…</div></section>
  <aside class="res" id="res" aria-label="Resolution"></aside>
</main>
<section class="band foot" id="foot"></section>
<nav class="mob-nav" aria-label="Mobile sections">
  <button type="button" data-panel="queue">Queue</button>
  <button type="button" data-panel="work" class="on">Ticket</button>
  <button type="button" data-panel="res">Resolve</button>
  <button type="button" data-panel="more">Skills</button>
</nav>
<script>
{js}
</script></body></html>
"""
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("wrote", ROOT / "index.html", "bytes", len(html.encode()))

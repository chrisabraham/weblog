#!/usr/bin/env python3
"""Regenerate the wiki's Blackbox commands page from `bb help` on pinebox.

Run after any bb change that adds or renames a command:
  python3 tools/bb_commands.py && python3 build.py

Real client and contact names in bb's examples are swapped for made-up ones
(SCRUB); add to it whenever bb's help gains a new real name.
"""
import datetime as dt
import html
import re
import subprocess
import textwrap
from pathlib import Path

BB = Path.home() / "blackbox" / "bb"
OUT = Path(__file__).resolve().parent.parent / "src" / "wiki" / "blackbox-commands.html"
SCRUB = [("Avigail", "Dana"), ("#StrongBond", "#Atlas"), ("Strong Bond", "Atlas"), ("TrueHealthLabs", "Juniper")]

text = subprocess.run([str(BB), "help"], capture_output=True, text=True, check=True).stdout
for real, fake in SCRUB:
    text = text.replace(real, fake)

sections = re.split(r"\n(?=[A-Z][^\n]*:\n)", "\n" + text.strip())
blocks, names = [], []
for s in sections:
    s = s.strip("\n")
    if not s:
        continue
    head, _, body = s.partition("\n")
    head = head.rstrip(":")
    title, _, note = head.partition(" (")
    names.append(title)
    note = f"<p><em>{html.escape(note.rstrip(')'))}.</em></p>\n" if note else ""
    blocks.append(f"<h2>{html.escape(title)}</h2>\n{note}<pre>{html.escape(textwrap.dedent(body).rstrip())}</pre>")

today = dt.date.today().isoformat()
OUT.write_text(f"""title: Blackbox commands
description: Every command Blackbox knows, straight from bb help: tasks, minutes, briefs, email, Upwork, inbox, calendar, continuity, memory, and models.
updated: {today}
categories: Blackbox, Reference
info.Source: <code>bb help</code> on [[Pinebox]]
info.Groups: {len(blocks)}
info.Regenerated: {today}
info.Program: [[Blackbox]]
---
<p>This is the complete list of commands that [[Blackbox]] prints for <code>bb help</code>, regenerated from the live program whenever it changes. Most of them also work as plain sentences: Blackbox treats command words as ordinary speech unless the rest of the line fits the command, and a short line that matches nothing gets a loud warning instead of silently going to the chat. Examples use made-up names where the real help names real clients.</p>
<p>Anything that sends, submits, or changes something outside Blackbox waits for a yes. Upwork is read-only, email goes out through Alpine only when Chris presses Ctrl+X, and Todoist changes are proposed before they happen. The [[Upwork verdicts]] page explains the triage labels.</p>
{chr(10).join(blocks)}
""", encoding="utf-8")
print(f"wrote {OUT.name}: {len(blocks)} groups")

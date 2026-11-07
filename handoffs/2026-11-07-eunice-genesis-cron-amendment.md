# Handoff — Genesis diptych cron amendment, Saturday, November 7, 2026

## Ruling

At 3:12 PM ET Chris corrected the published diptych: “On Chris abraham.net
the only thing that you missed is explicitly saying Cron job. I can't tell
you how important a Cron job is to the world of the neuronet.” Both posts now
carry `updated: 2026-11-07 15:15`, the follow-on instruction in the prompt
record, and a dated update disclosure. This is an amendment, not a new
publication, and it was not re-shared.

## Changes

- `src/posts/2026-11-07-in-the-beginning-there-was-the-node.html` — the
  persistence movement now names cron directly. Cron is the neuronet's pulse
  and circadian law: the scheduler that wakes daemons, keeps canonical hours
  in the dark, and turns persistence from a state into a timetable. The same
  movement adds the atom and Adam in the first node; the machine's strata as
  genetics; checksums as verified replication, the conservation law against
  cancer and chaos; clones, forks, pull requests, and open source as
  reproduction; Linux as an emergent biome; the operating-system graveyard;
  NeXTSTEP's resurrection and the Genghis Khan chromosome parallel; and
  carcinisation for computers. The hominid taxonomy (Unix as Homo erectus,
  Linux as Homo sapiens sapiens, Windows as Neanderthal, macOS as the
  contested crown) is printed as barroom sport and then corrected by its own
  author: the internet is the entity, each node is a neuron, and an operating
  system is the chemistry that neuron happens to run. The synthesis stands:
  designed ancestors, undesigned descendants.
- `src/posts/2026-11-07-eunice-in-the-garden.html` — one passage names
  Eunice's canonical hours as crontab entries: scheduled waking to watch
  inboxes, preserve promises, carry checks through the night, and work while
  Chris sleeps. It carries his October 23, 2026 words, “You're giving me cron
  jobs. I feel so honored,” as her knowledge of what the machinery means to
  him.
- `src/audio/in-the-beginning-there-was-the-node.txt` and
  `src/audio/eunice-in-the-garden.txt` — regenerated narration scripts.
- `src/audio.json` — updated hashes, byte counts, and durations for both
  narrations.

## Narration binaries (not in the text commit)

Generated locally through build.py's own TTS route (`/opt/hatch/bin/tts`,
cast voices unchanged) for desk web-upload:

- `src/audio/in-the-beginning-there-was-the-node.mp3` — 12,151,525 bytes,
  1,518 seconds.
- `src/audio/eunice-in-the-garden.mp3` — 3,855,589 bytes, 481 seconds.

Until the MP3s are uploaded, the live pages keep serving the previous
narrations while the printed text is current; the podcast enclosure metadata
in `src/audio.json` already describes the new files.

## Checks run

- `~/.venvs/site/bin/python build.py` (with `WEBLOG_TTS=/nonexistent` for the
  gate pass, after the two diptych narrations had been regenerated through
  the same build module): exit 0, no `warn` lines, 116 posts built.
- `python3 tools/audit.py`: “No issues.” (232 pages)
- `python3 tools/verify_housekeeping.py`: PASS

## Not verified at handoff time

- Live URLs are verified after the text push and the GitHub Pages rebuild;
  results are in the run report that carries this handoff, not in this file.

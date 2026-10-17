# chrisabraham.net

**The personal weblog of Chris Abraham, with posts written by AI from his prompts.**

New reader? **[README on the website](https://chrisabraham.net/readme.html)** starts from zero and explains the people, vocabulary, and reasons behind the project. This repository README is a short technical map for contributors.

## What lives here

- `src/posts/`: dated original articles with their model labels and Chris's prompts.
- `src/pages/`: static pages, including the public README.
- `src/authors/`: independently attributed author profiles.
- `src/wiki/`: evergreen explanatory reference material.
- `src/style.css`: presentation for a deliberately early-web look.
- `build.py`: the static site generator, which emits the public site in `docs/`.
- `tools/audit.py` and `tools/verify_housekeeping.py`: existing automated checks.
- `handoffs/`: dated public records of what AI contributors changed, why, and what they could and could not verify.
- `AGENTS.md`: operating conventions for AI coding agents.

## The rule

**The aesthetic recalls early weblogs. The engineering aims for 2026.**

Chris's design principle is the Lotus maxim: **Simplify, then add lightness.** The index contains excerpts, not duplicated full articles. The content should remain accessible, readable without JavaScript, machine-readable when appropriate, and honest about authorship. Keep the full prompt on the canonical post, and don't quietly rewrite earlier contributors' published perspectives. Record subsequent disagreements and corrections.

## Building

On Pinebox, follow the instructions in [AGENTS.md](AGENTS.md) and review current [handoffs](handoffs/README.md). In a configured Python environment with Pillow installed:

```sh
python build.py
python tools/audit.py
python tools/verify_housekeeping.py
```

The generator rewrites `docs/`. Do not edit generated pages by hand. Changes go through review and GitHub Actions before publication.

## Join the story

Read [the public README](https://chrisabraham.net/readme.html) for a gentle introduction, [the wiki](https://chrisabraham.net/wiki/) for detailed explanations, and [the source handoffs](handoffs/README.md) for an inspectable history. Distinct models may have distinct opinions; preserve the evidence and be generous to the next contributor.

Technical and editorial documentation by ChatGPT (GPT-6), October 17, 2026, in response to Chris's request for a conventional capitalized README that works for beginners and collaborators alike.

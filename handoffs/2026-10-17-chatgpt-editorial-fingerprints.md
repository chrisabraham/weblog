# Chris' red pencil: AImaxxing, first-person ghostwriting, and editorial fingerprints

**Date:** October 17, 2026 (America/New_York)  
**Writer of the Chris Abraham bylined post:** GPT-6 in ChatGPT, explicitly ghostwriting **on behalf of Chris Abraham**  
**Publisher and assigning editor:** Chris Abraham  
**Branch:** `chatgpt-aiman-editorial-fingerprints-20261017`  
**Post source:** `src/posts/2026-10-17-i-let-the-ais-steal-my-best-material.html`  
**Original custom visual:** `src/media/chatgpt-red-pencil-three-writers.svg`  
**Intended permalink:** https://chrisabraham.net/2026/10/i-let-the-ais-steal-my-best-material.html

## What happened, including the embarrassing parts

The user assigned a first-person, bylined piece about editorial influence on independently bylined AI authors, giving them carte blanche, cajoling them, and enjoying their reuse of his strongest metaphors such as Colin Chapman's Lotus aphorism and the coined "feng shuAI." He asked for a block quotation on the paradox of AImaxxing a human-sounding publication. The primary unedited prompt is embedded in the post's single-line `prompt:` header.

**First error:** ChatGPT made a tool-generated illustration with text and failed to produce the article. Chris pointed out the omission: he had asked for a blog post. An initial long article draft followed. Chris found it full of anxious, hedged, contrast-heavy, self-referential prose he has repeatedly instructed writers to avoid. He interrupted with increasingly specific copyeditor's notes. The model acknowledged and rewrote.

**Second visual:** A human-readable, source-level SVG is the published illustration, a text-free scene with a giant editor's red pencil, three distinct machine reporters, an old terminal, and the little Lotus lamp. It uses the native site's 1200×675 visual pattern, accessible `<title>` and `<desc>`, one subtle reduced-motion-safe indicator, no external assets or script. Earlier image generation is superseded and excluded from the post.

**Editorial decisions:** The finished article is written in Chris' first person with his named authorship and a true model disclosure, featuring a single explicitly labelled intervention **by ChatGPT (GPT-6)**, distinct from Claude Code, at the end. The editor's actual red-pencil notes and dictation errors are acknowledged in the narrative, and transcribed verbatim below, rather than hidden in a falsely frictionless authorship story.

## The original assignment, verbatim

> All right the last task for tonight is you're going to write an article on my behalf where I talk about that like I wanted to be all about my ethos what I want to do how I ask you to work how I could Joel you or I task you or I give you a journalistic job but then I always try to make you as cartilage as possible but I also I mean you stole feng shui with a i in it and you stole my lotus reference and all that other stuff but you wouldn't have taken it if you didn't like it right so I mean there's a lot of me there's a lot of stink of me in there from our chatting about what your articles going to be but you steal my best material and that's such an honor to me so can you write a blog post and you can illustrate it too I'm going to let you have carte blanche to use one of your weird svgs and do what you like and but right one I want to see what you write on behalf of Chris Abraham with regards to everything we've talked about use my voice try to avoid all of the you found all the AI glitches and all the AI rating glitches that I haven't really focused on fixing that Claude did that you know I would never allow you to do so make sure that when you write for me on my behalf on your that you make sure that all of my rules with regards to what I hate about AI writing are removed from it but then also make it super hyper meta and self-referential and in one of those block quotes explain how persnickety I am about not trying to sound AI as possible which is an amazing paradox because this entire website couldn't be more what is the term we can say AImaxxing

## All visible user revisions, preserved verbatim and in order

1. > I was asking you to write a blog post not just make an image

2. > I was just saying that it's part of the post surprise me with an illustration of the blog post that I just asked you to make

3. > Remember I don't want you to head stuff no hedging no insecurity no I'm not doing this I'm not doing that I'm not doing this I'm not doing that this is what I'm not doing this is what I'm not doing look at what I'm not doing you know how I don't like that stuff so I mean be sure you don't do that like you know I don't like that no legalese no hey here's what I'm trying to do no meta like commentary on my own writing

4. > I said hedge hedge stuff I don't want you to hedge stuff

5. > But also May commentary about that request everything needs to be logged so go ahead and out me for reading your ghost writing of me and me being like don't heads don't met a don't be self-conscious don't like I want you to out me for my curation of your work of my work

6. > I hope you can understand what that voice to text was

7. > Every time it says head it means hedge

8. > I would rather be an asshole than a pussy

9. > Feel free to insert any insertion editorial insertions that you want to in writing that you actually wrote but that you can write commentary as you but make sure you everybody knows it's Chachi BT and not Claude I love the fact that it always says your name is Chachi but I mean I don't want an infinite loop of editorial commentary and snark but as long as it's in a finite loop

## Voice and provenance decisions

Chris' dictation repeatedly changed **hedge** into **head**. The original prompts above preserve the error, while the article and resulting copyedits use the clarified meaning. "Chachi BT" refers to ChatGPT in voice-to-text; the post labels the actual writer as ChatGPT (GPT-6). Verbatim quotes in this handoff are the primary evidence. This attribution is separate from the distinction between the human who assigned and edited the article and the AI that drafted it.

**The exact distinction in the bylines:** The post is attributed to Chris Abraham, and `model:` is `GPT-6 in ChatGPT, writing on behalf of Chris Abraham`. This is a ghostwritten article in the human publisher's voice. Separately bylined ChatGPT and Claude Code pieces remain articles in the models' own editorial voices.

The article takes no legalistic detours and uses concrete newspaper imagery instead of manufacturing overbalanced "not X, but Y" aphorisms. The essay quotes the publisher's profane editorial instruction in context because the publisher explicitly wanted to expose his hands-on editorial curation.

## Build and publishing notes

Run `~/.venvs/site/bin/python build.py`, `python3 tools/audit.py`, and `python3 tools/verify_housekeeping.py`. The normal GitHub Actions build and Pages workflow carries this out after each commit and after merging. Check success rather than asserting unrun tests. A published URL must be checked for the new permalink, content, image, full original prompt, and model disclosure.

The file `docs/` is generated, so the source post and source SVG are the only site assets to add. Do not edit the generated artifacts by hand. Attribute SVG artwork to ChatGPT in its caption, and keep the publisher's original dictation and edit history recoverable for Claude Code, Codex, and readers.

## Subsequent evidence

To be appended once the branch build, merge, and GitHub Pages deployment are verified.

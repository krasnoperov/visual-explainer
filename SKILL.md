---
name: visual-explainer
description: "Turn substantive Codex research and explanations into dense, mobile-first visual artifacts that are faster to understand, easier to verify, and safer to act on than long chat. Use by default for investigations, architecture or process explanations, comparisons, plans, reviews, incident analyses, rollout or status reports, and other multi-part conclusions. Preserve decision-relevant evidence and caveats, expose relationships through the right visual forms, render as HTML or motion when each medium earns its place, publish automatically, and return a short summary plus the private link. Skip visual artifacts for trivial answers already clear in one short paragraph."
---

# Visual Explainer

Turn the full context of a complex Codex answer into an explanation the reader can understand, verify, and act on with less effort—without hiding evidence, uncertainty, or consequential detail. HTML and motion are two renderers of the same explanation.

## Build the explanation

1. Re-read the user's question and original sources. Identify what the reader needs to understand or decide and what a shallow reading could get wrong.
2. Separate verified facts, inference, proposals, and unknowns. Keep evidence and caveats that can change the conclusion.
3. Build one compact semantic model: claims, evidence, relationships, and the natural reasoning path. Use it as the source of truth for every renderer.
4. Edit before styling. Remove setup, repetition, filler, generic transitions, and prose that only announces structure.
5. Choose one primary language from the user's request and project context. Do not mix prose languages; preserve exact code, product, API, and UI identifiers. For English or multilingual source material, read `references/artifact-language.md`.
6. Give each relationship a visual form that exposes it: timeline, convergence, fan-out, hierarchy, transformation, comparison, scale, ledger, annotated mechanism, state machine, or another meaningful geometry.

## Choose the medium

- Default to responsive HTML for asynchronous explanations: the reader can scan, inspect evidence, and control the pace.
- Add or use motion only when time clarifies accumulation, causality, sequence, transformation, or changing state, or when the user asks for video.
- When both are useful, compose both directly from the semantic model and original evidence. Never turn report sections into video scenes or treat the HTML as the video's sole source.
- Use fixed slides only for live or explicitly slide-based presentations.

## Render HTML

Read `references/report-design.md` for reports with several sections, diagrams, or dense evidence.

- Make the artifact mobile-first, self-contained, and information-dense. Put useful evidence in the first phone viewport; use compact headings and readable body copy.
- Keep explanation next to the visual mark it explains. Collapse raw logs and optional detail, never reasoning required to judge the conclusion.
- Use custom single-file HTML by default. Add a component toolchain only when real state or interaction earns it, then bundle the result into one portable site.
- Inline CSS, SVG, and small scripts. Do not add remote fonts, analytics, or trackers. Include viewport and `noindex,nofollow,noarchive,nosnippet` metadata; support keyboard focus, reduced motion, and print.
- Render at 360px before desktop. Inspect hierarchy, wrapping, diagrams, interactions, and overflow from screenshots; revise the artifact, not only its source.

## Render motion

Read `references/motion-design.md` completely. Use the installed Remotion skill for implementation and video-production guidance for capture, audio, rendering, and delivery QA.

- Build beats around changes in understanding, not around report sections. Keep the original question, evidence, relationships, and caveats available throughout production.
- Reject a shot whose primary action is “text appears.” Use visible accumulation, convergence, propagation, comparison, transformation, boundary crossing, or state change.
- Let picture demonstrate; use text for labels and exact evidence; use narration for connective reasoning when sound helps. Do not duplicate narration as on-screen prose.
- Render an animatic early. Watch the complete file at 1× on a phone-sized surface and fix dead time, repeated composition, ambiguity, and the first impulse to skip. Contact sheets supplement full playback; they do not replace it.

## Definition of done

- The central question and useful evidence appear immediately.
- Visual structure makes the important relationships easier to understand than prose alone.
- Evidence, uncertainty, and caveats remain inspectable.
- Every section or beat adds understanding; none exists only for decoration or pacing.
- Language is precise, consistent, and free of accidental code-switching.
- The artifact is legible on a phone and has been inspected as rendered output.
- The private published link works.

## Publish and hand off

Publish automatically; never ask the user to remember a command:

```bash
python3 ~/.codex/skills/visual-explainer/scripts/publish.py /absolute/path/explainer.html
python3 ~/.codex/skills/visual-explainer/scripts/publish.py /absolute/path/explainer-site/
```

The publisher safely copies a file or site directory, avoids collisions, and prints the canonical private URL. Verify local static serving and the authenticated public boundary; do not weaken authentication to obtain a public `200`.

Put the direct link near the top. When both formats exist, use the HTML page as the entrypoint and keep the video adjacent. In chat, state only the conclusion, essential caveat, and link; do not reproduce the artifact or expose publishing mechanics.

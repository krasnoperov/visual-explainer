# Visual Explainer

Turn dense Codex work into mobile-first visual explanations that are faster to understand, easier to verify, and safer to act on than long chat.

Both formats begin from one evidence-backed semantic model. Video is not an animated export of the report: it returns to the original question, sources, relationships, and caveats, then composes them for time. The HTML remains the reader-controlled, inspectable artifact; motion is used only when accumulation, causality, sequence, transformation, or changing state becomes clearer by moving.

## Inspiration and credit

This skill is strongly inspired by [Frontend Slides](https://github.com/zarazhangrui/frontend-slides), created by [Zara Zhangrui](https://github.com/zarazhangrui).

The skill carries forward Frontend Slides' commitment to:

- producing distinctive work rather than generic AI-looking layouts;
- delivering portable, self-contained HTML;
- loading detailed design guidance progressively;
- inspecting the rendered result instead of trusting source code alone.

This is an independent skill, not a fork. No Frontend Slides templates or source code are bundled here.

The information-design guidance is also informed by Anthropic's [Frontend Design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) and [Web Artifacts Builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder). Unlike a general web-app builder, Visual Explainer starts with edited information and the smallest representation that exposes its relationships.

## Deliberate differences

The two skills optimize for different reading situations:

| Frontend Slides | This skill |
|---|---|
| Live or intentionally slide-based presentations | Asynchronous technical explanations and reports |
| Fixed 16:9 stage scaled to every viewport | Responsive scrolling layout designed at 360px first |
| Visual style discovery before producing a deck | One opinionated visual direction chosen automatically for routine reports |
| Speaker-led and reading-deck density modes | A natural causal reading path chosen for the subject |
| Optional deployment and export workflow | Automatic private publication |
| Slides are the primary artifact | Slides appear only when explicitly requested or meant for live presentation |

Animated explainers preserve the source context and use semantic state changes rather than revealing report sections or blocks of text in sequence.

For presentation work where a fixed stage, visual style selection, editing, or PowerPoint conversion matters, use [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) directly. For a report that should be opened from a Codex answer and read comfortably on a phone, use this skill.

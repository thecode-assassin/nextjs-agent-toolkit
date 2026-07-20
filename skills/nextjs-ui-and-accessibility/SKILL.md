---
name: nextjs-ui-and-accessibility
description: Build and review accessible, responsive, server-first Next.js App Router interfaces, component boundaries, forms, dialogs, navigation, images, fonts, and design-system integration. Use for UI implementation or review when framework rendering and accessibility must be considered together.
---

# Next.js UI and Accessibility

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- semantic HTML, keyboard behavior, focus, labels, announcements, contrast, and motion preferences
- small client islands, serializable props, stable server rendering, and hydration
- responsive layout, image and font components, reusable primitives, and form feedback

## Decision Rules

- Add a Client Component boundary only where interaction or browser APIs require it.
- Prefer native semantics before ARIA and preserve focus intentionally across navigation and dialogs.
- Verify real browser behavior at keyboard, mobile, reduced-motion, loading, empty, and error states.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

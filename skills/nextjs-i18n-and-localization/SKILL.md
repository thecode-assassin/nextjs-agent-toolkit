---
name: nextjs-i18n-and-localization
description: Design and refactor Next.js App Router internationalization, locale routing, language negotiation, localized metadata, dictionaries, formatting, and translation loading. Use when adding locales, changing locale URLs, or reviewing localization architecture.
---

# Next.js Internationalization and Localization

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- locale URL strategy, negotiation, persistence, and request interception
- server-side dictionaries, translation key boundaries, and bundle size
- localized metadata, dates, numbers, pluralization, direction, and fallback behavior

## Decision Rules

- Make the URL strategy explicit and preserve shareable, crawlable localized URLs.
- Keep dictionaries on the server unless interaction requires a client subset.
- Use locale-aware platform formatters and test fallback, right-to-left, and missing-key behavior.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

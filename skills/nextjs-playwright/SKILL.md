---
name: nextjs-playwright
description: Configure, write, and debug Playwright end-to-end tests for Next.js App Router projects, including production-like startup, navigation, authentication state, fixtures, network boundaries, accessibility, and CI artifacts. Use only when Playwright is installed or explicitly requested.
---

# Next.js Playwright

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- installed Playwright version, webServer command, base URL, projects, retries, traces, and CI settings
- role-based locators, user-visible behavior, navigation, hydration, cookies, redirects, uploads, and auth reuse
- isolated data, parallel safety, deterministic setup, screenshots, videos, and traces

## Decision Rules

- Prefer resilient accessible locators over CSS structure or timing sleeps.
- Keep test accounts and data isolated so parallel workers cannot corrupt each other.
- Capture traces on retry and reproduce failures against the same build mode used in CI.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

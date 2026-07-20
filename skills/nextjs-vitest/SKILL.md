---
name: nextjs-vitest
description: Configure, write, and repair hermetic Vitest tests for Next.js App Router projects, including React components, hooks, utilities, route boundaries, mocks, jsdom, and coverage. Use only when Vitest is installed or explicitly requested.
---

# Next.js Vitest

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- installed Vitest, React, and DOM-testing versions plus test environment configuration
- behavior-focused component and hook tests, deterministic modules, time, network, and environment
- Next.js module boundaries, server-only limitations, cleanup, isolation, and coverage value

## Decision Rules

- Do not render async Server Components in a unit environment that cannot execute them reliably; test extracted logic or use a browser layer.
- Mock at external seams, not every internal function, and reset mutable state between tests.
- Make a failing regression test reproduce the bug before implementing the fix.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

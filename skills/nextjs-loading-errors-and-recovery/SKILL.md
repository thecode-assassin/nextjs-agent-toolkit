---
name: nextjs-loading-errors-and-recovery
description: Design and refactor Next.js App Router loading, empty, not-found, forbidden, unauthorized, error, global error, and recovery experiences. Use when adding route-level boundaries, handling expected failures, preserving framework control flow, or improving streaming and retry behavior.
---

# Next.js Loading, Errors, and Recovery

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- loading.tsx, error.tsx, global-error.tsx, not-found.tsx, and installed-version access interrupts
- expected errors versus uncaught exceptions and framework control-flow throws
- Suspense placement, retry safety, logging, and user recovery

## Decision Rules

- Model expected failures as return values or explicit states; do not turn routine validation into crashes.
- Never catch and suppress redirect, not-found, or access-control interrupts.
- Place boundaries at the smallest segment that can recover without losing useful surrounding UI.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

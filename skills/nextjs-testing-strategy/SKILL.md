---
name: nextjs-testing-strategy
description: Design a risk-based test strategy for Next.js App Router applications across pure logic, components, server boundaries, route handlers, accessibility, browser flows, and production builds. Use when choosing test layers, reviewing coverage, or reducing slow and brittle tests.
---

# Next.js Testing Strategy

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- risk inventory and the cheapest test layer that catches each failure
- server/client boundaries, navigation, streaming, mutations, endpoints, accessibility, and deployment behavior
- hermetic fixtures, deterministic time and network control, and CI cost

## Decision Rules

- Test behavior and contracts rather than framework implementation details.
- Use real browser tests for hydration, navigation, focus, cookies, redirects, and cross-boundary behavior.
- Require a production build check when configuration, routing, runtime, or rendering behavior changes.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

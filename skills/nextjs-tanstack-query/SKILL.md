---
name: nextjs-tanstack-query
description: Design, implement, and review TanStack Query integration in Next.js App Router projects, including provider placement, QueryClient lifetime, server prefetch, hydration, streaming, query ownership, mutations, invalidation, and testing. Use only when TanStack Query is installed or explicitly requested.
---

# Next.js TanStack Query Integration

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- installed TanStack Query version, provider scope, QueryClient lifetime, prefetch, dehydration, and hydration
- one visible data owner after hydration, query keys, stale times, errors, retries, and cancellation
- mutation ownership, optimistic updates, invalidation, and server-rendered freshness

## Decision Rules

- Use a client cache only when post-hydration behavior benefits from client-owned freshness.
- Create QueryClient instances with the lifetime appropriate to server requests and browser sessions.
- Do not combine server refresh, framework cache invalidation, and query invalidation without an explicit ownership model.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

---
name: nextjs-rendering-and-data
description: Design and refactor Next.js App Router rendering and read-data ownership across Server Components, Client Components, Suspense, streaming, direct server access, fetch, caching, and revalidation. Use when deciding where data is read, what crosses the server-client boundary, or how freshness works.
---

# Next.js Rendering and Data

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- Server and Client Component boundaries
- direct server reads, fetch placement, streaming, Suspense, and parallelism
- the installed version's caching model, directives, tags, paths, and request-specific data

## Decision Rules

- Prefer server ownership until browser state or post-hydration interactivity requires a client boundary.
- Do not call an internal HTTP route from a Server Component when the server can call the underlying data source directly.
- Name one owner for each read and one freshness policy; avoid layered invalidation by accident.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

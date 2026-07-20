---
name: nextjs-routing-and-navigation
description: Design, implement, and review Next.js App Router route trees, layouts, pages, dynamic segments, route groups, parallel and intercepting routes, redirects, rewrites, proxy or middleware behavior, and client navigation. Use when changing URL structure, navigation, route ownership, or request interception.
---

# Next.js Routing and Navigation

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- app directory topology and URL ownership
- layouts, templates, dynamic params, route groups, parallel routes, and interception
- Link, router APIs, redirects, rewrites, and the installed version's proxy or middleware convention

## Decision Rules

- Preserve stable public URLs unless migration is explicitly requested.
- Use route groups for organization, not as hidden URL semantics.
- Keep request interception narrow; prefer route-local logic when global interception is unnecessary.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

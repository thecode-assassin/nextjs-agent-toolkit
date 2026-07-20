---
name: nextjs-auth-and-security
description: Design and review framework-neutral authentication, authorization, data exposure, request forgery defenses, security headers, server-only boundaries, data access layers, and DTOs in Next.js App Router applications. Use for access control, session boundaries, sensitive data, or security reviews.
---

# Next.js Authentication and Security

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- authentication versus authorization and where each check executes
- server-only modules, data access functions, DTOs, action and endpoint entry points
- cookies, CSRF, redirects, headers, secret handling, and client-visible serialization

## Decision Rules

- Authorize at the data or mutation boundary even when navigation is also protected.
- Treat layouts and request interception as early UX gates, not the only security boundary.
- Pass the minimum serializable data to Client Components and never expose server credentials.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

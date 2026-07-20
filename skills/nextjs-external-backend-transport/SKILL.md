---
name: nextjs-external-backend-transport
description: Design and implement typed HTTP transport between Next.js App Router applications and external backends, including server and browser clients, auth and CSRF propagation, timeouts, cancellation, retries, error normalization, caching, and observability. Use when a Next.js frontend calls a separate HTTP service.
---

# Next.js External Backend Transport

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- backend contract, base URL, server versus browser call paths, credentials, CSRF, and CORS
- typed request and response parsing, timeouts, cancellation, retry and idempotency policy, and normalized errors
- cache ownership, correlation, redaction, test doubles, and direct server access versus browser proxying

## Decision Rules

- Keep server credentials and privileged backend calls out of browser bundles.
- Retry only safe or explicitly idempotent operations and preserve cancellation.
- Validate untrusted responses at the boundary when runtime correctness matters; TypeScript types alone are not validation.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

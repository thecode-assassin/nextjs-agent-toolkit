---
name: nextjs-route-handlers
description: Design, implement, and review Next.js App Router Route Handlers, HTTP method exports, request parsing, validation, response semantics, runtime selection, caching, streaming, webhooks, and thin endpoint architecture. Use for API endpoints, external consumers, callbacks, or explicit HTTP contracts.
---

# Next.js Route Handlers

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- route.ts placement, method ownership, typed parameters, and Web Request/Response APIs
- status codes, headers, validation, authentication, idempotency, and content negotiation
- thin handlers that delegate business logic and declare runtime or caching only when needed

## Decision Rules

- Use an HTTP endpoint when HTTP semantics or external callers matter, not as an internal indirection layer.
- Validate inputs at the boundary and avoid leaking internal exceptions or sensitive fields.
- Verify caching behavior for the installed version instead of assuming GET handlers are cached or dynamic.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

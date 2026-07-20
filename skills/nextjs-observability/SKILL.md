---
name: nextjs-observability
description: Design and implement Next.js App Router observability and runtime debugging with instrumentation, request-error capture, Web Vitals, structured logs, traces, metrics, correlation, and privacy controls. Use for production diagnosis, telemetry setup, or runtime-specific failures.
---

# Next.js Observability

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- instrumentation registration, request error capture, Web Vitals, logs, traces, and metrics
- Node.js versus Edge runtime behavior and deployment telemetry
- correlation IDs, sampling, redaction, source maps, and actionable alert context

## Decision Rules

- Capture enough context to reproduce a failure without logging secrets, tokens, or sensitive user data.
- Keep instrumentation lightweight, failure-tolerant, and explicit about runtime compatibility.
- Separate user-visible recovery from operator telemetry and verify production behavior.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

---
name: spring-boot-nextjs-contracts
description: Review, synchronize, and test HTTP contracts between Spring Boot backends and Next.js TypeScript clients, including DTO shapes, nullability, enums, validation, errors, pagination, dates, authentication, OpenAPI, and compatibility. Use when both Spring Boot and Next.js participate in the same API contract.
---

# Spring Boot and Next.js Contracts

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- controller request and response DTOs, TypeScript schemas and types, OpenAPI, and actual serialized JSON
- nullability, defaults, enums, dates, numbers, validation errors, pagination, authentication, and content types
- backward-compatible evolution, generated clients, consumer tests, and deployment ordering

## Decision Rules

- Treat wire JSON and its runtime schema as the contract, not similarly named language types.
- Classify each drift as breaking, additive, or compatible before editing either side.
- Prefer one authoritative schema or automated contract check, and coordinate breaking changes across rollout order.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

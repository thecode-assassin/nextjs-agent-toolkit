---
name: nextjs-pr-review
description: Review Next.js App Router pull requests for correctness, regressions, security, rendering and cache mistakes, route behavior, accessibility, performance, tests, and deployment risk. Use when reviewing a diff, branch, commit, or proposed implementation.
---

# Next.js Pull Request Review

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- changed behavior and affected routes before style
- server/client boundaries, request data, caching, mutations, authorization, errors, and navigation
- test evidence, production build implications, rollout risk, and precise line-level findings

## Decision Rules

- Report only actionable findings supported by the diff or reproducible evidence.
- Rank findings by impact and include file, line, scenario, and concrete consequence.
- Do not require personal preferences when multiple correct framework patterns exist.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

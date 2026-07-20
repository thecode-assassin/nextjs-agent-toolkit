---
name: nextjs-deployment
description: Plan, configure, and verify provider-neutral Next.js App Router deployments, including build output, Node.js servers, containers, static export, runtime capabilities, environment variables, caching, assets, health checks, and rollback readiness. Use when preparing or diagnosing deployment.
---

# Next.js Deployment

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- deployment target capabilities, build command, output mode, runtime, and package-manager reproducibility
- environment values, assets, image behavior, caching, regions, health checks, and logs
- static export feature limits, standalone containers, migrations, rollout, and rollback

## Decision Rules

- Choose an output mode only after mapping required framework features to target capabilities.
- Build from a clean lockfile and verify the production artifact, not only the dev server.
- Keep deploy-time data migrations and irreversible changes independently controlled and recoverable.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

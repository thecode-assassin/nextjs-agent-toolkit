---
name: nextjs-vercel
description: Configure, deploy, and diagnose Next.js App Router projects on Vercel, including build settings, environments, functions, regions, caching, image behavior, observability, previews, domains, and rollbacks. Use only for Vercel targets or when Vercel configuration is present.
---

# Next.js on Vercel

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- Vercel project linkage, build settings, framework detection, environment scopes, functions, and regions
- preview versus production behavior, domains, caching, images, logs, traces, and deployment protection
- rollout, rollback, migrations, quotas, and platform-specific runtime limits

## Decision Rules

- Inspect project settings and deployment logs before changing framework configuration.
- Keep preview, development, and production environment values intentionally separate.
- Verify platform limits and current behavior from Vercel documentation rather than assuming framework defaults.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

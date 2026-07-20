---
name: nextjs-performance
description: Measure, diagnose, and improve Next.js App Router performance across rendering, client boundaries, JavaScript bundles, images, fonts, scripts, streaming, caching, and Core Web Vitals. Use for performance audits, regressions, bundle growth, or slow routes.
---

# Next.js Performance

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- measurement before optimization: build output, bundle analysis, Web Vitals, traces, and route timing
- client boundary size, waterfalls, streaming, caching, image, font, and script loading
- production-representative verification and regression budgets

## Decision Rules

- Fix the measured bottleneck instead of applying generic optimizations.
- Reduce client JavaScript by moving non-interactive work server-side and importing narrowly.
- Evaluate cold, warm, cached, uncached, mobile, and slow-network behavior where relevant.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

---
name: nextjs-metadata-and-seo
description: Design, implement, and review Next.js App Router metadata, canonical and alternate URLs, Open Graph and social cards, robots, sitemaps, icons, structured data, and crawl behavior. Use for search discoverability, share previews, or route-specific metadata.
---

# Next.js Metadata and SEO

## Workflow

1. Inspect the repository before proposing a pattern. Read package manifests and lockfiles, locate the App Router, identify relevant configuration and conventions, and preserve unrelated user changes.
2. Detect the installed versions and active feature flags. If behavior is version-sensitive, verify it in the matching official documentation. Report unknown or dynamically computed configuration as unknown instead of guessing.
3. Map the current behavior, ownership boundaries, and user-visible contract. State assumptions that materially affect the solution.
4. Choose the smallest architecture that satisfies the requirement. Keep framework boundaries explicit and avoid introducing optional libraries that are not installed or requested.
5. Implement narrowly. Preserve existing conventions unless they are the cause of the problem.
6. Verify with the repository's existing checks plus the most relevant focused test, production build, or browser scenario.

## Inspect Closely

- static metadata versus generateMetadata and parent metadata composition
- canonical URLs, alternates, robots, sitemaps, icons, Open Graph, and social images
- structured data provenance, escaping, and validation

## Decision Rules

- Use stable absolute production URLs and derive route-specific values from authoritative data.
- Do not duplicate or contradict canonical, alternate, and robots signals.
- Treat metadata generation as server work and handle missing records consistently with route behavior.
- Gate experimental, canary, or opt-in behavior behind explicit configuration and document the fallback.
- Do not assume a fixed Next.js major version or rename version-dependent conventions without inspecting the project.

## Output Contract

When designing or reviewing, state: evidence inspected, current behavior, recommended ownership and boundaries, version-sensitive assumptions, risks, and verification. When implementing, make the scoped change, run proportionate checks, and report exact files changed plus any remaining uncertainty.

## Sources

Read [references/sources.md](references/sources.md) when API behavior, supported configuration, or version-sensitive guidance determines the answer. Prefer the installed-version documentation and primary sources.

# Implementation plan

This repository implements the agreed personal Next.js agent toolkit:

- 16 project-neutral Next.js App Router core skills
- nine adapters for Auth.js, TanStack Query, Tailwind/shadcn, Vitest, Playwright, Next.js DevTools MCP, Vercel, external HTTP backends, and Spring Boot contracts
- five personal Codex agents installed globally by symlink
- dynamic installed-version and configuration detection
- core, UI, data/auth, testing, devtools, backend, platform, and full installer profiles
- two evaluation cases per skill plus deterministic validator, installer, and detector tests
- explicitly invoked Next.js DevTools MCP usage plus safe project configuration and scaffolding scripts, with no dependency from other skills or agents
- removal of the allowlisted legacy personal Next.js skills after replacement validation
- private GitHub publication under `thecode-assassin/nextjs-agent-toolkit`

The old mixed-purpose repository remains unchanged. This file records the implemented scope; ongoing capability status lives in `docs/capability-matrix.md`.

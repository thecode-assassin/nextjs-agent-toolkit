---
name: nextjs-devtools-mcp
description: Configure and use the optional Next.js DevTools MCP integration for App Router projects. Use when explicitly asked to scaffold or configure a project with next-devtools-mcp, inspect a running application's errors or metadata, query official Next.js documentation, perform supported migrations or Cache Components setup, or verify behavior through its browser tools.
---

# Next.js DevTools MCP

## Workflow

1. Inspect the target project, installed Next.js version, package manager, existing MCP configuration, and current task before selecting a capability. Do not import or execute `next.config` to inspect it.
2. Keep activation project-scoped unless the user explicitly requests a global installation. For a new application, run `scripts/create_project.py`. For an existing application, run `scripts/configure_project.py`.
3. Restart Codex or begin a fresh task after adding project MCP configuration so tool discovery can reload it.
4. Initialize the MCP for the explicit Next.js task when its `init` tool is available. Pass the target project path and reconcile returned guidance with the installed framework version and configuration.
5. Use only the capability needed for the task. Inspect read-only evidence before invoking migration, configuration, or browser actions that change state.
6. Verify resulting code with the project's normal checks. MCP results complement type checks, tests, production builds, and deployment evidence; they do not replace them.

## Project Setup

Create a new App Router project and configure Codex project settings:

```bash
python3 scripts/create_project.py /path/to/app -- --use-pnpm --ts --eslint --tailwind --app --yes
```

Configure an existing project:

```bash
python3 scripts/configure_project.py /path/to/app
```

Use `--format mcp-json` when the selected client reads the official project `.mcp.json` format. Use `--mcp-package next-devtools-mcp@<reviewed-version>` when reproducibility requires a pin. Add `--disable-telemetry` only when local policy requires it. Run either script with `--dry-run` before changing an unfamiliar project.

The configurator must preserve unrelated configuration, remain idempotent, and refuse to replace a conflicting `next-devtools` entry. Resolve the conflict explicitly instead of forcing an overwrite.

## Capability Selection

- **Runtime state:** Discover running servers first, select the server whose project metadata matches the target, then retrieve errors, logs, page metadata, or Server Action metadata. Runtime access requires a compatible running development server.
- **Documentation:** Search for the narrow concept, fetch the exact official page, and check that guidance applies to the installed version. Prefer installed version-matched documentation when current online documentation describes a different release.
- **Upgrade or migration:** Inspect current and target versions, invoke only the requested helper or codemod, review every diff, and separate compatibility work from optional feature adoption.
- **Cache Components:** Confirm the installed version and active flags before using setup or migration helpers. Do not enable canary, experimental, or opt-in behavior implicitly.
- **Browser verification:** Use browser tools when navigation, interaction, hydration, or visual evidence matters. Capture relevant console or page evidence and close sessions that the tool started.

## Boundaries

- Treat runtime MCP data as development evidence, not production observability.
- Do not assume runtime tools exist merely because the outer MCP server is configured; discover capabilities first.
- Do not block ordinary work when the MCP is absent. Use repository inspection, development logs, focused checks, or existing browser tooling as appropriate and report the unavailable capability only when material.
- Do not install packages, start migrations, modify configuration, or launch browser automation beyond the user's requested scope.
- Do not expose secrets through MCP arguments, logs, screenshots, or committed configuration.
- Account for the MCP server's telemetry and network behavior when repository or organization policy restricts external communication.

## Sources

Read [references/sources.md](references/sources.md) when setup syntax, supported capabilities, version requirements, or telemetry behavior affects the task.

# nextjs-agent-toolkit

Private, personal Codex tooling for the full Next.js App Router workflow. The repository contains 24 reusable skills, five focused Codex agents, a project-context detector, profile-based symlink installation, validation, tests, and eval cases.

The toolkit is framework-first and project-neutral. It inspects the installed Next.js version and active configuration instead of assuming one framework release. Optional stack skills activate only when their library is installed or explicitly requested.

## Install

From this repository, preview the default full installation:

```bash
python3 scripts/install.py --dry-run
```

Install all skills to `~/.agents/skills` and all agents to `~/.codex/agents`:

```bash
python3 scripts/install.py
```

On the first migration from the previous personal Next.js collection:

```bash
python3 scripts/install.py --profile full --remove-legacy
```

Legacy removal is restricted to an explicit allowlist under `~/.codex/skills`. A real directory is removed only when it contains `SKILL.md`; unrecognized directories and all non-Next.js skills are preserved.

Restart Codex or begin a fresh task after installation so discovery reflects the new links.

## Profiles

| Profile | Contents |
| --- | --- |
| `core` | 16 framework capabilities |
| `ui` | Core plus Tailwind/shadcn UI |
| `data-auth` | Core plus Auth.js and TanStack Query |
| `testing` | Core plus Vitest and Playwright |
| `backend` | Core plus generic external transport and Spring Boot contracts |
| `platform` | Core plus Vercel |
| `full` | Union of every profile; default |

Install a profile with `python3 scripts/install.py --profile testing`. Uninstall only repo-owned links with `python3 scripts/install.py --profile full --uninstall`. Use `--skills-dir` and `--agents-dir` for isolated testing or a custom Codex setup.

## Project context

Inspect a project without importing or executing its configuration:

```bash
node scripts/detect-nextjs-context.mjs /path/to/project --json
```

The detector reports versions, package manager, App Router location, proxy or middleware convention, statically visible cache/output settings, supported integrations, and deployment hints. Dynamic configuration is reported as unknown.

## Codex agents

- `nextjs-architect`: read-only architecture and migration design
- `nextjs-builder`: scoped implementation and verification
- `nextjs-reviewer`: read-only, evidence-based diff review
- `nextjs-debugger`: root-cause diagnosis; fixes only when requested
- `nextjs-migrator`: version upgrades, codemods, and router migrations

The agent files intentionally omit a fixed model and MCP configuration. They inherit the parent session. Next.js DevTools MCP may be configured separately in Codex for live runtime inspection, but no skill or agent depends on it.

## Validate and evaluate

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/run_evals.py --list
python3 scripts/run_evals.py --skill nextjs-rendering-and-data
```

There are two machine-readable cases per skill: one normal task and one misuse or boundary task. The runner prints prompts and rubrics; an explicit `--record .eval-results/<name>.json` creates a local result template. CI validates structure and deterministic tests but does not spend model tokens.

See [docs/capability-matrix.md](docs/capability-matrix.md), [docs/version-policy.md](docs/version-policy.md), and [docs/maintenance.md](docs/maintenance.md).

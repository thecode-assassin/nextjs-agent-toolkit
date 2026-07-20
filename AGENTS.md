# Repository guidance

This private repository is the canonical source for reusable Next.js App Router skills and personal Codex agents.

## Authoring rules

- Keep every skill project-neutral. Never embed a personal project path, organization name, domain model, error type, or repository convention.
- Detect installed package versions, configuration, feature flags, router structure, and optional integrations before recommending version-sensitive behavior.
- Treat dynamic configuration as unknown. Never import or execute an untrusted `next.config` merely to inspect it.
- Gate canary, experimental, or opt-in behavior explicitly and give a stable fallback.
- Keep each skill independently usable. Do not mention another skill by name, `$skill-name`, or repository path as a prerequisite.
- Use imperative instructions, concise workflows, and primary-source references. Put detailed source lists in `references/sources.md` with applicability and `Last verified` metadata.
- A skill frontmatter contains only `name` and `description`. Keep the folder and frontmatter names identical.
- Regenerate or update `agents/openai.yaml` whenever a skill's purpose changes. The default prompt must mention its own `$skill-name`.
- Do not add a plugin manifest, marketplace metadata, Cursor rules, or per-skill README files.

## Agents

Store distributable personal agent definitions in `.codex/agents/*.toml`. Every file must include `name`, `description`, and `developer_instructions`. Omit model and MCP settings unless an agent truly requires an override so it inherits the parent session.

## Verification

Run:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

For a changed skill, inspect both eval cases in `evals/cases.json` and run an independent live evaluation when its workflow or boundary rules materially change. Store local results only under `.eval-results/`.

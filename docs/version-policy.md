# Version policy

The toolkit never assumes a fixed Next.js major.

1. Inspect `package.json`, the lockfile, Node.js requirements, route layout, and configuration before applying framework guidance.
2. Prefer exact installed versions when available. Preserve ranges as ranges and do not claim a resolved version without lockfile evidence.
3. Match version-sensitive claims to primary documentation for that release. For upgrades, inspect both source and target guides.
4. Treat dynamically computed configuration as unknown unless the relevant value is statically evident. Never execute project configuration during inspection.
5. Gate experiments, canary APIs, and opt-in flags. State the stable fallback and do not enable them incidentally.
6. Separate compatibility migrations from adopting new behavior so regressions and rollback remain understandable.

The detector is deliberately conservative. Its `unknown` result is a request for targeted inspection, not permission to guess.

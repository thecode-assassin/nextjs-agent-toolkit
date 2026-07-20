# Maintenance

Run the following monthly, and whenever Next.js, React, or a supported adapter publishes a material release:

1. Review primary documentation links and update `Last verified` dates only after checking applicability.
2. Run `python3 scripts/validate.py` and the full unit suite.
3. Exercise detector fixtures against new configuration conventions without executing configs.
4. Review the normal and boundary eval for each materially affected skill.
5. Run independent live evals for changed behavior and save results under `.eval-results/`.
6. Keep compatibility changes separate from new optional features.

Do not add cross-skill prerequisites to solve overlap. Tighten descriptions, scope, and boundary rules inside the affected skill instead.

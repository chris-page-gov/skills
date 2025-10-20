# Repository Usage Guide

This document complements the original `README.md` (kept unchanged as a reference showcase) by describing how we actively use and develop within this repository.

## Philosophy

- Keep each skill self-contained: a folder with `SKILL.md` + any helper scripts/resources.
- Avoid coupling between skills; shared patterns belong in documentation rather than shared code.
- Provide reproducible environments (dev container) to eliminate host dependency drift.

## Development Environment

### Dev Container

We use a VS Code Dev Container (`.devcontainer/`) to isolate toolchains:
- Python 3.11 for scripting (GIF generation, MCP evaluation, future doc tooling).
- Node 20 for web/app artifact workflows and Playwright testing.
- System packages: imaging libs (libjpeg, libpng, libwebp, freetype, tiff), `ffmpeg`, `pandoc`, and Playwright browser deps.

### Post-Create Automation

The script `.devcontainer/scripts/postCreate.sh` automatically:

1. Installs Python dependencies from skill-specific `requirements.txt` files.
2. Installs Node dependencies for the Playwright sandbox.
3. Downloads Playwright browsers (`npx playwright install --with-deps`).

### Why Isolation Matters

- Prevents global `pnpm` or Node installs from modifying host environment.
- Ensures consistent versions across contributors.
- Smooth path to add heavier deps (e.g., PDF rendering libs) without polluting macOS.

## Node + Playwright Sandbox

`node-sandbox/` supplies a minimal scaffold:

- `@playwright/test` + TypeScript config.
- Example spec in `tests/` to validate environment.
- Helpful scripts: `npm test`, `npx playwright show-report`, `npx playwright codegen`.

Use this sandbox to prototype automation flows that can inform instructions in the `webapp-testing` skill.

## Skills Authoring Workflow

1. Create a folder named with lowercase-hyphen pattern (e.g. `my-new-skill`).
2. Add `SKILL.md` containing YAML frontmatter:

   ```markdown
   ---
   name: my-new-skill
   description: Concise description of capability & when to use it
   ---
   # My New Skill
   Guidance, examples, constraints...
   ```

3. Provide examples that reflect real inputs/outputs.
4. Include guardrails (what NOT to do) to reduce hallucinations.
5. For executable helpers (scripts, templates), keep them small, documented, and optional.

## Versioning & Changelog

We follow Semantic Versioning for repository releases (tagged states) and maintain `CHANGELOG.md` using Keep a Changelog format:

- `Unreleased` section accumulates changes awaiting next tag.
- Categorize entries: Added / Changed / Fixed / Security / Deprecated / Removed.

## Testing Strategy

- Python: Add lightweight scripts or tests near logic-heavy modules (`slack-gif-creator/core`). (Future: introduce pytest if complexity grows.)
- Playwright: Use `node-sandbox` for browser automation prototypes; production usage distilled into skill instructions rather than shipping heavy test suites.

## Adding Dependencies

- Prefer adding new Python dependencies to a dedicated `requirements.txt` within the skill directory.
- For cross-skill tooling, evaluate if it truly belongs globally; if not, document usage in that skill's README or in `USAGE.md`.
- Keep versions pinned or use upper bounds if stability matters.

## Security & Compliance

- Avoid embedding secrets in scripts or `SKILL.md` files.
- Document any external service interactions explicitly.
- Keep licenses for included assets (fonts, images) adjacent to the asset.

## Future Enhancements

- Introduce automated linting (Markdown, Python, TypeScript) via a pre-commit or CI workflow.
- Add reproducible lock files (`requirements.lock`, `package-lock.json` or `pnpm-lock.yaml`) once dependency churn slows.
- Provide script for validating all `SKILL.md` frontmatter correctness.

## Quick Commands (Inside Dev Container)

```bash
# Run Playwright tests
npm --prefix node-sandbox test

# Re-install Playwright browsers (if versions change)
npx --prefix node-sandbox playwright install --with-deps

# Run GIF builder example (pseudo)
python slack-gif-creator/core/gif_builder.py
```

## Contributing

- Open a branch, update or add a skill, ensure changelog entry under Unreleased.
- Submit PR with clear rationale; reviewers verify instructions clarity + env impact.

---
_This usage guide evolves; update alongside meaningful workflow changes._

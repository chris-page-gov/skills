# Repository Usage Guide

## Table of Contents

1. [Philosophy](#philosophy)
2. [Development Environment](#development-environment)
3. [Node + Playwright Sandbox](#node--playwright-sandbox)
4. [Skills Authoring Workflow](#skills-authoring-workflow)
5. [Skill Examples Catalog](#skill-examples-catalog)
6. [Versioning & Changelog](#versioning--changelog)
7. [Testing Strategy](#testing-strategy)
8. [Adding Dependencies](#adding-dependencies)
9. [Skill Validation Script](#skill-validation-script)
10. [Security & Compliance](#security--compliance)
11. [Future Enhancements](#future-enhancements)
12. [Quick Commands](#quick-commands-inside-dev-container)
13. [Release Tagging Workflow](#release-tagging-workflow)
14. [Contributing](#contributing)

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

### Git Workflow & Permissions

- Run git operations inside the devcontainer to avoid macOS `.git` extended-attribute permission errors on the host:
  `docker run --rm -it -v "$PWD:/workspace" -w /workspace skills-dev bash`
- Configure identity once inside:  
  `git config user.name "Chris Page"` and `git config user.email "chris.page@bduk.gov.uk"`
- Prefer SSH or a PAT for pushes from the container; see `agents.md` for the full workflow and recovery steps.

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

## Skill Examples Catalog

The repository maintains an up-to-date catalog of example assets for every skill in [docs/skill_examples.md](docs/skill_examples.md). Consult it before diving into a task to see which templates, sample artifacts, or walkthrough markdown accompany the skill you need.


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
- If multiple skills share exact versions, consider a consolidation script that composes a temporary combined constraints file (avoid a monolithic root requirements unless truly shared runtime emerges).
- Node dependencies live only in `node-sandbox/` for now; avoid adding a root-level `package.json` to keep skill folders lightweight.

## Skill Validation Script

The repository includes `scripts/verify_skills.py` which enforces required YAML frontmatter fields in each `SKILL.md`.

Run it inside the dev container:

```bash
python scripts/verify_skills.py
```
Expected output example (success):

```text
✔ skill brand-guidelines: frontmatter ok
✔ skill internal-comms: frontmatter ok
```
Example failure message:

```text
✘ skill example-skill: missing required field 'description'
```
Required fields (current rule set):

- name (lowercase, hyphenated)
- description (clear when to use)

Add new validation rules by editing the script (e.g., enforce a `Guidelines` heading). Update `CHANGELOG.md` under Unreleased when rules change.

## Security & Compliance

- Avoid embedding secrets in scripts or `SKILL.md` files.
- Document any external service interactions explicitly.
- Keep licenses for included assets (fonts, images) adjacent to the asset.

## Future Enhancements

- Introduce automated linting (Markdown, Python, TypeScript) via a pre-commit or CI workflow.
- Add reproducible lock files (`requirements.lock`, `package-lock.json` or `pnpm-lock.yaml`) once dependency churn slows.
- Provide script for validating all `SKILL.md` frontmatter correctness.
- Add CI job invoking `scripts/verify_skills.py` + markdown lint on pull requests.
- Introduce a lightweight schema check ensuring no prohibited frontmatter keys (e.g., secrets, tokens).

## Quick Commands (Inside Dev Container)

```bash
# Run Playwright tests
npm --prefix node-sandbox test

# Re-install Playwright browsers (if versions change)
npx --prefix node-sandbox playwright install --with-deps

# Run GIF builder example (pseudo)
python slack-gif-creator/core/gif_builder.py

# If Playwright test command fails with "playwright: command not found", run post-create steps manually:
bash .devcontainer/scripts/postCreate.sh
```

## Release Tagging Workflow

1. Accumulate changes under **Unreleased** in `CHANGELOG.md`.
2. Before tagging, replace placeholders with concrete bullet items.
3. Create tag (example):

```bash
git tag -a 0.3.0 -m "Release 0.3.0"
git push origin 0.3.0
```
4. Update link references at bottom of `CHANGELOG.md`:
   - `[Unreleased]:` compares new tag to `HEAD`.
   - Add a new `[0.3.0]` line comparing previous tag to new tag.
5. Open PR (if needed) to merge changes to `main`.
6. Announce changes or update internal docs if skill behaviors changed.

## Contributing

- Open a branch, update or add a skill, ensure changelog entry under Unreleased.
- Submit PR with clear rationale; reviewers verify instructions clarity + env impact.

---
_This usage guide evolves; update alongside meaningful workflow changes._

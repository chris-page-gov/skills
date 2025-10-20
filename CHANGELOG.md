# Changelog

All notable changes to this repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added (0.2.0)

- (placeholder) Future additions go here.
- Skill verification script `scripts/verify_skills.py` to enforce required frontmatter fields.

### Changed (0.2.0)

- (placeholder)

### Fixed (0.2.0)

- (placeholder)

---

## [0.2.0] - 2025-10-20

### Added (0.1.0)

- Dev Container configuration: `.devcontainer/devcontainer.json` and `Dockerfile` to isolate Python (3.11) and Node (20) toolchains.
- Post-create automation script `.devcontainer/scripts/postCreate.sh` installing Python and Node dependencies plus Playwright browsers.
- Playwright & TypeScript sandbox `node-sandbox/` with minimal test scaffold and documentation.
- System packages for imaging (ffmpeg, libjpeg, libpng, libwebp, freetype, tiff) and document tooling (pandoc) plus Playwright browser libraries in container image.
- `CHANGELOG.md` following Keep a Changelog best practices.
- `USAGE.md` describing repository usage patterns (skills authoring, environment, testing workflows).

### Changed

- Separated environment concerns by moving installation steps into post-create script instead of inline `postCreateCommand` chain.
- Improved README discoverability via side file (`USAGE.md`) without modifying original `README.md` reference content.

### Fixed

- Devcontainer build failure by removing unresolved `pandoc` feature, installing pandoc via apt.
- Dockerfile font copy issue (replaced with placeholder comment) to prevent build errors.
- Markdown lint issues in newly added `node-sandbox/README.md` (blank lines, list indentation).

### Security

- Avoided global pnpm installation on host by performing setup inside container.

---

## [0.1.0] - 2025-10-19

### Added

- Initial collection of example skills with `SKILL.md` definitions.
- Document skills snapshot (`document-skills/`) for docx, pdf, pptx, xlsx capabilities.
- Python scripts for GIF creation and MCP server evaluation.

[Unreleased]: https://github.com/anthropics/skills/compare/main...HEAD
[0.2.0]: https://github.com/anthropics/skills/compare/0.1.0...0.2.0

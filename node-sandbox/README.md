# Node Sandbox

This sandbox provides a minimal Playwright + TypeScript setup for experimentation related to the `webapp-testing` skill.

## Commands

Run tests:

```bash
npm test
```

Generate and explore selectors for a site:

```bash
npx playwright codegen https://example.com
```

View HTML report after a run:

```bash
npx playwright show-report
```

## Updating Browsers

To install or update Playwright browsers:

```bash
npx playwright install --with-deps
```

## Notes

 - Tests default to 30s timeout, HTML report enabled.
 - Traces captured on first retry; adjust in `playwright.config.ts`.
 - This sandbox is isolated; add more devDependencies as needed without polluting the host.

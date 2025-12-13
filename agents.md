# Agent Workflow Notes

This repo's `.git` directory can be locked down by host filesystem attributes on macOS, which blocks git writes when run directly on the host. To avoid rebase failures, run all git operations inside the devcontainer image.

## Quick git inside the devcontainer
- Build image once: `docker build -t skills-dev -f .devcontainer/Dockerfile .`
- Open a shell inside the image with the repo mounted: `docker run --rm -it -v "$PWD:/workspace" -w /workspace skills-dev bash`
- Set git identity (if not already configured): `git config user.name "Chris Page"` and `git config user.email "chrispage@warwickshire.gov.uk"`
- Perform fetch/rebase normally inside the container:  
  `git fetch upstream`  
  `git checkout crpage`  
  `git rebase upstream/main`  
  (resolve conflicts, `git add ...`, `git rebase --continue`)

## If you hit a stuck rebase
- Check status: `git status`
- Clean up: `git rebase --abort` (inside container)
- Re-run the rebase in the container; avoid host-side git commands to prevent permission errors on `.git/index.lock` or `.git/rebase-merge/*`.

## Rationale
- Host-side git writes can fail with “Operation not permitted” due to extended attributes on `.git`.
- Running git inside the devcontainer as root bypasses those host restrictions and keeps future rebases smooth.

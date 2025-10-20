#!/usr/bin/env bash
set -euo pipefail

echo "[postCreate] Installing Python dependencies..."
pip install --no-cache-dir -r mcp-builder/scripts/requirements.txt
pip install --no-cache-dir -r slack-gif-creator/requirements.txt

echo "[postCreate] Initializing Node sandbox dependencies..."
if [ -d "node-sandbox" ]; then
  cd node-sandbox
  if [ -f package.json ]; then
    corepack enable || true
    npm install
    npx playwright install --with-deps || true
  fi
  cd - >/dev/null
fi

echo "[postCreate] Complete."
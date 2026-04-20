#!/bin/bash
set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$BASE_DIR"

source /roms/be-more-agent/venv/bin/activate
exec python agent.py

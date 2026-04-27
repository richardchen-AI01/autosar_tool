#!/usr/bin/env bash
# tools/build_all.sh — Build bswgen + bswval Python EXEs (PyInstaller).
#
# On macOS produces unix binaries (for testing locally);
# on Windows must run as tools\build_all.cmd to produce .exe.
#
# Outputs end up in build/dist/.
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT"

mkdir -p build/dist build/work

PYTHONPATH=core
export PYTHONPATH

echo "=== building bswgen ==="
python3 -m PyInstaller \
    --workpath build/work/bswgen \
    --distpath build/dist \
    --noconfirm \
    --clean \
    generator/bswgen.spec

echo
echo "=== building bswval ==="
python3 -m PyInstaller \
    --workpath build/work/bswval \
    --distpath build/dist \
    --noconfirm \
    --clean \
    validator/bswval.spec

echo
echo "=== artifacts ==="
ls -la build/dist/
echo
echo "  bswgen size: $(du -h build/dist/bswgen 2>/dev/null | cut -f1)"
echo "  bswval size: $(du -h build/dist/bswval 2>/dev/null | cut -f1)"
echo
echo "  Smoke test:"
build/dist/bswgen --help 2>&1 | head -5 || echo "  (bswgen --help failed; expected if PyInstaller dependencies missing)"

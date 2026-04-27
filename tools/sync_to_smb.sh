#!/usr/bin/env bash
# Incremental sync local Mac project → SMB share. Run after git commit
# (or whenever you want Windows to see latest code).
#
# Usage: ./tools/sync_to_smb.sh
set -e

SRC=$(cd "$(dirname "$0")/.." && pwd)
DST=/Volumes/AUTOSAR_tool

if [ ! -d "$DST" ]; then
    echo "ERROR: SMB not mounted at $DST"
    echo "Mount via Finder: Cmd+K → smb://192.168.1.44/AUTOSAR_tool"
    exit 1
fi

echo "Syncing $SRC → $DST ..."
rsync -av --delete \
    --exclude='.git/' \
    --exclude='__pycache__/' \
    --exclude='*.pyc' \
    --exclude='.DS_Store' \
    --exclude='reference/' \
    --exclude='build/' \
    --exclude='dist/' \
    --exclude='target/' \
    --exclude='.metadata/' \
    "$SRC/" "$DST/"

echo
echo "✓ Synced. Latest files now visible at:"
echo "    $DST"
echo "    \\\\192.168.1.44\\AUTOSAR_tool  (from Windows)"

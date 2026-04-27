#!/usr/bin/env bash
# tools/ide_smoke.sh — boot the materialized RCP launcher headless-ish, give
# it ~8 s to come up, kill it, then read .metadata/.log for any
# `!ENTRY <bundle> 4` lines (Eclipse log level 4 = ERROR).
#
# Pass criterion: 0 ERROR-level log entries.
#
# Usage:
#   ./tools/ide_smoke.sh                   # run on Mac/Linux post-Tycho-build
#   ./tools/ide_smoke.sh -k 15             # give it 15 s before killing
#
# NOT for Windows (no `pkill`); CI on ubuntu-latest is the canonical runner.

set -u
ROOT=$(cd "$(dirname "$0")/.." && pwd)

KILL_AFTER=8
WORKSPACE=$(mktemp -d -t bswbuilder_smoke.XXXXXX)
LOG_DIR=

while getopts "k:" opt; do
    case $opt in
        k) KILL_AFTER=$OPTARG ;;
        *) echo "Usage: $0 [-k seconds]"; exit 2 ;;
    esac
done

# 1. Pick the right launcher for this OS / arch
case "$(uname -s)/$(uname -m)" in
    Darwin/arm64)
        APP="$ROOT/ide/product/cn.com.myorg.bswbuilder.product/target/products/cn.com.myorg.bswbuilder.product/macosx/cocoa/aarch64/Eclipse.app"
        LAUNCHER="$APP/Contents/MacOS/bswbuilder"
        LOG_DIR="$WORKSPACE/.metadata"
        ;;
    Darwin/x86_64)
        APP="$ROOT/ide/product/cn.com.myorg.bswbuilder.product/target/products/cn.com.myorg.bswbuilder.product/macosx/cocoa/x86_64/Eclipse.app"
        LAUNCHER="$APP/Contents/MacOS/bswbuilder"
        LOG_DIR="$WORKSPACE/.metadata"
        ;;
    Linux/x86_64)
        APP="$ROOT/ide/product/cn.com.myorg.bswbuilder.product/target/products/cn.com.myorg.bswbuilder.product/linux/gtk/x86_64"
        LAUNCHER="$APP/bswbuilder"
        LOG_DIR="$WORKSPACE/.metadata"
        ;;
    *)
        echo "[FAIL] unsupported OS/arch: $(uname -s)/$(uname -m)"
        exit 3
        ;;
esac

if [ ! -x "$LAUNCHER" ]; then
    echo "[FAIL] launcher not found: $LAUNCHER"
    echo "       did you run 'cd ide && mvn -B clean verify' first?"
    exit 4
fi

echo "=== ide_smoke ==="
echo "  launcher : $LAUNCHER"
echo "  workspace: $WORKSPACE"
echo "  kill after: ${KILL_AFTER}s"
echo

# 2. Launch in background. -data picks workspace; -consoleLog dumps to stderr;
#    -clearPersistedState wipes any stale e4 model state.
"$LAUNCHER" \
    -consoleLog \
    -clearPersistedState \
    -data "$WORKSPACE" \
    > "$WORKSPACE/stdout.log" 2>&1 &
PID=$!

echo "  spawned pid=$PID"

# 3. Sleep and kill
trap 'kill -9 "$PID" 2>/dev/null; rm -rf "$WORKSPACE"' EXIT

i=0
while [ $i -lt "$KILL_AFTER" ]; do
    if ! kill -0 "$PID" 2>/dev/null; then
        echo "  process exited at t=${i}s"
        break
    fi
    sleep 1
    i=$((i + 1))
done

if kill -0 "$PID" 2>/dev/null; then
    echo "  process still alive at t=${KILL_AFTER}s — sending SIGKILL"
    kill -9 "$PID" 2>/dev/null
    sleep 1
fi

# 4. Inspect .metadata/.log
#    Eclipse only writes .metadata/.log when something is logged. If the
#    workbench booted cleanly with no errors / warnings, the file simply
#    doesn't appear. So "file absent" is the BEST possible outcome.
echo
echo "=== results ==="
if [ -f "$LOG_DIR/.log" ]; then
    err=$(grep -c '!ENTRY .* 4 ' "$LOG_DIR/.log" 2>/dev/null || echo 0)
    warn=$(grep -c '!ENTRY .* 2 ' "$LOG_DIR/.log" 2>/dev/null || echo 0)
    info=$(grep -c '!ENTRY .* 1 ' "$LOG_DIR/.log" 2>/dev/null || echo 0)
    echo "  ENTRY level 4 (ERROR)  : $err"
    echo "  ENTRY level 2 (WARNING): $warn"
    echo "  ENTRY level 1 (INFO)   : $info"
    if [ "$err" -gt 0 ]; then
        echo
        echo "  --- first 5 ERROR messages ---"
        grep -A1 '!ENTRY .* 4 ' "$LOG_DIR/.log" | grep '!MESSAGE' | head -5
        echo
        echo "[FAIL] $err ERROR-level Eclipse log entries — workbench did not boot cleanly"
        exit 1
    fi
    echo
    echo "[PASS] no ERROR-level entries in .log"
    exit 0
fi

# No .log file. Two possibilities:
#  a) workbench booted cleanly, never logged anything → PASS
#  b) workbench died early, never reached the Eclipse logging facility
# Disambiguate via stdout: a clean boot writes only JVM warnings (sun.misc.Unsafe etc)
# and no Java stack traces. A failed boot writes a Throwable.
if [ -s "$WORKSPACE/stdout.log" ] && grep -qE '(Exception|Throwable|^\s+at .+\.java:)' "$WORKSPACE/stdout.log"; then
    echo "  no .log written but stdout contains a stack trace:"
    echo
    grep -B1 -A8 'Exception\|Throwable' "$WORKSPACE/stdout.log" | head -30
    echo
    echo "[FAIL] workbench crashed before writing to .log"
    exit 1
fi

echo "  no .log file produced AND no Java stack trace in stdout"
echo "  -> Eclipse logged nothing => clean boot (no errors, no warnings)"
echo
echo "[PASS] workbench booted cleanly (silent .log)"
exit 0

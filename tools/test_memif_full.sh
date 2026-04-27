#!/usr/bin/env bash
# tools/test_memif_full.sh — M2.7: MemIf "全栈正确性" 一键回归。
#
# Steps (each must PASS to exit 0):
#   1. PYTHONPATH imports OK (5 native helpers + MemIf domain class)
#   2. generator runs on Demo_S32K148, produces MemIf_Cfg.{c,h,Bswmd.arxml}
#   3. generated MemIf_Cfg.h byte-equals V25.10 reference (after filter timestamps)
#   4. validator runs on Demo_S32K148: 0 errors (clean)
#   5. validator runs on Demo_S32K148_BAD_2170: TCPP_2170 fires
#   6. validator runs on Demo_S32K148_BAD_2171: TCPP_2171 fires
#   7. docs §15 patch reproducible: '#define MEMIF_MODULE_VERSION "TEST_PROBE_42_V25_10"' present
#
# Usage: ./tools/test_memif_full.sh   (exits 0 on success, 1 on first failure)

set -u
ROOT=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT"

PASS=0; FAIL=0
G="\033[32m"; R="\033[31m"; Y="\033[33m"; N="\033[0m"

ok()   { echo -e "  [${G}OK${N}]   $*"; PASS=$((PASS+1)); }
fail() { echo -e "  [${R}FAIL${N}] $*"; FAIL=$((FAIL+1)); }
sect() { echo; echo "=== $* ==="; }

OUT=/tmp/v01_memif_full

sect "1. import smoke"
if PYTHONPATH=core python3 -c "
from Common import BswBase, Public, CodeGenerator, Context, J2Filters
import sys; sys.path.insert(0,'generator/modules')
from MemIf.src.MemIf import MemIf, MemIfGeneral
" 2>/dev/null; then
    ok "5 helpers + MemIf domain class import"
else
    fail "imports broken"
fi

sect "2. generator runs on Demo_S32K148"
rm -rf "$OUT"
if PYTHONPATH=core python3 -m generator -g MemIf -i samples/Demo_S32K148 -o "$OUT" >/dev/null 2>&1; then
    ok "generator finished"
else
    fail "generator threw"
fi

sect "3. MemIf_Cfg.h diff vs V25.10 reference (filtered)"
if [ -f "$OUT/MemIf_Cfg.h" ]; then
    diff <(sed -E '/@(date|toolVersion)/d' "$OUT/MemIf_Cfg.h") \
         <(sed -E '/@(date|toolVersion)/d' samples/Demo_S32K148/config/MemIf_Cfg.h) > /tmp/diff_h.txt
    if [ ! -s /tmp/diff_h.txt ]; then
        ok "MemIf_Cfg.h byte-identical to reference"
    else
        fail "MemIf_Cfg.h diff: $(wc -l < /tmp/diff_h.txt) lines"
    fi
else
    fail "MemIf_Cfg.h not generated"
fi

sect "4. validator on baseline Demo_S32K148 (expect 0 errors)"
if PYTHONPATH=core python3 -m validator -m MemIf -i samples/Demo_S32K148 2>&1 | grep -q 'critical: 0 error: 0 warning: 0'; then
    ok "validator clean on baseline"
else
    fail "baseline triggered findings"
fi

sect "5. M2.3 — validator catches Rule_BSW_MemIf_TCPP_2170 in BAD_2170"
if [ -d samples/Demo_S32K148_BAD_2170 ]; then
    if PYTHONPATH=core python3 -m validator -m MemIf -i samples/Demo_S32K148_BAD_2170 2>&1 | grep -q 'TCPP_2170'; then
        ok "TCPP_2170 fires"
    else
        fail "TCPP_2170 did NOT fire"
    fi
else
    fail "samples/Demo_S32K148_BAD_2170 missing"
fi

sect "6. M2.4 — validator catches Rule_BSW_MemIf_TCPP_2171 in BAD_2171"
if [ -d samples/Demo_S32K148_BAD_2171 ]; then
    if PYTHONPATH=core python3 -m validator -m MemIf -i samples/Demo_S32K148_BAD_2171 2>&1 | grep -q 'TCPP_2171'; then
        ok "TCPP_2171 fires"
    else
        fail "TCPP_2171 did NOT fire"
    fi
else
    fail "samples/Demo_S32K148_BAD_2171 missing"
fi

sect "7. M2.5 — docs §15 patch reproduces (#define MEMIF_MODULE_VERSION)"
if grep -q '#define MEMIF_MODULE_VERSION "TEST_PROBE_42_V25_10"' "$OUT/MemIf_Cfg.h" 2>/dev/null; then
    ok "MEMIF_MODULE_VERSION line present with correct value"
else
    fail "MEMIF_MODULE_VERSION line missing or wrong value"
fi

echo
echo "=================================================================="
echo "  test_memif_full: PASS=$PASS  FAIL=$FAIL"
[ $FAIL -eq 0 ] && exit 0 || exit 1

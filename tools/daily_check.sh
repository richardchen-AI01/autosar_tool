#!/usr/bin/env bash
# Daily check runner — pick the right C / M tests for current sprint day.
# Usage: ./tools/daily_check.sh [day_number]
# If day_number omitted, uses today - sprint_start (default sprint_start=2026-04-27)

set -e
ROOT=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT"

SPRINT_START=${SPRINT_START:-2026-04-27}
DAY=${1:-}
if [ -z "$DAY" ]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        SPRINT_EPOCH=$(date -j -f "%Y-%m-%d" "$SPRINT_START" "+%s")
    else
        SPRINT_EPOCH=$(date -d "$SPRINT_START" "+%s")
    fi
    NOW_EPOCH=$(date "+%s")
    DAY=$(( (NOW_EPOCH - SPRINT_EPOCH) / 86400 + 1 ))
fi

echo "=================================================================="
echo "  Autosar_tool · Day $DAY / 14   (sprint start $SPRINT_START)"
echo "=================================================================="

PASS=0
FAIL=0
SKIP=0

run_check() {
    local name="$1"; shift
    local desc="$1"; shift
    if "$@" >/dev/null 2>&1; then
        printf "  [\033[32mOK\033[0m]    %-12s %s\n" "$name" "$desc"
        PASS=$((PASS+1))
    else
        printf "  [\033[31mFAIL\033[0m]  %-12s %s\n" "$name" "$desc"
        FAIL=$((FAIL+1))
    fi
}

skip() {
    local name="$1"; shift
    local desc="$1"; shift
    printf "  [\033[33mSKIP\033[0m]  %-12s %s\n" "$name" "$desc"
    SKIP=$((SKIP+1))
}

# ----------------------------------------------------------------- D1
if [ "$DAY" -ge 1 ]; then
    echo
    echo "--- D1: 项目骨架 ---"
    run_check "C1.1" "monorepo 树就位" \
        bash -c 'test -d core/Common && test -d generator/modules/MemIf && test -d validator/Bsw/MemIf'
    run_check "C1.2" "git 初始化" \
        bash -c 'git rev-parse --git-dir'
    run_check "C1.3" "reference 软链可用" \
        bash -c 'test -L reference/autosar-cfg && test -e reference/autosar-cfg/ORIENTAISBswGen.exe/data/MemIf/src/MemIf.py'
    run_check "C1.4" "MemIf 生成器代码已搬入" \
        bash -c 'test -f generator/modules/MemIf/src/MemIf.py'
fi

# ----------------------------------------------------------------- D2
if [ "$DAY" -ge 2 ]; then
    echo
    echo "--- D2: native helper + 最小 plugin ---"
    run_check "C2.1" "MemIf 用到的 5 个 native helper 可 import" \
        env PYTHONPATH=core python3 -c "
import importlib
for m in ['BswBase','Public','CodeGenerator','Context','J2Filters']:
    importlib.import_module(f'Common.{m}')
"
    run_check "C2.2" "MemIf 自家 .py 能 import" \
        env PYTHONPATH=core:generator/modules python3 -c "
from MemIf.src.MemIf import MemIf, MemIfGeneral
m = MemIf()
"
    run_check "C2.3" "MemIfRules 能 import" \
        env PYTHONPATH=core:validator python3 -c "
from Bsw.MemIf.MemIfRules import RuleBSWMemIfR23
RuleBSWMemIfR23()
"
fi

# ----------------------------------------------------------------- M1
if [ "$DAY" -ge 3 ]; then
    echo
    echo "--- M1: MemIf walking skeleton ---"
    run_check "M1.1" "5 个 native helper 可 import" \
        env PYTHONPATH=core python3 -c "
import importlib
for m in ['BswBase','Public','CodeGenerator','Context','J2Filters']:
    importlib.import_module(f'Common.{m}')
"
    run_check "M1.2" "BswBase 5 个方法签名" \
        env PYTHONPATH=core python3 -c "
from Common.BswBase import BswBase
for m in ['getAttrValue','getSubContainer','getIndex','getWholeIndex','getParentContainer']:
    assert hasattr(BswBase, m), f'missing {m}'
"
    skip "M1.3" "IDE 启动 + MemIf 节点 (D2-D3 实例 C 任务)"
    skip "M1.4" "OSGi MemIf bundle started (D2-D3 实例 C 任务)"
    skip "M1.5" "IDE 双击 MemIf 表单显示 (D3 任务)"
    skip "M1.6" "Generate 按钮调起 bswgen.exe (D3 任务)"
fi

# ----------------------------------------------------------------- 汇总
echo
echo "=================================================================="
TOTAL=$((PASS+FAIL+SKIP))
echo "  Result: PASS=$PASS  FAIL=$FAIL  SKIP=$SKIP   (total $TOTAL)"
if [ "$FAIL" -eq 0 ]; then
    if [ "$DAY" -le 1 ]; then echo "  Status: D1 on track (D2-D3 在 sprint plan §5)"
    elif [ "$DAY" -le 3 ]; then echo "  Status: heading toward M1 (D3 EOD)"
    elif [ "$DAY" -le 7 ]; then echo "  Status: heading toward M2 (D7 EOD)"
    elif [ "$DAY" -le 11 ]; then echo "  Status: heading toward M3 (D11 EOD)"
    else echo "  Status: heading toward M4 release (D14 EOD)"
    fi
    exit 0
else
    echo "  Status: \033[31mFAIL\033[0m count > 0; address before EOD"
    exit 1
fi

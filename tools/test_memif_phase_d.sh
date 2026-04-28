#!/usr/bin/env bash
#
# tools/test_memif_phase_d.sh — Phase D 验收（Validate / Generate handler 真用）
#
# 因为 handler 是 IDE-only（GUI 触发 → BswgenLauncher → Python 子进程），
# 完整 Java 端自动测试需要 Eclipse PDE headless launch；v0.1 不投入。
# 这里验：(a) handler 类已编进 ui jar，(b) BswgenLauncher 共享的 Python
# 端真路径 byte-equal vs reference，(c) bswval 输出格式跟 ValidateMemIfHandler
# 的 regex 一致（finding 解析成功）。
#
# 对应 docs/MILESTONES_memif_replica.md §Phase D
#
# Usage:
#   ./tools/test_memif_phase_d.sh

set -u
ROOT=$(cd "$(dirname "$0")/.." && pwd)
PASS=0
FAIL=0

G="\033[32m"; R="\033[31m"; Y="\033[33m"; N="\033[0m"
ok()   { echo -e "  [${G}OK${N}]   $*"; PASS=$((PASS+1)); }
fail() { echo -e "  [${R}FAIL${N}] $*"; FAIL=$((FAIL+1)); }
sect() { echo; echo "=== $* ==="; }

# --- D.0 / D.1 jar 类完整性 ---------------------------------------------------

check_jar() {
    sect "D.0 ui jar 含 Generate/Validate handler + Launcher"
    local ui_jar=$(ls -t "$ROOT"/ide/builder_core/cn.com.myorg.bswbuilder.ui/target/*-SNAPSHOT.jar 2>/dev/null | head -1)
    if [ -z "$ui_jar" ]; then
        fail "ui jar 不存在"
        return
    fi
    for cls in 'GenerateMemIfHandler\.class' 'ValidateMemIfHandler\.class' 'BswgenLauncher\.class' 'BswgenLauncher\$Result\.class'; do
        if unzip -l "$ui_jar" | grep -q "$cls"; then
            ok "ui jar 含 $cls"
        else
            fail "ui jar 缺 $cls"
        fi
    done
}

# --- D.2 Generate 输出 byte-equal vs reference --------------------------------

check_generate_byte_equal() {
    sect "D.2 Generate handler 共享的 bswgen 输出 byte-equal vs reference"
    local out=$(mktemp -d -t phase_d_gen.XXXXXX)
    trap "rm -rf $out" RETURN

    if PYTHONPATH=core:. python3 -m generator -g MemIf -i samples/Demo_S32K148 -o "$out" >/dev/null 2>&1; then
        ok "bswgen subprocess 退出 0"
    else
        fail "bswgen 失败 — 跑 'PYTHONPATH=core python3 -m generator -g MemIf -i samples/Demo_S32K148 -o /tmp/out' 看错误"
        return
    fi

    if [ -f "$out/MemIf_Cfg.h" ]; then
        ok "MemIf_Cfg.h 生成 (size=$(wc -c < "$out/MemIf_Cfg.h"))"
    else
        fail "MemIf_Cfg.h 没生成"
        return
    fi

    if diff <(sed -E '/@(date|toolVersion)/d' "$out/MemIf_Cfg.h") \
            <(sed -E '/@(date|toolVersion)/d' samples/Demo_S32K148/config/MemIf_Cfg.h) >/dev/null 2>&1; then
        ok "MemIf_Cfg.h byte-equal vs reference (filtered timestamps)"
    else
        fail "MemIf_Cfg.h diff vs reference"
    fi
}

# --- D.3 Validate handler 输出格式可解析 -------------------------------------

check_validate_finding_format() {
    sect "D.3 bswval 输出 finding 格式跟 ValidateMemIfHandler.FINDING_RE 一致"

    # ValidateMemIfHandler regex (Java 风格):
    #   ^\s*\[(\d+)\]\s+(\w+):\s+(.+?)\s+@\s+(\S+)\s*$
    # Python 等价：
    local out=$(mktemp -t phase_d_val.XXXXXX)
    PYTHONPATH=core:. python3 -m validator -m MemIf -i samples/Demo_S32K148_BAD_2170 > "$out" 2>&1 || true

    local matches
    matches=$(python3 -c "
import re, sys
p = re.compile(r'^\s*\[(\d+)\]\s+(\w+):\s+(.+?)\s+@\s+(\S+)\s*\$')
hits = []
for line in open('$out', 'r', encoding='utf-8').read().splitlines():
    m = p.match(line)
    if m:
        hits.append((m.group(1), m.group(2), m.group(4)))
for h in hits:
    print('  level=%s rule=%s ecuc=%s' % h)
print('---', len(hits))
" 2>&1)

    rm -f "$out"
    echo "$matches" | grep -E "^\s*level=" || true
    local total=$(echo "$matches" | tail -1 | awk '{print $2}')
    if [ "$total" = "1" ]; then
        ok "1 个 finding 解析成功（BAD_2170 应只触发 TCPP_2170）"
    elif [ "$total" -ge 1 ] 2>/dev/null; then
        ok "$total 个 finding 解析成功"
    else
        fail "0 个 finding — regex 不匹配 bswval 输出"
    fi

    # 验证一定包含 TCPP_2170
    if echo "$matches" | grep -q "TCPP_2170"; then
        ok "BAD_2170 fixture 触发 TCPP_2170 ✓"
    else
        fail "BAD_2170 fixture 没触发 TCPP_2170"
    fi
}

# --- D.4 Validate clean workspace 不产生 finding ----------------------------

check_validate_clean() {
    sect "D.4 clean workspace (Demo_S32K148) validate 无 finding"
    local out=$(mktemp -t phase_d_clean.XXXXXX)
    PYTHONPATH=core:. python3 -m validator -m MemIf -i samples/Demo_S32K148 > "$out" 2>&1
    local rc=$?

    if [ $rc -eq 0 ]; then
        ok "validate clean workspace 退出 0"
    else
        fail "validate clean workspace 退出 $rc"
    fi

    local finding_count
    finding_count=$(grep -E "^\s*\[[0-9]+\]\s+\w+:" "$out" | wc -l | tr -d ' ')
    rm -f "$out"
    if [ "$finding_count" = "0" ]; then
        ok "0 finding（clean workspace 应该 0）"
    else
        fail "$finding_count finding（clean workspace 应该 0）"
    fi
}

# ---- run ---
check_jar
check_generate_byte_equal
check_validate_finding_format
check_validate_clean

echo
echo "=================================="
echo "Phase D 算法验证: PASS=$PASS FAIL=$FAIL"
echo "=================================="
[ "$FAIL" -eq 0 ]

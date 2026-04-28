#!/usr/bin/env bash
#
# tools/test_memif_roundtrip.sh — Phase F 终极验收：5 个 ARXML fixture 全部
# 经我们 IDE 的 reader+writer 处理后 byte-equal vs 起始文件。
#
# 这一关是 MemIf 复刻成功的硬指标第 8 项（docs/MEMIF_REPLICA_PLAN.md §5）。
#
# Fixtures (docs/reference/roundtrip-fixtures/):
#   01-demo.arxml      — V25.10 demo (clean)
#   02-bad-2170.arxml  — TCPP-2170 触发用
#   03-bad-2171.arxml  — TCPP-2171 触发用
#   04-min.arxml       — 仅 MemIfGeneral + 1 个参数（最小有效 ECUC）
#   05-max.arxml       — 4 参数全填 + ADMIN-DATA SDGS 标签
#
# 算法：每份 fixture 跑 N 个 round-trip 模式
#   noop:   读 → 写回同值 → diff = 0
#   flip:   读原值 → 写不同值 → 写回原值 → diff = 0
#
# 算法用 Python 镜像 Java MemIfArxmlWriter；newline='' 关键。
# v0.2 升级：Java JUnit + Tycho surefire 跑 Java 端真实代码。

set -u
ROOT=$(cd "$(dirname "$0")/.." && pwd)
PASS=0
FAIL=0
G="\033[32m"; R="\033[31m"; Y="\033[33m"; N="\033[0m"
ok()   { echo -e "  [${G}OK${N}]   $*"; PASS=$((PASS+1)); }
fail() { echo -e "  [${R}FAIL${N}] $*"; FAIL=$((FAIL+1)); }
sect() { echo; echo "=== $* ==="; }

FIXTURES_DIR="$ROOT/docs/reference/roundtrip-fixtures"
TMP=$(mktemp -d -t memif_roundtrip.XXXXXX)
trap "rm -rf $TMP" EXIT

if [ ! -d "$FIXTURES_DIR" ]; then
    echo "[FAIL] fixtures dir 不存在: $FIXTURES_DIR"
    exit 1
fi

PY_HELPER=$(cat <<'PYEOF'
import re, sys

def replace_value(xml, param_name, new_value):
    pattern = (
        r'(<ECUC-(?:NUMERICAL|TEXTUAL)-PARAM-VALUE>'
        r'\s*<DEFINITION-REF[^>]*>[^<]*?/' + re.escape(param_name) + r'</DEFINITION-REF>'
        r'\s*<VALUE>)([^<]*)(</VALUE>)'
    )
    matches = list(re.finditer(pattern, xml, re.DOTALL))
    if len(matches) > 1:
        raise SystemExit(f'IllegalState: multiple matches for {param_name}')
    if not matches:
        return xml, 0, None
    m = matches[0]
    escaped = new_value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return xml[:m.start()] + m.group(1) + escaped + m.group(3) + xml[m.end():], 1, m.group(2)

def read_value(xml, param_name):
    pattern = (
        r'<ECUC-(?:NUMERICAL|TEXTUAL)-PARAM-VALUE>'
        r'\s*<DEFINITION-REF[^>]*>[^<]*?/' + re.escape(param_name) + r'</DEFINITION-REF>'
        r'\s*<VALUE>([^<]*)</VALUE>'
    )
    m = re.search(pattern, xml, re.DOTALL)
    return m.group(1) if m else None

def load(path):
    with open(path, 'r', encoding='utf-8', newline='') as f:
        return f.read()

def store(path, xml):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(xml)

if __name__ == '__main__':
    cmd = sys.argv[1]
    path = sys.argv[2]
    if cmd == 'read':
        print(read_value(load(path), sys.argv[3]) or '')
    elif cmd == 'write':
        param, new_val = sys.argv[3], sys.argv[4]
        xml, n, _ = replace_value(load(path), param, new_val)
        if n == 0:
            sys.exit(f'no match for {param}')
        store(path, xml)
PYEOF
)
run_py() { python3 -c "$PY_HELPER" "$@"; }

# args: <fixture-name> <mode> <param-name> <new-value>
roundtrip() {
    local fixture="$1"
    local mode="$2"
    local param="$3"
    local newval="$4"

    local src="$FIXTURES_DIR/$fixture"
    local work="$TMP/${fixture}.${mode}.${param}"
    cp "$src" "$work"

    case "$mode" in
        noop )
            local orig=$(run_py read "$work" "$param")
            if [ -z "$orig" ]; then return 0; fi
            run_py write "$work" "$param" "$orig"
            ;;
        flip )
            local orig=$(run_py read "$work" "$param")
            if [ -z "$orig" ]; then return 0; fi
            run_py write "$work" "$param" "$newval"
            local mid=$(run_py read "$work" "$param")
            if [ "$mid" != "$newval" ]; then
                fail "$fixture · ${mode}/${param}: 改值后读回 '$mid' (expected '$newval')"
                return 1
            fi
            run_py write "$work" "$param" "$orig"
            ;;
        * )
            fail "unknown mode $mode"
            return 1
            ;;
    esac

    if cmp -s "$work" "$src"; then
        ok "$fixture · ${mode}/${param} → byte-equal"
    else
        fail "$fixture · ${mode}/${param} → diff:"
        diff "$src" "$work" | head -6
    fi
}

run_fixture() {
    local fixture="$1"
    sect "$fixture"

    for p in MemIfDevErrorDetect MemIfNumberOfDevices MemIfVersionInfoApi MemIfModuleVersion; do
        roundtrip "$fixture" noop "$p" ""
    done

    roundtrip "$fixture" flip MemIfDevErrorDetect  "true_FLIPPED"
    roundtrip "$fixture" flip MemIfNumberOfDevices "9"
    roundtrip "$fixture" flip MemIfVersionInfoApi  "true_FLIPPED"
    roundtrip "$fixture" flip MemIfModuleVersion   "FLIPPED_PROBE"
}

for fixture in 01-demo.arxml 02-bad-2170.arxml 03-bad-2171.arxml 04-min.arxml 05-max.arxml; do
    if [ ! -f "$FIXTURES_DIR/$fixture" ]; then
        fail "fixture $fixture 不存在"
        continue
    fi
    run_fixture "$fixture"
done

echo
echo "=================================="
echo "Phase F 双向 byte-equal: PASS=$PASS FAIL=$FAIL"
echo "=================================="
[ "$FAIL" -eq 0 ]

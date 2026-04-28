#!/usr/bin/env bash
#
# tools/test_memif_phase_b.sh — Phase B 验收脚本（先验最难的 byte-equal
# round-trip，再验改值持久化）。Java 端的 MemIfArxmlWriter 用同款 regex；
# 这里用 Python 跑等价算法，证明算法本身在真实 demo ARXML 上 byte-perfect。
#
# 对应 docs/MILESTONES_memif_replica.md §Phase B
#
# Usage:
#   ./tools/test_memif_phase_b.sh                       # 全跑
#   ./tools/test_memif_phase_b.sh --check noop          # 只 noop round-trip
#   ./tools/test_memif_phase_b.sh --check write-read    # 只改值再读

set -u
ROOT=$(cd "$(dirname "$0")/.." && pwd)
PASS=0
FAIL=0

G="\033[32m"; R="\033[31m"; Y="\033[33m"; N="\033[0m"
ok()   { echo -e "  [${G}OK${N}]   $*"; PASS=$((PASS+1)); }
fail() { echo -e "  [${R}FAIL${N}] $*"; FAIL=$((FAIL+1)); }
sect() { echo; echo "=== $* ==="; }

DEMO="$ROOT/samples/Demo_S32K148/BSW_Builder/S32K148/MemIf.arxml"
TMP=$(mktemp -d -t memif_phase_b.XXXXXX)
trap "rm -rf $TMP" EXIT

if [ ! -f "$DEMO" ]; then
    echo "[FAIL] demo arxml 不存在: $DEMO"
    exit 1
fi

# --- Python helper: same regex as MemIfArxmlWriter.java ----------------------
PY_HELPER=$(cat <<'PYEOF'
import re, sys

def replace_value(xml, param_name, new_value):
    """Mirrors Java MemIfArxmlWriter.replaceParamValue regex 1:1.
    Returns (new_xml, n_matches)."""
    pattern = (
        r'(<ECUC-(?:NUMERICAL|TEXTUAL)-PARAM-VALUE>'
        r'\s*<DEFINITION-REF[^>]*>[^<]*?/' + re.escape(param_name) + r'</DEFINITION-REF>'
        r'\s*<VALUE>)([^<]*)(</VALUE>)'
    )
    matches = list(re.finditer(pattern, xml, re.DOTALL))
    if len(matches) > 1:
        raise SystemExit(f'IllegalState: multiple matches for {param_name}')
    if len(matches) == 0:
        return xml, 0
    m = matches[0]
    escaped = new_value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return xml[:m.start()] + m.group(1) + escaped + m.group(3) + xml[m.end():], 1

if __name__ == '__main__':
    cmd = sys.argv[1]  # read | write | noop
    path = sys.argv[2]
    if cmd == 'read':
        param = sys.argv[3]
        with open(path, 'r', encoding='utf-8', newline='') as f:
            xml = f.read()
        pattern = (
            r'<ECUC-(?:NUMERICAL|TEXTUAL)-PARAM-VALUE>'
            r'\s*<DEFINITION-REF[^>]*>[^<]*?/' + re.escape(param) + r'</DEFINITION-REF>'
            r'\s*<VALUE>([^<]*)</VALUE>'
        )
        m = re.search(pattern, xml, re.DOTALL)
        print(m.group(1) if m else '')
    elif cmd == 'write':
        param, new_val = sys.argv[3], sys.argv[4]
        with open(path, 'r', encoding='utf-8', newline='') as f:
            xml = f.read()
        new_xml, n = replace_value(xml, param, new_val)
        if n == 0:
            sys.exit(f'no match for {param}')
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(new_xml)
    elif cmd == 'noop-roundtrip':
        # write the SAME value the file already has — should produce byte-equal output
        param = sys.argv[3]
        with open(path, 'r', encoding='utf-8', newline='') as f:
            xml = f.read()
        pattern = (
            r'<ECUC-(?:NUMERICAL|TEXTUAL)-PARAM-VALUE>'
            r'\s*<DEFINITION-REF[^>]*>[^<]*?/' + re.escape(param) + r'</DEFINITION-REF>'
            r'\s*<VALUE>([^<]*)</VALUE>'
        )
        m = re.search(pattern, xml, re.DOTALL)
        if not m:
            sys.exit(f'no match for {param}')
        original_value = m.group(1)
        new_xml, n = replace_value(xml, param, original_value)
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(new_xml)
PYEOF
)

run_py() { python3 -c "$PY_HELPER" "$@"; }

# --- Tests -------------------------------------------------------------------

check_noop_roundtrip() {
    sect "B.3 noop round-trip → byte-equal vs original"

    cp "$DEMO" "$TMP/file.arxml"

    # Read current value (should be '2')
    local original_value
    original_value=$(run_py read "$TMP/file.arxml" MemIfNumberOfDevices)
    if [ "$original_value" = "2" ]; then
        ok "demo MemIfNumberOfDevices = 2 as expected"
    else
        fail "demo MemIfNumberOfDevices = '$original_value' (expected 2) — demo file 改过？"
        return
    fi

    # Re-write the same value
    run_py noop-roundtrip "$TMP/file.arxml" MemIfNumberOfDevices

    if cmp -s "$TMP/file.arxml" "$DEMO"; then
        ok "noop write 后文件 byte-equal vs original"
    else
        fail "noop write 后产生差异 — string surgery 算法有问题"
        diff "$DEMO" "$TMP/file.arxml" | head -10
    fi
}

check_write_read() {
    sect "B.2 改值 → 读回 → 验值 → 改回 → 验 byte-equal"

    cp "$DEMO" "$TMP/file2.arxml"

    # 改成 1
    run_py write "$TMP/file2.arxml" MemIfNumberOfDevices 1
    local v1=$(run_py read "$TMP/file2.arxml" MemIfNumberOfDevices)
    if [ "$v1" = "1" ]; then
        ok "改值 2→1 持久化"
    else
        fail "改值后读回 = '$v1' (expected 1)"
    fi

    # 改回 2
    run_py write "$TMP/file2.arxml" MemIfNumberOfDevices 2
    local v2=$(run_py read "$TMP/file2.arxml" MemIfNumberOfDevices)
    if [ "$v2" = "2" ]; then
        ok "改值 1→2 持久化"
    else
        fail "改回后读回 = '$v2' (expected 2)"
    fi

    if cmp -s "$TMP/file2.arxml" "$DEMO"; then
        ok "改 1 又改 2 后 byte-equal vs original (round-trip 闭环)"
    else
        fail "round-trip 后产生差异"
        diff "$DEMO" "$TMP/file2.arxml" | head -10
    fi
}

check_all_four_params() {
    sect "B.x 4 个参数都能 round-trip"

    for param in MemIfDevErrorDetect MemIfNumberOfDevices MemIfVersionInfoApi MemIfModuleVersion; do
        cp "$DEMO" "$TMP/p.arxml"
        local orig=$(run_py read "$TMP/p.arxml" "$param")
        run_py noop-roundtrip "$TMP/p.arxml" "$param"
        if cmp -s "$TMP/p.arxml" "$DEMO"; then
            ok "$param noop byte-equal (orig=$orig)"
        else
            fail "$param noop produces diff"
        fi
    done
}

check_jar_class() {
    sect "B.0 MemIfArxmlWriter 在 jar 里"
    local jar=$(ls -t "$ROOT"/ide/modules/cn.com.myorg.bswbuilder.modules.memif/target/*-SNAPSHOT.jar 2>/dev/null | head -1)
    if [ -z "$jar" ]; then
        fail "memif jar 不存在 — 跑 mvn package 先"
        return
    fi
    if unzip -l "$jar" | grep -q 'MemIfArxmlWriter\.class'; then
        ok "MemIfArxmlWriter.class 已编进 jar"
    else
        fail "MemIfArxmlWriter.class 缺失"
    fi
}

# --- Dispatch ----------------------------------------------------------------

mode="${1:-}"
case "$mode" in
    --check )
        case "${2:-}" in
            noop ) check_noop_roundtrip ;;
            write-read ) check_write_read ;;
            all-four ) check_all_four_params ;;
            jar ) check_jar_class ;;
            * ) echo "Unknown check"; exit 2 ;;
        esac
        ;;
    "" )
        check_jar_class
        check_noop_roundtrip
        check_write_read
        check_all_four_params
        ;;
    * ) echo "Usage: $0 [--check noop|write-read|all-four|jar]"; exit 2 ;;
esac

echo
echo "=================================="
echo "Phase B 算法验证: PASS=$PASS FAIL=$FAIL"
echo "=================================="
[ "$FAIL" -eq 0 ]

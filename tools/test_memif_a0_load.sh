#!/usr/bin/env bash
#
# tools/test_memif_a0_load.sh — A0 fix 验证脚本（OSGi-runtime 模式）
#
# 用 Mac launcher 的 --test-load=<path> 启动模式：Application.start() 看到
# 这个 arg 就跳过 workbench 直接跑 MemIfArxmlReader.read()，证明：
#   (1) 不再抛 FeatureNotFoundException: Feature 'AR-PACKAGES' not found
#   (2) 返回 4 个 MemIfGeneral 参数的预期值
#
# 这是真正在 OSGi 容器里跑的，class loader 跟用户点 GUI 时一致。

set -u
ROOT=$(cd "$(dirname "$0")/.." && pwd)
LAUNCHER="$ROOT/ide/product/cn.com.myorg.bswbuilder.product/target/products/cn.com.myorg.bswbuilder.product/macosx/cocoa/aarch64/Eclipse.app/Contents/MacOS/bswbuilder"
DEMO="$ROOT/samples/Demo_S32K148/BSW_Builder/S32K148/MemIf.arxml"
WORKSPACE=$(mktemp -d -t a0_load_test.XXXXXX)
trap "rm -rf $WORKSPACE" EXIT

if [ ! -x "$LAUNCHER" ]; then
    echo "[FAIL] launcher 不存在: $LAUNCHER"
    echo "       先跑 'mvn -B -f ide/pom.xml clean package -DskipTests'"
    exit 1
fi
if [ ! -f "$DEMO" ]; then
    echo "[FAIL] demo arxml 不存在: $DEMO"
    exit 1
fi

OUT_LOG="$WORKSPACE/probe.log"
echo "[A0] launching headless probe ..."
"$LAUNCHER" \
    -consoleLog \
    -clearPersistedState \
    -data "$WORKSPACE" \
    --test-load="$DEMO" \
    > "$OUT_LOG" 2>&1
RC=$?

echo "[A0] launcher exit code = $RC"
echo "----- A0_PROBE log lines -----"
grep "A0_PROBE:" "$OUT_LOG" || echo "(no A0_PROBE lines — see full log below)"
echo "------------------------------"

PASS=0; FAIL=0
G="\033[32m"; R="\033[31m"; N="\033[0m"
ok()   { echo -e "  [${G}OK${N}]   $*"; PASS=$((PASS+1)); }
fail() { echo -e "  [${R}FAIL${N}] $*"; FAIL=$((FAIL+1)); }

if grep -q "A0_PROBE: STATUS=PASS" "$OUT_LOG"; then
    ok "headless probe reached STATUS=PASS"
else
    fail "no STATUS=PASS in output"
fi

# Verify expected demo values
expect_kv() {
    local key="$1" expect="$2"
    local got=$(grep "A0_PROBE: $key=" "$OUT_LOG" | head -1 | sed -E "s/.*$key=//")
    if [ "$got" = "$expect" ]; then
        ok "$key = $expect"
    else
        fail "$key got '$got' (expected '$expect')"
    fi
}
expect_kv "DevErrorDetect"  "false"
expect_kv "NumberOfDevices" "2"
expect_kv "VersionInfoApi"  "false"
expect_kv "ModuleVersion"   "TEST_PROBE_42_V25_10"

# Should NOT contain the old bug
if grep -q "Feature 'AR-PACKAGES' not found" "$OUT_LOG"; then
    fail "FeatureNotFoundException 仍然存在 — 修复回归了"
else
    ok "no 'AR-PACKAGES not found' error in log (回归不存在)"
fi

echo
if [ $FAIL -eq 0 ]; then
    echo "=================================="
    echo "A0 EMF Load 修复 OSGi 验证 PASS ✅ ($PASS/$PASS)"
    echo "=================================="
    exit 0
else
    echo "=================================="
    echo "A0 EMF Load 修复 验证 FAIL ($FAIL fail / $PASS ok)"
    echo "=================================="
    echo
    echo "===== 完整 launcher 输出 (debug) ====="
    cat "$OUT_LOG"
    exit 1
fi

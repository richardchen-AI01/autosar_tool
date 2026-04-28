#!/usr/bin/env bash
#
# tools/test_memif_phase_c.sh — Phase C 验收（Auto-fill 算法层）
#
# 现造 4 个 fixture（C0/C1/C2/C3），对每个跑算法，验返回值匹配真值表。
# 算法用 Python 镜像 Java MemIfDerivedCalculator.calculateFromXml 的逻辑。
# 也跑一次 Java jar 内 class 是否到位的检查。
#
# 对应 docs/MILESTONES_memif_replica.md §Phase C
#         docs/reference/memif-derived-truth-table.md
#
# Usage:
#   ./tools/test_memif_phase_c.sh                      # 全跑
#   ./tools/test_memif_phase_c.sh --check four-combos  # 只 4 组合
#   ./tools/test_memif_phase_c.sh --check python-vs-java # 同一 fixture Java 算 vs Python 算

set -u
ROOT=$(cd "$(dirname "$0")/.." && pwd)
PASS=0
FAIL=0

G="\033[32m"; R="\033[31m"; Y="\033[33m"; N="\033[0m"
ok()   { echo -e "  [${G}OK${N}]   $*"; PASS=$((PASS+1)); }
fail() { echo -e "  [${R}FAIL${N}] $*"; FAIL=$((FAIL+1)); }
sect() { echo; echo "=== $* ==="; }

TMP=$(mktemp -d -t memif_phase_c.XXXXXX)
trap "rm -rf $TMP" EXIT

# --- Fixture builder ---------------------------------------------------------
# 4 minimal NvM.arxml stubs covering C0/C1/C2/C3 from the truth table.
# Real V25.10 NvM.arxml is much bigger; for derived-calc we only need the
# SHORT-NAME=NvMFeeRef / NvMEaRef markers under NvMTargetBlockReference.

write_fixture_C0() {  # neither Fee nor Ea
    cat > "$1" <<'XML'
<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>NvM</SHORT-NAME>
      <ELEMENTS>
        <ECUC-CONTAINER-VALUE>
          <SHORT-NAME>NvMBlockDescriptor_0</SHORT-NAME>
          <SUB-CONTAINERS>
            <ECUC-CONTAINER-VALUE>
              <SHORT-NAME>NvMTargetBlockReference</SHORT-NAME>
              <!-- intentionally empty: no Fee no Ea -->
            </ECUC-CONTAINER-VALUE>
          </SUB-CONTAINERS>
        </ECUC-CONTAINER-VALUE>
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
XML
}

write_fixture_C1() {  # only Fee
    cat > "$1" <<'XML'
<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>NvM</SHORT-NAME>
      <ELEMENTS>
        <ECUC-CONTAINER-VALUE>
          <SHORT-NAME>NvMBlockDescriptor_0</SHORT-NAME>
          <SUB-CONTAINERS>
            <ECUC-CONTAINER-VALUE>
              <SHORT-NAME>NvMTargetBlockReference</SHORT-NAME>
              <SUB-CONTAINERS>
                <ECUC-CONTAINER-VALUE>
                  <SHORT-NAME>NvMFeeRef</SHORT-NAME>
                </ECUC-CONTAINER-VALUE>
              </SUB-CONTAINERS>
            </ECUC-CONTAINER-VALUE>
          </SUB-CONTAINERS>
        </ECUC-CONTAINER-VALUE>
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
XML
}

write_fixture_C2() {  # only Ea
    cat > "$1" <<'XML'
<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>NvM</SHORT-NAME>
      <ELEMENTS>
        <ECUC-CONTAINER-VALUE>
          <SHORT-NAME>NvMBlockDescriptor_0</SHORT-NAME>
          <SUB-CONTAINERS>
            <ECUC-CONTAINER-VALUE>
              <SHORT-NAME>NvMTargetBlockReference</SHORT-NAME>
              <SUB-CONTAINERS>
                <ECUC-CONTAINER-VALUE>
                  <SHORT-NAME>NvMEaRef</SHORT-NAME>
                </ECUC-CONTAINER-VALUE>
              </SUB-CONTAINERS>
            </ECUC-CONTAINER-VALUE>
          </SUB-CONTAINERS>
        </ECUC-CONTAINER-VALUE>
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
XML
}

write_fixture_C3() {  # both Fee and Ea
    cat > "$1" <<'XML'
<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>NvM</SHORT-NAME>
      <ELEMENTS>
        <ECUC-CONTAINER-VALUE>
          <SHORT-NAME>NvMBlockDescriptor_0</SHORT-NAME>
          <SUB-CONTAINERS>
            <ECUC-CONTAINER-VALUE>
              <SHORT-NAME>NvMTargetBlockReference</SHORT-NAME>
              <SUB-CONTAINERS>
                <ECUC-CONTAINER-VALUE>
                  <SHORT-NAME>NvMFeeRef</SHORT-NAME>
                </ECUC-CONTAINER-VALUE>
                <ECUC-CONTAINER-VALUE>
                  <SHORT-NAME>NvMEaRef</SHORT-NAME>
                </ECUC-CONTAINER-VALUE>
              </SUB-CONTAINERS>
            </ECUC-CONTAINER-VALUE>
          </SUB-CONTAINERS>
        </ECUC-CONTAINER-VALUE>
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
XML
}

# --- Algorithm (mirror of Java MemIfDerivedCalculator.calculateFromXml) -----
PY_HELPER=$(cat <<'PYEOF'
import re, sys
def derive(xml):
    has_fee = bool(re.search(r'<SHORT-NAME>NvMFeeRef</SHORT-NAME>', xml))
    has_ea  = bool(re.search(r'<SHORT-NAME>NvMEaRef</SHORT-NAME>',  xml))
    return (1 if has_fee else 0) + (1 if has_ea else 0)
if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8', newline='') as f:
        xml = f.read()
    print(derive(xml))
PYEOF
)

run_py() { python3 -c "$PY_HELPER" "$@"; }

# --- Tests -------------------------------------------------------------------

check_jar_class() {
    sect "C.0 MemIfDerivedCalculator.class 已编进 jar"
    local jar=$(ls -t "$ROOT"/ide/modules/cn.com.myorg.bswbuilder.modules.memif/target/*-SNAPSHOT.jar 2>/dev/null | head -1)
    if [ -z "$jar" ]; then
        fail "memif jar 不存在"
        return
    fi
    if unzip -l "$jar" | grep -q 'MemIfDerivedCalculator\.class'; then
        ok "MemIfDerivedCalculator.class 在 jar 里"
    else
        fail "MemIfDerivedCalculator.class 缺 — 跑 mvn package 先"
    fi
}

check_four_combos() {
    sect "C.3 四组合 (C0/C1/C2/C3) 算法验证"

    write_fixture_C0 "$TMP/c0.arxml"; local v0=$(run_py "$TMP/c0.arxml")
    if [ "$v0" = "0" ]; then ok "C0 (neither) → 0"; else fail "C0 → $v0 (expected 0)"; fi

    write_fixture_C1 "$TMP/c1.arxml"; local v1=$(run_py "$TMP/c1.arxml")
    if [ "$v1" = "1" ]; then ok "C1 (only Fee) → 1"; else fail "C1 → $v1 (expected 1)"; fi

    write_fixture_C2 "$TMP/c2.arxml"; local v2=$(run_py "$TMP/c2.arxml")
    if [ "$v2" = "1" ]; then ok "C2 (only Ea) → 1"; else fail "C2 → $v2 (expected 1)"; fi

    write_fixture_C3 "$TMP/c3.arxml"; local v3=$(run_py "$TMP/c3.arxml")
    if [ "$v3" = "2" ]; then ok "C3 (both) → 2"; else fail "C3 → $v3 (expected 2)"; fi
}

check_python_vs_java() {
    sect "C.4 Python 算法 vs Java 算法 (基于 jar bytecode 反汇编)"
    # 我们用 javap -c 看 Java MemIfDerivedCalculator.calculateFromXml 的字节码，
    # 验证它 import 的是同一个 SHORT-NAME pattern。这只是 sanity check，不
    # 真跑 JVM。Java 端真正的运行时一致性靠 Phase D 的端到端 IDE 测试再验。

    local jar=$(ls -t "$ROOT"/ide/modules/cn.com.myorg.bswbuilder.modules.memif/target/*-SNAPSHOT.jar 2>/dev/null | head -1)
    if [ -z "$jar" ]; then
        fail "memif jar 不存在"
        return
    fi
    local out
    out=$(javap -classpath "$jar" -c cn.com.myorg.bswbuilder.modules.memif.data.MemIfDerivedCalculator 2>&1 || echo "ERROR")
    if echo "$out" | grep -q "<SHORT-NAME>NvMFeeRef</SHORT-NAME>"; then
        ok "Java bytecode 含 NvMFeeRef pattern (跟 Python 一致)"
    else
        fail "Java bytecode 没找到 NvMFeeRef pattern"
    fi
    if echo "$out" | grep -q "<SHORT-NAME>NvMEaRef</SHORT-NAME>"; then
        ok "Java bytecode 含 NvMEaRef pattern"
    else
        fail "Java bytecode 没找到 NvMEaRef pattern"
    fi
}

check_existing_demos() {
    sect "C.5 现有 demo workspace 上跑算法（应该全是 C1）"

    for ws in samples/Demo_S32K148 samples/Demo_S32K148_BAD_2170 samples/Demo_S32K148_BAD_2171; do
        local nvm="$ROOT/$ws/BSW_Builder/S32K148/NvM.arxml"
        if [ ! -f "$nvm" ]; then
            fail "$ws/.../NvM.arxml 不存在"
            continue
        fi
        local v=$(run_py "$nvm")
        if [ "$v" = "1" ]; then
            ok "$ws → derived = 1 (C1 = only Fee)"
        else
            fail "$ws → derived = $v (expected 1, see truth table 的 'demo workspace 覆盖度' 表)"
        fi
    done
}

# --- Dispatch ----------------------------------------------------------------
mode="${1:-}"
case "$mode" in
    --check )
        case "${2:-}" in
            jar ) check_jar_class ;;
            four-combos ) check_four_combos ;;
            python-vs-java ) check_python_vs_java ;;
            existing-demos ) check_existing_demos ;;
            * ) echo "Unknown check"; exit 2 ;;
        esac
        ;;
    "" )
        check_jar_class
        check_four_combos
        check_python_vs_java
        check_existing_demos
        ;;
    * ) echo "Usage: $0 [--check jar|four-combos|python-vs-java|existing-demos]"; exit 2 ;;
esac

echo
echo "=================================="
echo "Phase C 算法验证: PASS=$PASS FAIL=$FAIL"
echo "=================================="
[ "$FAIL" -eq 0 ]

#!/usr/bin/env bash
#
# tools/test_memif_phase_e.sh — Phase E 验收（Properties tabs）
#
# Phase E 主体是 GUI（focus widget → 底部 3 tab 显示 schema metadata），
# 自动验只能查 jar 类完整性 + metadata 内容覆盖度。视觉手测见 §E.6 prompt。
#
# 对应 docs/MILESTONES_memif_replica.md §Phase E

set -u
ROOT=$(cd "$(dirname "$0")/.." && pwd)
PASS=0
FAIL=0
G="\033[32m"; R="\033[31m"; Y="\033[33m"; N="\033[0m"
ok()   { echo -e "  [${G}OK${N}]   $*"; PASS=$((PASS+1)); }
fail() { echo -e "  [${R}FAIL${N}] $*"; FAIL=$((FAIL+1)); }
sect() { echo; echo "=== $* ==="; }

check_jar() {
    sect "E.0 jar 含 MemIfParamMetadata + PropertyFormView 含 tab 字段"
    local memif_jar=$(ls -t "$ROOT"/ide/modules/cn.com.myorg.bswbuilder.modules.memif/target/*-SNAPSHOT.jar 2>/dev/null | head -1)
    local ui_jar=$(ls -t "$ROOT"/ide/builder_core/cn.com.myorg.bswbuilder.ui/target/*-SNAPSHOT.jar 2>/dev/null | head -1)

    if [ -z "$memif_jar" ] || [ -z "$ui_jar" ]; then
        fail "jar 不存在 — 跑 mvn package 先"
        return
    fi

    if unzip -l "$memif_jar" | grep -q 'MemIfParamMetadata\.class'; then
        ok "memif jar 含 MemIfParamMetadata.class"
    else
        fail "memif jar 缺 MemIfParamMetadata.class"
    fi

    if unzip -l "$memif_jar" | grep -q 'MemIfParamMetadata\$Entry\.class'; then
        ok "memif jar 含 MemIfParamMetadata\$Entry.class"
    else
        fail "memif jar 缺 MemIfParamMetadata\$Entry.class"
    fi

    # PropertyFormView 应该引用 TabFolder/TabItem (在 constant pool 里能找到)
    if javap -classpath "$ui_jar" -v cn.com.myorg.bswbuilder.ui.views.PropertyFormView 2>&1 | grep -qE "TabFolder|TabItem"; then
        ok "PropertyFormView 引用了 TabFolder/TabItem"
    else
        fail "PropertyFormView 没找到 TabFolder/TabItem 引用"
    fi
}

check_metadata_coverage() {
    sect "E.1 4 个参数的 metadata 都到位"
    local memif_jar=$(ls -t "$ROOT"/ide/modules/cn.com.myorg.bswbuilder.modules.memif/target/*-SNAPSHOT.jar 2>/dev/null | head -1)
    if [ -z "$memif_jar" ]; then
        fail "memif jar 不存在"
        return
    fi
    local strings_out
    strings_out=$(javap -classpath "$memif_jar" -c -p cn.com.myorg.bswbuilder.modules.memif.data.MemIfParamMetadata 2>&1)
    for param in MemIfDevErrorDetect MemIfNumberOfDevices MemIfVersionInfoApi MemIfModuleVersion; do
        if echo "$strings_out" | grep -q "$param"; then
            ok "metadata 含 $param"
        else
            fail "metadata 缺 $param"
        fi
    done

    # 验关键字段（spec 描述至少一个特征字符串）
    if echo "$strings_out" | grep -q "Concrete number of underlying memory abstraction modules"; then
        ok "NumberOfDevices 描述（来自 AUTOSAR R23-11 spec）就位"
    else
        fail "NumberOfDevices spec description 缺"
    fi

    if echo "$strings_out" | grep -q "ECUC-INTEGER-PARAM-DEF"; then
        ok "Definition tab 内容含 ECUC-INTEGER-PARAM-DEF type"
    else
        fail "Definition tab 缺类型信息"
    fi
}

check_visual_prompt() {
    sect "E.6 (手测) — Properties tabs 视觉验证"
    cat <<'EOF'
  操作（在前台 RCP 里）：
    1. 启动 RCP，按 Phase A 流程加载 demo workspace 的 MemIf.arxml
    2. PropertyForm 视图右下角应该出现 3 个 tab：
         [Description] [Definition] [Status]
    3. 点 NumberOfDevices 输入框（让它获取 focus）
    4. **预期**：
       - Description tab 显示
           "Concrete number of underlying memory abstraction modules.

            Calculation Formula: Count number of configured EA and FEE modules."
       - Definition tab 显示
           Parameter: MemIfNumberOfDevices
           Type:      ECUC-INTEGER-PARAM-DEF (MIN = 1, MAX = 2)
           Origin:    AUTOSAR_ECUC
           Default:   (no default; derived from NvM EA/FEE block references)
       - Status tab 显示
           Current value: <当前值>
           Original:      <加载时的值>
           Dirty:         no
           Derived:       1 (C1 or C2 — single backend)
    5. 切到 ModuleVersion 输入框 → 3 个 tab 都自动刷新
    6. 改一下 NumberOfDevices 值（不点 Save），切回 Status tab → Dirty 应该 = "yes (unsaved)"

  4 个步骤都符合预期 → Phase E 手测 PASS
EOF
    echo -e "  [${Y}MANUAL${N}] 这部分需前台 RCP 验，自动 ide_smoke 8 秒不够"
}

check_jar
check_metadata_coverage
check_visual_prompt

echo
echo "=================================="
echo "Phase E 自动部分: PASS=$PASS FAIL=$FAIL"
echo "=================================="
[ "$FAIL" -eq 0 ]

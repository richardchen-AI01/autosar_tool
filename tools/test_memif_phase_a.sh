#!/usr/bin/env bash
#
# tools/test_memif_phase_a.sh — Phase A 验收脚本（自动可检 + 手测 prompt）
#
# 对应 docs/MILESTONES_memif_replica.md §Phase A — 只读看
# 退出码 0 = 全部 PASS；非 0 = 有失败
#
# Usage:
#   ./tools/test_memif_phase_a.sh                    # 全跑（自动 + 手测）
#   ./tools/test_memif_phase_a.sh --auto             # 只跑能自动判定的
#   ./tools/test_memif_phase_a.sh --check <name>     # 只跑某一项
#                                                       sphinx-ext / tree-node /
#                                                       form-readonly / jar-classes /
#                                                       boot-clean

set -u
ROOT=$(cd "$(dirname "$0")/.." && pwd)
PASS=0
FAIL=0

G="\033[32m"; R="\033[31m"; Y="\033[33m"; N="\033[0m"
ok()   { echo -e "  [${G}OK${N}]   $*"; PASS=$((PASS+1)); }
fail() { echo -e "  [${R}FAIL${N}] $*"; FAIL=$((FAIL+1)); }
sect() { echo; echo "=== $* ==="; }

mode="${1:-}"
case "$mode" in
    --auto|"" ) ;;
    --check ) ;;
    * ) echo "Usage: $0 [--auto|--check <name>]"; exit 2 ;;
esac

# ---- Helpers ----------------------------------------------------------------

check_jar_classes() {
    sect "A.1 memif schema + Phase A classes 都在 jar 里"

    local memif_jar=$(ls -t "$ROOT"/ide/modules/cn.com.myorg.bswbuilder.modules.memif/target/*-SNAPSHOT.jar 2>/dev/null | head -1)
    if [ -z "$memif_jar" ]; then
        fail "memif jar 不存在 — 先跑 'mvn -B -f ide/pom.xml clean package -DskipTests'"
        return
    fi

    if unzip -l "$memif_jar" | grep -q 'MemIfDef\.arxml'; then
        ok "memif jar 含 MemIfDef.arxml"
    else
        fail "memif jar 缺 MemIfDef.arxml — 检查 build.properties bin.includes"
    fi

    for cls in 'data/MemIfData\.class' 'data/MemIfArxmlReader\.class' 'handlers/LoadMemIfArxmlHandler\.class'; do
        if unzip -l "$memif_jar" | grep -q "$cls"; then
            ok "memif jar 含 $(basename $(echo $cls | tr -d '\\\\'))"
        else
            fail "memif jar 缺 $cls"
        fi
    done

    local ui_jar=$(ls -t "$ROOT"/ide/builder_core/cn.com.myorg.bswbuilder.ui/target/*-SNAPSHOT.jar 2>/dev/null | head -1)
    if [ -z "$ui_jar" ]; then
        fail "ui jar 不存在"
        return
    fi
    for cls in 'PropertyFormView\.class' 'ConfigurationEditorsView\.class'; do
        if unzip -l "$ui_jar" | grep -q "$cls"; then
            ok "ui jar 含 $cls"
        else
            fail "ui jar 缺 $cls"
        fi
    done
}

check_boot_clean() {
    sect "A.2 RCP 启动 0 ERROR"
    if "$ROOT"/tools/ide_smoke.sh -k 10 2>&1 | tail -3 | grep -q '\[PASS\]'; then
        ok "ide_smoke PASS — workbench booted cleanly"
    else
        fail "ide_smoke 未通过 — 看 ./tools/ide_smoke.sh 输出"
    fi
}

check_sphinx_ext() {
    sect "A.3 Sphinx EMF + Artop 在 target-platform 里"

    local local_plugins="$ROOT/ide/target-platform/bswbuilder-target/local-plugins/plugins"
    if [ ! -d "$local_plugins" ]; then
        fail "local-plugins/plugins/ 不存在 — 先跑 tools/setup-artop.ps1"
        return
    fi

    if ls "$local_plugins"/org.eclipse.sphinx.emf_*.jar >/dev/null 2>&1; then
        ok "Sphinx emf bundle 存在"
    else
        fail "Sphinx emf bundle 缺"
    fi

    if ls "$local_plugins"/org.artop.aal.autosar448_*.jar >/dev/null 2>&1; then
        ok "Artop autosar448 bundle 存在"
    else
        fail "Artop autosar448 bundle 缺"
    fi

    # 验证 Artop 在 plugin.xml 里 self-register 到 Sphinx
    local artop_jar=$(ls "$local_plugins"/org.artop.aal.autosar448_*.jar | head -1)
    if unzip -p "$artop_jar" plugin.xml 2>/dev/null | grep -q 'org.eclipse.sphinx.emf.metaModelDescriptors'; then
        ok "Artop 已 self-register 到 sphinx.emf.metaModelDescriptors"
    else
        fail "Artop plugin.xml 没找到 metaModelDescriptors 注册"
    fi
}

check_tree_node() {
    sect "A.4 / A.5 (手测) — 树节点 + 表单显示"

    cat <<'EOF'
  这部分需要你启动前台 RCP 手测——ide_smoke 8 秒 kill 没法 reliably 自动测 GUI。

  操作步骤：
    1. 启动 RCP（前台）：
         open ide/product/cn.com.myorg.bswbuilder.product/target/products/cn.com.myorg.bswbuilder.product/macosx/cocoa/aarch64/Eclipse.app
    2. 等 BSW Configurator 窗口出来，左边能看到 "Configuration Editors" 面板
    3. 展开 "Memory" 类目（点 "▸ Memory" 那行）
    4. 点 "• MemIf ✓" 那行（不是 header，是模块行）
    5. 弹出 FileDialog → 选
         samples/Demo_S32K148/BSW_Builder/S32K148/MemIf.arxml
    6. **预期**：右边 PropertyForm 视图刷新，breadcrumb 显示
         "MemIf ▸ MemIfGeneral"，
         下方 4 行显示：
             Memif Dev Error Detect:   false
             Memif Number Of Devices:  2
             Memif Version Info Api:   false
             Memif Module Version:     TEST_PROBE_42_V25_10
         底部一行 source 路径

  如果第 6 步符合预期 → A.4 + A.5 PASS（手动记账到 risks-memif.md）
  否则 → 检查 stderr / .metadata/.log
EOF
    echo
    echo -e "  [${Y}MANUAL${N}] 手测后请在 docs/MILESTONES_memif_replica.md 把对应条标 ✅"
}

check_screenshot() {
    sect "A.6 (手测) — 视觉与 ORIENTAIS 对比"

    cat <<'EOF'
  完成 A.4/A.5 的手测后：
    7. 截图我们 IDE 的 PropertyForm 区域，存
         docs/reference/screenshots/phase-a-our-memif.png
    8. 在 win-automotive 上用 ORIENTAIS V25.10 打开同 demo workspace，
       双击 MemIf，截图存
         docs/reference/screenshots/phase-a-orientais-memif.png
    9. 并排看两张截图：4 个参数 label / 值 一致 → A.6 PASS

  视觉风格不要求像素级一致——Sphinx auto-render vs iSoft 自定义 layout 会有
  明显风格差，那是 Phase E 工作。
EOF
    echo -e "  [${Y}MANUAL${N}] 手测后把两张截图 commit 到 docs/reference/screenshots/"
}

# ---- Dispatch ---------------------------------------------------------------

if [ "$mode" = "--check" ]; then
    case "${2:-}" in
        jar-classes )    check_jar_classes ;;
        boot-clean )     check_boot_clean ;;
        sphinx-ext )     check_sphinx_ext ;;
        tree-node )      check_tree_node ;;
        form-readonly )  check_tree_node ;;
        * ) echo "Unknown check: ${2:-(empty)}"; exit 2 ;;
    esac
else
    check_jar_classes
    check_boot_clean
    check_sphinx_ext
    check_tree_node
    check_screenshot
fi

echo
echo "=================================="
echo "Phase A 自动部分: PASS=$PASS FAIL=$FAIL"
echo "=================================="
[ "$FAIL" -eq 0 ]

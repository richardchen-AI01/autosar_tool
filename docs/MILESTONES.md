# 可执行里程碑清单（v0.1 sprint）

> **每条都给出确切的命令、期望输出、通过/不通过条件**。任何人在任意机器上按命令跑一遍就能判断进度。
> 适合用作每日 standup 核对、CI 阻塞门、PR review checklist。

> 日期约定：D1 = 2026-04-27，D14 = 2026-05-11。
> 路径约定：`$ROOT = /Users/richard/AI-MiniWorkspace/project/autosar_tool`，`$REF = $ROOT/reference`（软链到 V25.10 反编结果）。

---

## 总览：4 大里程碑（MemIf-first）

```
D1 ── D2 ── D3 ─────── D4 ── D5 ── D6 ── D7 ─────── D8 ── D9 ── D10 ── D11 ── D12 ── D13 ── D14
              │                                        │                      │              │
              ▼                                        ▼                      ▼              ▼
              M1                                       M2                     M3            M4
   MemIf walking skeleton                       MemIf 完美            5 核心 + 30 smoke   v0.1 demo
   (链路通,diff 可不为 0)                  (diff = 0,补丁实战可重现)  (用 MemIf 模板复制)
```

| Milestone | 截止 | 一句话验收 | 详细 |
|---|---|---|---|
| **M1** | D3 EOD | **MemIf 单模块** 从 IDE 表单走到 .c/.h 文件输出（diff 可不为 0）| [§M1](#m1--memif-walking-skeletond3) |
| **M2** | D7 EOD | **MemIf 完美**：diff = 0 + 校验联动 + docs §15 端到端补丁实战可重现 | [§M2](#m2--memif-完美--端到端补丁可重现d7) |
| **M3** | D11 EOD | **5 核心模块用 MemIf 模板复制完成** + 30 模块 smoke + 校验器接入 IDE | [§M3](#m3--30-模块--校验d11) |
| **M4** | D14 EOD | "一键打包 / 一键 demo 工程能在新机器上跑通" | [§M4](#m4--v01-demod14) |

---

## D1：项目骨架就位

### C1.1 monorepo 目录树

```bash
cd $ROOT && tree -L 3 -d ide core generator validator schemas samples
```

**通过条件**：输出包含 `ide/`、`core/`、`generator/`、`validator/`、`schemas/`、`samples/` 6 个目录。

### C1.2 git 初始化 + 第一个 commit

```bash
cd $ROOT && git log --oneline | head -1
```

**通过条件**：第一个 commit 标题是 `Initial scaffolding from V25.10 extracts`，文件数 > 5000（schema + Python sources）。

### C1.3 reference 软链可用

```bash
ls -la $ROOT/reference/ORIENTAISBswGen.exe/data/MemIf/src/MemIf.py
```

**通过条件**：能看到 V25.10 反编出来的 MemIf.py（不是 broken symlink）。

### C1.4 Python 生成器代码已搬入

```bash
ls $ROOT/generator/modules/ | wc -l
```

**通过条件**：≥ 80（V25.10 的 BSW 模块数）。

---

## D2：第一个 native helper + 最小 plugin

### C2.1 BswBase.py 可 import 不报错

```bash
cd $ROOT && python3 -c "
from core.BswBase import BswBase
b = BswBase(None)
assert hasattr(b, 'getAttrValue')
assert hasattr(b, 'getSubContainer')
print('OK:', type(b).__name__)
"
```

**通过条件**：输出 `OK: BswBase`，无 ImportError / AttributeError。

### C2.2 Eclipse RCP 工程能 mvn / Tycho 编译

```bash
cd $ROOT/ide && mvn -B clean verify -fae 2>&1 | tail -3
```

**通过条件**：最后一行包含 `BUILD SUCCESS`。

### C2.3 第一个 module plugin（MemIf）jar 能打出来

```bash
ls $ROOT/ide/modules/cn.com.myorg.bswbuilder.modules.memif/target/*.jar
```

**通过条件**：存在 `cn.com.myorg.bswbuilder.modules.memif_*.jar`，size > 5 KB。

---

## M1 — MemIf walking skeleton（D3）

> 目标：MemIf **单模块** 从 IDE 表单走到 .c/.h 文件输出。所有架构性问题在 D3 EOD 暴露完毕。
> 输出对不对不重要，**链路通**才重要。diff 不为 0 完全 OK，那是 M2 的事。

### M1.1 MemIf 用到的 5 个 native helper 都可 import

MemIf 实际只调 5 个 helper（剩余 8 个先 stub，D6 再补）：

```bash
cd $ROOT && python3 -c "
import importlib
for m in ['BswBase','Public','CodeGenerator','Context','J2Filters']:
    importlib.import_module(f'Common.{m}')
    print(f'  ✓ {m}')
"
```

**通过条件**：5 行 ✓，无 ImportError。

### M1.2 BswBase 暴露 MemIf 用到的方法

```bash
cd $ROOT && python3 -c "
from core.BswBase import BswBase
for m in ['getAttrValue', 'getSubContainer', 'getIndex',
          'getWholeIndex', 'getParentContainer']:
    assert hasattr(BswBase, m), f'missing {m}'
    print(f'  ✓ BswBase.{m}')
"
```

**通过条件**：5 行 ✓。

### M1.3 IDE 能启动 + MemIf 节点可见

```bash
$ROOT/ide/product/launcher/launch.sh -clean &
sleep 8
# 手测：导航树里能看到 MemIf 节点；不需要其他模块
```

**通过条件**：手测可见 MemIf 节点（独此一个），splash 后主窗口出现。

### M1.4 OSGi 接受 MemIf bundle，无 ClassFormatError

```bash
tail -100 $ROOT/samples_test/.metadata/.log | \
    grep -iE 'BundleException|ClassFormatError|cn\.com\.myorg\.bswbuilder\.modules\.memif'
```

**通过条件**：MemIf bundle 在日志里出现 `STARTED` 或 `RESOLVED` 关键字，**不**应该出现 `BundleException` 或 `ClassFormatError`。

### M1.5 双击 MemIf → 表单显示 3 个原始参数

手测：

- 双击 NavigatorView 里的 MemIf 节点
- 编辑器打开
- 表单可见 3 个字段：`MemIfDevErrorDetect`、`MemIfNumberOfDevices`、`MemIfVersionInfoApi`

**通过条件**：3 个字段都可见，schema 里默认值正确显示。

### M1.6 IDE Generate 按钮能调起 bswgen.exe（哪怕输出错）

手测：右键 MemIf → Generate

**通过条件**：Console 视图打印 `**** Generator started ****`，最后 `Generator finished`，**`config/MemIf_Cfg.h` 文件被写出来**（内容对不对 D4 再说）。

### M1.7 (M1 通过/不通过门)

M1.1-M1.6 都通过 → **M1 PASS**：架构链路全通，进入 M2 bug bash。

任何一条 fail：D4-D5 用作 M1 修补缓冲，M2 自动延后。

---

## D4-D6：MemIf 端到端调试

### C4.1 IDE 中可打开 Demo 工程

D4 EOD 验收：

```bash
ls $ROOT/samples/Demo_S32K148/BSW_Builder/S32K148/MemIf.arxml
```

**通过条件**：文件存在，从 V25.10 复制过来。手测：IDE NavigatorView 能看到此工程。

### C5.1 bswgen.exe 能生成 MemIf

```bash
cd $ROOT && python3 -m generator \
    -i samples/Demo_S32K148 \
    -o /tmp/v01_out \
    -g MemIf 2>&1 | tail -5
```

**通过条件**：最后一行包含 `Code generation is complete` 或类似成功标志，`/tmp/v01_out/MemIf_Cfg.h` 存在。

### C5.2 输出非空且 `#include "MemIf_Types.h"` 出现

```bash
grep -c '^#define MEMIF_' /tmp/v01_out/MemIf_Cfg.h
```

**通过条件**：≥ 3（DEV_ERROR_DETECT、NUMBER_OF_DEVICES、VERSION_INFO_API 这三条至少在）。

---

## M2 — MemIf 完美 + 端到端补丁可重现（D7）

> 目标：MemIf 这条管线**任何细节** 跟 V25.10 等价，能充当后期复制的"金模板"。

### M2.1 MemIf_Cfg.h 与 V25.10 reference **字节一致**

```bash
cd $ROOT && python3 -m generator \
    -i samples/Demo_S32K148 \
    -o /tmp/v01_out -g MemIf
diff <(grep -v '^/\*.*Generated.*\*/$' /tmp/v01_out/MemIf_Cfg.h) \
     <(grep -v '^/\*.*Generated.*\*/$' reference/Demo_S32K148_V2510_BSW_ConfigProject/config/MemIf_Cfg.h)
echo "diff exit: $?"
```

**通过条件**：`diff exit: 0`（去掉时间戳行后完全一致）。

### M2.2 MemIf_Cfg.c 与 V25.10 reference 一致

注意：仅当 `MemIfNumberOfDevices > 1 or MemIfDevErrorDetect == STD_ON` 时才生成 .c
（详见 V25.10 `FilesList.jinja` 条件）。

```bash
diff <(grep -v Generated /tmp/v01_out/MemIf_Cfg.c) \
     <(grep -v Generated reference/.../MemIf_Cfg.c)
echo "diff exit: $?"
```

**通过条件**：`0`，或文件不生成（条件不满足时）但满足条件的 demo 工程必须 diff = 0。

### M2.3 跨模块校验 `Rule_BSW_MemIf_TCPP_2170` 工作

故意改 demo 工程：把 `MemIfNumberOfDevices` 改成 1，但 NvM 那边 NvMFeeRef + NvMEaRef 都存在。

```bash
cd $ROOT && python3 -m validator \
    -i samples/Demo_S32K148_BAD_2170 \
    -m MemIf 2>&1 | grep -c 'Rule_BSW_MemIf_TCPP_2170'
```

**通过条件**：≥ 1。

### M2.4 跨模块校验 `Rule_BSW_MemIf_TCPP_2171` 工作

故意改：`MemIfNumberOfDevices` ∈ {1,2}，但 NvM 那边 NvMFeeRef 和 NvMEaRef **都不存在**。

```bash
python3 -m validator -i bad_2171 -m MemIf 2>&1 | grep -c 'Rule_BSW_MemIf_TCPP_2171'
```

**通过条件**：≥ 1。

### M2.5 docs §15 的端到端补丁实战可重现（**关键**）

复刻 `reference/autosar-cfg/docs/04-recipes/15-add-new-param-end-to-end.md` 的实战：

1. 在 `ide/modules/.../MemIfDef.arxml` 加 `MemIfModuleVersion` STRING param 默认值 `TEST_PROBE_42_V25_10`
2. `schemas/common/MemIfDef.arxml` 同步加
3. 重启 IDE → Model upgrade 对话框 → Yes → 表单显示新字段 → Save → Generate
4. 看 `config/MemIf_Cfg.h`

```bash
grep '#define MEMIF_MODULE_VERSION' /tmp/v01_out/MemIf_Cfg.h
```

**通过条件**：输出 `#define MEMIF_MODULE_VERSION "TEST_PROBE_42_V25_10"`。**这条通过证明 schema → IDE → Save → 生成器 → C 输出整条链路与 V25.10 对齐**。

### M2.6 全部 13 个 native helper 都到位

```bash
cd $ROOT && python3 -c "
import importlib
for m in ['BswBase','Public','CodeGenerator','Context','IncGen','J2Filters',
         'main','ArgParser','ConfigParser','Constant','PerformanceMonitor',
         'Utils','logger']:
    importlib.import_module(f'Common.{m}')
    print(f'  ✓ {m}')
"
```

**通过条件**：13 行 ✓。M1 时 5 个就够，M2 必须全部 13 个（即使有 stub 也算"到位"，但调用现场不能炸）。

### M2.7 一键回归脚本

```bash
$ROOT/tools/test_memif_full.sh
echo "M2 exit: $?"
```

`tools/test_memif_full.sh` 顺序跑：generate → diff vs reference → validator on bad_2170 / bad_2171 → 端到端补丁实战。

**通过条件**：`M2 exit: 0`。

### M2.8 (M2 通过门)

M2.1 + M2.2 + M2.3/2.4 至少一条 + M2.5 + M2.7 都过 → **M2 PASS**：MemIf 模板就绪，进入 M3 复制阶段。

---

## D8-D10：扩展到 30 模块

### C8.1 30 模块 smoke test（不抛异常）

```bash
cd $ROOT && for mod in Det MemIf NvM Ea Fee EcuM Os WdgM Com PduR CanIf Can CanTp \
    BswM Crc Dem Dcm Mcu Port Dio Gpt Wdg LinIf LinSM Nm CanNm CanSM ComM IpduM Rte; do
  python3 -m generator -i samples/Demo_S32K148 \
    -o /tmp/v01_$mod -g $mod 2>&1 | tail -1 | tr -d '\n'
  echo "  ← $mod"
done
```

**通过条件**：30 行输出，每行包含 `complete` 或 `Total Count: critical: 0 error: 0`。

### C9.1 5 核心模块仍 100% diff = 0

```bash
$ROOT/tools/reference_diff.py --modules Det,MemIf,NvM,Ea,Fee
```

**通过条件**：脚本退出 0。脚本会跑完 5 个模块的 generate 然后跟 reference 对比，输出 diff 报告。

---

## M3 — 30 模块 + 校验（D11）

### M3.1 30 模块 smoke 通过 + 5 核心 diff = 0

```bash
$ROOT/tools/reference_diff.py --modules Det,MemIf,NvM,Ea,Fee && \
$ROOT/tools/smoke_30_modules.sh
echo "M3.1 exit: $?"
```

**通过条件**：`M3.1 exit: 0`。

### M3.2 校验器接入 IDE（手测）

故意改 `samples/Demo_S32K148/BSW_Builder/S32K148/MemIf.arxml` 把 `MemIfNumberOfDevices` 改成 `1`，但不改 NvM 那边的 NvMFeeRef + NvMEaRef 配对。

IDE 里 Validate MemIf。**通过条件**：ProblemView 出现 `Rule_BSW_MemIf_TCPP_2170` 红色错误，message 包含 `NvMTargetBlockReference not match lower modle`。

### M3.3 跨模块联动校验工作（命令行）

```bash
cd $ROOT && python3 -m validator \
    -i samples/Demo_S32K148_BAD_2170 \
    -m MemIf 2>&1 | grep -c 'TCPP_2170'
```

**通过条件**：≥ 1。

### M3.4 (M3 通过门)

M3.1 + M3.2 + M3.3 都通过 → M3 PASS。

---

## D12-D13：打磨

### C12.1 IDE 启动后 1 小时不崩

```bash
$ROOT/ide/product/launcher/launch.sh &
PID=$!
sleep 3600
kill -0 $PID && echo "still alive ✓"
```

**通过条件**：1 小时后进程仍在。

### C13.1 一键打包脚本能在 macOS / Windows 各跑一次

```bash
$ROOT/tools/build_all.sh   # macOS
# 在 Windows 上：tools\build_all.cmd
```

**通过条件**：`dist/autosar_tool-v0.1-{macos,win}.zip` 文件生成，size > 200 MB（包含 ARTOP + Sphinx + Eclipse RCP runtime）。

---

## M4 — v0.1 demo（D14）

### M4.1 一键 demo 在新机器上跑通

模拟 "拿到 zip 的新人" 路径：

```bash
# 在一台从未碰过这个项目的机器上
unzip dist/autosar_tool-v0.1-macos.zip -d /tmp/demo
/tmp/demo/autosar_tool/run.sh
# 等待 IDE 启动 → 自动打开内置 Demo 工程 → 自动选中 MemIf → 点 Generate
```

**通过条件**：从 unzip 到看到 `MemIf_Cfg.h` 内容上方 `#define MEMIF_NUMBER_OF_DEVICES 2u` 全过程不需要任何手工配置，时间 < 10 分钟。

### M4.2 5 核心模块的 diff = 0 CI

```bash
cd $ROOT && ./tools/reference_diff.py --modules Det,MemIf,NvM,Ea,Fee --strict
echo $?
```

**通过条件**：`0`。strict 模式连时间戳行也对比（如果做了 deterministic build）。

### M4.3 README walkthrough 可完成

新人按照 `README.md` 的步骤一步步操作，最终能：
- 启 IDE
- 看到 demo 工程
- 改一个 ECUC 参数
- Generate
- 看到改动反映在 .c/.h 输出

**通过条件**：30 分钟内全部走通，无步骤卡住。

### M4.4 已知 issue 文档化

```bash
wc -l $ROOT/docs/99-known-differences-from-V25.10.md
```

**通过条件**：≥ 50 行，至少列出 30 个模块里 5 核心之外那些跟 V25.10 不一致的地方。

### M4.5 (M4 通过门 / 即 v0.1 release 门)

M4.1 + M4.2 + M4.3 都通过 → **v0.1 RELEASE**。M4.4 是文档质量门。

---

## 每日 standup 模板（D1-D14）

每天早上跑一次：

```bash
cd $ROOT && ./tools/daily_check.sh
```

`daily_check.sh` 应该按当前 day 跑当天对应的 C / M 检查项，输出：

```
=== Day 5 / 14 ===
[OK]    C5.1 bswgen MemIf 不报错
[OK]    C5.2 MemIf_Cfg.h 含 ≥3 个 #define
[FAIL]  M2.1 MemIf vs reference diff = 0  → diff 17 行
[SKIP]  M2.2 Det (M2.1 fail 时不连测)
[SKIP]  M2.3 NvM
进度：on track for M2 (D7)
```

D7、D11、D14 这三个 milestone day 走完所有 M*.* 检查。

---

## 进度风险信号

按检查点 fail 数判断是否需要预警：

| 信号 | 含义 | 建议 |
|---|---|---|
| 任意一天 C 检查 ≥ 50% fail | 当天目标偏离严重 | 当晚 review，砍当天剩余非阻塞任务 |
| M1 / M2 推迟 1 天 | 缓冲已用尽 | M3 砍到 25 模块；M4 时间不变 |
| M2 推迟 ≥ 2 天 | sprint 风险 | 砍 M3 整章（只跑 5 核心），保 M4 |
| M3.1 fail 但 M3.2/M3.3 通过 | 30 模块覆盖差 | v0.1 release 时已知 issue 中如实声明 |

---

## 工具脚本清单（D1-D2 要写出来）

| 脚本 | 干什么 | 谁写 | 截止 |
|---|---|---|---|
| `tools/reference_diff.py` | 跑 generate 然后 diff vs reference，过滤 timestamp | 实例 D | D4 |
| `tools/smoke_30_modules.sh` | 30 模块 smoke 跑一遍 | 实例 D | D8 |
| `tools/daily_check.sh` | 当天对应的所有 C/M 检查 | You | D2 |
| `tools/build_all.sh` | macOS/Linux 打包脚本 | 实例 C | D11 |
| `tools/build_all.cmd` | Windows 打包脚本 | 实例 C | D13 |

这些脚本是验收的根基——脚本不写出来，没法客观判断里程碑。

---

## 关联文档

- [PLAN.md](PLAN.md) — 完整方案
- [README.md](../README.md) — 项目入口

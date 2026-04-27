# 可执行里程碑清单（v0.1 sprint）

> **每条都给出确切的命令、期望输出、通过/不通过条件**。任何人在任意机器上按命令跑一遍就能判断进度。
> 适合用作每日 standup 核对、CI 阻塞门、PR review checklist。

> 日期约定：D1 = 2026-04-27，D14 = 2026-05-11。
> 路径约定：`$ROOT = /Users/richard/AI-MiniWorkspace/project/Autosar_tool`，`$REF = $ROOT/reference`（软链到 V25.10 反编结果）。

---

## 总览：4 大里程碑 + 14 个每日检查点

```
D1 ── D2 ── D3 ─────── D4 ── D5 ── D6 ── D7 ─────── D8 ── D9 ── D10 ── D11 ── D12 ── D13 ── D14
              │                                        │                      │              │
              ▼                                        ▼                      ▼              ▼
              M1                                       M2                     M3            M4
       基础设施就位                                单模块端到端              30 模块 + 校验   v0.1 demo
```

| Milestone | 截止 | 一句话验收 | 详细 |
|---|---|---|---|
| **M1** | D3 EOD | "13 个 native helper 可 import + IDE 能弹空白窗口" | [§M1](#m1--基础设施就位d3) |
| **M2** | D7 EOD | "MemIf/Det/NvM 输出与 V25.10 reference 字节一致" | [§M2](#m2--单模块端到端d7) |
| **M3** | D11 EOD | "30 个 BSW 模块都能 generate 不抛异常 + 校验器接入 IDE" | [§M3](#m3--30-模块--校验d11) |
| **M4** | D14 EOD | "一键打包 / 一键 demo 工程能在新机器上跑通" | [§M4](#m4--v01-demod14) |

---

## D1：项目骨架就位

### C1.1 monorepo 目录树

```bash
cd $ROOT && tree -L 3 -d clone/
```

**通过条件**：输出包含 `eclipse_plugins/`、`python_common/`、`python_generator/`、`python_validator/`、`bswmd/`、`test_workspace/` 6 个目录。

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
ls $ROOT/clone/python_generator/modules/ | wc -l
```

**通过条件**：≥ 80（V25.10 的 BSW 模块数）。

---

## D2：第一个 native helper + 最小 plugin

### C2.1 BswBase.py 可 import 不报错

```bash
cd $ROOT && python3 -c "
from clone.python_common.BswBase import BswBase
b = BswBase(None)
assert hasattr(b, 'getAttrValue')
assert hasattr(b, 'getSubContainer')
print('OK:', type(b).__name__)
"
```

**通过条件**：输出 `OK: BswBase`，无 ImportError / AttributeError。

### C2.2 Eclipse RCP 工程能 mvn / Tycho 编译

```bash
cd $ROOT/clone/eclipse_plugins && mvn -B clean verify -fae 2>&1 | tail -3
```

**通过条件**：最后一行包含 `BUILD SUCCESS`。

### C2.3 第一个 module plugin（MemIf）jar 能打出来

```bash
ls $ROOT/clone/eclipse_plugins/modules/cn.com.myorg.bswbuilder.modules.memif/target/*.jar
```

**通过条件**：存在 `cn.com.myorg.bswbuilder.modules.memif_*.jar`，size > 5 KB。

---

## M1 — 基础设施就位（D3）

### M1.1 全部 13 个 native helper 都可 import

```bash
cd $ROOT && python3 -c "
import importlib
for m in ['BswBase','Public','CodeGenerator','Context','IncGen','J2Filters',
         'main','ArgParser','ConfigParser','Constant','PerformanceMonitor',
         'Utils','logger']:
    importlib.import_module(f'clone.python_common.{m}')
    print(f'  ✓ {m}')
"
```

**通过条件**：13 行 ✓，无任何 ImportError。

### M1.2 BswBase 的 6 个核心方法签名跟 V25.10 .pyd 对得上

```bash
cd $ROOT && python3 -c "
from clone.python_common.BswBase import BswBase
expected = ['getAttrValue', 'getSubContainer', 'getIndex', 'getWholeIndex', 'getParentContainer']
b = BswBase.__init__.__code__
for m in expected:
    assert hasattr(BswBase, m), f'missing {m}'
    print(f'  ✓ BswBase.{m}')
"
```

**通过条件**：5 行 ✓（5 个 public 方法都存在）。

### M1.3 Eclipse RCP product 能启动到空白窗口

```bash
$ROOT/clone/eclipse_plugins/product/launcher/launch.sh -clean &
sleep 8
osascript -e 'tell application "System Events" to count windows of (every process whose name contains "java")'
```

**通过条件**：返回值 ≥ 1（至少一个 Java 窗口存在）。也可手测看到 splash + 主窗口。

### M1.4 OSGi bundle resolve 不报错

启动 IDE 后，看 `workspace/.metadata/.log`：

```bash
tail -50 $ROOT/workspace_test/.metadata/.log | grep -iE 'BundleException|ClassNotFoundException|Error'
```

**通过条件**：**空输出**（无错误日志）。

### M1.5 (M1 通过/不通过门)

四条都通过 → M1 PASS，进入 D4。

否则 D4-D5 用作 M1 修补缓冲，M2 自动延后。

---

## D4-D6：MemIf 端到端调试

### C4.1 IDE 中可打开 Demo 工程

D4 EOD 验收：

```bash
ls $ROOT/clone/test_workspace/Demo_S32K148/BSW_Builder/S32K148/MemIf.arxml
```

**通过条件**：文件存在，从 V25.10 复制过来。手测：IDE NavigatorView 能看到此工程。

### C5.1 bswgen.exe 能生成 MemIf

```bash
cd $ROOT && python3 -m clone.python_generator \
    -i clone/test_workspace/Demo_S32K148 \
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

## M2 — 单模块端到端（D7）

### M2.1 MemIf 输出与 V25.10 reference **字节一致**

```bash
cd $ROOT && python3 -m clone.python_generator \
    -i clone/test_workspace/Demo_S32K148 \
    -o /tmp/v01_out -g MemIf
diff <(grep -v '^/\*.*Generated.*\*/$' /tmp/v01_out/MemIf_Cfg.h) \
     <(grep -v '^/\*.*Generated.*\*/$' reference/Demo_S32K148_V2510_BSW_ConfigProject/config/MemIf_Cfg.h)
echo "diff exit: $?"
```

**通过条件**：`diff exit: 0`（去掉时间戳行后完全一致）。

### M2.2 同样的 diff = 0 适用于 Det

```bash
cd $ROOT && python3 -m clone.python_generator -i ... -g Det
diff <(grep -v Generated /tmp/v01_out/Det_Cfg.h) \
     <(grep -v Generated reference/.../Det_Cfg.h)
echo "diff exit: $?"
```

**通过条件**：`0`。

### M2.3 同样的 diff = 0 适用于 NvM

同上替换为 `NvM`。**通过条件**：`0`。

### M2.4 IDE Generate 按钮能正常调起 bswgen.exe

手测：IDE 中右键 MemIf → Generate → Console 视图打印 `**** Generator started ****`，
最后 `Total Count: critical: 0 error: 0 warning: 0` + `Generator finished`。

**通过条件**：3 个核心模块全 0 critical 0 error 0 warning。

### M2.5 (M2 通过门)

M2.1 + M2.2 + M2.3 都通过 → M2 PASS。M2.4 是 nice to have，不通过的话延 D9 修。

---

## D8-D10：扩展到 30 模块

### C8.1 30 模块 smoke test（不抛异常）

```bash
cd $ROOT && for mod in Det MemIf NvM Ea Fee EcuM Os WdgM Com PduR CanIf Can CanTp \
    BswM Crc Dem Dcm Mcu Port Dio Gpt Wdg LinIf LinSM Nm CanNm CanSM ComM IpduM Rte; do
  python3 -m clone.python_generator -i clone/test_workspace/Demo_S32K148 \
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

故意改 `clone/test_workspace/Demo_S32K148/BSW_Builder/S32K148/MemIf.arxml` 把 `MemIfNumberOfDevices` 改成 `1`，但不改 NvM 那边的 NvMFeeRef + NvMEaRef 配对。

IDE 里 Validate MemIf。**通过条件**：ProblemView 出现 `Rule_BSW_MemIf_TCPP_2170` 红色错误，message 包含 `NvMTargetBlockReference not match lower modle`。

### M3.3 跨模块联动校验工作（命令行）

```bash
cd $ROOT && python3 -m clone.python_validator \
    -i clone/test_workspace/Demo_S32K148_BAD_2170 \
    -m MemIf 2>&1 | grep -c 'TCPP_2170'
```

**通过条件**：≥ 1。

### M3.4 (M3 通过门)

M3.1 + M3.2 + M3.3 都通过 → M3 PASS。

---

## D12-D13：打磨

### C12.1 IDE 启动后 1 小时不崩

```bash
$ROOT/clone/eclipse_plugins/product/launcher/launch.sh &
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

**通过条件**：`dist/Autosar_tool-v0.1-{macos,win}.zip` 文件生成，size > 200 MB（包含 ARTOP + Sphinx + Eclipse RCP runtime）。

---

## M4 — v0.1 demo（D14）

### M4.1 一键 demo 在新机器上跑通

模拟 "拿到 zip 的新人" 路径：

```bash
# 在一台从未碰过这个项目的机器上
unzip dist/Autosar_tool-v0.1-macos.zip -d /tmp/demo
/tmp/demo/Autosar_tool/run.sh
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
- [README.md](README.md) — 项目入口

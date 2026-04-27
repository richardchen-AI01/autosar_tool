# AUTOSAR Configurator 复刻方案 · v0.1 PLAN

> 项目目标：在 **2 周** 内、用 **Claude Code 多实例 + 已挖出的 ORIENTAIS Configurator V25.10 整套源码** 作为种子，端到端复刻一个能跑、能演示的 AUTOSAR BSW Configurator。

---

## 0. 一句话目标

```
2026-05-11 之前交付一个能：
  ① 启动 Eclipse RCP IDE
  ② 打开 Demo_S32K148 工程
  ③ 在 IDE 表单里编辑 5 个核心 BSW 模块（Det/MemIf/NvM/Ea/Fee）
  ④ 一键 Validate + Generate
  ⑤ 输出的 .c/.h 与 V25.10 reference 输出 ≥ 95% 一致
的可演示工具（v0.1）。
```

非目标（明确不做）：
- ❌ 商业级稳定性
- ❌ License / 加密狗 / 代码保护
- ❌ 80+ 模块全覆盖（仅 5 个核心 + 30 个能跑通）
- ❌ OEM 集成测试 / 第三方 IDE 兼容

---

## 1. 立项背景

### 1.1 重新评估为什么这次能 2 周

之前我按 "传统团队 + 全新做" 估了 12-18 个月。这次条件不同：

| 因子 | 传统估算前提 | 现状 |
|---|---|---|
| **团队** | 8-10 人小团队 | Claude Code 多实例（4 个）+ 你 1 人协调 |
| **节奏** | 5×8 工时 | 7×24 |
| **起点** | 全新写 | 整套 V25.10 已经被 reverse engineering 出来，明文资产 95% 在手 |
| **AUTOSAR 领域知识** | 边写边学 | 已有 reference 实现可对照（V25.10 是黄金对照）|
| **ARTOP 元模型** | 自己写需 1-2 人年 | 直接复用安装目录里的 ARTOP 4.5.2 + Sphinx 0.11.2（28+13 个 jar）|
| **代码保护层** | 是个大坑 | v0.1 不做，整体 -20% 工作量 |

### 1.2 这次能 2 周的根本原因

**已经把 V25.10 这套完整反编了**——见 `/Users/richard/AI-MiniWorkspace/project/autosar-cfg/`：

```
ORIENTAISBswGen.exe/        生成器整套：
  data/<Module>/*.py            ← 每个 BSW 模块的 Python domain model
  data/<Module>/*.jinja         ← 每个 BSW 模块的 C 代码模板
  data/Common/*.pyd             ← 13 个 native helper（API surface 已挖出）
  pyz_source/                   ← 2485 个反编 .py
  _pyd_analysis/                ← 13 个 native 模块的 API 索引

ORIENTAISBswVal.exe/        校验器整套：
  data/Bsw/<Module>/*.py        ← 47 个模块的明文规则算法（未编译，未混淆）
  data/Bsw/<Module>/*.json      ← 规则元数据
  pyz_source/                   ← 2408 个反编 .py（含 Common.ArxmlValidator,
                                   Common.base.BaseClass, BaseDecorator 等核心框架，全明文）

docs/04-recipes/15-add-new-param-end-to-end.md   ← 端到端补丁实战经验
```

**真正要从零写的只剩 13 个 .pyd 的 Python 等价实现**。其它都是搬。

---

## 2. 资产盘点（什么能直接复用）

### 2.1 可以直接搬的（几乎零成本）

| 资产 | 路径 | 体积 | 复用方式 |
|---|---|---|---|
| 80+ 模块 Python 生成器 | `ORIENTAISBswGen.exe/data/<Module>/` | ~3 MB | 整体复制，去掉 PyInstaller 包装 |
| 47 模块校验规则（明文 .py）| `ORIENTAISBswVal.exe/data/Bsw/<Module>/` | ~500 KB | 直接搬 |
| BSWMD schema 定义 | `bswmd/Common/*.arxml` (58 个) + 各代标准 | ~4 MB | 直接搬 |
| ARTOP plugin jar | `plugins/org.artop.*` (28 jar) | ~10 MB | 直接搬（合法用户用） |
| Sphinx plugin jar | `plugins/org.eclipse.sphinx.*` (13 jar) | ~5 MB | 直接搬（EPL 开源） |
| Eclipse RCP runtime | `plugins/org.eclipse.*` (~200 jar) | ~150 MB | 直接搬 |
| iSoft 自家 plugin（解密版）| `plugins/cn.com.isoft.bswbuilder.*` (~80 jar) | ~30 MB | **可参考实现，自己重写**（合法性更稳）|
| BswPath 常量字符串 | `_pyd_analysis/` 里挖出的 2789 项 | - | 1 小时生成新 enum class |

### 2.2 需要替换的（要写新代码）

| 替换对象 | V25.10 实现 | 我们的实现 | 工作量 |
|---|---|---|---|
| `Common/BswBase.pyd` | Cython 编译，闭源 | 纯 Python 类（API 已知）| 4-8 工时 |
| `Common/Public.pyd` | 同上 | 纯 Python 函数集 | 8-16 工时 |
| `Common/CodeGenerator.pyd` | 主循环，含模板引擎集成 | 纯 Python | 8-16 工时 |
| `Common/Context.pyd` | 模型 cache | 纯 Python | 4-8 工时 |
| `Common/IncGen.pyd` | 增量生成 + 用户代码区保留 | v0.1 不做 | 0 |
| `Common/J2Filters.pyd` | Jinja2 自定义过滤器 | 纯 Python | 4 工时 |
| `Common/main.pyd` | 入口 | 纯 Python | 2 工时 |
| `Common/{ArgParser, ConfigParser, Constant, PerformanceMonitor, Utils, logger}.pyd` | 工具类 | 纯 Python | 共 8 工时 |
| **小计** | | | **~64 工时** |

13 个 .pyd 加起来不到 64 工时——按多实例并行可压在 1.5 个工作日内。

### 2.3 法律边界

| 资产 | 协议 | 我们能用 |
|---|---|---|
| ARTOP jar | ASLP（Artop Software License for Preparatory Development）| ✅ 你作为 V25.10 合法用户，本机内使用 OK；不能再分发给非 ARTOP 会员 |
| Sphinx jar | EPL 2.0 | ✅ 自由使用 |
| iSoft 自家 jar / Python | 商业软件，含 V25.10 license | ⚠️ 仅用于**研究、本机自用**；商业化必须 clean-room 重写 |
| AUTOSAR 标准 | AUTOSAR Member License | 🟡 Free Specs 公开，覆盖核心；完整需 AUTOSAR 会员 |

**v0.1 定位为研究 / 内部 demo**，不分发不商用。商业化路线见 §9。

---

## 3. 架构设计

### 3.1 整体分层

```
┌──────────────────────────────────────────────────────────────────┐
│                     IDE Layer (Eclipse RCP)                      │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐    │
│  │ NavigatorView   │  │ ECUC FormEditor  │  │ ProblemView  │    │
│  └──────────────────┘  └──────────────────┘  └──────────────┘    │
│                              │                                   │
│  cn.com.<myorg>.bswbuilder.modules.<Module>_*.jar (per module)   │
│  - plugin.xml                                                    │
│  - <Module>Def.arxml         ← schema (从 bswmd/ 复制)            │
│  - <Module>DefaultRegistry   ← 表单注册                          │
│  - <Module>Validator         ← 校验入口                          │
│  - <Module>UpdateBswmd       ← 工程升级器                         │
│                              │                                   │
│            ┌─────────────────┴─────────────────┐                  │
│            │                                   │                  │
│  ┌─────────▼──────────┐               ┌────────▼──────────┐       │
│  │ ARTOP 4.5.2       │               │ Eclipse Sphinx     │       │
│  │ org.artop.aal.*   │               │ 0.11.2             │       │
│  │ (AUTOSAR 元模型)   │               │ (EMF 工作区)        │       │
│  └────────────────────┘               └────────────────────┘       │
└──────────────────────────────────────────────────────────────────┘
                              │ Runtime.exec
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│              Backend Layer (Python 子进程)                        │
│                                                                  │
│  bswgen.exe                          bswval.exe                  │
│  ┌──────────────────┐                ┌──────────────────┐        │
│  │ argparse 解析参数 │                │ argparse 解析参数 │        │
│  │ ▼                 │                │ ▼                 │        │
│  │ load_modules()    │                │ load_rules()      │        │
│  │ ▼                 │                │ ▼                 │        │
│  │ 80+ Module/       │                │ 47 Bsw/           │        │
│  │   src/*.py        │                │   <Module>Rules.py│        │
│  │   templates/*.j2  │                │ ▼                 │        │
│  │ ▼                 │                │ Common.base.*     │        │
│  │ Common.CodeGen    │                │ (规则装饰器 + ARXML│        │
│  │ ▼                 │                │  迭代 + 报告)     │        │
│  │ render → .c/.h    │                │ ▼                 │        │
│  │                   │                │ JSON / log        │        │
│  └──────────────────┘                └──────────────────┘        │
│       │                                       │                  │
│       └───────────┬───────────────────────────┘                  │
│                   │                                              │
│  ┌────────────────▼─────────────────────┐                        │
│  │ Common/ 13 个原 .pyd 的 Python 等价    │                        │
│  │  - BswBase, Public, CodeGenerator,   │                        │
│  │    Context, J2Filters, main, ...     │                        │
│  └──────────────────────────────────────┘                        │
└──────────────────────────────────────────────────────────────────┘
```

### 3.2 关键设计决策

| 决策点 | 选择 | 理由 |
|---|---|---|
| IDE 框架 | **Eclipse RCP / OSGi** | ARTOP 必须挂 OSGi；自己换 VS Code 等于放弃 ARTOP 元模型，工作量翻倍 |
| 后端语言 | **Python 3.8** | 直接复用 V25.10 的全部生成器代码；不要换 3.11+，因为 .pyd 复刻成 .py 后语法跟 3.8 兼容最简单 |
| 模板引擎 | **Jinja2** | V25.10 用的就是它，直接搬模板 |
| ECUC 模型 | **EMF + ARTOP** | 自己写一年都搞不定；用现成 |
| 进程模型 | **IDE → fork generator/validator exe** | 跟 V25.10 完全一致；JVM 和 Python 不同生命周期，进程隔离最简单 |
| 工程文件持久化 | **纯 ARXML + git** | v0.1 不做 .arxmlHashFile 那种完整性校验 |

---

## 4. 团队配置：4 个 Claude Code 实例分工

| 实例 | 角色 | 14 天内的输出 |
|---|---|---|
| **A** "Native Replacements" | 复刻 13 个 .pyd 为 Python | `clone/python_common/*.py`（~13 个文件，~3000 行）|
| **B** "Schema & Plugins" | 复刻 80+ iSoft 的 OSGi plugin jar | `clone/eclipse_plugins/cn.com.<org>.modules.*/` |
| **C** "RCP Product" | Eclipse RCP product 配置、p2 repo、launcher、splash | 一个能 `./run.sh` 启动的空 IDE |
| **D** "Generator & Validator" | 整理 V25.10 的 Python 代码 + 写 PyInstaller spec + 打 exe | `bswgen.exe` 和 `bswval.exe` 两个产物 |
| **You**（人）| 协调、验收、关键决策、对照测试、git/IP 边界守门 | 每天 review + 决定优先级 |

**并行度真正要做到的**：四个实例独立目录、独立分支、独立 PR；你每天 merge 一次。

---

## 5. 14 天逐日排期 — MemIf-first / Walking Skeleton

> **核心策略**：先把 **MemIf 这一个模块端到端打透**（schema → IDE 表单 → 子进程生成 → 校验器 → docs §15 端到端补丁可重现）。第一个模块走通后，所有架构性问题（OSGi resolve、IDE 表单 binding、Python helper 调用、模板渲染、Generate 子进程通信）都暴露完毕，剩下模块就是机械复制。

### 阶段 1：MemIf walking skeleton（D1-D3）

> 里程碑 **M1：MemIf 单模块能从 IDE 表单走到 .c/.h，哪怕 diff 不为 0**。

目标是**架构全链路打通**，不是输出正确。架构性问题在 D3 EOD 全部暴露。

| 天 | 任务 | 实例 | 验收 |
|---|---|---|---|
| **D1** | 立项目录骨架；从 V25.10 复制 **仅 MemIf 相关** 的资产到 `clone/`；git init | You + 全员 | `clone/` 目录就位，第一个 commit |
| **D1** | 复刻 MemIf 实际用到的 5 个 native helper（**只**做 BswBase, Public, CodeGenerator, Context, J2Filters，其它 8 个先 stub）| A | `python_common/{BswBase,Public,CodeGenerator,Context,J2Filters}.py` 单测通过 |
| **D1-D2** | Eclipse RCP product 最小骨架，仅注册 MemIf 一个 plugin | C | IDE 弹空白窗口 + MemIf 节点出现 |
| **D2** | MemIf plugin jar 全套（`MemIfDef.arxml` / `MemIfDefaultRegistry` / `MemIfValidator` / `MemIfUpdateBswmd` / `plugin.xml`）| B | OSGi 启动后 MemIf bundle started，无 ClassFormatError |
| **D2** | python_generator **只**含 MemIf；PyInstaller 第一次打 bswgen.exe | D | Windows 上 `bswgen.exe -g MemIf -i ... -o ...` 能产出**任意**输出（diff 不为 0 没关系）|
| **D3** | python_validator **只**含 MemIf 校验规则 + Common 框架基类（直接搬 V25.10 反编结果）| D | `bswval.exe -m MemIf -i ...` 能跑 |
| **D3** | IDE 接入：双击 MemIf → 表单 → Generate 按钮调起 bswgen.exe | All | **端到端走通**：表单 → 输出文件（diff 可以不为 0）|

### 阶段 2：MemIf 完美 + 端到端补丁可重现（D4-D7）

> 里程碑 **M2：MemIf 输出与 V25.10 reference 字节一致 + docs §15 端到端补丁实战可重现**。

D3 暴露的所有 bug 在这 4 天修干净。这是真正的 bug bash 阶段。完成后 MemIf 这条管线**任何细节**跟 V25.10 等价，可以充当后期复制的"金模板"。

| 天 | 任务 | 实例 | 验收 |
|---|---|---|---|
| **D4** | MemIf_Cfg.h diff vs V25.10 reference | A + D | diff = 0 |
| **D4** | MemIf_Cfg.c diff（NumberOfDevices > 1 才生成）| A + D | diff = 0 |
| **D5** | MemIf_Bswmd.arxml diff（如生成）| D | diff = 0 或 known reason |
| **D5** | 校验器跑 `Rule_BSW_MemIf_TCPP_2170` / `2171` 跨模块规则 | A + D | 故意改 NvMFeeRef + NvMEaRef 配对，校验器报错命中 |
| **D6** | **重现 docs §15 的端到端补丁实战**：在 MemIfDef.arxml 加 `MemIfModuleVersion` STRING param → IDE 表单显示 → 编辑保存 → Generate 后 .h 含 `#define MEMIF_MODULE_VERSION "..."` | All | 跟 docs §15 输出 100% 等价 |
| **D6** | 补齐剩余 8 个 native helper（IncGen 可继续 stub）：main、ArgParser、ConfigParser、Constant、PerformanceMonitor、Utils、logger、IncGen | A | 13 个 helper 全部 Python 化 |
| **D7** | MemIf "全栈正确性" 自动回归脚本（一键跑 Generate + Validate + diff 对比 + 端到端补丁实战）| You + D | `tools/test_memif_full.sh` 退出 0 |

### 阶段 3：用 MemIf 模板复制（D8-D11）

> 里程碑 **M3：5 核心模块 diff = 0；30 模块 smoke 通过；校验器接入 IDE**。

D8 起 MemIf 已经完美——把它当**模板**复制。每个新模块的工作量 ≈ MemIf 工作量 / 5（架构问题全解决，剩下只是模块特定逻辑）。

| 天 | 任务 | 实例 | 验收 |
|---|---|---|---|
| **D8** | 复制 MemIf 模板到 NvM、Ea、Fee | B + D | 3 模块 diff = 0（NV 链完整）|
| **D9** | 复制到 Det（最简单，单元测试用）| B + D | Det diff = 0 |
| **D9** | 批量脚本化生成剩余 25 模块的 plugin jar 骨架 | B | 30 模块 OSGi resolve 全过 |
| **D10** | python_generator 加入剩余 25 模块（直接搬 V25.10 反编代码 + 改 import 路径）| D | 30 模块 smoke：generate 不抛异常 |
| **D10** | python_validator 加入对应规则文件 | D | 30 模块 validate smoke |
| **D11** | 校验器整套接入 IDE Validate 按钮 + ProblemView 显示 | C | 故意改 ARXML 后 IDE 红色错误 |
| **D11** | 跨模块校验集成测试（NvM ↔ MemIf ↔ Ea/Fee）| A + D | 跨模块规则在 IDE 中触发 |

### 阶段 4：打磨 + 文档 + Demo（D12-D14）

> 里程碑 **M4: shippable v0.1 demo**。

| 天 | 任务 | 实例 | 验收 |
|---|---|---|---|
| **D12** | UI 体验打磨（图标、菜单、错误提示中文化）| C | 演示给非工程师看不至于一脸懵 |
| **D12** | 跨模块联动 bug 修复 | All | NvM/Ea/Fee/MemIf 完整链跑通 |
| **D13** | 集成 builder 脚本 / installer / Windows 打包 | C + D | 生成 setup.exe 或 .zip |
| **D13** | 自动化回归测试套件（5 核心模块的 reference diff CI）| You + A | CI 跑通 |
| **D14** | README + 演示视频脚本 + 一键 demo 工程 | You | v0.1 release |

### 里程碑总览（MemIf-first）

| 里程碑 | 时间 | 一句话验收 | 详细可执行检查 |
|---|---|---|---|
| **M1** | D3 EOD | **MemIf 单模块** 端到端走通（schema → IDE 表单 → Generate → 文件输出，diff 可不为 0）| [MILESTONES §M1](MILESTONES.md#m1--基础设施就位d3) |
| **M2** | D7 EOD | **MemIf 完美**（diff = 0 + 校验联动 + docs §15 端到端补丁实战可重现）| [MILESTONES §M2](MILESTONES.md#m2--单模块端到端d7) |
| **M3** | D11 EOD | **5 核心模块用 MemIf 模板复制完成**（NvM/Ea/Fee/Det diff = 0），30 模块 smoke 通过 | [MILESTONES §M3](MILESTONES.md#m3--30-模块--校验d11) |
| **M4** | D14 EOD | v0.1 demo 可演示 | [MILESTONES §M4](MILESTONES.md#m4--v01-demod14) |

> **每个里程碑的具体命令、期望输出、通过/不通过条件全部在 [MILESTONES.md](MILESTONES.md)**。
> 那份文档可以直接用作每日 standup 核对清单 / CI 阻塞门 / PR review checklist。

---

## 6. 风险登记 + 对策

| # | 风险 | 影响 | 概率 | 对策 |
|---|---|---|---|---|
| R1 | 13 个 .pyd 的某个内部行为复刻不到位（特别是 `Common.CodeGenerator` 的模板渲染细节）| MemIf 生成结果跟 reference 不一致 | 高 | 留 D5-D6 整两天 diff 调优；最坏情况：直接读 V25.10 反编出来的 dis 反汇编看那一段算法 |
| R2 | OSGi bundle 之间循环依赖 / version 不匹配 | IDE 起不来 | 中 | 把 V25.10 的 `bundles.info` 做 baseline，逐个对照 |
| R3 | ARTOP 4.5.2 + 我们的 plugin 兼容问题 | 表单渲染不对 | 中 | M1 之前就要在 D1-D2 跑通最小 plugin 例子 |
| R4 | AUTOSAR 标准里的边角 case（特定 schema 的引用解析）| 30 模块覆盖里有几个跑不通 | 中 | v0.1 接受 30 模块覆盖，不够补不到 |
| R5 | Claude Code 多实例输出冲突（同时改同一个文件）| Merge 痛苦 | 高 | 严格按实例分目录，每天定时 merge |
| R6 | 法律边界（v0.1 用了 V25.10 的 Python 代码）| 不能商业化 | 100% | v0.1 明确"研究 / 内部 demo"，商业化走 clean-room（v1.0）|
| R7 | 你 1 个人 review 不过来 | 进度卡协调 | 中 | 把验收标准量化，写 CI；不能跑通的不要 merge |
| R8 | AUTOSAR 元模型 / ARTOP 升级 | 一年后某代标准跟不上 | 低 | v0.1 锁定 R20-11 + R23-11；后续每年 1 人月升级 |

---

## 7. 项目目录骨架（D1 第一件事）

```
/Users/richard/AI-MiniWorkspace/project/Autosar_tool/
├── PLAN.md                              ← 本文档
├── CHANGELOG.md
├── README.md
├── .gitignore
│
├── docs/                                 设计文档
│   ├── 01-architecture.md
│   ├── 02-replacement-strategy-pyd.md
│   ├── 03-osgi-bundle-layout.md
│   ├── 04-build-and-package.md
│   └── 99-known-differences-from-V25.10.md
│
├── clone/                                ← 真正的代码
│   ├── eclipse_plugins/                  Eclipse RCP plugin 工程
│   │   ├── product/                          (实例 C 主战场)
│   │   │   └── cn.com.myorg.bswbuilder.product.product
│   │   ├── frameworks/                       从 V25.10 复制：
│   │   │   ├── org.artop.aal.*              （ARTOP 28 jar）
│   │   │   ├── org.eclipse.sphinx.*         （13 jar）
│   │   │   └── org.eclipse.*                （RCP runtime ~200 jar）
│   │   ├── builder_core/                     自家框架层（解密 V25.10 的 jar 改写）
│   │   │   ├── cn.com.myorg.bswbuilder.common/
│   │   │   ├── cn.com.myorg.bswbuilder.ui/
│   │   │   ├── cn.com.myorg.bswbuilder.extensionpoints/
│   │   │   └── cn.com.myorg.bswbuilder.validation/
│   │   └── modules/                          每个 BSW 模块一个 plugin（实例 B）
│   │       ├── cn.com.myorg.bswbuilder.modules.det/
│   │       ├── cn.com.myorg.bswbuilder.modules.memif/
│   │       └── ...
│   │
│   ├── python_common/                    13 个 .pyd 的等价 Python（实例 A）
│   │   ├── __init__.py
│   │   ├── BswBase.py
│   │   ├── Public.py
│   │   ├── CodeGenerator.py
│   │   ├── Context.py
│   │   ├── IncGen.py                     v0.1 stub
│   │   ├── J2Filters.py
│   │   ├── main.py
│   │   ├── ArgParser.py
│   │   ├── ConfigParser.py
│   │   ├── Constant.py
│   │   ├── PerformanceMonitor.py
│   │   ├── Utils.py
│   │   ├── logger.py
│   │   └── arxmlparse/
│   │       ├── constant/
│   │       │   └── BswPathConstant.py    自动生成 enum，2789 项
│   │       └── ...
│   │
│   ├── python_generator/                 (实例 D 主战场)
│   │   ├── pyproject.toml
│   │   ├── pyinstaller.spec
│   │   ├── tests/
│   │   └── modules/
│   │       ├── Det/                      （从 V25.10 data/Det/ 直接复制）
│   │       ├── MemIf/                    （从 V25.10 data/MemIf/ 直接复制）
│   │       └── ... 80 个
│   │
│   ├── python_validator/                 (实例 D 主战场)
│   │   ├── pyproject.toml
│   │   ├── pyinstaller.spec
│   │   └── modules/
│   │       └── ... 47 个
│   │
│   ├── bswmd/                            ECUC schema 资产
│   │   ├── Common/                       （从 V25.10 复制）
│   │   ├── AUTOSAR_00048/
│   │   ├── AUTOSAR_00052/
│   │   ├── AUTOSAR_4-2-2/
│   │   └── STD/
│   │
│   └── test_workspace/                   golden 工程
│       └── Demo_S32K148/                 （从 V25.10 复制）
│
├── tools/                                构建脚本
│   ├── build_eclipse.sh                  Eclipse RCP product 打包
│   ├── build_python_exes.sh              PyInstaller 打 generator/validator
│   ├── pack_installer.sh                 Windows installer
│   └── reference_diff.py                 跟 V25.10 reference 对比 5 核心模块输出
│
└── reference/                            V25.10 reference（作为黄金对照）
    └── (软链到 /Users/richard/AI-MiniWorkspace/project/autosar-cfg/)
```

---

## 8. 起步动作（D1 上午就能干）

### 8.1 一键建骨架

```bash
cd /Users/richard/AI-MiniWorkspace/project/Autosar_tool
mkdir -p clone/{eclipse_plugins/{product,frameworks,builder_core,modules},python_common/arxmlparse/constant,python_generator/modules,python_validator/modules,bswmd,test_workspace}
mkdir -p tools docs reference

# 软链 reference V25.10 资产
ln -s /Users/richard/AI-MiniWorkspace/project/autosar-cfg/ORIENTAISBswGen.exe reference/ORIENTAISBswGen.exe
ln -s /Users/richard/AI-MiniWorkspace/project/autosar-cfg/ORIENTAISBswVal.exe reference/ORIENTAISBswVal.exe

# 复制可直接搬的资产
SRC=/Volumes/ORIENTAIS_Studio/ORIENTAIS_Configurator_for_EasyXMen_V25.10
cp -r $SRC/bswmd/* clone/bswmd/
cp -r reference/ORIENTAISBswGen.exe/data/* clone/python_generator/modules/    # 80 个模块
cp -r reference/ORIENTAISBswVal.exe/data/Bsw/* clone/python_validator/modules/ # 47 个模块

git init
git add . && git commit -m "Initial scaffolding from V25.10 extracts"
```

### 8.2 D1 起步任务清单（按优先级）

| 优先级 | 任务 | 谁 | 截止 |
|---|---|---|---|
| P0 | 建 monorepo 骨架（上面那段脚本）| You | D1 上午 |
| P0 | `python_common/BswBase.py` v1（从 `_pyd_analysis/BswBase.md` API + `Bsw/MemIf/MemIfRules.py` 调用现场反推）| 实例 A | D1 EOD |
| P0 | Eclipse RCP `.product` 文件 + 最小启动配置 | 实例 C | D1 EOD |
| P1 | `python_common/Public.py` v1 | 实例 A | D2 上午 |
| P1 | 1 个 minimal plugin（cn.com.myorg.bswbuilder.modules.memif）—— 仅 plugin.xml + MemIfDef.arxml | 实例 B | D2 上午 |
| P1 | python_generator 跑通 `python -m generator -g Det -i clone/test_workspace/Demo_S32K148`（哪怕错）| 实例 D | D2 EOD |

---

## 9. 后续路线（v0.1 之后）

| 版本 | 时间 | 重点 | 详细 |
|---|---|---|---|
| **v0.1** | 2 周 | 现 sprint：5 核心模块端到端 + 30 模块 smoke + iSoft 风 UI | 本文档 |
| **v0.2** | +10-12 天 | **UI 重设计**为 EB tresos 风（三栏 + 分类导航 + 面包屑 + Properties + Validation） + **80 模块全覆盖** | [PLAN_v0.2.md](PLAN_v0.2.md) |
| **v0.3** | +2-4 周 | **Clean-room 重写**所有 V25.10 派生代码；自家 license（简单 RSA 签名）| 等 v0.2 收尾时再细化 |
| **v0.5** | +1-2 月 | 完成第一个 OEM 客户实际项目跑通（这一步卡在 AUTOSAR 领域知识，AI 帮不了）| - |
| **v1.0** | +3-6 月 | 商业级稳定性、回归测试矩阵、多 MCU/OS 支持、完整文档 | - |

**v0.1 / v0.2 都是 "研究 / 内部 demo"**，含 V25.10 派生代码，不能商业发布。
**v0.3 是商业化的法律分水岭**：必须 clean-room 重写所有 iSoft 派生的 Python / Java 代码，
参考 V25.10 接口但不直接复制。AI 加速比从 v0.1/v0.2 的 5-10x 降到 v0.3 的 1.5-2x，
因为变成"看接口写实现"——不能再"复制粘贴 + 改 import"。

**为什么 UI 重设计放 v0.2 而不是 v0.1**：

- v0.1 sprint 14 天里**功能管线打通**已经满载（M1-M4），不能再背 UI 重做
- UI 重做要新 perspective + 4 个 view + selection 同步，Eclipse RCP 这块 AI 加速比反而低
- v0.1 出来后能立刻演示 "generate 出来的 .c/.h"，UI 风格内部知道就行
- v0.2 阶段 UI 重做和 80 模块扩展可以并行（4 实例 → A/B/C 做 UI、D 做模块）

---

## 10. 验收标准

### v0.1 通过/不通过的硬指标

| # | 标准 | 测试方法 | 阻塞 |
|---|---|---|---|
| 1 | IDE 能启动并保持 1 小时不崩 | 手测 + uptime monitor | 否 |
| 2 | 5 核心模块（Det/MemIf/NvM/Ea/Fee）的 generate 输出与 V25.10 100% 一致 | `tools/reference_diff.py` 自动跑 | **是** |
| 3 | 30 模块都能 generate 不抛异常 | smoke test 跑遍 | **是** |
| 4 | Validate 能正确报告 3 条经典跨模块错误（NvM/MemIf/Ea/Fee 配置不一致）| 故意改 ARXML，看 ProblemView | 否 |
| 5 | 改 schema 加新参数能从表单流到 C 代码（重现 docs §15 那条端到端） | 手测 | 否 |
| 6 | 一键打包 / 一键 demo 工程 | 拿到一个新 macOS / Windows 机器，按 README 操作能跑通 | 否 |

第 2、3 条是硬阻塞。其它达不到也算 v0.1，文档里写明 known issue。

---

## 11. 现在就动

授权我开干，我下一条消息就执行 §8.1 的脚本，把骨架建出来 + commit 第一个版本。

四个 Claude Code 实例的初始任务包（D1 启动）也准备好了——只要骨架建出来，可以同时分发：

- **实例 A**：去 `python_common/` 写 BswBase.py 和 Public.py（参考 `reference/ORIENTAISBswGen.exe/_pyd_analysis/BswBase.md` 和 `reference/ORIENTAISBswVal.exe/data/Bsw/MemIf/MemIfRules.py`）
- **实例 B**：去 `clone/eclipse_plugins/modules/cn.com.myorg.bswbuilder.modules.memif/` 写 plugin.xml 和 MANIFEST.MF（参考 `reference/ORIENTAISBswGen.exe/...`，但用我们自己的 vendor 名称）
- **实例 C**：去 `clone/eclipse_plugins/product/` 写 product.product 文件 + p2 metadata
- **实例 D**：去 `clone/python_generator/` 写 PyInstaller spec + 修 import 路径

每个实例的具体任务卡片我可以下一步出。先确认这份方案是不是你想要的样子。

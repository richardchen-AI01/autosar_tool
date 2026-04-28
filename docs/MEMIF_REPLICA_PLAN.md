# MemIf 完整复刻计划

> 子计划。属于 [PLAN.md](PLAN.md) 的延伸——只覆盖 **MemIf 一个模块** 的端到端复刻，
> 不涉及其它模块（Det / NvM / Ea / Fee 等）的 IDE 体验。

## 0. 目标

在我们仓里实现一个 **MemIf 模块**，让用户在我们的 IDE 里做的所有事（打开、看、改、
校验、生成）**视觉与行为都与 ORIENTAIS V25.10 里的 MemIf 等价**，并且 ARXML 文件
**双向兼容**：

- 我们 IDE 存的 ARXML 能在 ORIENTAIS V25.10 打开，显示一致
- ORIENTAIS V25.10 存的 ARXML 能在我们 IDE 打开，显示一致
- 双向操作的最终文件 **字节级一致**（除时间戳行外）

## 1. 范围

### 做

- MemIf 模块从 schema 到 GUI 到生成 / 校验整条链
- 从 AUTOSAR R23-11 公开 spec + 观察 ORIENTAIS 外部行为 + Sphinx/Artop 公开 doc，
  实现参考项目 .class 等价的不可见语义（spec-only 路线，详见 §3）
- 跟 ORIENTAIS V25.10 的等价性比对（同一份 ARXML、同一份 demo workspace）

### 不做

- 其它任何模块（Det / NvM / Ea / Fee 等）的 IDE 体验
- iSoft 私有的加密 / 授权 / 序列化（`cn.com.isoft.mal.encrypt.*` 等）
- 跨模块联动的对侧（NvM ↔ MemIf ↔ Ea 链路只复刻 MemIf 端那一半）
- AUTOSAR R23-11 之外的 schema 兼容
- 商业化合规（v0.3 clean-room 的事，见 [PLAN.md §9.3](PLAN.md#93-法律分水岭)）

## 2. 参考项目里 MemIf 的资产清单

把 ORIENTAIS V25.10 里所有跟 MemIf 沾边的产物逐项列出来，标"现状 / 替代方案 / 风险"。

| # | 参考资产 | 类型 | 现状 | 复刻方案 | 风险 |
|---|---|---|---|---|---|
| 1 | `bswmd/Common/MemIfDef.arxml` | ECUC schema | ✅ 已 ship 自有（4 参数 + iSoft 探针）| — | 低 |
| 2 | `MemIf_Bswmd.arxml` 骨架 | BSWMD impl | ✅ Python 端已生成对齐 | — | 低 |
| 3 | `MemIfGenerator.class` | Java 生成器入口 | ⚠️ Python 端已对齐；Java 入口缺 | 不复刻 Java 入口；保持 IDE 按钮 shell out 到 Python | 低 |
| 4 | `MemIf_Cfg_c.class` / `MemIf_Cfg_h.class` | 文件 emitter | ✅ Python jinja 已 byte-equal | — | 低 |
| 5 | `MemIfValidator.class` | 校验入口 | ⚠️ Python 端 TCPP_2170/2171 已实现；IDE Problems View 集成缺 | 不复刻 Java；Python validator stdout / JSON → 解析回 IMarker | 中 |
| 6 | `MemIfMessages.json` | i18n 报错文案 | ✅ 已 copy（字节级一致）| — | 低 |
| 7 | `MemIfBswmdData.class` | schema 元数据加载 | ❌ 缺 | spec-only：让 Sphinx 自动从 MemIfDef.arxml 加载，不写等价类 | 中 |
| 8 | `MemIfMetaModelDescriptor.class` | Sphinx EMF 描述符 | ❌ 缺 | spec-only：写 30 行最小 IMetaModelDescriptor 实现 | 中 |
| 9 | `MemIfDefaultRegistry.class` | **表单布局** | ❌ 缺 | spec-only：用 Sphinx auto-render 默认表单，不逐像素复刻 iSoft UI | **高** |
| 10 | `MemIfUpdateBswmd.class` | 旧 ARXML 升级到新 schema | ❌ 缺 | v0.1 不做；写 stub return null；记 known issue | 低（已知差距）|
| 11 | `MemIfFunctionExtension.class` | 业务 hook 入口注册 | ❌ 缺 | spec-only：5-10 行注册逻辑挂到我们自己的扩展点 | 低 |
| 12 | `MemIfGeneralEaMapSupport.class` | **auto-fill NumberOfDevices**（EA 侧）| ❌ 缺 | spec-only：EMF model change listener，行为对齐 Python `MemIf.derivedNumberOfDevices` | **高** |
| 13 | `MemIfGeneralFeeMapSupportEnable.class` | **auto-fill** Fee map 启用 | ❌ 缺 | 同上 | **高** |
| 14 | iSoft 工具栏 / 菜单的 "Generate / Validate / Update Bswmd" 入口 | UI hook | ⚠️ 已注册占位 button，handler 是 stub | 把 stub 换成真调用 Python 子进程 + 流式 console | 中 |
| 15 | iSoft 风的属性面板（Description / Definition / Status 三 tab）| UI | ❌ 缺 | 用 IPropertySource + ECUC ParamDef 元数据；不必逐字符复刻 | 中 |
| 16 | Tree view 里 MemIf 节点的图标 | UI 资源 | ❌ 缺 | 自绘一个等价的（不直接抄 PNG，避免 trade dress）| 低 |

→ **原计划要反编的 4 项**（#9 / #11 / #12 / #13）改走 spec-only 实现。详见 §3。

## 3. spec-only 实现策略（原"反编填补"已废弃）

> **2026-04-28 重大变更**：执行 §7.P1 时发现 iSoft 的所有 MemIf .class 文件**都是
> 加密的**（magic bytes `eb df 9b 9f`，不是标准 Java `ca fe ba be`），CFR / Procyon /
> javap 都读不了。原计划 "反编 → paraphrase" 路线被堵死。
>
> 改走 **spec-only 实现**：放弃反编，从 AUTOSAR R23-11 公开 spec + 观察 ORIENTAIS
> 跑起来的外部行为 + Eclipse Sphinx / Artop 公开 JavaDoc 三条信息源拼出自有实现。
>
> 详见 [ADR 0006](decisions/0006-memif-replica-source-strategy.md)。

### 信息源（不再反编）

1. **AUTOSAR R23-11 ECUC Templates spec** — 公开标准，定义 MemIf 模块的所有参数
   语义、跨模块约束（NvM ↔ MemIf ↔ EA/FEE）、derived 参数的计算规则
2. **观察 ORIENTAIS 跑起来的外部行为** — 启动参考 IDE，操作 demo workspace，记录
   输入 / 输出 / UI 反馈，反推语义。**不**反编、**不**绕加密、**不**抓内存
3. **Eclipse Sphinx + Artop 公开文档 / 源码** — 都是 EPL，可直接读、可直接抄

### 每个 MemIf 能力的实现策略

| MemIf 能力 | 信息源 | 自有实现策略 |
|---|---|---|
| `MemIfBswmdData` (schema 元数据加载) | Sphinx `IModelDescriptor` JavaDoc + Artop 示例工程 | 让 Sphinx 自动从我们 ship 的 `MemIfDef.arxml` 加载，不写 iSoft 的等价类 |
| `MemIfMetaModelDescriptor` | Sphinx 公开 API + autosar 公开 nsURI | 写一个 30 行最小 `IMetaModelDescriptor` 实现；引用 `http://autosar.org/schema/r4.0` 即可 |
| `MemIfDefaultRegistry` (form layout) | Sphinx `org.eclipse.sphinx.emf.editors.forms` 默认 generator | 接受 Sphinx auto-render 的默认表单；不逐像素复刻 iSoft UI |
| `MemIfFunctionExtension` (注册 hook) | 看我们自己的 plugin.xml extension 点签名 | 写 5-10 行注册逻辑，注册到我们自己的扩展点 |
| `MemIfGeneralEaMapSupport` / `FeeMapSupportEnable` (auto-fill) | AUTOSAR R23-11 ECUC TPS spec MemIf 章 + 我已有的 Python `MemIf.derivedNumberOfDevices` | 用 EMF model change listener，每次 NvM 模型 dirty 时重算 `numberOfDevices = (有 EaRef ? 1 : 0) + (有 FeeRef ? 1 : 0)` |

### 法律姿态

spec-only 实现等于把 v0.3 clean-room（[PLAN.md §9.3](PLAN.md#93-法律分水岭)）原本计划的
"重新写一遍"动作**提前到 v0.1，仅针对 MemIf**。

法律姿态从此比原计划更稳：MemIf 这条线 v0.1 release 也可以含（前提是
`generator/modules/MemIf/`、`validator/Bsw/MemIf/`、`samples/Demo_S32K148/`、
`schemas/common/MemIfDef.arxml` 这些 V25.10 派生资产**不**进入 release artifact）。
其它模块（Det / NvM / Ea / Fee）的 v0.1 demo 范围保留派生资产用法不变，仍是研究 demo。

### 验证手段（不变）

不论实现方式如何，最终的退出条件是 §5 那 8 条硬指标，特别是双向 ARXML byte-equal
这一条。spec-only 容易在某些细节上跟参考行为有可见偏差——靠 §5 验收兜底。

## 4. 阶段化路径

每个 Phase 都有明确的：进入条件 / 退出条件（自动验收脚本 + 手测剧本）。

### Phase A — 只读看

**目标**：在我们 IDE 里能"导入 demo workspace → 在 tree view 里看到 MemIf →
双击 → 表单显示 4 个参数的当前值"。

| 项 | 内容 |
|---|---|
| 进入条件 | Phase 1 完成（按钮加载 ARXML 弹窗显示 NumberOfDevices=2，已通过） |
| 关键产物 | `MemIfBswmdData` 等价（Sphinx 自动加载 MemIfDef.arxml）/ tree view ContentProvider / 双击触发的只读 Form |
| 退出条件（自动） | `tools/test_memif_phase_a.sh`：headless 启动 RCP，注入 `samples/Demo_S32K148`，console 出现 "MemIf node visible, form rendered, NumberOfDevices=2" |
| 退出条件（手测） | 启动 RCP → File → Open Workspace → 选 demo → 树展开 → 双击 MemIf → 表单出来，4 个值正确，**界面截图与 ORIENTAIS 同操作截图并排**对比无明显差异 |

### Phase B — 可编辑 + 保存

**目标**：改 `MemIfNumberOfDevices` 为 `1`，Ctrl+S，关掉再开，值还是 1；
用 ORIENTAIS 打开同一文件，看到的也是 1。

| 项 | 内容 |
|---|---|
| 进入条件 | Phase A 通过 |
| 关键产物 | EditingDomain + Command stack；ARXML 序列化（保持元素顺序、缩进、命名空间）；脏状态指示；冲突 / 文件外部变更检测 |
| 退出条件（自动） | java 单测：load → mutate → save → byte-compare（除时间戳外）= 0 |
| 退出条件（手测） | 在我们 IDE 改值保存，然后用 ORIENTAIS 打开同文件，确认看到的值变了；再在 ORIENTAIS 改回去保存，我们这边重开看到改回去的值 |
| 主要风险 | EMF EditingDomain + ARXML round-trip 是最硬的一关；若 Sphinx 路径走不通需要回退到 DOM-level 改写 |

### Phase C — Auto-fill（spec-only 实现 NumberOfDevices 联动）

**目标**：在 NvM 里加一个 NvMFeeRef → 切回 MemIf 表单 → `MemIfNumberOfDevices`
自动从 1 变 2，跟 ORIENTAIS 行为一致。

| 项 | 内容 |
|---|---|
| 进入条件 | Phase B 通过 |
| 关键产物 | Java 端 EMF model change listener 监听 NvMTargetBlockReference 子树；行为对齐 Python `MemIf.derivedNumberOfDevices`；4 种组合（仅 Ea / 仅 Fee / 都有 / 都无）行为表先在 demo workspace 上跑 ORIENTAIS 观察后落到 `docs/reference/memif-derived-truth-table.md` |
| 退出条件（自动） | 在 demo workspace 里加一个 NvMFeeRef block → 跑 script → 读 MemIf 表单的 NumberOfDevices 值 → 等于真值表对应行 |
| 退出条件（手测） | 4 种组合肉眼看，跟 ORIENTAIS 同操作截图对照一致 |

### Phase D — Validate / Generate 按钮真用

**目标**：工具栏 "Validate MemIf" 点了 → Problems View 弹错误（如果 ARXML 有
TCPP_2170/2171 违规）；"Generate MemIf" 点了 → 输出 .c/.h 到 `config/`，跟命令行
`python -m generator -g MemIf` 输出一致。

| 项 | 内容 |
|---|---|
| 进入条件 | Phase B 通过（这两件事之前 Phase A/B 已能做但 handler 是 stub） |
| 关键产物 | `BswgenLauncher` / `BswvalLauncher`（已 80% 写好）；Problems View IMarker 桥接（解析 validator stdout / JSON）|
| 退出条件（自动） | 跑 BAD_2170 demo → 点 Validate → Problems 出现 1 条 TCPP_2170 红色 marker；跑 demo → 点 Generate → 输出 .h 与 reference byte-equal |
| 退出条件（手测） | Validate 后红色错误能跳到对应 ARXML 行；Generate 时 console 能流式看到 Python 输出 |

### Phase E — Properties 面板 + UI polish

**目标**：选中一个参数 → 底部 Properties 面板有 Description / Definition / Status
三 tab，内容来自 schema 元数据。

| 项 | 内容 |
|---|---|
| 进入条件 | Phase A 通过 |
| 关键产物 | IPropertySource 实现；selection listener；图标资源；自定义状态文案 |
| 退出条件（手测） | 选中 NumberOfDevices → Description tab 显示 "Concrete number of underlying memory abstraction modules."；Definition tab 显示 ECUC-INTEGER-PARAM-DEF + MIN/MAX；Status tab 显示当前 dirty / 默认值 / 是否 derived |

### Phase F — Round-trip 兼容性硬测试

**目标**：拿 5 份不同的 ARXML 文件（demo + BAD_2170 + BAD_2171 + 极小 + 极大），
双向编辑，验证字节级兼容。

| 项 | 内容 |
|---|---|
| 进入条件 | Phase A-E 全过 |
| 关键产物 | `tools/test_memif_roundtrip.sh` 自动跑 5 个文件双向 |
| 退出条件（自动） | 5/5 文件双向 byte-equal（除时间戳行）|
| 退出条件（手测） | 把 ORIENTAIS 改完保存的 ARXML 直接 git diff 跟我们改完的 ARXML 比，0 行差异 |

## 5. 验收硬指标（"MemIf 复刻成功"的定义）

不达成不算"复刻成功"：

1. ✅ 启动我们的 RCP → 打开 `samples/Demo_S32K148` → 视觉上看到 MemIf node + 表单
2. ✅ 改 4 个参数中的任意一个 → 保存 → 重启 → 值保留
3. ✅ 用 ORIENTAIS V25.10 打开同一文件 → 显示同样的值
4. ✅ 反过来：ORIENTAIS 改完，我们 IDE 打开 → 显示同样的值
5. ✅ 在 NvM 里 mutate EA/FEE 引用 → MemIf 的 NumberOfDevices 自动联动（跟 ORIENTAIS 一致）
6. ✅ 工具栏 Validate / Generate 与命令行行为一致
7. ✅ Properties 面板有 Description / Definition / Status 三 tab
8. ✅ `tools/test_memif_roundtrip.sh` 5/5 PASS

## 6. 风险登记

| # | 风险 | 概率 | 影响 | 对策 |
|---|---|---|---|---|
| R1 | EMF EditingDomain + ARXML 序列化（Phase B）不能 100% 保留元素顺序 / 命名空间 | 高 | F 失败 | 直接用 Sphinx ExtendedResource，不自己写 XMI；如不行回退到 DOM-level 改写 |
| R2 | DefaultRegistry 反编后是用 Forms API 手写大量 widget，不是数据驱动 | 中 | Phase A 工作量翻倍 | 接受 "不逐像素复刻"，让 Sphinx 默认生成器渲染，截图比对接近即可 |
| R3 | Function extension 的"何时触发 / 监听哪个事件"反编看不出来 | 中 | Phase C 行为不一致 | 用 model change listener + 全模型 dirty 时 re-derive，性能差点但行为对 |
| R4 | ARTOP 4.5.2 + Sphinx 0.11.2 跟 Eclipse 2024-09 兼容性裂缝 | 中 | 任意阶段崩 | Phase A 起步先把 minimal Sphinx + ARTOP 集成跑通；发现版本不兼容立刻退到 ORIENTAIS 用的 Eclipse 4.x 老版 |
| R5 | 反编后的代码合法性边界（"我看了反编但写自己的"边界在哪）| 中 | 法律 | `docs/decisions/0006-decompile-scope.md` 明确 paraphrase 流程；反编原文不入 git |
| R6 | 工具链：Mac/Win 谁是 build canonical | 中 | 协作摩擦 | 起 ADR 锁定 → Mac 是 daily dev / Win 是 RCP 实际运行 sandbox |
| R7 | Phase B 之后如果 round-trip 不过，前面 Phase 全部白做 | 中 | 整体回退 | Phase A 之后立刻做一次"最小可行 round-trip 测试"（即使表单没做完），把 R1 风险尽早暴露 |

每周 review 一次风险登记，标记新风险 / 失效风险。

## 7. 在动手之前必须先做的 4 件事（pre-conditions）

| # | 动作 | 产物 |
|---|---|---|
| P1 | 反编 4 个核心 .class，做合法性 review，写 `docs/decisions/0006-decompile-scope.md` | 反编原文（gitignored）+ ADR |
| P2 | 起 `docs/MILESTONES_memif_replica.md`，把 Phase A-F 的退出条件全转成可执行 shell 命令 | milestone 文档 |
| P3 | 起 `docs/risks-memif.md` 把 §6 那张表落到纸面，并约定每周 review 一次 | risk 文档 |
| P4 | 在 PLAN.md 里加一节 §10「MemIf 完整复刻 sub-sprint」，one-line 链回这份文档 | PLAN 编辑 |

不做这 4 件事就开干，会回到"打游击"循环。

## 8. 关键决策点

按重要性排，需要在 Phase A 起步前确认：

1. **Phase B 的 ARXML round-trip 用 Sphinx 还是自写 DOM**？  
   Sphinx 风险低但学习曲线陡；自写 DOM 简单但兼容 corner case 容易出问题。
   **推荐：先 Sphinx；若 Phase B 起步出 R1 风险，立刻回退到 DOM**。

2. **Function extension（Phase C）走 Java 还是延续 Python derive-pass**？  
   Java 跟参考行为对齐度更高；Python derive-pass 已加了 `MemIf.derivedNumberOfDevices`。  
   **推荐：反编后看代码量决定——< 200 行就 Java，否则 Python 兜底**。

3. **反编合法性边界**——本机反编 + paraphrase 出 ship 代码，作为 v0.1 研究 demo OK。
   **正式 release / 商业化必须 v0.3 clean-room，重新走一遍**。  
   **决策：在 NOTICE.md 里加一段 explicitly 说明这条边界**（已在 P1 的 ADR 中覆盖）。

## 9. 进度记账

每个 Phase 完成（自动 + 手测都过）后：

1. 在 `docs/MILESTONES_memif_replica.md` 把对应 Phase 标记 ✅ + 实际完成日期
2. `docs/sprint-logs/D<n>.md` 当日记录写一段「MemIf Phase X done, 通过手段 Y, 遇到 Z」
3. CHANGELOG.md 加一行（不写时间，只写 phase 编号 + 关键 deliverable）
4. 如果发现新风险，加进 `docs/risks-memif.md`

不批量更新——每个 Phase 收尾就更新一次，否则文档迟早变成"早晨写的 plan"。

## 10. 关联文档

- [PLAN.md](PLAN.md) — 主 sprint 计划（这份是它的子计划）
- [MILESTONES.md](MILESTONES.md) — v0.1 主 sprint 的 M1-M4 里程碑
- [ARCHITECTURE.md](ARCHITECTURE.md) — 三层架构地图
- 即将创建：
  - `docs/MILESTONES_memif_replica.md`（在 P2 起）
  - `docs/risks-memif.md`（在 P3 起）
  - `docs/decisions/0006-decompile-scope.md`（在 P1 起）

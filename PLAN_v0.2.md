# v0.2 sprint plan · UI 重设计 + 80 模块全覆盖

> v0.2 是 v0.1 上线之后的下一个里程碑 sprint。在 v0.1（功能管线打通、iSoft 风格 UI）的基础上，
> 主要做两件事：
>   1. **UI 重设计** 为 EB tresos 风格（三栏 + 分类导航 + 面包屑 + Properties + Validation）
>   2. **模块覆盖** 从 30 扩到 80（V25.10 全部 BSW 模块）
>
> 入口看板：[README.md](README.md) · 主方案：[PLAN.md](PLAN.md) · v0.1 里程碑：[MILESTONES.md](MILESTONES.md)

---

## 0. 目标

```
v0.1 出来后 1-2 周内交付 v0.2：
  ① 三栏 + 底部 Properties + 右下 Validation 的全新 perspective
  ② 80 模块全覆盖（generate 不抛异常）
  ③ 5 核心模块继续保持跟 V25.10 reference 100% diff
  ④ Validation 面板能筛选严重级，且跨模块联动校验全跑通
```

## 1. UI 重设计：从 iSoft 风格切到 EB tresos 风格

### 1.1 目标布局

```
┌──────────────┬─────────────────────────┬──────────────────────────────────────────┐
│ Configuration│  CanTp > CanTpGeneral   │ Safe Bsw Checks                  ✓        │
│ Editors      │ ┌─────────────────────┐ │ Single Rx Buffer Optim           ☐ *      │
│ <Filter>     │ │<Filter>             │ │ Split Main Function              ☐ *      │
│              │ ├─────────────────────┤ │ Support Addressing 'Extended'    ☐ *      │
│ ▾ Base Svc  │ │  ▸ BswMGeneral      │ │ Support Addressing 'Mixed11'     ☐ *      │
│   Det       │ │  ▾ Can              │ │ Support Addressing 'Standard'    ✓ *      │
│   Crc       │ │    CanConfigSet     │ │ Support CAN-FD                   ☐ *      │
│ ▾ Communic. │ │    CanGeneral       │ │ Support Long First Frames        ☐ *      │
│   Can       │ │  ▾ CanIf            │ │ Synchronous Transmission         ✓        │
│   CanIf     │ │    CanIfCtrlDrvCfgs │ │ Transmit Cancellation            ☐ *      │
│   CanTp ◀───┼─┼─▾ CanTp            │ │ Transmit Queue                   ☐ *      │
│   ...       │ │    CanTpConfig      │ │ Use Only First Fc                ✓        │
│ ▸ Diagnostic│ │    CanTpGeneral ◀───┼─│ User Config File                 [...]    │
│ ▸ I/O       │ │  ▸ CanSM           │ │ Version Info Api                 ☐ *      │
│ ▸ Memory    │ │  ...                │ │                                            │
│ ▸ Mode Mgmt │ └─────────────────────┘ │                                            │
│ ▸ Network   │                         │                                            │
│ ▸ Runtime   │                         │                                            │
├──────────────┴─────────────────────────┼──────────────────────────────────────────┤
│ Properties [User Config File]          │ Validation                  50 messages  │
│ ▸ Description: Reference to external...│  ⚠ Rule_BSW_MemIf_TCPP_2170 ...           │
│   Definition: ECUC-STRING-PARAM-DEF... │  ⚠ Rule_BSW_CanTp_..., ...                 │
│   Status:     <empty>                  │  filter: [ All ▼ ] [Errors] [Warn] [Info] │
└────────────────────────────────────────┴──────────────────────────────────────────┘
```

### 1.2 8 处变化点对照

| # | 变化点 | iSoft V25.10 | EB tresos 风 | 实现 |
|---|---|---|---|---|
| 1 | 左栏分类导航 | Project Explorer 平铺 | 8 大类折叠 | 自定义 ContentProvider + taxonomy |
| 2 | 左栏 `<Filter>` | 无 | 实时过滤 | JFace `FilteredTree` |
| 3 | 中栏容器树 | 嵌在 MasterDetail | 独立 view | 抠出 tree 部分成 standalone view |
| 4 | 中栏面包屑 | 无 | `CanTp > CanTpGeneral` | ToolBar + selection listener |
| 5 | 中栏 `<Filter>` | 无 | 当前模块的容器过滤 | 同 #2 |
| 6 | 右栏参数表单 | 嵌在 MasterDetail | 独立 view，跟随选择 | 抠出 form 部分；监听中栏 selection |
| 7 | 底部 Properties | 简易 | Description / Definition / Status 三 tab | IPropertySource + ECUC ParamDef 元数据 |
| 8 | 右下 Validation | 现有 view 但风格不同 | 紧凑 + 严重级筛选 | view 重 layout + filter toolbar |

### 1.3 模块分类 taxonomy（8 大类、80 个模块映射）

```yaml
Base Services:
  - Det
  - Crc
  - IStdLib

Communication:
  - Can, CanIf, CanTp, CanNm, CanSM, CanTSyn, CanTrcv
  - LinIf, LinTp, LinSM
  - Eth, EthIf, EthSM, EthTSyn, EthTrcv
  - SoAd, TcpIp, DoIP
  - Com, ComM, IpduM, PduR, SecOC, LdCom, J1939Tp, J1939Nm, J1939Rm, J1939Dcm
  - CDD_*

Diagnostics:
  - Dcm, Dem, FiM, Dlt, IdsM, Xcp

I/O:
  - Adc, Pwm, Spi, Dio, Port, Gpt, Icu

Memory:
  - NvM, MemIf, Ea, Eep_62, Fee_62, MemMap, MemLayout, FlsTst, RamTst

Mode Management:
  - BswM, EcuM

Network Management:
  - Nm, OsekNm

Runtime System:
  - Rte, Os, WdgM, WdgIf, AppStub, Sd, StbM, Csm, CryIf, Crypto_62, KeyM, Tm, E2E, Bfx
```

每个模块归类后还要标"显示顺序权重"（数字越小越靠前）保证 OEM 习惯的视觉顺序。

---

## 2. 模块覆盖：从 30 扩到 80

### 2.1 v0.1 已覆盖 30 个

```
Det, MemIf, NvM, Ea, Fee, EcuM, Os, WdgM,           # 8 系统服务/内存
Com, PduR, CanIf, Can, CanTp, BswM,                  # 6 通信
Crc, Dem, Dcm, Mcu, Port, Dio, Gpt, Wdg, IpduM,     # 9 driver/诊断
LinIf, LinSM, Nm, CanNm, CanSM, ComM, Rte           # 7 NM/Rte
```

### 2.2 v0.2 新增 50 个（按优先级）

| 优先级 | 类别 | 模块 |
|---|---|---|
| P1 | 通信 | CanTSyn, CanTrcv, LinTp, EthIf, EthSM, EthTSyn, SoAd, TcpIp, DoIP, SecOC, LdCom |
| P1 | 加密 | Csm, CryIf, Crypto_62, KeyM, IdsM |
| P2 | 通信扩展 | J1939Tp, J1939Nm, J1939Rm, J1939Dcm, Sd, StbM, Tm |
| P2 | 内存扩展 | Eep_62, MemMap, MemLayout, FlsTst, RamTst |
| P2 | 诊断扩展 | FiM, Dlt, Xcp |
| P3 | I/O 扩展 | Adc, Pwm, Spi, Icu |
| P3 | 工具/CDD | AppStub, Bfx, E2E, IStdLib, OsekNm, WdgIf |
| P3 | CDD 套件 | CDD_CanIds, CDD_DcmClient, CDD_DoIPClient, CDD_FVM |

### 2.3 工作量估算

| 子任务 | 工时 |
|---|---|
| 50 模块的 plugin jar 骨架（每个 ~30 分钟）| 25 工时 ≈ 3 天 |
| 50 模块的 Python 代码 import 路径调整（已有 V25.10 reference）| 12 工时 ≈ 1.5 天 |
| 50 模块跑通 smoke（generate 不抛异常）| 16 工时 ≈ 2 天 |
| **小计** | **6-7 天**（一个实例并行可压到 3-4 天）|

---

## 3. UI 重设计 + 模块覆盖：合并排期

### 3.1 设原 sprint：10-12 个工作日

| 实例 | D1-3 | D4-6 | D7-9 | D10-12 |
|---|---|---|---|---|
| **A** UI Perspective | 写 perspective.xml + 三栏空骨架 | 容器树 view + form view 抠出来 | 选择联动 + 面包屑 | bug 修 |
| **B** Navigator + 分类 | taxonomy YAML + ContentProvider | Filter 框 + 折叠态 | 选模块 → 切到中栏 | UI 一致性 |
| **C** Properties + Validation | IPropertySource 实现 | Description/Definition/Status 三 tab | Validation severity filter | UI polish |
| **D** 50 模块覆盖 | 批量 jar 骨架（25 个）| 批量 jar 骨架（25 个）| 50 个 generate smoke | 跨模块校验 |
| **You** | review + 协调 | review | 集成测试 | release |

### 3.2 4 个 v0.2 里程碑

| Milestone | 截止 | 验收 |
|---|---|---|
| **M5** | D3 EOD | 三栏 perspective 能弹出来（哪怕空空的）+ taxonomy YAML 就位 |
| **M6** | D6 EOD | 中栏容器树 + 右栏 form 联动工作（选 CanTpGeneral，右栏立刻显示对应参数）|
| **M7** | D9 EOD | 80 模块都能 generate；左栏 8 类导航 + 面包屑 + filter 全工作 |
| **M8** | D12 EOD | v0.2 release：UI 一致 + 80 模块覆盖 + 5 核心 diff 仍 = 0 |

详细 checkable 命令清单等 v0.2 sprint 启动当天再写（参考 v0.1 [MILESTONES.md](MILESTONES.md) 格式，
新建 `MILESTONES_v0.2.md`）。现在过早写会因为 v0.1 retro 反馈而过时。

---

## 4. 风险与对策

| # | 风险 | 应对 |
|---|---|---|
| R1 | 跨 view selection 同步是 Eclipse RCP 老大难，AI 加速比低 | M5 之前就要打通最小 4-view 联动；如果 D5 还没好，砍掉 #4 面包屑、#5 中栏 filter 这种锦上添花的 |
| R2 | EB tresos 的 ☐ * 这种"非默认值"标记可能涉及商业产品 UI 的 trade dress | 用我们自己的视觉语言（比如用 ▴ 或灰色背景）表达"非默认值"，不直接抄星号 |
| R3 | 50 个新模块里有边角 case（schema 复杂的如 Rte / Dcm）跑不通 | v0.2 release 接受 5-10 个模块标 known issue，列入 docs/99 |
| R4 | 模块分类有歧义（CDD_CanIds 算 Communication 还是单独类）| taxonomy YAML 在 D1 就 freeze，后续不再调 |
| R5 | OEM 看到新 UI 觉得"不像他们熟悉的 Vector / EB"，回退要求 | v0.1 那套保留作为 alternative perspective，运行时 Window → Open Perspective → "iSoft Classic" 仍可切回 |

---

## 5. 法律提醒（v0.2 不再是研究 demo）

v0.2 如果还包含 V25.10 派生的 Python 代码（`generator/modules/<Module>/*.py` 这些），**仍属于研究 / 内部用，不能商业化**。

商业化路线（v0.3 起）需要 clean-room 重写：
- 把 `generator/modules/` 整个换成自己实现（每个模块 ~200-500 行 Python，AI 加速 2-3x）
- iSoft 衍生 jar（cn.com.isoft.bswbuilder.\*）替换为自家 namespace 的 clean-room 实现
- 引用 ARTOP / Sphinx 的部分继续合法（你是 ARTOP 会员或买断）

预估 v0.3 单独 sprint：2-4 周。

---

## 6. v0.1 → v0.2 → v0.3 → v1.0 总路线图

```
v0.1 (14 天)      ──→  功能管线 + iSoft 风 UI + 30 模块         [研究 demo]
                                                                       │
v0.2 (10-12 天)   ──→  EB tresos 风 UI + 80 模块全覆盖           [研究 demo]
                                                                       │
v0.3 (2-4 周)     ──→  Clean-room 重写所有 V25.10 派生代码        [商业化预备]
                                                                       │
v0.5 (1-2 月)     ──→  第一个 OEM 客户实际项目跑通               [Beta]
                                                                       │
v1.0 (3-6 月)     ──→  商业级稳定性 + 完整测试矩阵               [Production]
```

---

## 7. 现在不动手

v0.2 sprint 不立即开。先把 v0.1 的 14 天打透：
- v0.1 的 4 个里程碑（M1-M4）按 [MILESTONES.md](MILESTONES.md) 跑
- v0.1 release 之后，根据实际进度（特别是是否有延期）再决定 v0.2 起跑日

v0.1 release 当天的 retrospective 输出几条决策点：
1. AI 加速比实际是多少？（比预期更高就压 v0.2 工期，更低就放宽）
2. 哪些模块 v0.1 没覆盖好但 v0.2 优先要补？
3. 客户 / 老板看到 v0.1 demo 后对 UI 风格的真实反馈
4. v0.3 clean-room 是否要并行在 v0.2 同步启动

带着这些信息再正式启动 v0.2，比现在提前规划得更细更准。

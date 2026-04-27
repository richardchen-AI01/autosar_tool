# AUTOSAR Configurator 复刻项目（v0.1 sprint）

> 2 周内、用 Claude Code 多实例并行 + 已挖出的 ORIENTAIS Configurator V25.10 整套源码作为种子，
> 端到端复刻一个能跑、能演示的 AUTOSAR BSW Configurator。

## 入口文档

| 文档 | 用途 |
|---|---|
| **[PLAN.md](PLAN.md)** | v0.1 完整方案：14 天逐日排期、4 个里程碑、资产盘点、架构、风险登记 |
| **[MILESTONES.md](MILESTONES.md)** | v0.1 可执行里程碑清单：每条带具体命令 + 期望输出 + 通过/不通过条件 |
| **[PLAN_v0.2.md](PLAN_v0.2.md)** | v0.2 sprint：UI 重设计为 EB tresos 风格 + 80 模块全覆盖（10-12 天，v0.1 release 后启动）|

## 快速一览

| | |
|---|---|
| 工期 | 14 天（2026-04-27 → 2026-05-11） |
| 团队 | Claude Code 4 实例并行 + 1 人协调 |
| 起点 | `/Users/richard/AI-MiniWorkspace/project/autosar-cfg/`（已反编 V25.10 全套）|
| 里程碑 | M1 (D3) IDE 启 + 13 helper 替换 → M2 (D7) MemIf 端到端 → M3 (D11) 30 模块 + 校验 → M4 (D14) v0.1 demo |
| v0.1 定位 | **研究 / 内部 demo**，不商用（含 V25.10 派生代码）|
| 商业化路径 | v0.3 起 clean-room 重写，第 +6-12 个月达到商业级（v1.0） |

## 版本路线一览

```
v0.1 (14 天)      ──→  iSoft 风 UI + 5 核心模块端到端 + 30 smoke    [研究 demo]
v0.2 (10-12 天)   ──→  EB tresos 风 UI + 80 模块全覆盖              [研究 demo]
v0.3 (2-4 周)     ──→  Clean-room 重写所有 V25.10 派生代码           [商业化预备]
v0.5 (1-2 月)     ──→  第一个 OEM 客户实际项目跑通                  [Beta]
v1.0 (3-6 月)     ──→  商业级稳定性 + 完整测试矩阵                  [Production]
```

**当前阶段：v0.1 sprint 设计完毕，等授权启动 D1**。

## 目录（D1 建好后）

```
Autosar_tool/
├── PLAN.md
├── README.md  (this)
├── docs/                设计文档
├── clone/               真正的代码
│   ├── eclipse_plugins/   Eclipse RCP 工程
│   ├── python_common/     13 个原 .pyd 的 Python 等价
│   ├── python_generator/  bswgen.exe 源码
│   ├── python_validator/  bswval.exe 源码
│   ├── bswmd/             ECUC schema 资产
│   └── test_workspace/    Demo_S32K148 黄金对照
├── tools/               构建脚本
└── reference/           V25.10 reference (软链)
```

详见 PLAN §7 目录骨架。

## 现在做什么

PLAN §8 起步动作给出了 D1 第一件事的命令脚本和实例任务清单。授权后我直接执行 §8.1
建 monorepo 骨架。

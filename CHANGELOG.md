# Changelog

格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，
版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。

## [Unreleased] — 进行中

### Added
- 项目立项与方案设计：`README.md`、`PLAN.md`、`MILESTONES.md`、`PLAN_v0.2.md`
- v0.1 sprint 14 天计划与 4 个里程碑（M1-M4）
- v0.2 sprint 计划：UI 重设计为 EB tresos 风格 + 80 模块全覆盖
- `.gitignore` 覆盖 Python / Java / Eclipse / macOS / 大二进制制品

### Changed
- **策略调整：sprint 重排为 MemIf-first / Walking Skeleton 模式**
  - 原计划：M1 横向地基 → M2 三模块端到端 → M3 横向铺 30 模块
  - 新计划：M1 MemIf 单模块走通（链路通，diff 可不为 0）→ M2 MemIf 完美（diff = 0 + 跨模块校验 + docs §15 端到端补丁实战可重现）→ M3 用 MemIf 模板复制到 5 核心 + 30 smoke
  - 理由：第一个模块端到端打透后，所有架构性问题在 D3 EOD 就暴露完毕；后续模块呈线性机械复制，风险显著前移降低
- M1/M2 检查项重写：M1 仅要求 5 个 native helper（MemIf 实际用到的那批），剩余 8 个先 stub；M2 才要求全部 13 个

### Notes
- 项目代号：**Autosar_tool**
- 起源：基于 ORIENTAIS Configurator V25.10 的反编结果（详见
  `/Users/richard/AI-MiniWorkspace/project/autosar-cfg/`）作为种子工程
- 当前定位：研究 / 内部 demo（v0.1, v0.2 阶段）；商业化路径见 PLAN §9 v0.3 起

## 模板（供未来 release 使用）

> ## [vX.Y.Z] — YYYY-MM-DD
>
> ### Added
> ### Changed
> ### Fixed
> ### Removed

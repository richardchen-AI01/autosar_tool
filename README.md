# Autosar_tool

AUTOSAR ECUC code generator + cross-module validator + IDE skeleton, modeled on
ORIENTAIS Configurator V25.10. Currently at v0.1 — research / internal demo.

## 当前状态（D2, 2026-04-28）

| 里程碑 | 计划 EOD | 实际 | 状态 |
|---|---|---|---|
| **M1** MemIf walking skeleton | D3 | D2 上午 | ✅ 提前 2 天 |
| **M2.1** MemIf_Cfg.h diff = 0  vs V25.10 | D7 | D2 上午 | ✅ 提前 5 天 |
| **M2.2** MemIf_Cfg.c diff = 0 | D7 | D2 上午 | ✅ |
| **M2.3** TCPP_2170 cross-module rule fires | D7 | D2 中午 | ✅ |
| **M2.4** TCPP_2171 cross-module rule fires | D7 | D2 中午 | ✅ |
| **M2.5** docs §15 端到端补丁可重现 | D7 | D2 上午 | ✅ |
| **M2.7** 一键回归脚本 | D7 | D2 中午 | ✅ |
| **M2.6** 13 helper 全功能 | D7 | 8 stub + 5 实现 | 部分（MemIf 用到的 5 个全实现，其它 8 个 D6 stub） |
| **M3.1** 5 核心模块 diff = 0 | D11 | MemIf done; Det/NvM/Ea 各有小坑 | 进行中 |
| **M3.2** 30 模块 smoke | D11 | 4 模块 (MemIf+Det+NvM+Ea) | 进行中 |
| **M4.1** PyInstaller 打包 | D14 | macOS bswgen/bswval 已打包 OK | ✅ |

测试套件：`pytest core/tests/ generator/tests/ validator/tests/` — **16/16 PASS**

## 上手 30 秒

```bash
# 装依赖
pip install jinja2 lxml pytest pyinstaller

# 跑生成器（MemIf 模块）
PYTHONPATH=core python3 -m generator -g MemIf -i samples/Demo_S32K148 -o /tmp/out
ls /tmp/out/                      # → MemIf_Cfg.{c,h} + MemIf_Bswmd.arxml

# 跑校验器
PYTHONPATH=core python3 -m validator -m MemIf -i samples/Demo_S32K148           # 干净: 0 error
PYTHONPATH=core python3 -m validator -m MemIf -i samples/Demo_S32K148_BAD_2170  # 触发 Rule_2170

# 一键全栈回归（M2.7）
./tools/test_memif_full.sh

# 单元测试
PYTHONPATH=core:. python3 -m pytest core/tests/ generator/tests/ validator/tests/ -v

# 打包成单文件 binary（macOS / Linux）
./tools/build_all.sh                # → build/dist/bswgen, build/dist/bswval
# Windows
tools\build_all.cmd                  # → build\dist\bswgen.exe, build\dist\bswval.exe

# 每日 standup checker
./tools/daily_check.sh
```

## 目录布局

```
Autosar_tool/
├── README.md                ← 本文件
├── CHANGELOG.md             变更记录
├── docs/
│   ├── PLAN.md              v0.1 sprint 完整方案
│   ├── PLAN_v0.2.md         v0.2 UI 重设计 + 80 模块覆盖
│   ├── MILESTONES.md        可执行里程碑清单
│   ├── sprint_logs/D1.md    Day 1 sprint log
│   ├── assets/              UI 参考图
│   └── v25_pyz_source_reference/  V25.10 反编出来的参考代码（含 syntax errors，仅供阅读）
│
├── core/                    Common.* 共享库（替代 V25.10 的 13 个 .pyd）
│   ├── pyproject.toml
│   ├── Common/
│   │   ├── BswBase.py / Public.py / CodeGenerator.py / Context.py / J2Filters.py
│   │   ├── ArxmlValidator.py + base/{BaseClass,BaseDecorator}.py
│   │   ├── arxmlparse/{loader,constant/BswPathConstant(6870 项),cache,artop}
│   │   └── templates/Template_Base.jinja
│   └── tests/
│
├── generator/               bswgen 源
│   ├── pyproject.toml + bswgen.spec
│   ├── __main__.py
│   ├── modules/
│   │   ├── MemIf/             ← 5 个核心模块
│   │   ├── Det/
│   │   ├── NvM/
│   │   └── Ea/
│   └── tests/
│
├── validator/               bswval 源
│   ├── pyproject.toml + bswval.spec
│   ├── __main__.py
│   ├── Bsw/
│   │   └── MemIf/{MemIfRules.py, MemIfRegister.py, MemIfMessages.json}
│   └── tests/
│
├── schemas/                 ECUC schema 资产
│   ├── common/{MemIfDef,NvMDef,EaDef,Fee_62Def}.arxml
│   └── std/AUTOSAR_StdTypes.arxml + SwAddrMethods.arxml
│
├── samples/                 黄金对照工程
│   ├── Demo_S32K148/             V25.10 自带 demo
│   ├── Demo_S32K148_BAD_2170/    刻意触发 Rule_BSW_MemIf_TCPP_2170
│   └── Demo_S32K148_BAD_2171/    刻意触发 Rule_BSW_MemIf_TCPP_2171
│
├── ide/                     Eclipse RCP 工程（D2-D3 实例 C 战场，骨架已留）
│   ├── product/
│   ├── frameworks/
│   ├── builder_core/
│   └── modules/
│
├── tools/                   构建/检查脚本
│   ├── daily_check.sh           每天 standup checker
│   ├── test_memif_full.sh       M2.7 一键回归
│   ├── reference_diff.py        M2.1 / M3.1 diff 检查
│   ├── build_all.{sh,cmd}       PyInstaller 打 bswgen/bswval
│   └── sync_to_smb.sh           Mac → SMB 同步
│
├── reference/               V25.10 反编结果（gitignored 软链）
│   └── autosar-cfg → /Users/richard/AI-MiniWorkspace/project/autosar-cfg
│
└── build/                   构建产物（gitignored）
    └── dist/{bswgen, bswval}
```

## 版本路线

```
v0.1 (14 天)      iSoft 风 UI + 5 核心模块端到端 + 30 smoke           [研究 demo]
v0.2 (10-12 天)   EB tresos 风 UI + 80 模块全覆盖                      [研究 demo]
v0.3 (2-4 周)     Clean-room 重写所有 V25.10 派生代码                   [商业化预备]
v0.5 (1-2 月)     第一个 OEM 客户实际项目跑通                          [Beta]
v1.0 (3-6 月)     商业级稳定性 + 完整测试矩阵                          [Production]
```

详见 [docs/PLAN.md](docs/PLAN.md)。

## 法律边界

v0.1 / v0.2 含 V25.10 派生代码（`generator/modules/<Module>/`、`validator/Bsw/<Module>/`、
`samples/Demo_S32K148/`、`schemas/common/*Def.arxml`），属于**研究 / 内部 demo**，
**不能商业发布**。商业化路线请走 v0.3 clean-room 重写。

ARTOP / Sphinx jar 因为我们的合法 V25.10 用户身份才能本机使用，但禁止再分发给非 ARTOP 会员。

## 状态徽章

| 类别 | 状态 |
|---|---|
| pytest | 16 / 16 PASS |
| MemIf full pipeline | M2.1 + M2.2 + M2.3 + M2.4 + M2.5 + M2.7 PASS |
| GitHub | https://github.com/richardchen-AI01/Autosar_tool (private) |
| SMB mirror | smb://192.168.1.44/Autosar_tool |

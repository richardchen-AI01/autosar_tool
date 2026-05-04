# Changelog

格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，
版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。

## [Unreleased] — D2 EOD (2026-04-28)

### IDE 半边 — D2 晚追加（Eclipse RCP walking skeleton）

- 新增 `ide/` 完整 Tycho 4 + Java 17 多模块工程：
  - `ide/pom.xml` Tycho 父 pom
  - `ide/target-platform/bswbuilder-target/` Eclipse 2024-09 target
  - `ide/builder_core/cn.com.myorg.bswbuilder.common/` RCP shell
    （Application + WorkbenchAdvisor + ActionBarAdvisor + Perspective）
  - `ide/builder_core/cn.com.myorg.bswbuilder.ui/`
    Generate / Validate handler + ModuleNavigator view + BswgenLauncher
  - `ide/modules/cn.com.myorg.bswbuilder.modules.memif/` 占位
  - `ide/feature/cn.com.myorg.bswbuilder.feature/` 统一 feature
  - `ide/product/cn.com.myorg.bswbuilder.product/` 可启动 RCP 产品
- **唯一 IDE↔Python 桥**：`BswgenLauncher.run(Tool, args, console, monitor)`
  - 自动定位 repo 根（向上找 `generator/__main__.py + core/Common/`）
  - 优先用 `build/dist/bswgen[.exe]`，否则 fallback `python3 -m generator`
  - `PYTHONPATH=core` 注入子进程
  - 输出流式写入 BSW Builder 共享 console
- 没有 ARTOP / Sphinx 依赖，不需要 licensed jar
- Java 25 上跑 Tycho 4 需要把 `jdk.xml.maxGeneralEntitySizeLimit` 放开
  （p2 元数据超 100k 字符），已在 `ide/.mvn/jvm.config` 处理
- **e4 IEventBroker 启动失败已修复**：common plugin Require-Bundle 上
  补 `e4.core.services` / `e4.ui.services` / `equinox.event`，否则
  `CommandProcessingAddon` / `ContextProcessingAddon` 在 e3 IApplication
  上 inject IEventBroker 会报 ENTRY 4。osascript 确认 `bswbuilder` 进
  入可见 app 列表 → GUI 真起来了
- `tools/ide_smoke.sh`：自动选当前平台 launcher → 启动 → 8s 后 kill →
  检 `.metadata/.log` 是否 0 条 ERROR。本机 Mac aarch64 验证 [PASS]
- `.github/workflows/ide.yml`：Tycho 矩阵（Java 17/21）+ p2 缓存 +
  Linux 上用 xvfb-run 跑 `ide_smoke.sh`，4 平台 launcher 上传 artifacts

### M3.1 — D2 下午追加（提前 9 天）

- **Det 端到端跑通** —— 5/5 文件全生成，`Det_Bswmd.arxml` byte-equal vs
  V25.10 reference（filtered diff = 0）
  - 修复：`CodeGenerator` env.globals 注入默认 `EcucPartition=''`，让
    `Det_Bswmd_arxml.jinja` line 110 的 `VAR_CLEARED_{{EcucPartition}}_…`
    能渲染（V25.10 在没有 EcucPartition 配置时输出双下划线即空串拼接）
- **NvM 端到端跑通** —— 4/4 文件全生成，`NvM_Bswmd.arxml` byte-equal vs
  V25.10 reference
  - 新增 `core/Common/arxmlparse/artop.by_path` —— ECUC instance-path →
    EObject 的反向索引（loader 在解析 AR-PACKAGE 时按
    `/<package_sn>/<module_sn>/<container_sn>/...` 建立）
  - 新增 `core/Common/BswBase._RefTarget(str)` —— V25.10 ref-wrapper API：
    `.shortName_` / `.shortName` / `.ref_type_.shortName_` /
    `.getAttrValue` / `.getSubContainer` / `.getParentContainer`，全部
    lazy-resolve 到 `by_path[path]`
  - `_RefList` 升级：元素从 str 升为 `_RefTarget`，新增 `_first` 代理
    给单基数 ref 用法
  - `BswBase` 加 `.shortName_` / `.shortName` 委托到 `self.container`
  - 顶层 container 的 `parent_` 现在指向 owning module（mirror EMF
    eContainer 语义）
- **Ea 优雅退出** —— 模块未在 workspace 配置时不再崩在模板渲染
  - `Ea.__init__` 列表型属性（`EaBlockConfiguration` / `EaEepApi`）默认
    `[]` 而不是 `None`
  - `bswgen __main__` 加"模块是否配置"探针：查 modules 列表中 shortName
    == module_name 是否存在；不存在则 print "No ECUC configuration for X"
    + rc=0 退出
- **回归扩展** —— `tools/test_memif_full.sh` 从 7 项扩到 10 项（+ Det /
  NvM / Ea 三项 M3.1 检查），全部 PASS
- **测试覆盖** —— pytest 16 → 25（+ Det 3、NvM 5、no-config 1）



### Added — D2 半天压缩 5 天计划
- **M1 MemIf walking skeleton** — generator MemIf 完整端到端跑通（提前 D3 EOD 计划 2 天）
- **M2.1 / M2.2** MemIf_Cfg.h / MemIf_Cfg.c 与 V25.10 reference **byte-equal**
  （过滤时间戳 / 工具版本后），diff = 0
- **M2.3 / M2.4** 跨模块校验规则 `Rule_BSW_MemIf_TCPP_2170` 与 `_2171`
  在 BAD- 工程上正确触发
- **M2.5** docs §15 端到端补丁（自定义 `MemIfModuleVersion`
  schema → IDE → generator → C 输出）实战可重现
- **M2.7** 一键全栈回归脚本 `tools/test_memif_full.sh`（7 项检查全 PASS）
- **M4.1（提前）** PyInstaller 打包：macOS bswgen 9.4 MB / bswval 8.4 MB
- **基础库**（替代 V25.10 13 个 Cython `Common/*.pyd`）：
  - `core/Common/BswBase.py` — `getAttrValue` 含 reference 列表语义 + `'Ref'`
    后缀启发式
  - `core/Common/CodeGenerator.py` — Jinja2 渲染主循环 + CRLF 输出 +
    StrictUndefined
  - `core/Common/Public.py` — `getSwitchValue` / `getBooleanValue` /
    `getIntegerValue` / `getURIPath`
  - `core/Common/Context.py` — 含 `ModuleContextBase = Context` 别名
  - `core/Common/J2Filters.py` — Jinja 自定义 filter 注册
  - `core/Common/ArxmlValidator.py` + `base/{BaseClass,BaseDecorator}.py`
  - `core/Common/arxmlparse/loader.py` — ECUC ARXML 加载器（含
    `ECUC-NUMERICAL-PARAM-VALUE` / `ECUC-TEXTUAL-PARAM-VALUE` /
    `ECUC-REFERENCE-VALUE` 三态解析，`is_reference=True` flag 透传）
  - `core/Common/arxmlparse/constant/BswPathConstant.py` — 6870 项 BP enum
    全量从 V25.10 `.pyc` 用 xdis 自动抽取
  - `core/Common/arxmlparse/cache/BswModuleCache.py` — `getBswContainerByEnum`
  - `core/Common/templates/Template_Base.jinja` — V25.10 共享 jinja 基底
- **应用层**：
  - `generator/__main__.py` bswgen CLI
  - `validator/__main__.py` bswval CLI（带 `Bsw.<M>.<M>Register` 反射调用）
  - `generator/modules/{MemIf,Det,NvM,Ea}/`（V25.10 派生）
  - `validator/Bsw/MemIf/`（V25.10 派生 + docs §15 patch）
- **测试**（**16 / 16 PASS**）：
  - `core/tests/test_imports.py` — 7 项，Common.* 全部可 import + API surface
  - `generator/tests/test_memif_generation.py` — 6 项，含 MemIf 生成 +
    diff = 0 + §15 patch
  - `validator/tests/test_memif_validator.py` — 3 项，clean baseline +
    TCPP_2170 + TCPP_2171
- **工具链**：
  - `tools/test_memif_full.sh` — 7 项 M2.7 一键回归
  - `tools/reference_diff.py` — 通用 module-vs-V25.10 diff 检查器
  - `tools/build_all.sh` / `.cmd` — PyInstaller bswgen / bswval 打包
  - `tools/sync_to_smb.sh` — Mac → SMB 同步
  - `tools/daily_check.sh` — 每天 standup checker
- **PyInstaller spec**：`generator/bswgen.spec`、`validator/bswval.spec`
- **包配置**：`core/pyproject.toml`、`generator/pyproject.toml`、
  `validator/pyproject.toml`
- **文档**：
  - `docs/ARCHITECTURE.md` — 三层架构地图（Tier 1 IDE / Tier 2 apps /
    Tier 3 common-lib）+ 数据流 + 测试策略 + 兼容性约定
  - `docs/sprint-logs/D2.md` — D2 当日进度记录
  - `docs/v25_pyz_source_reference/` — V25.10 反编结果归档
  - `ide/README.md` — Eclipse RCP 后续实现指南
- **基础设施**：
  - `.github/workflows/test.yml` — pytest 矩阵 + MemIf 全栈回归 +
    PyInstaller smoke（Linux / macOS / Windows）
  - `NOTICE.md` — 法律边界声明（v0.1 / v0.2 研究 demo only）
  - `CONTRIBUTING.md` — 贡献者上手指南

### Fixed — D2 期间踩过的坑
- `ModuleNotFoundError: jinja2` — 标注依赖到 `pip install jinja2 lxml`
- `ImportError: ModuleContextBase` — `Common.Context` 加 `ModuleContextBase
  = Context` 别名
- `TemplateNotFound: Template_Base.jinja` — 把 V25.10 模板搬到
  `core/Common/templates/`，并加入 `FileSystemLoader` 搜索路径
- `UndefinedError: 'DefaultCustomer'` — `env.globals` 注入 V25.10 默认值
  (`DefaultCustomer='iSoft'`、`DefaultMcu='S32K148'`、`DefaultToolVersion`、
  `DefaultLicense`、`UserCodeDefinitions={}`)
- `'MemIf' object has no attribute 'checkFee'` — `_Container` 加
  `getSubContainer` 方法
- `BP.Det_DetGeneral` 等枚举缺失 — 用 `xdis` 从 V25.10
  `BswPathConstant.pyc` 抽出全量 6870 条
- `generateCode() takes 1 positional but 2 given` — 加 `*args, **kwargs`
  支持子类传 `incFileList`
- 行尾不一致（LF vs CRLF）— 输出强制转 CRLF 匹配 V25.10 Windows 风格
- validator 自带 broken `pyz_source` 撞名 core — 移到
  `docs/v25_pyz_source_reference/validator_Common`
- `NvMEcucPartitionRef` 无值 → `None` → 不可迭代 — `BswBase getAttrValue`
  对 `'Ref'` / `'Refs'` 后缀的 key 返 `[]`
- 120 条 `ECUC-REFERENCE-VALUE` 元素未解析 — `loader.py` 增加
  `<REFERENCE-VALUES>/<ECUC-REFERENCE-VALUE>` 解析

### Changed
- **策略调整：sprint 重排为 MemIf-first / Walking Skeleton 模式**
  - 原计划：M1 横向地基 → M2 三模块端到端 → M3 横向铺 30 模块
  - 新计划：M1 MemIf 单模块走通 → M2 MemIf 完美 → M3 复制到 5 核心 + 30 smoke
  - 理由：第一个模块端到端打透后，所有架构性问题 D3 EOD 暴露完毕；
    后续模块线性机械复制，风险前移降低
- M1 / M2 检查项重写：M1 仅要求 MemIf 实际用到的 5 个 native helper
  （剩余 8 个先 stub）；M2 才要求 13 个全实现

### Known
- **Det**：5 个文件中 4 个生成；`Det_Externals.c` 卡在 template 缺
  `EcucPartition` 全局变量（M3.1 stretch — 在 env.globals 加默认即可）
- **NvM**：Context init OK；模板渲染卡 `checkRTE` / `checkiRTE`
  （V25.10 BswBase 对 ref 返 wrapper 对象 `.ref_type_.shortName_`，我们
  返路径字符串。需要 `_Reference` 包装类，M3.1 stretch）
- **Ea**：`Ea.__init__` 迭代 `EaEepApi`（`None` 时崩）。需要默认 `[]`
  或修源（M3.1 stretch）
- 这些**不是架构问题** —— 架构（schema → loader → BswBase → @property →
  Jinja → CRLF 输出）已经经 MemIf 验证完整 work。剩下的是 module-specific
  的 V25.10 closed-source 行为还原细节。

### Notes
- 项目代号：**autosar_tool**
- 起源：基于 ORIENTAIS Configurator V25.10 的反编结果（详见
  `/Users/richard/AI-MiniWorkspace/project/autosar-cfg/`）作为种子工程
- 当前定位：研究 / 内部 demo（v0.1、v0.2 阶段）；商业化路径见
  `docs/PLAN.md` §9 / `NOTICE.md` v0.3 起

## [D1] — 2026-04-27

### Added
- 项目立项与方案设计：`README.md`、`PLAN.md`、`MILESTONES.md`
- v0.1 sprint 14 天计划与 4 个里程碑（M1-M4）
- v0.2 路线（UI 重设计 + 80 模块覆盖）合并进 `PLAN.md` §9
- `.gitignore` 覆盖 Python / Java / Eclipse / macOS / 大二进制制品

## 模板（供未来 release 使用）

> ## [vX.Y.Z] — YYYY-MM-DD
>
> ### Added
> ### Changed
> ### Fixed
> ### Removed

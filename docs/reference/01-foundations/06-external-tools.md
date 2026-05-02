# 07 · 外挂独立工具 (generator / upgrader / validator)

ORIENTAIS Configurator 除了主 IDE 之外, 在根目录下还附带了 **3 个独立可执行工具**,
都用 Python / C++ 打包成单文件 EXE, 可以被 IDE 内部调用, 也能在 CI/脚本里脱离 IDE 独立运行。

```
isoft_generator/   ← C 代码生成器 (37 MB)
isoft_upgrader/    ← 工程升级器 (23 MB)
isoft_validator/   ← 配置校验器 (14 MB)
```

和 IDE 内的 `cn.com.isoft.pal.cgenerator`、`cn.com.isoft.bswbuilder.validation` 等
bundle 的关系:**后者通过 JNI/Process 调用前者**, 复用同一份 Python 代码基于自动化,
避免 Java 和 Python 两端各写一套。

---

## 1. `isoft_generator/` — C 代码生成器

### 1.1 文件

| 文件 | 说明 |
|---|---|
| `ORIENTAISBswGen.exe` | PyInstaller 打包的单文件可执行, Windows x64 |
| `pack_info.txt` | 来源信息(Git 仓库 + 分支 + 提交) |

### 1.2 `pack_info.txt` 内容

```
仓库: git@gitlab.i-soft.com.cn:prd/cp_bsw_mirror_group/r23_bsw_03_GenerateScripts.git
分支: release_v2.2.x
提交: 1a2a75899237b81c613b74fb9876be1cb8b1fd39
```

关键信息:

- 源代码在 iSoft 内部 GitLab, 仓库属于 **CP BSW Mirror Group** 的 R23 BSW 子项
- 发布分支 `release_v2.2.x` — 对应 "EasyXMen V25.10 / BSW 2.2.x" 系列
- Git 提交哈希可以和后续发布做一致性核对

### 1.3 功能

接收已经配置好的 ECU 配置(`.arxml`), 按模块生成 C/H 源码:

- BSW 模块的 `Cfg.c/h` (模块静态配置)
- `Lcfg.c/h` (链接期配置, 若启用)
- `PBcfg.c/h` (post-build 配置)
- `Cbk.c` (回调桩)
- RTE 生成在独立 bundle, 此处不处理

### 1.4 调用方式

**IDE 内**: 菜单"生成 BSW 代码"→ `cn.com.isoft.pal.cgenerator` 启动此 exe 并传入工程路径。

**命令行**:

```cmd
isoft_generator\ORIENTAISBswGen.exe --project <工程路径> --module <模块名>
```

(具体参数以该 exe `--help` 为准, 不同版本可能略有出入)

---

## 2. `isoft_upgrader/` — 工程升级器

### 2.1 文件

| 文件 | 说明 |
|---|---|
| `ORIENTAISBswUpg.exe` | 单独的升级工具可执行 |

没有 `pack_info.txt`, 可能是因为升级器与 Configurator 主版本同步, 不走独立迭代。

### 2.2 功能

老版本 ORIENTAIS 工程(基于旧版 BSW 模块定义)迁移到当前版本时的自动化工具:

- 读取旧工程的 `.arxml` 文件
- 对照 `bswmd/` 下当前版本的定义, 识别已删除/改名/迁移的参数
- 按规则改写工程, 使其可被当前 Configurator 打开
- 生成升级报告(哪些参数被自动迁移 / 哪些需要人工修复)

### 2.3 调用方式

**IDE 内**: 打开旧工程时 IDE 检测到版本差, 弹窗询问是否升级 → 调用这个 exe。

**命令行**: 通常不直接使用, 除非做批量迁移。

---

## 3. `isoft_validator/` — 配置校验器

### 3.1 文件

| 文件 | 说明 |
|---|---|
| `ORIENTAISBswVal.exe` | 校验器可执行 |
| `pack_info.txt` | 来源信息 |
| `rules_Bsw/` | 46 个 **JSON 校验规则文件** |

### 3.2 `pack_info.txt` 内容

```
仓库: git@gitlab.i-soft.com.cn:toolchain/rte_tool/python_validator.git
分支: fixbug_v2.2.2
提交: 937a848e5d8aa27cbeaa2531c1fb59ca35e23ba4
```

- 源代码归 **Toolchain / RTE Tool** 组管理(与 generator 不同项目组)
- 分支 `fixbug_v2.2.2` 表明此构建是从该 tag 的一个 bugfix 分叉打出来

### 3.3 `rules_Bsw/` — JSON 规则清单

每个 BSW 模块一份 `<Module>Messages.json`, 46 个模块对应 46 个文件。样例:

```
BswMMessages.json          Basic Software Mode Manager
CanIfMessages.json         CAN Interface
CanTpMessages.json         CAN Transport Protocol
CanTSynMessages.json       CAN Time Sync
CDD_*Messages.json         Complex Device Driver (多个)
ComMessages.json / ComMMessages.json    通信与通信管理
DcmMessages.json / DemMessages.json     诊断
DoIPMessages.json / DltMessages.json   
EcuCMessages.json / EcuMMessages.json   
EthIfMessages.json / EthSwtMessages.json / EthTSynMessages.json 
FeeMessages.json / FimMessages.json    
IPduMMessages.json / LdComMessages.json 
LinIfMessages.json / LinSMMessages.json / LinTpMessages.json 
MemIfMessages.json / NmMessages.json / NvMMessages.json 
OsMessages.json / PduRMessages.json    
SDMessages.json / SecOCMessages.json   
SomeipTpMessages.json / StbMMessages.json 
TcpIPMessages.json / UdpNmMessages.json 
WdgIfMessages.json / WdgMMessages.json / XcpMessages.json 
XfrmMessages.json
```

每条 JSON 定义:
- 规则 ID
- 触发条件(哪个参数值范围 / 引用完整性 / 模块间一致性)
- 错误等级(ERROR / WARNING / INFO)
- 提示文本(中/英)
- 修复建议(可选)

### 3.4 调用方式

**IDE 内**: 右键工程→"Validate BSW Configuration"→ IDE 调用此 exe。

**命令行**(CI 集成推荐):

```cmd
isoft_validator\ORIENTAISBswVal.exe --project <工程路径> --rules rules_Bsw --format junit
```

返回非零退出码表示校验失败, 方便 CI/CD 流水线集成。

---

## 4. 三工具协作链路

典型流水线:

```
  ┌──────────────────┐
  │ 用户在 IDE 修改   │
  │ ECU 配置 (.arxml)│
  └────────┬─────────┘
           │ 触发 Validate
           ▼
  ┌──────────────────┐    rules_Bsw/*.json
  │ isoft_validator  │ ◄─ 规则库
  └────────┬─────────┘
           │ 通过
           ▼
  ┌──────────────────┐
  │ isoft_generator  │ → 生成 Cfg.c/h, Lcfg.c/h, PBcfg.c/h
  └────────┬─────────┘
           │
           ▼
      BSW 集成编译
           
  ┌──────────────────┐
  │ 旧版本工程迁入?  │ → isoft_upgrader 先升级
  └──────────────────┘
```

---

## 5. 与 IDE 内 plugin 的职责划分

| 阶段 | IDE 内 (plugins/) | 外挂工具 (本目录) |
|---|---|---|
| 编辑 ARXML | `cn.com.isoft.def.editor*`<br>`cn.com.isoft.bswbuilder.ui` | — |
| 校验 | `cn.com.isoft.mal.validation` 做框架层 | **`isoft_validator` 做实际规则匹配** |
| 生成 C 代码 | `cn.com.isoft.pal.cgenerator` 做框架层 | **`isoft_generator` 做实际模板渲染** |
| 版本升级 | 无 | **`isoft_upgrader` 独立完成** |

这种拆分让 IDE 和 CI 工具链都能用同一套核心逻辑, 避免 Java/Python 两端行为分歧。

---

## 6. CI 场景接入提示

做无 IDE 的自动化构建时, 只需要:

```
autosar-configurator/
├── jre/                     (如果工具依赖 Java 部分 — 通常不需要)
├── bswmd/                   (validator 和 generator 都会引用)
├── isoft_generator/
├── isoft_upgrader/
└── isoft_validator/
    └── rules_Bsw/
```

完整解包到 CI agent 即可; **不需要**安装 Configurator 主程序、不需要 dongle(若只做校验/生成且 license 允许)。

---

## 7. 排错速查

| 现象 | 可能原因 |
|---|---|
| generator.exe 启动直接退出 | 缺 VC Redistributable; 安装 Microsoft VC++ 2017/2019 x64 运行库 |
| validator 报规则文件找不到 | 命令行没传 `--rules rules_Bsw` 或工作目录不对 |
| upgrader 提示 "Source version unknown" | 老工程 `.arxml` 里没有 ARELEASE 版本号; 需手工补充后重试 |
| 和 IDE 结果不一致 | exe 版本与 IDE 里 plugin 版本不匹配(升级时有时只更新了一半, 对比 `pack_info.txt`) |

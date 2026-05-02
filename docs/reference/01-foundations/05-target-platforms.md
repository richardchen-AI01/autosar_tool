# 06 · 目标芯片 & OS 工程模板

ORIENTAIS Configurator V25.10 的"出厂支持"有两层:

1. **MCU 级**: 整包已经预置好 OS 参数、模板工程的芯片
2. **AUTOSAR 版本级**: 可选的 MCAL 模块定义(见 [04-metamodel-and-definitions.md](04-metamodel-and-definitions.md))

本章聚焦第一层 — 配套的芯片和随包附带的模板工程。

---

## 1. 出厂预置的 MCU

相关文件三处:

```
bswmd/<MCU名>/OsDef.arxml              OS 元模型
configuration/osinfo/<MCU名>.json      OS 运行参数(Core/内存/中断表 等)
configuration/os_projects/<MCU名>_set  预置工程模板
```

有 `.json` 或 `os_projects` 中之一存在, 就表示该芯片有官方模板。

### 1.1 MCU 清单

| MCU | 架构 | 厂商 | 有 bswmd | 有 osinfo | 有 os_projects |
|---|---|---|---|---|---|
| **S32K148** | ARM Cortex-M4F | NXP | ✅ OsDef.arxml | ✅ S32K148.json | ❌(示例在 workspace/ 里) |
| **TC397** | TriCore 1.6P × 3 核 | Infineon (AURIX 2G) | ✅ OsDef.arxml | ✅ TC397.json | ✅ **16 套模板**(TC397_set/) |
| **TC4D9** | TriCore 1.8 × 6 核 | Infineon (AURIX 3G) | ❌(用共享定义) | ❌ | ✅ 4 套模板(TC4D9_set/) |
| **U2A16** | RH850 V850Ex × 多核 | Renesas (U2A16) | ✅ OsDef.arxml | ✅ U2A16.json | ❌ |

> 产品品牌 bundle 名 `cn.com.isoft.bswbuilder.mcus.infineon` 以及 Infineon 独占 20 套
> 模板, 说明本次交付**主打 Infineon TriCore 平台**;
> NXP / Renesas 的支持能跑, 但配套没那么全。

### 1.2 `configuration/osinfo/*.json` 的作用

每个 JSON 文件列出对应 MCU 在 AUTOSAR OS 上的**具体运行参数**:

- Core 数量与标识
- 中断优先级层级
- 内存保护区域划分 (MPU / HSM 区域)
- Trap / Hook 处理点
- 默认堆栈尺寸
- 编译器/链接器约定

工程创建向导会用这个 JSON 作为"默认值"填入 OS 配置, 避免用户手动从头写。

### 1.3 `configuration/os_projects/` 的作用

**预置工程模板**, 按"芯片 + 安全等级 + Core 组合"命名, 新建工程向导里会直接引用。

#### TC397_set/(16 套 · 21 MB)

Infineon AURIX 2G 系列的 16 套模板, 按两个维度的笛卡尔积:

| 维度 1 · 安全等级 (Safety Class) | SC1 / SC2 / SC3 / SC4 |
|---|---|
| 维度 2 · Core 配置 | Core0 / Core5 / CrossCore / SingleCore |

命名规则 `TC397_Auto_SC<1-4>_<CoreConfig>`:

```
TC397_Auto_SC1_Core0       → 只在 Core0 运行, ISO 26262 ASIL-A 等级
TC397_Auto_SC1_Core5       → 只在 Core5 运行
TC397_Auto_SC1_CrossCore   → 多核分布
TC397_Auto_SC1_SingleCore  → 单核完整系统
TC397_Auto_SC2_*           → SC2 等级(ASIL-B)
TC397_Auto_SC3_*           → SC3 等级(ASIL-C/D 下限)
TC397_Auto_SC4_*           → SC4 等级(ASIL-D 高安全)
```

#### TC4D9_set/(4 套 · 5.1 MB)

Infineon AURIX **3G** 系列 TC4D9 的 4 套, 都带有 "Alarm"(告警)前缀, **只提供 CrossCore 配置**:

```
TC4D9_Alarm_Auto_SC1_CrossCore
TC4D9_Alarm_Auto_SC2_CrossCore
TC4D9_Alarm_Auto_SC3_CrossCore
TC4D9_Alarm_Auto_SC4_CrossCore
```

TC4D9 的支持看起来还处于推进中(仅 CrossCore 变体), 随后续版本扩充。

#### 模板内部结构

每个子目录约 500 KB ~ 2 MB, 含:

- `.arxml` 工程描述
- 预编译好的 EcuC 配置(与对应 OS/BSW 版本匹配)
- `Makefile` / `linker.ld` 片段(若需要)

---

## 2. `configuration/OsInfo.xlsx` — 速查表

~29 KB 的 Excel, 人类可读的"支持矩阵", 平铺:

- MCU × AUTOSAR 版本 × 支持的模块
- Core 约束
- 编译器推荐
- 安全等级可选项

是给销售/FAE 人员做对客户交付范围的讲解用的, 运行时不读。

---

## 3. 示例工程(不在 `configuration/` 里)

**不要忽略**: workspace 下带着两份官方示例工程:

```
workspace/
├── Demo_S32K148_V2510_S32DS_V3p5_Project/   NXP S32K148 基于 S32DS 3.5 的完整工程
├── s32k148_bsw/                              S32K148 配套 BSW 工程
└── 开源小满S32K148示例工程说明.pdf (1.7 MB)   对应手册
```

- Demo 工程面向 NXP 的 S32 Design Studio IDE 3.5
- "**开源小满**"是 iSoft 开源的 S32K148 MCAL 驱动套件(搭配 `S32K148/OsDef.arxml` 与 `S32K148.json`)
- 与 `TC397_set`、`TC4D9_set` 模板不同: 这里是**完整工程 + 工具链**, 可直接编译

---

## 4. 芯片/平台支持的扩展边界

**可以扩展**:

1. 添加新 MCU 支持: 
   - 在 `bswmd/` 下新建目录放 `OsDef.arxml`
   - 在 `configuration/osinfo/` 下添加 `<MCU>.json`
   - 在 `configuration/os_projects/` 下添加 `<MCU>_set` 模板(可选)
   - 更新品牌 bundle `plugin.xml` 的 MCU 扩展点列表

2. 增加 OS 配置变体:
   - 在现有 `<MCU>_set/` 下加新子目录(如 `TC397_Auto_SC5_CustomCore`)

**不便扩展**:

- 新增 AUTOSAR 版本(需要完整新 schema + MCAL 模块定义)
- 跨芯片架构复用(每款 MCU 的 OsDef 都需要人工适配)

---

## 5. 核对表

想知道"本包支持我的芯片吗?", 按下面步骤:

1. 打开 `configuration/OsInfo.xlsx` 快速看
2. 查 `configuration/osinfo/<MCU>.json` 是否存在
3. 查 `bswmd/<MCU>/OsDef.arxml` 是否存在
4. 查 `configuration/os_projects/<MCU>_set/` 有没有模板
5. 最终: 启动 ORIENTAIS, 在"新建工程向导"的 MCU 下拉列表里能选到才算官方支持

---

## 6. 排错速查

| 现象 | 可能原因 |
|---|---|
| 新建工程向导里没有你的 MCU | `osinfo/<MCU>.json` 缺失 或 品牌 bundle 里未声明 |
| 工程创建后 OS 配置全空 | `bswmd/<MCU>/OsDef.arxml` 缺失 |
| 模板工程打开报 "Missing ARXML" | `os_projects/<MCU>_set/` 路径错或版本与当前 bswmd 不匹配 |
| 安全等级选项灰色 | license 的 `ECUCFilter` 参数没覆盖该 SC 等级 |

# 05 · BSW 元模型 & 模块定义 (`bswmd/`)

`bswmd/` 目录(= **BSW Module Definition**)存放了 ORIENTAIS Configurator 用于
驱动配置编辑器、校验器、生成器的**ARXML 元模型**。没有这些定义文件, 配置编辑器
左侧的属性面板、右侧的校验提示、生成器的模板都无从依据。

---

## 1. 目录总览(~16 MB)

```
bswmd/
├── STD/                 AUTOSAR 标准类型(所有版本共享)  2 个文件
├── Common/              BSW 通用栈定义(与 AUTOSAR 版本无关)  58 个文件
├── AUTOSAR_4-2-2/       经典版本 4.2.2 对应的 MCAL 定义  15 个文件
├── AUTOSAR_00048/       AUTOSAR R20-11(schema 00048)的 MCAL 定义  17 个文件
├── AUTOSAR_00052/       AUTOSAR R23-11(schema 00052)的 MCAL 定义  17 个文件
├── S32K148/             NXP S32K148 专用 OS 定义  1 个
├── TC397/               Infineon TriCore TC397 专用 OS 定义  1 个
└── U2A16/               Renesas RH850 U2A 专用 OS 定义  1 个
```

---

## 2. 子目录详解

### 2.1 `STD/` — AUTOSAR 标准类型(2 项)

所有 AUTOSAR 版本/厂商/BSW 模块都引用的 "底座":

| 文件 | 说明 |
|---|---|
| `AUTOSAR_StdTypes.arxml` | 标准类型定义: `Std_ReturnType`, `Std_VersionInfoType` 等 |
| `SwAddrMethods.arxml` | 内存分段寻址方法(`_RAM`, `_ROM`, `_VAR_INIT`, `_CODE` …) |

### 2.2 `Common/` — BSW 通用栈(58 项)

与 MCAL 层相对, 这里是"芯片无关"的 BSW 服务层模块定义。涵盖完整的 AUTOSAR Classic 栈:

**通信栈**: `BswMDef`, `ComDef`, `ComMDef`, `CanIfDef`, `CanNmDef`, `CanSMDef`, `CanTPDef`,
`CanTrcvDef`, `CanTSynDef`, `EthIfDef`, `EthSMDef`, `EthSwtDef`, `EthTrcvDef`,
`EthTSynDef`, `DoIPDef`, `LdComDef`, `LinIfDef`, `LinSMDef`, `LinTPDef`, `NmDef`,
`PduRDef`, `SoAdDef`, `SomeIpTpDef`, `TcpIpDef`, `UdpNmDef`, `XfrmDef`

**诊断**: `DcmDef`, `DemDef`, `DetDef`, `DltDef`, `FimDef`, `XcpDef`

**存储**: `EaDef`, `Eep_62Def`, `Fee_62Def`, `FlsDef`(与 MCAL 版本的 Fls 区分), 
`MemIfDef`, `MemMapDef`, `NvMDef`

**服务**: `BswMDef`, `EcuCDef`, `EcuMDef`, `ComMDef`, `KeyMDef`, `StbMDef`, 
`SdDef`(Service Discovery)

**安全**: `CrcDef`, `CryIfDef`, `CryptoDef`, `Crypto_ISoft.arxml`(iSoft 扩展), 
`CsmDef`, `SecOcDef`

**看门狗**: `WdgDef`(通用), `WdgIfDef`, `WdgMDef`

**其他**: `TmDef`, `CantSynDef`, `MemProtectDef`(若存在), `…`

**`<vendor>_ISoft.arxml`** 结尾的文件(如 `Crypto_ISoft.arxml`, `EthTrcv_ISoft.arxml`)是
**iSoft 基于标准定义追加的厂商扩展参数** — 兼容 AUTOSAR 标准同时暴露 ORIENTAIS 特有配置项。

### 2.3 AUTOSAR 版本目录 — MCAL 层

AUTOSAR 把协议/接口定义放在`*Def.arxml`, 版本以 **schema 编号**区分:

| 目录 | AUTOSAR 版本 | 对应 SCHEMA | 典型命名 | 文件数 |
|---|---|---|---|---|
| `AUTOSAR_4-2-2` | Classic 4.2.2 | (无编号) | `Can422Def.arxml`, `Adc422Def.arxml`, ... | 15 |
| `AUTOSAR_00048` | R20-11 | 00048 | `CanDef.arxml`, `AdcDef.arxml`, `FlsDef.arxml`, ... | 17 |
| `AUTOSAR_00052` | R23-11 | 00052 | `Can23Def.arxml`, `AdcR23Def.arxml`, `FlsR23Def.arxml`, ... | 17 |

每个目录列出的都是 **MCAL(Microcontroller Abstraction Layer)** 驱动模块定义:

`Adc`, `Can`, `Dio`, `Eep`, `Eth`, `EthTrcv`, `Fee`, `Fls`, `Fr`(4-2-2/00048 有), 
`Gpt`, `Icu`, `Lin`(低层), `Mcu`, `Port`, `Pwm`, `Spi`, `Wdg`

> **本交付产品的 `aboutText` 声称 "Autosar Version: R19-11"**, 但 `bswmd/` 同时
> 提供了 4.2.2 / R20-11 / R23-11 三套定义, 说明**实际配置时可按工程需要选择版本**,
> R19-11 只是主打合规标签。

### 2.4 MCU 专用目录 — OS 定义

每个目录只有 **1 个文件 `OsDef.arxml`**, 定义该芯片对应的 OSEK/AUTOSAR OS
配置参数(中断优先级表、Core 数、内存保护区域、Trap 处理等):

| 目录 | 目标 MCU | 架构 | 厂商 |
|---|---|---|---|
| `S32K148` | NXP S32K148 | ARM Cortex-M4 | NXP |
| `TC397` | Infineon AURIX TC397 | TriCore (3 核) | Infineon |
| `U2A16` | Renesas RH850/U2A16 | RH850 V850Ex | Renesas |

这 3 款芯片和 `configuration/osinfo/*.json`、`configuration/os_projects/` 共同构成
本产品"出厂支持"的硬件平台, 详见 [05-target-platforms.md](05-target-platforms.md)。

---

## 3. 文件形式(ARXML)

`bswmd/` 下所有文件都是 **ARXML**(AUTOSAR XML), 基于 AUTOSAR 发布的 XSD schema。
一个 `*Def.arxml` 的典型结构:

```xml
<AUTOSAR xmlns="http://autosar.org/schema/r4.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="...">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>AUTOSAR_Dcm</SHORT-NAME>
      <ELEMENTS>
        <BSW-MODULE-DEF>
          <SHORT-NAME>Dcm</SHORT-NAME>
          <PARAMETERS>…</PARAMETERS>
          <REFERENCES>…</REFERENCES>
          <SUB-CONTAINERS>…</SUB-CONTAINERS>
        </BSW-MODULE-DEF>
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
```

ORIENTAIS 的配置编辑器(`cn.com.isoft.def.editor*`)使用 Sphinx+EMF 把这些 `*Def` 加载
为模型, 然后驱动左侧树/右侧属性面板, 并在保存时按同一元模型生成 `EcuC`。

---

## 4. 加载与消费链路

```
bswmd/<version>/<Module>Def.arxml        ARXML 元模型(本目录)
         │
         ▼
cn.com.isoft.mal.model(.modelutils)      EMF 模型加载 + 工具(明文, 非加密)
         │
         ▼
cn.com.isoft.def.editor                  定义编辑器(Eclipse 编辑器扩展点)
         │
         ├───► cn.com.isoft.bswbuilder.ui              配置编辑器(加密)
         │          (左右分屏的模块参数视图)
         │
         ├───► cn.com.isoft.bswbuilder.validation      校验器(加密)
         │
         ├───► cn.com.isoft.bswbuilder.modules.<X>     每个模块的专用规则(加密)
         │
         └───► cn.com.isoft.rtebuilder.generator       RTE 代码生成(加密)
```

---

## 5. 版本选择与组合规则

工程创建时会选定一条 AUTOSAR 路径, 决定从哪个版本目录取 MCAL 定义, 并与 `Common/`
的通用栈共用。典型组合:

| 工程类型 | MCAL 目录 | Common 目录 | MCU OS 目录 |
|---|---|---|---|
| AUTOSAR 经典 4.2.2 工程 | `AUTOSAR_4-2-2/` | `Common/` | 按芯片选一个 |
| R20-11 工程 | `AUTOSAR_00048/` | `Common/` | 按芯片选一个 |
| R23-11 工程 | `AUTOSAR_00052/` | `Common/` | 按芯片选一个 |

在一个工程里**同时混用**两套 MCAL 的情况不支持, 因为 AR-PACKAGE 路径会冲突。

---

## 6. 能做什么 / 不能做什么

**能做**:

- 为新模块追加厂商扩展参数 → 新建 `<Module>_<Vendor>.arxml`, 引用官方 `<Module>Def`
- 新增 MCU 支持 → 新建 `bswmd/<MCU名>/OsDef.arxml`, 同时给 `configuration/osinfo/<MCU名>.json` 补对应条目
- 升级 AUTOSAR 版本 → 从官方拿新 schema 的 `*Def.arxml`, 放到新目录(如 `AUTOSAR_00053`)

**不能做**:

- 删除 `STD/` 下任何文件 — 整个元模型的根会坏
- 修改 `Common/` 下官方模块的 `SHORT-NAME` 或 UUID — 工程 ECU 配置会失去引用完整性
- 手工改生成的 `ECUC-VALUE-COLLECTION`(属于客户工程输出, 不在这里)

---

## 7. 排错速查

| 现象 | 原因 |
|---|---|
| 打开配置编辑器时空白, 不显示参数 | `*Def.arxml` 文件损坏或未被识别 → 用 XML 解析器校验 |
| 提示 `Could not find BSW-MODULE-DEF /AUTOSAR/xxx/xxx` | 依赖的 Module Def 缺失 → 对比 Common/ 与版本目录 |
| 保存工程后丢失参数 | 编辑器版本与 `*Def` 版本不匹配 → 产品自带版本用自带定义, 禁混用 |
| OS 参数不支持当前芯片 | `bswmd/<MCU>/OsDef.arxml` 没有配套 → 需先补充, 再重启 |

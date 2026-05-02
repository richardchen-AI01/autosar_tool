# ORIENTAIS Configurator for EasyXMen V25.10 — 工程目录总览

本文档对 `smb://192.168.1.83/ORIENTAIS_Studio/ORIENTAIS_Configurator_for_EasyXMen_V25.10`
整个安装目录做结构化梳理, 帮助使用者快速理解每个文件/目录的用途、相互关系, 以及在什么场景下会被用到。

---

## 1. 产品一句话

**ORIENTAIS Configurator** 是 **iSoft(上海东软睿驰)** 发布的 AUTOSAR BSW/RTE 配置工具,
基于 **Eclipse RCP** 打包, 集成 **ARTOP**(AUTOSAR Tool Platform)、**Sphinx**、**EMF/GMF**
模型框架, 交付时捆绑 Java 8 JRE、硬件锁授权运行时与自研代码保护机制。

| 项目 | 值 |
|---|---|
| 产品全名 | ORIENTAIS Configurator for EasyXMen V25.10 |
| 版本号 | 2.0.5.202601300910 (主 bundle) |
| AUTOSAR 标准 | R19-11 (兼容定义可选 R20-11 / R23-11 / 4-2-2) |
| 构建时间 | 2026-01-30 17:12:43 CST |
| Build JDK | Oracle Java 1.8.0_221 (x64) |
| 构建工具 | Apache Maven 3.8.6 |
| 目标客户 | PuHua Company (交付编号 PHBSW2510) |
| 授权邮箱 | support@i-soft.com.cn |
| 产品官网 | http://www.i-soft.com.cn/ |
| 运行平台 | 仅 Windows x64 |
| 授权机制 | **BitAnswer（比特安索）软锁激活码** + `PuHuaLicense.lic`（AES 签名 XML）|

---

## 2. 顶层目录/文件一览

```
ORIENTAIS_Configurator_for_EasyXMen_V25.10/
├── ORIENTAIS_Configurator_for_EasyXMen_V25.10.exe   ← Eclipse 原生启动器
├── ORIENTAIS_Configurator_for_EasyXMen_V25.10.ini   ← JVM 启动参数
├── ISOFT.cmd                                        ← 命令行入口
├── 00018990_00000004.dll        \
├── 00018990_00000004_x64.dll     ⟩ BitAnswer 比特安索授权 SDK 运行时
├── patch.xml                     ← 本交付包含的 ISOFT plugin 清单(80+ 条)
├── artifacts.xml                 ← p2 制品清单
├── unins000.exe / unins000.dat   ← Inno Setup 卸载程序
├── jre/                          ← 内嵌 Java 8u221 (~216 MB)
├── plugins/                      ← OSGi bundle 仓库 (396 个 jar, ~269 MB)
├── features/                     ← Eclipse 特性描述 (5 个)
├── configuration/                ← 运行期配置 + OSGi bundle 缓存 (~109 MB)
│   ├── config.ini                   指向产品 ID / splash / p2 数据区
│   ├── PuHuaLicense.lic             XML license(客户/功能授权)
│   ├── OsInfo.xlsx                  支持 OS/MCU 清单
│   ├── osinfo/*.json                S32K148 / TC397 / U2A16 的 OS 参数
│   ├── os_projects/                 预置 OS 工程模板 (TC397 16 套 + TC4D9 4 套)
│   └── org.eclipse.osgi/            Equinox bundle 解压缓存 (~81 MB)
├── bswmd/                        ← BSW Module Definition(ARXML 元模型)
│   ├── Common/                      通用 BSW stack 定义 (58 个模块)
│   ├── STD/                         AUTOSAR_StdTypes / SwAddrMethods
│   ├── AUTOSAR_00048/               R20-11 版本 MCAL 定义 (17 模块)
│   ├── AUTOSAR_00052/               R23-11 版本 MCAL 定义 (17 模块)
│   ├── AUTOSAR_4-2-2/               经典 4.2.2 版本 MCAL 定义 (15 模块)
│   ├── S32K148/                     NXP 芯片 OS 定义
│   ├── TC397/                       Infineon TriCore OS 定义
│   └── U2A16/                       Renesas RH850 OS 定义
├── isoft_generator/              ← 外部 C 代码生成器 (37 MB)
├── isoft_upgrader/               ← 外部工程升级器 (23 MB)
├── isoft_validator/              ← 外部配置校验器 (14 MB, 含 JSON 规则)
├── p2/                           ← Eclipse p2 provisioning 状态
├── usermanual/                   ← 产品 PDF 用户手册 (8.5 MB)
└── workspace/                    ← 默认工作空间 + 示例工程 (~78 MB)
```

---

## 3. 文档导航

| # | 主题 | 文档 |
|---|---|---|
**第一部分：产品结构概览** — `01-foundations/`
| # | 主题 | 文档 |
|---|---|---|
| 01 | 产品身份 & 品牌资产 | [01-product-identity.md](01-foundations/01-product-identity.md) |
| 02 | 启动器 & 运行时(exe / ini / cmd / JRE / config.ini) | [02-runtime-and-launcher.md](01-foundations/02-runtime-and-launcher.md) |
| 03 | Plugin / Feature / p2 架构 | [03-plugins-and-features.md](01-foundations/03-plugins-and-features.md) |
| 04 | BSW 元模型定义 (`bswmd/`) | [04-metamodel-and-definitions.md](01-foundations/04-metamodel-and-definitions.md) |
| 05 | 目标芯片 & OS 工程模板 | [05-target-platforms.md](01-foundations/05-target-platforms.md) |
| 06 | 外挂独立工具(generator/upgrader/validator) | [06-external-tools.md](01-foundations/06-external-tools.md) |
| 07 | 运行期状态目录(workspace / configuration / p2) | [07-runtime-state-dirs.md](01-foundations/07-runtime-state-dirs.md) |

**第二部分：Java 架构深入** — `02-architecture/`
| # | 主题 | 文档 |
|---|---|---|
| 01 | `mal` / `pal` 核心架构（扩展点、模块注册） | [01-mal-pal-architecture.md](02-architecture/01-mal-pal-architecture.md) |
| 02 | 授权 & 代码保护总览（两道强制门 + 三层辅助） | [02-licensing-and-protection.md](02-architecture/02-licensing-and-protection.md) |
| 03 | Artop 技术分析（数据驱动的依赖闭包与最小子集） | [03-artop-analysis.md](02-architecture/03-artop-analysis.md) |

**第三部分：授权与保护机制深度拆解** — `03-security-research/`
| # | 主题 | 文档 |
|---|---|---|
| 01 | "三把锁" 通俗心智模型（小白友好版） | [01-three-locks-walkthrough.md](03-security-research/01-three-locks-walkthrough.md) |
| 02 | 水分 1：`isdoggle()` 彩蛋 + 字符开关 | [02-isdoggle-easter-egg.md](03-security-research/02-isdoggle-easter-egg.md) |
| 03 | 水分 2：硬编码 DRM 密钥泄漏 | [03-hardcoded-keys-leak.md](03-security-research/03-hardcoded-keys-leak.md) |
| 04 | **结案报告：每次要重输授权码的根因**（RCA） | [04-pes-session-key-rca.md](03-security-research/04-pes-session-key-rca.md) |
| 05 | 安全漏洞披露报告（6 项 V-1~V-6） | [05-vulnerability-disclosure-report.md](03-security-research/05-vulnerability-disclosure-report.md) |

**第四部分：动手指南（Recipes）** — `04-recipes/`
| # | 主题 | 文档 |
|---|---|---|
| 01 | 端到端给一个 BSW 模块加新 ECUC 参数 | [01-add-new-param-end-to-end.md](04-recipes/01-add-new-param-end-to-end.md) |

**附录**
| # | 主题 | 文档 |
|---|---|---|
| 99 | 本次诊断会话产生的临时文件 | [99-session-artifacts.md](99-session-artifacts.md) |
| — | 本次整改变更记录 | [CHANGELOG.md](CHANGELOG.md) |

---

## 4. 文件/目录分类视图

按 **存在目的** 重新分组, 与上面的物理布局视图互补:

| 类别 | 成员 |
|---|---|
| **可执行入口** | `ORIENTAIS_Configurator_*.exe`、`ISOFT.cmd`、`unins000.exe` |
| **JVM/OSGi 配置** | `*.ini`、`configuration/config.ini`、`configuration/org.eclipse.equinox.simpleconfigurator/bundles.info` |
| **品牌资源** | `plugins/cn.com.isoft.bswbuilder.mcus.infineon_*.jar` 内的 splash/icons/plugin.xml |
| **授权** | `configuration/PuHuaLicense.lic`、`00018990_*.dll`、`plugins/cn.com.isoft.pal.doggle_*.jar` |
| **代码保护** | `jre/bin/decrypt.dll`(JVMTI agent)+ 108 个加密 plugin jar(共 4809 个 class) |
| **业务代码** | `plugins/cn.com.isoft.*`(121 个 bundle, 4 组: pal/mal/bswbuilder/rtebuilder) |
| **第三方 OSGi** | `plugins/org.eclipse.*`(~240 个)、`plugins/org.artop.*`(22 个)、`plugins/org.apache.*`(~16 个) |
| **元模型** | `bswmd/`(按 AUTOSAR 版本 + MCU 划分的 ARXML 定义) |
| **目标平台** | `configuration/osinfo/*.json`、`configuration/os_projects/` |
| **外部工具** | `isoft_generator/`、`isoft_upgrader/`、`isoft_validator/` |
| **用户文档** | `usermanual/ORIENTAIS_Configurator_User_Manual_*.pdf` |
| **运行期数据**(可删) | `workspace/.metadata/`、`configuration/org.eclipse.osgi/`、`p2/` |
| **卸载器** | `unins000.exe`、`unins000.dat` |

---

## 5. 使用建议

1. **要理解启动过程** → 先读 02
2. **要追授权或买单范围** → 读 03
3. **要扩展功能或插入自写 plugin** → 读 04
4. **要新增芯片/OS 支持** → 读 05 + 06
5. **要做自动化/CI 集成** → 读 07(外部工具支持脚本化调用)
6. **要清理磁盘/重置环境** → 读 08

---

## 6. 本文档版本

- 生成时间: 2026-04-23
- 基于构建: 2026-01-30 17:12:43 CST 的 V25.10 交付
- 分析路径: `smb://192.168.1.83/ORIENTAIS_Studio/ORIENTAIS_Configurator_for_EasyXMen_V25.10`

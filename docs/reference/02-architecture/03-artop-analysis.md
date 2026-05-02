# Artop 技术分析报告

> **分析对象**：ORIENTAIS_Configurator_for_EasyXMen_V25.10
> **分析时间**：2026-04-28
> **用途**：自研 AUTOSAR Classic BSW 配置工具的技术选型与开发参考
> **数据来源**：参考工具 `plugins/`、`configuration/bundles.info`、14 个 iSoft 插件 MANIFEST 抽样

---

## 1. 定位

**Artop（AUTOSAR Tool Platform）= AUTOSAR ARXML 的 EMF 元模型实现 + 工作区集成。**

它向上提供 ~3000 个 AUTOSAR 标准元素的 Java 类，向下基于 Eclipse EMF/Sphinx，使工具开发者无需实现 ARXML schema 解析、跨文件引用解析、ARXML 序列化即可操作 AUTOSAR 模型。

---

## 2. 在 ORIENTAIS 架构中的位置

```
┌─────────────────────────────────────────────────────────┐
│ iSoft UI 层（cn.com.isoft.bswbuilder.ui）                │
├─────────────────────────────────────────────────────────┤
│ iSoft 业务层（cn.com.isoft.bswbuilder.modules.* + mal）  │
│   每个 BSW 模块 1 个 Bundle,通过扩展点                   │
│   cn.com.isoft.bswbuilder.extensionpoints.module 接入    │
├─────────────────────────────────────────────────────────┤
│ ★ Artop 层（org.artop.aal.* / org.artop.ecuc.*）★       │
│   - 元模型 Java 类（autosar40.* / gautosar.*）            │
│   - ARXML 序列化与反序列化                                │
│   - 跨文件引用解析（DEFINITION-REF / *-REF）              │
│   - 工作区集成（autosarnature）                           │
├─────────────────────────────────────────────────────────┤
│ Eclipse Sphinx + EMF（org.eclipse.sphinx.* / emf.*）    │
├─────────────────────────────────────────────────────────┤
│ Eclipse Platform / Equinox OSGi                          │
└─────────────────────────────────────────────────────────┘
```

iSoft 业务代码 100% 通过 Artop 提供的强类型 API 访问 ARXML 数据，不直接接触 XML。

---

## 3. Bundle 清单（数据驱动）

### 3.1 多层口径

| 口径 | 数据源 | 数量 | 含义 |
|---|---|---|---|
| 文件系统 | `plugins/org.artop.*.jar` | **28** | 安装包打包数量 |
| OSGi 注册 | `configuration/.../bundles.info` | **28** | 启动注册到 runtime |
| iSoft 直接依赖 | iSoft jar 的 `Require-Bundle`（14 jar 抽样） | **12** | 显式声明的 |
| 传递闭包 | 12 个种子在 Artop 间做依赖闭包 | **20** | 真正会被加载 |
| 未使用 | 28 − 20 | **8** | 打包但未启用 |

### 3.2 真实使用的 20 个 Bundle（按职责分组）

| 类别 | Bundle | 大小 | 必备性 |
|---|---|---|---|
| **核心元模型** | `org.artop.aal.autosar448` | 26 MB | ★★★ |
| | `org.artop.aal.gautosar` | 846 KB | ★★★ |
| | `org.artop.eel.common` | 11 KB | ★★★ |
| | `org.artop.aal.common` | 92 KB | ★★★ |
| **序列化** | `org.artop.aal.serialization` | 78 KB | ★★★ |
| | `org.artop.eel.serialization` | 15 KB | ★★★ |
| **服务（高级 API）** | `org.artop.aal.gautosar.services` | 773 KB | ★★ |
| | `org.artop.aal.autosar448.services` | 65 KB | ★★ |
| **EMF.edit（label/icon）** | `org.artop.aal.autosar448.edit` | 7.6 MB | ★★（UI 阶段需要） |
| | `org.artop.aal.gautosar.edit` | 92 KB | ★★ |
| **校验** | `org.artop.aal.validation` | 25 KB | ★★ |
| **工作区** | `org.artop.aal.workspace` | 45 KB | ★★（实现 autosarnature） |
| | `org.artop.aal.workspace.ui` | 65 KB | ★ |
| **扩展机制** | `org.artop.aal.extender` | 25 KB | ★（mal 用） |
| **ECUC 初始化** | `org.artop.ecuc.gautosar.initializers` | 22 KB | ★★ |
| **AUTOSAR 4.0 兼容**（可选） | `org.artop.aal.autosar40` | 26 MB | 仅兼容老工程 |
| | `org.artop.aal.autosar40.services` | 190 KB | 仅兼容 |
| | `org.artop.aal.autosar40.services.common` | 3 KB | 仅兼容 |
| | `org.artop.aal.autosar40.validation` | 9 KB | 仅兼容 |
| | `org.artop.ecuc.autosar40.initializers` | 10 KB | 仅兼容 |

### 3.3 未使用的 8 个 Bundle（可剔除）

| Bundle | 原因 |
|---|---|
| `org.artop.aal.autosar40.converters` | 4.0/4.4 模型转换，iSoft 未启用 |
| `org.artop.aal.converters` | 通用转换器 |
| `org.artop.aal.autosar40.validation.ui` | 校验 UI 增强 |
| `org.artop.aal.validation.ui` | 校验 UI 增强 |
| `org.artop.aal.examples.common.ui` | Artop 官方示例 |
| `org.artop.aal.examples.editor` | Artop 官方示例 |
| `org.artop.ecuc.autosar40.xtend.typesystem` | Xtend 模板代码生成（iSoft 用独立 EXE） |
| `org.artop.ecuc.gautosar.xtend.typesystem` | Xtend 模板代码生成 |

### 3.4 抽样误差说明

- iSoft 共 ~123 个插件，本次抽样 14 个（≈11%）
- 抽样覆盖：核心层 8 个（mal/pal/bswbuilder.common/ui/extensionpoints/parallelmodelmanager/def.editor/rtebuilder.generator）+ 模块层 4 个（memif/com/dem/os_tc397）+ 其他 2 个
- **置信度**：核心层全覆盖，结论中"20 个使用"可信；"8 个未使用"中的 Xtend 类可能被 dcm/dem 等大模块隐式使用，需做完整扫描确认

---

## 4. 核心 API 速查

### 4.1 关键 Java 包

| 包 | 内容 | 所在 Bundle |
|---|---|---|
| `autosar40.autosartoplevelstructure` | `AUTOSAR` 根类 | autosar448 |
| `autosar40.genericstructure.generaltemplateclasses.arpackage` | `ARPackage` | autosar448 |
| `autosar40.ecucdescription` | ECUC 配置实例（Values 层） | autosar448 |
| `autosar40.ecucparameterdef` | ECUC 模块定义（Def 层） | autosar448 |
| `autosar40.bswmodule` | BSW Module Description | autosar448 |
| `autosar40.swcomponent` | SWC 模型（RTE 用） | autosar448 |
| `autosar40.system` | System Description | autosar448 |
| `gautosar.*` | 跨版本通用抽象 | gautosar |

### 4.2 ECUC 三层映射对照

| ARXML 元素 | Java 类（all in `autosar40.ecucdescription`） | 角色 |
|---|---|---|
| `<ECUC-VALUE-COLLECTION>` | `EcucValueCollection` | 顶层聚合（ecuconfig.arxml） |
| `<ECUC-MODULE-CONFIGURATION-VALUES>` | `EcucModuleConfigurationValues` | 一个 BSW 模块的配置 |
| `<ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL>` | `EcucModuleConfigurationValuesRefConditional` | 模块引用 |
| `<ECUC-CONTAINER-VALUE>` | `EcucContainerValue` | 容器（可嵌套） |
| `<ECUC-NUMERICAL-PARAM-VALUE>` | `EcucNumericalParamValue` | 数值/布尔参数 |
| `<ECUC-TEXTUAL-PARAM-VALUE>` | `EcucTextualParamValue` | 字符串/枚举参数 |
| `<ECUC-REFERENCE-VALUE>` | `EcucReferenceValue` | 跨容器引用 |
| `<ECUC-INSTANCE-REFERENCE-VALUE>` | `EcucInstanceReferenceValue` | 实例引用 |

| ARXML 元素 | Java 类（all in `autosar40.ecucparameterdef`） | 角色 |
|---|---|---|
| `<ECUC-MODULE-DEF>` | `EcucModuleDef` | 模块定义（schema） |
| `<ECUC-PARAM-CONF-CONTAINER-DEF>` | `EcucParamConfContainerDef` | 容器定义 |
| `<ECUC-INTEGER-PARAM-DEF>` | `EcucIntegerParamDef` | 整数参数定义（min/max/default） |
| `<ECUC-BOOLEAN-PARAM-DEF>` | `EcucBooleanParamDef` | 布尔参数定义 |
| `<ECUC-STRING-PARAM-DEF>` | `EcucStringParamDef` | 字符串参数定义 |
| `<ECUC-ENUMERATION-PARAM-DEF>` | `EcucEnumerationParamDef` | 枚举参数定义 |
| `<ECUC-FLOAT-PARAM-DEF>` | `EcucFloatParamDef` | 浮点参数定义 |
| `<ECUC-REFERENCE-DEF>` | `EcucReferenceDef` | 引用参数定义 |

### 4.3 标准代码模式

```java
// 1. 加载（Sphinx 工作区会自动加载工程内所有 .arxml；脱离工作区则手工加载）
ResourceSet rs = new ResourceSetImpl();
Resource defRes = rs.getResource(URI.createFileURI("MemIfDef.arxml"), true);
Resource cfgRes = rs.getResource(URI.createFileURI("MemIf.arxml"), true);

// 2. 取根
AUTOSAR root = (AUTOSAR) cfgRes.getContents().get(0);

// 3. 强类型遍历
for (ARPackage pkg : root.getArPackages()) {
    for (Object e : pkg.getElements()) {
        if (e instanceof EcucModuleConfigurationValues) {
            EcucModuleConfigurationValues mod = (EcucModuleConfigurationValues) e;
            EcucModuleDef def = mod.getDefinition();           // 跨文件引用自动解析
            for (EcucContainerValue c : mod.getContainers()) {
                for (EcucParameterValue p : c.getParameterValues()) {
                    if (p instanceof EcucNumericalParamValue) {
                        EcucNumericalParamValue np = (EcucNumericalParamValue) p;
                        EcucParameterDef pd = np.getDefinition();
                        // 从 def 拿 min/max/default 等约束
                    }
                }
            }
        }
    }
}

// 4. 修改 + 保存（自动序列化为合规 ARXML）
np.setValue("3");
cfgRes.save(null);
```

---

## 5. 集成方式

### 5.1 OSGi Bundle 接入

每个使用 Artop 的插件在 `MANIFEST.MF` 声明：

```
Require-Bundle:
    org.artop.aal.autosar448,
    org.artop.aal.gautosar,
    org.artop.aal.workspace,
    org.eclipse.sphinx.emf,
    org.eclipse.emf.ecore
```

### 5.2 Eclipse 工程标记

参考工程 `.project`：

```xml
<natures>
    <nature>org.artop.aal.workspace.autosarnature</nature>
</natures>
```

Artop 的 `org.artop.aal.workspace` Bundle 实现该 nature，激活后：
- 自动扫描工程内 `.arxml` 文件
- 加入 Sphinx 工作区模型集合
- 维护跨文件引用的反向索引

### 5.3 EMF EPackage 注册

`org.artop.aal.autosar448` 的 `plugin.xml` 通过 `org.eclipse.emf.ecore.generated_package` 扩展点注册 ~50 个 EPackage（每个对应一个 ARXML 命名空间分支），使 EMF Resource Factory 能识别 `http://autosar.org/schema/r4.0` 命名空间并实例化对应类。

### 5.4 扩展能力

iSoft 通过 `org.artop.aal.extender` 提供的扩展机制注入自有功能（参见 `cn.com.isoft.mal_*.jar` 的 Require-Bundle）。该 Bundle 提供编辑器扩展、命令、属性等钩子点，使 iSoft 能复用 Artop UI 框架而不修改其代码。

---

## 6. 自研工具的依赖建议

### 6.1 阶段化清单

| 阶段 | 推荐 Bundle | 数量 |
|---|---|---|
| **P0 验证模型加载** | autosar448, gautosar, common, eel.common, serialization, eel.serialization | **6** |
| **P1 加上工作区集成** | + workspace, gautosar.services, autosar448.services | **9** |
| **P2 加上 UI（label/edit）** | + autosar448.edit, gautosar.edit, workspace.ui | **12** |
| **P3 加上校验** | + validation, ecuc.gautosar.initializers, extender | **15** |
| **完整复刻 ORIENTAIS 能力** | + 4.0 兼容（5 个 autosar40.* / ecuc.autosar40.*） | **20** |

新工具若仅需支持 AUTOSAR R22-11 (4.4.8) 及以上，可永久略过 4.0 兼容那 5 个，**最小完整集 = 15**。

### 6.2 必备的 Eclipse/EMF/Sphinx 依赖（非 Artop，但 Artop 跑不起来时缺它们）

```
org.eclipse.emf.ecore                   EMF 核心
org.eclipse.emf.ecore.xmi               XMI 序列化（ARXML 是 XMI 变种）
org.eclipse.emf.common                  EMF 工具
org.eclipse.emf.edit                    EMF 编辑（UI 阶段）
org.eclipse.sphinx.emf                  Sphinx 模型管理
org.eclipse.sphinx.emf.workspace        Sphinx 工作区
org.eclipse.sphinx.platform             Sphinx 平台
org.eclipse.core.runtime                OSGi runtime
org.eclipse.core.resources              Eclipse 工作区
org.eclipse.equinox.common              Equinox
```

---

## 7. 关键技术约束与风险

| 项 | 说明 |
|---|---|
| **运行时形态** | Artop 强依赖 OSGi 启动机制（Bundle Activator + EPackage 注册），**不能在普通 Java main 里直接跑**。开发期通过 Eclipse PDE 的 "Run As → Eclipse Application" 启动；命令行场景需用 Equinox launcher（headless）模式 |
| **Java 版本** | Bundle 声明 `Bundle-RequiredExecutionEnvironment: JavaSE-1.6`/`1.7`，但实际可在 JDK 8/11/17 上运行（参考工具用 `jre/bin/javaw.exe` 内嵌 JRE 1.8） |
| **AUTOSAR 版本绑定** | `autosar448` 对应 AUTOSAR R22-11；R23-11 需要更新版本的 Artop（参考工具内置 4.13.1 已支持） |
| **法律使用** | Artop 受 ASLR (Artop Software License based on AUTOSAR Released material) 约束，理论上需要 AUTOSAR 成员资格才能合法分发；**自用/原型阶段不受限**，商业发布需公司具备 AUTOSAR Partner 身份 |
| **扩展性** | Artop 元模型为代码生成产物（`.genmodel`），不可在运行时扩展；私有元数据通过 ARXML 标准的 `ADMIN-DATA/SDGS/SDG` 携带（iSoft 用 `iSoft::EcuOptions`、`iSoft::ModuleOptions` 等 GID） |
| **性能** | 大型工程（>100MB ARXML）首次加载耗时较长（Sphinx 反向索引构建）；参考工程 `catch.xml`(4 MB) 即缓存产物 |

---

## 8. 与 EMF / Sphinx 的关系

| 层 | 提供者 | 提供能力 |
|---|---|---|
| 通用对象建模 | **EMF** | EObject, EPackage, EClass, ResourceSet, Resource, EReference |
| 模型工作区/事务 | **Sphinx** | 跨文件模型管理、ProxyResolver、TransactionalEditingDomain、增量加载 |
| AUTOSAR 元模型 | **Artop AAL** | 上述通用层的 AUTOSAR 实例化（autosar40/gautosar 包） |
| ARXML I/O | **Artop Serialization** | XMI Resource 子类，处理 ARXML 命名空间/格式约定 |
| AUTOSAR 工作区集成 | **Artop Workspace** | autosarnature、模型描述符注册 |
| ECUC 服务 | **Artop ECUC** | ECUC 默认值初始化器 |

**层次关系**：EMF（通用） → Sphinx（工作区） → Artop（AUTOSAR 专用）。新工具 100% 可以照搬这个分层。

---

## 9. 关键参考文件清单

参考工具内可用于源码学习的文件（解压 `.jar` 即可阅读）：

| 文件 | 内容 |
|---|---|
| `plugins/org.artop.aal.autosar448_*.jar/plugin.xml` | EPackage 注册示范 |
| `plugins/org.artop.aal.workspace_*.jar/plugin.xml` | autosarnature 实现示范 |
| `plugins/cn.com.isoft.bswbuilder.modules.memif_*.jar/plugin.xml` | iSoft 业务插件接入扩展点示范（最简模块） |
| `bswmd/Common/*.arxml`（58 份） | AUTOSAR 标准 ECUC-MODULE-DEF 全集 |
| `bswmd/AUTOSAR_00048/*.arxml`（17 份） | MCAL 模块定义 |
| `workspace/Demo_S32K148.../BSW_Builder/S32K148/*.arxml`（32 份） | ECUC-MODULE-CONFIGURATION-VALUES 实例样本 |

---

## 10. 结论

1. **Artop 是必选基础设施**：自实现 AUTOSAR 元模型（~3000 个类）成本不可承受，Artop 是事实标准。
2. **真实使用 20 个 Bundle**，最小工作集 15 个（不含 4.0 兼容），UI 阶段前可压到 9 个。
3. **集成路径明确**：OSGi `Require-Bundle` + 工程 `autosarnature` + 标准 EMF API，无私有协议。
4. **架构借鉴明确**：iSoft 的"业务插件 → mal/pal 中间层 → Artop → Sphinx/EMF"分层可直接复用，差异仅在最上层业务代码。
5. **法律风险可控**：自研项目处于原型阶段时无障碍；商用前需厘清 AUTOSAR 成员资格。

# iSoft V25.10 UI 架构分析（plugin.xml 挖掘）

> 配套 [MEMIF_REPLICA_PLAN.md](../MEMIF_REPLICA_PLAN.md) 和 §9.2 UI 重设计。
>
> .class 加密无法反编（详见 [ADR 0006](../decisions/0006-memif-replica-source-strategy.md)）
> 但 **plugin.xml 是明文 XML**，从中可以挖出整套架构。本文档记录挖到的资产，
> 用作 v0.1 UI 重设计借鉴清单。
>
> 来源：
>   `cn.com.isoft.pal_2.0.5.202601300910.jar` plugin.xml (681 行)
>   `cn.com.isoft.bswbuilder.ui_2.0.5.202601300910.jar` plugin.xml (612 行)

## 1. 透视图 / 视图层

### 1.1 透视图

| ID | Class | 备注 |
|---|---|---|
| `cn.com.isoft.pal.perspectives.autosar` | `cn.com.isoft.pal.perspectives.AutosarPerspective` | 主透视图，名 "Autosar" |

### 1.2 视图

| Name | ID | Class | 在哪 |
|---|---|---|---|
| **Autosar Explorer** | `cn.com.isoft.pal.views.autosarexplorer` | `cn.com.isoft.pal.ui.explorer.AutosarNavigator` | 左栏，项目树 |
| **Autosar Validation** | `cn.com.isoft.pal.autosar.validation` | `cn.com.isoft.pal.ui.views.CustomValidationView` | 底部，表格 |
| **Detail** | `cn.com.isoft.bswbuilder.ui.detailview` | `cn.com.isoft.bswbuilder.ui.ViewPart.DetailView` | 底部右侧，描述/详情 |

`AutosarNavigator` 继承 Eclipse **CommonNavigator** (`org.eclipse.ui.navigator.*`)。
内容来自多个 navigatorContent 扩展拼装：标准 resourceContent + AUTOSAR-specific
content + Bswmd 文件夹 filter。

## 2. 模型层（`cn.com.isoft.mal.model.*`）

虽然 .class 加密读不了，但 plugin.xml 的 `instanceof value="..."` 揭示模型类：

| 模型类 | 角色 |
|---|---|
| `BswBuilderModel` | 项目根（一个 BSW 工程） |
| `EcuConfigurationModel` | 一个 ECU 配置（对应 BSW_Builder/ 文件夹）|
| `ModuleModel` | 单个 BSW 模块（如 MemIf）|
| `ModuleKindModel` | 模块大类（如 MEM）|

工程树：`BswBuilderModel → EcuConfigurationModel → ModuleKindModel → ModuleModel`

## 3. 模块分类（modulekind）—— 共 12 类

通过 `cn.com.isoft.bswbuilder.extensionpoints.modulekind` 扩展点声明：

| name | description |
|---|---|
| `SYS`     | System Service |
| `COM`     | Communication |
| `SEC`     | Security |
| `NM`      | Network Management |
| `DIAG`    | Diagnosis |
| `WDG`     | Wdg, WdgIf and WdgM |
| `MEM`     | Memory |
| `ETHER`   | Ethernet |
| `MCAL`    | Microcontroller |
| `OTHERS`  | Others |
| `CRYPTO`  | CRYPTO Service |
| `CDD`     | CDD |

> 我们当前 ConfigurationEditorsView (已废) 用的是 8 类（PLAN.md §9.2 的简化版）。
> AutosarExplorer 的虚拟分类应该改成这 12 类，与参考一致。

## 4. ActionProviders（右键菜单分级）

| Class | 触发节点类型 | 用途 |
|---|---|---|
| `BswNodeActionProvider` | `BswBuilderModel` | 项目根的右键 |
| `BswFileContainerActionProvider` | `EcuConfigurationModel` | BSW_Builder 文件夹右键 |
| `BswModuleConfigurationActionProvider` | `ModuleModel` | **模块右键 — Validate/Generate/Update Bswmd/Delete 在这里** |
| `ModuleKindActionProvider` | `ModuleKindModel` | 大类节点右键 |

我们当前实现（U1）右键菜单挂在 view 整体，根据选中 File 类型判断显示——
功能等价但架构粒度更粗。v0.2 可改成 typed model + per-class action provider。

## 5. 编辑器（3 个 EditorPart）

| ID | Class | 内容类型 binding | 用途 |
|---|---|---|---|
| `cn.com.isoft.bswbuilder` | `NewBswBuilderEditor` | `org.artop.aal.autosar40.autosar40XMLFile` | 主编辑器，ARXML 默认打开 |
| `cn.com.isoft.bswbuilder.rte` | `BswBuilderRteEditor` | 同上 | RTE 专用 |
| `cn.com.isoft.bswbuilder.ext` | `BswBuilderExtEditor` | 同上 | Extract / 变体 |

全部用同一个 `cn.com.isoft.pal.ui.editors.AutosarActionBarContributor`。

## 6. Master/Detail 页（编辑器内部布局）

通过 `cn.com.isoft.bswbuilder.extensionpoints.container` 扩展点声明：

```xml
<container
      container="MasterDetailContainer"
      containerUIName="General"
      editor="cn.com.isoft.bswbuilder.ui.editor.GeneralMasterDetailPage"
      moduleName="general">
</container>
```

`GeneralMasterDetailPage` 是 Eclipse Forms 主从页面，左 master 树 + 右 detail
表单。**这就是用户截图中央"MemIf Module Manager"的布局**：
- 左侧 "Container Hierarchical information" = master 树（MemIfGenerals → MemIfGeneral）
- 右侧 "MemIfGeneral" 表单 = detail form（4 个参数）

## 7. Properties tabbed sheet（底部 Properties 多 tab）

通过 Eclipse 自带 `org.eclipse.ui.views.properties.tabbed.*` 扩展点：

| contributorId | category | tabs |
|---|---|---|
| `cn.com.isoft.bswbuilder` | `bswbuilder` | PDU Layout |
| `cn.com.isoft.bswbuilder` | `bswbuilderpbs` | Variant |
| `cn.com.isoft.bswbuilder` | `advanced` | Advanced |

每个 tab 对应一个 `propertySection` Java 类，按选中对象类型 filter 启用。

## 8. 资源（icons / messages）

iSoft jar 含 PNG / GIF 图标（约 30+ 个）+ properties 文件（i18n）：

```
icons/autosar.png             # 主品牌图标
icons/autosarFile.png         # ARXML 文件图标
icons/bsw_project.png         # BSW 项目图标
icons/folder.png              # 文件夹
icons/page_white_edit.png     # Detail 视图图标
icons/validation_view_icon.png # Validation 视图图标
icons/OrientaisCoreLogo.png   # iSoft 公司 logo
... 等等
```

法律姿态：图标是 iSoft 商业产品资产，**不直接复用**。我们用 Eclipse
`ISharedImages` 标准图标 + 自绘等价。

messages.properties 是英文 UI 文案，**可以参考措辞** 但不直接复制。

## 9. 我们 v0.1 借鉴清单（按风险排序）

| 借鉴项 | 风险 | 已做 / 计划 |
|---|---|---|
| View 名 "Autosar Explorer" | 低 | ✅ U1 |
| View 名 "Autosar Validation"（之前叫 "Validation"）| 低 | 改名（这一次） |
| View 名 "Detail"（新建底部 tab）| 低 | U4 |
| 12 modulekind 分类 | 低 | 立刻改（这一次） |
| Master/Detail 编辑器布局（Eclipse Forms） | 中 | U3 |
| Tabbed properties sheet（Eclipse 标准）| 中 | U4 |
| ARXML editor with content type binding | 中 | U2 |
| Eclipse CommonNavigator framework | 高 | v0.2 升级 |
| typed model classes (BswBuilderModel etc.) | 高 | v0.2 |

**不借鉴**（明确避免）：
- iSoft 私有 ActionBarContributor 等编译类——加密反编不了，且会引入法律风险
- iSoft 图标资源——商业产品 trade dress
- iSoft 公司 logo / 品牌信息

## 10. 关联

- [MEMIF_REPLICA_PLAN.md](../MEMIF_REPLICA_PLAN.md) — 主复刻计划
- [decisions/0006-memif-replica-source-strategy.md](../decisions/0006-memif-replica-source-strategy.md) — spec-only 路线 ADR
- 用户截图 (Image #5)：参考 UI 视觉

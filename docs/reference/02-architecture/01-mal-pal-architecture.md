# mal / pal 架构总览

> 方向 1 的研究笔记：先把 `cn.com.isoft.mal` 和 `cn.com.isoft.pal` 两个核心 bundle 的骨架摸清楚，后续深入任何 BSW 模块都从这里出发。
>
> 源材料：`src_decompiled/` 下的反编译代码（CFR 0.152，对 `plugins_decrypted/*.jar` 反编译所得）。

---

## 一句话概括

**Eclipse RCP + Sphinx (EMF) + Artop 的"插件全家桶"。每个 BSW 模块是独立 OSGi bundle，通过扩展点注册到一个中央协调器。**

---

## 分层

```
   ┌─────────────────────────────────────────────┐
   │    Eclipse Platform + Sphinx + Artop        │  ← 官方开源
   ├─────────────────────────────────────────────┤
   │  pal/  (Platform Abstraction Layer)          │  ← UI + 工作区/项目/编辑器
   │    Activator · ModelManager · startup        │
   │    ui/* · actions/* · commands/* · nebula    │
   ├─────────────────────────────────────────────┤
   │  mal/  (Model Abstraction Layer)             │  ← 逻辑+模型，无 UI
   │    AutocoreCoordinator  ← 中央注册表         │
   │    BswModuleManager     ← 运行时视图         │
   │    AutocoreModuleDefinition                  │
   │    interfaces/IModuleGenerator/Validator     │
   ├─────────────────────────────────────────────┤
   │  bswbuilder.modules.*   (74 个模块)          │  ← 每个 AUTOSAR BSW 模块各一个
   │  bswbuilder.mcus.*                          │  ← 每个芯片厂商一个
   │  bswbuilder.extensionpoints                 │  ← 声明扩展点（无代码）
   └─────────────────────────────────────────────┘
```

---

## 核心设计：Eclipse 扩展点（Extension Point）

一切插件通过 `plugin.xml` 往几个扩展点注册，`mal` 只读不写。

| 扩展点 | 注册什么 | 谁消费 |
|---|---|---|
| `cn.com.isoft.bswbuilder.extensionpoints.module` | 一个 BSW 模块（Dcm / Com / NVM …） | `AutocoreCoordinator.getVendorModules()` |
| `cn.com.isoft.bswbuilder.extensionpoints.mcu` | 一个 MCU（TC397 / S32K148 …） | `AutocoreCoordinator.getMCUs()` |
| `cn.com.isoft.bswbuilder.extensionpoints.modulekind` | 一个模块分类（Communication / Diagnostic / Memory …） | `AutocoreCoordinator.getBswModuleKind()` |
| `cn.com.isoft.pal.base.common.FunctionBlock` | 启动时要初始化的"功能块" | `SystemInitialize.initialize()` |

一条 module 注册典型属性（见 `AutocoreModuleDefinition` 构造函数与 `AutocoreCoordinator.getVendorModules`）：

```xml
<module shortName="Dcm" kind="Diagnostic"
        vendor="cn.com.isoft.vendor.isoft"
        requiredMcus="TC397,S32K148"
        requiredAutoSarType="..."
        generator="cn.com.isoft.bswbuilder.modules.dcm.DcmGenerator"
        validator="cn.com.isoft.bswbuilder.modules.dcm.DcmValidator"
        editor="cn.com.isoft.bswbuilder.modules.dcm.ui.DcmEditor"
        moduleDescriptor="cn.com.isoft.bswbuilder.modules.dcm.DcmDescriptor"
        bswmd="bswmd/Dcm.arxml"/>
```

运行时 `AutocoreModuleDefinition.getGenerator()` 等方法，本质上是：

```java
confElement.createExecutableExtension("generator")
```

去实例化 `plugin.xml` 里填的那个类 —— 这就是整个软件的**控制反转入口**。

---

## 数据流：从打开工程到看到模块树

```
① 启动
   pal/Activator.start()                       (OSGi 入口)
   └─ 装饰菜单 / 注册 save 拦截
   └─ SystemInitialize.initialize()
       └─ 遍历 FunctionBlock 扩展点 → 逐个 init()

② 打开 BSW 工程
   ui/explorer/AutosarNavigator                (左侧树视图)
   └─ ModelManager.getBswBuilderByProject(project)
       └─ ModelFactory.createBswBuilderModel()
       └─ 读 ARXML → Sphinx 的 EcorePlatformUtil 加载成 EMF 模型
           (autosar40.AUTOSAR / EcucValueCollection)

③ 枚举可用模块
   BswModuleManager.getInstance(mcu)
   └─ AutocoreCoordinator.getBswModuleKind()     (读 modulekind 扩展点)
   └─ AutocoreCoordinator.getVendorModules(mcu)  (读 module 扩展点，按 MCU 过滤)
   └─ 按 kind 分类 → 每个 KindContainModule 下挂一组 AutocoreModuleDefinition

④ 用户点开 Dcm 模块
   moduleDef.getEditorPage()       → 实例化该模块 plugin.xml 里登记的编辑器类
   moduleDef.getModuleDescriptor() → 加载该模块的 bswmd(ARXML) 元模型
```

---

## 关键类速查表

| 类 | 作用 | 位置（相对 `src_decompiled/`） |
|---|---|---|
| `AutocoreCoordinator` | 读扩展点、列模块/MCU/分类 | `cn.com.isoft.mal/cn/com/isoft/mal/coordinator/` |
| `BswModuleManager` | 单例，每次新 MCU 重建；持 `lstKindStructure` | `cn.com.isoft.mal/cn/com/isoft/mal/` |
| `AutocoreModuleDefinition` | 一个模块元数据，能 new 出 generator/validator/editor | `cn.com.isoft.mal/cn/com/isoft/mal/` |
| `AutocoreMetaModelDescriptor` | 抽象基类，每模块提供自己的元模型描述符 | `cn.com.isoft.mal/cn/com/isoft/mal/` |
| `ModelManager` | 工程 → ARXML 模型的静态缓存 | `cn.com.isoft.pal/cn/com/isoft/pal/model/` |
| `ModelFactory` (EMF 生成) | 创建 BswBuilderModel / ModuleKindModel / ModuleModel | `cn.com.isoft.mal.model/` |
| `FunctionBlockManager` | 收集 FunctionBlock 扩展点 | `cn.com.isoft.pal.base.common/` |
| `SystemInitialize` | 启动序列 | `cn.com.isoft.pal/cn/com/isoft/pal/startup/` |

---

## 关键接口（模块作者要实现的"契约"）

```java
// 配置校验
public interface IModuleValidator {
    IStatus validate(IValidationContext ctx);       // 基于 EMF Validation
}

// 代码生成（生成 .c/.h）
public interface IModuleGenerator {
    MultiStatus generate(GModuleConfiguration cfg,
                         File outDir, OutputStream log);
    BSWModuleVersionConstraint[] getSupportedVersions();
}

// 通用序列化
public interface AutosarGenerator {
    String generate(Object obj) throws Exception;   // 给 XML/ARXML 模板用
}

// 模块初始化回调
public interface IModuleInit {
    void init();
    void setObjective(Object o);
}
```

所有 74 个 `bswbuilder.modules.*` 模块都要实现其中若干个。

---

## 注意到的授权机制（另开线路研究）

`AutocoreCoordinator` 中穿插着授权校验，后续如要独立研究 license/dongle 可由此切入：

- `LincenseEncrptyParse.licenseFileValidate()` — 授权文件校验
- `BitAnswerCheck`（`cn.com.isoft.pal.doggle`）— dongle 校验
- 硬编码常量：
  - `HASPID = "1064805545943472156"` — 赛孚耐 HASP 加密狗 ID
  - `HASPTYPE = "HASP-HL"`
  - `FEATUREID = "4"`
- **`getMCUs()` 会在读扩展点前先跑 license 校验，没许可证时 MCU 列表直接被过滤空** —— 这是整个软件的硬性门槛。

相关源码体量：

- `mal/encrypt/FileEncryptyManager.java` — 789 行
- `mal/encrypt/LincenseEncrptyParse.java` — 498 行
- `pal.doggle` 整个子包 — 14 个 .java

---

## 建议的精读顺序（按重要性）

1. `mal/coordinator/AutocoreCoordinator.java` ← 把 200 行后面看完
2. `mal/AutocoreModuleDefinition.java`
3. `mal/BswModuleManager.java`
4. `mal/interfaces/IModuleGenerator.java` + `IModuleValidator.java`
5. `pal/model/ModelManager.java` ← 项目模型全貌
6. `pal/startup/SystemInitialize.java` ← 启动序列
7. 挑一个具体 `bswbuilder.modules.dcm/`，读它的 Generator/Validator 是怎么实现这几个接口的 —— 把理论和实现完全串起来

---

## 相关资源

- 反编译源码根目录：`src_decompiled/`
- 解密后的 jar：`plugins_decrypted/`（`.class` 字节码已 XOR 0x21 还原）
- 原始加密 jar：`plugins/`（运行时由 `00018990_00000004*.dll` + `-agentlib:decrypt` 解密）

# Reference Architecture — Deep Dive

> 5 个盲点 (E3 反思后) 通过 XOR 0x21 解密 + CFR 反编译 iSoft jars 全部挖清。
> 来源 jars: cn.com.isoft.{mal, pal, pal.base.common, bswbuilder.extensionpoints, bswbuilder.ui}_2.0.5.202601300910.jar
> 解密脚本: tools/decrypt_isoft_jar.py (XOR 0x21 .class 字节)
> 反编译: CFR 0.152

## 1. AutocoreCoordinator (mal IoC 入口)

```java
public class AutocoreCoordinator {
    public static AutocoreCoordinator INSTANCE;

    // 读 module 扩展点 → 构建 AutocoreModuleDefinition 列表
    public static ArrayList<AutocoreModuleDefinition> getVendorModules() {
        IExtensionRegistry reg = Platform.getExtensionRegistry();
        IConfigurationElement[] extensions =
            reg.getConfigurationElementsFor("cn.com.isoft.bswbuilder.extensionpoints.module");
        for (IConfigurationElement element : extensions) {
            String mcu = element.getAttribute("requiredMcus");
            ArrayList<String> requiredMcus = mcu == null ? null
                : Arrays.stream(mcu.split(",")).map(String::trim).collect(...);
            list.add(new AutocoreModuleDefinition(
                requiredMcus,
                element.getAttribute("version"),
                element.getAttribute("requiredAutoSarType"),
                element.getAttribute("moduledefinition"),
                element.getAttribute("imageIdentifier"),
                element));   // 持 IConfigurationElement，后续 createExecutableExtension
        }
        return list;
    }

    // 按 MCU 过滤
    public static ArrayList<AutocoreModuleDefinition> getVendorModules(String mcu) {
        for (AutocoreModuleDefinition mod : getVendorModules()) {
            if (mod.getRequiredMcus() == null  // 无 MCU 限制
             || hasCompatibleMcu(mod, mcu))    // MCU 命中
                modules.add(mod);
        }
    }

    // 读 mcu 扩展点 + license 过滤 (必经)
    public static ArrayList<AutocoreMCU> getMCUs() {
        boolean ok = LincenseEncrptyParse.licenseFileValidate();
        List<String> licMcus = ok ? LincenseEncrptyParse.getMcuList() : new ArrayList<>();
        Map<String, OsInfoEntity> osMap = ExcelUtils.getAllOsInfoEntity();
        // 1. 先从 OS info excel 拿 (按 license 白名单过滤)
        for (Entry<String, OsInfoEntity> e : osMap.entrySet()) {
            if (licMcus.contains(e.getKey()))
                mcus.add(new AutocoreMCU(key, manufacturer, chipSeries, false, 1));
        }
        // 2. 再从 mcu 扩展点补充 (license 白名单 + osMap 没有的)
        for (IConfigurationElement elem : reg.getConfigurationElementsFor(
                "cn.com.isoft.bswbuilder.extensionpoints.mcu")) {
            if (!osMap.containsKey(elem.getAttribute("mcuName"))
             && licMcus.contains(elem.getAttribute("mcuName"))) {
                mcus.add(new AutocoreMCU(name, manufacturer, mcuModel, multicore, numCores));
            }
        }
    }

    // 读 modulekind 扩展点
    public ArrayList<BswModuleKind> getBswModuleKind() {
        for (IConfigurationElement elem : reg.getConfigurationElementsFor(
                "cn.com.isoft.bswbuilder.extensionpoints.modulekind")) {
            list.add(new BswModuleKind(elem.getAttribute("name"),
                                       elem.getAttribute("description")));
        }
    }
}
```

**关键不变量**: 所有读扩展点都用标准 Eclipse `Platform.getExtensionRegistry().getConfigurationElementsFor(point_id)`。
不缓存——每次调用都重新扫扩展点（Eclipse 内部已缓存，无需自己缓存）。

## 2. AutocoreModuleDefinition (IoC dispatcher)

```java
public class AutocoreModuleDefinition implements Cloneable {
    private final IConfigurationElement confElement;  // 来自扩展点
    // 6-arg constructor
    // (requiredMcus, version, autosarType, moduledefinition, imageIdentifier, IConfigurationElement)

    public Object getGenerator()        throws CoreException
        { return confElement.createExecutableExtension("generator"); }
    public Object getValidator()        throws CoreException
        { return confElement.createExecutableExtension("validator"); }
    public Object getEditorPage()       throws CoreException
        { return confElement.createExecutableExtension("editor"); }
    public Object getModuleDescriptor() throws CoreException
        { return confElement.createExecutableExtension("moduleDescriptor"); }
    public Object getUpdateBswmd()      throws CoreException
        { return confElement.createExecutableExtension("updateBswmd"); }

    public String getModuleBswmd()     { return confElement.getAttribute("bswmd"); }
    public String getModuleInterface() { return confElement.getAttribute("moduleInterface"); }
    public String getNamespaceIdentifier() { return confElement.getNamespaceIdentifier(); }
}
```

**关键模式**: `confElement.createExecutableExtension("attr")` 是 Eclipse 标准 IoC 实例化机制。
每次调用都 new 一个新实例（无 cached singleton）。

## 3. BswModuleManager (按 MCU 过滤的"伪单例")

```java
public class BswModuleManager {
    private static BswModuleManager INSTANCE;
    private List<KindContainModule> lstKindStructure;
    private List<AutocoreModuleDefinition> availableModules;
    private List<BswModuleKind> lstBswModuleKind;

    // 注意: 每次调用都 new 新实例！不是真单例
    public static BswModuleManager getInstance(String mcu) {
        INSTANCE = new BswModuleManager(mcu);
        return INSTANCE;
    }

    private BswModuleManager(String mcu) {
        // 1. lstBswModuleKind 来自 AutocoreCoordinator.getBswModuleKind() (modulekind 扩展点)
        for (BswModuleKind k : lstBswModuleKind)
            lstKindStructure.add(new KindContainModule(k));   // 每个 kind 一个空容器
        // 2. 按 MCU 过滤模块，塞进 KindContainModule
        classifyModules(mcu);
        // 3. 删空 KindContainModule (那个 kind 没模块)
        clearUnusedKind();
    }

    private void classifyModules(String mcuName) {
        availableModules = AutocoreCoordinator.getVendorModules(mcuName);
        for (AutocoreModuleDefinition module : availableModules) {
            for (KindContainModule obj : lstKindStructure) {
                if (obj.getKindName().equals(module.getKind())) {
                    obj.addModule(module);
                    module.setParent(obj);
                }
            }
        }
    }
}
```

**MCU 切换**: 用户/代码再调一次 `BswModuleManager.getInstance(newMcu)` —— 直接 new 新实例覆盖 INSTANCE。
旧 INSTANCE 引用还指向旧 MCU 数据（短生命周期对象，GC 回收）。

## 4. AutocoreMetaModelDescriptor (Sphinx 集成的元模型注册)

```java
public abstract class AutocoreMetaModelDescriptor extends Sphinx::AbstractMetaModelDescriptor {
    protected AutocoreMetaModelDescriptor(String, String, MetaModelVersionData);
    public String getDefaultContentTypeId();
    public abstract IFunctionExtension getFunctionExtension();   // 模块自己实现
}
```

**bswmd 路径不在这里**——通过 `AutocoreModuleDefinition.getModuleBswmd()`
读 `confElement.getAttribute("bswmd")`（plugin.xml 属性）。
此抽象类只负责 Sphinx 元模型注册 + IFunctionExtension。

## 5. ModelManager (pal 静态缓存)

```java
public class ModelManager {
    // 4 张静态 Map
    private static Map<String, BswBuilderModel>                   projectBswBuilderModelMap;
    private static Map<String, Map<String, AUTOSAR>>              projectAutosarMap;
    private static Map<String, Map<String, EcucValueCollection>>  ecucValueCollectionMap;
    private static Map<String, Map<String, EcucModuleConfigurationValues>>  ecucModuleConfigurationValuesMap;
    public static String oldProjectName;

    public static BswBuilderModel getBswBuilderByProject(IProject project) {
        BswBuilderModel model = projectBswBuilderModelMap.get(project.getName());
        if (model == null) {
            if (loadNavigatorModel(project))            // 从持久化加载
                return projectBswBuilderModelMap.get(project.getName());
            // 兜底: 检查 IFunctionBlock 注册 + isBSWBuilderProject
            for (IFunctionBlock fb : FunctionBlockManager.getRegFunctionBlock()) {
                if (WorkspaceUtils.isBSWBuilderProject(project)
                 && fb.getId().equals("cn.com.isoft.bsw.funcId")) {
                    model = ModelFactory.eINSTANCE.createBswBuilderModel();  // EMF factory
                    model.setName("BSW_Builder");
                    model.setProjectName(project.getName());
                    projectBswBuilderModelMap.put(project.getName(), model);
                }
            }
        }
        return model;
    }

    // 失效: 清空 4 张 map 中该 project 的所有缓存 + 重建 mal model children
    public static void resetBswBuildModel(IProject project) {
        ecucValueCollectionMap[project].clear();
        ecucModuleConfigurationValuesMap[project].clear();
        projectAutosarMap[project].clear();
        BswBuilderModel model = getBswBuilderByProject(project);
        model.getEcuConfigurationModels().clear();
        // 然后扫 BSW_Builder/ 重建 EcuConfigurationModel 列表 (代码截断)
    }

    public static void loadProjectResource(IProject project) {
        BswBuilderModel model = getBswBuilderByProject(project);
        for (EcuConfigurationModel ecu : model.getEcuConfigurationModels())
        for (ModuleKindModel kind : ecu.getModuleKindModels())
        for (ModuleModel mod : kind.getModuleModels()) {
            IFile lib = getLibFileByModuleName(project, mod.getModuleName());
            IModelDescriptor md = ModelDescriptorRegistry.INSTANCE.getModel(lib);
            modelDescriptors.add(md);
        }
        ModelLoadManager.INSTANCE.loadModels(modelDescriptors, true, null);
    }
}
```

**Cache 失效触发点** (5 处):
1. 用户右键 *Reset Cache* → ResetCacheAction.run() → resetBswBuildModel + refreshNavigatorViewer
2. 用户 *Open Resource* (覆盖标准 action) → OpenResourceOverrideAction (implements IResourceChangeListener)
3. 新工程向导 → NewBswExampleProjectWizard
4. 树展开 IProject → CustomExplorerContentProvider.getChildren 检查 oldProjectName 是否需 rename
5. ModelManager 内部 reload 路径

**没有自动 ResourceChangeListener**——iSoft 选择"用户主动 reset" + "针对性 hook"，不监 workspace 全量 delta。

## 6. CustomExplorerContentProvider (pal: IProject → BswBuilderModel 桥)

```java
public class CustomExplorerContentProvider extends Sphinx::BasicExplorerContentProvider {
    public Object[] getChildren(Object parentElement) {
        if (parentElement instanceof IProject && project.isOpen()) {
            // rename hook
            if (ModelManager.oldProjectName != null) {
                ModelManager.renameProjectMapCache(project.getName());
                ModelManager.loadProjectResource(project);
                ModelManager.resetBswBuildModel(project);
                ModelManager.refreshProject(project);
            }
            ArrayList<BswBuilderModel> nodes = new ArrayList<>();
            nodes.add(ModelManager.getBswBuilderByProject(project));
            return nodes.toArray();
        }
        // else: super 处理 (Resource / EObject 等)
    }
}
```

**关键**: 不全量 override，只覆盖 IProject 那一格；其它走 Sphinx super (IFile→Resource→EObject)。

## 7. BswExplorerContentProvider (bswbuilder.ui: BswBuilderModel→子树)

```java
public class BswExplorerContentProvider extends Sphinx::BasicExplorerContentProvider
                                        implements ITreeContentProvider {

    // 监 EMF ResourceSet 变化，刷新 viewer
    protected ResourceSetListener createResourceChangedListener() {
        return new ResourceSetListenerImpl(
            NotificationFilter.createFeatureFilter(EResourceSet, 0)
                .or(NotificationFilter.createFeatureFilter(EResource, 4))   // CONTENTS feature
                .or(NotificationFilter.createFeatureFilter(EResource, 3))   // URI feature
        ) {
            public void resourceSetChanged(ResourceSetChangeEvent ev) {
                ExtendedPlatformUI.getDisplay().asyncExec(() -> getViewer().refresh());
            }
            public boolean isPostcommitOnly() { return true; }
        };
    }

    public Object[] getChildren(Object parentElement) {
        if (parentElement instanceof BswBuilderModel)
            return baseNode.getEcuConfigurationModels().toArray();
        if (parentElement instanceof EcuConfigurationModel)
            return bswFileContainer.getModuleKindModels().toArray();
        if (parentElement instanceof ModuleKindModel)
            return ((ModuleKindModel)parentElement).getModuleModels().toArray();
        return new Object[0];   // ModuleModel 是叶子
    }
}
```

**关键**: 不 override `getElements/hasChildren/getParent` —— 完全继承 Sphinx 父类逻辑。

## 8. AutosarNavigator (pal: 自定义 view)

```java
public class AutosarNavigator extends Sphinx::ExtendedCommonNavigator {
    protected IPartListener partListenerNew;

    protected CommonViewer createCommonViewer(Composite);
    protected CommonViewer createCommonViewerObject(Composite);
    public void restoreState(IMemento);    // 恢复树展开状态
    public void saveState(IMemento);       // 保存树展开状态
    protected SaveablesProvider createModelSaveablesProvider();   // 接 EMF dirty 状态
    public Saveable[] getActiveSaveables();
    private Set<Saveable> getSaveables(IProject);
    protected boolean isActivePart();
    private boolean isActiveEditor();
}
```

继承 **ExtendedCommonNavigator** (Sphinx)，比 Eclipse 标准 CommonNavigator 多:
- SaveablesProvider 集成 (跟 EMF EditingDomain dirty 状态联动)
- TreeViewer state 持久化 (IMemento)
- partListener (响应 editor 切换刷新选择)

## 9. SystemInitialize + ProjectResourceLoad (启动序列)

```java
// pal Activator.start (BundleContext) 仅注册 Save command 拦截 + workbench listener
public void start(BundleContext context) {
    PlatformUI.getWorkbench().addWorkbenchListener(this.workbenchListener);
    saveCommand.addExecutionListener(new SaveInterceptor());
    saveAllCommand.addExecutionListener(new SaveInterceptor());
    PreferencesUtils.iniTheadEnable();
}

// 触发 IFunctionBlock.initialize() 在 ProjectResourceLoad.earlyStartup() 之外 (不在 Activator 里)
public class SystemInitialize {
    public void initialize() {
        for (IConfigurationElement elem : reg.getConfigurationElementsFor(
                "cn.com.isoft.pal.base.common.FunctionBlock")) {
            IFunctionBlock fb = (IFunctionBlock)elem.createExecutableExtension("FunctionBlock");
            fb.initialize();
        }
    }
}

// org.eclipse.ui.startup 早启动钩子
public class ProjectResourceLoad implements IStartup {
    public void earlyStartup() {
        ProfileUtil.updateStartDate();
        initFuncEnableStatus();
        createDef();
        createStdDef();
        createSwAddrMethodsFile();
        setPathManager();    // 注 "Temp" path variable -> bswmd/
    }
}
```

## 10. 5 个核心扩展点完整 schema

### `cn.com.isoft.bswbuilder.extensionpoints.module` (16 attr)
| attr | required | basedOn |
|---|---|---|
| kind | ✓ | string |
| moduledefinition | ✓ | resource |
| requiredMcus | - | string (comma-separated) |
| version | - | string |
| imageIdentifier | ✓ | string |
| editor | ✓ | java |
| generator | - | java basedOn IModuleGenerator |
| vendor | ✓ | identifier (cn.com.isoft.pal.vendor/@id) |
| shortName | ✓ | string |
| validator | - | java basedOn IModuleValidator |
| outlineContributor | - | java |
| moduleDescriptor | ✓ | java |
| moduleInterface | - | resource |
| bswmd | - | resource |
| requiredAutoSarType | - | string |
| updateBswmd | - | java basedOn IModuleUpdateBswmd |

### `mcu` (5 attr): mcuName / mcuManufacturer / multicore / numberOfCores / mcuModel
### `modulekind` (2 attr): name / description
### `container` (5 attr): requiredMcus / moduleName / container / editor / containerUIName
### `cn.com.isoft.pal.base.common.FunctionBlock` (1 attr): FunctionBlock (java)

## 11. 真实 module 注册示例 (memif jar plugin.xml)

```xml
<extension point="cn.com.isoft.bswbuilder.extensionpoints.module">
  <module
    editor="cn.com.isoft.bswbuilder.modules.memif.MemIfDefaultRegistry"
    generator="cn.com.isoft.bswbuilder.modules.memif.generator.MemIfGenerator"
    imageIdentifier="MemIf"
    kind="MEM"
    moduleDescriptor="cn.com.isoft.bswbuilder.modules.memif.MemIfMetaModelDescriptor"
    moduledefinition="MemIfDef.arxml"
    shortName="MemIf"
    validator="cn.com.isoft.bswbuilder.modules.memif.validator.MemIfValidator"
    vendor="cn.com.isoft.pal.arccorevendor"
    version="2.0.1"
    bswmd="MemIf_Bswmd.arxml"
    updateBswmd="cn.com.isoft.bswbuilder.modules.memif.bswmd.MemIfUpdateBswmd"/>
</extension>
```

`editor` 属性指向 `MemIfDefaultRegistry` —— 不是 FormEditor 子类，而是某种 registry/factory。
`requiredMcus` 在 memif 没设 → 所有 MCU 通用。
`requiredAutoSarType` 也没设 → 所有 AUTOSAR 版本通用。

## 12. 回答 5 个盲点

| 盲点 | 答案 |
|---|---|
| 1. AutocoreCoordinator 内部 API | `Platform.getExtensionRegistry().getConfigurationElementsFor(point)` 标准 Eclipse pattern；4 个扩展点：module/mcu/modulekind/container/FunctionBlock |
| 2. ModelManager 缓存失效 | 5 处显式触发；**无 ResourceChangeListener 自动失效**；`oldProjectName != null` 检查在 ContentProvider 里做 rename 兜底 |
| 3. BswModuleManager MCU 切换 | `getInstance(newMcu)` 直接 new 覆盖；旧实例被 GC |
| 4. AutocoreMetaModelDescriptor | extends Sphinx `AbstractMetaModelDescriptor`；只持元模型注册数据，bswmd 路径走 plugin.xml `bswmd=` 属性 |
| 5. requiredAutoSarType 值集合 | plugin.xml 字段，runtime 透传给 AutocoreModuleDefinition；具体值由 `hasCompatibleAutosarType` 比对（未挖完，但实例 memif 没设 = 通用） |

## 13. 6 个 bonus 发现 (E3 之外的)

1. **CustomExplorerContentProvider 真的 extends Sphinx BasicExplorerContentProvider** —— 我 E3 第一版方向接近对的，错在用了 `IPipelinedTreeContentProvider2` 干扰
2. **AutosarNavigator extends Sphinx ExtendedCommonNavigator** —— 不是裸 CommonNavigator
3. **mal.model 是 EMF generated**: `ModelFactory.eINSTANCE.createBswBuilderModel()` 标准 EMF factory
4. **getBswBuilderByProject 兜底**: 检查 `WorkspaceUtils.isBSWBuilderProject(project)` AND FunctionBlock id `"cn.com.isoft.bsw.funcId"` 双条件
5. **createExecutableExtension** 是 IoC 入口的核心机制
6. **没有 ResourceChangeListener 自动监 workspace** —— 选择"用户主动 reset" + "针对性 hook"

## 14. 对 E3-B Plan 的影响

基于上述精确数据，E3-B 修订:

- **navigator content provider 走 Sphinx**：`extends BasicExplorerContentProvider` + 单 `getChildren` override（**不**用 IPipelinedTreeContentProvider2，**不**用纯 ITreeContentProvider）
- **navigator view 走 Sphinx ExtendedCommonNavigator**：`extends ExtendedCommonNavigator` 不是 CommonNavigator
- **getBswBuilderByProject 兜底**：判 BSW project 用复合条件 (`isBSWBuilderProject` + FunctionBlock id 匹配)，不是简单 `findMember("BSW_Builder")`
- **mal model 不强求 EMF Ecore 生成**：参考是 EMF 但 POJO + `ModelFactory.create*()` 静态工厂可平替
- **Cache 失效不监 ResourceChangeListener**：5 处显式触发就够了（rename / new wizard / reset action / open resource override / content provider 兜底）
- **createExecutableExtension** 是必走的 IoC 路径：每个模块通过 plugin.xml 注册到 `bswbuilder.extensionpoints.module`

E3-B 计划文件清单 (修订):
1. `cn.com.myorg.bswbuilder.extensionpoints` bundle (5 .exsd schema + plugin.xml + manifest)
2. `pal.ModelManager` (EMF factory + 4 静态 cache map)
3. `pal.SystemInitialize` (FunctionBlock 启动序列) + `pal.ProjectResourceLoad` (IStartup)
4. `pal.functionblock.{IFunctionBlock, FunctionBlockManager}` (基础设施)
5. `mal.AutocoreCoordinator` (读 4 扩展点)
6. `mal.BswModuleManager` (按 MCU 过滤)
7. `mal.AutocoreModuleDefinition` (createExecutableExtension 5 个)
8. `mal.AutocoreMetaModelDescriptor` (Sphinx AbstractMetaModelDescriptor 继承)
9. 5 接口: `IModuleGenerator/Validator/Editor/Init/UpdateBswmd` + `IFunctionBlock`
10. `BswExplorerContentProvider`: `extends BasicExplorerContentProvider` + 仅 override `getChildren`
11. `BswAutosarExplorerView`: `extends ExtendedCommonNavigator`
12. memif bundle 改造: plugin.xml 注册 module 扩展点 + 实现 IModuleEditor

总文件数估计 ~25 (含新 extensionpoints bundle)。

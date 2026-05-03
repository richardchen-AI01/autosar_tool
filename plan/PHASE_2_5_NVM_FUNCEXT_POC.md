# Phase 2.5 — NvM functionextensions hook PoC

> 关联: `orientais_studio/plan/NVM_MEMIF_DECOMPILE_PLAN_v3.md` Phase 2.5 + 6c 起点
> 状态: 待用户拍板 D-PoC 后开撸; 推进时通过 commit message body 更新 [ ] 状态; 工作完成后让本文件自然过时
> 范围: 14 文件 (10 新建 + 4 改)

---

## 0. 背景 + 反编验证

参考端 hook 数据流 (反编实证, 文件路径全部引用至 `_decompiled/`):

```
host UI widget (BaseEditUnit / EnableUnit / ParamConfContainerUnit / BswContainerUtil 等)
    ↓ 调用
MetaModelDescriptorParser.getUIDefinitionList(ecuName, elementName, variantFlag)   [mal jar]
    ↓ via BswModuleManager.getInstance(ecuName).getMetaModelDescriptorList()
metaModelDescriptor.getFunctionExtension()  [AutocoreMetaModelDescriptor.abstract]
    ↓
funcExtension.getUIDefinitionMap()  [模块 NvMFunctionExtension/MemIfFunctionExtension impl]
    ↓
uiDefinitionMap.getUIDefinitionList(elementName) → 按 variant flag 过滤
    ↓
host widget 拿到 List<IUIDefinition> 应用 (灰显/disable/auto-compute)
```

参考端 `IUIDefinition` 5 种父类 (覆盖 NvM 49 个 functionextensions):
| 父类 | 数量 | 用途 |
|---|---|---|
| ComputeEnableUIDefinition | 32 | 字段灰显 + 自动计算 (Block 主流) |
| ReferenceValueScopeUIDefinition | 10 | Ref 字段 drop-down 候选 (Phase 6d 用) |
| RelatedUIDefinition | 4 | Block 关联属性, 跨字段联动 |
| ReserveUIDefinition | 1 | 容器右键菜单约束 (NvMBlockDescriptorEnable) |
| EnumValueScopeUIDefinition | 1 | enum 值动态域 |

参考端 plugin.xml 注册路径: `cn.com.isoft.bswbuilder.extensionpoints.module` extension point 的 `moduleDescriptor` 属性指向 NvMMetaModelDescriptor (实装 `AutocoreMetaModelDescriptor` 抽象 + 返回 `new NvMFunctionExtension()`); host 端 `AutocoreCoordinator.getVendorModules()` 读 plugin.xml 拿到所有 module → `BswModuleManager` 单例缓存。

---

## 1. MEN 现状 (sweep 实证)

| 资产 | 状态 | 评价 |
|---|---|---|
| `frameworks/cn.com.myorg.mal/BswModuleManager.java` | ✅ 已 port (字节级跟参考一致) | 不动 |
| `frameworks/cn.com.myorg.mal/AutocoreMetaModelDescriptor.java` | ✅ 已 port (跟参考一致) | 不动 |
| `frameworks/cn.com.myorg.mal/interfaces/{IFunctionExtension, IModuleValidator, IModuleGenerator, IModuleUpdateBswmd, IModuleInit, AutosarGenerator}.java` | ⚠ IFunctionExtension 是 marker (E3-B-4 临时), 其余正常 | IFunctionExtension 待扩 |
| `frameworks/cn.com.myorg.mal/uidefinition/` 整个包 | ❌ 不存在 | 全新建 |
| `frameworks/cn.com.myorg.mal/MetaModelDescriptorParser.java` | ❌ 不存在 | 新建 |
| `modules/.../nvm/NvMMetaModelDescriptor.java` | ✅ 已 wire `getFunctionExtension()` 返回 `new NvMFunctionExtension()` | 不动 |
| `modules/.../nvm/functionextensions/NvMFunctionExtension.java` | ⚠ 15 行 stub (空 marker impl) | 实装 `getUIDefinitionMap` |
| `modules/.../nvm/block/functionextensions/` 整个包 | ❌ 不存在 | PoC 阶段新建 1 个 |
| `modules/.../memif/functionextensions/MemIfFunctionExtension.java` | ⚠ 15 行 stub | 同步扩 (返回空 map, 跟参考一致) |
| `builder_core/.../GenericGeneralFormPage.java` | ✅ 已就位 (E5-2, 291 行) | 加 hook dispatch |
| `builder_core/.../GenericMasterDetailFormPage.java` | ✅ 已就位 (E5-3, 693 行) | 同上 (本 PoC 优先 GeneralForm) |

骨架 70% 已搭好。

---

## 2. 范围 — 动哪些文件

### S1. mal framework 扩补 (10 新 + 1 改)

**改**:
- `frameworks/cn.com.myorg.mal/src/cn/com/myorg/mal/interfaces/IFunctionExtension.java`
  - marker → 完整契约 (3 abstract methods + `DataHandle` 内类 + 9 EOperation `public static final String` 常量)
  - 照搬参考 `cn.com.isoft.mal.interfaces.IFunctionExtension`

**新建** (照搬参考反编, 包路径 `cn.com.isoft.mal.uidefinition.*` → `cn.com.myorg.mal.uidefinition.*`):
- `mal/uidefinition/IUIDefinition.java` (12 long flag 常量 + `getDefElementName()` + `getVariant()`)
- `mal/uidefinition/UIDefinitionMap.java` (HashMap<String, List<IUIDefinition>>, `put` + `getUIDefinitionList`)
- `mal/uidefinition/RelatedUIDefinition.java` (abstract, `getRelatedUIElementList()`)
- `mal/uidefinition/EnableUIDefinition.java` (abstract extends RelatedUIDefinition, `isEnable` + `isDisable`)
- `mal/uidefinition/ComputeEnableUIDefinition.java` (abstract extends EnableUIDefinition, `compute()` + final isEnable/isDisable + getVariant=12296L)
- `mal/uidefinition/IAutoComputeUIDefinition.java` (extends IUIDefinition, `calc()`)
- `mal/uidefinition/ReferenceValueScopeUIDefinition.java` (abstract, drop-down 候选 — Phase 6d 用, PoC 仅占位)
- `mal/uidefinition/ReserveUIDefinition.java` (abstract, 右键菜单约束 — NvMBlockDescriptorEnable 用, PoC 仅占位)
- `mal/uidefinition/EnumValueScopeUIDefinition.java` (abstract, enum 动态域 — PoC 仅占位)

**新建** (中央分发):
- `frameworks/cn.com.myorg.mal/src/cn/com/myorg/mal/MetaModelDescriptorParser.java` (静态 4 个方法, 照搬参考)

**MANIFEST.MF**: 加 `Export-Package: cn.com.myorg.mal.uidefinition` (现有 `cn.com.myorg.mal` + `cn.com.myorg.mal.interfaces` 已 export)

**验收**: `mvn install -pl ide/frameworks/cn.com.myorg.mal -am` 退出 0; jar 内含 11 个新 .class

### S2. NvM bundle PoC (1 新 + 1 改)

**新建**:
- `modules/cn.com.myorg.bswbuilder.modules.nvm/src/cn/com/myorg/bswbuilder/modules/nvm/block/functionextensions/NvMBlockUseCrcEnable.java`
  - 照搬反编 `cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMBlockUseCrcEnable`
  - 包路径迁移 `cn.com.isoft.* → cn.com.myorg.*`
  - 依赖: `EcuUtils.getBooleanValue` — Phase 4 已反 `cn.com.isoft.mal.modelutils.EcuUtils`, 但 MEN 是否已 port 需查 (`frameworks/cn.com.myorg.mal/modelutils/` 现仅有 `DefaultRegistry.java`, 缺 EcuUtils) → S2 子任务: 同时 port `EcuUtils.getBooleanValue` 到 MEN (单方法, 不全套)

**改**:
- `modules/.../nvm/functionextensions/NvMFunctionExtension.java`
  - body 实装 `getUIDefinitionMap()`: `m.put(new NvMBlockUseCrcEnable())` (PoC 仅 1 个)
  - 实装 `getModuleInit()` 返 null
  - 实装 `getDataHandleMap()` 返 empty HashMap
- `modules/.../memif/functionextensions/MemIfFunctionExtension.java` (同步)
  - 实装 `getUIDefinitionMap()` 返 empty `UIDefinitionMap` (跟参考一致)
  - 其余同上

**验收**: NvM bundle build OK + `unzip -l ...nvm-*.jar | grep NvMBlockUseCrcEnable.class` 命中

### S3. GenericGeneralFormPage host wire (1 改)

**改**:
- `builder_core/cn.com.myorg.bswbuilder.ui/src/cn/com/myorg/bswbuilder/ui/editor/pages/GenericGeneralFormPage.java`
  - 字段 widget 创建 + 字段 value change 事件 (现有 RecordingCommand wrap, E5-6 S3) 触发时:
    1. 取 `ecuName` (项目名/当前编辑器对应的 ECU 标识 — R1 风险点)
    2. `MetaModelDescriptorParser.getUIDefinitionList(ecuName, elementName, IUIDefinition.ENABLE_FLAG)`
    3. 遍历 list, instanceof EnableUIDefinition → `enable.isEnable(parent)` 决定灰显
  - 也调 `getRelatedUIElementList()` 注册联动 — 当相关字段值变化时 re-evaluate 所有 dependent

**验收**: editor bundle build OK; 启动后 widget 创建路径含 hook 调用 (log trace)

### S4. PoC 集成测试

1. Mac: `mvn clean install` 全 build OK
2. bump N (按 memory dev_workflow_deploy 纪律, 跨 commit bump N)
3. Win: deploy `D:\bswbuilderN\` + workspace 副本 `D:\bswbuilderN\workspace\Demo_S32K148`
4. 启动 → 打开 Demo_S32K148/.../NvMDef.arxml (其实是 NvM 配置 .arxml — Demo 项目里)
5. 选 `NvMBlock_DataA` (示例 NvBlockDescriptor 实例)
6. 改 `NvMWriteBlockOnce` toggle:
   - true → `NvMBlockUseCrc` 字段**灰显** (因 compute 返 false)
   - false → `NvMBlockUseCrc` **可编辑**
7. 边界: shortName == "NvMBlock_ConfigID" 时永远灰显 (compute 包了这条)

---

## 3. 步骤 (依赖顺序)

- [ ] **S1** mal framework 扩补 — 10 新 + 1 改 + MANIFEST + build 验
- [ ] **S2** NvM bundle PoC — 1 新 functionextension + 改 NvMFunctionExtension/MemIfFunctionExtension + EcuUtils.getBooleanValue port + build 验
- [ ] **S3** GenericGeneralFormPage host wire — 1 改 + build 验
- [ ] **S4** PoC 集成测试 — Mac build + bump N + Win deploy + GUI 验灰显切换

每步 1 个 commit. S 失败 → restore 前一步 commit.

---

## 4. 验收

- 硬验收 (S4): NvMWriteBlockOnce=true 时 NvMBlockUseCrc 字段灰显; =false 时可编辑
- 边界: NvMBlock_ConfigID 容器永远灰显
- 工作量: 14 文件 (10 新 + 4 改)
- 质量门: 每步 build 退出 0; 反编对照 file:line 写在 commit body (按 conventions/GIT_CONVENTION.md)

---

## 5. 风险 + 回滚

| # | 风险 | 触发信号 | 回滚 / 纠偏 |
|---|---|---|---|
| R1 | `BswModuleManager.getInstance(ecuName)` 的 ecuName 来源不显式 | 启动后 `getMetaModelDescriptorList()` 返空, hook list 空 | 反 `AutocoreCoordinator.getVendorModules` 看 ecuName 用法 → MEN 对齐 (按 memory 撞坑先回溯参考) |
| R2 | host wire 时机跟 Sphinx EditingDomain transactional 冲突 | widget value change 时 hook 调用抛 IllegalStateException | hook 调用挪到 RecordingCommand 之外的 listener (E5-6 S3 已经把 SetCommand 包好, hook 是只读 dispatch 应该没问题) → 走错回 S3 commit restore |
| R3 | IFunctionExtension marker → full impl 影响 implements 它的所有类 | MemIf / 未来其他 module 编译失败 | S1 + S2 同 commit 出, MemIfFunctionExtension 同步实装空 map |
| R4 | EcuUtils.getBooleanValue 还没 port | NvMBlockUseCrcEnable.compute 编译失败 | S2 子任务先 port (单方法, 不全套) |

回滚总策略: 4 个 step 每个独立 commit, 任何一步挂了 `git restore` + revert commit, 不污染 main 分支。

---

## 6. 待用户确认决策点

### D-PoC: 范围

- [ ] **A** (推荐, 跟 plan v3 D1 验收一致): 只做 1 个 NvMBlockUseCrcEnable PoC, 通了再扩 32 个 (= Phase 6c)
- [ ] **B**: 一次做 32 个 Block functionextensions
- [ ] **C**: 一次做 49 个 (Block 32 + Demevent 8 + Common 9)

回滚成本: A=14 文件 / B=46 文件 / C=63 文件

推荐 **A** — 工作量可控, hook 路通过后 Phase 6c 把 32 个全 port 是机械工作 (照搬反编), 风险低。

### D-NS (PoC 后): 命名空间

- [ ] **N1** (推荐, plan v3 D1): 包路径迁移 `cn.com.isoft.* → cn.com.myorg.*`, 类名/方法名/字段名/逻辑全照搬
- [ ] **N2**: 完全自起 MEN 命名空间不复用任何 isoft 名字 (溯源不清, 不推荐)

推荐 **N1** — 反编代码可直接 paraphrase, commit message body 引用反编 file:line 满足复刻溯源 (按 GIT_CONVENTION).

---

## 7. 后续 (本 plan 范围外, 衔接 task #2~#8)

PoC 通过后:
- Phase 6c (Task #2): NvM 32 + 17 个 functionextensions 全 port + 通用底座加载 NvMDef.arxml 显示 NvMBlockDescriptor
- Phase 6d (Task #6): NvBlockDescriptor 多实例 + NvMFeeRef/NvMEaRef 跨 .arxml drop-down (要 ReferenceValueScopeUIDefinition 全用上)
- Phase 6e (Task #3): NvM Validator 12 校验函数 port (Java 813 行参考)
- Phase 6f (Task #7): NvmSelectWizard SW-C → NvBlockDescriptor 联动 (要 service 层 NvmParallelModel + NvBlockDescriptorObj 等 26 类 port)

PoC 不解决 R1 (ecuName 来源), 但暴露问题让 Phase 6c 修。

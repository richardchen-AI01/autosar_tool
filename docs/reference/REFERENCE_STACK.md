# 参考项目 (ORIENTAIS V25.10) 完整技术栈

**Sweep 日期**: 2026-04-30
**目的**: 在做 v0.2 EMF 路线切换前，先把参考项目用了什么、版本多少全列清。
我们 v0.1 应该用的就是这套，避免再撞"路线不一致"。

源数据：
- Win 上 `D:\ORIENTAIS_Studio\ORIENTAIS_Configurator_for_EasyXMen_V25.10\`
- 启动 ini: `ORIENTAIS_Configurator_for_EasyXMen_V25.10.ini`
- 309 个 plugin/feature jar in `plugins/`

---

## 1. JVM + Launcher

| 项 | 参考 | 我们 v0.1 现状 | 一致？ |
|---|---|---|---|
| **JRE** | 自带 (在 `jre/bin/javaw.exe`) | 我们 ini 也指向参考自带的同一个 JRE | ✅ |
| **`-Dosgi.requiredJavaVersion`** | `1.8` | （我们 ini 没显式声明）| 🟡 隐式一致 |
| **`-Xms` / `-Xmx`** | `512m` / `2048m` | `256m` / `1024m` | ⚠️ 我们小一半 |
| **`-Xss`** | `2m` | (默认) | ⚠️ |
| **`-XX:+UseParallelGC` / `-Xverify:none`** | 都开了 | 都没开 | ⚠️ |
| **`-agentlib:decrypt`** | iSoft 自家 .class 解密 agent | 我们不需要（v0.1 没 iSoft 加密 class）| ✅ 不适用 |
| **Equinox launcher** | `1.5.200.v20180922-1751` (Eclipse 2018-12) | 同 | ✅ |
| **launcher win32 x86_64** | `1.1.900.v20180922-1751` | 同 | ✅ |

---

## 2. Eclipse 平台基础

| 部件 | 参考版本 | 我们 v0.1 |
|---|---|---|
| **Eclipse RCP / Platform** | 2018-12 (org.eclipse.core.runtime 3.15.100) | 同 |
| **org.eclipse.core.runtime** | 3.15.100.v20181107-1343 | 同 |
| **org.eclipse.core.commands** | 3.9.200.v20180827-1727 | 同 |
| **org.eclipse.core.databinding** | 1.7.100.v20181030-1443 | **未引** |
| **org.eclipse.core.databinding.property** | 1.6.300.v20180827-2028 | **未引** |
| **org.eclipse.ui** + `ui.workbench` + `ui.ide` + `ui.editors` + `ui.navigator` | 2018-12 套 | 已引（IDE pivot 阶段补齐） |
| **org.eclipse.ui.forms** | 同 | 已引 |
| **Application id** | `org.eclipse.ui.ide.workbench` | 同 (IDE pivot 后) |

**结论**: Eclipse 平台层我们 v0.1 已基本对齐。**唯一缺**: `core.databinding` + `core.databinding.property` —— EMF databound editor 需要，下一步要补。

---

## 3. EMF (核心数据模型层)

参考用的 EMF 全套：

| Bundle | 版本 | 我们引了吗 |
|---|---|---|
| `org.eclipse.emf` | 2.8.0 | ✅ (transitively via Sphinx) |
| `org.eclipse.emf.common` | 2.15.0 | ✅ |
| `org.eclipse.emf.common.ui` | 2.15.0 | ✅ |
| `org.eclipse.emf.ecore` | 2.16.0 | ✅ |
| `org.eclipse.emf.ecore.edit` | 2.11.0 | ✅ |
| `org.eclipse.emf.ecore.xmi` | 2.15.0 | ✅ |
| `org.eclipse.emf.ecore.change` | 2.13.0 | ✅ |
| `org.eclipse.emf.codegen.ecore` | 2.16.0 | ✅ |
| **`org.eclipse.emf.transaction`** | 1.9.1 | ✅ (刚引到 common bundle) |
| **`org.eclipse.emf.transaction.ui`** | 1.4.0 | ❌ **未引** |
| **`org.eclipse.emf.workspace`** | 1.5.1 | ✅ |
| **`org.eclipse.emf.workspace.ui`** | 1.3.0 | ❌ **未引** |
| **`org.eclipse.emf.validation`** | 1.8.0 | ❌ **未引** (validate 走 Python，不是 EMF) |
| `org.eclipse.emf.codegen.ecore.ui` | 2.16.0 | ❌ |
| `org.eclipse.emf.emfstore.common` | 1.9.0 | ❌ |
| `org.eclipse.emf.mwe.core` / `mwe2.runtime` | 1.3.21 / 2.9.1 | ❌ (template engine, 用 jinja2 替代了) |

**结论**: EMF 核心层（Ecore + Transaction + Workspace）我们已有大部分，**缺 `transaction.ui` + `workspace.ui` + `validation`** —— EMF databound editor / 内联 validate 需要。

---

## 4. Sphinx (EMF + Workspace 集成)

参考用 **Sphinx 0.11.2** (2021-08-25 发布)：

| Bundle | 版本 | 我们引了吗 |
|---|---|---|
| `org.eclipse.sphinx.emf` | 0.11.2 | ✅ |
| `org.eclipse.sphinx.emf.editors` | 0.11.2 | ❌ **未引** |
| `org.eclipse.sphinx.emf.editors.forms` | 0.11.2 | ❌ **未引** ⭐ EMF FormEditor 父类在这 |
| `org.eclipse.sphinx.emf.explorer` | **0.9.2** ⚠️ | ❌ 版本错配 (其它 sphinx 都 0.11.2) |
| `org.eclipse.sphinx.emf.ui` | 0.11.2 | ❌ |
| `org.eclipse.sphinx.emf.workspace` | 0.11.2 | ✅ |
| `org.eclipse.sphinx.emf.workspace.ui` | 0.11.2 | ❌ **未引** |
| `org.eclipse.sphinx.emf.validation` | 0.11.2 | ❌ |
| `org.eclipse.sphinx.gmf.workspace` | 0.11.2 | ❌ (我们不用 GMF) |
| `org.eclipse.sphinx.platform.ui` | 0.11.2 | ❌ |

**结论**: 我们只引了 sphinx.emf + sphinx.emf.workspace 两个最底层。**完整 EMF model-driven editor / explorer 需要补 6 个**。
**注意**: `sphinx.emf.explorer` 是 **0.9.2** 不是 0.11.2 ——iSoft 自己包了一份旧的。这是个坑。

---

## 5. Artop AAL (AUTOSAR 元模型)

参考用 **Artop AAL 4.5.2 + autosar448 4.13.1** (2025-09-19 build)：

| Bundle | 版本 | 我们引了吗 |
|---|---|---|
| `org.artop.aal.common` | 4.5.2 | ✅ |
| `org.artop.aal.gautosar` + `.edit` + `.services` | 4.5.2 | ✅ |
| `org.artop.aal.autosar40` + `.converters` + `.services` + `.services.common` + `.validation` + `.validation.ui` | 4.5.2 | ✅ (大部分) |
| `org.artop.aal.autosar448` + `.edit` + `.services` | **4.13.1** | ✅ |
| `org.artop.aal.serialization` + `.converters` + `.workspace` + `.workspace.ui` | 4.5.2 | 部分 |
| `org.artop.aal.validation` + `.validation.ui` | 4.5.2 | 部分 |
| `org.artop.aal.examples.common.ui` + `.editor` | 4.5.2 | ❌ |
| `org.artop.aal.extender` | 4.5.2 | ❌ |
| `org.artop.ecuc.autosar40.initializers` + `.xtend.typesystem` | 4.5.2 | ✅ |
| `org.artop.ecuc.gautosar.initializers` + `.xtend.typesystem` | 4.5.2 | ✅ |
| `org.artop.eel.common` + `.serialization` | 1.0.0 | ✅ |

**结论**: Artop 主力 bundle 我们已有。版本号一致 (4.5.2 / 4.13.1 / 1.0.0)。**缺**: `examples.common.ui` / `editor` (EMF FormEditor 例子，可参考但不必装) / `extender` (运行时扩展机制)。

---

## 6. iSoft 自有 bundles

### 6.1 核心 4 个

| Bundle | 作用 |
|---|---|
| `cn.com.isoft.bswbuilder.common` | 基础工具 + 通用 model 类 |
| `cn.com.isoft.bswbuilder.extensionpoints` | 全部扩展点 schema 定义 |
| `cn.com.isoft.bswbuilder.ui` | UI / Editor / ContentProvider / 右键菜单 |
| `cn.com.isoft.pal` | 平台抽象层 (PAL) — Sphinx 上层封装、project natures、editing domain factory listener |

### 6.2 模块 bundles (59 个！)

```
adc, bswm, can, canif, cannm, cantp, cantrcv, cantsyn, com, comm, crc,
csm-4-4, dcm, dem, det, dio, doip, ea, ecuc, ecum, eeprom, eth, ethif,
ethsm, ethtsyn, fee, fim, flstst, gpt, icu, ipdum, irte, keym, ldcom,
lin, linsm, mcalcrypto, mcaleep, mcalethtrcv, mcalfee, memif, memlayout,
memmap, nm, nvm, os_tc397, port, pwm_mcal, ramtst, sd, secoc, soad,
someiptp, tcpip, tm, udpnm, wdgif, wdgm, xfrm
```

每个模块**独立 OSGi bundle**，注册到 `cn.com.isoft.bswbuilder.extensionpoints.module`。
我们 v0.1 只有 `memif` 一个，跟参考差了 58 个。

### 6.3 其它支持 bundles

- `cn.com.isoft.bswbuilder.parallelmodelmanager 2.4.0` — 多模型并行管理
- `cn.com.isoft.bswbuilder.validation 2.0.5` — 校验框架
- `cn.com.isoft.commandline 2.0.5` + `cn.com.isoft.generator.commandline 2.0.5` — 命令行入口
- `cn.com.isoft.def.editor 4.3.0` — Definition (schema) 编辑器
- `cn.com.isoft.expansion.definition 1.0.0` — schema 扩展机制
- `cn.com.isoft.importers.dbctobsw / fibex / odx / ...` — 各种格式导入器
- `cn.com.isoft.bswbuilder.os.core 1.0.0` + `cn.com.isoft.bswbuilder.utils.os 2.0.5` — OS 工具
- `cn.com.isoft.examples 1.0.0` — 示例工程

---

## 7. 关键架构决策（参考实际形状）

| 维度 | 参考用什么 | 我们 v0.1 用什么 | 切到一致需要什么 |
|---|---|---|---|
| **Host 应用** | Eclipse IDE (`org.eclipse.ui.ide.workbench` application) | 同（IDE pivot phase 1+2 已切）| ✅ |
| **数据模型** | EMF EObject (typed 模型，从 .arxml 加载) | java.io.File path + String 字段 | ❌ 这是核心差距 |
| **持久化** | Sphinx ResourceSet.save (XMI 序列化) | `MemIfArxmlWriter` 字符串外科 | 🟡 hybrid 折中 |
| **编辑器** | `Sphinx AbstractFormPage` extends `FormEditor` + EMF databinding | 自撸 SWT widget + 字符串值 | ❌ |
| **Project Explorer** | `BswExplorerContentProvider extends BasicExplorerContentProvider` (Sphinx EMF 模型遍历) | `IPipelinedTreeContentProvider2` 拦截 IFile | 🟡 路线差 |
| **Editing domain** | Sphinx `ITransactionalEditingDomainFactoryListener` + per-metamodel pattern | 已注册 no-op listener (修了 NPE) | 部分 |
| **模块插件机制** | 每模块独立 OSGi bundle 注册到 `extensionpoints.module` | 同（架构对了）| ✅ |
| **生成器/验证器** | 自带 `cn.com.isoft.commandline` Java 生成器 + Xtend templates | Python `bswgen` / `bswval` (CLI 子进程) | 🟢 v0.1 algorithm 层独立可保留 |
| **Project nature** | `cn.com.isoft.workspace.bswbuildernature` + `org.artop.aal.workspace.autosarnature` | 用户手动加 .project (无 nature) | ❌ |
| **Form 颜色** | `decorateFormHeading` + Verdana 15 + RGB(33,33,33) | 同 (F2 已对齐) | ✅ |
| **菜单结构** | navigatorContent + actionProvider | popup:any + visibleWhen 路径过滤 | 🟡 简化版 |

---

## 8. 我们 v0.1 现状 vs 参考的差距清单

### ✅ 已对齐

1. Eclipse 2018-12 + Java 8
2. Eclipse IDE workbench (application id)
3. Artop AAL 4.5.2 / autosar448 4.13.1 主力 bundle
4. Sphinx EditingDomain factory listener 注册（pattern 一致）
5. 模块插件 extension point 机制
6. 5 项扁平右键菜单
7. Form 颜色 / 字体 / 前景色

### ❌ 未对齐（按重要性排）

1. **数据模型路线**: file-system path String → 应切 EMF EObject typed
2. **缺 6 个 Sphinx UI bundle**: `emf.editors` / `emf.editors.forms` / `emf.ui` / `emf.workspace.ui` / `platform.ui` / `emf.explorer`
3. **缺 EMF databinding**: `core.databinding` + `core.databinding.property`
4. **缺 EMF transaction.ui + workspace.ui + validation**
5. **缺 Project nature**: BSW workspace 应该自动加上 `autosarnature`，让 Sphinx 识别
6. **navigatorContent 路线**: 我们用 IFile-based pipelining → 应切 EMF EObject-based
7. **Editor 路线**: 自撸 SWT → 应切 Sphinx AbstractFormPage + EMF databinding
8. **生成器**: Python 子进程 → 长远应切 Xtend (但 v0.1 algorithm 84/84 PASS 是资产，保留也行)
9. **缺 commandline / def.editor / importers / validation 等扩展功能**
10. **JVM 启动参数**: heap / GC / stack 都比参考小

### 🟡 折中

- 生成器/验证器: Python 现状 84/84 PASS 是已验证资产，**继续保留**比切 Xtend 划算（algorithm 层 vs UI 层独立解耦）

---

## 9. 现在该问的决策

要把 v0.1 切到跟参考完全一致的架构，必须先决定：

**Q1**: hybrid 还是全 EMF？
- **hybrid**: load EMF / write 字符串外科 — Phase F byte-equal 保住，UI 红利大部分拿到
- **全 EMF**: load + save 都 EMF — Phase F 大概率挂，Refactor / Compare / Search 全套都能用

**Q2**: Phase F byte-equal 这条 v0.1 验收线，v0.2+ 是否继续要？
- 要 → 必须 hybrid
- 不要 → 全 EMF (商业 IDE 通常只要语义等价)

**Q3**: Algorithm 层 (generator / validator) 切 Xtend 还是保留 Python？
- 切 Xtend: 跟参考一致，UI 内联调用，无子进程
- 保留 Python: 84/84 PASS 是资产，独立解耦，跟模块 EMF model 解耦反而健康

**Q4**: 多模块 (Det/NvM/Ea/Fee/...) 接入策略？
- 一次性把 59 个模块 bundle 都搞起来 → 工作量极大
- 渐进 (先 Det/NvM 这两个 v0.1 algorithm 已支持的) → 务实

---

## 10. 推荐

**最务实路径**:
1. **Sphinx UI bundles 全引齐**（缺的 6 个 + databinding）→ 0.5 天
2. **Project nature 加上 + auto-add**（用户导入 BSW workspace 时自动加 autosarnature）→ 0.5 天
3. **MemIfArxmlReader 切 EMF**（Sphinx ResourceSet.load → EObject）→ 1 天
4. **MemIfModuleManagerEditor 切 Sphinx AbstractFormPage**（EMF databinding）→ 2 天
5. **BswExplorerContentProvider 切 Sphinx BasicExplorerContentProvider**（EMF model 遍历）→ 1 天
6. **Save 决策**：测 EMF save，挂了 fallback 到字符串外科 hybrid → 1 天
7. **加 Det / NvM 两个模块**作为多模块验证 → 2 天
8. JVM ini 调到参考一致 (`-Xms512m -Xmx2048m -Xss2m`) → 5 分钟
9. 跑测试 + Phase F + GUI 验 → 1 天

**总 9-10 天**（不含撞坑迭代）

不切的代价: v0.2 加每个模块 ~500 行 hand-code，4 模块 = 2000 行，长远超过切的成本。

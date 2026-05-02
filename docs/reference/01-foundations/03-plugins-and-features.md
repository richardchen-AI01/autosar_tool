# 04 · Plugin / Feature / p2 架构

ORIENTAIS Configurator 本质是一个**定制化的 Eclipse RCP 产品**, 所有功能都装在
OSGi bundle(以 `.jar` 形式存在于 `plugins/`)里。本章讲清楚:

- bundle 的组织方式与分组
- 功能怎么通过 feature 聚合
- 安装/升级走的 p2 机制
- `patch.xml` 和 `artifacts.xml` 各承担什么角色

---

## 1. 总览

| 目录 | 条目数 | 大小 | 作用 |
|---|---|---|---|
| `plugins/` | 396 个 jar | 269 MB | OSGi bundle 仓库(运行时加载) |
| `features/` | 5 个 | 263 KB | 特性分组描述 |
| `p2/` | 2 个引擎目录 | 906 KB | Equinox p2 provisioning 状态 |
| `configuration/org.eclipse.equinox.simpleconfigurator/bundles.info` | — | 64 KB | **启动时需激活的 bundle 显式清单** |
| `patch.xml`(根目录) | — | 9.8 KB | 本次交付**全部 ISOFT bundle 版本清单** |
| `artifacts.xml`(根目录) | — | 93 KB | p2 制品哈希/大小清单 |

---

## 2. plugins/ — bundle 仓库

### 2.1 按 vendor 分组(按数量降序)

| 前缀 | 数量 | 性质 |
|---|---|---|
| `cn.com.isoft.*` | 121 | **iSoft 自有业务代码**(本产品核心) |
| `org.eclipse.equinox.*` | 34 | OSGi 运行时、应用模型、simple configurator |
| `org.eclipse.emf.*` | 23 | EMF 建模框架 |
| `org.artop.aal.*` | 22 | ARTOP AUTOSAR Abstraction Layer |
| `org.eclipse.e4.*` | 21 | Eclipse 4 应用模型、CSS 主题 |
| `org.eclipse.ui.*` | 14 | IDE 基础 UI |
| `org.eclipse.sphinx.*` | 13 | Sphinx EMF 工具链(ARTOP 上层) |
| `org.eclipse.core.*` | 13 | Core 运行时、Jobs、资源模型 |
| `org.eclipse.wst.*` | 11 | WST XML 工具 |
| `org.eclipse.gmf.*` | 11 | GMF 图形化建模 |
| `org.apache.batik.*` | 9 | SVG 渲染 |
| `org.apache.commons.*` | 7 | 常用工具库 |
| `org.eclipse.jetty.*` | 6 | 内嵌 HTTP server |
| `org.eclipse.osgi.*` | 5 | OSGi framework 与扩展 |
| `org.eclipse.nebula.*` | 5 | 高级 SWT 控件(如 grid, nattable) |
| 其他 | ~80 | JFace / EMF Transaction / SWT / Batik Util / … |

### 2.2 ISOFT bundle 家族树

121 个 `cn.com.isoft.*` bundle 大致可分 5 族:

```
cn.com.isoft.
├── pal.*                              ← Platform Abstraction Layer
│   ├── pal                               UI 层(AUTOSAR Navigator 等)
│   ├── pal.base.common                   跨模块通用
│   ├── pal.cgenerator                    C 代码生成器(集成式)
│   ├── pal.doggle                        ★ Sentinel dongle JNI 桥(授权)
│   ├── pal.feedback                      用户反馈/日志
│   ├── pal.graphics                      绘图支持
│   ├── pal.librarymanager                库依赖管理
│   └── pal.rte.common                    RTE 层共享代码
├── mal.*                              ← Module Abstraction Layer
│   ├── mal                               基础
│   ├── mal.exceptions                    异常体系
│   ├── mal.licm                          license 管理
│   ├── mal.model                         模型定义(EMF 生成)
│   ├── mal.modelutils                    模型工具(constants, utils)
│   └── mal.validation                    通用校验框架
├── bswbuilder.*                       ← BSW 配置器(核心)
│   ├── bswbuilder.common                 框架公共
│   ├── bswbuilder.extensionpoints        扩展点定义
│   ├── bswbuilder.librarymanager         BSW 库管理
│   ├── bswbuilder.mcus.infineon          ★ 产品品牌 bundle
│   ├── bswbuilder.os.core                OS 基础
│   ├── bswbuilder.parallelmodelmanager   并行模型
│   ├── bswbuilder.ui                     ★ 所有配置编辑器 UI(最大, 1028 class)
│   ├── bswbuilder.utils.os               OS 工具
│   ├── bswbuilder.validation             配置校验
│   └── bswbuilder.modules.<XX>           每个 BSW 模块一个(~55 个)
│       ├── os_tc397 / os / osal          操作系统
│       ├── com / comm / ipdum / xfrm      通信栈
│       ├── canif / can / cantp / …        CAN stack
│       ├── ethif / eth / tcpip / doip …   Ethernet stack
│       ├── linif / lin / linsm / udpnm    LIN/UDP NM
│       ├── mem* / fee / ea / eeprom / fls 存储栈
│       ├── crypto / csm / cryif / keym    安全栈
│       ├── dem / det / dlt / fim          诊断
│       ├── dcm / doip                     UDS 诊断
│       ├── nvm / memif / memmap / ramtst  存储/运行时测试
│       ├── wdg / wdgm / wdgif             看门狗
│       ├── bswm / ecum / comm / nm        服务
│       ├── adc/dio/gpt/icu/pwm/spi/port   MCAL
│       ├── xcp / stbm / sd / secoc        其他
│       └── …
├── rtebuilder.*                       ← RTE 生成器
│   ├── rtebuilder.generator
│   ├── rtebuilder.modules.rte
│   ├── rtebuilder.ui
│   └── rtebuilder.validator
├── def.editor*                        ← ARXML 定义编辑器
│   ├── def.editor
│   └── def.editor.common.ui
├── importers.*                        ← 导入器
│   ├── importers.deftolib
│   └── importers.systemsignalmappingfibex  (FIBEX 网络描述)
├── commandline.*                      ← CLI 入口
│   ├── commandline
│   └── commandline.common
├── examples                           ← 示例工程
├── expansion.definition               ← 工具栏/命令扩展点
├── generator.commandline              ← CLI 代码生成接入
└── cn.com.cetc.isoft.val(.rules)      ← 独立的安全/合规校验插件(CETC 系出品)
```

### 2.3 bundle 版本规律

- 绝大多数 ISOFT bundle 版本号为 `2.0.5.202601300910`
  - 语义版本 `2.0.5`
  - 构建限定符 `202601300910` = 构建时间 2026-01-30 09:10
- 少数 bundle 停留在早期版本:
  - `1.0.0.*`: `expansion.definition`、`bswbuilder.os.core`、`examples`、
    `importers.systemsignalmappingfibex` 的老版本、`mal.model`、`cetc.isoft.val(.rules)`、
    `bswbuilder.modules.fr`、`bswbuilder.modules.ramtst`、`bswbuilder.modules.flstst`
  - `2.0.1.*`: `pal.cgenerator`(比主线稍旧)
  - `2.4.0.*`: `bswbuilder.parallelmodelmanager`(更激进)
  - `4.3.0.*`: `def.editor(.common.ui)`(独立演进的定义编辑器)

---

## 3. features/ — 特性目录

5 个 feature, 每个就是一个"功能集合"的逻辑分组, 供 p2 提供升级/回滚粒度。

| 目录 | label | provider | 绑定 plugin 数 | 说明 |
|---|---|---|---|---|
| `cn.com.isoft.addition.feature` | Feature | (未填) | 0 | 扩展插件占位 |
| `cn.com.isoft.artop.feature` | Artop Feature | iSoft | 0 | ARTOP 核心 |
| `cn.com.isoft.common.feature` | Feature | iSoft | 0 | 通用 |
| `cn.com.isoft.rte.feature` | Feature | (未填) | 0 | RTE |
| `cn.com.isoft.variable.feature` | Feature | (未填) | **79** | **本次实际承载所有 ISOFT 业务 bundle 的特性** |

**注意**: 前 4 个 feature 的 `feature.xml` 只有 label/description 占位, **未列出任何 plugin**;
真正的 plugin → feature 绑定全部集中在 `variable.feature`。这是一种"单一 feature 总装"的打包风格,
对使用者没有负面影响, 但升级时无法做子模块级粒度回滚。

每个 feature 目录结构相同:

```
features/<id>_<version>/
├── feature.xml          特性描述(id/label/version/provider + <plugin>... 列表)
└── META-INF/            feature 自己的签名/清单(若有)
```

---

## 4. patch.xml — 本次交付的 ISOFT bundle 全清单

根目录下, XML 格式, 仅含 `<original>` 段, 列出本包中所有 **`cn.com.isoft.*`** 的 plugin 名与版本号。

用途:

- **升级对照表**: `isoft_upgrader` (见 07) 检查现有安装是否需要打 patch
- **审计清单**: 验证客户手里交付包是否完整
- **依赖锁定**: 人工对比 `plugins/` 目录文件名, 不一致立刻能发现

节选:

```xml
<patchs>
  <original>
    <plugin name="cn.com.isoft.bswbuilder.common"         version="2.0.5.202601300910"/>
    <plugin name="cn.com.isoft.bswbuilder.extensionpoints" version="2.0.5.202601300910"/>
    ...
    <plugin name="cn.com.isoft.pal"                       version="2.0.5.202601300910"/>
    <plugin name="cn.com.isoft.pal.doggle"                version="2.0.5.202601300910"/>
    ...
  </original>
</patchs>
```

---

## 5. artifacts.xml — p2 制品清单

p2 provisioning 的"仓库索引", 93 KB, 列出每个 artifact(bundle/feature)的:

- 标识符与版本号
- 文件大小
- SHA-1 / MD5 哈希
- 压缩参数

Eclipse update manager 用它来确认下载/安装结果是否正确。本地安装场景下这个文件**很少被直接读**,
但一旦配合 p2 director 做远程更新就会发挥作用。

---

## 6. p2/ — Provisioning 引擎状态

```
p2/
├── org.eclipse.equinox.p2.core/
│   └── cache/
│       └── binary/          ← 已下载的二进制缓存(通常为空或极小)
└── org.eclipse.equinox.p2.engine/
    ├── .settings/
    └── profileRegistry/
        └── DefaultProfile.profile/
            └── *.profile.xml  ← 当前 profile 快照(已安装 IU 的完整状态)
```

作用:

- **记住**: 当前安装了哪些 IU (Installable Unit, 约等于 feature+bundle)
- **支持 rollback**: profile 会按时间戳保留多个版本, 可回到历史状态
- **升级判断**: `director` 比对远程 repo 和本地 profile 决定要装什么

**可安全清空的时机**: 仅在"完全重装/重建 provisioning"场景下, 且伴随删除
`configuration/org.eclipse.osgi/` 缓存; 平时**不要动**。

---

## 7. configuration/org.eclipse.equinox.simpleconfigurator/bundles.info

**启动时实际生效的 bundle 列表**, 由 simpleconfigurator 读取。每行一个 bundle:

```
<symbolic-name>,<version>,<path-or-url>,<start-level>,<autostart>
```

`bundles.info` 是**运行期权威**: 如果 `plugins/` 里有 jar 但这里没登记, 不会被加载;
反之如果这里登记了但 `plugins/` 里缺文件, 启动就报错。

因此**要让一个新 bundle 生效**有两种方式:
1. 放 jar 到 `plugins/` 然后运行带 `-clean` 的启动 — Equinox 会重扫
2. 手动编辑 `bundles.info` 加一行(需要确切的 start-level 值)

---

## 8. 排错速查

| 现象 | 定位 |
|---|---|
| 启动提示 `bundle not resolved` | `configuration/<timestamp>.log` 会指出缺哪个依赖; 对比 `plugins/` 目录 |
| 新装的 plugin 看不到菜单 | 先检查是否出现在 `bundles.info`; 未出现执行 `-clean -refresh` |
| 加密 plugin 报 `ClassFormatError` | `decrypt.dll` 未加载(检查 `.ini` 的 `-agentlib:decrypt`) |
| `patch.xml` 和 `plugins/` 不一致 | 升级/卸载过程中断 → 重走 `isoft_upgrader` 或者重装 |
| p2 profile 损坏 | 删除 `p2/` + `configuration/org.eclipse.osgi/`, 再启动时 Equinox 会用 `bundles.info` 重建 |

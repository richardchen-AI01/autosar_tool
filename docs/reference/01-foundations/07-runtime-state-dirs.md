# 08 · 运行期状态目录 (workspace / configuration / p2)

有三类目录在产品**首次启动后**会被自动填充或扩大。它们不是"源代码"而是"运行状态",
理解它们有助于做清理、排错、迁移工作区。

```
workspace/                       用户数据(工程) + Eclipse workspace 元数据
configuration/org.eclipse.osgi/  OSGi bundle 解压缓存 (最大, ~81 MB)
configuration/org.eclipse.<*>/   各 Equinox 子系统的运行时状态
p2/                              Provisioning profile 与 cache
```

---

## 1. workspace/ — 用户工作空间 (~78 MB)

Eclipse IDE 的 **workspace 目录** — 用户的工程、偏好、视图布局都在这里。

### 1.1 结构

```
workspace/
├── .metadata/                           ← Eclipse 自己的元数据
│   └── .plugins/
│       ├── org.eclipse.core.resources/     项目索引
│       ├── org.eclipse.core.runtime/       运行时状态
│       ├── org.eclipse.e4.workbench/       窗口/视图布局
│       ├── org.eclipse.ui.ide/             IDE 偏好
│       ├── org.eclipse.emf.common.ui/      EMF UI 状态
│       ├── org.eclipse.sphinx.emf.validation.ui/
│       └── org.artop.aal.workspace.ui/     ARTOP workspace 状态
├── Demo_S32K148_V2510_S32DS_V3p5_Project/  (示例工程, NXP S32K148)
│   ├── .settings/                         Eclipse 工程设置
│   ├── ASW/                                应用软件
│   ├── BSW/                                基础软件配置
│   ├── LinkFile/                           链接脚本
│   └── Main/                               主程序
├── s32k148_bsw/                          (S32K148 BSW 配置工程)
│   ├── .settings/
│   ├── BSW_Builder/
│   └── ServiceComponents/
└── 开源小满S32K148示例工程说明.pdf        示例配套说明 (1.7 MB)
```

### 1.2 关键文件

- `.metadata/.log` — Eclipse 的 error log, 启动/运行异常首先看它
- `.metadata/.plugins/org.eclipse.e4.workbench/workbench.xmi` — 窗口布局
- `.metadata/.plugins/org.eclipse.core.resources/.projects/` — 每个工程的索引快照

### 1.3 何时可以删

| 场景 | 动作 |
|---|---|
| "UI 布局乱了想恢复默认" | 删 `workspace/.metadata/.plugins/org.eclipse.e4.workbench/` |
| "ERROR log 太大" | 删 `workspace/.metadata/.log` (自动重建) |
| "想完全重置 workspace" | 删整个 `workspace/` 重启时会自动重建空 workspace |
| "只换 workspace 不动状态" | 启动时带 `-data X:\other_ws` |

**⚠️ 不要一边运行 ORIENTAIS 一边删 `.metadata`** — 会导致 workspace 损坏到无法启动。

### 1.4 示例工程的位置问题

- 两个 Demo 工程**直接放在 workspace 下**, 相当于"工厂预设"
- 客户上手后, 通常会把工程移到别的目录并用 `File > Import` 重新导入, 以避免卸载时误删

---

## 2. configuration/ 的运行时部分

(静态部分 config.ini/PuHuaLicense.lic/osinfo/os_projects 已在 02/03/06 章讨论)

### 2.1 `configuration/org.eclipse.osgi/` (~81 MB 最大)

**OSGi framework 的 bundle cache**。Equinox 会把 `plugins/` 下的 jar 解压、索引、生成 pack, 存到这里加速后续启动。目录结构:

```
configuration/org.eclipse.osgi/
├── 11/       ┐
├── 12/       │  每个数字子目录 = 一个 bundle 的 cache
├── 112/      │  目录名 = bundle 在 framework 里的 ID
├── 117/      │  内容 = 解压的 class、资源、.cp (classpath 描述)
├── 118/      │
├── …        ┘
└── .state   framework 状态持久化
```

**可以清空**: `rm -rf configuration/org.eclipse.osgi/` 后启动加 `-clean` — Equinox 会重建。
常用于 "新装了 plugin 但不生效" 的情况。

**清空代价**: 下次启动慢 20~60 秒(要重新解压 396 个 jar)。

### 2.2 `configuration/org.eclipse.core.runtime/` (1.2 MB)

Runtime 子系统的内部状态(registry 缓存、preferences 持久化)。
一般**无需手动触碰**, 只在极端排错时才清。

### 2.3 `configuration/org.eclipse.equinox.launcher/` (704 KB)

原生启动器的工作目录 — 包含启动日志、快照等。可删。

### 2.4 `configuration/org.eclipse.equinox.app/` (32 KB)

Equinox 的 application 注册状态 — 记录哪些 Application 被声明、哪个是默认。

### 2.5 `configuration/org.eclipse.update/` (44 KB)

老的 update 机制历史记录(`history/<timestamp>.xml`), 每次装卸 plugin 都追加一条。
新机制走 p2(见下), 但这里仍然保留兼容记录。

### 2.6 `configuration/org.eclipse.e4.ui.css.swt.theme/` (16 KB)

E4 CSS 主题缓存 — 主题(浅色/深色/自定义)切换时的样式索引。

### 2.7 `configuration/org.eclipse.equinox.simpleconfigurator/` (64 KB)

这里有启动最关键的 `bundles.info`(详见 [03-plugins-and-features.md](03-plugins-and-features.md) 第 7 节)。
**绝对不要手工改**, 修改得不对整个 framework 起不来。

### 2.8 `configuration/org.eclipse.equinox.source/` (17 KB)

source bundle 索引(已安装的源码 bundle 列表)。ORIENTAIS 没发布源码, 这个基本是空的。

---

## 3. p2/ — Equinox Provisioning 状态 (906 KB)

```
p2/
├── org.eclipse.equinox.p2.core/
│   └── cache/
│       └── binary/                ← 已下载的 binary artifact 缓存
└── org.eclipse.equinox.p2.engine/
    ├── .settings/
    └── profileRegistry/
        └── DefaultProfile.profile/
            └── *.profile.xml      ← 当前 profile 快照, 按时间戳多份历史
```

### 3.1 核心概念

- **Profile**: 当前安装状态的完整快照, 记录所有 IU(Installable Unit)
- **IU**: 可安装单元 = feature 或 bundle + 元数据
- **Touchpoint**: 安装动作(copy, addRepository, ...)的抽象

### 3.2 profileRegistry 里的历史快照

每次 p2 修改安装状态(装插件、回滚、升级), 都会在 `DefaultProfile.profile/`
新增一份以时间戳命名的 `<timestamp>.profile.gz` 或 `*.profile.xml`, 方便回退。

### 3.3 何时需要清

- **无法在线更新**: 清 `p2/org.eclipse.equinox.p2.core/cache/` 后重试
- **profile 损坏导致启动失败**: 完全删 `p2/` + `configuration/org.eclipse.osgi/`,
  启动时 Equinox 会根据 `configuration/org.eclipse.equinox.simpleconfigurator/bundles.info`
  重建最小 profile
- 清理时间戳很多的 profile 历史: 删 profileRegistry 下旧时间戳文件即可

---

## 4. 三者关系

```
plugins/        ← 静态源("有哪些 bundle 可用")
features/       ← 静态特性描述
    │
    ├──► configuration/org.eclipse.equinox.simpleconfigurator/bundles.info
    │      ("启动时要激活哪些")
    │            │
    │            ▼
    │   configuration/org.eclipse.osgi/
    │      (启动后解压缓存)
    │
    └──► p2/
           (完整安装状态, 用于升级回滚)

workspace/      ← 用户数据(独立于上面)
```

---

## 5. 清理策略速查

| 我想... | 动作 |
|---|---|
| 只重置 UI 布局 | 删 `workspace/.metadata/.plugins/org.eclipse.e4.workbench/` |
| 重置 IDE 状态但保留工程 | 删 `workspace/.metadata/` 整个目录 |
| 让新装的 plugin 生效 | 启动时加 `-clean` |
| 启动变慢了, 怀疑缓存坏 | 删 `configuration/org.eclipse.osgi/`, 启动自动重建 |
| 卸载重装前备份 | 打包保存 `workspace/` 和 `configuration/PuHuaLicense.lic` |
| 减小占用(不用了) | 删 `workspace/.metadata/`, `configuration/org.eclipse.osgi/`, `p2/` (~260 MB) |

---

## 6. 排错速查

| 现象 | 首选定位 |
|---|---|
| 启动黑屏或闪退 | `workspace/.metadata/.log` + `configuration/<timestamp>.log` |
| 菜单消失/视图找不到 | `workbench.xmi` 损坏 → 删后重启 |
| 工程报错 "Project is missing .project" | `workspace/.metadata/.plugins/org.eclipse.core.resources/.projects/<name>/` 损坏 → 从备份恢复或用 Import Existing Projects 重新关联 |
| 升级后部分 plugin 不加载 | `-clean` 重启; 仍不行则删 `p2/` + 加 `-clean` |
| 同时两个 ORIENTAIS 进程冲突 | workspace 存在 lock: `workspace/.metadata/.lock` — 一次只允许一个实例 |

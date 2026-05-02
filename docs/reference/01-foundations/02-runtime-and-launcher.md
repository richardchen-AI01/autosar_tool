# 02 · 启动器 & 运行时

本章聚焦**从双击图标到 workbench 出现之间**发生的一切: 原生启动器、JVM 参数、
OSGi bootstrap、内嵌 JRE。

---

## 1. 启动链路一图

```
用户双击 ORIENTAIS_Configurator_for_EasyXMen_V25.10.exe
                │
                ▼
 ① exe 解析同名 .ini, 读取 -vm / -vmargs / -startup / --launcher.library
                │
                ▼
 ② 加载 plugins/org.eclipse.equinox.launcher.win32.win32.x86_64_*/eclipse_*.dll
                │
                ▼
 ③ 启动 jre/bin/javaw.exe, 按 .ini 所列 -vmargs 组装 JVM 参数
                │   其中 -agentlib:decrypt 触发 jre/bin/decrypt.dll 加载 (见 03)
                ▼
 ④ 以 org.eclipse.equinox.launcher.Main 为主类, 加载 org.eclipse.osgi 作为 OSGi 框架
                │
                ▼
 ⑤ Equinox 读 configuration/config.ini, 解析 eclipse.product
                │
                ▼
 ⑥ 按 configuration/org.eclipse.equinox.simpleconfigurator/bundles.info 启动所有 bundle
                │
                ▼
 ⑦ 显示 splash.bmp(来自品牌 bundle) → 进度条推进
                │
                ▼
 ⑧ 启动 org.eclipse.ui.ide.workbench → 主界面出来
```

命令行入口(`ISOFT.cmd`)直接跳到 ③, 并改用 `EcuWorxCommandLine` 作为 Application,
不启动 workbench, 仅执行 `-generate` 等批处理动作。

---

## 2. 原生启动器 — `ORIENTAIS_Configurator_for_EasyXMen_V25.10.exe`

- 类型: PE32+ GUI, Windows x64, 2.18 MB
- 身份: **Eclipse 原生 launcher 的定制重签名版本**
- 同目录必须有同名的 `.ini`, 这是 Eclipse launcher 的硬约定
- 资源段(Resource Hacker 可查): 图标、版本号、File Description
- 依赖: `plugins/org.eclipse.equinox.launcher.win32.win32.x86_64_1.1.900.v20180922-1751/eclipse_1801.dll`(就地平台启动代码)

**可选参数**(写在 `.ini` 的 `-vmargs` 之前):

| 参数 | 作用 |
|---|---|
| `-clean` | 清空 `configuration/org.eclipse.osgi` 缓存, 强制重建 bundle index |
| `-refresh` | 扫描新 plugin |
| `-data <path>` | 指定 workspace, 不走默认 `./workspace/` |
| `-console` | 开 OSGi 控制台(排错时很有用) |
| `-debug` | 输出启动调试日志 |

---

## 3. JVM 启动参数 — `ORIENTAIS_Configurator_for_EasyXMen_V25.10.ini`

原版内容(按行传给 Eclipse launcher):

```
-startup
plugins/org.eclipse.equinox.launcher_1.5.200.v20180922-1751.jar
--launcher.library
plugins/org.eclipse.equinox.launcher.win32.win32.x86_64_1.1.900.v20180922-1751
--launcher.XXMaxPermSize
256m
-vm
./jre/bin/javaw.exe
-vmargs
-Dosgi.requiredJavaVersion=1.8
-Xms512m
-Xmx2048m
-Xss2m
-XX:+UseParallelGC
-Xverify:none
-agentlib:decrypt
```

逐行解释:

| 行 | 作用 |
|---|---|
| `-startup …launcher_*.jar` | OSGi 引导 jar |
| `--launcher.library …win32.x86_64_…` | 原生启动器目录 |
| `--launcher.XXMaxPermSize 256m` | Eclipse 兼容参数(Java 8 以上忽略) |
| `-vm ./jre/bin/javaw.exe` | **强制使用内嵌 JRE**, 不用系统 Java |
| `-Dosgi.requiredJavaVersion=1.8` | OSGi 自检 Java 版本 |
| `-Xms512m` / `-Xmx2048m` | JVM 堆 512M 起步, 最大 2G |
| `-Xss2m` | 线程栈 2M |
| `-XX:+UseParallelGC` | 并行 GC(Java 8 桌面应用常见) |
| `-Xverify:none` | **禁用字节码校验** — 是 `decrypt.dll` 正常工作的前提之一 |
| `-agentlib:decrypt` | 加载 `jre/bin/decrypt.dll` 作为 JVMTI agent(见 03) |

---

## 4. 命令行入口 — `ISOFT.cmd`

面向自动化/CI 场景, 调用内置命令行 Application:

```bat
SET CLASSPATH="%BSW_BASE%plugins\org.eclipse.equinox.launcher_1.5.200.v20180922-1751.jar"
SET APPLICATION=cn.com.isoft.commandline.EcuWorxCommandLine
SET VMARGS=-Dosgi.requiredJavaVersion=1.7 -Xms128m -Xmx768m -Xss4m -agentlib:decrypt
SET LAUNCHER=org.eclipse.equinox.launcher.Main
SET CMD="%JAVA%" %VMARGS% -classpath %CLASSPATH% %LAUNCHER% -application %APPLICATION% %*
call %CMD%
```

要点:

- 与 GUI 的唯一共性是**同一个 agent `-agentlib:decrypt`**
- Application 换成 `cn.com.isoft.commandline.EcuWorxCommandLine`, 由 `cn.com.isoft.commandline*` bundle 提供
- 目前只接受 `-generate` 一个合法顶层命令; 其他入参直接拒绝
- 堆 128~768M, 比 GUI 小得多

典型用法(Win10 命令行):

```cmd
cd /d D:\ORIENTAIS_Studio\ORIENTAIS_Configurator_for_EasyXMen_V25.10
ISOFT.cmd -generate -project <工程路径> -module <模块名>
```

---

## 5. OSGi bootstrap 配置 — `configuration/`

启动相关的几个核心文件:

| 文件 | 作用 |
|---|---|
| `configuration/config.ini` | OSGi 根配置: 指向 product、splash、p2 数据区、启动 bundle |
| `configuration/org.eclipse.equinox.simpleconfigurator/bundles.info` | **显式列出需启动的所有 bundle**(含版本/启动级别) |
| `configuration/org.eclipse.update/platform.xml` | 安装的 feature 列表(兼容老机制) |
| `configuration/org.eclipse.equinox.launcher/` | 原生启动器工作目录 |

`config.ini` 关键字段(这次交付的值):

```ini
osgi.framework               = plugins/org.eclipse.osgi_3.15.100.v20191114-1701.jar
osgi.bundles                 = reference:file:…simpleconfigurator_1.3.200.jar@1:start
osgi.bundles.defaultStartLevel = 4
osgi.framework.extensions    = …osgi.compatibility.state_1.1.300.jar
osgi.splashPath              = platform:/base/plugins/cn.com.isoft.bswbuilder.mcus.infineon
eclipse.product              = cn.com.isoft.bswbuilder.mcus.infineon.product
eclipse.application          = org.eclipse.ui.ide.workbench
eclipse.p2.profile           = DefaultProfile
eclipse.p2.data.area         = @config.dir/../p2
org.eclipse.update.reconcile = false
```

---

## 6. 内嵌 JRE — `jre/`

| 项目 | 值 |
|---|---|
| 版本 | Oracle Java **1.8.0_221-b11** |
| HotSpot | 25.221-b11, 64-Bit Server VM |
| 架构 | windows-amd64 |
| 构建时间 | 2019-07-04 |
| 占用 | ~216 MB |

**为什么选择这个版本**:

1. Eclipse Equinox/Sphinx 要求 Java 8(后续的 module system 会破坏 OSGi 反射)
2. 最后一个免费授权的 Oracle Java 8 update
3. 自带 JavaFX / Web Start / Applet(虽然 ORIENTAIS 不用)

**关键 native 组件**(jre/bin/):

| DLL | 作用 |
|---|---|
| `java.dll` / `javaw.exe` | JVM 入口 |
| `decrypt.dll` | **自研 JVMTI agent, 解密加密 class**(详见 03) |
| `jvm.dll`(server/) | HotSpot 核心 |
| `awt.dll` / `jfxmedia.dll` / `glass.dll` | GUI/多媒体支持 |

**不要升级 JRE** — 因为 `decrypt.dll` 依赖 Java 8 的 JVMTI 接口和对齐方式,
换到 Java 9+ 会立即失效。

---

## 7. 修改启动行为的几个切入点

| 需求 | 改哪里 |
|---|---|
| 加大内存(处理大工程) | `.ini` 的 `-Xmx2048m` → `-Xmx4096m` |
| 切 G1 GC | `.ini` 的 `-XX:+UseParallelGC` → `-XX:+UseG1GC` |
| 开 OSGi 控制台排错 | 启动时加 `-console -consoleLog`(命令行启动) |
| 指定 workspace | `ORIENTAIS_Configurator_*.exe -data X:\my_ws` |
| 排除 JRE 校验(临时) | 去掉 `-Xverify:none` 会导致加密 class 报 `VerifyError` |
| 临时关掉加密 agent | 去掉 `-agentlib:decrypt` → 启动失败(加密 class 过不了 ClassFileFormatError) |

---

## 8. 启动故障排查速查

| 现象 | 可能原因 |
|---|---|
| 启动闪一下退出 | `.ini` 里 `-vm` 路径错误 → 查 `jre/bin/javaw.exe` 存不存在 |
| `Java was started but returned exit code=1` | 内存不够或 agent 加载失败 → 去 `ORIENTAIS_*.exe -consoleLog` 看堆栈 |
| splash 出现但卡住 | bundle 启动异常 → `configuration/<timestamp>.log` 有详细栈 |
| `No Application ID has been found` | `config.ini` 的 `eclipse.application` 被改坏 |
| About 对话框版本号对不上 | 产品 bundle 被替换但 `aboutText` 未更新 |

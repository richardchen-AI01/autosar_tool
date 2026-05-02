# 01 · 产品身份 & 品牌资产

本章回答「这是什么产品、它的版本号写在哪里、图标/启动画面/"关于"对话框从哪里取的」
这一类"身份识别"问题。所有品牌资产**集中在一个 OSGi bundle 里**, 结构很清晰。

---

## 1. 产品 ID(OSGi 侧身份)

```
configuration/config.ini
  └─ eclipse.product = cn.com.isoft.bswbuilder.mcus.infineon.product
```

这一行告诉 Eclipse Runtime: 启动时以 **`cn.com.isoft.bswbuilder.mcus.infineon`** 这个
bundle 贡献的 `org.eclipse.core.runtime.products` 扩展点作为产品定义。
换句话说, **从这里起, 整个 IDE 的身份和外观都由那个 bundle 决定**。

---

## 2. 品牌 Bundle — `cn.com.isoft.bswbuilder.mcus.infineon`

完整路径:
```
plugins/cn.com.isoft.bswbuilder.mcus.infineon_2.0.5.202601300910.jar
```

内部清单(共 21 个条目,708 KB):

| 内部路径 | 作用 |
|---|---|
| `META-INF/MANIFEST.MF` | OSGi bundle 清单(名字、版本、依赖、构建 JDK) |
| `META-INF/maven/cn.com.isoft/cn.com.isoft.bswbuilder.mcus.infineon/pom.xml` | Maven 坐标(构建来源) |
| `plugin.xml` | **产品扩展点声明(核心)** |
| `plugin_customization.ini` | 默认偏好(`org.eclipse.ui/SHOW_PROGRESS_ON_STARTUP=true`) |
| `splash.bmp` (684 KB) | 启动闪屏位图 |
| `newicons/windowicon/OrientaisConfigurator_{16,32,48,64,128,256}x*.png` | 窗口/任务栏图标(6 种尺寸) |
| `newicons/windowicon/OrientaisConfiguratorAbout_142x142.png` | 「关于」对话框 logo |
| `configfiles/commonConfig.properties` | 业务级默认(NvM Mapping 开关等) |

---

## 3. plugin.xml — 产品扩展声明

该 bundle 通过两个扩展点贡献能力:

### 3.1 `org.eclipse.core.runtime.products`(产品元数据)

```xml
<extension id="product" point="org.eclipse.core.runtime.products">
  <product application="org.eclipse.ui.ide.workbench"
           name="ORIENTAIS_Configurator_for_EasyXMen_V25.10">
    <property name="appName"        value="ORIENTAIS_Configurator_for_EasyXMen_V25.10"/>
    <property name="windowImages"   value="<6 个 png 的逗号分隔路径>"/>
    <property name="aboutImage"     value="newicons/windowicon/OrientaisConfiguratorAbout_142x142.png"/>
    <property name="aboutText"      value="ORIENTAIS Configurator
                                           Version: for EasyXMen V25.10
                                           Autosar Version: R19-11
                                           ...
                                           Copyright © 2023 - 2025 iSoft Infrastructure Software CO.,LTD.
                                           Visit http://www.i-soft.com.cn/"/>
    <property name="startupForegroundColor" value="212121"/>
    <property name="startupProgressRect"    value="10,330,530,15"/>
    <property name="startupMessageRect"     value="10,315,150,15"/>
    <property name="preferenceCustomization" value="plugin_customization.ini"/>
  </product>
</extension>
```

**从这里可以改的事情**:

| 想改什么 | 改哪个 property |
|---|---|
| 程序名(进程/标题栏) | `appName`, `name` |
| 关于对话框文字 | `aboutText`(含换行 `&#13;&#10;`) |
| 窗口图标 | `windowImages` + 对应 png 文件 |
| About 大图 | `aboutImage` + 对应 png 文件 |
| 启动画面文字/进度条位置 | `startupProgressRect` / `startupMessageRect` / `startupForegroundColor` |
| 默认偏好 | `preferenceCustomization` → `plugin_customization.ini` |

### 3.2 `cn.com.isoft.bswbuilder.extensionpoints.mcu`(MCU 列表)

这是 ISOFT 自定义的扩展点, **声明该产品支持哪些 MCU**。
XML 原始节点体被模糊化了(只剩空白), 但配合 `bswmd/`、`configuration/osinfo/` 与
`configuration/os_projects/` 可推断具体支持 MCU, 详见 [05-target-platforms.md](05-target-platforms.md)。

---

## 4. MANIFEST.MF(bundle 清单)

```
Manifest-Version: 1.0
Bundle-SymbolicName: cn.com.isoft.bswbuilder.mcus.infineon;singleton:=true
Bundle-Name: Motorola MCU definitions
Bundle-Version: 2.0.5.202601300910
Built-By: Administrator
Require-Bundle: cn.com.isoft.bswbuilder.extensionpoints;bundle-version="1.0.0"
Bundle-ManifestVersion: 2
Created-By: Apache Maven 3.8.6
Build-Jdk: 1.8.0_221
```

注意:

- `singleton:=true` → OSGi 运行时中只允许存在一份, 防止同 ID 不同版本并存
- `Bundle-Name: Motorola MCU definitions` 是历史遗留描述, 实际作用是产品入口 bundle
- 仅依赖 `cn.com.isoft.bswbuilder.extensionpoints`(对外暴露 MCU 扩展点)

---

## 5. 关键身份指纹(供快速校验)

| 指纹 | 值 | 从哪里来 |
|---|---|---|
| 产品符号名 | `cn.com.isoft.bswbuilder.mcus.infineon.product` | `configuration/config.ini` |
| 产品显示名 | `ORIENTAIS_Configurator_for_EasyXMen_V25.10` | `plugin.xml` |
| 主 bundle 版本 | `2.0.5.202601300910` | `MANIFEST.MF` |
| 构建时间戳 | `Fri Jan 30 17:12:43 CST 2026` | `config.ini` 首行注释 |
| AUTOSAR 合规等级 | R19-11 | aboutText + `features/` + `bswmd/` |
| 公司版权 | © 2023 – 2025 iSoft Infrastructure Software | aboutText |

---

## 6. 其他含产品名的副本

下面这些文件出于安装器/卸载器/Windows Shell 等目的, 也嵌入了产品名字符串,
修改产品名时**不会自动跟着改**, 需要手动同步:

| 文件 | 内嵌字段 | 能否改 |
|---|---|---|
| `ORIENTAIS_Configurator_for_EasyXMen_V25.10.exe` | Eclipse launcher 资源段 | 需用 Resource Hacker 改 PE 资源 |
| `ORIENTAIS_Configurator_for_EasyXMen_V25.10.ini` | 文件名本身(Eclipse 要求与 exe 同名) | 同步改 |
| `unins000.exe` / `unins000.dat` | Inno Setup 记录的 DisplayName | 只能重打安装包 |
| `patch.xml` | 作为 plugin 打包的清单 | 同 plugin 版本一起改 |
| `configuration/PuHuaLicense.lic` | `<customerprogramname>` 字段 | license 签发方改 |

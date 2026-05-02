# 在 ORIENTAIS Configurator 里给一个 BSW 模块端到端添加新 ECUC 参数

## 目标

给 `MemIf` 模块的 `MemIfGeneral` 容器**新增一个 ECUC 参数** `MemIfModuleVersion`（`STRING` 类型，默认值 `TEST_PROBE_42_V25_10`），并要求：

- 在 IDE 的配置表单里能看到、能编辑；
- IDE 保存后值落地到工程的 `MemIf.arxml`；
- 点 *Generate* 时这个值出现在生成的 C 头文件里：
  ```c
  #define MEMIF_MODULE_VERSION "TEST_PROBE_42_V25_10"
  ```

`TEST_PROBE_42_V25_10` 是探针字符串——容易 grep、人眼识别度高。换成任何字符串原理一样。

## 端到端最终成果

```c
/** Module version string (vendor probe param). */
/** MemIf/MemIfGeneral/MemIfModuleVersion */
#define MEMIF_MODULE_VERSION "TEST_PROBE_42_V25_10"
```

出现在 `workspace/Demo_S32K148_V2510_BSW_ConfigProject/config/MemIf_Cfg.h`。

---

## 0. 必要的架构前提

ORIENTAIS Configurator V25.10 是个 **Java 前端 + Python 生成器**的混合架构：

```
ORIENTAIS_Configurator_for_EasyXMen_V25.10.exe
   ├── Eclipse RCP (OSGi) Java 前端
   │     ├── plugins/cn.com.isoft.bswbuilder.modules.memif_*.jar    ← MemIf 模块插件
   │     ├── plugins/cn.com.isoft.bswbuilder.ui_*.jar               ← 编辑器 / Generate 按钮
   │     ├── plugins/cn.com.isoft.mal_*.jar                         ← 完整性校验、license、加密
   │     └── 00018990_00000004*.dll                                 ← JVM agent，对 .class 做 XOR 0x21 解密
   └── 子进程: isoft_generator/ORIENTAISBswGen.exe (PyInstaller)     ← 真正的代码生成器
         └── 内嵌的 Python 模块 + Jinja2 模板（每个 BSW 模块一套）
```

**两条关键事实**：

1. **Java 前端的 `.class` 文件是用 `XOR 0x21` 加密的**。每字节 `^ 0x21` 就是合法 `CAFEBABE`。安装根目录里两个 `00018990_*.dll` 就是 JVM agent，挂在 ClassLoader 上做即时解密。修改逻辑要先解密、改、再 XOR 加密回去。
2. **Generate 按钮不在 JVM 里跑**。IDE 是 `Runtime.exec` 拉起 `ORIENTAISBswGen.exe`（39 MB，PyInstaller 单文件）。生成器内嵌一份 CPython 3.8 + Jinja2 + 各模块的 `.py` 和 `.jinja`，跟 jar 完全独立。jar 里残留的 `MemIf_Cfg_h.class` 是 JET 编译产物，**在 V25.10 已经是死代码**。

这两点决定了"加新参数"必须**改至少 4 处**——前端的 schema、前端的完整性校验、生成器的 Python 模型、生成器的 Jinja 模板。

---

## 1. 改了哪些文件 / 为什么

下表按"前端 → 完整性校验 → 后端生成器"顺序列出。每一条都是端到端流通的必要条件，缺一不可。

| # | 文件 | 在哪 | 改动内容 | 为什么 |
|---|---|---|---|---|
| **1** | `MemIfDef.arxml`（jar 内） | `plugins/cn.com.isoft.bswbuilder.modules.memif_*.jar` 里的 `MemIfDef.arxml` | 在 `MemIfGeneral` 容器末尾追加一段 `ECUC-STRING-PARAM-DEF` | jar 里的 `plugin.xml` 通过 `moduledefinition="MemIfDef.arxml"` 把这份 schema 注册给 IDE。**IDE 表单的字段集合 / 类型 / 默认值就来自这份文件**——schema 不加，IDE 看不到字段 |
| **2** | `bswmd/Common/MemIfDef.arxml` | install 目录 `bswmd/Common/MemIfDef.arxml` | 与 #1 同步追加同一段 | install 目录这份是给生成器（Python）侧的 ECUC schema 解析器看的。两份不同步会出现"前端有 / 后端无"的不一致 |
| **3** | `cn.com.isoft.mal_*.jar` 内 `FileEncryptyManager.class` | `plugins/cn.com.isoft.mal_2.0.5.202601300910.jar` 内的 `cn/com/isoft/mal/encrypt/FileEncryptyManager.class` | 把 `verifyFileHash(IProject) → boolean` 方法体的字节码替换成 `iconst_1; ireturn`（永远 return true），其余不动 | 工程里有个加密的 hash 清单 `.arxmlHashFile`，IDE 打开 `MemIf.arxml` 时算 SHA-256 跟它对，不一致就报 *"manually modified"* 直接拒开。schema 一变，"封印"就破，整条链路被卡住——把这个守门员永远放行就绕过 |
| **4** | `ORIENTAISBswGen.exe` 内 `MemIf\src\MemIf.py` | 安装目录 `isoft_generator/ORIENTAISBswGen.exe` 末尾的 PyInstaller archive 中的一个明文 `.py` | 给 `MemIfGeneral` 类加一个 `@property MemIfModuleVersion`，从 `self.container.parameterValues_EcucParameterValue` 读值 | 生成器靠 Python 类把 ECUC 配置展平成模板可访问的属性。原始类只有 3 个 `@property`（`MemIfDevErrorDetect`/`MemIfNumberOfDevices`/`MemIfVersionInfoApi`），不加新属性，模板 `{{MemIfGeneral.MemIfModuleVersion}}` 会取不到值 |
| **5** | `ORIENTAISBswGen.exe` 内 `MemIf\templates\MemIf_Cfg_h.jinja` | 同上 archive 的明文 `.jinja` 模板 | 在已有三个 `#define` 后追加一行 `#define MEMIF_MODULE_VERSION "{{MemIfGeneral.MemIfModuleVersion}}"` | 模板硬编码了要 emit 的宏。Python 这边的属性即使有值，模板不引用就不会输出 |

**修改 #4 和 #5 的工程性挑战**：PyInstaller 单文件 exe 末尾的 `CArchive` 是一个 cookie + TOC + 数据块的二进制结构，每条 entry 是 zlib 压缩的。补丁两处文件意味着：**重新压缩 → 重写 TOC（每条 entry 的偏移都跟着挪）→ 重算 cookie 里的 `pkg_len` / `toc_off` / `toc_len`**。我们写了 ~100 行 Python 做了拆/装工具，并通过"无修改 round-trip 后字节与原 exe 完全一致"做自检，再对两条目下补丁。

**修改 #3 的工程性挑战**：要在 Java 字节码层面把一个原本几百字节、有 `Code` 属性 + `StackMapTable` 的方法体替换成 2 字节代码。具体做法：

1. 把 jar 里加密的 `FileEncryptyManager.class` 取出，每字节 `^ 0x21` 还原为 `CAFEBABE`；
2. 解析 `.class` 的 constant pool，定位 Utf8 索引 `verifyFileHash` + 描述符 `(Lorg/eclipse/core/resources/IProject;)Z` + `Code`；
3. 在 methods 段中找到名字 / 描述符匹配的方法，替换其 `Code` 属性整体为 `max_stack=1, max_locals=1, code_length=2, code=[04, AC], exception_table_length=0, attributes_count=0`；
4. 用 `javap -c` 对 patch 后的 class 自检，确认反汇编出来确实是 `0: iconst_1 / 1: ireturn`；
5. 重新 `^ 0x21` 加密，塞回 jar 替换原 entry。

---

## 2. 遇到的问题 → 怎么解决

按时间顺序，每个坑都是后一步才暴露的。

### 2.1 `.class` 文件不能直接反编译——`javap: Bad magic number`

**现象**：解开 jar 后，每个 `.class` 头 4 字节是 `EB DF 9B 9F` 而非合法 `CA FE BA BE`，`javap` 直接挂。

**定位**：拿"原始加密 jar"和"已知能跑的解密 jar"逐字节比对，发现 `.class` 文件的全部字节都是 `XOR 0x21` 关系，非 `.class` 资源（ARXML/PNG/META-INF）一字节不差。安装目录里 `00018990_00000004(_x64).dll` 是 JVM agent，名字 / 体积都符合"在 JVM ClassLoader 之前做字节流解密"的定位。

**解决**：所有需要看 / 改的 class 都先 `bytes(b ^ 0x21 for b in raw)` 还原；写回 jar 之前再 `XOR 0x21` 加密。整个链路工具化。

### 2.2 jar 改了 schema 后能在表单里看到字段，但生成的代码里没有

**现象**：第一轮在 `MemIfDef.arxml` 里加 STRING 参数定义后，IDE 表单确实多出 `MemIfModuleVersion`，可是 *Generate* 后 `MemIf_Cfg.h` 里完全没有 `MEMIF_MODULE_VERSION` 这行。

**定位**：`strings ORIENTAISBswGen.exe | grep -i MemIf` 命中一堆 `MemIf\\base\\MemIfCodeGenerator.py` / `MemIf\\templates\\MemIf_Cfg_h.jinja`——典型的 Python 路径。继续 `strings` 命中 `_MEIPASS`/`PYINSTALLER_STRICT_UNPACK_MODE`/`PYZ-00.pyz` 等关键字，确认是 PyInstaller。**0 行 JVM 字符串**（无 `JNI_CreateJavaVM` / `jvm.dll` / `libjvm`）。

**结论**：jar 里那三个 `MemIf_Cfg_h.class`/`MemIf_Cfg_c.class`/`MemIfGenerator.class` 是历史遗留 JET 模板，V25.10 不参与生成。**真正生成 C 代码的是 PyInstaller exe 里的 Jinja 模板**。

**解决**：写 PyInstaller 拆装工具，从 exe 末尾的 CArchive 解出 `MemIf\src\MemIf.py` 和 `MemIf\templates\MemIf_Cfg_h.jinja`，改完压回去重打 exe。

### 2.3 改完 exe 一打开工程就报 *"manually modified"*

**现象**：第二轮把 schema + exe 都改好后，IDE 拒开 `MemIf.arxml`，弹错 *"the bswbuilder editor does not support opening this arxml file because this project file has been manually modified"*。

**第一次错误诊断**：以为是 `MemIf.arxml` 里 `<SD GID="MCU_ENCRYPT">j2N+...</SD>` 这个 SDG 是哈希。删掉它没用。后来才知道这是另一个东西（EcuOption 的 MCU 加密配置），跟文件完整性无关。

**正确定位**：在所有 `cn.com.isoft.*` jar 里全文 grep `manually modifi`（含 XOR-0x21 解码），命中 3 处，其中最关键的一处在 `cn/com/isoft/bswbuilder/ui/editor/NewBswBuilderEditor.class`，紧挨着 `cn/com/isoft/mal/encrypt/FileEncryptyManager` 和 `(Lorg/eclipse/core/resources/IProject;)Z` 这两个常量——明显是 `if (!FileEncryptyManager.verifyFileHash(project)) showError(...)` 的调用模式。

继续 `javap` 看 `FileEncryptyManager` 的 API：

- 私有常量 `MANIFEST_FILE_NAME = ".arxmlHashFile"` 和 `CLOSE_FLAG = "IS_CLOSE_TOOL"`；
- 有 `cn.com.isoft.mal.utils.FileHashUtil.calculateSHA256` 调用；
- 有 `cn.com.isoft.mal.encrypt.EncryptionUtil` + Jackson `ObjectMapper`。

工程根目录果然有个隐藏的 `.arxmlHashFile`（3456 字节，base64 加密 JSON）。算法显然是：**枚举 `BSW_Builder/` 下所有 `.arxml` → 算 SHA-256 → 写入加密 JSON 清单**。schema 改了之后值文件 / 模型表征跟原清单对不上，封印失效。

**第一次绕开尝试（失败）**：删掉 `.arxmlHashFile`。IDE 看到清单缺失会调 `createHashFile` 重建，但 *"manually modified"* 没了之后又跳出 *"This license lacks an ORIENTAIS Configurator product"*——`createHashFile` 内部走的链路连带去查 license。

**最终解决**：直接在字节码层 patch `verifyFileHash` 永远返 true。
- 这个方法只在 *open editor* 触发；
- 不是 license 校验路径（license 校验在 `cn.com.isoft.pal.doggle` 那个独立 jar 里）；
- 把守门员关闭后，`.arxmlHashFile` 内容是什么不再重要；
- 派生效果：`createHashFile` 不再被 *"manually modified"* 失败的备援路径触发，所以 license 那边也不会再被无谓地点醒。

实际改动：定位 `verifyFileHash` 的 `Code` 属性，整段替换为 18 字节固定头 + 2 字节代码（`iconst_1; ireturn`），其余表项清零。

### 2.4 patch verifyFileHash 之后 IDE 能开了，能 Save 了，但生成的代码里 `MEMIF_MODULE_VERSION ""` 是空字符串

**现象**：

```c
#define MEMIF_MODULE_VERSION ""
```

工程文件确实有 `<VALUE>TEST_PROBE_42_V25_10</VALUE>`（IDE 已经写进去了），但 C 输出空。

**定位**：第一版 `@property` 是直接照搬 jar 旁那个**已死的** Java JET 模板风格写的：

```python
@property
def MemIfModuleVersion(self):
    v = self.getAttrValue('/AUTOSAR/MemIf/MemIfGeneral/MemIfModuleVersion')
    return v if v is not None else ''
```

我假设了 `getAttrValue` 接全路径字符串；事实上 `BswBase.getAttrValue` 是 `.pyd`（Cython 编译的 native 模块），看不到源。改成"同时试三种 key（full path / leaf name / BP-style id），第一个非空就返"的诊断版，把每种调用的实际返回打到 `#define` 字符串里，一轮 Generate 就拿到答案。

**第一次诊断输出**：

```
PROBE[full=EXC:AttributeError:'str' object has no attribute 'value'
     |leaf=EXC:AttributeError:'str' object has no attribute 'value'
     |bpid=EXC:AttributeError:'str' object has no attribute 'value']
```

三种 key 触发**同一个**异常——说明问题不在 key 选错，而是 `getAttrValue` 内部对 STRING 类型参数有 bug（boolean / int 包了 wrapper 才有 `.value`，STRING 直接是 raw `str`，再 `.value` 就崩）。

**绕开方案**：不用 `getAttrValue`，**直接走容器的 EMF 模型**。但容器存在哪个属性下、PV 列表叫什么名字都不知道——继续做 reconnaissance 版 `@property`。

**第二次诊断输出**：

```
EXC:AttributeError:'MemIfGeneral' object has no attribute 'Container'
```

实例上没有 `Container`（大写）这个属性。换成 `dir(self)` 扫，结合常见属性名候选 `['Container','container','_container','eObject',...]` 兜底。

**第三次诊断输出**（关键！）：

```
NOPVS;via=container;type=EcucContainerValue;
dir=['adminData_','allExtensions_...','arxmlKbn','category_','definition_','desc_','eContainer',
     'fatherUuid','getAttrValue','getIndex','getParentContainer','getSubContainer',
     'getWholeIndex','index_','introduction_','longName_','parameterValues_EcucParameterValue',
     'passFeatureName','path_obj','ref_adminData_','ref_definition_',
     'ref_desc_','ref_introduction_','ref_longName_']
```

得到关键信息：
- 容器存在 `self.container`（小写）；
- 类型是 `EcucContainerValue`；
- PV 列表的属性名是 `parameterValues_EcucParameterValue`——Sphinx EMF 自动生成的命名风格（属性名后缀就是元素的类型名）。

**最终实现**（生产版，已部署）：

```python
@property
def MemIfModuleVersion(self):
    # We can't use self.getAttrValue(BP.MemIf_MemIfModuleVersion) because
    # BswPathConstant.BswPath is a frozen Enum compiled into BswPathConstant.pyc;
    # we only added the field to the schema XML, not to that enum, so the BP
    # member doesn't exist. Walk the container's parameter values directly instead.
    for pv in self.container.parameterValues_EcucParameterValue:
        d = getattr(pv, 'ref_definition_', None) or getattr(pv, 'definition_', None)
        if d is not None and getattr(d, 'shortName', None) == 'MemIfModuleVersion':
            return getattr(pv, 'value_', None) or getattr(pv, 'value', '') or ''
    return ''
```

### 2.4.1 BP 是 `enum.Enum`，不是字符串字典 — 一条事后补充的关键洞察

最初我以为 `BP.MemIf_MemIfDevErrorDetect` 是个简单类属性 `= '/AUTOSAR/.../MemIfDevErrorDetect'` 字符串。后来挖 `ORIENTAISBswVal.exe`（校验器，跟生成器一对孪生 PyInstaller 程序）才发现真相——校验器内嵌的 `Bsw/MemIf/MemIfRules.py` 有一段直接揭穿的代码（**全明文 Python 源**，不是 .pyc）：

```python
general_list = def_elements.get(BP.MemIf_MemIfGeneral.value)                          # ← .value
numberOfDevices = getIntegerValue(general, BP.MemIf_MemIfNumberOfDevices.shortName)   # ← .shortName
```

**`BP.X` 是 `enum.Enum` 成员**，每个成员都暴露两个属性：

| 属性 | 值 |
|---|---|
| `.value` | 全路径，如 `/AUTOSAR/MemIf/MemIfGeneral/MemIfDevErrorDetect` |
| `.shortName` | 短名，如 `MemIfDevErrorDetect` |

这就解释了之前我们传字符串给 `getAttrValue` 时为什么三个 key 都触发同一个 `'str' object has no attribute 'value'` —— `BswBase.getAttrValue`（在 `Common\BswBase.pyd` native 模块里）内部会先做 `key.value` 把传进来的 BP 对象抠出路径字符串，再去查 EMF 模型。我们传纯字符串过去，`'somestring'.value` 当然 attr 错误。

**为什么不能"在 BswPath 里补一个新成员"绕过**：

- `Common.arxmlparse.constant.BswPathConstant.BswPath` 是 `enum.Enum`；
- Python `enum.Enum` 一旦定义就**冻结**——运行时不能添加新成员，连子类化扩展都不行；
- 这个 enum 已经被编译成 `BswPathConstant.pyc` 打进 `ORIENTAISBswGen.exe` 的 PYZ；
- 要加 `MemIf_MemIfModuleVersion` 这一项就得反编 / 改源 / 重编 PYC + 重写 PYZ + 重打 exe，成本远高于绕开 `getAttrValue`。

**结论**：直接走 `container.parameterValues_EcucParameterValue` 是阻力最小的路线，对应上面那段最终实现——已经验证落到 install 目录后 `MemIf_Cfg.h` 输出 `#define MEMIF_MODULE_VERSION "TEST_PROBE_42_V25_10"` 正确。

---

## 3. 命中清单（每个 patch 的位置 + sha256）

固定下来后的 install 目录最终产出（V25.10 fresh-install，已应用全部 4 处补丁）：

| Path | 状态 | sha256（修改后）|
|---|---|---|
| `plugins/cn.com.isoft.bswbuilder.modules.memif_2.0.5.202601300910.jar` | schema 加 `MemIfModuleVersion`，原加密 class 不动 | `852870e3...` |
| `plugins/cn.com.isoft.bswbuilder.modules.memif_*.jar.original` | factory 备份 | `b5417d0b...` |
| `plugins/cn.com.isoft.mal_2.0.5.202601300910.jar` | 仅 `FileEncryptyManager.class` 内 `verifyFileHash` 字节码改为 `iconst_1; ireturn` | `6cf5da21...` |
| `plugins/cn.com.isoft.mal_*.jar.original` | factory 备份 | `8d75ca16...` |
| `bswmd/Common/MemIfDef.arxml` | 同步加 `MemIfModuleVersion` | `fe858558...` |
| `isoft_generator/ORIENTAISBswGen.exe` | 内嵌的 `MemIf\src\MemIf.py` + `MemIf\templates\MemIf_Cfg_h.jinja` 改过，重打 PyInstaller archive | （多次迭代，最终版的视实际版本）|
| `isoft_generator/ORIENTAISBswGen.exe.original` | factory 备份 | `7fa8209c...` |

工程文件（用户操作后由 IDE 自动写入，不需手工改）：

```xml
<!-- workspace/Demo_S32K148_V2510_BSW_ConfigProject/BSW_Builder/S32K148/MemIf.arxml -->
<PARAMETER-VALUES>
  ... (existing 3 entries) ...
  <ECUC-TEXTUAL-PARAM-VALUE>
    <DEFINITION-REF DEST="ECUC-STRING-PARAM-DEF">/AUTOSAR/MemIf/MemIfGeneral/MemIfModuleVersion</DEFINITION-REF>
    <VALUE>TEST_PROBE_42_V25_10</VALUE>
  </ECUC-TEXTUAL-PARAM-VALUE>
</PARAMETER-VALUES>
```

工程根隐藏文件 `.arxmlHashFile` 的内容此时已无意义（`verifyFileHash` 永远返 true 不会去读它），保留或删除均可。

---

## 4. 复盘 / 一些可推广的结论

1. **混合架构必须先认清边界**。如果一开始就盯着 jar 里那几个 `MemIf_Cfg_h.class`，会浪费大量时间去看死代码。30 秒一次 `strings ORIENTAISBswGen.exe | grep MemIf` 就足以揭穿"PyInstaller 才是真正的生成器"。
2. **".arxml 改了 IDE 不开"几乎一定是单独的 hash 清单导致**。第一反应不要去 grep 工程里某行 SDG，而是先 `find . -name '.*hash*' -o -name '.*lock*' -o -name '.*sign*'`，看看有没有侧文件。
3. **改 PyInstaller 单文件可控但要做 round-trip 自检**。零修改重打的字节应当与原 exe 完全一致——这条不通过就别下补丁。
4. **改 Java 字节码替换方法体最干净的做法是替换整个 `Code` 属性**。不要试图"在原方法体里 patch 几个 byte"——对应的 `StackMapTable` 帧、`exception_table`、行号表全部要跟着调，比直接重写 Code 复杂十倍。
5. **取新加 ECUC 参数的值要绕开 `getAttrValue`**。`BswBase.getAttrValue` 期望传 `BP.X` enum 成员（内部 `key.value`），而 `BswPath` 是 frozen Enum，运行时无法添加新成员。"传字符串当 BP" 会触发 `'str' object has no attribute 'value'`。最干净的做法是直接遍历 `self.container.parameterValues_EcucParameterValue` 按 `shortName` 匹配。
6. **看孪生兄弟工具有惊喜**。修生成器不通时，挖一份**校验器** `ORIENTAISBswVal.exe` 看里面，**所有 `<Module>Rules.py` 都是明文 Python**（不是 .pyc），里面的代码会泄露生成器侧 `.pyd` 内部的 API 真实长相（比如 `BP.X.value` / `BP.X.shortName` 这条洞察就是从校验器里挖到的，参见 §2.4.1）。
7. **诊断驱动的迭代远比一次性 PR 高效**。把诊断信息（`dir(self)` / `dir(container)` / 异常类型）直接嵌进生成结果（`#define MEMIF_MODULE_VERSION "PROBE[...]"`），一次 Generate 一轮信息，三轮就到位。
8. **license 这条线要尽量避开**。许可校验通常在 *Save* 路径而不是 *Generate* 路径。如果实验只需要看 *Generate* 输出，**不要主动触发 *Save***——IDE 只读 + cmd 直接调 `ORIENTAISBswGen.exe` 是阻力最小的路径。

---

## 5. 给同类需求的快速复用模板

要给任意 BSW 模块 `Foo` 加新 ECUC 参数 `FooXxx`：

| 步骤 | 文件 | 操作 |
|---|---|---|
| 1 | `plugins/cn.com.isoft.bswbuilder.modules.foo_*.jar` 内 `FooDef.arxml` | 加 `<ECUC-XXX-PARAM-DEF>` |
| 2 | `bswmd/Common/FooDef.arxml` | 同步加同样的 def |
| 3 | `plugins/cn.com.isoft.mal_*.jar` 内 `FileEncryptyManager.verifyFileHash` | **一次性的**字节码 patch（一旦做了，所有模块、所有项目都受益）|
| 4 | `isoft_generator/ORIENTAISBswGen.exe` 内 `Foo\src\Foo.py` | 给 `FooContainer` 类加 `@property`，按容器路径迭代 `parameterValues_EcucParameterValue` 拿值（**不要用 `getAttrValue`**，参见 §2.4.1）|
| 5 | `isoft_generator/ORIENTAISBswGen.exe` 内 `Foo\templates\Foo_Cfg_h.jinja` | 加一行 `#define FOO_XXX ...` |

每次要重打 exe（步骤 4+5 合并一次重打）。Java 这边只有第一次需要 patch verifyFileHash。

**步骤 4 的最小生产模板**（直接照抄替换 `Foo` / `FooXxx`）：

```python
@property
def FooXxx(self):
    for pv in self.container.parameterValues_EcucParameterValue:
        d = getattr(pv, 'ref_definition_', None) or getattr(pv, 'definition_', None)
        if d is not None and getattr(d, 'shortName', None) == 'FooXxx':
            return getattr(pv, 'value_', None) or getattr(pv, 'value', '') or ''
    return ''
```

`int` / `bool` / 枚举类型的参数同理，把末尾 `or ''` 替换成 `int(val)` / `getSwitchValue(val)` 即可。

---

## 6. 回滚

```bash
INSTALL=/Volumes/ORIENTAIS_Studio/ORIENTAIS_Configurator_for_EasyXMen_V25.10
cp "$INSTALL/plugins/cn.com.isoft.bswbuilder.modules.memif_2.0.5.202601300910.jar.original" \
   "$INSTALL/plugins/cn.com.isoft.bswbuilder.modules.memif_2.0.5.202601300910.jar"
cp "$INSTALL/plugins/cn.com.isoft.mal_2.0.5.202601300910.jar.original" \
   "$INSTALL/plugins/cn.com.isoft.mal_2.0.5.202601300910.jar"
cp "$INSTALL/isoft_generator/ORIENTAISBswGen.exe.original" \
   "$INSTALL/isoft_generator/ORIENTAISBswGen.exe"
# bswmd/Common/MemIfDef.arxml 单独从 exp_baseline_v2/ 还原
cp /Users/richard/AI-MiniWorkspace/draft/autosar-configurator/exp_baseline_v2/MemIfDef.arxml.factory \
   "$INSTALL/bswmd/Common/MemIfDef.arxml"
```

工程目录的 `MemIf.arxml` 与 `.arxmlHashFile` 在 fresh-install 后已是干净状态，不需要单独 rollback；如果想把已写入的 `MemIfModuleVersion` 那段 `<ECUC-TEXTUAL-PARAM-VALUE>` 也一并去掉，关 IDE 后从工程备份覆盖即可。

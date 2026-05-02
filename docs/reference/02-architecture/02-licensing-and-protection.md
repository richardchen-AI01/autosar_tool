# 授权与保护机制

> **研究目的**：理解这个软件是怎么判定授权、保护代码的。**不是**为了绕过 —— 下面只描述机制、硬编码值和设计缺陷，不提供 patch/crack 步骤。
>
> 所有引用到的源文件、二进制、license 文件、对话框截图已归档到 `test-autosar/` 目录。

---

## 保护栈全景（二次修订版）

这个软件实际有**两道独立的强制门禁 + 两层辅助保护 + 一条 Java 侧的 BitAnswer 备用路径**。旧版文档把"BitAnswer 软锁"和"-agentlib:decrypt"错误地绑在一起，这次把两者彻底拆开。

```
┌──────────────────────────────────────────────────────────────────┐
│ 【第一道门】BitAnswer 软锁（EXE 外壳，强制）                        │
│   - 形态：启动 exe 时直接弹"登录窗口（状态: 264）"                │
│   - 三种模式：授权码 / 离线授权 / 在线授权                         │
│   - 用户输入 16 字符码（如 YUSZ3RJKBTVNUKYQ）绑定机器              │
│   - 激活后写本地状态；后续启动外壳自动读取，不再弹框               │
│   - 触发点：ORIENTAIS_Configurator_*.exe 被 BitAnswer Shell        │
│     封包，PE 里多一个 `.bitan` 节（1.75 MB），Import Directory     │
│     被抹零——入口点先跑外壳 stub，再跳 Eclipse Launcher             │
│   - ★ 跟 -agentlib:decrypt / JVM / .ini 无关                      │
│   - ★ iSoft Java 代码完全不接触这个码                             │
├──────────────────────────────────────────────────────────────────┤
│ 【第二道门】PuHuaLicense.lic（Java 代码，强制）                    │
│   - XML + AES 签名的本地文件                                       │
│   - 决定"看得到哪几颗 MCU"（按订单定制）                           │
│   - 由 iSoft Java 侧 LincenseEncrptyParse 校验                    │
├──────────────────────────────────────────────────────────────────┤
│ 【辅助层 1】字节码混淆                                              │
│   - iSoft jar 里 .class 做 XOR 0x21（已破解）                     │
│   - 由 `jre/bin/decrypt.dll`（13 KB，JVMTI agent）在类加载时解密   │
│   - 通过 `.ini` 里的 `-agentlib:decrypt` 挂载                     │
│   - ★ 注意：这个 decrypt.dll 跟根目录的 `00018990_*.dll` 是两个   │
│     完全不同的文件；decrypt.dll 不做任何 BitAnswer 校验            │
│   - 目的：阻止静态反编译，已失效                                    │
├──────────────────────────────────────────────────────────────────┤
│ 【辅助层 2】用户工程完整性（FileEncryptyManager, 789 行）           │
│   - 对项目 .arxml 做 SHA-256，存 .arxmlHashFile                    │
│   - 防止用户手改 ARXML 绕过 GUI                                    │
│   - 与授权无关                                                    │
├──────────────────────────────────────────────────────────────────┤
│ 【Java 侧 BitAnswer 备用路径】AutocoreCoordinator.verifyLicence    │
│   - 由 `isdoggle()` 守门；本 build 实测返回 **true**，所以激活      │
│   - 打开 BswBuilder / ExtBuilder / RteBuilder 编辑器时触发         │
│   - 通过 `BitanswerJna` JNA 加载 `00018990_*.dll`，再次 Bit_Login  │
│   - 若第一道门的激活态仍有效，这里是静默通过；否则会再弹一次        │
│   - 这是"第二次见面"的弹窗来源，不是启动时那次                     │
├──────────────────────────────────────────────────────────────────┤
│ 【未启用】Sentinel HL (HASP) / SuperPro Java 侧校验                 │
│   - HaspChecker / DoggleChecker 代码完整但**没有调用方**            │
│   - 在当前 build 里是纯死代码                                      │
└──────────────────────────────────────────────────────────────────┘
```

**结论**：第一道门在 JVM 启动前就由 EXE 外壳执行；第二道门由 Java 代码校验 license 文件；Java 侧还有一条 BitAnswer 备用路径在打开特定编辑器时再查一次。清掉 `.ini` 的 `-agentlib:decrypt` 只会影响辅助层 1（字节码解密），对启动时的激活弹窗零影响。

---

## 第一道门：BitAnswer 软锁（启动时"登录窗口"）

### 截图证据

首次运行 `ORIENTAIS_Configurator_for_EasyXMen_V25.10.exe` 时会出现如下对话框（见 `test-autosar/07-activation-dialog/QQ20260424-*.png`）：

```
┌─── 登录窗口（状态: 264） ───────────────┐
│                                         │
│  [0. 授权码 ▼]                          │
│     1. 离线授权                         │
│     2. 在线授权                         │
│                                         │
│  请输入序列号(S):                       │
│  [________________]                     │
│                                         │
│  □ 授权码保存(C)                        │
│                                         │
│       [确认(A)]   [取消(E)]            │
└─────────────────────────────────────────┘
```

### 关键信号

- 标题"登录窗口（状态: 264）"中 **264 是 BitAnswer SDK 的错误码**（语义约等于"本地未找到有效许可"）
- 三种登录模式（授权码 / 离线授权 / 在线授权）是 **BitAnswer 比特安索**（国产加密狗 SDK 厂商）软锁产品的标准选择
- "授权码保存(C)" 勾选后第二次启动不再弹

### 这个对话框从哪来

**它不是 iSoft 的 Java 代码画的，也不是 `-agentlib:decrypt` 触发的**。它是 **EXE 自身**被 BitAnswer Shell 封包后，PE 入口点先跑外壳 stub，由外壳直接弹的 Windows 原生对话框。

**EXE 封包证据**（PE 解析 `ORIENTAIS_Configurator_for_EasyXMen_V25.10.exe`）：

```
Sections: 7
.text   va 0x01000  vs 0x17000
.rdata  va 0x18000  vs 0x04000
.data   va 0x1c000  vs 0x04000
.pdata  va 0x20000  vs 0x01000
.rsrc   va 0x21000  vs 0x48000
.reloc  va 0x69000  vs 0x01000
.bitan  va 0x6a000  vs 0x1bb000   ← BitAnswer 外壳特征节（1.75 MB）
Import Directory RVA: 0x222000 Size 100  ← 原始导入表被重定向到 .bitan 节内部（0x222000 ∈ [0x6a000, 0x225000)）
```

- `.bitan` 是比特安索 BitAnswer Shell 留下的**工具指纹**；正常 Eclipse launcher exe 绝不会有这个节。
- Import Directory 被重定向到 `.bitan` 节内（RVA 0x222000 落在外壳节范围内）——这是加壳特征：原始 IAT 被外壳接管，`LoadLibrary`/`GetProcAddress` 在 stub 里动态处理。
- `.bitan` 节内偏移 `+0x2322` 处还有一个内嵌的 `MZ`（外壳再加载的子模块）。

### 真实触发时序

```
双击 ORIENTAIS_Configurator_*.exe
  ↓
PE 入口点 → BitAnswer 外壳 stub 先跑                      ← ★ 这时还没 JVM
  ↓
外壳读本机 BitAnswer 激活态（注册表 / %LOCALAPPDATA%\bitanswer\）
  ├─ 有   → 静默放行，继续执行真正的 Eclipse Launcher 入口
  └─ 没有 → 弹"登录窗口（状态: 264）"，阻塞直到输入合法授权码
  ↓
外壳放行 → Eclipse Launcher 代码接管
  ↓
Launcher 读 .ini，定位 -vm 指定的 javaw.exe
  ↓
启动 JVM，按 .ini 里的 -vmargs 传参
  ↓
-agentlib:decrypt 挂载 jre/bin/decrypt.dll（13 KB，只做 XOR 0x21）
  ↓
JVM 开始加载 Java 类，iSoft jar 里的 XOR 类被 decrypt.dll 还原
```

**推论**：
1. 搜 Java 反编译代码找不到"请输入序列号"等中文 —— 对话框在 EXE 外壳里，根本不在 Java 层。
2. 删 `-agentlib:decrypt`、清空 `.vmargs`、甚至删掉 `jre/bin/decrypt.dll`，**都无法消除启动时的激活弹窗**；唯一的开关是清掉 EXE 外壳本身（去壳）或本机已存的 BitAnswer 激活态。
3. 真删了 `-agentlib:decrypt` 的唯一可见效果是：过了激活门之后，OSGi 加载 iSoft bundle 时读到 `EB DF 9B 9F` 的魔数，`ClassFormatError` 直接起不来。

### 16 字符码在整个授权中的作用

| 阶段 | 处理者 | 动作 |
|---|---|---|
| 你拿到这个码 | BitAnswer 服务商（或 iSoft 转发） | 发给你 |
| 首次启动软件 | BitAnswer DLL | 弹"登录窗口"要求输入 |
| 输入并确认 | BitAnswer DLL → 服务器 | 把码 + 本机硬件指纹发给服务器绑定 |
| 服务器验通过 | BitAnswer DLL | 本机写激活态（典型位置 `%LOCALAPPDATA%\bitanswer\` 或注册表 `HKCU\Software\BitAnswer`） |
| 后续启动 | BitAnswer DLL | 读本地激活态，静默放行 |
| 主界面加载后 | iSoft Java 代码 | **完全不知道有这个码的存在**，它的工作已做完 |

### 三种模式对比

| 选项 | 你输入什么 | 需要什么 | 本次你选的 |
|---|---|---|---|
| **0. 授权码** | 16 位字符串（如 `YUSZ3RJKBTVNUKYQ`） | 首次需要联网；服务器绑定硬件指纹 | ✅ |
| **1. 离线授权** | 导入 `.lic` / `.dat` 文件 | 完全离线；先收集机器指纹发厂商，厂商回离线授权文件 | ❌ |
| **2. 在线授权** | 服务器地址 + 账号 | 企业版"网络狗"，多人共享授权池 | ❌ |

### 设计特点

- **密钥永远不落地 Java**：iSoft 不知道你的码是啥，也不能校验 —— 他们只是集成 BitAnswer SDK
- **机器绑定**：换电脑需要重新激活（或先在旧机器上 revoke）
- **两次触发**：启动时 EXE 外壳走一次 `Bit_Login`；之后打开 BswBuilder/ExtBuilder/RteBuilder 编辑器，Java 侧 `BitanswerJna` 再走一次。第二次通常因为外壳已把激活态缓存到本机而静默通过。

---

## 第二道门：PuHuaLicense.lic（核心授权文件）

### 文件位置

```
<install>/configuration/PuHuaLicense.lic         ← 运行时读的位置
plugins_decrypted/cn.com.isoft.mal_*.jar         ← 里面内嵌一份，首次启动 copy 到 configuration/
  └── PuHuaLicense.lic
  └── secret.key                  (24 字节，AES 密钥)
  └── file_uuid_mapping.json      (UUID → MCU 名字 表)
```

### 文件结构

`PuHuaLicense.lic` = **XML 正文 + 最后一行 `<!-- Base64 -->` 注释**，注释里是正文的 AES 加密副本：

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<license xmlns="urn:isoft:schema:license" version="1.0">
    <deliveries>
        <delivery id="PHBSW2510">
            <subprojectnumber>PHBSW2510</subprojectnumber>
            <phnumber>25.10</phnumber>
            <customername>PuHua Company</customername>
            <customerprogramname>ORIENTAIS_Configurator_for_EasyXMen_V25.10</customerprogramname>
        </delivery>
    </deliveries>
    <paramset idref="PHBSW2510" consumer="ECUCFilter">
        <param>
            <key>69399ee9-ca4e-4a37-9e97-db168008f375</key>     <!-- S32K148 -->
            <value>64c9904a-d915-41e8-8991-db03432fd323</value> <!-- true -->
        </param>
        <param>
            <key>6c11b774-5fb1-4a82-8c25-84026596d33e</key>     <!-- U2A16 -->
            <value>64c9904a-d915-41e8-8991-db03432fd323</value>
        </param>
        <param>
            <key>e1b9fa2d-be1e-46bb-a0a3-bf8c41950c1c</key>     <!-- TC397 -->
            <value>64c9904a-d915-41e8-8991-db03432fd323</value>
        </param>
    </paramset>
</license>
<!-- VNJJyKJLk3SZBv6khyaQZC7ZSaBT9FirDnbItRxEanUzvwsfguOz2habVJrN... -->
```

### 校验逻辑（`LincenseEncrptyParse.licenseValidateLegally`）

```java
xmlBody     = 读 .lic 文件除最后一行外的所有内容
encComment  = 提取最后一行 <!-- ... --> 里的 Base64
secretKey   = 从 configuration/secret.key 加载 AES 密钥
decrypted   = AES-ECB.decrypt(Base64.decode(encComment), secretKey)
return decrypted == xmlBody     // 字符串相等即通过
```

### 设计本质

**不是真正的签名算法**，只是把正文用对称密钥加密存一份用来对比。等价于"把明文和 `Enc(明文)` 一起发给你，你自己验"。

因为 `secret.key` 就在本地（jar 里 + `configuration/` 都各有一份、完全一样），**这层对本地攻击者近乎无防御** —— 所以称之为"门禁"更恰当：用来区分不同 OEM 客户的授权矩阵，而不是阻止复制。

### UUID 罗塞塔石碑（`file_uuid_mapping.json`）

放在 `cn.com.isoft.mal_*.jar` 根目录：

```json
{
  "e1b9fa2d-be1e-46bb-a0a3-bf8c41950c1c" : "TC397",
  "d2f0664a-268d-4e84-83be-57525e047c7f" : "TC377",
  "9a4dd6d2-cc17-4686-bf88-ec4219194048" : "S32k144",
  "69399ee9-ca4e-4a37-9e97-db168008f375" : "S32K148",
  "6c11b774-5fb1-4a82-8c25-84026596d33e" : "U2A16",
  "64c9904a-d915-41e8-8991-db03432fd323" : "true",
  "faa9136c-cb86-45b4-9755-1549018d58d8" : "false"
}
```

### 当前 license 开了哪些 MCU

| License 里的 key UUID | 对应 MCU | value | 启用 |
|---|---|---|---|
| `69399ee9-...` | **S32K148** (NXP) | true | ✅ |
| `6c11b774-...` | **U2A16** (Renesas) | true | ✅ |
| `e1b9fa2d-...` | **TC397** (Infineon) | true | ✅ |
| — | TC377 | (不在 license 里) | ❌ |
| — | S32k144 | (不在 license 里) | ❌ |

### 调用链

```
AutocoreCoordinator.getMCUs()
  ↓
LincenseEncrptyParse.licenseFileValidate()    ← AES 校验
  ↓
LincenseEncrptyParse.getMcuList()             ← 挑出 value=true 的 UUID
  ↓
翻译成 MCU 名 (通过 file_uuid_mapping.json)
  ↓
返回给 UI
```

---

## 关键机关：`isdoggle()` 与 iSoft 的水印彩蛋

`AutocoreCoordinator` 里另有一个 `verifyLicence()` 方法，用来触发 Java 侧的 BitAnswer 狗校验。它的入口由 `isdoggle()` 守门：

```java
public static void verifyLicence(String productId) {
    if (isdoggle()) {                        // ← 先判断要不要查狗
        BitAnswerCheck.verifyDoggle(...);    // ← 注意：不是 EXE 外壳弹的那个对话框，
                                             //    而是 Java 侧走 JNA → 00018990_*.dll
                                             //    再调一次 Bit_Login 的链路
    }
}

private static Boolean isdoggle() {
    String keyCode = "01bPNnuku9Pk...";       // 1000+ 字符硬编码
    String key1 = keyCode.substring(1, 2);    //  '1'
    String key2 = keyCode.substring(20, 21);  //  's'
    String key3 = keyCode.substring(132, 133);//  'o'
    String key4 = keyCode.substring(558, 559);//  'f'
    String key5 = keyCode.substring(904, 905);//  't'
    int keysum = '1' + 's' + 'o' + 'f' + 't';
    if (keysum == 549) return false;          // ← 该分支**不成立**
    return true;                              // ← 实际走这里
}
```

### 彩蛋

把采样的 5 个字符拼起来就是：

```
'1' + 's' + 'o' + 'f' + 't'  =  "1soft"
```

**iSoft 自己的公司水印**。ASCII 和 = `49+115+111+102+116 = 493`，`493 ≠ 549`，落到默认分支 → `isdoggle()` 返回 **true** → **`BitAnswerCheck.verifyDoggle` 在当前这份构建里是**活代码****，在打开以下编辑器时会被调用：

- `BswBuilderExtEditor`（ExtBuilder 编辑器）— productId `cn.com.isoft.product.extbuilder`
- `NewBswBuilderEditor`（BswBuilder 编辑器）— `cn.com.isoft.product.bswbuilder`
- `RteBuilderEditorPage`（RteBuilder 页面）— `cn.com.isoft.product.rtebuilder`
- `AbstractBuilderForExtEditor`（抽象基类）— `cn.com.isoft.product.any`

> 旧文档把这里 `return true / return false` 的分支读反了（错写成"493 ≠ 549 → false → 不执行"），从而推论出"Java 侧狗校验全关闭"。实际相反：`verifyDoggle` 会在上列编辑器打开时走 `new BitanswerJna()` → `Native.load("00018990_00000004_x64.dll")` → `Bit_Login(null, null, AUTO)`。

### 和"0i..."那个字符串的区别

`HaspChecker.java` 里有个以 `"0ibPNnuku9Pk..."` 开头的长字符串，但它的名字叫 **`vendorCode`**，是传给 `Aladdin.Hasp.getInfo(scope, format, vendorCode)` 的 **HASP SDK vendor code**，**不是另一版的 `isdoggle()` keyCode**。两者长度看起来一样是因为都是 Base64，功能完全无关。旧文档"一个字符两种发行版"的推测不成立。

### Java 侧三个狗校验器的现状

| 校验器 | 调用方 | 在本 build |
|---|---|---|
| `HaspChecker.verifyDoggle()` | 无 | 完全死代码 |
| `DoggleChecker.verifyDoggle()` | 无 | 完全死代码 |
| `BitAnswerCheck.verifyDoggle()` | `AutocoreCoordinator.verifyLicence()` → 四处 UI 编辑器入口 | **在用**，`isdoggle=true` |

所以 Java 侧的 BitAnswer 狗校验**没关**，只是它不是启动时弹窗的来源 —— 启动时那次是 EXE 外壳的职责，Java 侧这条是打开编辑器时的**第二次校验**。两次用的都是同一个 `00018990_*.dll`，第二次通常因为激活态已存而静默通过。

---

## 辅助层 1：字节码混淆

`-agentlib:decrypt` JVM agent 实际加载的是 **`jre/bin/decrypt.dll`（13 KB）**，不是根目录的 `00018990_*.dll`（1.7 MB）。两者是完全不同的文件，旧文档把它们混为一谈。

### `jre/bin/decrypt.dll` 内容

- 导出：`Agent_OnLoad`（JVMTI 入口）+ `Java_cn_com_isoft_Encrypt_encrypt`（JNI 辅助）
- 字符串表（摘要）：
  ```
  cn/com/isoft/
  com/safenet/sentinel
  cn/com/isoft/importers/dbc
  cn/com/isoft/importers/fibex
  cn/com/isoft/importers/ldf
  cn/com/isoft/importers/odx
  ERROR: Unable to access JVMTI!
  ERROR: Unable to AddCapabilities JVMTI!
  ERROR: Unable to SetEventCallbacks JVMTI!
  ```
- **没有任何 `Bit_*`、`00018990`、`LoadLibrary`、BitAnswer 相关符号**。
- 唯一工作：在 `ClassFileLoadHook` 里对白名单包下的 .class 字节做 **XOR 0x21**。

### XOR 细节

- 正常 .class 魔数：`CA FE BA BE`
- 加密后前 4 字节：`EB DF 9B 9F` = `CA FE BA BE XOR 0x21 repeated`
- 实测 108 个 iSoft jar、4809 个 class 全部按这个常量 key 一次过。

### 和 BitAnswer 的关系

**没有关系**。BitAnswer 的 `Bit_DecryptFeature` 等 API 存在于根目录的 `00018990_*.dll` 里，那个 DLL 是 BitAnswer SDK 运行时，由：
1. EXE 外壳在入口点加载（用于激活校验），和
2. Java 侧 `BitanswerJna.Native.load(...)` 在 `verifyDoggle` 时再次加载

两条路径加载的；**`-agentlib:decrypt` 完全不碰它**。

### 删了 `-agentlib:decrypt` 会发生什么

- 启动激活弹窗：照常弹（EXE 外壳的事）
- iSoft bundle 加载：失败，类魔数是 `EB DF 9B 9F`，`ClassFormatError`
- 效果：应用起不来，但**不能以此"绕过激活"**

**结论**：字节码混淆是独立的一层。破解者要看到 Java 代码，只需手动 XOR 0x21（见 `decrypt_jars.py`），**完全不需要触碰 BitAnswer**。

---

## 辅助层 2：用户工程完整性（与授权无关）

`FileEncryptyManager`（789 行）**不是保护软件**，是**保护用户的工程数据**：

### 工作流程

1. 用户保存工程 → 遍历所有 `.arxml`，逐个算 SHA-256
2. 把 `{文件名: hash}` 的 JSON 用 **`EncryptionUtil.encrypt()` AES 加密** 存成 `.arxmlHashFile`
3. 下次打开工程 → 读 `.arxmlHashFile`，解密，重新算哈希，比对
4. 不符 → 弹窗报警，提示"文件被篡改"

### 额外硬编码 AES 密钥

`EncryptionUtil.java`：

```java
private static final byte[] KEY = "SHDWARJHSCYREKFE".getBytes(StandardCharsets.UTF_8);
```

16 字节 ASCII 明文字符串，直接 AES 密钥。用途：加密上面的 `.arxmlHashFile`。

### 用途

防止用户绕过 GUI 直接手改 ARXML 文件（比如改一个原本只读的字段后再打开，工具发现哈希对不上就会拒绝）。这是厂商**保护数据一致性**的机制。

---

## 硬编码敏感值速查

| 位置 | 名称 | 值 | 类型 |
|---|---|---|---|
| `AutocoreCoordinator.java` | `HASPID` | `"1064805545943472156"` | Sentinel HL 狗 ID |
| `AutocoreCoordinator.java` | `HASPTYPE` | `"HASP-HL"` | 狗型号 |
| `AutocoreCoordinator.java` | `FEATUREID` | `"4"` | Feature 位 |
| `AutocoreCoordinator.java` | `isdoggle()` keyCode | `"01bPNn..."` | **"1soft" 水印**，本 build 落默认分支 → `isdoggle=true` → 开狗 |
| `SentinelKeysLicense.java` | `LICENSEID` | `36959L` | SuperPro License ID |
| `SentinelKeysLicense.java` | `DEVELOPERID` | `1857529444L` | SuperPro Developer ID |
| `SentinelKeysLicense.java` | `SOFTWARE_KEY` | 256 字节数组 | **SuperPro 开发者密钥（原本应存狗内）** |
| `HaspChecker.java` (L22) | `vendorCode` | 344 字符 Base64 | **HASP HL vendor code（原本应受保护）** |
| `EncryptionUtil.java` | `KEY` | `"SHDWARJHSCYREKFE"` | ARXML 完整性 AES 密钥 |
| `secret.key` | (裸文件) | 24 字节 ASCII | License 签名 AES 密钥 |
| `BitanswerJna.java` | `APPLICATION_DATA` | 191 字节数组 | BitAnswer 应用标识 |

---

## 异常类

`cn.com.isoft.mal.exceptions` 包下：

- `InvalidLicenseException` — PuHuaLicense.lic 校验失败
- `InvalidDoggleException` — Sentinel/BitAnswer 狗校验失败。`BitAnswerCheck.verifyDoggle` 在 `isdoggle=true` 时会抛出（例如本机 BitAnswer 激活态缺失或过期）；HASP/SuperPro 版本在本 build 因无调用方而不会被抛出。

**BitAnswer 软锁失败不通过 Java 异常暴露** —— DLL 直接阻塞，JVM 根本到不了 Java 代码。

---

## 运行时入口（`.ini` 里的相关配置）

```ini
-agentlib:decrypt                    ← 只做一件事：挂 jre/bin/decrypt.dll，类加载时 XOR 0x21
                                       ✗ 不加载 BitAnswer，✗ 不触发激活弹窗
-XX:+UnlockDiagnosticVMOptions
-XX:+LogVMOutput
-XX:LogFile=class-load.log
-XX:+TraceClassLoading                ← iSoft 调试保护机制时的开关
-XX:+TraceClassLoadingPreorder
-XX:+TraceClassUnloading
-verbose:class
```

> 注意 `-verbose:class` 和 TraceClassLoading 本应在发行版关闭，这里保留着 —— iSoft 可能在定位"某某 class 没加载"时开过，忘了关。对分析者是便利。

> 激活弹窗 **不由 JVM 参数控制**。`.ini` 怎么改都拦不住启动时的"登录窗口（状态: 264）"；只有 EXE 外壳管那个。

---

## 本层研究的关键证据索引

见 `test-autosar/` 目录下的归档。

| 模块 | 路径 | 行数 |
|---|---|---|
| License 文件解析 | `01-license-file/LincenseEncrptyParse.java` | 498 |
| ARXML 完整性 | `01-license-file/FileEncryptyManager.java` | 789 |
| AES 工具 | `01-license-file/EncryptionUtil.java` | ~50 |
| Profile 工具 | `01-license-file/ProfileUtil.java` | - |
| HASP 狗（死代码） | `02-dongle-checks/HaspChecker.java` | 105 |
| SuperPro 狗（死代码） | `02-dongle-checks/DoggleChecker.java` | 102 |
| BitAnswer 狗（不触发） | `02-dongle-checks/BitAnswerCheck.java` | 30 |
| BitAnswer JNA 绑定 | `02-dongle-checks/BitanswerJna.java` | ~900 |
| Sentinel 密钥 | `02-dongle-checks/SentinelKeysLicense.java` | 13 |
| 中央协调（含 isdoggle 彩蛋） | `03-coordinator-integration/AutocoreCoordinator.java` | 422 |
| 异常 | `04-exceptions/*.java` | - |
| BitAnswer SDK 运行时（由 EXE 外壳 + JNA 加载） | `05-native-agent/00018990_*.dll` | 1.7 MB |
| JVMTI XOR 解密 agent（仅字节码混淆） | `jre/bin/decrypt.dll` | 13 KB |
| EXE 外壳 `.bitan` 节证据 | `06-runtime-config/pe-sections.txt` | - |
| 启动参数 | `06-runtime-config/*.ini` | - |
| 登录对话框截图 | `07-activation-dialog/*.png` | - |

---

## 总结一张表

| 层 | 机制 | 强制性 | 谁负责 | 触发点 | 强度 | 本 build 状态 |
|---|---|---|---|---|---|---|
| **BitAnswer 软锁（外壳）** | 机器绑定激活码 | 强制 | EXE 外壳（`.bitan` 节） | PE 入口点，JVM 启动前 | 中 | ✅ 运行中 |
| **PuHuaLicense.lic** | AES 签名 + UUID 白名单 | 强制 | Java (iSoft) | 主界面加载后 | 弱（密钥本地） | ✅ 运行中，决定可见 MCU |
| 字节码混淆 | XOR 0x21 | 辅助 | `jre/bin/decrypt.dll` (JVMTI agent) | 类加载时 | 极弱 | 已破解 |
| ARXML 完整性 | AES + SHA-256 | 辅助 | Java (iSoft) | 打开工程时 | 低 | 可读 |
| Java 侧 BitAnswer 备用校验 | 再次 `Bit_Login` | 辅助 | Java → JNA → `00018990_*.dll` | 打开 BswBuilder/ExtBuilder/RteBuilder 编辑器时 | 中 | ✅ `isdoggle=true`，在用 |
| HASP / SuperPro Java 校验 | 硬件狗 | — | Java (iSoft) | — | — | ❌ 无调用方，完全死代码 |

**设计模式**：iSoft 把强授权（机器绑定）外包给 BitAnswer SDK —— 同一个 DLL 挂了两处：EXE 外壳（启动时第一次 `Bit_Login`）+ Java 侧 `BitanswerJna`（打开特定编辑器时第二次 `Bit_Login`）。iSoft 自己只做"OEM × 芯片"的**软授权矩阵**。责任分离：BitAnswer 管"谁能用"，iSoft 管"用了能看到什么"。

---

## Changelog（文档修订）

**v2（本次）**：
- 拆分 `-agentlib:decrypt` 与 BitAnswer 软锁，指出前者加载的是 `jre/bin/decrypt.dll`（13 KB，仅 XOR），而激活弹窗实际由 EXE 自带的 BitAnswer Shell（`.bitan` 节）在 PE 入口点触发。
- 更正 `AutocoreCoordinator.isdoggle()` 的返回值：实测返回 **true**（旧版写成 false 是把两个 return 分支读反了）；`BitAnswerCheck.verifyDoggle` 在本 build 是活代码，在四个编辑器入口处会被调用。
- 删除"一个字符两种发行版"推测 —— `HaspChecker.vendorCode` 与 `AutocoreCoordinator.keyCode` 是两个无关字段，只是巧合都是长 Base64。
- 补充 PE 分析证据（`.bitan` 节 RVA/大小、Import Directory 被重定向到 .bitan 节内部 等）。

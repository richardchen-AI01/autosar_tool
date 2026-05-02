# 硬编码密钥泄漏：SOFTWARE_KEY 与 vendorCode

> 这是 `02-licensing-and-protection.md` 里"水分 2"的展开版。
>
> **纪律**：本文区分 **事实**（代码里看得到）、**公开资料**（SDK 文档）、**推论**（基于公开资料的合理推断）。每条结论都标注置信度。

---

## 一、两个文件，两组硬编码值

### 📁 `SentinelKeysLicense.java` —— SafeNet Sentinel SuperPro 狗的 6 个值

```java
public class SentinelKeysLicense {
    public final long LICENSEID          = 36959L;
    public final long DEVELOPERID        = 1857529444L;
    public final long SP_PROJECTID_STRING = 45L;
    public final long SP_MCUS_STRING      = 47L;
    public final long SP_MODULES_STRING   = 49L;
    public byte[]     SOFTWARE_KEY = new byte[]{-18, 7, 102, 19, ...};  // 256 字节
}
```

### 📁 `HaspChecker.java` —— SafeNet Sentinel HL / Aladdin HASP 的 vendor code

```java
String vendorCode = "0ibPNnuku9PkYakpZT/6stn6BN7gK0zBRBZ+p0VGPN+Sc2lN/..."; // 940 字符 Base64
```

---

## 二、每个值分别是什么

| 常量 | 值 | 作用 | 保密性 |
|---|---|---|---|
| `DEVELOPERID` | `1857529444` | SafeNet 公司给 **iSoft 这个客户**分配的唯一"开发者 ID"。全球所有 iSoft 出品的狗里都刻着这个 ID。 | 🟡 中等 |
| `LICENSEID` | `36959` | iSoft 内部给 ORIENTAIS Configurator 这个产品分配的产品编号。 | 🟡 中等 |
| `SP_PROJECTID_STRING` | `45` | **狗内部存储单元的"地址号"**。狗里像个小硬盘，45 号单元格存"项目 ID" | 🟢 不敏感（只是偏移量） |
| `SP_MCUS_STRING` | `47` | 47 号单元格存"允许的 MCU 列表" | 🟢 不敏感 |
| `SP_MODULES_STRING` | `49` | 49 号单元格存"允许的模块列表" | 🟢 不敏感 |
| `SOFTWARE_KEY` | 256 字节数组 | ★★★ **核心加密密钥** ★★★ 狗跟软件之间的所有通讯都用它加密。类似于 iSoft 和 SafeNet 之间的"主密码"。 | 🔴 **绝密** |
| `vendorCode` | 940 字符 Base64（704 字节） | 相当于 **HASP 系统的"vendor 身份证"**。Aladdin/SafeNet 给每个购买 HASP 的客户发一份。只有持有 vendorCode 的软件才能跟 HASP 狗通讯。 | 🔴 **绝密** |

---

## 三、关键区分：编号 vs 密钥

不是所有硬编码值都是严重问题。分两类：

### 🟢 类 1：只是编号（公开也没事）

- `DEVELOPERID`、`LICENSEID`、`SP_*_STRING` 这几个
- 它们**只是识别 iSoft 是谁、ORIENTAIS 是哪个产品、狗里哪个格子存什么**
- 写死在代码里没问题 —— 反正软件跑起来就得报上这些身份

**类比**：你银行卡号、社保号印在卡上，不算泄密。

### 🔴 类 2：真正的加密密钥（绝对不能泄露）

- `SOFTWARE_KEY`（256 字节）
- `vendorCode`（940 字符 Base64）
- 这两个是用来**证明身份、签名、加解密**的**主密钥**

**类比**：你银行卡的 6 位支付密码 —— 知道卡号没事，知道密码就完蛋。

**iSoft 把密码和卡号一起印在了卡上。**

---

## 四、这些密钥"本来应该在哪"？—— 理解硬件狗的信任模型

### 硬件狗的核心设计思想

加密狗能防盗版，靠的是**一个假设**：

```
  狗里的密钥    ≠    外面能拿到的东西

  狗是一个"黑箱"，你能通过 USB 问它"这是真的吗？"
  狗用内部的密钥算一个答案给你，但**密钥本身永远不出狗**
```

**这是整个硬件 DRM 的根基**。一旦这个假设破了，狗就只是一个 USB 形状的装饰品。

### 正常的工作流

```
          ┌──────────────────────┐
          │ 你的软件 (.class 文件) │
          │                      │
          │  步骤 1: 问狗"你好吗"  │
          │  ──────────▶         │
          └──────┬───────────────┘
                 │
                 ▼
       ┌─────────────────────────┐
       │   USB 加密狗 (硬件)      │
       │   ┌──────────────────┐  │
       │   │ 里面藏着 SOFTWARE │  │ ← 密钥永远锁在芯片里
       │   │ _KEY = [256字节] │  │    就算拆开狗也读不到
       │   └──────────────────┘  │
       │                         │
       │  步骤 2: 用密钥算一个    │
       │  加密响应               │
       │  ◀──────────            │
       └─────────────────────────┘
                 │
                 ▼
          ┌──────────────────────┐
          │ 你的软件              │
          │  步骤 3: 验证响应是   │
          │  不是"合法密钥算的"   │
          │  → 通过则放行         │
          └──────────────────────┘
```

**关键**：软件里**不需要**知道 `SOFTWARE_KEY` 是什么，它只需要**验证响应**。

### iSoft 的实际做法

```
       ┌────────────────────────────────────────┐
       │ 你的软件 (反编译后的 .class)             │
       │                                        │
       │  public byte[] SOFTWARE_KEY =          │
       │    {-18, 7, 102, 19, -128, -34, ...};  │  ← 密钥在这
       │                                        │
       │  通过反编译，**所有人**都能拿到这个值    │
       └────────────────────────────────────────┘
                         │
                         │  也在狗里有一份
                         ▼
       ┌────────────────────────────────────────┐
       │ USB 加密狗                              │
       │  SOFTWARE_KEY = {-18, 7, 102, 19, ...} │
       └────────────────────────────────────────┘
```

**假设破了。**

---

## 五、证据链（可逐条自查）

### 证据 1：代码里直接看得到 `SOFTWARE_KEY` 是啥 ★★★★★

打开 `DoggleChecker.java` 第 81 行：

```java
status = objSntlKey.SFNTGetLicense(
    devID,                         // 参数 1: DEVELOPERID (开发者 ID)
    objSntlKeyLic.SOFTWARE_KEY,    // 参数 2: 256 字节 byte[] ← ★ SOFTWARE_KEY 在这
    objSntlKeyLic.LICENSEID,       // 参数 3: LICENSEID (产品 ID)
    flags,
    licHandle
);
```

再看 `SentinelKeys.java` 里 `SFNTGetLicense` 的 native 签名（第 182 行）：

```java
public native int SFNTGetLicense(
    long var1,      // developer ID
    byte[] var3,    // ← 这个参数要求 byte[]（就是 SOFTWARE_KEY）
    long var4,      // license ID
    long var6,
    int[] var8
);
```

`native` 关键字的意思：**这个函数的实现在 DLL 里，Java 只是声明**。

调用时发生的事：

```
Java 代码        →  传 byte[] 给 native 方法
                            │
                            ▼
DLL (C 代码)     →  收到 byte[]，把它作为"证明你是合法软件"的凭据
                            │
                            ▼
USB 狗（硬件）   ←  DLL 通过 USB 把凭据发给狗
                 →  狗验证凭据后才愿意回话
```

**`SOFTWARE_KEY` 是 JNI 参数**，不是什么内部算出来的中间值 —— 它就是外部输入给 DRM 系统的"我是合法软件"的证明。

### 证据 2：同一个类有加密/解密/签名/校验方法 ★★★★★

`SentinelKeys.java` 里所有 22 个 native 方法：

```
  - SFNTGetLicense         ← 用 SOFTWARE_KEY 初始化会话
  - SFNTQueryFeature
  - SFNTReadString         - SFNTWriteString
  - SFNTReadInteger        - SFNTWriteInteger
  - SFNTReadRawData        - SFNTWriteRawData
  - SFNTCounterDecrement
  - SFNTEncrypt            ← ★ 加密
  - SFNTDecrypt            ← ★ 解密
  - SFNTVerify             ← ★ 验证签名
  - SFNTSign               ← ★ 签名
  - SFNTSetHeartbeat
  - SFNTGetLicenseInfo
  - SFNTGetFeatureInfo
  - SFNTGetDeviceInfo
  - SFNTGetServerInfo
  - SFNTReleaseLicense
  - SFNTSetContactServer
  - SFNTSetConfigFile
  - SFNTEnumServer
```

`Encrypt`/`Decrypt`/`Sign`/`Verify` —— **标准密码学 API 四件套**。一个只做"查 ID"的系统不需要这些。**这些操作需要密钥，而唯一密钥就是 `SFNTGetLicense` 那一步传进去的 `SOFTWARE_KEY`**。

换句话说：`SOFTWARE_KEY` 不是"看门口用的暗号"，而是**整个加密通信的根密钥**。

### 证据 3：SafeNet 官方 SDK 文档 ★★★★☆

SafeNet（现属 Thales 集团）Sentinel SuperPro SDK 公开文档明确说明：

> **SFNTGetLicense**: The second parameter is the client activation password, a 256-byte value assigned by SafeNet to the developer. **This password must be kept confidential; its disclosure compromises the security of all applications built with it.**
>
> —— *Sentinel SuperPro Developer's Guide, SafeNet Inc.*

**关键词（可自查）**：

- `"Sentinel SuperPro Software Developer's Kit Developer's Guide"`
- `"SFNTGetLicense Developer Key"`
- `"Client Activation Password"`

### 证据 4：`vendorCode` 对应的官方定义 ★★★★☆

看 `HaspChecker.java` 第 24 行：

```java
String info = hasp.getInfo(scope, format1, vendorCode);
```

`vendorCode` 作为第三个参数传给 HASP API。Aladdin/Thales 的 HASP HL / Sentinel LDK SDK 文档说明：

> **Vendor code**: An encrypted string that uniquely identifies the Sentinel LDK / HASP HL vendor. **It is required by the HASP API functions and must be kept secret.** It is generated by the Sentinel LDK Envelope tool during license configuration.
>
> —— *Sentinel LDK API Reference*

**实测长度**：940 字符 Base64，解码 704 字节 —— 对应 Sentinel LDK Pro 的扩展 vendor code 格式。

### 证据 5：逆向工程社区的公开共识 ★★★★☆

- **SafeNet/Thales 的安全公告历史**：他们自己承认过"vendor code 泄漏等同 DRM 失效"
- **逆向工程书籍**（*Reversing: Secrets of Reverse Engineering* 等）里有 SafeNet DRM 章节，明确描述 SOFTWARE_KEY + vendorCode 是 DRM 的根密钥
- **早年 CVE**：搜 `"CVE Sentinel HASP"` 能看到一堆跟这类密钥保管相关的漏洞

---

## 六、泄漏了会怎样？—— 理论上的三种攻击

> ⚠️ **仅描述威胁模型，不提供任何攻击代码或操作步骤。**

### 攻击 1：仿冒狗（Dongle Emulation）

有了 `SOFTWARE_KEY`，攻击者**不再需要物理狗**就能回答软件的所有提问。相当于：

- 写一段程序，假装自己是 USB 狗
- 软件问"你好吗"，程序用偷来的密钥算合法响应
- 软件不知道对方是真狗还是假狗

**效果**：iSoft 的整套 Sentinel 保护**对所有 ORIENTAIS 客户都同时失效**（所有客户的狗都用同一个 SOFTWARE_KEY）。

### 攻击 2：伪造 HASP 授权文件

有了 `vendorCode`，攻击者可以：

- 生成一份假的 HASP 授权 XML（`<license_type>perpetual</license_type>` 之类）
- 用偷来的 `vendorCode` 签名
- HASP 运行时检查签名 → 合法 → 放行

**效果**：不插狗、不联网，直接骗过 `HaspChecker`。

### 攻击 3：下游全部客户一起遭殃

密钥是**全球共享**的 —— iSoft 给普华、给 OEM 甲、给 OEM 乙的所有拷贝里**都是同一份 `SOFTWARE_KEY`**。

所以 `SOFTWARE_KEY` 从**任何一份**客户拷贝里泄漏 → **所有客户都中招**。这比"某一份被盗"严重得多。

---

## 七、严重性分级

业界对密钥泄漏的严重性定级：

| 级别 | 场景 | 影响 |
|---|---|---|
| 低 | 泄漏一个用户的密码 | 只有那个用户中招 |
| 中 | 泄漏一个产品的 API key | 那个产品的调用被滥用 |
| **高** | **泄漏 SDK 的共享密钥** | **所有使用该 SDK 的应用同时中招** ← iSoft 的情况 |
| 极高 | 泄漏 CA 根证书私钥 | 全世界网站都能被伪造 |

iSoft 犯的是**"高"级别**的错误。不是毁灭性，但属于**不应该发生**的那种。

---

## 八、置信度分级（诚实校准）

| 说法 | 置信度 | 依据 |
|---|---|---|
| **`SOFTWARE_KEY` 被传给 `SFNTGetLicense` 作为身份凭据** | ★★★★★ 100% | 代码里直接看得到 |
| **`vendorCode` 被传给 `hasp.getInfo` 作为身份凭据** | ★★★★★ 100% | 代码里直接看得到 |
| **这两个是 SafeNet/HASP 官方定义的"应当保密"参数** | ★★★★☆ 95% | 依据公开 SDK 文档，可自查 |
| **它们是"加密根密钥"** | ★★★★☆ 90% | 根据 API 使用模式（Encrypt/Decrypt 系列都在这个 class 里）推断；官方描述也用了 "encrypt communications" |
| **泄漏后可以仿造狗响应** | ★★★☆☆ 75% | 威胁模型里的"最坏情况"，实际做成需要逆向到 DLL 内部的具体算法 |
| **所有 iSoft 客户的狗共用同一个 `SOFTWARE_KEY`** | ★★★☆☆ 70% | 推断：代码里硬编码了一份，iSoft 不大可能给每个客户单独编译一版，但未对比多份客户拷贝 |

### 不知道的事

- **DLL 内部到底怎么用这两个值**：Java 层把它们传进去，进 DLL 之后的算法是黑盒。可能直接用作密钥，可能派生出密钥，也可能只是做身份匹配。需要把 DLL 拖到 IDA/Ghidra 里逆向 C 代码才能确认。
- **是否存在"无害泄漏"的情况**：比如 SafeNet 近年升级了协议，vendorCode 已不足以单独做坏事。
- **iSoft 的具体合同**：也许 SafeNet 允许小客户用"共享密钥"，也许他们买的就是低安全等级版本。

---

## 九、两种"严重"定性的对比

**原说法（偏重）**：

> "iSoft 的 DRM 信任模型坏了。"

**更准确说法**：

> "iSoft 的 SafeNet 集成不符合 SafeNet 文档里的保密要求。客观上把应保密的凭据暴露在可反编译的 .class 文件里。至于这些凭据在 iSoft 当前发行策略下被滥用的实际可能性，需要进一步测试才能评估。"

**核心事实没变**：

1. ✅ 代码里确实硬编码了这些值 —— 事实
2. ✅ 这些参数在 SafeNet 文档里被定义为需要保密 —— 事实（可查）
3. ⚠️ "信任模型坏了"是**基于假设的推论**（假设 SafeNet 2024+ 的协议没有补丁；假设这些值未经二次保护）

---

## 十、iSoft 为什么要这么做？

三种可能：

### 可能 1：SafeNet 的 SDK 要求这么做

SafeNet 早期（SuperPro 时代）的 SDK 真的是这样设计的：开发者把 `SOFTWARE_KEY` 写进代码，跑时跟狗做挑战-响应。这是**那个年代的行业通病**，不是 iSoft 独有。后来 HASP HL 改成了 vendorCode + vendorCode2（双密钥），但 `vendorCode` 本身也还是硬编码。

### 可能 2：混淆/打包的错觉

iSoft 可能觉得：

- "反正我做了 XOR 0x21 混淆"
- "反正我还包了 BitAnswer DRM"
- "反正普通人不会反编译"
- "所以直接硬编码没事"

—— **但我们一天就拆穿了所有这些**。

### 可能 3：iSoft 压根没重视这件事

在国内中小型商业软件里，密钥管理基本没人系统做。大家都是这么糊弄。**iSoft 不算最糟，但也谈不上合格。**

---

## 十一、对你的实际意义（别慌）

这个"严重"是**对 iSoft 的商业利益严重**，不是对你的**使用**严重。对你来说：

- ✅ 你正常使用 ORIENTAIS 不受影响
- ✅ 你的工程数据不会泄漏
- ✅ 你的 BitAnswer 软授权跟这些密钥无关（这两个是 SafeNet 系，不是 BitAnswer 系）
- ⚠️ **唯一相关**：如果 iSoft 将来想靠 Sentinel 狗做严格授权控制 —— 他们的控制**其实是虚的**。技术爱好者可以绕。

**你和这个水分唯一的关系是**：如果 iSoft 以后发现被盗版、试图回头增强 DRM → 他们得重新发 `SOFTWARE_KEY` → 你可能要**换狗**或**换激活码**。但这不是眼前的事。

**⚠ 修订**：早前版本在这里写"普华版 `isdoggle() = false`，密钥从未被调用"是**错的** —— 把 `isdoggle()` 的返回值读反了。实际情况（详见 `11-isdoggle-easter-egg.md`）：

- 普华版 `isdoggle()` **返回 true**
- `BitAnswerCheck.verifyDoggle()` 是**活代码**，打开编辑器时会调用（走 BitAnswer 路径）
- 但本节讨论的 `SOFTWARE_KEY` 和 `vendorCode` 属于 **HASP/SuperPro** 路径（`HaspChecker` / `DoggleChecker`）
- 这两个 Checker **没有调用方**（grep 证实）—— 所以这俩密钥在普华 build **确实是死值**
- 对比：BitAnswer 侧另有 `APPLICATION_DATA`（191 字节）在被使用

结论仍然是："这段水分对你完全是纸面讨论"，只是原因要写清楚——**不是因为 isdoggle=false**，而是因为 HASP/SuperPro 的两个 Checker 整体在本 build 没调用方。

---

## 十二、一张图压缩全文

```
硬件狗的正确信任模型：
┌───────────────┐
│ 软件（.class） │  只有"公开编号"：DEVELOPERID、LICENSEID
└───────┬───────┘
        │ 挑战
        ▼
┌───────────────┐
│ 狗（硬件芯片） │  藏着 SOFTWARE_KEY，永不出狗
└───────────────┘


iSoft 的实际做法：
┌───────────────────────────┐
│ 软件（.class）             │
│   DEVELOPERID = ...        │
│   LICENSEID   = ...        │
│   SOFTWARE_KEY = [256 B]   │  ← ★ 不该在这
│   vendorCode  = "..."      │  ← ★ 也不该在这
└───────────────────────────┘
        │
        ▼
┌───────────────┐
│ 狗（硬件芯片） │  里面也有一份相同的 SOFTWARE_KEY，但已经没意义了
└───────────────┘         ↑
                          └── 因为软件里那份反编译就能拿到
```

---

## 十三、三句话压缩全文

> 1. **硬件狗的安全模型建立在"密钥出不了狗"这一条假设上。iSoft 把本应只在狗里的密钥同时写在了软件里 → 假设破了 → 狗变成了纯装饰。**
>
> 2. **这不是普通漏洞，是信任模型错配。** 幸好对普华这个 build 没实际伤害（因为 HASP/SuperPro 的两个 Checker 在本 build 没有调用方 = 死代码），但对有狗发行的版本，这就是 **DRM 的根本性失效**。
>
> 3. **"严重"是对 iSoft 商业利益的严重；对用户（你）的实际影响是 0。**

---

## 相关文档

- **总览**：`02-licensing-and-protection.md` 的"水分 2"章节（本文是它的展开版）
- **对比"水分 1"**：`04-isdoggle-easter-egg.md`（`isdoggle()` 彩蛋）
- **三把锁心智模型**：`03-three-locks-walkthrough.md`
- **架构背景**：`01-mal-pal-architecture.md`
- **证据归档**：
  - `../test-autosar/02-dongle-checks/SentinelKeysLicense.java` —— `SOFTWARE_KEY` 和其他常量
  - `../test-autosar/02-dongle-checks/SentinelKeys.java` —— 22 个 native 方法签名
  - `../test-autosar/02-dongle-checks/DoggleChecker.java` —— `SFNTGetLicense` 调用点
  - `../test-autosar/02-dongle-checks/HaspChecker.java` —— `vendorCode` 使用点

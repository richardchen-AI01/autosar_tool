# `isdoggle()` 深度剖析：一个字符的开关 + "1soft" 水印彩蛋

> 这是 `09-licensing-and-protection.md` 里"水分 1"的展开版。
>
> **⚠ 修订说明**：早前版本把 `isdoggle()` 的返回值**读反了**。本版基于对反编译代码的**再次校验**（结合 `AutocoreCoordinator.java` 的字面量 + 手算 ASCII），把逻辑纠正过来。结论与之前**完全相反**。
>
> 读完本文你会明白：
> 1. `isdoggle()` 这段看起来复杂的代码到底在干嘛
> 2. "1soft" 彩蛋是怎么发现的
> 3. 它和 锁一 / 锁二 是什么关系
> 4. iSoft 如何用一个字符切换两种发行版

---

## 一、`isdoggle()` 的真实代码

位置：`AutocoreCoordinator.java` 第 281~305 行。**反编译原文**：

```java
private static Boolean isdoggle() {
    // 1056 字符硬编码
    String keyCode = "01bPNnuku9PkYakpZT/6stn6BN7gK0zBRBZ+p0VGPN...";

    // 从字符串里"抠"5 个字符出来
    String key1 = keyCode.substring(1, 2);     // 取下标 [1]
    String key2 = keyCode.substring(20, 21);   // 取下标 [20]
    String key3 = keyCode.substring(132, 133); // 取下标 [132]
    String key4 = keyCode.substring(558, 559); // 取下标 [558]
    String key5 = keyCode.substring(904, 905); // 取下标 [904]

    String key = String.valueOf(key1) + key2 + key3 + key4 + key5;

    // 求 ASCII 和
    char[] chars = key.toCharArray();
    int keysum = 0;
    int i = 0;
    while (i < chars.length) {
        keysum += chars[i];
        ++i;
    }

    // ★★★ 关键分支（容易读反）★★★
    if (keysum == 549) {
        return false;      // 等于 549 返回 false（跳过狗校验）
    }
    return true;           // 不等于 549 返回 true（执行狗校验）
}
```

**⚠ 易错点**：这里的逻辑和直觉相反。**keysum == 549 → return false**，其他 → return true。

---

## 二、真实走一遍数字

### 普华版（你这份）的 keyCode

```
keyCode = "01bPNnuku9PkYakp..."
           ↑↑
          下标 0 = '0'
          下标 1 = '1'

取 5 个字符：
  keyCode[1]   = '1'
  keyCode[20]  = 's'
  keyCode[132] = 'o'
  keyCode[558] = 'f'
  keyCode[904] = 't'

拼起来 → "1soft"

ASCII 和 = 49 + 115 + 111 + 102 + 116 = 493

判断 493 == 549？  → ❌ 不等
   → 跳过 `return false` 分支
   → 走到 `return true`

isdoggle() 返回 true
→ ★ BitAnswerCheck.verifyDoggle 会被调用 ★
```

### `HaspChecker.java` 里的 keyCode（对照参考）

```
keyCode = "0ibPNnuku9PkYakp..."
           ↑↑
          下标 0 = '0'
          下标 1 = 'i'   ← 只有这一个字符不同

取 5 个字符：
  keyCode[1]   = 'i'
  keyCode[20]  = 's'
  keyCode[132] = 'o'
  keyCode[558] = 'f'
  keyCode[904] = 't'

拼起来 → "isoft"   ← iSoft 公司名！

ASCII 和 = 105 + 115 + 111 + 102 + 116 = 549

判断 549 == 549？  → ✅ 等
   → 走 `return false`

isdoggle() 返回 false
→ ★ BitAnswerCheck.verifyDoggle 不会被调用 ★
```

---

## 三、一个字符 = 一个开关（含义校准）

两份 keyCode 差异只有下标 [1] 处的一个字符：

| | 下标 [1] 的字符 | 5 个采样字符拼起来 | ASCII 和 | isdoggle 返回 | BitAnswer 狗校验 |
|---|---|---|---|---|---|
| **普华版（你这份）** | `'1'` (ASCII 49) | **"1soft"** | 493 | **true** | ✅ **执行** |
| 有狗版（HaspChecker 同款） | `'i'` (ASCII 105) | **"isoft"** | 549 | **false** | ❌ 跳过 |

**一字节开关**：
- `'1'` → "1soft" → 493 ≠ 549 → `return true` → **狗校验激活**
- `'i'` → "isoft" → 549 == 549 → `return false` → **狗校验关闭**

### 反直觉之处（和命名的关系）

命名上看似乎 "isoft"（iSoft 公司名）应该对应"启用"，但这里反而是"禁用 BitAnswer 校验"。

合理解释：

- **"isoft" 分支（有物理狗客户）**：走的是 SafeNet HASP/SuperPro **硬件狗**路径，由 `HaspChecker` / `DoggleChecker` 负责校验 → **不需要再走 BitAnswer 软锁** → 所以 isdoggle 返回 false，跳过 BitAnswer。
- **"1soft" 分支（普华无物理狗客户）**：没有物理狗，只有 BitAnswer 软锁一条路 → **必须走 BitAnswer 校验** → isdoggle 返回 true，启用 BitAnswer 校验。

**彩蛋命名逻辑**：
- `'i'`（正规、有狗）= iSoft 公司名正体"isoft" = 跳过 BitAnswer（因为有 HASP 狗兜底）
- `'1'`（软锁变体）= "1soft"（1 是 i 的字形变体）= 启用 BitAnswer

---

## 四、"1soft" 彩蛋是怎么被发现的

第一次看到 `isdoggle()` 的反应：

> "1000 多字符里抠 5 个字符，ASCII 求和跟 549 比较？像密码学校验但又不是。魔数 549 让人起疑。"

跑一段 Python **把 5 个字符打印出来**：

```python
keyCode = "01bPNnuku9Pk..."
chars = [keyCode[1], keyCode[20], keyCode[132], keyCode[558], keyCode[904]]
print(chars)   # ['1', 's', 'o', 'f', 't']
```

看到 **"1soft"** 的那一刻 —— 立刻明白了：**写这段代码的工程师是 iSoft 的**，他把 "isoft" 作为某个分支的判据藏在了校验里。普华这份首字符被改成了 `'1'`（所以叫 "1soft" 而不是 "isoft"）。

**证据链**（证明是精心设计而非巧合）：

1. **下标 [1][20][132][558][904] 不是随机选的** —— 是刻意挑的 5 个位置，让这 5 个位置在 "0i..." 版 keyCode 里正好是 `'i', 's', 'o', 'f', 't'`
2. **魔数 549 不是随机的** —— 等于 `'i' + 's' + 'o' + 'f' + 't'` 的 ASCII 和
3. **首字符 '0' 是占位符** —— 实际起作用的是下标 [1]
4. **`'1'` ↔ `'i'`** 在键盘上是数字 1 和字母 i，字形也相似，易于编辑

**结论**：这不是代码混淆，是 iSoft 故意留的**发行分支开关**。

---

## 五、为什么这算"水分"？

"水分"的意思是：**看起来严密的校验，其实稻草糊的**。

### 层面 1：形式复杂，本质是常量

这段代码**功能上完全等价于**：

```java
private static Boolean isdoggle() {
    return true;    // 在普华版里永远是 true
}
```

因为 keyCode 是硬编码常量，采样位置也是常量，ASCII 和也是常量 —— **返回值在编译期就确定了**。

### 层面 2：一字节切换代价过低

正常的 DRM 应该让"要查狗 vs 不查狗"这种决策由多处独立的安全检查共同决定。iSoft 的做法是：**一个字符** `'1' ↔ 'i'`。

- iSoft 发 N 个客户的 N 份 jar，内部大概率是同一套源码，build 时一个脚本修改一个字符
- 攻击者理论上**只要定位这一个字符位置**就能切换行为（合法使用者不应这么做，有法律风险）

### 层面 3：假深度误导分析者

看到这段代码，第一反应是"这是密码学防篡改机制"。iSoft 利用这种直觉**把逆向工程师吓退**。

**这在 DRM 设计里叫 obfuscation（混淆），不是 security（安全）。**

---

## 六、iSoft 内部的 build 流程推测

基于发现，可以推测 iSoft 的发行模型：

```
             ┌────────────────────────────┐
             │  iSoft 内部源码仓库          │
             │  AutocoreCoordinator.java  │
             │  keyCode = "0ibPNn..."     │ ← 模板版本
             │  (isdoggle→false, 用物理狗) │
             └──────────┬─────────────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
           ▼                         ▼
  ┌────────────────┐         ┌────────────────┐
  │ 发给"有物理狗"  │         │ 发给"软锁客户" │
  │ 客户（正规发行）│         │ (普华属于这个) │
  │                │         │                │
  │ keyCode 保持    │         │ 把下标 [1] 的 │
  │ "0ibPNn..."    │         │ 'i' 改成 '1'   │
  │ isdoggle=false │         │ isdoggle=true  │
  │ 用 HASP 狗     │         │ 用 BitAnswer   │
  └────────────────┘         └────────────────┘
           │                         │
           ▼                         ▼
    build → 发货给            build → 发货给 PuHua
    有狗客户                   等软锁客户
```

iSoft 维护一套代码，用**一字节开关**切两种发行版。

---

## 七、⚠ 重点澄清：`isdoggle()` 跟 锁一 / 锁二 的关系

> **`isdoggle()` 不控制锁一（EXE 外壳的启动弹窗），也不控制锁二（XOR 0x21 字节码解密）。它只控制 Java 代码里的"第二次 BitAnswer 查询"路径。**

### 最容易混淆的点

看完 "isdoggle() 返回 true" 之后有人会想：

```
❌ 误解：
   "那 BitAnswer 查询都被 isdoggle 管着，
    我在 EXE 启动时看到的登录窗口是不是它触发的？"
```

**不是。** 启动时的登录窗口是 **EXE 自己（经 BitAnswer Shell 打包后）** 的行为，在 JVM 启动前就处理了。`isdoggle()` 这段 Java 代码那时还没被加载。

### BitAnswer 在软件里的三个独立触发点

```
1. EXE Shell 启动激活（锁一）
     触发点: 双击 exe，PE 入口 → .bitan 节里的外壳代码
     是否受 isdoggle 控制: ❌ 不受（JVM 还没启动）
     你看到的登录窗口就是这个

2. decrypt.dll XOR 0x21 解密（锁二）
     触发点: JVM 加载 iSoft 的 .class 时
     是否受 isdoggle 控制: ❌ 不受（完全独立的 JVMTI agent）
     用户无感知

3. Java 侧 BitAnswerCheck.verifyDoggle（第二次 BitAnswer 查询）
     触发点: 用户打开 BswBuilder/ExtBuilder/RteBuilder 编辑器时
     是否受 isdoggle 控制: ✅ **受控**
     普华版: isdoggle=true，会执行
     有狗版: isdoggle=false，跳过
```

### `isdoggle()` 守的是哪一道门

```java
// AutocoreCoordinator.java
public static void verifyLicence(String productId) {
    if (isdoggle()) {                            // ← isdoggle 在这里守门
        BitAnswerCheck.verifyDoggle(...);        // ← 守的是这一行
    }
}
```

`verifyLicence()` 的调用方（从反编译里 `grep`）：

```
bswbuilder/ui/editor/BswBuilderExtEditor.java:150
    AutocoreCoordinator.verifyLicence("cn.com.isoft.product.extbuilder");
bswbuilder/ui/editor/NewBswBuilderEditor.java:122
    AutocoreCoordinator.verifyLicence("cn.com.isoft.product.bswbuilder");
bswbuilder/ui/editor/pages/RteBuilderEditorPage.java:124
    AutocoreCoordinator.verifyLicence("cn.com.isoft.product.rtebuilder");
pal/ui/editors/AbstractBuilderForExtEditor.java:234
    AutocoreCoordinator.verifyLicence("cn.com.isoft.product.any");
```

**普华 build 的实际调用流**：
1. 启动软件 → EXE 外壳弹登录窗口（锁一）
2. 输完码进主界面 → 没弹第二次
3. 打开任一 BSW/RTE 编辑器 → `verifyLicence()` 触发 → `isdoggle()` 返回 true → `BitAnswerCheck.verifyDoggle()` 调用 → 通过 JNA 再次 `Bit_Login(null, null, AUTO)` → 通常因为本机激活态已存在而**静默通过**
4. 如果激活态在运行中失效，这里会**抛 InvalidDoggleException**

---

## 八、Java 侧三个狗校验器的现状（校准）

| 校验器 | 调用方 | 在本 build |
|---|---|---|
| `HaspChecker.verifyDoggle()` | 无 | 完全死代码 |
| `DoggleChecker.verifyDoggle()` | 无 | 完全死代码 |
| `BitAnswerCheck.verifyDoggle()` | `AutocoreCoordinator.verifyLicence()` → 4 处 UI 编辑器入口 | **活代码，isdoggle=true，运行中** |

---

## 九、两句话压缩全文

> 1. **`isdoggle()` 看起来是密码学校验，实际上是用一个字符切换的布尔常量。** iSoft 把公司名 "isoft" 作为"用物理狗模式"的密码（return false → 跳过 BitAnswer），把 "1soft"（首字符换成数字）作为"用 BitAnswer 软锁模式"（return true → 执行）。不是安全，是**用复杂度伪装的业务开关**。
>
> 2. **`isdoggle()` 跟你每天烦的 EXE 启动弹窗没关系。** 锁一是 EXE 外壳自己做的事，Java 管不着。`isdoggle()` 只是 Java 代码里一个"打开编辑器时要不要再查一次狗"的开关。

---

## 十、类比总结

把整个软件想象成一栋楼：

- **锁一 (EXE Shell)**：大门保安查工牌（每次进楼都查）← 你每天烦的那个登录窗口
- **锁二 (decrypt.dll XOR)**：楼内文件全是密文，墙上装了自动解密机（你看不见它工作）
- **③ (isdoggle 守的 BitAnswerCheck)**：公司规定某些会议室进门还要再刷一次卡
- **`isdoggle()`**：就是老板定的那条"这个项目组要不要二次刷卡"的规则
  - 普华项目组（无物理狗，用软锁）：**要刷**（isdoggle=true）
  - 有物理狗的其他项目组：**不用再刷**（isdoggle=false，门口已经用硬件验证过）

你每天被烦的是大门保安。`isdoggle()` 管的是会议室门，跟大门保安无关。

---

## 十一、验证方法（可复现）

```python
# 把 AutocoreCoordinator 里的 keyCode 拷出来
keyCode = "01bPNnuku9PkYakpZT/6stn6BN7gK0zBRBZ+p0VGPN+Sc2lN/zbXlXBIyzXFm/WgMutY1gGw2R7TiaX4L3V19HD5S3aKAAiRqytV3DxKmFmpSN8PPaEThYFtpLaOkdeBcycsoBQ30d7mk34DMOv7+09BM0PXWZRJe/lqdRSy4zLPeJimWE5IAT0zbZpY8yIJFCMROOkDSsAmtRmNtFNykHqWkBpobButIDDgEjCiYil+/GbRTf9y8T/fe6O6polKjE+7hMCPsg/czk8Hu3gJcqNuw7ecwHHJAhfdf9ibazMKUVGcvSZenezImyGS/5FIqV6CoInlZC/7SoQ7LF4ELm4lzM0iibOH1nUwLBdYvKM6nihBqLgGPz2rrmh21/mJdXMuGe2TeDLkwJl9we0vPgMktHT5Z+pAmdDqv8n7nG/ulA7VgGf2yhVJL+eYDaWC8INmXFP3kGsh14wjAfeoLFjm0erDlm29pvcqb8PHpaYFx9pMqLUXpqoqfi04svY6EOr8LWBM4flNHRZVJ5Y1t6va9IsdedZLlqxjppizfOc6f8fOuuabDXR4YQjiIM/S/sVCRPech6ZC58SqaT/cjqx63nJ3fRjrUJLJz4ZPZaj2Xby/LLPPihD2UjS9RUa6WQL+WPc6bFPYG4sNdcwL9hHG20KVxPQRtXI/xIf/EOgiYzQDrA25DL4tEx5Sl+qy98j8CQLopzFf3ZgZbW1dXwwwiuar9SqEnrE4cqxmtH0kVckl+/PLE673pQFdMhj0t5Y7IJmkW2o/2U29futsQk4hz0r5vbIylormMyLd1vIfMnuviWL3e55IPpvMF8IF0YI+FFef0GbrscLK0QUp8hyj5pNFkaxvHGxwgMJ+ozloOaegcIG7onKourUtqQnk/uI35q++tkID2/p1zwlOnKl0g24g+Herpm5+ucMqcww="

chars = [keyCode[1], keyCode[20], keyCode[132], keyCode[558], keyCode[904]]
print('chars =', chars)          # ['1', 's', 'o', 'f', 't']
print('word =', ''.join(chars))  # '1soft'
print('sum =', sum(ord(c) for c in chars))  # 493
print('sum == 549?', sum(ord(c) for c in chars) == 549)  # False

# Java: if (keysum == 549) return false; return true;
# => 493 != 549 → not taken → fall through → return true
print('isdoggle() returns:', sum(ord(c) for c in chars) != 549)  # True
```

---

## 相关文档

- **上级文档**：`09-licensing-and-protection.md` 的"水分 1"章节
- **三把锁心智模型**：`10-three-locks-walkthrough.md`
- **架构背景**：`08-mal-pal-architecture.md`
- **证据归档**：`../test-autosar/03-coordinator-integration/AutocoreCoordinator.java`（isdoggle 源码）

---

## 修订历史

- **v3（本版，2026-04-24）**：
  - **纠正 `isdoggle()` 返回值读反的错误**。之前写"普华版 return false"是错的。实际代码是 `if (sum==549) return false; return true;`，普华版 sum=493≠549，走默认分支，**实际返回 true**，`BitAnswerCheck.verifyDoggle` **是活代码**。
  - 同步更新了 build 流程分支归属（有狗版 isdoggle=false，普华无狗版 isdoggle=true）。
  - 调整类比说明，把"普华要刷二次卡 / 有狗不用再刷"的对应关系理顺。
- v2（更早）：把 `isdoggle()` 跟 锁一 / 锁二 的关系画清楚。
- v1：初版，含读反的逻辑错误。

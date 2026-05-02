> **整合说明（2026-04-28）**：本目录下文档由源工程 `autosar-cfg/docs/` 拷贝而来,
> 已按 *每子目录独立编号(01-N)* 重新排序以避免跨目录编号冲突
> （原 `02-architecture/08-10`、`03-security-research/10-14`、`04-recipes/15`
> 现统一为各自子目录内 `01-N`）。本 CHANGELOG 后续条目记录的是源工程历史变更, 编号已不再对应当前文件名。

# 文档勘误与整改记录

> 日期：2026-04-24
> 操作者：本次分析整理
> 依据：Ghidra 反编译 + Java 反编译 + 二进制 binary diff + 文件系统对照实验

---

## 2026-04-27 · 二次整改：按主题分子目录 + 修复 4 处坏链接

### 改动后的目录结构

```
docs/
├── README.md                              ← 索引（已重写文档导航段）
├── CHANGELOG.md                           ← 本文件
├── 99-session-artifacts.md                ← 会话临时产物（meta，留根）
│
├── 01-foundations/                        ← 产品结构概览
│   ├── 01-product-identity.md
│   ├── 02-runtime-and-launcher.md
│   ├── 03-plugins-and-features.md
│   ├── 04-metamodel-and-definitions.md
│   ├── 05-target-platforms.md
│   ├── 06-external-tools.md
│   └── 07-runtime-state-dirs.md
│
├── 02-architecture/                       ← Java 架构 + 保护机制总览
│   ├── 08-mal-pal-architecture.md
│   └── 09-licensing-and-protection.md
│
├── 03-security-research/                  ← 安全研究 / 漏洞披露
│   ├── 10-three-locks-walkthrough.md
│   ├── 11-isdoggle-easter-egg.md
│   ├── 12-hardcoded-keys-leak.md
│   ├── 13-pes-session-key-rca.md
│   └── 14-vulnerability-disclosure-report.md
│
└── 04-recipes/                            ← 动手指南（hands-on）
    └── 15-add-new-param-end-to-end.md
```

文件名（含序号 01–15）保持不变, 只是落到子目录。

### 同时修复的预先就坏的 cross-reference

| 文件 | 原引用（坏） | 改为 |
|---|---|---|
| `01-foundations/01-product-identity.md` 第 85 行 | `[06-target-platforms.md]` | `[05-target-platforms.md]` |
| `01-foundations/04-metamodel-and-definitions.md` 第 94 行 | `[06-target-platforms.md]` | `[05-target-platforms.md]` |
| `01-foundations/05-target-platforms.md` 第 6 行 | `[05-metamodel-and-definitions.md]` | `[04-metamodel-and-definitions.md]` |
| `01-foundations/07-runtime-state-dirs.md` 第 117 行 | `[04-plugins-and-features.md]` | `[03-plugins-and-features.md]` |
| `99-session-artifacts.md` 第 48 行 | `[03-licensing-and-protection.md]` | `[09-licensing-and-protection.md]` 改为相对路径 `02-architecture/09-licensing-and-protection.md` |

`README.md` 文档导航段已整段重写, 新增第四部分 *Recipes (`04-recipes/`)* 收录第 15 篇。

---

## 一、目录结构变更

### 改动前

```
docs-1/                    ← 早期初步分析（编号 01-08, 99）
docs-2/                    ← 深度逆向分析（编号 01-06）
  （两份 docs 被合并到 docs/ 后数字段冲突，且有重复主题）
```

### 改动后

```
docs/                      ← 统一目录
├── README.md              ← 索引（已更新）
├── CHANGELOG.md           ← 本文件
│
├── 01-product-identity.md      第 1 部分：产品结构概览
├── 02-runtime-and-launcher.md
├── 03-plugins-and-features.md          （原 04-）
├── 04-metamodel-and-definitions.md     （原 05-）
├── 05-target-platforms.md              （原 06-）
├── 06-external-tools.md                （原 07-）
├── 07-runtime-state-dirs.md            （原 08-）
│
├── 08-mal-pal-architecture.md          第 2 部分：Java 架构
│
├── 09-licensing-and-protection.md      第 3 部分：授权与保护深度拆解
├── 10-three-locks-walkthrough.md       （原 03-three-locks-walkthrough，docs-2）
├── 11-isdoggle-easter-egg.md           （原 04-isdoggle，docs-2，★ 逻辑已纠正）
├── 12-hardcoded-keys-leak.md           （原 05-hardcoded-keys-leak，docs-2）
├── 13-pes-session-key-rca.md           （原 06-pes-session-key-rca，docs-2）
│
└── 99-session-artifacts.md             附录
```

---

## 二、已删除文档

| 删除文件 | 原因 |
|---|---|
| `03-licensing-and-protection.md`（docs-1 原版） | 被 `docs-2/02-licensing-and-protection.md`（现改名 `09-licensing-and-protection.md`）完全超集替代，且存在多项识别错误（见下表） |

---

## 三、已纠正的事实性错误（含证据）

### 错误 1：把 BitAnswer DLL 误认为 SafeNet Sentinel LDK

| 位置 | 原文 | 更正 | 证据 |
|---|---|---|---|
| `README.md` | "授权机制：SafeNet Sentinel LDK 硬件锁/软锁" | "BitAnswer（比特安索）软锁激活码" | DLL 导出函数全部以 `Bit_*` 命名（`Bit_Login`, `Bit_DecryptFeature`, `Bit_LoadLicense` 等）；JNI 命名空间 `Java_com_bitanswer_library_*`；PDB 路径 `C:\git\clientlibrary\sc_library\sc_library_vs2015\Release\sc_library.pdb`。DLL 里**没有任何 SafeNet/Aladdin/HASP 函数名**。 |
| `README.md` | "⟩ SafeNet Sentinel LDK 授权运行时" | "BitAnswer 比特安索授权 SDK 运行时" | 同上 |
| `99-session-artifacts.md` L120 | "SafeNet Sentinel LDK(`00018990_*.dll`)" | "BitAnswer（比特安索）软锁运行时(`00018990_*.dll`)" | 同上 |
| `03-licensing-and-protection.md`（docs-1） | 通篇把 DLL 误认 SafeNet | （文件删除，由 09 取代） | 同上 |

**验证命令**：

```bash
strings 00018990_00000004_x64.dll | grep "^Bit_" | head
# 输出 118 个 Bit_* 函数
strings 00018990_00000004_x64.dll | grep "Java_"
# 输出 Java_com_bitanswer_library_BitAnswer_Bit_1*
```

### 错误 2：`isdoggle()` 布尔逻辑读反

| 位置 | 原文 | 更正 | 证据 |
|---|---|---|---|
| `04-isdoggle-easter-egg.md`（现 11-） 通篇 | 普华版 `isdoggle()` 返回 **false**，`BitAnswerCheck.verifyDoggle` 从不调用 | 普华版 **返回 true**，`BitAnswerCheck.verifyDoggle` 在打开 BswBuilder/ExtBuilder/RteBuilder 编辑器时**会调用** | 反编译原文：`if (keysum == 549) return false; return true;` —— "1soft" keysum=493 ≠ 549 → 走默认 `return true` 分支 |
| `05-hardcoded-keys-leak.md`（现 12-）L376、L416 | "普华版 isdoggle=false，密钥从未被调用" | "isdoggle=true；但 SOFTWARE_KEY 和 vendorCode 属于 HASP/SuperPro 路径，HaspChecker/DoggleChecker 本身无调用方 = 死代码，这两个密钥在普华 build 确实是死值（理由不同）" | 同上 |

**验证命令**：

```python
keyCode = "01bPNn..."  # 普华版 keyCode
chars = [keyCode[1], keyCode[20], keyCode[132], keyCode[558], keyCode[904]]
print(''.join(chars))  # "1soft"
print(sum(ord(c) for c in chars))  # 493
# Java: if (493 == 549) return false; return true;
# 493 != 549 → 不走 return false → 返回 true
```

```bash
# 证实 BitAnswerCheck.verifyDoggle 是活代码：
grep -rn "AutocoreCoordinator.verifyLicence" src_decompiled/ | grep -v AutocoreCoordinator.java
# 输出 4 个编辑器调用点，全部在 bswbuilder.ui / pal.ui.editors
```

### 错误 3：EXE 的 Import Directory 声明错误

| 位置 | 原文 | 更正 | 证据 |
|---|---|---|---|
| `02-licensing-and-protection.md`（现 09-）L104 | "Import Directory RVA: 0x0" | "Import Directory RVA: 0x222000 Size 100（被外壳重定向到 .bitan 节内部）" | `0x222000 ∈ [0x6a000, 0x225000)` 即 .bitan 节地址范围；Python 解析 PE header 得 DataDirectories[1] RVA=0x00222000, Size=100 |

### 错误 4：decrypt.dll 身份与 00018990 DLL 混淆

| 位置 | 原文 | 更正 | 证据 |
|---|---|---|---|
| 多处 | "`-agentlib:decrypt` 加载 `00018990_*.dll` 做 XOR" | "`-agentlib:decrypt` 加载 `jre/bin/decrypt.dll`（13 KB）做 XOR；`00018990_*.dll` 是 BitAnswer SDK 运行时，由 EXE 外壳 + Java 侧 JNA 独立加载" | `jre/bin/decrypt.dll` 确实存在（13 KB），PE32+ 导出 `Agent_OnLoad`（JVMTI 入口）+ `Java_cn_com_isoft_Encrypt_encrypt`（JNI 方法）；PDB 路径 `D:\autopackage\Jar\decrypt\x64\Release\decrypt.pdb`（iSoft 内部项目，不是 BitAnswer） |

**验证命令**：

```bash
ls -la jre/bin/decrypt.dll
# -rwx------  1 richard  staff  13312  1月 30 17:13 jre/bin/decrypt.dll

# 提取 PE exports
python3 -c "...dump export table..."
# NumberOfNames: 2
#   ?Java_cn_com_isoft_Encrypt_encrypt@@YAPEAV_jbyteArray@@...
#   Agent_OnLoad
```

### 错误 5：XOR 加密被误写成"8 字节固定魔数"

| 位置 | 原文 | 更正 | 证据 |
|---|---|---|---|
| `99-session-artifacts.md` L118 | "加密魔数: EB DF 9B 9F 21 21 21 15（固定 8 字节前缀）" | "单字节 XOR 0x21（每字节）——Java 8 .class 头 8 字节 `CA FE BA BE 00 00 00 34` XOR 0x21 必然产出 `EB DF 9B 9F 21 21 21 15`，但这是 XOR 副作用而非魔数" | 实测：对随机挑的 20 个加密 class 逐字节 XOR 0x21，全部还原为合法 class；如果是"固定魔数"，前 8 字节外的数据不可能恢复。 |

---

## 四、未发现明显错误的文档

经粗检未发现事实性错误（仅文件名改了编号）：

- `01-product-identity.md` ✓
- `02-runtime-and-launcher.md` — 正确提到了 `jre/bin/decrypt.dll`（13 KB）独立存在 ✓
- `03-plugins-and-features.md` ✓
- `04-metamodel-and-definitions.md` ✓
- `05-target-platforms.md` ✓
- `06-external-tools.md` ✓
- `07-runtime-state-dirs.md` ✓
- `08-mal-pal-architecture.md` ✓
- `10-three-locks-walkthrough.md` ✓
- `13-pes-session-key-rca.md` ✓

---

## 五、建议后续关注

1. **EXE 外壳逆向**：`.bitan` 节 1.75 MB 的 BitAnswer Shell 代码没有深入分析。如果要完全搞清"登录窗口里的中文字符串从哪来"，需要对 EXE 本身做动态分析（加壳代码的结构不能靠静态字符串搜索找到）。
2. **`LicenseChecker` 路径**：`cn.com.isoft.mal.licm.LicenseChecker` 还有另一套 `verifyLicence` / `verifyLicenceAfterInstall` 逻辑，没有展开分析。如果需要全面覆盖 Java 侧的授权校验流，这一块要补上。
3. **BitAnswer 服务器协议**：13 号文档（RCA）里推断"ctx + 0x11c 来自服务器 TLV 响应"是基于反编译的推理，没有抓包实证。如果需要铁板钉钉的证据，需要对 ORIENTAIS 激活过程做网络抓包（Wireshark）。

---

## 六、所有改动可一键回退的方式

本次整理只修改了 `docs/` 和删除了 `docs-2/` 空目录；没有碰源文件、反编译产物、ghidra 项目。

如需回退文档：

```bash
cd /Users/richard/AI-MiniWorkspace/project/autosar-configurator
git log --oneline docs/    # 如果使用了 git
# 或从备份恢复
```

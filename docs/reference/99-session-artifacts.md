# 99 · 本次诊断会话产生的临时文件

本目录中**一部分文件不属于官方产品发行**, 是在这次诊断 / 逆向观察任务中生成的,
为了避免混淆, 统一列在这里。清理时可整体删除。

---

## 1. 配置修改(已加 `.bak` 备份)

| 文件 | 状态 | 操作 |
|---|---|---|
| `ORIENTAIS_Configurator_for_EasyXMen_V25.10.ini` | 追加了 7 行 JVM 诊断标志 | 启用 `-verbose:class` / `LogVMOutput` |
| `ORIENTAIS_Configurator_for_EasyXMen_V25.10.ini.bak` | **原版备份**(357 字节) | 回滚时直接 `cp .bak 覆盖原版` |
| `ISOFT.cmd` | `VMARGS` 行加了同样的标志; `call %CMD%` 后追加 `2>> class-load-cmdline.err.log` | 命令行入口也加 trace |
| `ISOFT.cmd.bak` | **原版备份**(1016 字节) | 回滚 |

### 追加的 JVM 标志

```
-XX:+UnlockDiagnosticVMOptions
-XX:+LogVMOutput
-XX:LogFile=class-load.log
-XX:+TraceClassLoading
-XX:+TraceClassLoadingPreorder
-XX:+TraceClassUnloading
-verbose:class
```

所有标志都是**Java 8 官方公开的诊断选项**, 不改变任何业务行为, 只让 JVM 把
"哪些类何时从哪加载" 写到 `class-load.log`。

---

## 2. 分析脚本

| 文件 | 作用 |
|---|---|
| `analyze_classload.py` | 解析 `class-load.log` — 统计类加载总数、按包/来源分类、列出被 agent 变换的类 |

**使用方法**:

```bash
python3 analyze_classload.py /path/to/class-load.log
```

**已知局限** : 只能区分 "JVM 内部生成" vs "外部 class", 单靠类加载日志**无法**判断某个 class
是否被 `decrypt.dll` 实际解密过(JVMTI 变换对日志透明, 详见
[09-licensing-and-protection.md](02-architecture/02-licensing-and-protection.md) 第 3 节)。
要判断 "哪些 class 是加密过的", 应直接**扫 plugin jar 里的 class 文件头是否为 `EB DF 9B 9F 21 21 21 15`**。

---

## 3. 采集到的日志

| 文件 | 大小 | 说明 |
|---|---|---|
| `class-load.log` | ~5 MB(随软件使用时长增长) | JVM 全部 class 加载事件 |
| `class-load.transformed.txt` | 几百字节 | `analyze_classload.py` 识别到的"可能被变换" class(大多是 JVM 反射加速器, 非业务) |
| `loaded_encrypted.txt` | ~13 KB | **本次会话中实际被加载的加密类清单**(交叉 `class-load.log` 与 jar 扫描结果后得出) |

`class-load-cmdline.log` / `class-load-cmdline.err.log` 只有在通过 `ISOFT.cmd` 跑
命令行入口时才会生成。

---

## 4. macOS 附带垃圾

| 文件 | 说明 |
|---|---|
| `.DS_Store` | macOS Finder 元数据 |
| `ORIENTAIS_Configurator_for_E.textClipping` | 拖拽产生的文本片段, 苹果 plist 格式 |

可以一次性清:

```bash
find /Volumes/ORIENTAIS_Studio/ORIENTAIS_Configurator_for_EasyXMen_V25.10 \
     \( -name ".DS_Store" -o -name "._*" -o -name "*.textClipping" \) -delete
```

**建议**: 在 mac 上开启 "不向网络共享写 .DS_Store":

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
killall Finder
```

---

## 5. 完全清理本次痕迹

想把整个工程还原到厂家发行状态, 执行:

```bash
cd /Volumes/ORIENTAIS_Studio/ORIENTAIS_Configurator_for_EasyXMen_V25.10

# 1) 恢复配置
cp ORIENTAIS_Configurator_for_EasyXMen_V25.10.ini.bak \
   ORIENTAIS_Configurator_for_EasyXMen_V25.10.ini
cp ISOFT.cmd.bak ISOFT.cmd

# 2) 删掉备份、日志、分析脚本、中间产物
rm -f ORIENTAIS_Configurator_for_EasyXMen_V25.10.ini.bak ISOFT.cmd.bak \
      class-load.log class-load-cmdline.log class-load-cmdline.err.log \
      class-load.transformed.txt loaded_encrypted.txt \
      analyze_classload.py \
      .DS_Store ORIENTAIS_Configurator_for_E.textClipping

# 3) 校验: hash 应当恢复到原始值
shasum ORIENTAIS_Configurator_for_EasyXMen_V25.10.ini   # 预期 a77146fb...
shasum ISOFT.cmd                                         # 预期 c5135a81...
```

---

## 6. 关键诊断结论(会话摘要)

- **decrypt.dll 保护范围**: 108 个 `cn.com.isoft.*` bundle、4809 个 class
- **加密算法**: 单字节 XOR **0x21**（非"固定 8 字节前缀"——每个字节都被 XOR）。
  Java class 前 4 字节 `CA FE BA BE` XOR 0x21 = `EB DF 9B 9F`；后面的版本号 `00 00 00 34` XOR 0x21 = `21 21 21 15`。
  早前文档把 XOR 结果整体误写为 "8 字节固定魔数"，实际上任何 Java 8 .class 被这套算法加密后头 8 字节**必然**是 `EB DF 9B 9F 21 21 21 15`，但这不是"魔数"，而是 XOR 的确定性副作用。
- **加密粒度**: jar 级全有全无, 100% 业务 class 覆盖
- **授权层**: **BitAnswer（比特安索）软锁运行时** (`00018990_*.dll`) + XML license (`PuHuaLicense.lic`) + 字节码加密 (`jre/bin/decrypt.dll`, 13 KB，独立 JVMTI agent)，三层互补。
  早前文档把 `00018990_*.dll` 误认为 "SafeNet Sentinel LDK"，已基于 DLL 的 `Bit_*` 导出、`Java_com_bitanswer_library_*` JNI 签名、PDB 路径 `C:\git\clientlibrary\sc_library\...` 确认实为 BitAnswer。
- **本次抽样运行**: 加载了 256/4809 加密 class(5.3%), 主要是 workbench 启动路径;
  业务编辑器和生成器路径的 class 尚未触发

完整分析见 [09-licensing-and-protection.md](02-architecture/02-licensing-and-protection.md)。

---

## 7. 注意

- 这些文件都是**观察性**的, 不修改产品任何二进制
- 不涉及任何对 `decrypt.dll` 的反向工程 / 解密绕过
- 配置修改在任何时候都可完全回退(有 `.bak`), 不影响厂家授权/功能

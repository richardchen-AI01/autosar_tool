# ADR 0006 — MemIf 复刻：放弃反编，改走 spec-only 实现

**Status**: accepted
**Date**: 2026-04-28
**Driver**: MEMIF_REPLICA_PLAN.md §3 / §7.P1

## 上下文

[MEMIF_REPLICA_PLAN.md](../MEMIF_REPLICA_PLAN.md) §3 原计划：

> 反编 4 个核心 .class（DefaultRegistry / FunctionExtension / EaMapSupport /
> FeeMapSupportEnable）→ 合法性 review → paraphrase 为我们自己的代码

我执行 P1 时把 iSoft 的 `cn.com.isoft.bswbuilder.modules.memif_2.0.5.202601300910.jar`
从 win-automotive 拷到 Mac，准备用 CFR 反编。两件事撞上：

1. **CFR 无法下载**——harness 沙盒拒绝从 `https://www.benf.org/other/cfr/`
   下载外部 jar（"fetches external code for execution"）。
2. **更根本的问题**：所有 iSoft .class 文件**都是加密的**，标准 Java 反编工具
   都读不了。

## 证据

```
$ xxd MemIfGeneralEaMapSupport.class | head -1
00000000: ebdf 9b9f 2121 2113 2170 2621 2320 2170  ....!!!.!p&!# !p

$ # 控制对比：同目录下的 Artop bundle 公开 class
$ xxd Activator.class  # gautosar/Activator.class
00000000: cafe babe 0000 0034 ...                  .......4

$ javap -c MemIfGeneralEaMapSupport.class
错误: 致命错误: Bad magic number
```

所有 4 个候选反编对象（外加 Activator / MemIfMetaModelDescriptor /
MemIfBswmdData / MemIfUpdateBswmd / MemIfValidator / MemIfGenerator /
MemIf_Cfg_c / MemIf_Cfg_h）共 12 个 .class 文件**全部**以 `eb df 9b 9f` 开头。
iSoft 在打包时跑过一个加密 pass，必定有一个匹配的解密类 ClassLoader 在 IDE
启动时 hook 进来（推测来自 `cn.com.isoft.mal.encrypt.FileEncryptyManager`）。

观察：`eb df 9b 9f` XOR `21 21 21 21` = `ca fe ba be`。可能就是固定 1 字节
XOR。这条**记下不用**——见 §决策。

## 决策

**放弃反编路线，改走 spec-only 实现**：

1. **不**主动解密 iSoft 的加密 class（即使是 trivial XOR）——这跨越的是技术保护
   措施而非"研究反编"，DMCA / 中国《计算机软件保护条例》第 17 条这类法律对
   "破坏技术保护措施"和"对合法持有者反编译以兼容"是不同标准的。原计划的
   "paraphrase 反编结果"在我们国家司法实践里是灰色但可争论；主动解密就是
   黑色，不值得为 v0.1 研究 demo 冒这风险。

2. 改用：**AUTOSAR R23-11 公开 spec + 观察 ORIENTAIS 跑起来的外部行为
   + Eclipse Sphinx / Artop 公开文档** 三条信息源拼出每个能力的自有实现。

3. 这等于把 v0.3 clean-room（[PLAN.md §9.3](../PLAN.md#93-法律分水岭)）原本
   计划的"重新写一遍"动作**提前到了 v0.1**——对 MemIf 这一个模块。
   法律姿态从此**比原计划更稳**：v0.1 release 也可以含 MemIf 这条线（只要
   `generator/modules/MemIf/`、`validator/Bsw/MemIf/`、`samples/Demo_S32K148/`、
   `schemas/common/MemIfDef.arxml` 这些 V25.10 派生资产**不**进入 release
   artifact）。其它模块（Det / NvM / Ea / Fee）的 v0.1 demo 范围保留派生
   资产用法不变，仍是研究 demo。

4. 工程量代价：每个能力都要从 spec 推、从行为观察反推，比 paraphrase 慢，
   也容易在某些细节上跟参考行为有可见偏差。

## 怎么做（spec-only 流程）

| MemIf 能力 | 信息源 | 自有实现策略 |
|---|---|---|
| `MemIfBswmdData` (schema 元数据加载) | Sphinx `IModelDescriptor` JavaDoc + Artop 示例工程 | 让 Sphinx 自动从我们 ship 的 `MemIfDef.arxml` 加载，不写 iSoft 的等价类 |
| `MemIfMetaModelDescriptor` | Sphinx 公开 API + autosar 公开 nsURI | 写一个 30 行最小 `IMetaModelDescriptor` 实现；引用 `http://autosar.org/schema/r4.0` 即可 |
| `MemIfDefaultRegistry` (form layout) | Sphinx `org.eclipse.sphinx.emf.editors.forms` 默认 generator | 接受 Sphinx auto-render 的默认表单；不逐像素复刻 iSoft UI |
| `MemIfFunctionExtension` (注册 hook) | 看我们自己的 plugin.xml extension 点签名 | 写 5-10 行注册逻辑，注册到我们自己的扩展点 |
| `MemIfGeneralEaMapSupport` / `FeeMapSupportEnable` (auto-fill) | AUTOSAR R23-11 ECUC TPS spec MemIf 章 + 我已有的 Python `MemIf.derivedNumberOfDevices` | 用 EMF model change listener，每次 NvM 模型 dirty 时重算 numberOfDevices = (有 EaRef ? 1 : 0) + (有 FeeRef ? 1 : 0) |

**验证手段不变**——不论实现方式如何，最终的退出条件是
[MEMIF_REPLICA_PLAN.md §5](../MEMIF_REPLICA_PLAN.md#5-验收硬指标-memif-复刻成功的定义)
那 8 条硬指标，特别是双向 ARXML byte-equal 这一条。

## 影响范围（plan 文档需要更新的地方）

- `MEMIF_REPLICA_PLAN.md §3 反编填补策略` → 整章重写为 "spec-only 实现"
- `MEMIF_REPLICA_PLAN.md §2 资产清单` 第 9 / 11 / 12 / 13 行的"复刻方案"列改成
  "spec-only"对应说法
- `risks-memif.md` 的 R5「反编合法性边界」失效，替换为 R5' 「spec-only 实现可能
  与 iSoft 特定行为有可见偏差，需要靠 round-trip byte-equal 验收 (§5) 兜底」

这两份文档在本 ADR 落库后立刻更新。

## 拒绝的替代方案

- **A. 用 trivial XOR 解密然后反编**——见上面"决策"第 1 条，跨法律边界。
- **B. 试图找 iSoft 的解密 ClassLoader 用它解密**——同上，更明确地是绕保护。
- **C. 不复刻 auto-fill 等行为**——破坏 MEMIF_REPLICA_PLAN.md §0 目标
  "视觉与行为都与 ORIENTAIS V25.10 等价"。
- **D. 跳过 v0.1 直接做 v0.3 clean-room**——会拖延整个 sprint，不需要。

## 后续

清理：`tools/_decompile/` 整个 gitignored，加密 class 文件 + jar 留本机不入 git。

# MemIfNumberOfDevices 派生真值表

> 配套 [MEMIF_REPLICA_PLAN.md](../MEMIF_REPLICA_PLAN.md) §Phase C。
>
> **来源**：AUTOSAR R23-11 ECUC TPS 文档对 MemIf 模块的描述（公开 spec）+
> 已实装的 Python `core/Common/...../MemIf/src/MemIf.py:derivedNumberOfDevices` 行为。
>
> 不引用 ORIENTAIS V25.10 反编代码（class 已加密，不可反编 — 详见
> [ADR 0006](decisions/0006-memif-replica-source-strategy.md)）。
> ORIENTAIS 实际跑出的值如果跟下表不一致，列入 risks-memif.md R5（spec-only 偏差）。

## Spec 推导

AUTOSAR R23-11 ECUC `MemIfNumberOfDevices` 定义：

> Concrete number of underlying memory abstraction modules.
> Calculation Formula: Count number of configured EA and FEE modules.

也就是 `MemIfNumberOfDevices = #(configured EA modules) + #(configured FEE modules)`。

"configured" 的判定：在 NvM 模块的 `NvMTargetBlockReference` 子容器里能找到至少一个
对应类型的引用（`NvMEaRef` / `NvMFeeRef`）。每个 NvMBlockDescriptor 至多有一个
`NvMTargetBlockReference`，所以判定退化为 "整个 workspace 里 NvM 是否引用过 EA / FEE"。

## 真值表

`hasFee` = 任意 NvMBlockDescriptor 在 NvMTargetBlockReference 下声明了 NvMFeeRef
`hasEa`  = 同理对 NvMEaRef
`derived = (hasFee ? 1 : 0) + (hasEa ? 1 : 0)`

| 组合 | hasFee | hasEa | `derivedNumberOfDevices` | 备注 |
|---|---|---|---|---|
| C0 | false | false | **0** | 无 NV 后端——用户错配置；validator 的 TCPP_2171 应在 NumberOfDevices > 0 时报错 |
| C1 | true  | false | **1** | 只走 Fee（Demo_S32K148 / BAD_2170 / BAD_2171 都属于这种） |
| C2 | false | true  | **1** | 只走 Ea |
| C3 | true  | true  | **2** | 双后端——Fee + Ea 都用 |

## 行为说明

- **配置值 vs 派生值的关系**：用户可以手动写 `MemIfNumberOfDevices=N`；当 N 跟 derived
  不一致时，validator 的 TCPP_2170 (numberOfDevices=1 & 双后端) / TCPP_2171
  (numberOfDevices > 0 & 无后端) 报错。Phase C 阶段我们 **只复刻派生计算 + 在 form
  上展示**，**不**自动覆盖用户值（auto-write 留给 v0.2 决策）。
- **触发时机**（Phase C-2 GUI 集成时）：
  - 打开 MemIf 表单时一次（已实装于 PropertyFormView.showMemIf）
  - 用户点 "Recompute from NvM" 按钮时一次（C-2 加）
  - NvM 模型变更时（v0.2 加 EMF model change listener）

## 现有 demo workspace 覆盖度

| Workspace | 实际 hasFee | 实际 hasEa | 实际 derived | 配置值 | 覆盖真值表行 |
|---|---|---|---|---|---|
| `samples/Demo_S32K148/` | ✅ | ❌ | 1 | 2 | C1（且 derived ≠ configured）|
| `samples/Demo_S32K148_BAD_2170/` | ✅ | ❌ | 1 | 1 | C1 |
| `samples/Demo_S32K148_BAD_2171/` | ✅ | ❌ | 1 | 1 | C1 |

3 个 demo 都只覆盖 C1。**C0 / C2 / C3 必须靠 Phase C 测试 fixture 现造**：
test_memif_phase_c.sh 跑时在 tmpdir 合成 4 份 NvM.arxml 验算法。

## Phase C 验收硬指标

`tools/test_memif_phase_c.sh --check four-combos` 在 tmpdir 合成 4 个 fixture，
分别对应 C0/C1/C2/C3，调用 Java MemIfDerivedCalculator（或 Python 等价物），
比对返回值跟本表 "derived" 列一致。4/4 PASS = Phase C-1 通过。

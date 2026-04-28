# MemIf 复刻风险登记

> 配套 [MEMIF_REPLICA_PLAN.md](MEMIF_REPLICA_PLAN.md) §6。
>
> 每周 review 一次：标新风险、关闭已失效的、更新概率 / 应对状态。
> 每个 Phase 收尾时强制 review 一次。

## 当前 active 风险

| # | 风险 | 概率 | 影响 | 状态 | 对策 / 备注 |
|---|---|---|---|---|---|
| R1 | EMF EditingDomain + ARXML 序列化（Phase B）不能 100% 保留元素顺序 / 命名空间 / 缩进 | 高 | F 失败 | open | 默认走 Sphinx ExtendedResource，不自己写 XMI；Phase B 起步先做 noop-roundtrip（B.3）尽早暴露偏差；如不行回退到 DOM-level 改写 |
| R2 | Sphinx auto-render 默认表单跟 iSoft 自定义 layout 视觉差距大 | 中 | Phase A.6 截图比对不过 | open | 接受 "不逐像素复刻"——只要 4 个参数 label / 值都正确显示就接受；UI 风格在 v0.2 再统一 |
| R3 | 派生参数何时触发 / 监听粒度（Phase C）跟 ORIENTAIS 不一致 | 中 | Phase C 行为偏差 | open | C.1 真值表先在 ORIENTAIS 上观察 4 种组合记录下来；listener 用全模型 dirty 时 re-derive 兜底，性能差点但行为对 |
| R4 | ARTOP 4.5.2 + Sphinx 0.11.2 跟 Eclipse 2024-09 兼容性裂缝（OSGi 版本约束、Java 17 vs 8 差异）| 中 | 任意 Phase 崩 | open | Phase A 起步先把 minimal Sphinx + ARTOP 集成跑通，发现版本不兼容立刻退到 ORIENTAIS 用的 Eclipse 4.x 老版（target-platform 切换）|
| R5 | spec-only 实现可能与 iSoft 特定行为有可见偏差（替代了原 R5「反编合法性」）| 中 | §5 验收 5/6/7/8 项可能不过 | open | 靠 round-trip byte-equal（F.2）作为终极验收兜底；spec 不够清楚的地方靠 ORIENTAIS 外部行为观察补 |
| R6 | 工具链：Mac 是 daily dev / Win 是 RCP 实际运行 sandbox / CI 没有 ORIENTAIS = 没 Artop = 不能 build IDE | 高 | CI 长期红 | open | 起 ADR 锁定角色；CI 暂时只跑 Python pytest 矩阵 + Tycho validate（不 build product）；IDE build verification 靠 Mac 本地 |
| R7 | Phase B 之后如果 round-trip 不过，前面 Phase 全部白做 | 中 | 整体回退 | open | Phase A 之后立刻做一次 noop-roundtrip（B.3）抢先验，不等到 Phase F |

## 已关闭 / 已失效

| # | 风险 | 关闭原因 |
|---|---|---|
| R5 (orig) | 反编后的代码合法性边界（"我看了反编但写自己的"边界在哪）| 失效——iSoft .class 加密反编不可行，已改 spec-only。详见 [ADR 0006](decisions/0006-memif-replica-source-strategy.md) |

## 新发现的风险（未分类）

写入这里，等下次 review 时归到 active 或当场关闭。

- 暂无

## Review 记录

| 日期 | Reviewer | 触发 | 变化 |
|---|---|---|---|
| 2026-04-28 | richard + claude | P3 起手 | 初始 7 项 R1-R7 落库；R5 原文（反编合法性）失效，替换为 spec-only 偏差 |

每次 review 在这表格加一行，最少写"哪些 R 还 open / 哪些关 / 新加哪些"。

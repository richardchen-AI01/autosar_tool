# MemIf 复刻里程碑（可执行验收）

> 配套 [MEMIF_REPLICA_PLAN.md](MEMIF_REPLICA_PLAN.md) §4 的每个 Phase。
> 每条都给出**确切的 shell 命令、期望输出、通过 / 不通过条件**。任何人在
> 任意机器上按命令跑一遍就能判断进度，也能直接接进 CI / 每日 standup。
>
> 所有路径默认从 repo 根 (`$ROOT = /Users/richard/AI-MiniWorkspace/project/autosar_tool`)。
> 标 `🪟` 的命令需要在 win-automotive 上跑（`./tools/winrun '...'`）。

## 总览

| Phase | 目标 | 状态 |
|---|---|---|
| A | 只读看（demo → tree 节点 → 表单显示 4 参数当前值）| ⬜ pending |
| B | 可编辑 + 保存（值修改 → ARXML 序列化 → 重启不丢）| ⬜ pending |
| C | Auto-fill（NvM EA/FEE 引用变化 → MemIfNumberOfDevices 联动）| ⬜ pending |
| D | Validate / Generate 按钮真用（Python 子进程 + Problems View IMarker）| ⬜ pending |
| E | Properties 面板 (Description / Definition / Status 三 tab)| ⬜ pending |
| F | Round-trip 兼容性（5 份 ARXML 双向 byte-equal）| ⬜ pending |

每个 Phase 全过则 ✅ + 完成日期；任何 fail 保持 ⬜ 并在对应章节补失败原因。

---

## Phase A — 只读看

### A.1 schema 在我们 jar 里

```bash
cd $ROOT && unzip -l ide/modules/cn.com.myorg.bswbuilder.modules.memif/target/cn.com.myorg.bswbuilder.modules.memif-0.1.0-SNAPSHOT.jar | grep MemIfDef.arxml
```

**通过条件**：输出 1 行 `MemIfDef.arxml`，size ≥ 4 KB（即 schema 文件被 Tycho 打进 jar）。

### A.2 RCP 启动 0 ERROR

```bash
cd $ROOT && ./tools/ide_smoke.sh -k 12 2>&1 | tail -3
```

**通过条件**：最后输出 `[PASS] workbench booted cleanly (silent .log)`。

### A.3 Sphinx 能识别 ARXML 文件类型

```bash
cd $ROOT && ./tools/test_memif_phase_a.sh --check sphinx-ext 2>&1 | tail -1
```

**通过条件**：输出 `[OK] sphinx recognizes .arxml extension`。

### A.4 demo workspace 导入后 tree 里有 MemIf 节点（headless 检测）

```bash
cd $ROOT && ./tools/test_memif_phase_a.sh --check tree-node 2>&1 | grep "MemIf"
```

**通过条件**：输出含 `[OK] tree shows MemIf node under Demo_S32K148/.../BSW_Builder/S32K148`。

### A.5 双击 MemIf 节点弹出的只读 form 显示 4 个值（headless 检测）

```bash
cd $ROOT && ./tools/test_memif_phase_a.sh --check form-readonly 2>&1 | grep -E "MemIfDevErrorDetect|MemIfNumberOfDevices|MemIfVersionInfoApi|MemIfModuleVersion"
```

**通过条件**：4 行输出，每行格式 `[OK] form shows <param> = <value>`，且：
- `MemIfDevErrorDetect = false`
- `MemIfNumberOfDevices = 2`
- `MemIfVersionInfoApi = false`
- `MemIfModuleVersion = TEST_PROBE_42_V25_10`

### A.6 视觉比对（手测）

操作：

1. 启动我们的 RCP（前台）：
   ```bash
   open ide/product/cn.com.myorg.bswbuilder.product/target/products/cn.com.myorg.bswbuilder.product/macosx/cocoa/aarch64/Eclipse.app
   ```
2. File → Open Workspace → 选 `samples/Demo_S32K148`
3. 树展开到 `BSW_Builder/S32K148/MemIf` → 双击
4. 截图保存到 `docs/reference/screenshots/phase-a-our-memif.png`
5. 启动 ORIENTAIS V25.10（在 win-automotive 上）：
   ```
   🪟 ./tools/winrun '& "D:\ORIENTAIS_Studio\...\bswbuilder.exe" -data D:\demo_workspace_copy'
   ```
6. 同样导入 demo，双击 MemIf，截图为 `docs/reference/screenshots/phase-a-orientais-memif.png`

**通过条件**：两张截图并排看，4 个参数 label / 值 / 默认值标记一致；UI 风格可不同
（我们 Sphinx auto-render；iSoft 自己 layout）。

### A.7 Phase A 通过门

A.1 + A.2 + A.3 + A.4 + A.5 + A.6 全过 → **Phase A PASS**。

---

## Phase B — 可编辑 + 保存

### B.1 EditingDomain 已注册

```bash
cd $ROOT && ./tools/test_memif_phase_b.sh --check editing-domain 2>&1 | tail -1
```

**通过条件**：`[OK] TransactionalEditingDomain registered for autosar40 nsURI`。

### B.2 改值 → 保存 → 重开持久化（自动）

```bash
cd $ROOT && ./tools/test_memif_phase_b.sh --check edit-save-reopen 2>&1
```

脚本内部跑：load → eGet 当前值 → eSet 新值 → save → reload → eGet 验证。

**通过条件**：最后一行 `[OK] value persisted across reload (changed 2 -> 1 -> reload -> 1)`。

### B.3 ARXML byte-equal（修改回原值后跟原文件比）

```bash
cd $ROOT && ./tools/test_memif_phase_b.sh --check noop-roundtrip 2>&1
```

脚本：load → 不改任何值 → save → diff 跟原文件 → 应该 0 差异（除时间戳行）。

**通过条件**：`[OK] noop save produces byte-equal output (filtered timestamps)`。

### B.4 ORIENTAIS 双向兼容（手测）

操作：

1. 我们 IDE：把 `MemIfNumberOfDevices` 从 2 改成 1，Ctrl+S
2. 把改过的 `samples/Demo_S32K148/BSW_Builder/S32K148/MemIf.arxml` 拷到 win-automotive
3. ORIENTAIS 打开同 workspace → 双击 MemIf → 看到 `NumberOfDevices = 1` ✓
4. 在 ORIENTAIS 改回 2，保存
5. 文件拉回 Mac，我们 IDE 重开 → 看到 `NumberOfDevices = 2` ✓

**通过条件**：步骤 3 + 5 的值跟期望一致；中间任何一步报错算 fail。

### B.5 Phase B 通过门

B.1 + B.2 + B.3 + B.4 全过 → **Phase B PASS**。

---

## Phase C — Auto-fill

### C.1 行为真值表已记录（参考）

```bash
cd $ROOT && wc -l docs/reference/memif-derived-truth-table.md
```

**通过条件**：≥ 4 数据行（覆盖 4 种组合：仅 Ea / 仅 Fee / 都有 / 都无）。

### C.2 EMF listener 注册

```bash
cd $ROOT && ./tools/test_memif_phase_c.sh --check listener-registered 2>&1 | tail -1
```

**通过条件**：`[OK] NvMTargetBlockReference listener registered`。

### C.3 4 种组合自动测试

```bash
cd $ROOT && ./tools/test_memif_phase_c.sh --check four-combos 2>&1
```

脚本依次构造 4 种 NvM 配置，读 MemIfNumberOfDevices 派生值，跟 C.1 的真值表对比。

**通过条件**：4 行 `[OK] combo_<n> derived = <expected>`，0 行 FAIL。

### C.4 跟 Python 后端 derivedNumberOfDevices 一致

```bash
cd $ROOT && PYTHONPATH=core:. python3 -m pytest core/tests/test_memif_derive.py -v 2>&1 | tail -3
```

**通过条件**：Java listener 输出和 Python `MemIf.derivedNumberOfDevices` 输出在同一份 demo 上完全相等（脚本内部对比）。

### C.5 Phase C 通过门

C.1 + C.2 + C.3 + C.4 全过 → **Phase C PASS**。

---

## Phase D — Validate / Generate 按钮真用

### D.1 Generate handler 调起 bswgen 子进程

```bash
cd $ROOT && ./tools/test_memif_phase_d.sh --check generate-subprocess 2>&1 | tail -3
```

脚本：headless 触发 GenerateMemIfHandler → 等子进程 → 检查输出文件。

**通过条件**：
```
[OK] bswgen subprocess returned rc=0
[OK] /tmp/phase_d_out/MemIf_Cfg.h exists, size > 8 KB
```

### D.2 Generate 输出与 reference byte-equal

```bash
cd $ROOT && diff <(sed -E '/@(date|toolVersion)/d' /tmp/phase_d_out/MemIf_Cfg.h) \
                <(sed -E '/@(date|toolVersion)/d' samples/Demo_S32K148/config/MemIf_Cfg.h)
echo "diff exit: $?"
```

**通过条件**：`diff exit: 0`。

### D.3 Validate handler 触发 bswval 子进程并桥接 Problems View

```bash
cd $ROOT && ./tools/test_memif_phase_d.sh --check validate-bad2170 2>&1 | tail -3
```

跑 BAD_2170 demo 的 validate handler。

**通过条件**：
```
[OK] bswval subprocess returned rc=1
[OK] Problems View has 1 IMarker with severity ERROR, message contains TCPP_2170
```

### D.4 Phase D 通过门

D.1 + D.2 + D.3 全过 → **Phase D PASS**。

---

## Phase E — Properties 面板

### E.1 选中参数 → IPropertySource 提供 Description / Definition / Status

```bash
cd $ROOT && ./tools/test_memif_phase_e.sh --check property-source 2>&1 | tail -5
```

**通过条件**：5 行 `[OK]`，分别对应：
- 选中后 IPropertySource 非 null
- Description tab 内容包含 `Concrete number of underlying memory abstraction modules`
- Definition tab 内容包含 `ECUC-INTEGER-PARAM-DEF` + `MIN=1` + `MAX=2`
- Status tab 内容包含当前值 + dirty 标志
- selection 切到另一参数时 IPropertySource 重新计算

### E.2 Phase E 通过门

E.1 全过 → **Phase E PASS**。

---

## Phase F — Round-trip 兼容性

### F.1 准备 5 份 ARXML

```bash
cd $ROOT && ls -1 docs/reference/roundtrip-fixtures/ 2>&1 | wc -l
```

**通过条件**：≥ 5。约定 5 份：
1. `01-demo.arxml` — 复制 demo
2. `02-bad-2170.arxml` — 复制 BAD_2170
3. `03-bad-2171.arxml` — 复制 BAD_2171
4. `04-min.arxml` — 仅 General 容器，无任何参数（最小有效 ECUC）
5. `05-max.arxml` — 4 参数全填 MAX 值 + 自定义 vendor 标签

### F.2 双向 round-trip 自动跑

```bash
cd $ROOT && ./tools/test_memif_roundtrip.sh 2>&1
```

脚本逻辑（每个 fixture 都跑）：

```
fixture → load via 我们 IDE → 不改 → save A → diff(A, fixture) == 0
fixture → load via 我们 IDE → 改 NumberOfDevices → save → load via ORIENTAIS → 改回去 → save → diff(ORIENTAIS_save, fixture) == 0
```

**通过条件**：脚本退出 0；屏幕输出最后一行 `[5/5] all roundtrip fixtures byte-equal`。

### F.3 Phase F 通过门

F.1 + F.2 全过 → **Phase F PASS**。

---

## §5 验收硬指标对应表

[MEMIF_REPLICA_PLAN.md §5](MEMIF_REPLICA_PLAN.md#5-验收硬指标-memif-复刻成功的定义)
列了 8 条复刻成功硬指标，跟本文档的 Phase 对应：

| §5 # | 内容 | Phase | 检查项 |
|---|---|---|---|
| 1 | RCP → 打开 demo → 看到 MemIf node + 表单 | A | A.4 + A.5 + A.6 |
| 2 | 改参数 → 保存 → 重启 → 值保留 | B | B.2 |
| 3 | ORIENTAIS 打开同文件 → 显示同样的值 | B | B.4 |
| 4 | ORIENTAIS 改完，我们 IDE 打开 → 显示同样的值 | B | B.4 |
| 5 | NvM mutate → MemIfNumberOfDevices 联动 | C | C.3 |
| 6 | 工具栏 Validate / Generate 与命令行一致 | D | D.2 + D.3 |
| 7 | Properties 面板有 Description / Definition / Status 三 tab | E | E.1 |
| 8 | `tools/test_memif_roundtrip.sh` 5/5 PASS | F | F.2 |

8 项全过 → **MemIf 复刻完成**。

---

## 工具脚本清单（每个 Phase 起步要写）

| 脚本 | 干什么 | Phase |
|---|---|---|
| `tools/test_memif_phase_a.sh` | A.3 / A.4 / A.5 自动检查 | A |
| `tools/test_memif_phase_b.sh` | B.1 / B.2 / B.3 自动检查 | B |
| `tools/test_memif_phase_c.sh` | C.2 / C.3 / C.4 自动检查 | C |
| `tools/test_memif_phase_d.sh` | D.1 / D.3 自动检查 | D |
| `tools/test_memif_phase_e.sh` | E.1 自动检查 | E |
| `tools/test_memif_roundtrip.sh` | F.2 五份 fixture 双向 byte-equal | F |

每个脚本第一次写出来就 commit，后续 Phase 不动。

## 关联

- [MEMIF_REPLICA_PLAN.md](MEMIF_REPLICA_PLAN.md) — 主计划文档
- [risks-memif.md](risks-memif.md) — 风险登记 + 周更
- [decisions/0006-memif-replica-source-strategy.md](decisions/0006-memif-replica-source-strategy.md) — 改走 spec-only 的原因

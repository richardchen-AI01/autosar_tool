# 经验教训 — NvM/MemIf 复刻 N=46~59 撞坑总结

> 状态: 用户明确 ask, working doc. 配套 memory 立的 8 条纪律, 给"开发方式"探讨备料。
> 日期: 2026-05-04

---

## 0. 一句话根因

**项目从 v0.1 起 host framework 底盘 (ARTOP/Sphinx 19 bundle) 没装进 product**, 我连续 7 次 (N=46~53) 在 UI/逻辑层 paraphrase 修业务 bug, 全部跑空 — 因为底盘没装, 业务代码不可能正确运行. **真根因 1 行 (feature.xml)**, 但被 7 次表层修包装掩盖.

---

## 1. 时间线 — 14 次 deploy 撞坑实录

| N | 提交 | 用户撞 | 我以为根因 | 真根因 |
|---|---|---|---|---|
| 46 | hook PoC S1+S2+S3 | "和原来一样" | UI 改少了 | feature.xml 缺 ARTOP |
| 47 | log trace 加 | 同上 | log 没出 → ProxyResolveHelper 没调 | 同上 |
| 48 | 4 列 layout (checkbox+D) | tree 死循环 + checkbox 加错 | 机械照搬 visible 元素 | 同上 + 没读 SDG flag 语义 |
| 49 | 撤回 4 列 + master tree log | 字段不渲染 | def= 空 (proxy) | 同上 + EcoreUtil.resolve 不认 ar:/ |
| 50 | 99% paraphrase ContentProvider | New 后全消失 | refreshInstancesAndSelect 用旧 setInput | 漏 fix 同名方法 |
| 51 | New 消失 fix + hint 配色 | 字段还不渲染, Del/Copy/Rename 全显 | proxy 还没 resolve | 同上 + ReserveUIDefinition 没接 |
| 52 | proxy resolve via EcoreUtil + Reserve 过滤 | 同上 | EcoreUtil 不行 | ARTOP services 没装 (feature.xml) |
| 53 | log trace 详细 | 同上 | 看 log 仍 def=空 | 同上 |
| 54 | **真根因 fix**: feature.xml 加 ARTOP/Sphinx 19 | (没启动验) | — | 部署坑: Expand-Archive silent 丢 12 jar |
| 55-58 | UI 对齐参考截图 + ProxyResolveHelper + ORIENTAIS Demo | sub-folder 全 (0), 多余 New X | sub-instance.gGetDefinition() 还是 proxy | sub-instance proxy 漏 fix |
| 59 | sub-instance proxy fix | (待验) | — | — |

**核心模式**: 每次撞坑我都修 N+1 层 (UI→hook→proxy→sub-instance proxy), 但**真根因 N=54 才发现** — 之前 7 次都是噪声.

---

## 2. 5 个深层失败模式 (memory 8 条纪律对应)

### 失败 1: 没爬 host framework 层 → memory `host_wiring_first.md`
- **现象**: feature.xml 含 `<plugin id="cn.com.myorg.*">` 业务 bundle, 但**没列 ARTOP/Sphinx 运行时 bundle**, Tycho package 时跳过 (`skippedP2Dependencies.txt`), product 启动 OSGi 没这些 → ar:/ proxy 永远 resolve 不了
- **memory 纪律**: build 后必查 `skippedP2Dependencies.txt`, 任何 SKIPPED 的 framework bundle 必须装进 product
- **判别**: product/plugins/ 跟参考 product/plugins/ 比对, 缺的 framework bundle 立即 fix

### 失败 2: 挑着读参考 + 简化照抄 → memory `paraphrase_whole_class.md` + `99_percent_replication.md`
- **现象**: 看 IUIDefinition 接口签名就写 hook PoC (没读完整 ContentProvider), 看截图 visible 元素位置就加 checkbox+D 列 (没读 SDG flag 触发条件), 写 ContentProvider 简化 isDisplay + SDG flag 5 个分支
- **memory 纪律**: 整文件 paraphrase, 字符级 99% 跟参考一致, 1% 微调仅限包名/必要 syntax 适配. 不允许 "PoC 阶段先简化"
- **判别**: 字符级 diff 反编 vs MEN, 反编 if/switch 数 == MEN if/switch 数, 任何 skip/TODO 注释都是违反

### 失败 3: 反编当 ground truth → memory `99_percent_replication.md` 第 9-18 行
- **现象**: 反编 cfr 0.152 输出可能含 dead code (例: `MemIfValidator.validateSupport` 反编出来定义私有方法但 `validate()` 没调), 我直接照搬就错
- **memory 纪律**: 反编是线索不是 ground truth. 终极基准是参考项目本身, 通过多源证据 (行为真值 + 反编 + Python + schema) 逼近. 撞证据冲突时站参考, 不站反编
- **判别**: Phase 1.5 真值 (跑参考工具链 byte-equal) 是终极通过门, 反编/Python 不一致时必回多源交叉

### 失败 4: build SUCCESS 当自验 → memory `unit_test_before_deploy.md`
- **现象**: 我 7 次都是 mvn install SUCCESS 后立即 deploy, 让用户当 QA. SSH session 跑不了 SWT 我没法 GUI 自验
- **memory 纪律**: deploy 前必有 SWT 无关 unit test pass. bug 先 reproduce test 再 fix. commit msg 必报 test 数. 但 unit test 是**必要不充分** — 测算法不测集成 / 不替代 byte-equal 真值
- **判别**: unit test 测层 1 (算法), 集成 test 测层 2 (OSGi wiring), byte-equal 测层 3 (终极真实)

### 失败 5: deploy 不可靠 → memory `dev_workflow_deploy.md` 第 4+5 条
- **现象**: PowerShell `Expand-Archive` 在 156MB+ zip 上 silent 丢文件 (N=54 实证, 19 个 ARTOP jar 丢成 7 个), 不报错不抛 exception, 看起来 "成功"
- **memory 纪律**: 大 zip 用 `jar.exe -xf`, 不用 `Expand-Archive`. deploy 后必须 `Get-ChildItem plugins -Filter "org.artop.*"`数 count, 不对立即重 extract
- **判别**: 任何 deploy 后必 verify ARTOP=10 / Sphinx=9 / Total≈292

---

## 3. 这次开发的"反模式"清单 (用户视角)

| 反模式 | 用户感知 | 修法 |
|---|---|---|
| **每次空话 "立即 fix"** | 7 次"立即"全是空, 信任崩 | 改完做完先自验, 给 evidence 才报完成 |
| **每次都让用户当 QA** | "我项目要废了, 人也要废了" | unit test 层 1 自动 + framework 装齐再 UI |
| **bug fix 没 reproduce test** | 同款 bug 反复撞 (proxy resolve 改了 3 次) | bug 先写 reproduce test, fix 后 test 转 pass 防回归 |
| **"挑着读参考"** | "UI 一直做不对" | 整文件 paraphrase, 字符级 99% 一致 |
| **底盘没装就做 UI** | 7 次撞坑根因都是它 | host framework 100% 装齐再 UI paraphrase |
| **deploy 不可靠没人查** | N=54 差点又撞 | jar.exe -xf + 数 plugin count |

---

## 4. memory 立的 8 条纪律 (这次撞坑沉淀)

1. `feedback_99_percent_replication.md` — 99% 复刻 1% 微调 (字符级量化硬线)
2. `feedback_paraphrase_whole_class.md` — 整文件 paraphrase, 不允许"PoC 简化"分支
3. `feedback_host_wiring_first.md` — host 框架底盘 100% 装齐再 paraphrase
4. `feedback_unit_test_before_deploy.md` — deploy 前必有 unit test pass
5. `feedback_self_verify_no_micro_pauses.md` — 改完自验给证据 + 里程碑判断主体在我
6. `dev_workflow_deploy.md` — 第 4+5 条: jar.exe -xf + verify plugin count
7. `feedback_replication_no_downgrade.md` (旧) — 复刻不降级
8. `feedback_align_reference_three_layers.md` (旧) — 对齐参考爬到数据流

每条都对应一次撞坑实证.

---

## 5. 没能解决但已识别的开发方式问题 (待用户探讨)

### A. SSH 无 GUI session → 我无法独立 GUI 验证
- **现状**: Windows 工作站 SWT 需 desktop session, SSH (sshd 普通用户) 跑不起 GUI app, 启动后 `Shell.open()` 抛 SWTException
- **当前 workaround**: 用户当 QA + 我读 .metadata/.log
- **可能改进**:
  - 装 Tycho UI test framework (eclipse-test-plugin + SWTBot), CI 跑 → 但 M1 aarch64 vs target x86_64 还要解 (N=53 撞过)
  - 重构 ContentProvider/Reserve permit 等业务逻辑成纯函数, 100% 单元测覆盖
  - 用户 RDP + 录屏观察 (人工成本未降)

### B. 反编 ≠ 参考 → byte-equal 真值才终极
- **现状**: 反编是 cfr 输出, 含 dead code / 失真. 我直接照搬就错
- **当前 partial fix**: Phase 1.5 真值已采集 (commit e6950d6), reference_diff.py byte-equal ALL PASS (commit 1f41f3a)
- **可能改进**:
  - 每个 commit 自动跑 reference_diff.py (CI 不行, 工作区 git hook?)
  - byte-equal diff > 0 自动阻止 push

### C. 长 deploy 周期 → 用户疲劳
- **现状**: 每 commit → mvn build → zip 156MB → scp → jar -xf → cp workspace → import → 启动. 全程 5-10 分钟
- **当前部分 fix**: jar.exe -xf 替代 Expand-Archive (N=54 后)
- **可能改进**:
  - 增量 deploy (只 cp 改的 jar, 不重整 product) — 但 OSGi cache 可能不刷
  - hot-deploy 绑 dev mode (Eclipse PDE)
  - 不用 product zip, 直接 RDP 跑 mvn install + Eclipse runtime

### D. 用户当 QA → 单点瓶颈
- **现状**: 我每次 deploy 都让用户启动 + 描述行为. 一个 bug 5+ 轮才修对
- **可能改进**:
  - 写完整 reproduce test for 已撞 bug (N=46~59 至少 5 个 reproduce test 应有)
  - 集成测试覆盖 OSGi wiring + framework 装齐
  - 把"用户报现象"翻成"自动化断言"

---

## 6. 当前进度 (commit 级)

| Phase | 状态 |
|---|---|
| Phase 0+1 反编 (NvM 73 + MemIf 12 .java) | ✅ |
| Phase 1.5 真值 (commit e6950d6) | ✅ |
| Phase 2 ANATOMY | ✅ |
| **Phase 2.5 hook PoC** (commit 6e47912 + 662b6b3) | ⏳ N=59 待用户验 |
| Phase 3+4 跨模块/框架基类反编 | ✅ (decompile 已做) |
| Phase 6a MemIf byte-equal (commit 1f41f3a "ALL PASS") | ✅ |
| Phase 6c NvM 49 functionextensions 全 port | ⏳ 当前 PoC 只 2 个 (NvMBlockUseCrcEnable + NvMBlockDescriptorEnable) |
| Phase 6d NvBlockDescriptor 多实例 + 跨模块 ref drop-down | ⏳ |
| Phase 6e NvM Validator | ⏳ |
| Phase 6f NvmSelectWizard | ⏳ |
| Phase 6g NvM Generator | ⏳ |

剩 6c~6g 主体工作量. 按"99% 复刻"机械 paraphrase, 不再有路线决策风险.

---

## 7. Phase 6c 实测工作量 (2026-05-04 当前 session 探索)

尝试系统化 port 49 functionextensions, 撞 chained dependency 链:

```
49 functionextensions  →  调用 EcuUtils.getEnumerationValue/getIntegerValue/getStringValue/...
                          调用 ModelUtils.getModelRootObject/getModuleConfiguration
                          调用 NvmUtils (NvM bundle utils, 533 行)
                          调用 NvMDef constants (common bundle)
                          ↓
mal.modelutils 包 (10 文件, ~3000 行):
  EcuUtilsBase 924 行 / EcuUtils ~280 行 / Model40Factory + Base ~400 行
  ModelUtils 489 行 / ModelUtilsBase 1431 行 / ParameterUtils / VariantDataBase / WorkspaceModelUtils
                          ↓
cfr 反编 Generic 信息丢失:
  raw EList 没 type parameter → for (GParameterValue p : list) 编译挂
  需手动加 <GParameterValue> generic
  每个文件 N 处 raw EList, 总 ~50+ 处需手动 fix
```

**估计工作量**: 整套 port + Generic 修复 + chained dep (autosar40 / sphinx.platform / 等 transitive bundle) ~30+ commit, 多 session.

**当前 session 决定**: 回退 mal.modelutils 批量 cp, 保留 N=59 build pass 状态. Phase 6c 留下 session 系统做 (避免 token cost 爆炸 + 中间状态 build 挂)。

**Phase 6c 待 session 计划**:
- Step 1: port `mal.modelutils.EcuUtilsBase` 整文件 + 手动修 Generic raw EList → typed EList. ~50 处, 1 session
- Step 2: port `mal.modelutils.ModelUtils*` (Base + sub) ~1900 行, 1 session
- Step 3: port `mal.modelutils.{Model40Factory*, ParameterUtils, VariantDataBase, WorkspaceModelUtils}` ~600 行, 1 session
- Step 4: port `bswbuilder.modules.nvm.utils.NvmUtils` 533 行, 0.5 session
- Step 5: port `bswbuilder.common.def.NvMDef` constants, 0.5 session
- Step 6: 重 cp 49 functionextensions + 改 NvMFunctionExtension 注册, 0.5 session
- Step 7: build + commit + deploy 验, 0.5 session

总 ~4-5 session 完成 Phase 6c 整体. 比一次性塞当前 session 健康得多.

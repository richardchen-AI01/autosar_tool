# ORIENTAIS V25.10 真值采集 — Demo S32K148

**采集时间**: 2026-05-04
**Configurator**: ORIENTAIS_Configurator_for_EasyXMen_V25.10 (Win 工作站 DESKTOP-DVNJ925)
**Demo 工程**: `D:\ORIENTAIS_Studio\...\workspace\Demo_S32K148_V2510_BSW_ConfigProject`
**操作**: 用户 GUI 点击 NvM + MemIf 模块 Generate Configuration

## 文件 (config/)

| 文件 | bytes | sha256 |
|---|---|---|
| `MemIf_Cfg.h` | 9233 | `94607f825e2da15bf4c212bb8e66c3a750edb6e44c85e2a93d1c1fecc4316231` |
| `NvM_Cfg.h` | 7011 | `51122d69e28240a47282f3e23a22bc581b6c676dab00ddd3a16eccf42b935594` |
| `NvM_Lcfg.c` | 48160 | `676f744bca2025173685366ff01fe217c5d3187a18c14a80da87414390f38516` |
| `NvM_Lcfg.h` | 7004 | `95239d8c86a3bb5ab91159c07e687bbe9b80a9c4c8ce9ad1991b6de7989afc9b` |

## 实测发现 — 反编 ≠ 实际生成

反编 jar 含 JET 模板 `NvM_Cfg_c.java` (366 行) / `MemIf_Cfg_c.java` / `Rte_NvM_Type_h.java`, 但 Configurator 实际**未生成** `NvM_Cfg.c` / `MemIf_Cfg.c` / `Rte_NvM_Type.h` — 跟 `*ElementAction` 0 引用同款, JET 模板反编出来但未激活. MEN 复刻**只对应 4 个真生成文件**, 不照搬 dead JET。

## 用法

```bash
# byte-equal 回归 (MEN 实装 generator 后):
python tools/reference_diff.py --modules NvM,MemIf
```

## 重采条件

- ORIENTAIS 工具链版本升级 → 整套重采 + 更新本文件 (按 `复刻不降级` 纪律)
- Demo 工程修改 → 同上
- 不允许局部 patch golden (per `参考锚点不可变`)

# Contributing to Autosar_tool

Thanks for picking this up. This guide gets you from a fresh clone to a
green test run, then walks you through the contribution flow.

> **Heads-up**: Read [`NOTICE.md`](NOTICE.md) first. v0.1 / v0.2 are
> research-only and contain V25.10-derived code; do not redistribute.

---

## 1. Prerequisites

| Tool | Version | Why |
|---|---|---|
| Python | 3.10 or 3.11 | Tier 2 + Tier 3 (generator / validator / Common) |
| Java | 8+ (only when working in `ide/`) | Eclipse RCP / Tycho |
| Maven | 3.8+ (only when working in `ide/`) | Tycho build |
| `git` | any recent | source control |
| `pyinstaller` | latest | only if you build single-file binaries |

Python deps:

```bash
pip install jinja2 lxml pytest pyinstaller
```

(Or `pip install -e core/ -e generator/ -e validator/` if you prefer
editable installs once we publish the pyprojects.)

## 2. Quick start

Clone, then run the regression:

```bash
git clone git@github.com:richardchen-AI01/Autosar_tool.git
cd Autosar_tool

# 30-second smoke check
PYTHONPATH=core:. python3 -m pytest core/tests generator/tests validator/tests -q

# 2-minute full-stack regression (M2.7)
./tools/test_memif_full.sh
```

If both finish green, your environment is good.

## 3. Project layout

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the three-tier
diagram. TL;DR:

- `core/Common/` — shared library (Jinja, Common base classes)
- `generator/` — `bswgen` CLI + per-module Python + Jinja templates
- `validator/` — `bswval` CLI + per-module Python rules + Messages JSON
- `schemas/` — ECUC schema ARXMLs (read-only, vendor-derived)
- `samples/` — golden / BAD demo workspaces
- `ide/` — Eclipse RCP product (skeleton, no Java yet)
- `tools/` — build & regression scripts
- `docs/` — plan, milestones, sprint logs

## 4. Running the test layers

| Layer | Command | What it covers |
|---|---|---|
| Unit | `PYTHONPATH=core:. pytest core/tests generator/tests validator/tests -q` | API surface, generation, rule firing |
| Integration | `./tools/test_memif_full.sh` | bswgen + bswval + diff vs V25.10 reference |
| Daily | `./tools/daily_check.sh` | Per-sprint-day PASS/FAIL/SKIP report |
| Binary | `./tools/build_all.sh && build/dist/bswgen -g MemIf -i samples/Demo_S32K148 -o /tmp/smoke` | PyInstaller bundle works |

**All four must pass before you mark a milestone done.** CI (see
`.github/workflows/test.yml`) re-runs the first three on Linux + macOS.

## 5. Branch & commit style

Conventions are in [`docs/GIT_CONVENTION.md`](docs/GIT_CONVENTION.md).
Summary:

- Branch: `<type>/<short-description>` — e.g. `feat/det-externals-default`
- Commit: `<type>(<scope>): <chinese imperative subject>` — e.g.
  `fix(generator): 为 Det_Externals 模板补默认 EcucPartition`

Allowed types: `feat`, `fix`, `refactor`, `perf`, `chore`, `docs`, `test`,
`style`.

## 6. Workflow for a typical change

```bash
# 1. Branch from main
git checkout -b fix/det-externals-default

# 2. Code, then run the tests that touch your area
PYTHONPATH=core:. pytest generator/tests -q

# 3. If you're touching MemIf or anything cross-module, run the full regression
./tools/test_memif_full.sh

# 4. Commit
git commit -m "fix(generator): 为 Det_Externals 模板补默认 EcucPartition"

# 5. Push and open PR
git push -u origin fix/det-externals-default
gh pr create --title "fix(generator): 为 Det_Externals 模板补默认 EcucPartition" \
    --body "Fixes the M3.1 stretch issue where Det generation aborts on missing global."
```

## 7. Adding a new BSW module

The MemIf vertical slice is the reference shape. To add module `Foo`:

1. Drop `FooDef.arxml` into `schemas/common/`.
2. Create `generator/modules/Foo/` with `base/`, `src/`, `templates/` — copy
   MemIf's structure as a starting point.
3. Create `validator/Bsw/Foo/{FooRules.py, FooRegister.py, FooMessages.json}`.
4. Add a golden workspace `samples/Demo_<chip>_<Foo>/` with the .arxml
   pair to compare against.
5. Add `generator/tests/test_foo_generation.py` (byte-equal vs golden).
6. Add `validator/tests/test_foo_validator.py` (clean + at least one BAD- case).
7. If the module participates in cross-module rules, extend the existing
   BAD- workspaces or add new ones.

## 8. Adding a validator rule

In `validator/Bsw/<Module>/<Module>Rules.py`:

```python
@RuleHandler("Rule_BSW_<Module>_TCPP_xxxx")
def Rule_BSW_<Module>_TCPP_xxxx(self):
    findings = []
    # walk self.def_elements / getBswContainerByEnum, append
    # (uri, args, [], container) tuples for each finding.
    return findings
```

Then add the rule's metadata to `<Module>Messages.json`:

```json
{
  "Rule_BSW_<Module>_TCPP_xxxx": {
    "level": "ERROR",
    "summary": "...",
    "description": "..."
  }
}
```

Cover it with a BAD- workspace + a test asserting it fires.

## 9. Code style

- **Python**: PEP 8 + type hints where they help. No formal black/ruff yet —
  match the surrounding file. `from __future__ import annotations` if the
  module uses postponed evaluation.
- **Templates**: stay close to the V25.10 source for byte-equality.
- **Docs**: prefer Markdown, keep tables narrow, ASCII diagrams over images.

## 10. Things to **not** do

- Don't add new V25.10-derived files outside `generator/modules/<M>/` and
  `validator/Bsw/<M>/` — those two areas are already covered by NOTICE.md.
- Don't `git add` anything under `reference/` or `dist/` — both are
  gitignored on purpose.
- Don't bypass `tools/test_memif_full.sh` failures with `--no-verify`. If
  the regression breaks, fix it or revert.
- Don't push to `main` directly. Open a PR.

## 11. Where to ask

- Architecture questions: `docs/ARCHITECTURE.md` first, then open an issue.
- Sprint context: `docs/sprint_logs/D*.md`.
- Reverse-engineering notes on V25.10: `docs/v25_pyz_source_reference/`
  (read-only, syntax-incomplete, but useful for "how did V25.10 do X").

Welcome aboard.

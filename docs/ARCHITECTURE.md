# Architecture · Autosar_tool v0.1

A condensed map of how this project is organised, what each part does, and why
we made the design choices we did. For the sprint timeline, see
[PLAN.md](PLAN.md). For end-user usage, see project root [README.md](../README.md).

---

## 1. Three-tier architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                  Tier 1 — IDE (Java / Eclipse RCP)               │
│                                                                  │
│  ide/product/      Eclipse RCP product configuration             │
│  ide/frameworks/   ARTOP 28 + Sphinx 13 + RCP runtime jars      │
│  ide/builder_core/ cn.com.myorg.bswbuilder.{common,ui,...}       │
│  ide/modules/      cn.com.myorg.bswbuilder.modules.<Module>      │
│                                                                  │
│  Role: form-based ECUC editor + project lifecycle + Generate     │
│        button / Validate button. Hosts no business logic — all   │
│        computation delegated to subprocess Tier 2 / 3.           │
│                                                                  │
│  Status (D2): skeleton dirs only. Java code TBD.                 │
└──────────────────────────────────────────────────────────────────┘
                              │ Runtime.exec
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│                  Tier 2 — Generator + Validator (Python apps)    │
│                                                                  │
│  generator/__main__.py          bswgen CLI                       │
│  generator/modules/<Module>/    per-BSW Python + Jinja2 template │
│                                                                  │
│  validator/__main__.py          bswval CLI                       │
│  validator/Bsw/<Module>/        per-BSW rule algorithms (Python) │
│  validator/Bsw/<Module>/<Module>Messages.json  rule metadata     │
│                                                                  │
│  Role: read workspace .arxml files, run module-specific Python   │
│        domain model, render Jinja2 templates → emit .c / .h /    │
│        .arxml files; or run validation rules and produce JSON    │
│        report.                                                   │
│                                                                  │
│  Distribution: PyInstaller single-file .exe (Windows) or         │
│                native binary (macOS/Linux).                      │
│                                                                  │
│  Status (D2): MemIf works end-to-end byte-identical to V25.10.   │
└──────────────────────────────────────────────────────────────────┘
                              │ imports
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│                  Tier 3 — Common library (Python)                │
│                                                                  │
│  core/Common/                                                    │
│  ├── BswBase.py            base class for module domain          │
│  ├── Public.py             helpers (getSwitchValue, etc.)        │
│  ├── CodeGenerator.py      Jinja2 main loop                      │
│  ├── Context.py            context wiring                        │
│  ├── J2Filters.py          Jinja2 custom filters                 │
│  ├── ArxmlValidator.py     validator framework                   │
│  ├── base/                                                       │
│  │   ├── BaseClass.py      BaseRule for validator               │
│  │   └── BaseDecorator.py  @RuleHandler decorator               │
│  └── arxmlparse/                                                 │
│      ├── loader.py         ECUC ARXML parser                    │
│      ├── constant/                                               │
│      │   └── BswPathConstant.py  6870 BP enum members           │
│      ├── cache/BswModuleCache.py  getBswContainerByEnum         │
│      └── artop/__init__.py def_elements / all_objects globals    │
│                                                                  │
│  Role: replaces V25.10's 13 closed-source `Common/*.pyd`         │
│        Cython modules with pure Python.                          │
└──────────────────────────────────────────────────────────────────┘
```

---

## 2. Why three tiers?

This split mirrors the original ORIENTAIS Configurator V25.10. Reasons it
remains the right structure:

| Tier | Why separate |
|---|---|
| 1 IDE | Eclipse RCP / OSGi only runs in JVM. ARTOP requires it. Java is the right tool for the GUI part of an AUTOSAR tool — there's no equally-supported alternative for the EMF metamodel. |
| 2 Apps | Python with Jinja2 templates is the right tool for code generation — readable templates, fast iteration, easy debugging. Distribute as exe so customers don't need Python. |
| 3 Lib | Shared between generator and validator. Lives in the same `Common.*` namespace as V25.10 to maximize compatibility with copied module sources. |

The IDE *and* the apps both ship to customers; the customer sees a single
"BSW Configurator". Behind the scenes it's three coordinated processes (JVM,
bswgen, bswval).

---

## 3. Data flow (Generate button)

```
User clicks Generate in IDE
   │
   │ Java IDE invokes Runtime.exec([
   │   "bswgen.exe",
   │   "-i", workspace_dir,
   │   "-o", config_dir,
   │   "-g", "MemIf"])
   ▼
bswgen.exe (PyInstaller bundle of Python 3.8 + our code)
   │
   ├─ argparse parses args
   │
   ├─ Common.arxmlparse.loader.load_project(workspace_dir)
   │     reads every .arxml in BSW_Builder/, parses
   │     ECUC-MODULE-CONFIGURATION-VALUES → ECUC-CONTAINER-VALUE →
   │     PARAMETER-VALUES (ECUC-NUMERICAL-PARAM-VALUE,
   │     ECUC-TEXTUAL-PARAM-VALUE, ECUC-REFERENCE-VALUE),
   │     populates global Common.arxmlparse.artop.def_elements
   │
   ├─ importlib.import_module('MemIf.base.MemIfRegister')
   │     registers Context + CodeGenerator
   │
   ├─ Context.postLoadArtopCache()
   │     instantiates MemIf domain class (calls
   │     getBswContainerByEnum(BP.MemIf_MemIfGeneral) → wraps in MemIfGeneral)
   │
   └─ CodeGenerator.generateCode()
         Jinja2 Environment with module's templates/ + Common's templates/
         renders FilesList.jinja → list of (output_file, template_file) pairs
         for each pair: render template → CRLF-encode → write to config_dir/
         emits "**** Total Count: critical: 0 error: 0 warning: 0 ****"
   ▼
config_dir/MemIf_Cfg.h, MemIf_Cfg.c, MemIf_Bswmd.arxml
```

**Key contract**: `bswgen` output for a given `(workspace, module)` must be
byte-identical to V25.10's `ORIENTAISBswGen.exe` output (after filtering
timestamps and tool-version markers). This is M2.1's hard gate.

---

## 4. Data flow (Validate button)

Symmetric to Generate, with `bswval.exe` and rule execution instead of
template rendering.

```
User clicks Validate
   │
   ▼
bswval.exe -i <workspace> -m <Module>
   ├─ load_project() — same as bswgen
   ├─ import Bsw.<Module>.<Module>Register  (V25.10 namespace)
   ├─ register_mod.getModuleArxmlValidator() → MemIfArxmlValidator()
   ├─    → super().createMessageData(<dir>) loads <Module>Messages.json
   ├─ runRules('') — execute every @RuleHandler-decorated rule on
   │     RuleBSW<Module>R23() instance
   ├─ each rule returns list of (uri, args, [], container) tuples
   │     for findings; framework formats and prints
   └─ exit code:
        0 if no ERROR/CRITICAL findings
        1 otherwise
```

Cross-module rules (e.g. `Rule_BSW_MemIf_TCPP_2170` checks NvM block
descriptors) work because all modules share the same `def_elements` global
populated at load time.

---

## 5. Compatibility with V25.10

We deliberately kept these points identical to V25.10 to maximize the value
of "search V25.10 for how X works":

- Python package names: `Common.*`, per-module top-level (not nested under a project root)
- `BswPath` enum values: full 6870 entries auto-generated from V25.10's
  BswPathConstant.pyc
- Jinja2 template syntax: `trim_blocks=True, lstrip_blocks=True`, CRLF output
- File output line endings: CRLF (matches V25.10 Windows-built output)
- Per-module file layout: `<Module>/{base,src,templates}/` for generator,
  `Bsw/<Module>/{<Module>Rules,<Module>Register,<Module>Messages}.{py,json}` for validator
- Global `def_elements` dict keyed by full ECUC path
- `@RuleHandler()` decorator pattern with `dict_message` lookup

We deliberately do **not** clone:

- `cn.com.isoft.mal.encrypt.FileEncryptyManager` — it's a license / hash
  protection layer; we don't need it (research-only v0.1).
- Cython compilation of `Common/*.pyd` — we use plain Python, ~10-100x easier
  to debug. The compiled-Cython optimization isn't needed at our scale.
- iSoft's Eclipse plugin namespace `cn.com.isoft.bswbuilder.*` — we use our
  own `cn.com.myorg.bswbuilder.*` to avoid conflict and clarify origin.

---

## 6. Test strategy

```
┌──────────────────────────────────────────────────────────────────┐
│ Layer 1: pytest (16 tests passing)                               │
│   core/tests/         API surface + import sanity                │
│   generator/tests/    end-to-end generation, byte-equal-to-ref   │
│   validator/tests/    cross-module rule correctness              │
├──────────────────────────────────────────────────────────────────┤
│ Layer 2: tools/test_memif_full.sh (M2.7 integration regression)  │
│   subprocess-level integration of bswgen + bswval + diff         │
├──────────────────────────────────────────────────────────────────┤
│ Layer 3: tools/daily_check.sh                                    │
│   per-sprint-day assertions; runs PASS/FAIL/SKIP report          │
├──────────────────────────────────────────────────────────────────┤
│ Layer 4: PyInstaller smoke test                                  │
│   build/dist/bswgen runs end-to-end; output byte-equal to source │
└──────────────────────────────────────────────────────────────────┘
```

To re-run everything:

```bash
./tools/test_memif_full.sh && \
./tools/daily_check.sh && \
PYTHONPATH=core:. python3 -m pytest core/tests generator/tests validator/tests -q && \
./tools/build_all.sh && \
build/dist/bswgen -g MemIf -i samples/Demo_S32K148 -o /tmp/smoke && \
echo "ALL PASS"
```

---

## 7. Cross-platform strategy

| Phase | Mac mini (dev hub) | Windows PC (test runner) |
|---|---|---|
| Code edit | ✓ all editing here | — |
| pytest | ✓ runs natively | ✓ same |
| Source-mode generator | ✓ `python -m generator` | ✓ same |
| PyInstaller build | ✓ produces Mac binary | ✓ produces .exe |
| IDE runtime test | partial (Eclipse RCP runs but iSoft .pyd not portable) | ✓ full |
| Final integration test | — | ✓ recommended |

Sync mechanism: pure git over SSH. Mac is the only place code is edited;
GitHub `main` is the source of truth. Windows pulls via
`./tools/winrun 'Set-Location D:\Autosar_tool; git pull; <build / test>'`,
runs the test path locally, and reports results back through stdout —
Windows never commits. For ad-hoc remote PowerShell use
`./tools/winrun '<script>'` (SSH alias `win-automotive` →
`AUTOMOTIVE@192.168.1.44`; base64 EncodedCommand transport so quoting
can't bite).

GitHub remote is the ultimate source of truth. Branch: `main` (private).

---

## 8. Known constraints / non-goals

- **License protection**: not implemented. v0.1 is a research demo only;
  v0.3 will need clean-room rewrite of license/hash before commercial release.
- **Incremental generation**: V25.10's IncGen / UserCodeDefinitions feature
  (preserve user-edited code blocks across regeneration) is stubbed out.
- **Schema validation**: ECUC schema (`schemas/common/*Def.arxml`) is loaded
  but not used for value-range checking. V25.10 does this at IDE form level.
- **80-module coverage**: only 4 modules ported (MemIf full, Det/NvM/Ea
  partial). Full coverage is M3 / v0.2 work.
- **Eclipse RCP**: no Java code yet. ide/ has a placeholder structure.
  Building the IDE side is M3.3 / M4 work.

---

## 9. Going forward

Sprint plan: [PLAN.md](PLAN.md) §5 has the 14-day timeline.

Per-day checkable milestones: [MILESTONES.md](MILESTONES.md).

Post-v0.1 work: [PLAN.md §9](PLAN.md#9-v01-之后的路线).

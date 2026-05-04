# Eclipse RCP IDE — `ide/`

Java / Tycho / OSGi half of autosar_tool: a minimal Eclipse RCP shell that
hosts the BSW configuration GUI and shells out to Python `bswgen` / `bswval`
for the actual code generation and validation.

## Status (D2 EOD → walking skeleton landed)

| Layer | Status |
|---|---|
| Tycho parent + target platform | ✅ `ide/pom.xml`, `ide/target-platform/bswbuilder-target/bswbuilder-target.target` |
| `mvn -B clean verify` | ✅ all 7 reactor modules SUCCESS, 4 launcher zips produced |
| Per-platform RCP launcher materialized | ✅ macOS arm64/x86_64, Win x86_64, Linux x86_64 → `target/products/.../Eclipse.app/` (mac), `bswbuilder.exe` (win) |
| RCP application + perspective | ✅ `cn.com.myorg.bswbuilder.common` |
| UI: navigator + Generate/Validate handlers | ✅ `cn.com.myorg.bswbuilder.ui` |
| MemIf module placeholder | ✅ `cn.com.myorg.bswbuilder.modules.memif` |
| Feature + Product | ✅ `cn.com.myorg.bswbuilder.feature` + `cn.com.myorg.bswbuilder.product` |
| Eclipse 4 IEventBroker DI on first boot | ✅ fixed — `Require-Bundle` on e4 services + `equinox.event`; `tools/ide_smoke.sh` PASS |
| ARTOP / Sphinx integration | 🚧 deferred to M3.3+ (need licensed jars) |
| ECUC form editor | 🚧 deferred (M3.3+) |
| Validate → ProblemView | 🚧 deferred (M3.3+) |

### Smoke test

Once `mvn -B clean verify` finishes:

```bash
./tools/ide_smoke.sh                 # default: 8s alive then SIGKILL
./tools/ide_smoke.sh -k 15           # give it longer if your machine is slow
```

Pass criterion: zero `!ENTRY <bundle> 4` (level 4 = ERROR) lines in
`<workspace>/.metadata/.log`. Cleanest possible PASS is "no `.log` written
at all" — Eclipse only creates that file when something is logged.

The walking skeleton **proves the IDE ↔ Python bridge** —
`BswgenLauncher.run(Tool, …)` is the single contact point between the JVM
and our Python tooling, so the architecture stays cleanly two-tier even
once the IDE grows.

## Directory layout

```
ide/
├── pom.xml                                    Tycho parent
├── target-platform/
│   └── bswbuilder-target/                     Eclipse 2024-09 target platform
├── builder_core/
│   ├── cn.com.myorg.bswbuilder.common/        RCP app + perspective
│   └── cn.com.myorg.bswbuilder.ui/            handlers, views, launcher
├── modules/
│   └── cn.com.myorg.bswbuilder.modules.memif/ MemIf module (placeholder)
├── feature/
│   └── cn.com.myorg.bswbuilder.feature/       wraps all plugins
└── product/
    └── cn.com.myorg.bswbuilder.product/       launchable RCP product
```

## How to build (Tycho)

```bash
cd ide
mvn -B clean verify
```

First run downloads ~150 MB from `download.eclipse.org`. Subsequent builds
are seconds.

Outputs land in:
```
ide/product/cn.com.myorg.bswbuilder.product/target/products/cn.com.myorg.bswbuilder.product/
├── macosx/cocoa/aarch64/Eclipse.app/         (on Mac)
├── win32/win32/x86_64/...                    (on Windows)
└── linux/gtk/x86_64/...                      (on Linux)
```

Plus per-platform .zip archives in
`target/products/cn.com.myorg.bswbuilder.product-<os>.<ws>.<arch>.zip`.

## How to launch the built RCP

```bash
# Mac
open ide/product/cn.com.myorg.bswbuilder.product/target/products/cn.com.myorg.bswbuilder.product/macosx/cocoa/aarch64/Eclipse.app
```

The window title should read **"BSW Configurator (autosar_tool)"**, with:

- **BSW** menu (Generate MemIf / Validate MemIf)
- Toolbar buttons for the same
- Left-side **BSW Modules** view
- Bottom **Console** view (output of bswgen/bswval streams here)

Clicking **Generate MemIf** prompts for a workspace dir and an output dir,
then runs the equivalent of:

```
PYTHONPATH=core python3 -m generator -g MemIf -i <workspace> -o <output>
```

…unless `build/dist/bswgen[.exe]` exists, in which case the binary is used.

## How to develop interactively (Eclipse PDE)

1. Install the **Eclipse IDE for RCP and RAP Developers** package
   (any 2024-x release works).
2. File → Import… → Existing Maven Projects → point at `ide/` →
   Eclipse imports all six Tycho modules.
3. Window → Preferences → Plug-in Development → Target Platform →
   Add → File system → pick
   `ide/target-platform/bswbuilder-target/bswbuilder-target.target` → Set as Active.
4. Open `ide/product/cn.com.myorg.bswbuilder.product/cn.com.myorg.bswbuilder.product` →
   click **Launch an Eclipse application** in the Overview tab.
5. The launched RCP runs against your local sources — edit, save, relaunch.

## How the IDE finds the Python repo at runtime

`BswgenLauncher.locateRepoRoot()` walks up from the JVM `user.dir` until it
finds both `generator/__main__.py` AND `core/Common/`. So launching from the
repo root works automatically. If you're launching from elsewhere, pass
`-Dautosar.repoRoot=/path/to/autosar_tool` to the JVM.

## Bundle / package naming

| Bundle SymbolicName | Role |
|---|---|
| `cn.com.myorg.bswbuilder.common`         | RCP shell — Application, Perspective, ActionBarAdvisor |
| `cn.com.myorg.bswbuilder.ui`             | Module navigator view + Generate/Validate command handlers + bswgen launcher |
| `cn.com.myorg.bswbuilder.modules.memif`  | MemIf module plugin (placeholder until ARTOP integration) |
| `cn.com.myorg.bswbuilder.feature`        | feature wrapping the three plugins above |
| `cn.com.myorg.bswbuilder.product`        | product config (RCP launcher build) |

The `myorg` is a placeholder — pick your real organization domain before
external sharing.

## What's intentionally missing (vs V25.10)

| V25.10 component | Why we don't have it (yet) |
|---|---|
| `cn.com.isoft.mal.encrypt.FileEncryptyManager` | License/hash protection — not needed for research demo |
| ARTOP 4.5.2 jars in `frameworks/` | Licensed; need ARTOP-member entitlement to redistribute |
| Sphinx 0.11.2 jars | Same as ARTOP — pulled from Eclipse p2 only when integrated |
| Forms-based ECUC parameter editor | Needs ARTOP integration first |
| Project Explorer with .arxml model | Needs Sphinx workspace lifecycle |
| ProblemView integration | Needs Sphinx + a problem-marker producer |

Tracking: see [PLAN.md](../docs/PLAN.md) M3.3 ("Validator → IDE Validate
button") and [PLAN.md §9.2](../docs/PLAN.md#92-v02-之-ui-重设计eb-tresos-风) for
the form editor.

## Reference: V25.10 plugin layout (for cloning)

`reference/autosar-cfg/plugins/`:

| jar | role | clone status |
|---|---|---|
| `cn.com.isoft.bswbuilder.modules.memif_*.jar` | per-module schema + UI registry | TODO when ARTOP lands |
| `cn.com.isoft.bswbuilder.ui_*.jar` | NewBswBuilderEditor + actions | partially done — basic actions in our `.ui` |
| `cn.com.isoft.bswbuilder.common_*.jar` | shared base classes | partially done — RCP shell in our `.common` |
| `cn.com.isoft.bswbuilder.validation_*.jar` | validator framework | not yet (will hook into bswval JSON) |
| `cn.com.isoft.mal_*.jar` | FileEncryptyManager (license / hash) | skip; v0.1 doesn't need it |
| `org.artop.aal.*` (28 jar) | AUTOSAR EMF metamodel | will copy as-is to `frameworks/` once ARTOP lands |
| `org.eclipse.sphinx.*` (13 jar) | EMF workspace lifecycle | same |
| `org.eclipse.*` RCP base | Eclipse RCP runtime | already pulled via `bswbuilder-target.target` |

## Architectural decisions (recap)

1. **Native helpers (V25.10 `.pyd`) NOT needed in IDE.** Java side only
   contains schema + UI + extension points + validator integration. All actual
   computation lives in `bswgen.exe` / `bswval.exe`.
2. **OSGi compat.** Walking skeleton uses Eclipse 2024-09 because Tycho 4.x
   builds it cleanly. ARTOP 4.5.2 + Sphinx 0.11.2 will likely require an
   older target — we'll branch the target if needed.
3. **No license / file-integrity protection** for v0.1. V25.10's
   `FileEncryptyManager.verifyFileHash` is intentionally **not cloned** — see
   [`NOTICE.md`](../NOTICE.md).
4. **Plugin namespace `cn.com.myorg.*`** — placeholder. Choose your real
   organization domain before any external sharing.

## Suggested next steps

| Step | Effort | Output |
|---|---|---|
| ⬜ Wire up project picker + recent-projects MRU | 0.5 day | better workspace UX |
| ⬜ Stream JSON validator findings into ProblemView | 1 day | M3.3 |
| ⬜ Add Det / NvM module plugins (mirror MemIf) | 0.5 day | parity with generator side |
| ⬜ Add ARTOP target file branch | 1 day | unlocks form editor |
| ⬜ Form-based ECUC parameter editor | 3-5 days | M4 / v0.2 |

Total to functional v0.1 IDE: ~1 week for one engineer; less in parallel.

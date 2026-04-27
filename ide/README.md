# Eclipse RCP IDE — `ide/`

The Eclipse RCP product that hosts the BSW configuration GUI. This is the
**Java/OSGi** half of the tool, complementing the Python `generator/` and
`validator/` exes.

## Directory layout

```
ide/
├── product/                    Eclipse Product configuration
│   └── (TODO: cn.com.myorg.bswbuilder.product.product)
├── frameworks/                 Third-party plugin jars (committed binary)
│   └── (TODO: ARTOP 28 + Sphinx 13 + Eclipse RCP runtime)
├── builder_core/               Our Java code framework plugins
│   ├── cn.com.myorg.bswbuilder.common/
│   ├── cn.com.myorg.bswbuilder.ui/
│   ├── cn.com.myorg.bswbuilder.extensionpoints/
│   └── cn.com.myorg.bswbuilder.validation/
└── modules/                    Per-BSW-module plugin jars
    ├── cn.com.myorg.bswbuilder.modules.memif/
    ├── cn.com.myorg.bswbuilder.modules.det/
    └── ...
```

## Status (D2 EOD)

🚧 **Skeleton only.** No Java code written yet. The functional pipeline
(generator + validator + Common) all works **without** Eclipse RCP — see
project root `README.md` quickstart. The IDE is for the GUI experience and
forms part of M3.3 (校验器接入 IDE Validate 按钮) and M4 (v0.1 demo).

## How to build (when implemented)

```bash
# Maven Tycho build (Java 8 + Maven 3.8+)
cd ide
mvn -B clean verify

# Output:
#   product/target/products/cn.com.myorg.bswbuilder.product/macosx/cocoa/aarch64/...
#   product/target/products/cn.com.myorg.bswbuilder.product/win32/win32/x86_64/...
```

## Reference: V25.10 plugin layout (for cloning)

`reference/autosar-cfg/plugins/`:

| jar | role | clone status |
|---|---|---|
| `cn.com.isoft.bswbuilder.modules.memif_*.jar` | per-module schema + UI registry | TODO: clone-and-rename to `cn.com.myorg.*` |
| `cn.com.isoft.bswbuilder.ui_*.jar` | NewBswBuilderEditor + actions | TODO |
| `cn.com.isoft.bswbuilder.common_*.jar` | shared base classes | TODO |
| `cn.com.isoft.bswbuilder.validation_*.jar` | validator framework | TODO |
| `cn.com.isoft.mal_*.jar` | FileEncryptyManager (license / hash) | TODO: skip; we don't need V25.10's hash protection |
| `org.artop.aal.*` (28 jar) | AUTOSAR EMF metamodel | copy as-is to frameworks/ |
| `org.eclipse.sphinx.*` (13 jar) | EMF workspace lifecycle | copy as-is |
| `org.eclipse.*` (RCP runtime, ~200 jar) | Eclipse RCP base | copy as-is via p2 |

## Per-plugin minimum file set (for one BSW module)

For each `<Module>` (e.g. MemIf):

```
ide/modules/cn.com.myorg.bswbuilder.modules.<Module>/
├── META-INF/
│   └── MANIFEST.MF              OSGi bundle manifest
├── plugin.xml                   Eclipse plugin descriptor — registers:
│                                  editor / validator / generator / metaModelDescriptor
├── pom.xml                      Tycho build descriptor
├── <Module>Def.arxml            ECUC schema (copied from schemas/common/)
├── <Module>_Bswmd.arxml         BSWMD module description stub
└── src/cn/com/myorg/bswbuilder/modules/<module>/
    ├── Activator.java           OSGi bundle activator
    ├── <Module>DefaultRegistry.java     Form / table layout
    ├── <Module>MetaModelDescriptor.java Sphinx metamodel descriptor
    ├── <Module>UpdateBswmd.java         Project upgrader (auto-add new params)
    ├── functionextensions/
    │   ├── <Module>FunctionExtension.java
    │   └── ...
    ├── generator/
    │   └── <Module>Generator.java       (in V25.10) calls bswgen.exe; can shell out via Runtime.exec
    └── validator/
        └── <Module>Validator.java       calls bswval.exe similarly
```

## Architectural decisions

1. **Native helpers (V25.10 .pyd) are NOT needed in IDE.** Java side only
   contains schema + UI + extension points + validator integration. All actual
   computation lives in `bswgen.exe` / `bswval.exe` (Python).

2. **OSGi version compatibility.** ARTOP 4.5.2 + Sphinx 0.11.2 (from V25.10).
   Don't upgrade for v0.1.

3. **No license / file-integrity protection** for v0.1. V25.10's
   `FileEncryptyManager.verifyFileHash` is intentionally **not cloned** — its
   sole purpose was anti-tampering, which we don't need for our demo. (Skipping
   it also avoids the entire docs §15 §2.4 reverse-engineering rabbit hole.)

4. **Plugin namespace `cn.com.myorg.*`** — placeholder. Choose your real
   organization domain before any external sharing.

## Suggested implementation order

| Step | Effort | Output |
|---|---|---|
| 1. Tycho parent pom + product-feature.xml | 1 day | `mvn verify` builds empty .zip |
| 2. Copy ARTOP / Sphinx / RCP jars to frameworks/ | 0.5 day | bundles list complete |
| 3. cn.com.myorg.bswbuilder.common plugin (shared base classes) | 1 day | Other plugins can require-bundle |
| 4. cn.com.myorg.bswbuilder.modules.memif (1 module template) | 1 day | IDE shows MemIf node |
| 5. Connect Generate button to bswgen.exe via Runtime.exec | 0.5 day | M1.6 |
| 6. Form-page: parameter editing | 1 day | M1.5 |
| 7. Validate button → ProblemView | 0.5 day | M3.3 |
| 8. Replicate to NvM/Det/Ea/Fee | 1-2 days | M3.1 prep |

Total: ~6-8 days for one engineer; less for parallel Claude Code instances.

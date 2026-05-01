package cn.com.myorg.bswbuilder.ui.schema;

import java.util.Collections;
import java.util.List;

/**
 * Top-level ECUC module definition — read from {@code <Module>Def.arxml}.
 *
 * <p>Reference V25.10 path: {@code GModuleConfiguration.gGetDefinition() →
 * GModuleDef.gGetContainers()} on EMF/ARTOP. We read the same data via plain
 * DOM XML parse (no ARTOP/Sphinx dep) — equivalent ModuleSchema produces the
 * same UI behavior.
 */
public final class ModuleSchema {

    public final String moduleName;       // SHORT-NAME of the ECUC-MODULE-DEF
    public final String description;
    public final List<ContainerSchema> containers;

    public ModuleSchema(String moduleName, String description,
                        List<ContainerSchema> containers) {
        this.moduleName = moduleName;
        this.description = description;
        this.containers = containers == null
                ? Collections.<ContainerSchema>emptyList()
                : Collections.unmodifiableList(containers);
    }
}

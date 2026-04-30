package cn.com.myorg.mal.modelutils;

import java.util.HashMap;

import org.eclipse.jface.resource.ImageRegistry;

/**
 * Reference: {@code cn.com.isoft.mal.modelutils.DefaultRegistry} — module-level
 * default registry contract used as the {@code editor=} value of the
 * {@code module} extension point. Despite the schema attribute name
 * {@code editor}, this is NOT an EditorPart — it's a 2-method hook for
 * registering per-module display defaults (icon names + name aliases).
 *
 * <p>The actual form editor is opened via Eclipse standard file association
 * (.arxml → registered editor) when the user double-clicks a ModuleModel
 * leaf in the navigator.
 *
 * <p><b>Note</b>: method name {@code intiDefaultImages} (sic) is a typo
 * preserved from the reference {@code cn.com.isoft.mal.modelutils.DefaultRegistry}
 * (CFR-confirmed). All 74 reference module bundles spell it the same way;
 * fixing here would break drop-in port of those modules.
 */
public interface DefaultRegistry {

    /** Populate human-readable name aliases for tree labels / property views. */
    void initDefaultName(HashMap<String, String> registry);

    /** Register module-specific images with the workbench ImageRegistry. */
    void intiDefaultImages(ImageRegistry reg);
}

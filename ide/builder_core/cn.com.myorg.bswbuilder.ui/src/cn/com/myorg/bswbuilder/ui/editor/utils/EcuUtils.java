package cn.com.myorg.bswbuilder.ui.editor.utils;

import java.util.ArrayList;
import java.util.List;

import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;
import gautosar.gecucdescription.GParameterValue;
import gautosar.gecucparameterdef.GConfigParameter;
import gautosar.gecucparameterdef.GContainerDef;

/**
 * Minimal subset of reference V25.10 {@code cn.com.isoft.mal.modelutils.EcuUtils}
 * — bridges schema (GContainerDef / GConfigParameter) and instance
 * (GContainer / GParameterValue) sides via EMF cross-reference identity.
 *
 * <p>v0.2 helpers cover what {@link cn.com.myorg.bswbuilder.ui.editor.pages
 * .GenericGeneralFormPage} needs. E5-3 will extend with multi-instance
 * variants for master-detail.
 */
public final class EcuUtils {

    private EcuUtils() {}

    /**
     * Return all instance containers of {@code module} whose definition cross-ref
     * resolves to {@code def}. Equivalent to reference
     * {@code EcuUtils.getContainerFromModuleByDef}.
     *
     * <p>EMF identity comparison is the right move here: if Def.arxml + instance
     * .arxml share a ResourceSet (Sphinx EditingDomain), every instance's
     * gGetDefinition() returns the canonical EObject from Def.arxml, so {@code ==}
     * works (no need for path-string equality).
     */
    public static List<GContainer> getContainersByDef(GModuleConfiguration module, GContainerDef def) {
        List<GContainer> out = new ArrayList<>();
        if (module == null || def == null) return out;
        for (GContainer c : module.gGetContainers()) {
            if (c.gGetDefinition() == def) out.add(c);
        }
        return out;
    }

    /**
     * First container instance for a single-instance ('General') definition,
     * or null if missing. Logs a warning if multiple instances exist for a
     * 1..1 def — schema violation.
     */
    public static GContainer getSingleContainerByDef(GModuleConfiguration module, GContainerDef def) {
        List<GContainer> all = getContainersByDef(module, def);
        if (all.isEmpty()) return null;
        if (all.size() > 1) {
            System.err.println("[EcuUtils] " + def.gGetShortName()
                    + " expected 1 instance, got " + all.size() + " — using first.");
        }
        return all.get(0);
    }

    /**
     * Find the {@link GParameterValue} on {@code container} whose definition
     * resolves to {@code paramDef}. Returns null if absent (parameter not yet
     * configured — caller should fall back to schema's default value).
     */
    public static GParameterValue getParameterValue(GContainer container, GConfigParameter paramDef) {
        if (container == null || paramDef == null) return null;
        for (GParameterValue pv : container.gGetParameterValues()) {
            if (pv.gGetDefinition() == paramDef) return pv;
        }
        return null;
    }
}

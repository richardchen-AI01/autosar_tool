package cn.com.myorg.bswbuilder.ui.editor.utils;

import java.util.ArrayList;
import java.util.List;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.InternalEObject;

import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;
import gautosar.gecucdescription.GParameterValue;
import gautosar.gecucparameterdef.GConfigParameter;
import gautosar.gecucparameterdef.GContainerDef;
import gautosar.ggenericstructure.ginfrastructure.GIdentifiable;

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
        String defShortName = ((GIdentifiable) def).gGetShortName();
        for (GContainer c : module.gGetContainers()) {
            if (matchesDefinition(c.gGetDefinition(), def, defShortName)) {
                out.add(c);
            }
        }
        return out;
    }

    /**
     * Match instance's def-cross-ref against the schema GContainerDef.
     *
     * <p>EMF cross-ref via {@code ==} works only when the instance's
     * gGetDefinition() proxy was already resolved. ARTOP encodes proxy URIs
     * with AR-path fragments which our {@link cn.com.myorg.bswbuilder.ui.schema.BswSchemaLoader}
     * doesn't bridge (no LibraryManager AR-path → file-URI registry). Fall
     * back to comparing the def's short-name via proxy URI fragment.
     *
     * <p>AR-path fragment example: {@code "//AUTOSAR/MemIf/MemIfGeneral"}
     * → leaf segment {@code "MemIfGeneral"} == def's short-name.
     */
    private static boolean matchesDefinition(GContainerDef instanceDef, GContainerDef schemaDef,
                                             String schemaDefShortName) {
        // Strategy 1: EMF cross-ref already resolved, identity matches.
        if (instanceDef == schemaDef) return true;
        if (instanceDef == null) return false;

        // Strategy 2: instance is unresolved proxy — compare proxy URI fragment
        // leaf segment to schema def's short name.
        if (((EObject) instanceDef).eIsProxy() && instanceDef instanceof InternalEObject) {
            URI proxyUri = ((InternalEObject) instanceDef).eProxyURI();
            if (proxyUri != null) {
                String fragment = proxyUri.fragment();
                if (fragment != null) {
                    int slash = fragment.lastIndexOf('/');
                    String leaf = slash < 0 ? fragment : fragment.substring(slash + 1);
                    if (schemaDefShortName.equals(leaf)) return true;
                }
            }
        }

        // Strategy 3: even non-proxy non-identity case (e.g. cross-ref resolved
        // but to a sibling EObject in a different ResourceSet) — match by
        // typed shortName.
        try {
            String name = ((GIdentifiable) instanceDef).gGetShortName();
            return schemaDefShortName.equals(name);
        } catch (Throwable ignored) {
            return false;
        }
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
        String paramDefShortName = ((GIdentifiable) paramDef).gGetShortName();
        for (GParameterValue pv : container.gGetParameterValues()) {
            GConfigParameter pvDef = pv.gGetDefinition();
            if (pvDef == paramDef) return pv;
            if (pvDef == null) continue;
            // Same proxy URI fragment fallback as matchesDefinition.
            if (((EObject) pvDef).eIsProxy() && pvDef instanceof InternalEObject) {
                URI proxyUri = ((InternalEObject) pvDef).eProxyURI();
                if (proxyUri != null) {
                    String fragment = proxyUri.fragment();
                    if (fragment != null) {
                        int slash = fragment.lastIndexOf('/');
                        String leaf = slash < 0 ? fragment : fragment.substring(slash + 1);
                        if (paramDefShortName.equals(leaf)) return pv;
                    }
                }
            }
            try {
                String name = ((GIdentifiable) pvDef).gGetShortName();
                if (paramDefShortName.equals(name)) return pv;
            } catch (Throwable ignored) { /* fall through */ }
        }
        return null;
    }
}

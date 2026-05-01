package cn.com.myorg.bswbuilder.ui.schema;

import java.io.IOException;
import java.net.URL;

import org.eclipse.core.runtime.FileLocator;
import org.eclipse.core.runtime.Platform;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.osgi.framework.Bundle;

import gautosar.gecucdescription.GModuleConfiguration;
import gautosar.gecucparameterdef.GModuleDef;

/**
 * Resolves the {@link GModuleDef} (BSWMD schema definition) for a loaded
 * {@link GModuleConfiguration} instance — mirrors reference V25.10's
 * {@code module.gGetDefinition()} usage path in
 * {@code cn.com.isoft.bswbuilder.ui.editor.NewBswBuilderEditor.addPages()}.
 *
 * <p>Reference relies on its {@code librarymanager} bundle to register Def
 * resources at logical AR paths (e.g. {@code /AUTOSAR/MemIf}). We emulate the
 * minimal subset needed: when {@code module.gGetDefinition()} returns an
 * unresolved EMF proxy, look up {@code <Module>Def.arxml} from the matching
 * module bundle's classloader resources, load it into the same ResourceSet as
 * the instance, and try again. EMF cross-ref resolution then walks the loaded
 * Def to find the target EObject by AR path.
 *
 * <p>Behavior matches reference: callers walk {@code def.gGetContainers()},
 * {@code containerDef.gGetParameters()}, {@code containerDef.gGetReferences()}
 * with strongly-typed ARTOP {@code gautosar.gecucparameterdef.*} APIs — no
 * intermediate POJO layer.
 */
public final class BswSchemaLoader {

    private BswSchemaLoader() {}

    /**
     * Get the {@link GModuleDef} for an instance module configuration.
     *
     * <p>Resolution order:
     * <ol>
     *   <li>{@code module.gGetDefinition()} — if EMF already resolved the
     *       cross-ref (Def.arxml in same ResourceSet), return it directly.</li>
     *   <li>Otherwise, find {@code <Module>Def.arxml} from the matching module
     *       bundle, load it into the instance's ResourceSet, then re-call
     *       {@code gGetDefinition()}.</li>
     * </ol>
     *
     * @return resolved GModuleDef, or null if no Def.arxml is found.
     */
    public static GModuleDef resolveDef(GModuleConfiguration module) {
        if (module == null) {
            System.err.println("[BswSchemaLoader] module == null");
            return null;
        }
        String moduleName = module.gGetShortName();
        System.err.println("[BswSchemaLoader] resolveDef(" + moduleName + ") starting");

        GModuleDef def = module.gGetDefinition();
        if (def != null && !((EObject) def).eIsProxy()) {
            System.err.println("[BswSchemaLoader] " + moduleName
                    + ": gGetDefinition() already resolved (cross-ref auto-resolve worked)");
            return def;
        }
        if (def == null) {
            System.err.println("[BswSchemaLoader] " + moduleName
                    + ": gGetDefinition() returned null — instance .arxml may have no DEFINITION-REF");
            return null;
        }
        System.err.println("[BswSchemaLoader] " + moduleName
                + ": gGetDefinition() returned proxy, attempting to load Def.arxml from bundle");

        Resource instanceRes = ((EObject) module).eResource();
        if (instanceRes == null) {
            System.err.println("[BswSchemaLoader] " + moduleName
                    + ": instance EObject not attached to a Resource — cannot get ResourceSet");
            return null;
        }
        ResourceSet rs = instanceRes.getResourceSet();
        if (rs == null) {
            System.err.println("[BswSchemaLoader] " + moduleName
                    + ": Resource not attached to a ResourceSet");
            return null;
        }

        URI defUri = locateDefArxml(moduleName);
        if (defUri == null) {
            System.err.println("[BswSchemaLoader] " + moduleName
                    + ": locateDefArxml returned null — bundle 'cn.com.myorg.bswbuilder.modules."
                    + moduleName.toLowerCase()
                    + "' or its " + moduleName + "Def.arxml not found");
            return null;
        }
        System.err.println("[BswSchemaLoader] " + moduleName + ": loading Def from " + defUri);
        try {
            rs.getResource(defUri, true);
        } catch (Exception e) {
            System.err.println("[BswSchemaLoader] " + moduleName + ": rs.getResource(" + defUri
                    + ") threw " + e.getClass().getSimpleName() + ": " + e.getMessage());
            e.printStackTrace();
            return null;
        }

        if (def instanceof InternalEObject) {
            EObject resolved = org.eclipse.emf.ecore.util.EcoreUtil.resolve(def, rs);
            if (resolved != null && !resolved.eIsProxy() && resolved instanceof GModuleDef) {
                System.err.println("[BswSchemaLoader] " + moduleName
                        + ": EcoreUtil.resolve worked, schema OK");
                return (GModuleDef) resolved;
            }
        }
        def = module.gGetDefinition();
        boolean ok = def != null && !((EObject) def).eIsProxy();
        System.err.println("[BswSchemaLoader] " + moduleName
                + ": after Def load, gGetDefinition() resolved=" + ok);
        return ok ? def : null;
    }

    /**
     * Find {@code <Module>Def.arxml} in any module bundle whose symbolic name
     * follows the convention {@code cn.com.myorg.bswbuilder.modules.<lowerCase(module)>}.
     *
     * <p>Each module bundle bundles its own Def.arxml at the bundle root (see
     * {@code build.properties} {@code bin.includes} entry). We use Eclipse's
     * {@link FileLocator} to convert the bundle-internal URL into a local file
     * URI usable by EMF.
     */
    private static URI locateDefArxml(String moduleName) {
        if (moduleName == null || moduleName.isEmpty()) return null;
        String bundleId = "cn.com.myorg.bswbuilder.modules." + moduleName.toLowerCase();
        Bundle bundle = Platform.getBundle(bundleId);
        if (bundle == null) return null;

        URL entry = bundle.getEntry(moduleName + "Def.arxml");
        if (entry == null) return null;
        try {
            URL fileUrl = FileLocator.toFileURL(entry);
            return URI.createURI(fileUrl.toString());
        } catch (IOException io) {
            System.err.println("[BswSchemaLoader] FileLocator failed for "
                    + moduleName + "Def.arxml in " + bundleId + ": " + io);
            return null;
        }
    }
}

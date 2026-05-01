package cn.com.myorg.bswbuilder.ui.schema;

import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

import org.eclipse.core.runtime.FileLocator;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Platform;
import org.eclipse.core.runtime.Status;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.osgi.framework.Bundle;

import cn.com.myorg.bswbuilder.ui.Activator;

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

    /** Per-thread diagnostic lines accumulated during a {@link #resolveDef} call.
     *  Editor can read via {@link #drainDiagnostics()} after a null result and
     *  surface to the user via {@link cn.com.myorg.bswbuilder.ui.editors.EditorOpenFailurePage}. */
    private static final ThreadLocal<List<String>> DIAGNOSTICS =
            ThreadLocal.withInitial(ArrayList::new);

    private BswSchemaLoader() {}

    /** Log to .metadata/.log (Eclipse ILog) AND collect for caller diagnostics. */
    private static void log(String msg) {
        DIAGNOSTICS.get().add(msg);
        try {
            if (Activator.getDefault() != null) {
                Activator.getDefault().getLog().log(
                        new Status(IStatus.INFO, Activator.PLUGIN_ID, msg));
            }
        } catch (Throwable ignored) {
            // Activator might not be initialized yet — fall back silently
        }
    }

    /** Pull and clear the diagnostics from the current thread.
     *  Caller (typically GenericModuleEditor.addPages) shows them to user. */
    public static List<String> drainDiagnostics() {
        List<String> copy = new ArrayList<>(DIAGNOSTICS.get());
        DIAGNOSTICS.get().clear();
        return copy;
    }

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
            log("[BswSchemaLoader] module == null");
            return null;
        }
        String moduleName = module.gGetShortName();
        log("[BswSchemaLoader] resolveDef(" + moduleName + ") starting");

        GModuleDef def = module.gGetDefinition();
        if (def != null && !((EObject) def).eIsProxy()) {
            log("[BswSchemaLoader] " + moduleName
                    + ": gGetDefinition() already resolved (cross-ref auto-resolve worked)");
            return def;
        }
        if (def == null) {
            log("[BswSchemaLoader] " + moduleName
                    + ": gGetDefinition() returned null — instance .arxml may have no DEFINITION-REF");
            return null;
        }
        log("[BswSchemaLoader] " + moduleName
                + ": gGetDefinition() returned proxy, attempting to load Def.arxml from bundle");
        if (def instanceof InternalEObject) {
            URI proxyUri = ((InternalEObject) def).eProxyURI();
            log("[BswSchemaLoader] " + moduleName
                    + ": proxy URI = " + proxyUri);
        }

        Resource instanceRes = ((EObject) module).eResource();
        if (instanceRes == null) {
            log("[BswSchemaLoader] " + moduleName
                    + ": instance EObject not attached to a Resource — cannot get ResourceSet");
            return null;
        }
        ResourceSet rs = instanceRes.getResourceSet();
        if (rs == null) {
            log("[BswSchemaLoader] " + moduleName
                    + ": Resource not attached to a ResourceSet");
            return null;
        }

        URI defUri = locateDefArxml(moduleName);
        if (defUri == null) {
            log("[BswSchemaLoader] " + moduleName
                    + ": locateDefArxml returned null — bundle 'cn.com.myorg.bswbuilder.modules."
                    + moduleName.toLowerCase()
                    + "' or its " + moduleName + "Def.arxml not found");
            return null;
        }
        log("[BswSchemaLoader] " + moduleName + ": loading Def from " + defUri);
        Resource defRes;
        try {
            defRes = rs.getResource(defUri, true);
        } catch (Exception e) {
            log("[BswSchemaLoader] " + moduleName + ": rs.getResource(" + defUri
                    + ") threw " + e.getClass().getSimpleName() + ": " + e.getMessage());
            return null;
        }

        // Strategy 1: 尝试直接 EcoreUtil.resolve(def proxy, rs) — 标准 EMF 路径
        if (def instanceof InternalEObject) {
            EObject resolved = org.eclipse.emf.ecore.util.EcoreUtil.resolve(def, rs);
            if (resolved != null && !resolved.eIsProxy() && resolved instanceof GModuleDef) {
                log("[BswSchemaLoader] " + moduleName
                        + ": EcoreUtil.resolve worked (strategy 1)");
                return (GModuleDef) resolved;
            }
        }

        // Strategy 2: proxy URI 跟 Def.arxml URI 对不上 (常见 — ARTOP 用 AR 路径
        // proxy URI, 不是文件 URI)。直接在 loaded Def 里按 AR-PACKAGE 路径找
        // ECUC-MODULE-DEF SHORT-NAME == moduleName 的 EObject。
        if (defRes != null) {
            for (EObject root : defRes.getContents()) {
                EObject found = findModuleDefByName(root, moduleName);
                if (found instanceof GModuleDef) {
                    log("[BswSchemaLoader] " + moduleName
                            + ": found GModuleDef in Def.arxml by name (strategy 2)");
                    return (GModuleDef) found;
                }
            }
        }
        def = module.gGetDefinition();
        boolean ok = def != null && !((EObject) def).eIsProxy();
        log("[BswSchemaLoader] " + moduleName
                + ": after Def load, gGetDefinition() resolved=" + ok);
        return ok ? def : null;
    }

    /**
     * Strategy 2 helper: walk an EObject tree (typically loaded Def.arxml root)
     * looking for an ECUC-MODULE-DEF whose SHORT-NAME matches {@code moduleName}.
     * Used when EMF cross-ref resolution couldn't bridge proxy URI ↔ loaded
     * Resource (because ARTOP encodes proxies with AR paths, not file URIs).
     */
    private static EObject findModuleDefByName(EObject root, String moduleName) {
        if (root == null) return null;
        if (matchesModuleDef(root, moduleName)) return root;
        org.eclipse.emf.common.util.TreeIterator<EObject> it = root.eAllContents();
        while (it.hasNext()) {
            EObject obj = it.next();
            if (matchesModuleDef(obj, moduleName)) return obj;
        }
        return null;
    }

    private static boolean matchesModuleDef(EObject obj, String moduleName) {
        if (!(obj instanceof GModuleDef)) return false;
        // GModuleDef extends GIdentifiable which has gGetShortName()
        try {
            String sn = ((gautosar.ggenericstructure.ginfrastructure.GIdentifiable) obj)
                    .gGetShortName();
            return moduleName.equals(sn);
        } catch (Throwable t) {
            return false;
        }
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
            log("[BswSchemaLoader] FileLocator failed for "
                    + moduleName + "Def.arxml in " + bundleId + ": " + io);
            return null;
        }
    }
}

package cn.com.myorg.bswbuilder.ui.editor.utils;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.util.EcoreUtil;

import cn.com.myorg.bswbuilder.ui.Activator;
import gautosar.ggenericstructure.ginfrastructure.GIdentifiable;

/**
 * Resolves ARTOP cross-resource ECUC def proxies.
 *
 * <p>ARTOP encodes proxies with the {@code ar:/} URI scheme and a
 * {@code ?type=<EClass>} query suffix, e.g.
 * {@code ar:/#/AUTOSAR/NvM/NvMBlockDescriptor?type=EcucParamConfContainerDef}.
 * Standard {@link EcoreUtil#resolve} only resolves these when the ResourceSet
 * is Sphinx's {@code ExtendedResourceSetImpl} AND a per-metamodel
 * {@code IProxyResolverService} is registered AND the workspace project has
 * the matching nature. Without all three, {@code resolve} silently returns
 * the still-proxy.
 *
 * <p>This helper short-circuits that chain by walking every {@link Resource}
 * already in the context's {@link ResourceSet} (which includes the Def.arxml
 * loaded by {@link cn.com.myorg.bswbuilder.ui.schema.BswSchemaLoader}) and
 * looking for an {@link GIdentifiable} whose {@code eClass().getName()} matches
 * the proxy URI's {@code ?type=} value AND whose {@code shortName} matches the
 * URI fragment's leaf. Returns the first match or the original proxy.
 */
public final class ProxyResolveHelper {

    private ProxyResolveHelper() {}

    /**
     * Resolve a possibly-proxy EObject reference. {@code context} must be
     * attached to a {@link Resource} in the right {@link ResourceSet}; if it
     * isn't, the proxy is returned unchanged.
     */
    public static EObject resolve(EObject maybeProxy, EObject context) {
        if (maybeProxy == null || !maybeProxy.eIsProxy()) return maybeProxy;
        if (!(maybeProxy instanceof InternalEObject)) return maybeProxy;

        URI proxyUri = ((InternalEObject) maybeProxy).eProxyURI();
        if (proxyUri == null) return maybeProxy;

        // Try standard EMF resolve first — works when Sphinx + ARTOP are fully wired.
        try {
            EObject standard = EcoreUtil.resolve(maybeProxy, context);
            if (standard != null && !standard.eIsProxy()) {
                log("standard resolve worked for " + proxyUri);
                return standard;
            }
        } catch (Throwable ignored) {
            // fall through to manual scan
        }

        ResourceSet rs = (context != null && context.eResource() != null)
                ? context.eResource().getResourceSet() : null;
        if (rs == null) {
            log("no ResourceSet from context for " + proxyUri);
            return maybeProxy;
        }

        String typeName = parseTypeQuery(proxyUri);
        String fragment = proxyUri.fragment();
        String leafName = leafSegment(fragment);
        if (typeName == null || leafName == null) {
            log("could not parse type/leaf from " + proxyUri
                    + " (type=" + typeName + " leaf=" + leafName + ")");
            return maybeProxy;
        }

        for (Resource r : rs.getResources()) {
            EObject hit = scanResource(r, typeName, leafName, fragment);
            if (hit != null) {
                log("manual scan resolved " + proxyUri + " → "
                        + hit.eClass().getName() + "[" + safeShortName(hit)
                        + "] in " + r.getURI());
                return hit;
            }
        }

        log("manual scan FAILED for " + proxyUri + " — type=" + typeName
                + " leaf=" + leafName + " resources=" + rs.getResources().size());
        return maybeProxy;
    }

    /**
     * Walk one Resource's contents looking for a {@link GIdentifiable} whose
     * EClass name matches {@code typeName} and whose shortName matches
     * {@code leafName}. AR-path fragment match (full path) is preferred when
     * the EObject's full AR path is reconstructable, but a shortName +
     * EClass type tuple is unique enough for ECUC defs in our scope.
     */
    private static EObject scanResource(Resource r, String typeName, String leafName,
                                        String fullFragment) {
        if (r == null) return null;
        for (EObject root : r.getContents()) {
            EObject hit = scanTree(root, typeName, leafName, fullFragment);
            if (hit != null) return hit;
        }
        return null;
    }

    private static EObject scanTree(EObject root, String typeName, String leafName,
                                    String fullFragment) {
        if (root == null) return null;
        if (matches(root, typeName, leafName)) return root;
        java.util.Iterator<EObject> it = root.eAllContents();
        while (it.hasNext()) {
            EObject obj = it.next();
            if (matches(obj, typeName, leafName)) return obj;
        }
        return null;
    }

    private static boolean matches(EObject obj, String typeName, String leafName) {
        if (!(obj instanceof GIdentifiable)) return false;
        EClass cls = obj.eClass();
        if (cls == null) return false;
        String clsName = cls.getName();
        if (!typeName.equals(clsName)) return false;
        String sn;
        try {
            sn = ((GIdentifiable) obj).gGetShortName();
        } catch (Throwable t) {
            return false;
        }
        return leafName.equals(sn);
    }

    private static String safeShortName(EObject obj) {
        if (!(obj instanceof GIdentifiable)) return "?";
        try {
            return ((GIdentifiable) obj).gGetShortName();
        } catch (Throwable t) {
            return "?";
        }
    }

    /** Extract value of {@code ?type=...} from a proxy URI fragment. */
    static String parseTypeQuery(URI proxyUri) {
        if (proxyUri == null) return null;
        String f = proxyUri.fragment();
        if (f == null) return null;
        int q = f.indexOf("?type=");
        if (q < 0) return null;
        String t = f.substring(q + "?type=".length());
        int amp = t.indexOf('&');
        return amp >= 0 ? t.substring(0, amp) : t;
    }

    /** Last AR-path segment, ignoring {@code ?type=} suffix. */
    static String leafSegment(String fragment) {
        if (fragment == null) return null;
        int q = fragment.indexOf('?');
        String pure = q >= 0 ? fragment.substring(0, q) : fragment;
        int slash = pure.lastIndexOf('/');
        String leaf = slash < 0 ? pure : pure.substring(slash + 1);
        return leaf.isEmpty() ? null : leaf;
    }

    private static void log(String msg) {
        try {
            Activator a = Activator.getDefault();
            if (a != null) {
                a.getLog().log(new Status(IStatus.INFO, Activator.PLUGIN_ID,
                        "[ProxyResolve] " + msg));
            }
        } catch (Throwable ignored) { /* fallback silent */ }
    }
}

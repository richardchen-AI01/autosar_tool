package cn.com.myorg.bswbuilder.modules.memif.data;

import org.eclipse.emf.common.util.TreeIterator;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.emf.ecore.xmi.impl.XMIResourceFactoryImpl;

/**
 * Loads an ARXML file via the EMF / Artop stack and extracts the four
 * MemIfGeneral parameters into a {@link MemIfData} POJO.
 *
 * <p>This is the loading half of Phase 1's
 * {@code LoadMemIfArxmlHandler}, factored out so multiple call sites
 * (toolbar handler, view click, headless test) share the same code path.
 *
 * <p>EPackage registration uses reflection so the class name is decoupled
 * from a hard import — Artop ships the AUTOSAR R4.0 root EPackage as
 * {@code autosar40.util.Autosar40Package}, but the package class name has
 * not been stable across all 4.x revisions.
 */
public final class MemIfArxmlReader {

    /** Tried in order; first one that loads wins. */
    private static final String[] CANDIDATE_AUTOSAR_PACKAGES = new String[] {
            "autosar40.util.Autosar40Package",
            "autosar40.Autosar40Package",
            "autosar448.util.Autosar448Package",
            "autosar448.Autosar448Package",
    };

    private MemIfArxmlReader() {
        // utility class
    }

    /**
     * @param path absolute filesystem path to the ARXML file
     * @return populated {@link MemIfData}; fields not present in the file
     *         come back as {@code null}
     * @throws RuntimeException if the file cannot be loaded as a Resource
     */
    public static MemIfData read(String path) {
        ResourceSet rs = new ResourceSetImpl();
        rs.getResourceFactoryRegistry()
          .getExtensionToFactoryMap()
          .put("arxml", new XMIResourceFactoryImpl());
        registerAutosarPackages(rs);

        Resource resource = rs.getResource(URI.createFileURI(path), true);

        return new MemIfData(
                path,
                findParam(resource, "MemIfDevErrorDetect"),
                findParam(resource, "MemIfNumberOfDevices"),
                findParam(resource, "MemIfVersionInfoApi"),
                findParam(resource, "MemIfModuleVersion"));
    }

    private static void registerAutosarPackages(ResourceSet rs) {
        for (String fqn : CANDIDATE_AUTOSAR_PACKAGES) {
            try {
                Class<?> cls = Class.forName(fqn);
                Object instance = cls.getField("eINSTANCE").get(null);
                if (instance instanceof EPackage) {
                    EPackage p = (EPackage) instance;
                    rs.getPackageRegistry().put(p.getNsURI(), p);
                    return;
                }
            } catch (Throwable ignored) {
                // try next candidate
            }
        }
    }

    /**
     * Walks every EObject in the resource looking for an
     * {@code EcucNumericalParamValue} or {@code EcucTextualParamValue}
     * whose {@code definition}-ref's path ends with {@code paramShortName}.
     */
    private static String findParam(Resource resource, String paramShortName) {
        TreeIterator<EObject> iter = resource.getAllContents();
        while (iter.hasNext()) {
            EObject obj = iter.next();
            String typeName = obj.eClass().getName().toLowerCase();
            // We want either numerical or textual ECUC param-value subtypes
            if (!typeName.contains("paramvalue")) {
                continue;
            }
            String defRef = stringValueOf(obj, "definition");
            if (defRef == null) {
                defRef = stringValueOf(obj, "definitionRef");
            }
            if (defRef == null || !defRef.endsWith(paramShortName)) {
                continue;
            }
            return stringValueOf(obj, "value");
        }
        return null;
    }

    private static String stringValueOf(EObject obj, String featureName) {
        EStructuralFeature feature = obj.eClass().getEStructuralFeature(featureName);
        if (feature == null) {
            return null;
        }
        Object raw = obj.eGet(feature);
        return raw != null ? raw.toString() : null;
    }
}

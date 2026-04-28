package cn.com.myorg.bswbuilder.modules.memif.handlers;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.emf.common.util.TreeIterator;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.emf.ecore.xmi.impl.XMIResourceFactoryImpl;
import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.FileDialog;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.ui.handlers.HandlerUtil;

/**
 * Phase 1 deliverable: load an ARXML through Artop / Sphinx / EMF and surface
 * one parameter value to the user.
 *
 * <p>Flow:
 * <ol>
 *   <li>Show file dialog filtered to *.arxml</li>
 *   <li>Build a ResourceSet, register the AUTOSAR EPackages by reflection so
 *       EMF understands the {@code http://autosar.org/schema/r4.0} namespace</li>
 *   <li>Load the file as a Resource</li>
 *   <li>Walk for an {@code EcucNumericalParamValue} whose definition path ends
 *       with {@code MemIfNumberOfDevices} and read its value</li>
 *   <li>Pop up a MessageDialog with what was found</li>
 * </ol>
 *
 * <p>Reflection on the AUTOSAR EPackage class is used (rather than a hard
 * import) because Artop ships the metamodel in two parallel bundles —
 * {@code org.artop.aal.autosar40} (R4.0) and {@code org.artop.aal.autosar448}
 * (R4.4.8). The class names are not stable across versions; loading whichever
 * is on the classpath at runtime is the most robust path.
 */
public class LoadMemIfArxmlHandler extends AbstractHandler {

    /** Artop EPackage class names tried in order. First one that loads wins.
     *  Verified by inspecting org.artop.aal.autosar448 plugin.xml — the root
     *  AUTOSAR namespace `http://autosar.org/schema/r4.0` maps to
     *  `autosar40.util.Autosar40Package` in Artop 4.13.x. */
    private static final String[] CANDIDATE_AUTOSAR_PACKAGES = new String[] {
            "autosar40.util.Autosar40Package",
            "autosar40.Autosar40Package",
            "autosar448.util.Autosar448Package",
            "autosar448.Autosar448Package",
    };

    @Override
    public Object execute(ExecutionEvent event) throws ExecutionException {
        Shell shell = HandlerUtil.getActiveShell(event);

        FileDialog dialog = new FileDialog(shell, SWT.OPEN);
        dialog.setFilterExtensions(new String[] { "*.arxml" });
        dialog.setText("Select an ARXML file (e.g. samples/Demo_S32K148/.../MemIf.arxml)");
        String path = dialog.open();
        if (path == null) {
            return null;
        }

        try {
            ResourceSet rs = new ResourceSetImpl();
            rs.getResourceFactoryRegistry()
              .getExtensionToFactoryMap()
              .put("arxml", new XMIResourceFactoryImpl());

            String registered = registerAutosarPackages(rs);

            URI uri = URI.createFileURI(path);
            Resource resource = rs.getResource(uri, true);

            int topLevel = resource.getContents().size();
            String value = findMemIfNumberOfDevices(resource);

            String body = "ARXML       : " + path + "\n"
                        + "EPackage    : " + registered + "\n"
                        + "Top-level   : " + topLevel + " EObject(s)\n"
                        + "MemIfNumberOfDevices = "
                        + (value != null ? value : "<not found in this file>");
            System.out.println("[LoadMemIfArxml]\n" + body);
            MessageDialog.openInformation(shell, "Phase 1 — Artop load OK", body);
        } catch (Throwable t) {
            t.printStackTrace();
            MessageDialog.openError(shell, "ARXML load failed",
                    t.getClass().getSimpleName() + ": " + t.getMessage());
        }
        return null;
    }

    private String registerAutosarPackages(ResourceSet rs) {
        for (String fqn : CANDIDATE_AUTOSAR_PACKAGES) {
            try {
                Class<?> cls = Class.forName(fqn);
                Object instance = cls.getField("eINSTANCE").get(null);
                if (instance instanceof EPackage) {
                    EPackage p = (EPackage) instance;
                    rs.getPackageRegistry().put(p.getNsURI(), p);
                    return fqn + " (nsURI=" + p.getNsURI() + ")";
                }
            } catch (Throwable ignored) {
                // Try next candidate
            }
        }
        return "<none registered — relying on namespace auto-discovery>";
    }

    private String findMemIfNumberOfDevices(Resource resource) {
        TreeIterator<EObject> iter = resource.getAllContents();
        while (iter.hasNext()) {
            EObject obj = iter.next();
            String typeName = obj.eClass().getName();
            if (!typeName.toLowerCase().contains("numerical")) {
                continue;
            }
            String defRef = stringValueOf(obj, "definition");
            if (defRef == null) {
                defRef = stringValueOf(obj, "definitionRef");
            }
            if (defRef == null || !defRef.endsWith("MemIfNumberOfDevices")) {
                continue;
            }
            String value = stringValueOf(obj, "value");
            if (value != null) {
                return value;
            }
        }
        return null;
    }

    private String stringValueOf(EObject obj, String featureName) {
        EStructuralFeature feature = obj.eClass().getEStructuralFeature(featureName);
        if (feature == null) {
            return null;
        }
        Object raw = obj.eGet(feature);
        return raw != null ? raw.toString() : null;
    }
}

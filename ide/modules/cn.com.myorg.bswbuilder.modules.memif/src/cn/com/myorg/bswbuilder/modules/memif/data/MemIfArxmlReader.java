package cn.com.myorg.bswbuilder.modules.memif.data;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IWorkspaceRoot;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.Path;
import org.eclipse.emf.common.util.TreeIterator;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;

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

    /** EPackage classes tried in order; first one that loads wins. */
    private static final String[] CANDIDATE_AUTOSAR_PACKAGES = new String[] {
            "autosar40.util.Autosar40Package",
            "autosar40.Autosar40Package",
            "autosar448.util.Autosar448Package",
            "autosar448.Autosar448Package",
    };

    /** Resource.Factory.Impl classes tried in order; first one that loads wins.
     *  These are AUTOSAR-aware factories that map ARXML element names like
     *  {@code <AR-PACKAGES>} to EMF features like {@code arPackages} (the
     *  generic XMIResourceFactoryImpl does NOT do this and trips on
     *  "Feature 'AR-PACKAGES' not found"). */
    private static final String[] CANDIDATE_ARXML_FACTORIES = new String[] {
            "autosar40.util.Autosar40ResourceFactoryImpl",
            "org.artop.aal.common.resource.impl.AutosarResourceFactoryImpl",
    };

    private MemIfArxmlReader() {
        // utility class
    }

    /**
     * Workspace-aware overload — preferred path. Routes through Sphinx
     * {@link MemIfModelAccess#loadModelRoot}, getting a properly initialized
     * EditingDomain (no manual ResourceSet creation, no manual factory /
     * package registration).
     *
     * <p>v0.2 E2: this is the new path; older {@link #read(String)} is kept
     * as a transitional fallback for callers still passing absolute paths.
     */
    public static MemIfData read(IFile iFile) {
        if (iFile == null) {
            return null;
        }
        String absPath = iFile.getLocation() != null
                ? iFile.getLocation().toOSString() : null;
        EObject modelRoot = null;
        try {
            modelRoot = MemIfModelAccess.loadModelRoot(iFile);
        } catch (Throwable t) {
            // Sphinx 路径异常 → 不要冒泡，让 fallback 处理。打印诊断
            // 信息让运行时仍能看到原因 (Win .metadata/.log)。
            System.err.println("[MemIfArxmlReader] Sphinx loadModelRoot threw "
                    + t.getClass().getSimpleName() + ": " + t.getMessage()
                    + " — falling back to legacy reader for " + absPath);
        }
        if (modelRoot == null) {
            // Sphinx didn't claim this resource (project nature missing,
            // metamodel not matched, or load failed) → fall back to the
            // legacy file-system path **directly**. Do NOT recurse to
            // read(String path), because that would call back to read(IFile)
            // for any path inside the workspace and stack-overflow.
            return absPath != null ? readLegacy(absPath) : null;
        }
        // E2.5: 用 ARTOP typed API 读 — instanceof EcucModuleConfigurationValues
        // / EcucContainerValue / EcucNumericalParamValue / EcucTextualParamValue,
        // typed getValue() / getMixedText() / gGetShortName(), 不再走 untyped
        // eClass.name.toLowerCase() walker (违反参考不变量 #1)。
        return extractTyped(modelRoot, absPath);
    }

    /**
     * Typed traversal of the loaded EMF model — uses ARTOP's strongly-typed
     * Java classes per AUTOSAR ECUC schema. Mirrors the canonical pattern
     * documented in {@code writeups/architecture/03-artop-analysis.md §4.3}.
     */
    private static MemIfData extractTyped(EObject modelRoot, String absPath) {
        java.util.Map<String, String> values = new java.util.HashMap<>();

        org.eclipse.emf.common.util.TreeIterator<EObject> iter = modelRoot.eAllContents();
        while (iter.hasNext()) {
            EObject obj = iter.next();
            if (obj instanceof autosar40.ecucdescription.EcucModuleConfigurationValues) {
                autosar40.ecucdescription.EcucModuleConfigurationValues mod =
                        (autosar40.ecucdescription.EcucModuleConfigurationValues) obj;
                for (autosar40.ecucdescription.EcucContainerValue c : mod.getContainers()) {
                    walkContainer(c, values);
                }
            }
        }

        return new MemIfData(absPath,
                values.get("MemIfDevErrorDetect"),
                values.get("MemIfNumberOfDevices"),
                values.get("MemIfVersionInfoApi"),
                values.get("MemIfModuleVersion"));
    }

    private static void walkContainer(
            autosar40.ecucdescription.EcucContainerValue c,
            java.util.Map<String, String> values) {
        for (autosar40.ecucdescription.EcucParameterValue p : c.getParameterValues()) {
            String shortName = paramShortNameOf(p);
            if (shortName == null) continue;
            String stringValue = extractTypedValue(p);
            if (stringValue != null) values.put(shortName, stringValue);
        }
        // recurse into sub-containers (typed)
        for (autosar40.ecucdescription.EcucContainerValue sub : c.getSubContainers()) {
            walkContainer(sub, values);
        }
    }

    /**
     * Get the parameter's definition short-name via typed cross-reference.
     * Fallback to proxy-URI fragment parsing only if EMF resolve fails
     * (e.g. ARXML loaded outside Sphinx EditingDomain → "ar:" protocol).
     */
    private static String paramShortNameOf(autosar40.ecucdescription.EcucParameterValue p) {
        if (p == null) return null;
        gautosar.gecucparameterdef.GConfigParameter def = p.getDefinition();
        if (def == null) return null;
        if (def.eIsProxy()) {
            org.eclipse.emf.common.util.URI uri =
                    ((org.eclipse.emf.ecore.InternalEObject) def).eProxyURI();
            if (uri == null) return null;
            String frag = uri.fragment();
            if (frag == null) return null;
            int q = frag.indexOf('?');
            if (q >= 0) frag = frag.substring(0, q);
            int slash = frag.lastIndexOf('/');
            return slash >= 0 ? frag.substring(slash + 1) : frag;
        }
        return def.gGetShortName();  // typed
    }

    /**
     * Get a parameter's value as a String, using typed casts. Mirrors
     * iSoft's pattern: {@code setMixedText(String)} on the variation point
     * (verified via decompiled {@code DataTypeFactory.testCreateSimpleImplementationDataType}).
     */
    private static String extractTypedValue(autosar40.ecucdescription.EcucParameterValue p) {
        if (p instanceof autosar40.ecucdescription.EcucTextualParamValue) {
            // String / enum 直接 typed accessor
            return ((autosar40.ecucdescription.EcucTextualParamValue) p).getValue();
        }
        if (p instanceof autosar40.ecucdescription.EcucNumericalParamValue) {
            // Numeric / boolean 走 NumericalValueVariationPoint.getMixedText()
            // (FormulaExpression 接口提供, typed)
            autosar40.genericstructure.varianthandling.attributevaluevariationpoints.NumericalValueVariationPoint vp =
                    ((autosar40.ecucdescription.EcucNumericalParamValue) p).getValue();
            return vp != null ? vp.getMixedText() : null;
        }
        // Other parameter value types (reference, instance ref) — N/A for
        // MemIf 4 fields, return null.
        return null;
    }

    /**
     * Path-based overload. Tries to map the path back to an
     * {@link IFile} via the workspace root and route through
     * {@link #read(IFile)}; if the path is not in the workspace, falls back
     * to the legacy manual ResourceSet pipeline (kept around for headless
     * smoke tests and external callers).
     *
     * @param path absolute filesystem path to the ARXML file
     * @return populated {@link MemIfData}; fields not present in the file
     *         come back as {@code null}
     */
    public static MemIfData read(String path) {
        // Try to map path → workspace IFile so we can route through Sphinx.
        // 如果 path 在 workspace 内，调 read(IFile)；workspace 外或 Sphinx
        // 不可用时直接 readLegacy。
        // 注意: read(IFile) 自己会 fallback 到 readLegacy，不会回调 read(String)，
        // 避免栈溢出。
        try {
            IWorkspaceRoot wsRoot = ResourcesPlugin.getWorkspace().getRoot();
            IFile iFile = wsRoot.getFileForLocation(Path.fromOSString(path));
            if (iFile != null && iFile.exists()) {
                return read(iFile);
            }
        } catch (Throwable t) {
            // ResourcesPlugin 可能在 OSGi 没起来时抛 (e.g. unit test 环境)
            // → 直接走 legacy
        }
        return readLegacy(path);
    }

    /**
     * Legacy v0.1 manual-ResourceSet pipeline. Kept for fallback when
     * Sphinx can't claim the resource (project not in workspace, etc).
     * Will be deleted entirely once the workspace-import flow is the only
     * supported entry point (v0.2 late or v0.3).
     */
    private static MemIfData readLegacy(String path) {
        // JDK 17+ pitfall: Sphinx 0.11.2 was written for Java 8 and assumes
        // SAXParserFactory.newInstance() returns Apache Xerces. On modern JDKs
        // it returns the JDK-internal Xerces, which then ClassCast's on
        // Sphinx's ExtendedErrorHandlerWrapper. Force the JAXP factory to
        // Apache and switch the TCCL to our bundle (which Require-Bundles
        // org.apache.xerces) so the factory class is visible.
        ClassLoader savedTccl = Thread.currentThread().getContextClassLoader();
        String savedSaxFactoryProp = System.getProperty("javax.xml.parsers.SAXParserFactory");
        String savedDomFactoryProp = System.getProperty("javax.xml.parsers.DocumentBuilderFactory");
        try {
            Thread.currentThread().setContextClassLoader(MemIfArxmlReader.class.getClassLoader());
            System.setProperty("javax.xml.parsers.SAXParserFactory",
                    "org.apache.xerces.jaxp.SAXParserFactoryImpl");
            System.setProperty("javax.xml.parsers.DocumentBuilderFactory",
                    "org.apache.xerces.jaxp.DocumentBuilderFactoryImpl");

            ResourceSet rs = new ResourceSetImpl();
            registerAutosarFactory(rs);
            registerAutosarPackages(rs);

            Resource resource = rs.getResource(URI.createFileURI(path), true);

            return new MemIfData(
                    path,
                    findParam(resource, "MemIfDevErrorDetect"),
                    findParam(resource, "MemIfNumberOfDevices"),
                    findParam(resource, "MemIfVersionInfoApi"),
                    findParam(resource, "MemIfModuleVersion"));
        } finally {
            Thread.currentThread().setContextClassLoader(savedTccl);
            restoreOrClear("javax.xml.parsers.SAXParserFactory", savedSaxFactoryProp);
            restoreOrClear("javax.xml.parsers.DocumentBuilderFactory", savedDomFactoryProp);
        }
    }

    /**
     * Headless debug helper — dumps every EObject's EClass name + a few
     * features to System.out, prefixed with "A0_DUMP:". Called by Application
     * when {@code --test-load} is set. Production code never invokes this.
     */
    private static String truncate(String s, int max) {
        if (s == null) return "null";
        s = s.replace('\n', ' ').replace('\r', ' ');
        return s.length() > max ? s.substring(0, max) + "..." : s;
    }

    public static void debugDump(String path) {
        ClassLoader savedTccl = Thread.currentThread().getContextClassLoader();
        try {
            Thread.currentThread().setContextClassLoader(MemIfArxmlReader.class.getClassLoader());
            System.setProperty("javax.xml.parsers.SAXParserFactory",
                    "org.apache.xerces.jaxp.SAXParserFactoryImpl");
            ResourceSet rs = new ResourceSetImpl();
            registerAutosarFactory(rs);
            registerAutosarPackages(rs);
            Resource resource = rs.getResource(URI.createFileURI(path), true);
            System.out.println("A0_DUMP: top-level EObject count = "
                    + resource.getContents().size());
            int count = 0;
            TreeIterator<EObject> iter = resource.getAllContents();
            while (iter.hasNext() && count < 50) {
                EObject obj = iter.next();
                String className = obj.eClass().getName();
                if (className.toLowerCase().contains("paramvalue")) {
                    // Full feature list + value probe for these specifically
                    StringBuilder sb = new StringBuilder("A0_DUMP_PARAM: ");
                    sb.append(className).append(" allFeatures=[");
                    int f = 0;
                    for (EStructuralFeature feat : obj.eClass().getEAllStructuralFeatures()) {
                        if (f++ > 0) sb.append(",");
                        sb.append(feat.getName());
                    }
                    sb.append("]");
                    System.out.println(sb.toString());
                    // Try common names for "definition" + "value"
                    for (String fName : new String[]{"definition", "value"}) {
                        EStructuralFeature feat = obj.eClass().getEStructuralFeature(fName);
                        if (feat == null) continue;
                        Object raw = obj.eGet(feat, false);
                        if (raw instanceof EObject) {
                            EObject ref = (EObject) raw;
                            if (ref.eIsProxy()) {
                                org.eclipse.emf.common.util.URI u =
                                        ((org.eclipse.emf.ecore.InternalEObject) ref).eProxyURI();
                                System.out.println("A0_DUMP_PARAM:   " + fName + " = proxy fragment='"
                                        + (u == null ? "null" : u.fragment()) + "'");
                            } else {
                                // It's a contained EObject (e.g. NumericalValueVariationPoint)
                                // — dump its features too
                                System.out.println("A0_DUMP_PARAM:   " + fName + " = EObject("
                                        + ref.eClass().getName() + ")");
                                for (EStructuralFeature inner : ref.eClass().getEAllStructuralFeatures()) {
                                    Object innerRaw = ref.eGet(inner, false);
                                    if (innerRaw == null) continue;
                                    String summary = innerRaw.getClass().getSimpleName()
                                            + " = " + truncate(innerRaw.toString(), 80);
                                    System.out.println("A0_DUMP_PARAM:     ." + inner.getName()
                                            + " <" + summary + ">");
                                }
                            }
                        } else if (raw != null) {
                            System.out.println("A0_DUMP_PARAM:   " + fName + " = "
                                    + raw.getClass().getSimpleName() + "='" + raw + "'");
                        }
                    }
                } else {
                    System.out.println("A0_DUMP: " + className);
                }
                count++;
            }
            System.out.println("A0_DUMP: traversed " + count + " EObjects");
        } catch (Throwable t) {
            System.out.println("A0_DUMP: error " + t.getClass().getSimpleName() + ": " + t.getMessage());
        } finally {
            Thread.currentThread().setContextClassLoader(savedTccl);
        }
    }

    private static void restoreOrClear(String key, String saved) {
        if (saved == null) {
            System.clearProperty(key);
        } else {
            System.setProperty(key, saved);
        }
    }

    /**
     * Register the AUTOSAR-aware Resource.Factory for the {@code arxml}
     * extension by reflecting on Artop's classes. We can't import them
     * directly because Artop versions ship slightly different class names.
     *
     * <p>Falls back silently to whatever the global registry has — by the
     * time this runs inside the OSGi-activated RCP, Artop's bundle has
     * already registered factories on
     * {@link org.eclipse.emf.ecore.resource.Resource.Factory.Registry#INSTANCE}.
     */
    private static void registerAutosarFactory(ResourceSet rs) {
        for (String fqn : CANDIDATE_ARXML_FACTORIES) {
            // Try the INSTANCE singleton field first (preferred — Artop's
            // factory classes initialize themselves once via static init).
            try {
                Class<?> cls = Class.forName(fqn);
                Object instance;
                try {
                    instance = cls.getField("INSTANCE").get(null);
                } catch (NoSuchFieldException nsfe) {
                    instance = cls.getDeclaredConstructor().newInstance();
                }
                if (instance instanceof Resource.Factory) {
                    rs.getResourceFactoryRegistry()
                      .getExtensionToFactoryMap()
                      .put("arxml", (Resource.Factory) instance);
                    return;
                }
                System.err.println("[MemIfArxmlReader] " + fqn
                        + " is not a Resource.Factory (got "
                        + (instance == null ? "null" : instance.getClass().getName()) + ")");
            } catch (Throwable t) {
                Throwable cause = t.getCause() != null ? t.getCause() : t;
                System.err.println("[MemIfArxmlReader] cannot use " + fqn
                        + ": " + cause.getClass().getSimpleName() + ": " + cause.getMessage());
            }
        }
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
            if (!typeName.contains("paramvalue")) {
                continue;
            }
            String defRef = stringValueOf(obj, "definition");
            if (defRef == null) {
                defRef = stringValueOf(obj, "definitionRef");
            }
            if (defRef == null) {
                continue;
            }
            // Sphinx writes proxy URI fragments like
            //   /AUTOSAR/MemIf/MemIfGeneral/MemIfDevErrorDetect?type=EcucBooleanParamDef
            // Strip the ?type=... suffix before suffix-matching the short name.
            int q = defRef.indexOf('?');
            String defPath = (q >= 0) ? defRef.substring(0, q) : defRef;
            if (!defPath.endsWith(paramShortName)) {
                continue;
            }
            return stringValueOf(obj, "value");
        }
        return null;
    }

    /**
     * Read a feature value as String. For cross-reference features (e.g.
     * {@code definition} on EcucParameterValue) we **don't** resolve the
     * proxy — Sphinx's proxy resolver maps ECUC instance paths to a custom
     * {@code ar:} URI scheme that EMF's plain URL parser rejects on
     * isolated ARXML loads (no project context). Reading the proxy URI
     * fragment instead gives us the path string directly without triggering
     * resolution.
     */
    private static String stringValueOf(EObject obj, String featureName) {
        EStructuralFeature feature = obj.eClass().getEStructuralFeature(featureName);
        if (feature == null) {
            return null;
        }
        // Pass resolve=false so cross-references stay as proxies (no
        // MalformedURLException: unknown protocol: ar).
        Object raw = obj.eGet(feature, /* resolve */ false);
        if (raw instanceof EObject) {
            EObject ref = (EObject) raw;
            if (ref.eIsProxy()) {
                org.eclipse.emf.common.util.URI uri =
                        ((org.eclipse.emf.ecore.InternalEObject) ref).eProxyURI();
                if (uri != null) {
                    String frag = uri.fragment();
                    return (frag != null) ? frag : uri.toString();
                }
                return ref.toString();
            }
            // Contained EObject (e.g. NumericalValueVariationPoint) — drill into
            // its `mixed` FeatureMap to find the actual text content
            //   <VALUE>2</VALUE>  →  mixed[text]=2
            //   <VALUE>false</VALUE> → mixed[text]=false
            EStructuralFeature mixedFeat = ref.eClass().getEStructuralFeature("mixed");
            if (mixedFeat != null) {
                Object mixed = ref.eGet(mixedFeat);
                if (mixed instanceof org.eclipse.emf.ecore.util.FeatureMap) {
                    for (org.eclipse.emf.ecore.util.FeatureMap.Entry entry
                            : (org.eclipse.emf.ecore.util.FeatureMap) mixed) {
                        if ("text".equals(entry.getEStructuralFeature().getName())) {
                            Object v = entry.getValue();
                            return v != null ? v.toString() : null;
                        }
                    }
                }
            }
            return null;
        }
        return raw != null ? raw.toString() : null;
    }
}

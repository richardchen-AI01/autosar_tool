package cn.com.myorg.bswbuilder.modules.nvm.utils;

import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.nvm.utils.NvmUtils.
 *
 * <p>M1a stub — only the 3 entry points referenced by NvM functionextensions
 * are declared (getModule, isRteModelExist, isRamBlockService). M1b will
 * paraphrase the bodies (RteSoftwareComponentInstanceRef walk +
 * NvMBlockUsePort/NvMBlockUseSyncMechanism check + module lookup by name).
 */
public final class NvmUtils {

    private NvmUtils() {
    }

    /**
     * Reference: NvmUtils.getModule(GContainer, String) (line 341).
     *
     * <p>TODO M1b: walk to GAUTOSAR root then find module by short name.
     */
    public static GModuleConfiguration getModule(GContainer container, String moduleName) {
        throw new UnsupportedOperationException(
                "NvmUtils.getModule stub — not yet ported (M1a)");
    }

    /**
     * Reference: NvmUtils.isRteModelExist(EObject) (line 60).
     *
     * <p>TODO M1b: scan Rte module's RteSoftwareComponentInstanceRef list
     * for a SwComponentPrototype whose component shortName equals "NvM".
     */
    public static boolean isRteModelExist(EObject conf) {
        throw new UnsupportedOperationException(
                "NvmUtils.isRteModelExist stub — not yet ported (M1a)");
    }

    /**
     * Reference: NvmUtils.isRamBlockService(GContainer) (line 480).
     *
     * <p>TODO M1b: paraphrase the NvMBlockUsePort + NvMBlockUseSyncMechanism
     * predicate body.
     */
    public static boolean isRamBlockService(GContainer block) {
        throw new UnsupportedOperationException(
                "NvmUtils.isRamBlockService stub — not yet ported (M1a)");
    }
}

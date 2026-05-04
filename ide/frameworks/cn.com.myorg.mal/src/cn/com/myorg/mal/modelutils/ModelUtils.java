package cn.com.myorg.mal.modelutils;

import cn.com.myorg.mal.exceptions.ModelObjectNotFoundException;
import gautosar.gecucdescription.GModuleConfiguration;
import gautosar.ggenericstructure.ginfrastructure.GAUTOSAR;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.mal.modelutils.ModelUtils (extends ModelUtilsBase).
 *
 * <p>M1a stub — only the 3 entry points used by NvM functionextensions are
 * declared. Bodies throw UnsupportedOperationException so any runtime caller
 * trips immediately; M1b will paraphrase the resolver/ECU-root walks from
 * ModelUtilsBase.getEObjectByPath / getModelRootObject / getModuleConfiguration.
 */
public final class ModelUtils {

    private ModelUtils() {
    }

    /**
     * Reference: ModelUtilsBase.getEObjectByPath(String, Object)
     * (cn.com.isoft.mal.modelutils.ModelUtils line 112).
     *
     * <p>TODO M1b: paraphrase resource-walk + path-resolution body.
     */
    public static EObject getEObjectByPath(String path, EObject contextResolver)
            throws ModelObjectNotFoundException {
        throw new UnsupportedOperationException(
                "ModelUtils.getEObjectByPath stub — not yet ported (M1a)");
    }

    /**
     * Reference: ModelUtilsBase.getModuleConfiguration(GAUTOSAR, String)
     * (line 940).
     *
     * <p>TODO M1b: paraphrase scan-EcucValueCollection-for-shortName body.
     */
    public static GModuleConfiguration[] getModuleConfiguration(GAUTOSAR autosar, String shortName) {
        throw new UnsupportedOperationException(
                "ModelUtils.getModuleConfiguration stub — not yet ported (M1a)");
    }

    /**
     * Reference: ModelUtilsBase.getModelRootObject(EObject) (line 1092).
     *
     * <p>TODO M1b: walk eContainer until GAUTOSAR.
     */
    public static EObject getModelRootObject(EObject eObject) {
        throw new UnsupportedOperationException(
                "ModelUtils.getModelRootObject stub — not yet ported (M1a)");
    }
}

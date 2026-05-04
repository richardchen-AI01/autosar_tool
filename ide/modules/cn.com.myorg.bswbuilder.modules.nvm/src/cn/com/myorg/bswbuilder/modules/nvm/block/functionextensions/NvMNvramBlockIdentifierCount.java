package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import autosar40.ecucdescription.EcucNumericalParamValue;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import cn.com.myorg.mal.uidefinition.IAutoComputeUIDefinition;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMNvramBlockIdentifierCount.
 *
 * <p>Skeleton hook — compute always false / calc always null. Reference keeps
 * the parent dereference for symmetry with sibling Count classes; preserved.
 */
public class NvMNvramBlockIdentifierCount
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMNvramBlockIdentifier";
    }

    @Override
    public boolean compute(Object parentContainer) {
        return false;
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucNumericalParamValue) obj).eContainer();
        return null;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        return null;
    }
}

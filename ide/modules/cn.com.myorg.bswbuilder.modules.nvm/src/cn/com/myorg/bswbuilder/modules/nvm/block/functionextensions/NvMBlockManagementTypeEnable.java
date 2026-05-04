package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import autosar40.ecucdescription.EcucTextualParamValue;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import cn.com.myorg.mal.uidefinition.IAutoComputeUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMBlockManagementTypeEnable.
 */
public class NvMBlockManagementTypeEnable
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMBlockManagementType";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        String blockName = container.gGetShortName();
        return !"NvMBlock_ConfigID".equals(blockName);
    }

    @Override
    public List<String> getRelatedUIElementList() {
        return null;
    }

    @Override
    public Object calc(Object obj) {
        EObject block = ((EcucTextualParamValue) obj).eContainer();
        if ("NvMBlock_ConfigID".equals(((GContainer) block).gGetShortName())) {
            return "NVM_BLOCK_REDUNDANT";
        }
        return null;
    }
}

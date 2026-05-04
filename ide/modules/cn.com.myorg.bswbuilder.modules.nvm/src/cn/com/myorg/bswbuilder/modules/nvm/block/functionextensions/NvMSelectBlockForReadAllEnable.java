package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import autosar40.ecucdescription.EcucNumericalParamValue;
import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import cn.com.myorg.mal.uidefinition.IAutoComputeUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.ArrayList;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMSelectBlockForReadAllEnable.
 */
public class NvMSelectBlockForReadAllEnable
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMSelectBlockForReadAll";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        String blockName = container.gGetShortName();
        String type = EcuUtils.getEnumerationValue(container, "NvMBlockManagementType");
        String blockDataAddress = EcuUtils.getStringValue(container, "NvMRamBlockDataAddress");
        Boolean blockUseSyncMechanism = EcuUtils.getBooleanValue(container, "NvMBlockUseSyncMechanism");
        return !type.equals("NVM_BLOCK_DATASET")
                && !blockName.equals("NvMBlock_ConfigID")
                && (blockDataAddress != null || blockUseSyncMechanism != Boolean.FALSE);
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMBlockManagementType");
        lstRet.add("NvMRamBlockDataAddress");
        lstRet.add("NvMBlockUseSyncMechanism");
        return lstRet;
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucNumericalParamValue) obj).eContainer();
        if (parent instanceof GContainer) {
            GContainer container = (GContainer) parent;
            String name = container.gGetShortName();
            String type = EcuUtils.getEnumerationValue(container, "NvMBlockManagementType");
            String blockDataAddress = EcuUtils.getStringValue(container, "NvMRamBlockDataAddress");
            Boolean blockUseSyncMechanism = EcuUtils.getBooleanValue(container, "NvMBlockUseSyncMechanism");
            if (!name.equals("NvMBlock_ConfigID")
                    && (type.equals("NVM_BLOCK_DATASET")
                            || (blockDataAddress == null && !blockUseSyncMechanism.booleanValue()))) {
                return false;
            }
            if (name.equals("NvMBlock_ConfigID")) {
                return true;
            }
        }
        return null;
    }
}

package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import autosar40.ecucdescription.EcucNumericalParamValue;
import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import cn.com.myorg.mal.uidefinition.IAutoComputeUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMNvBlockNumEnable.
 */
public class NvMNvBlockNumEnable
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMNvBlockNum";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer nvMBlockDescriptor = (GContainer) parentContainer;
        String blockName = nvMBlockDescriptor.gGetShortName();
        String nvMBlockManagementType = EcuUtils.getEnumerationValue(nvMBlockDescriptor, "NvMBlockManagementType");
        return !blockName.equals("NvMBlock_ConfigID")
                && !"NVM_BLOCK_NATIVE".equalsIgnoreCase(nvMBlockManagementType)
                && !"NVM_BLOCK_REDUNDANT".equalsIgnoreCase(nvMBlockManagementType);
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMBlockManagementType");
        return lstRet;
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucNumericalParamValue) obj).eContainer();
        String nvMBlockManagementType = EcuUtils.getEnumerationValue((GContainer) parent, "NvMBlockManagementType");
        if (nvMBlockManagementType.equals("NVM_BLOCK_NATIVE")) {
            return BigInteger.valueOf(1L);
        }
        if (nvMBlockManagementType.equals("NVM_BLOCK_REDUNDANT")) {
            return BigInteger.valueOf(2L);
        }
        return null;
    }
}

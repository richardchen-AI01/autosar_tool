package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import autosar40.ecucdescription.EcucNumericalParamValue;
import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import cn.com.myorg.mal.uidefinition.IAutoComputeUIDefinition;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;
import java.util.ArrayList;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMResistantToChangedSwEnable.
 */
public class NvMResistantToChangedSwEnable
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMResistantToChangedSw";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        EObject nvm = container.eContainer();
        GContainer general = EcuUtils.getFirstModuleContainer((GModuleConfiguration) nvm, "NvMCommon");
        Boolean dynamicConfiguration = EcuUtils.getBooleanValue(general, "NvMDynamicConfiguration");
        return dynamicConfiguration != Boolean.FALSE;
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucNumericalParamValue) obj).eContainer();
        if (parent instanceof GContainer) {
            EObject nvm = parent.eContainer();
            GContainer general = EcuUtils.getFirstModuleContainer((GModuleConfiguration) nvm, "NvMCommon");
            Boolean dynamicConfiguration = EcuUtils.getBooleanValue(general, "NvMDynamicConfiguration");
            if (!dynamicConfiguration.booleanValue()) {
                return true;
            }
            if (((GContainer) parent).gGetShortName().equals("NvMBlock_ConfigID")) {
                return true;
            }
        }
        return null;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMDynamicConfiguration");
        return lstRet;
    }
}

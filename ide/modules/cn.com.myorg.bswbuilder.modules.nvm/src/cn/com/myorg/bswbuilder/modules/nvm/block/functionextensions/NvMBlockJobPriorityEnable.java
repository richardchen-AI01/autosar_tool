package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import autosar40.ecucdescription.EcucNumericalParamValue;
import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.modelutils.ModelUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import cn.com.myorg.mal.uidefinition.IAutoComputeUIDefinition;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;
import gautosar.ggenericstructure.ginfrastructure.GAUTOSAR;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMBlockJobPriorityEnable.
 */
public class NvMBlockJobPriorityEnable
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMBlockJobPriority";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        EObject nvm = container.eContainer();
        String blockName = container.gGetShortName();
        GContainer general = EcuUtils.getFirstModuleContainer((GModuleConfiguration) nvm, "NvMCommon");
        String apiconfigclass = EcuUtils.getEnumerationValue(general, "NvMApiConfigClass");
        Boolean jobPrioritization = EcuUtils.getBooleanValue(general, "NvMJobPrioritization");
        return !blockName.equals("NvMBlock_ConfigID")
                && !apiconfigclass.equals("NVM_API_CONFIG_CLASS_1")
                && jobPrioritization != Boolean.FALSE;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMJobPrioritization");
        lstRet.add("NvMApiConfigClass");
        return lstRet;
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucNumericalParamValue) obj).eContainer();
        if (parent instanceof GContainer) {
            String name = ((GContainer) parent).gGetShortName();
            GModuleConfiguration[] arrNvMModule = ModelUtils.getModuleConfiguration(
                    (GAUTOSAR) ModelUtils.getModelRootObject((GContainer) parent), "NvM");
            GContainer general = EcuUtils.getFirstModuleContainer(arrNvMModule[0], "NvMCommon");
            String apiconfigclass = EcuUtils.getEnumerationValue(general, "NvMApiConfigClass");
            Boolean jobPrioritization = EcuUtils.getBooleanValue(general, "NvMJobPrioritization");
            if (!name.equals("NvMBlock_ConfigID")
                    && !apiconfigclass.equals("NVM_API_CONFIG_CLASS_1")
                    && jobPrioritization.booleanValue()) {
                return null;
            }
        }
        return BigInteger.valueOf(1L);
    }
}

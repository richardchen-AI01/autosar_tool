package cn.com.myorg.bswbuilder.modules.nvm.common.functionextensions;

import autosar40.ecucdescription.EcucNumericalParamValue;
import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import cn.com.myorg.mal.uidefinition.IAutoComputeUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.ArrayList;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.nvm.common.functionextensions.NvMJobPrioritizationEnable.
 */
public class NvMJobPrioritizationEnable
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMJobPrioritization";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        String configClass = EcuUtils.getEnumerationValue(container, "NvMApiConfigClass");
        return !configClass.equals("NVM_API_CONFIG_CLASS_1");
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucNumericalParamValue) obj).eContainer();
        if (parent instanceof GContainer) {
            String configClass = EcuUtils.getEnumerationValue((GContainer) parent, "NvMApiConfigClass");
            if (configClass.equals("NVM_API_CONFIG_CLASS_1")) {
                return false;
            }
        }
        return null;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMApiConfigClass");
        return lstRet;
    }
}

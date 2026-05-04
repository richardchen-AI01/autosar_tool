package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import autosar40.ecucdescription.EcucTextualParamValue;
import cn.com.myorg.bswbuilder.modules.nvm.utils.NvmUtils;
import cn.com.myorg.mal.exceptions.ModelObjectNotFoundException;
import cn.com.myorg.mal.modelutils.ModelUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import cn.com.myorg.mal.uidefinition.IAutoComputeUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMSingleBlockCallbackEnable.
 */
public class NvMSingleBlockCallbackEnable
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMSingleBlockCallbackFnc";
    }

    @Override
    public boolean compute(Object parentContainer) {
        EObject initBlockCallbackObj = null;
        try {
            initBlockCallbackObj = ModelUtils.getEObjectByPath(
                    "NvMSingleBlockCallbackFnc", (EObject) parentContainer);
        } catch (ModelObjectNotFoundException e) {
            e.printStackTrace();
        }
        return initBlockCallbackObj != null;
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucTextualParamValue) obj).eContainer();
        String value = ((EcucTextualParamValue) obj).getValue();
        if (parent instanceof GContainer) {
            boolean rteModelExist = NvmUtils.isRteModelExist(parent);
            GContainer container = (GContainer) parent;
            String name = container.gGetShortName();
            if (rteModelExist && (value == null || value.trim().isEmpty())) {
                return "Rte_Call_NvM_PNJF_" + name + "_JobFinished";
            }
        }
        return null;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        return null;
    }
}

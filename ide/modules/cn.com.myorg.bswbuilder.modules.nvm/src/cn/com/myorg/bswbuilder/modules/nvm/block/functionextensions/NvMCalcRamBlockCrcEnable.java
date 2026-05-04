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
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMCalcRamBlockCrcEnable.
 */
public class NvMCalcRamBlockCrcEnable
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMCalcRamBlockCrc";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        String blockName = container.gGetShortName();
        Boolean blockUseCrc = EcuUtils.getBooleanValue(container, "NvMBlockUseCrc");
        if (blockName.equals("NvMBlock_ConfigID")) {
            return false;
        }
        return blockUseCrc != Boolean.FALSE;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMBlockUseCrc");
        return lstRet;
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucNumericalParamValue) obj).eContainer();
        if (parent instanceof GContainer) {
            String name = ((GContainer) parent).gGetShortName();
            if (name.equals("NvMBlock_ConfigID")) {
                return true;
            }
            Boolean blockUseCrc = EcuUtils.getBooleanValue((GContainer) parent, "NvMBlockUseCrc");
            if (!name.equals("NvMBlock_ConfigID") && !blockUseCrc.booleanValue()) {
                return false;
            }
        }
        return null;
    }
}

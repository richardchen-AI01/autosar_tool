package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import autosar40.ecucdescription.EcucTextualParamValue;
import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import cn.com.myorg.mal.uidefinition.IAutoComputeUIDefinition;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;
import java.util.ArrayList;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMRamBlockDataAddressEnable.
 */
public class NvMRamBlockDataAddressEnable
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMRamBlockDataAddress";
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucTextualParamValue) obj).eContainer();
        if (parent != null) {
            EObject nvm = parent.eContainer();
            if (parent instanceof GContainer) {
                Boolean nvMRamBlockDataBufferAutoFill =
                        EcuUtils.getBooleanValue((GContainer) parent, "NvMRamBlockDataBufferAutoFill");
                if (nvMRamBlockDataBufferAutoFill != null && nvMRamBlockDataBufferAutoFill.booleanValue()) {
                    List<GContainer> blocks = EcuUtils.getModuleChildContainers(
                            (GModuleConfiguration) nvm, "NvMBlockDescriptor");
                    int id = blocks.indexOf((GContainer) parent) + 1;
                    return "NvMBlockRamBuffer" + id;
                }
            }
        }
        return null;
    }

    @Override
    public boolean compute(Object parentContainer) {
        if (!(parentContainer instanceof GContainer)) {
            return true;
        }
        Boolean nvMRamBlockDataAddressAutoCount =
                EcuUtils.getBooleanValue((GContainer) parentContainer, "NvMRamBlockDataBufferAutoFill");
        return nvMRamBlockDataAddressAutoCount == null
                || nvMRamBlockDataAddressAutoCount == Boolean.FALSE;
    }

    @Override
    public long getVariant() {
        return super.getVariant();
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMRamBlockDataBufferAutoFill");
        return lstRet;
    }
}

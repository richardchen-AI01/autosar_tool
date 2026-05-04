package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import autosar40.ecucdescription.EcucNumericalParamValue;
import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.modelutils.ModelUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import cn.com.myorg.mal.uidefinition.IAutoComputeUIDefinition;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;
import gautosar.ggenericstructure.ginfrastructure.GAUTOSAR;
import java.util.ArrayList;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMBlockUseSetRamBlockStatusEnable.
 */
public class NvMBlockUseSetRamBlockStatusEnable
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMBlockUseSetRamBlockStatus";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        String blockName = container.gGetShortName();
        String blockDataAddress = EcuUtils.getStringValue(container, "NvMRamBlockDataAddress");
        Boolean blockUseSyncMechanism = EcuUtils.getBooleanValue(container, "NvMBlockUseSyncMechanism");
        GModuleConfiguration[] arrNvMModule = ModelUtils.getModuleConfiguration(
                (GAUTOSAR) ModelUtils.getModelRootObject(container), "NvM");
        GContainer general = EcuUtils.getFirstModuleContainer(arrNvMModule[0], "NvMCommon");
        Boolean setRamBlockStatusApi = EcuUtils.getBooleanValue(general, "NvMSetRamBlockStatusApi");
        return !blockName.equals("NvMBlock_ConfigID")
                && setRamBlockStatusApi != Boolean.FALSE
                && (blockUseSyncMechanism != Boolean.FALSE || blockDataAddress != null);
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMRamBlockDataAddress");
        lstRet.add("NvMBlockUseSyncMechanism");
        lstRet.add("NvMSetRamBlockStatusApi");
        return lstRet;
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucNumericalParamValue) obj).eContainer();
        if (parent instanceof GContainer) {
            String name = ((GContainer) parent).gGetShortName();
            String blockDataAddress = EcuUtils.getStringValue((GContainer) parent, "NvMRamBlockDataAddress");
            Boolean blockUseSyncMechanism = EcuUtils.getBooleanValue((GContainer) parent, "NvMBlockUseSyncMechanism");
            GModuleConfiguration[] arrNvMModule = ModelUtils.getModuleConfiguration(
                    (GAUTOSAR) ModelUtils.getModelRootObject((GContainer) parent), "NvM");
            GContainer general = EcuUtils.getFirstModuleContainer(arrNvMModule[0], "NvMCommon");
            Boolean setRamBlockStatusApi = EcuUtils.getBooleanValue(general, "NvMSetRamBlockStatusApi");
            if (!(name.equals("NvMBlock_ConfigID")
                    || setRamBlockStatusApi.booleanValue()
                            && (blockUseSyncMechanism.booleanValue() || blockDataAddress != null))) {
                return false;
            }
        }
        return null;
    }
}

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
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMNvBlockBaseNumberCount.
 */
public class NvMNvBlockBaseNumberCount
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMNvBlockBaseNumber";
    }

    @Override
    public boolean compute(Object parentContainer) {
        return false;
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucNumericalParamValue) obj).eContainer();
        GModuleConfiguration[] arrNvMModule = ModelUtils.getModuleConfiguration(
                (GAUTOSAR) ModelUtils.getModelRootObject((GContainer) parent), "NvM");
        GContainer general = EcuUtils.getFirstModuleContainer(arrNvMModule[0], "NvMCommon");
        Integer bits = EcuUtils.getIntegerValue(general, "NvMDatasetSelectionBits");
        if (bits != null) {
            GContainer blockRef = EcuUtils.getFirstChildContainer((GContainer) parent, "NvMTargetBlockReference");
            GContainer nvMEaRef = EcuUtils.getFirstChildContainer(blockRef, "NvMEaRef");
            if (nvMEaRef != null) {
                GContainer nvMNameOfEaBlock = EcuUtils.getSingleRefValue(nvMEaRef, "NvMNameOfEaBlock");
                if (nvMNameOfEaBlock != null) {
                    Integer blockNum = EcuUtils.getIntegerValue(nvMNameOfEaBlock, "EaBlockNumber");
                    if (blockNum != null) {
                        return BigInteger.valueOf(blockNum >> bits);
                    }
                }
            }
            GContainer nvMFeeRef = EcuUtils.getFirstChildContainer(blockRef, "NvMFeeRef");
            if (nvMFeeRef != null) {
                GContainer nvMNameOfFeeBlock = EcuUtils.getSingleRefValue(nvMFeeRef, "NvMNameOfFeeBlock");
                if (nvMNameOfFeeBlock != null) {
                    Integer blockNum = EcuUtils.getIntegerValue(nvMNameOfFeeBlock, "FeeBlockNumber");
                    if (blockNum != null) {
                        return BigInteger.valueOf(blockNum >> bits);
                    }
                }
            }
        }
        return null;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMDatasetSelectionBits");
        lstRet.add("NvMNameOfEaBlock");
        lstRet.add("NvMNameOfFeeBlock");
        return lstRet;
    }
}

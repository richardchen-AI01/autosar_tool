package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import autosar40.ecucdescription.EcucNumericalParamValue;
import cn.com.myorg.bswbuilder.modules.nvm.utils.NvmUtils;
import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.uidefinition.IAutoComputeUIDefinition;
import cn.com.myorg.mal.uidefinition.RelatedUIDefinition;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMNvramDeviceIdCount.
 */
public class NvMNvramDeviceIdCount
        extends RelatedUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMNvramDeviceId";
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucNumericalParamValue) obj).eContainer();
        GModuleConfiguration eaModule = NvmUtils.getModule((GContainer) parent, "Ea");
        GModuleConfiguration feeModule = NvmUtils.getModule((GContainer) parent, "Fee");
        GContainer blockRef = EcuUtils.getFirstChildContainer((GContainer) parent, "NvMTargetBlockReference");
        if (eaModule != null && feeModule != null) {
            GContainer nvMEaRef = EcuUtils.getFirstChildContainer(blockRef, "NvMEaRef");
            if (nvMEaRef != null) {
                GContainer nvMNameOfEaBlock = EcuUtils.getSingleRefValue(nvMEaRef, "NvMNameOfEaBlock");
                if (nvMNameOfEaBlock != null) {
                    return BigInteger.valueOf(1L);
                }
            }
            GContainer nvMFeeRef = EcuUtils.getFirstChildContainer(blockRef, "NvMFeeRef");
            if (nvMFeeRef != null) {
                GContainer nvMNameOfFeeBlock = EcuUtils.getSingleRefValue(nvMFeeRef, "NvMNameOfFeeBlock");
                if (nvMNameOfFeeBlock != null) {
                    return BigInteger.valueOf(0L);
                }
            }
        }
        return BigInteger.valueOf(0L);
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMNameOfEaBlock");
        lstRet.add("NvMNameOfFeeBlock");
        return lstRet;
    }

    @Override
    public long getVariant() {
        return 0L;
    }
}

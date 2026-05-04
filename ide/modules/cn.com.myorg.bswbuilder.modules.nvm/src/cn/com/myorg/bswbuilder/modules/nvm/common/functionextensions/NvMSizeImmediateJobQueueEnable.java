package cn.com.myorg.bswbuilder.modules.nvm.common.functionextensions;

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
 * Reference: cn.com.isoft.bswbuilder.modules.nvm.common.functionextensions.NvMSizeImmediateJobQueueEnable.
 */
public class NvMSizeImmediateJobQueueEnable
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMSizeImmediateJobQueue";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        Boolean nvMJobPrioritization = EcuUtils.getBooleanValue(container, "NvMJobPrioritization");
        return nvMJobPrioritization != Boolean.FALSE;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMJobPrioritization");
        return lstRet;
    }

    @Override
    public long getVariant() {
        return super.getVariant() | 0x10000L;
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucNumericalParamValue) obj).eContainer();
        if (parent instanceof GContainer) {
            Boolean nvMJobPrioritization = EcuUtils.getBooleanValue((GContainer) parent, "NvMJobPrioritization");
            if (!nvMJobPrioritization.booleanValue()) {
                return BigInteger.valueOf(0L);
            }
        }
        return null;
    }
}

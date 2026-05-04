package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

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
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMWriteVerificationDataSize.
 */
public class NvMWriteVerificationDataSize
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMWriteVerificationDataSize";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        Boolean verification = EcuUtils.getBooleanValue(container, "NvMWriteVerification");
        return verification != Boolean.FALSE;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMWriteVerification");
        lstRet.add("NvMNvBlockLength");
        return lstRet;
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucNumericalParamValue) obj).eContainer();
        if (parent instanceof GContainer) {
            Boolean verification = EcuUtils.getBooleanValue((GContainer) parent, "NvMWriteVerification");
            Integer length = EcuUtils.getIntegerValue((GContainer) parent, "NvMNvBlockLength");
            if (!verification.booleanValue() || length == null) {
                return BigInteger.valueOf(1L);
            }
            EcucNumericalParamValue numericalParamValue = (EcucNumericalParamValue) obj;
            if (numericalParamValue.getValue().eIsProxy()
                    || numericalParamValue.getValue().getMixedText().equals("1")) {
                return BigInteger.valueOf(length.intValue());
            }
        }
        return null;
    }
}

package cn.com.myorg.bswbuilder.modules.nvm.common.functionextensions;

import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.ArrayList;
import java.util.List;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.nvm.common.functionextensions.NvMMultiBlockCallbackEnable.
 */
public class NvMMultiBlockCallbackEnable extends ComputeEnableUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMMultiBlockCallback";
    }

    @Override
    public long getVariant() {
        return super.getVariant() | 0x10000L;
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        Boolean info = EcuUtils.getBooleanValue(container, "NvMBswMMultiBlockJobStatusInformation");
        return info == Boolean.FALSE;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMBswMMultiBlockJobStatusInformation");
        return lstRet;
    }
}

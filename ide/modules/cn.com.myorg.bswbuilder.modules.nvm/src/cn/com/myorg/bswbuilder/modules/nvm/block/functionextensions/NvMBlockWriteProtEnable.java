package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.ArrayList;
import java.util.List;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMBlockWriteProtEnable.
 */
public class NvMBlockWriteProtEnable extends ComputeEnableUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMBlockWriteProt";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        Boolean writeOnce = EcuUtils.getBooleanValue(container, "NvMWriteBlockOnce");
        return writeOnce == Boolean.FALSE;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMWriteBlockOnce");
        return lstRet;
    }
}

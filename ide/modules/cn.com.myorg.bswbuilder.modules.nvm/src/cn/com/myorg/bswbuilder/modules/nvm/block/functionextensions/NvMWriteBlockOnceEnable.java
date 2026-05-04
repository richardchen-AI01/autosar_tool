package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.ArrayList;
import java.util.List;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMWriteBlockOnceEnable.
 */
public class NvMWriteBlockOnceEnable extends ComputeEnableUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMWriteBlockOnce";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        Boolean writeProt = EcuUtils.getBooleanValue(container, "NvMBlockWriteProt");
        return writeProt == Boolean.FALSE;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMBlockWriteProt");
        return lstRet;
    }
}

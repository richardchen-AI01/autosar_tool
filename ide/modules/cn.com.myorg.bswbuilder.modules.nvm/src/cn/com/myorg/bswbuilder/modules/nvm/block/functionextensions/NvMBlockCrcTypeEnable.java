package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.ArrayList;
import java.util.List;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMBlockCrcTypeEnable.
 */
public class NvMBlockCrcTypeEnable extends ComputeEnableUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMBlockCrcType";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        Boolean nvMBlockUseCrc = EcuUtils.getBooleanValue(container, "NvMBlockUseCrc");
        return nvMBlockUseCrc != null && nvMBlockUseCrc != Boolean.FALSE;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMBlockUseCrc");
        return lstRet;
    }

    @Override
    public long getVariant() {
        return super.getVariant() | 0x10000L;
    }
}

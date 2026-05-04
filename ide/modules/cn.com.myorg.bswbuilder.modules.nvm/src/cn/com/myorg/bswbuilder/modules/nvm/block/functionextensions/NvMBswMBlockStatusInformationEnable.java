package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.List;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMBswMBlockStatusInformationEnable.
 */
public class NvMBswMBlockStatusInformationEnable extends ComputeEnableUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMBswMBlockStatusInformation";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        String blockName = container.gGetShortName();
        return !blockName.equals("NvMBlock_ConfigID");
    }

    @Override
    public List<String> getRelatedUIElementList() {
        return null;
    }
}

package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.List;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMRomBlockDataAddressEnable.
 */
public class NvMRomBlockDataAddressEnable extends ComputeEnableUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMRomBlockDataAddress";
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

    @Override
    public long getVariant() {
        return super.getVariant() | 0x10000L;
    }
}

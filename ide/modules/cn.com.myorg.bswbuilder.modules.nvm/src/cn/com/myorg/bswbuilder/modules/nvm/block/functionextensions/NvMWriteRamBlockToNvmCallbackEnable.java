package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.ArrayList;
import java.util.List;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMWriteRamBlockToNvmCallbackEnable.
 *
 * <p>Note: getDefElementName returns "NvMWriteRamBlockToNvCallback" — yes the
 * class name has "Nvm" but the def name has "Nv"; preserved verbatim from
 * reference.
 */
public class NvMWriteRamBlockToNvmCallbackEnable extends ComputeEnableUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMWriteRamBlockToNvCallback";
    }

    @Override
    public long getVariant() {
        return super.getVariant() | 0x10000L;
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        String blockName = container.gGetShortName();
        Boolean blockUseSyncMechanism = EcuUtils.getBooleanValue(container, "NvMBlockUseSyncMechanism");
        return !blockName.equals("NvMBlock_ConfigID") && blockUseSyncMechanism != Boolean.FALSE;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMBlockUseSyncMechanism");
        return lstRet;
    }
}

package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.List;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMBlockUseSyncMechanismEnable.
 *
 * <p>Note: reference's getDefElementName returns "NvMBlockUseCRCCompMechanism"
 * (verbatim copy from sibling, looks like an upstream naming bug — preserved
 * for 99% fidelity).
 */
public class NvMBlockUseSyncMechanismEnable extends ComputeEnableUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMBlockUseCRCCompMechanism";
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

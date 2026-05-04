package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import java.util.List;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.SelectionEnable.
 *
 * <p>Generic always-disabled hook constructed with the def name to apply to.
 * Used to mass-disable fields that are always read-only in the UI for a given
 * scenario.
 */
public class SelectionEnable extends ComputeEnableUIDefinition {

    private String defName;

    public SelectionEnable(String defName) {
        this.defName = defName;
    }

    @Override
    public String getDefElementName() {
        return this.defName;
    }

    @Override
    public boolean compute(Object parentContainer) {
        return false;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        return null;
    }
}

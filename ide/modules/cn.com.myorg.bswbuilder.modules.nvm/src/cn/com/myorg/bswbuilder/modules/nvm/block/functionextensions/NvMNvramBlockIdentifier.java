package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import autosar40.ecucdescription.EcucTextualParamValue;
import cn.com.myorg.mal.uidefinition.IAutoComputeUIDefinition;
import cn.com.myorg.mal.uidefinition.RelatedUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMNvramBlockIdentifier.
 */
public class NvMNvramBlockIdentifier
        extends RelatedUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMNvramBlockIdentifier";
    }

    @Override
    public long getVariant() {
        return 0L;
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucTextualParamValue) obj).eContainer();
        if (parent instanceof GContainer) {
            String name = ((GContainer) parent).gGetShortName();
            return "NvMConf_NvMBlockDescriptor_" + name;
        }
        return null;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        return null;
    }
}

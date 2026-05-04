package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import autosar40.ecucdescription.EcucTextualParamValue;
import cn.com.myorg.bswbuilder.modules.nvm.utils.NvmUtils;
import cn.com.myorg.mal.uidefinition.IAutoComputeUIDefinition;
import cn.com.myorg.mal.uidefinition.RelatedUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.ArrayList;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMWriteRamBlockToNvCallback.
 */
public class NvMWriteRamBlockToNvCallback
        extends RelatedUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMWriteRamBlockToNvCallback";
    }

    @Override
    public long getVariant() {
        return 0L;
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucTextualParamValue) obj).eContainer();
        if (parent instanceof GContainer) {
            GContainer container = (GContainer) parent;
            boolean ramBlockService = NvmUtils.isRamBlockService(container);
            if (ramBlockService) {
                String name = container.gGetShortName();
                return "Rte_Call_PM_" + name + "_WriteRamBlockToNvM";
            }
        }
        return null;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMBlockUsePort");
        lstRet.add("NvMBlockUseSyncMechanism");
        return lstRet;
    }
}

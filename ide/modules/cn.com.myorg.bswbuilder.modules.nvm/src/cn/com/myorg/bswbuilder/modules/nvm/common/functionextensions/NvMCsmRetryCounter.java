package cn.com.myorg.bswbuilder.modules.nvm.common.functionextensions;

import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import gautosar.gecucdescription.GModuleConfiguration;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.common.functionextensions.NvMCsmRetryCounter.
 *
 * <p>Reference uses cn.com.isoft.bswbuilder.common.def.NvMDef.NvMCsmRetryCounter.value()
 * and NvMDef.NvMBlockCiphering.value(); MEN inlines those resolved string
 * literals (NvMDef enum not yet ported into MEN's bswbuilder.common bundle —
 * 1% deviation, byte-equivalent at runtime).
 */
public class NvMCsmRetryCounter extends ComputeEnableUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMCsmRetryCounter";
    }

    @Override
    public boolean compute(Object parentContainer) {
        EObject nvmConf = ((EObject) parentContainer).eContainer();
        if (nvmConf instanceof GModuleConfiguration) {
            List lstNvMBlockCiphering = EcuUtils.getModuleChildContainers(
                    (GModuleConfiguration) nvmConf, "NvMBlockCiphering");
            return lstNvMBlockCiphering != null && !lstNvMBlockCiphering.isEmpty();
        }
        return false;
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

package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.uidefinition.EnumValueScopeUIDefinition;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;
import java.util.ArrayList;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMBlockManagementType.
 *
 * <p>Limits the NvMBlockManagementType enum candidate set to {NATIVE,
 * REDUNDANT} when NvMApiConfigClass == NVM_API_CONFIG_CLASS_1, else full set.
 */
public class NvMBlockManagementType extends EnumValueScopeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMBlockManagementType";
    }

    @Override
    public String[] getValueScope(Object parent) {
        GContainer container = (GContainer) parent;
        ArrayList<String> directionRange = new ArrayList<>();
        if (container != null) {
            directionRange.clear();
            EObject nvm = container.eContainer();
            GContainer general = EcuUtils.getFirstModuleContainer((GModuleConfiguration) nvm, "NvMCommon");
            String apiconfigclass = EcuUtils.getEnumerationValue(general, "NvMApiConfigClass");
            if (apiconfigclass.equals("NVM_API_CONFIG_CLASS_1")) {
                directionRange.add("NVM_BLOCK_NATIVE");
                directionRange.add("NVM_BLOCK_REDUNDANT");
            } else {
                directionRange.add("NVM_BLOCK_DATASET");
                directionRange.add("NVM_BLOCK_NATIVE");
                directionRange.add("NVM_BLOCK_REDUNDANT");
            }
            String[] type = new String[directionRange.size()];
            int i = 0;
            while (i < directionRange.size()) {
                type[i] = directionRange.get(i).toString();
                ++i;
            }
            return type;
        }
        directionRange.add("NVM_BLOCK_DATASET");
        directionRange.add("NVM_BLOCK_NATIVE");
        directionRange.add("NVM_BLOCK_REDUNDANT");
        String[] type = new String[directionRange.size()];
        int i = 0;
        while (i < directionRange.size()) {
            type[i] = directionRange.get(i).toString();
            ++i;
        }
        return type;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMApiConfigClass");
        return lstRet;
    }
}

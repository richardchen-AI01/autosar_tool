package cn.com.myorg.bswbuilder.modules.nvm.functionextensions;

import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMBlockUseCrcEnable;
import cn.com.myorg.mal.interfaces.IFunctionExtension;
import cn.com.myorg.mal.interfaces.IModuleInit;
import cn.com.myorg.mal.uidefinition.IUIDefinition;
import cn.com.myorg.mal.uidefinition.UIDefinitionMap;
import java.util.HashMap;
import java.util.Map;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.nvm.functionextensions.NvMFunctionExtension.
 *
 * <p>Phase 2.5 PoC: registers only NvMBlockUseCrcEnable to validate the hook
 * dispatch chain end-to-end. Phase 6c expands to the full 32 sub-extensions
 * (mirroring the reference NvMFunctionExtension.getUIDefinitionMap body).
 */
public class NvMFunctionExtension implements IFunctionExtension {

    @Override
    public UIDefinitionMap getUIDefinitionMap() {
        UIDefinitionMap uiDefinitionMap = new UIDefinitionMap();
        uiDefinitionMap.put((IUIDefinition) new NvMBlockUseCrcEnable());
        return uiDefinitionMap;
    }

    @Override
    public IModuleInit getModuleInit() {
        return null;
    }

    @Override
    public Map<String, DataHandle> getDataHandleMap() {
        return new HashMap<>();
    }
}

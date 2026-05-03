package cn.com.myorg.bswbuilder.modules.memif.functionextensions;

import cn.com.myorg.mal.interfaces.IFunctionExtension;
import cn.com.myorg.mal.interfaces.IModuleInit;
import cn.com.myorg.mal.uidefinition.UIDefinitionMap;
import java.util.Map;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.memif.functionextensions.MemIfFunctionExtension.
 *
 * <p>Reference returns an empty UIDefinitionMap and null DataHandle map —
 * MemIf has no field-enable rules registered explicitly (the 2 reference
 * MemIfGeneralEaMapSupport / MemIfGeneralFeeMapSupportEnable are picked up by
 * the implicit OSGi extension-point scanner; not exercised in our PoC).
 */
public class MemIfFunctionExtension implements IFunctionExtension {

    @Override
    public UIDefinitionMap getUIDefinitionMap() {
        return new UIDefinitionMap();
    }

    @Override
    public IModuleInit getModuleInit() {
        return null;
    }

    @Override
    public Map<String, DataHandle> getDataHandleMap() {
        return null;
    }
}

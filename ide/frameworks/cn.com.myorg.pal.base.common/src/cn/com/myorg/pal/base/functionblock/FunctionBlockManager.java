package cn.com.myorg.pal.base.functionblock;

import cn.com.myorg.pal.base.common.Activator;
import cn.com.myorg.pal.base.interfaces.common.IFunctionBlock;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import org.eclipse.core.runtime.IConfigurationElement;
import org.eclipse.core.runtime.IExtension;
import org.eclipse.core.runtime.IExtensionPoint;
import org.eclipse.core.runtime.IExtensionRegistry;
import org.eclipse.core.runtime.Platform;
import org.eclipse.core.runtime.Plugin;
import org.eclipse.sphinx.platform.util.PlatformLogUtil;

public class FunctionBlockManager {
    private static Map<String, IFunctionBlock> mapFunctionBlock;
    private static final String funcBlockExtensionPoint = "cn.com.myorg.pal.base.common.FunctionBlock";

    public static Collection<IFunctionBlock> getRegFunctionBlock() {
        if (mapFunctionBlock == null) {
            FunctionBlockManager.createFunctionBlockMap();
        }
        assert (mapFunctionBlock != null);
        return mapFunctionBlock.values();
    }

    private static void createFunctionBlockMap() {
        HashMap registry = new HashMap();
        mapFunctionBlock = Collections.synchronizedMap(registry);
        IExtensionRegistry reg = Platform.getExtensionRegistry();
        IExtensionPoint extensionPoint = reg.getExtensionPoint(funcBlockExtensionPoint);
        if (extensionPoint == null) {
            return;
        }
        IExtension[] iExtensionArray = extensionPoint.getExtensions();
        int n = iExtensionArray.length;
        int n2 = 0;
        while (n2 < n) {
            IExtension extension = iExtensionArray[n2];
            try {
                IConfigurationElement configElement = extension.getConfigurationElements()[0];
                Object obj = configElement.createExecutableExtension("FunctionBlock");
                IFunctionBlock unit = (IFunctionBlock)obj;
                assert (unit.getId() != null);
                mapFunctionBlock.put(unit.getId(), unit);
            }
            catch (Exception e) {
                PlatformLogUtil.logAsError((Plugin)Activator.getDefault(), (Object)e);
            }
            ++n2;
        }
    }
}

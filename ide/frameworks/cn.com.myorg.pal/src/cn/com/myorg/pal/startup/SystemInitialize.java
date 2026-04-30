package cn.com.myorg.pal.startup;

import cn.com.myorg.pal.Activator;
import cn.com.myorg.pal.base.interfaces.common.IFunctionBlock;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IConfigurationElement;
import org.eclipse.core.runtime.Platform;
import org.eclipse.core.runtime.Plugin;
import org.eclipse.sphinx.platform.util.PlatformLogUtil;

public class SystemInitialize {
    private static SystemInitialize Instance = null;

    public static SystemInitialize getInstance() {
        if (Instance == null) {
            Instance = new SystemInitialize();
        }
        return Instance;
    }

    public void initialize() {
        IConfigurationElement[] arrayConfigurationElement;
        IConfigurationElement[] iConfigurationElementArray = arrayConfigurationElement = Platform.getExtensionRegistry().getConfigurationElementsFor("cn.com.myorg.pal.base.common.FunctionBlock");
        int n = arrayConfigurationElement.length;
        int n2 = 0;
        while (n2 < n) {
            IConfigurationElement configurationElement = iConfigurationElementArray[n2];
            Object executableExtension = null;
            try {
                executableExtension = configurationElement.createExecutableExtension("FunctionBlock");
            }
            catch (CoreException e) {
                PlatformLogUtil.logAsError((Plugin)Activator.getDefault(), (Object)((Object)e));
            }
            if (executableExtension != null && executableExtension instanceof IFunctionBlock) {
                IFunctionBlock functionBlock = (IFunctionBlock)executableExtension;
                functionBlock.initialize();
            }
            ++n2;
        }
    }
}

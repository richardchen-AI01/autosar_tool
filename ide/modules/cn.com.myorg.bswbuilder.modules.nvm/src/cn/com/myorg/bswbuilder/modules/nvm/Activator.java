package cn.com.myorg.bswbuilder.modules.nvm;

import org.eclipse.core.runtime.Plugin;
import org.osgi.framework.BundleContext;

/**
 * NvM module-plugin activator.
 *
 * <p>v0.1 stays minimal — actual NvM schema / form layout / generator
 * all live on the Python side. This bundle exists so the Eclipse extension
 * registry has a place to hang NvM-specific IoC contributions.
 */
public class Activator extends Plugin {

    public static final String PLUGIN_ID = "cn.com.myorg.bswbuilder.modules.nvm";

    private static Activator instance;

    @Override
    public void start(BundleContext context) throws Exception {
        super.start(context);
        instance = this;
    }

    @Override
    public void stop(BundleContext context) throws Exception {
        instance = null;
        super.stop(context);
    }

    public static Activator getDefault() {
        return instance;
    }
}

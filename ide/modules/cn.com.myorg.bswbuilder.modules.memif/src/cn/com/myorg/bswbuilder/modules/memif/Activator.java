package cn.com.myorg.bswbuilder.modules.memif;

import org.eclipse.core.runtime.Plugin;
import org.osgi.framework.BundleContext;

/**
 * MemIf module-plugin activator.
 *
 * <p>v0.1 stays minimal — the actual MemIf schema / form layout / generator
 * all live on the Python side. This bundle exists so the Eclipse extension
 * registry has a place to hang MemIf-specific contributions when ARTOP
 * integration lands (M3.3+).
 */
public class Activator extends Plugin {

    public static final String PLUGIN_ID = "cn.com.myorg.bswbuilder.modules.memif";

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

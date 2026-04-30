package cn.com.myorg.pal;

import org.eclipse.core.runtime.Plugin;
import org.osgi.framework.BundleContext;

/**
 * Reference: cn.com.isoft.pal.Activator — extends AbstractUIPlugin in reference
 * (registers SaveInterceptor on workbench commands). For E3-B-4 we only need
 * the Plugin.getDefault() accessor; SaveInterceptor wiring deferred to the
 * UI integration phase. Promote to AbstractUIPlugin when SaveInterceptor is
 * added (E3-B-5/6).
 */
public class Activator extends Plugin {

    public static final String PLUGIN_ID = "cn.com.myorg.pal";

    private static Activator plugin;

    public Activator() {}

    @Override
    public void start(BundleContext context) throws Exception {
        super.start(context);
        plugin = this;
    }

    @Override
    public void stop(BundleContext context) throws Exception {
        plugin = null;
        super.stop(context);
    }

    public static Activator getDefault() { return plugin; }
}

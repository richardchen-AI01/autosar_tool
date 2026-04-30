package cn.com.myorg.mal;

import org.eclipse.core.runtime.Plugin;
import org.osgi.framework.BundleContext;

/**
 * Reference: cn.com.isoft.mal.Activator — bundle activator + global
 * Plugin.getDefault() accessor (used by PlatformLogUtil for error logging).
 */
public class Activator extends Plugin {

    public static final String PLUGIN_ID = "cn.com.myorg.mal";

    private static Activator plugin;

    public Activator() { /* default ctor */ }

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

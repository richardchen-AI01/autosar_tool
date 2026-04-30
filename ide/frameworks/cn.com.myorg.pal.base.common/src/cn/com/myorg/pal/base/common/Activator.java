package cn.com.myorg.pal.base.common;

import org.eclipse.core.runtime.Plugin;
import org.osgi.framework.BundleContext;

/** Reference: cn.com.isoft.pal.base.common.Activator. */
public class Activator extends Plugin {

    public static final String PLUGIN_ID = "cn.com.myorg.pal.base.common";

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

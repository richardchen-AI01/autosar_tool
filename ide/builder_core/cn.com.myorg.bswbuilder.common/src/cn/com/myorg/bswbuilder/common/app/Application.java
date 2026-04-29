package cn.com.myorg.bswbuilder.common.app;

import java.lang.reflect.Method;

import org.eclipse.equinox.app.IApplication;
import org.eclipse.equinox.app.IApplicationContext;
import org.eclipse.swt.widgets.Display;
import org.eclipse.ui.IWorkbench;
import org.eclipse.ui.PlatformUI;

/**
 * RCP application entry. Boots the workbench with WorkbenchAdvisor, returns
 * EXIT_OK on graceful shutdown or EXIT_RESTART when the user requests restart.
 *
 * <p>Special headless probe mode: if the launcher is invoked with
 * {@code --test-load=<path>} as an application arg, the workbench is NOT
 * started; instead {@code MemIfArxmlReader.read} is invoked on the given
 * path and the resulting 4 MemIfGeneral parameters are printed to stdout in
 * a parseable form, then the process exits with EXIT_OK. Used by
 * tools/test_memif_a0_load.sh to prove the EMF load path works inside the
 * real OSGi runtime (not just plain-Java).
 */
public class Application implements IApplication {

    @Override
    public Object start(IApplicationContext context) {
        Object argsObj = context.getArguments().get(IApplicationContext.APPLICATION_ARGS);
        if (argsObj instanceof String[]) {
            String[] args = (String[]) argsObj;
            for (String a : args) {
                if (a != null && a.startsWith("--test-load=")) {
                    return runHeadlessTestLoad(a.substring("--test-load=".length()));
                }
            }
        }

        Display display = PlatformUI.createDisplay();
        try {
            int returnCode = PlatformUI.createAndRunWorkbench(
                    display, new ApplicationWorkbenchAdvisor());
            if (returnCode == PlatformUI.RETURN_RESTART) {
                return IApplication.EXIT_RESTART;
            }
            return IApplication.EXIT_OK;
        } finally {
            display.dispose();
        }
    }

    /**
     * Headless probe — calls MemIfArxmlReader.read via reflection (avoids hard
     * compile-time dep from common bundle on memif bundle), prints values
     * marked {@code A0_PROBE:} so the test script can grep them.
     */
    private Object runHeadlessTestLoad(String path) {
        try {
            // Resolve via the memif bundle's class loader (cross-bundle
            // reflection — Class.forName(...) uses our bundle's loader and
            // can't see memif's Export-Package).
            org.osgi.framework.Bundle memifBundle =
                    org.eclipse.core.runtime.Platform.getBundle(
                            "cn.com.myorg.bswbuilder.modules.memif");
            if (memifBundle == null) {
                throw new IllegalStateException("memif bundle not loaded");
            }

            // DEBUG dump: load resource directly and list every EObject's
            // EClass name + first few feature names. Helps diagnose why
            // findParam returned null on a successful load.
            try {
                Class<?> dumpCls = memifBundle.loadClass(
                        "cn.com.myorg.bswbuilder.modules.memif.data.MemIfArxmlReader");
                Method dumpM = dumpCls.getMethod("debugDump", String.class);
                dumpM.invoke(null, path);
            } catch (Throwable d) {
                System.err.println("A0_PROBE: debugDump skipped: " + d.getMessage());
            }

            Class<?> readerCls = memifBundle.loadClass(
                    "cn.com.myorg.bswbuilder.modules.memif.data.MemIfArxmlReader");
            Method readM = readerCls.getMethod("read", String.class);
            Object data = readM.invoke(null, path);
            Class<?> dataCls = data.getClass();
            String dev  = (String) dataCls.getMethod("getMemIfDevErrorDetect").invoke(data);
            String num  = (String) dataCls.getMethod("getMemIfNumberOfDevices").invoke(data);
            String vapi = (String) dataCls.getMethod("getMemIfVersionInfoApi").invoke(data);
            String mver = (String) dataCls.getMethod("getMemIfModuleVersion").invoke(data);
            System.out.println("A0_PROBE: path=" + path);
            System.out.println("A0_PROBE: DevErrorDetect=" + dev);
            System.out.println("A0_PROBE: NumberOfDevices=" + num);
            System.out.println("A0_PROBE: VersionInfoApi=" + vapi);
            System.out.println("A0_PROBE: ModuleVersion=" + mver);
            System.out.println("A0_PROBE: STATUS=PASS");
            return IApplication.EXIT_OK;
        } catch (Throwable t) {
            Throwable cause = t.getCause() != null ? t.getCause() : t;
            System.err.println("A0_PROBE: STATUS=FAIL");
            System.err.println("A0_PROBE: exception=" + cause.getClass().getName());
            System.err.println("A0_PROBE: message=" + cause.getMessage());
            cause.printStackTrace();
            return Integer.valueOf(1);
        }
    }

    @Override
    public void stop() {
        IWorkbench workbench = PlatformUI.getWorkbench();
        if (workbench == null || workbench.isClosing()) {
            return;
        }
        Display display = workbench.getDisplay();
        display.syncExec(() -> {
            if (!workbench.isClosing()) {
                workbench.close();
            }
        });
    }
}

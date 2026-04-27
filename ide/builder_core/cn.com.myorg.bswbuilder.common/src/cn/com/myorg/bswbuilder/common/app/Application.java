package cn.com.myorg.bswbuilder.common.app;

import org.eclipse.equinox.app.IApplication;
import org.eclipse.equinox.app.IApplicationContext;
import org.eclipse.swt.widgets.Display;
import org.eclipse.ui.IWorkbench;
import org.eclipse.ui.PlatformUI;

/**
 * RCP application entry. Boots the workbench with WorkbenchAdvisor, returns
 * EXIT_OK on graceful shutdown or EXIT_RESTART when the user requests restart.
 */
public class Application implements IApplication {

    @Override
    public Object start(IApplicationContext context) {
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

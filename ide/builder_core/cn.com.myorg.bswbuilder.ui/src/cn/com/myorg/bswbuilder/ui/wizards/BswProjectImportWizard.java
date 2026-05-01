package cn.com.myorg.bswbuilder.ui.wizards;

import org.eclipse.ui.IWorkbench;
import org.eclipse.ui.IWorkbenchWindow;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.WorkbenchException;
import org.eclipse.ui.wizards.datatransfer.ExternalProjectImportWizard;

/**
 * "Existing BSW Project into Workspace" — thin subclass of Eclipse's standard
 * "Existing Projects into Workspace" wizard
 * ({@link ExternalProjectImportWizard}, public API). Reuses the same UI and
 * import logic the user gets from {@code File → Import → General → Existing
 * Projects into Workspace}; only adds a perspective switch on finish so
 * AUTOSAR Explorer ends up visible.
 *
 * <p>Reference: V25.10 has a placeholder {@code cn.com.isoft.importWizards}
 * category with no concrete wizards inside. We populate ours with this thin
 * shortcut so {@code File → Import → BSW Configurator → Existing BSW Project}
 * does the right thing in one step.
 */
public class BswProjectImportWizard extends ExternalProjectImportWizard {

    private static final String BSW_PERSPECTIVE_ID =
            "cn.com.myorg.bswbuilder.common.perspective";

    public BswProjectImportWizard() {
        super();
        setWindowTitle("Import BSW Project");
    }

    @Override
    public boolean performFinish() {
        boolean ok = super.performFinish();
        if (ok) {
            switchToBswPerspective();
        }
        return ok;
    }

    private static void switchToBswPerspective() {
        IWorkbench wb = PlatformUI.getWorkbench();
        IWorkbenchWindow win = wb.getActiveWorkbenchWindow();
        if (win == null) return;
        try {
            wb.showPerspective(BSW_PERSPECTIVE_ID, win);
        } catch (WorkbenchException ignored) {
            // not fatal — user can switch manually if perspective fails to open.
        }
    }
}

package cn.com.myorg.bswbuilder.modules.memif.handlers;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.FileDialog;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.ui.handlers.HandlerUtil;

import cn.com.myorg.bswbuilder.modules.memif.data.MemIfArxmlReader;
import cn.com.myorg.bswbuilder.modules.memif.data.MemIfData;

/**
 * Phase 1 toolbar action — kept as a fast diagnostic alongside the Phase A
 * tree-driven flow. Both call paths share {@link MemIfArxmlReader} for the
 * actual load + walk; this handler additionally pops a MessageDialog so a
 * developer can see in one click "did EMF/Artop accept the file".
 *
 * <p>Phase A's tree click in
 * {@code ConfigurationEditorsView} also feeds the result into
 * {@code PropertyFormView}; this handler does the same so the toolbar
 * button stays usable as a no-tree-needed quick-test.
 */
public class LoadMemIfArxmlHandler extends AbstractHandler {

    @Override
    public Object execute(ExecutionEvent event) throws ExecutionException {
        Shell shell = HandlerUtil.getActiveShell(event);

        FileDialog dialog = new FileDialog(shell, SWT.OPEN);
        dialog.setFilterExtensions(new String[] { "*.arxml" });
        dialog.setText("Select an ARXML file (e.g. samples/Demo_S32K148/.../MemIf.arxml)");
        String path = dialog.open();
        if (path == null) {
            return null;
        }

        try {
            MemIfData data = MemIfArxmlReader.read(path);
            String body = "ARXML       : " + data.getSourcePath() + "\n"
                        + "DevErrorDetect      = " + nullToDash(data.getMemIfDevErrorDetect()) + "\n"
                        + "NumberOfDevices     = " + nullToDash(data.getMemIfNumberOfDevices()) + "\n"
                        + "VersionInfoApi      = " + nullToDash(data.getMemIfVersionInfoApi()) + "\n"
                        + "ModuleVersion       = " + nullToDash(data.getMemIfModuleVersion());
            System.out.println("[LoadMemIfArxml]\n" + body);

            // Phase A: also feed PropertyFormView so the parameters show up
            // in the right pane. PropertyFormView class is in the ui bundle;
            // we look it up via the workbench instead of an OSGi import to
            // keep the dependency direction memif → ui (not ui → memif),
            // matching Phase A's wire direction (the ui bundle Require-Bundle's
            // memif, not the other way around).
            try {
                Class<?> view = Class.forName(
                        "cn.com.myorg.bswbuilder.ui.views.PropertyFormView");
                view.getMethod("showAndPopulate", MemIfData.class)
                    .invoke(null, data);
            } catch (Throwable ignored) {
                // PropertyFormView not on classpath (toolbar still works,
                // just no form update). Not a hard error.
            }

            MessageDialog.openInformation(shell, "MemIf ARXML loaded", body);
        } catch (Throwable t) {
            t.printStackTrace();
            MessageDialog.openError(shell, "ARXML load failed",
                    t.getClass().getSimpleName() + ": " + t.getMessage());
        }
        return null;
    }

    private static String nullToDash(String s) {
        return (s == null || s.isEmpty()) ? "—" : s;
    }
}

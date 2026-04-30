package cn.com.myorg.bswbuilder.ui.handlers;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.core.resources.IFile;
import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.ui.handlers.HandlerUtil;

/**
 * Stub for "Delete" right-click action on a BSW module .arxml.
 * v0.1 仅提示并指向资源管理器，不实际删文件 (防误操作 + 保留 byte-equal 基准)。
 */
public class DeleteModuleStubHandler extends AbstractHandler {
    @Override
    public Object execute(ExecutionEvent event) throws ExecutionException {
        Shell shell = HandlerUtil.getActiveShellChecked(event);
        IFile arxmlFile = GenerateMemIfHandler.pickIFile(event);
        String path = (arxmlFile != null && arxmlFile.getLocation() != null)
                ? arxmlFile.getLocation().toFile().getAbsolutePath()
                : "(unknown)";
        boolean ok = MessageDialog.openConfirm(shell,
                "Delete",
                "永久删除 " + (arxmlFile != null ? arxmlFile.getName() : "?") + " ?\n\n"
              + "v0.1 仅提示，不实际删除文件。如果确实要删，请用文件管理器手动删:\n"
              + path);
        if (ok) {
            MessageDialog.openInformation(shell, "Delete deferred",
                    "v0.1 不真正删除以防误操作。");
        }
        return null;
    }
}

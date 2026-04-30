package cn.com.myorg.bswbuilder.ui.handlers;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.ui.handlers.HandlerUtil;

/**
 * Stub for "Update Bswmd" right-click action. v0.1 schema 固定，
 * bswmd 骨架在 Generate 时自动重生成；显式 Update Bswmd 留 v0.2 加。
 */
public class UpdateBswmdStubHandler extends AbstractHandler {
    @Override
    public Object execute(ExecutionEvent event) throws ExecutionException {
        MessageDialog.openInformation(
                HandlerUtil.getActiveShellChecked(event),
                "Update Bswmd",
                "Update Bswmd 在 v0.2 加。v0.1 schema 固定，\n"
              + "bswmd 骨架在 Generate 时自动重生成，不需要单独 update。");
        return null;
    }
}

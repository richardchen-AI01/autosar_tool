package cn.com.myorg.bswbuilder.ui.handlers;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.ui.handlers.HandlerUtil;

/**
 * Stub for "Synchronize Module" right-click action — keeps menu shape
 * matching reference V25.10. Real cross-module sync (EcuC/Rte/NvM
 * back-reference) lands in v0.2 when those modules ship.
 */
public class SynchronizeModuleStubHandler extends AbstractHandler {
    @Override
    public Object execute(ExecutionEvent event) throws ExecutionException {
        MessageDialog.openInformation(
                HandlerUtil.getActiveShellChecked(event),
                "Synchronize Module",
                "Sync Module 在 v0.2 加 — 这个动作把模块跟其它配置 "
              + "(EcuC / Rte / NvM) 互相同步引用。v0.1 仅 MemIf 单模块，"
              + "没有跨模块同步可做。");
        return null;
    }
}

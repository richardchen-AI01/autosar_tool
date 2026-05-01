package cn.com.myorg.bswbuilder.ui.handlers;

import java.io.File;
import java.util.Arrays;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.core.runtime.jobs.Job;
import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.ui.console.MessageConsole;
import org.eclipse.ui.handlers.HandlerUtil;

import cn.com.myorg.bswbuilder.ui.Activator;
import cn.com.myorg.bswbuilder.ui.launcher.BswgenLauncher;
import cn.com.myorg.bswbuilder.ui.launcher.ConsoleAccess;

/**
 * Generate handler — IDE pivot phase 2 (2026-04-30):
 * 选中 Project Explorer 里 BSW_Builder/&lt;MCU&gt;/&lt;Module&gt;.arxml 后右键
 * Generate 触发。从选中的 IFile 推断模块名 + workspace 根 + 输出目录，
 * 不再弹 DirectoryDialog。
 *
 * <p>路径推断: workspace = arxml 文件向上 3 级 (BSW_Builder/&lt;MCU&gt;/X.arxml
 * → workspace 是 BSW_Builder 的父目录)；output = workspace/config/；
 * Bswmd 后处理: 把 *_Bswmd.arxml 移到 workspace/bswmds/。
 */
public class GenerateMemIfHandler extends AbstractHandler {

    @Override
    public Object execute(ExecutionEvent event) throws ExecutionException {
        Shell shell = HandlerUtil.getActiveShellChecked(event);

        IFile arxmlFile = pickIFile(event);
        if (arxmlFile == null) {
            MessageDialog.openInformation(shell, "Generate",
                    "请先在 Project Explorer 里右键一个模块 .arxml 文件。");
            return null;
        }

        File arxml = arxmlFile.getLocation() != null
                ? arxmlFile.getLocation().toFile() : null;
        if (arxml == null || !arxml.isFile()) {
            MessageDialog.openError(shell, "Generate",
                    "无法定位 ARXML 文件: " + arxmlFile.getFullPath());
            return null;
        }

        String fileName = arxml.getName();
        if (!fileName.toLowerCase().endsWith(".arxml")) return null;
        final String moduleName = fileName.substring(0, fileName.length() - ".arxml".length());

        // workspace 推断: <ws>/BSW_Builder/<MCU>/<Module>.arxml → <ws>
        File mcuDir = arxml.getParentFile();
        File bswBuilder = mcuDir == null ? null : mcuDir.getParentFile();
        if (bswBuilder == null || !"BSW_Builder".equals(bswBuilder.getName())) {
            MessageDialog.openError(shell, "Generate " + moduleName,
                    "无法从路径推断 workspace —— 期望 <workspace>/BSW_Builder/<MCU>/"
                  + moduleName + ".arxml");
            return null;
        }
        final File workspaceDir = bswBuilder.getParentFile();
        final File configDir = new File(workspaceDir, "config");
        if (!configDir.isDirectory() && !configDir.mkdirs()) {
            MessageDialog.openError(shell, "Generate " + moduleName,
                    "无法创建输出目录: " + configDir.getAbsolutePath());
            return null;
        }
        // bswmds/ 由 Update Bswmd 命令独立管 (跟参考 V25.10 一致), 不在 Generate
        // 路径里创建/写入 — 删 post-move 救场代码。

        if (!"MemIf".equals(moduleName)) {
            MessageDialog.openInformation(shell, "Generate " + moduleName,
                    "v0.1 仅 MemIf 接通生成器，" + moduleName + " 暂搁置。");
            return null;
        }

        final MessageConsole console = ConsoleAccess.getConsole();
        ConsoleAccess.show(console);

        Job job = Job.create("Generate " + moduleName, (IProgressMonitor monitor) -> {
            try {
                int exit = BswgenLauncher.run(
                        BswgenLauncher.Tool.BSWGEN,
                        Arrays.asList("-g", moduleName,
                                      "-i", workspaceDir.getAbsolutePath(),
                                      "-o", configDir.getAbsolutePath()),
                        console, monitor);
                if (exit != 0) {
                    return new Status(IStatus.ERROR, Activator.PLUGIN_ID,
                            "bswgen returned exit code " + exit + " — see BSW Builder console.");
                }
                // Generate 命令现在只产 Cfg.c/.h 到 -o (跟参考 V25.10 一致)。
                // Bswmd 走独立的 Update Bswmd 命令 → bswmds/, 不需要 post-move。
                // 让 Project Explorer 看到新文件
                try {
                    arxmlFile.getProject().refreshLocal(
                            org.eclipse.core.resources.IResource.DEPTH_INFINITE, monitor);
                } catch (Exception ignored) { /* not fatal */ }
                return Status.OK_STATUS;
            } catch (Exception ex) {
                return BswgenLauncher.errorStatus(Activator.PLUGIN_ID,
                        "Generate " + moduleName + " failed", ex);
            }
        });
        job.setUser(true);
        job.schedule();
        return null;
    }

    /**
     * Pull the first {@link IFile} out of the command's selection. Supports
     * three selection types:
     * <ul>
     *   <li>raw IFile (Project Explorer right-click on .arxml)</li>
     *   <li>IAdaptable that adapts to IFile</li>
     *   <li>{@link cn.com.myorg.mal.model.ModuleModel} from AUTOSAR Explorer
     *       (resolved via projectName + pathValue → IFile)</li>
     * </ul>
     */
    static IFile pickIFile(ExecutionEvent event) {
        IStructuredSelection sel =
                HandlerUtil.getCurrentStructuredSelection(event);
        if (sel == null) return null;
        Object first = sel.getFirstElement();
        if (first instanceof IFile) return (IFile) first;
        if (first instanceof cn.com.myorg.mal.model.ModuleModel) {
            cn.com.myorg.mal.model.ModuleModel m =
                    (cn.com.myorg.mal.model.ModuleModel) first;
            return org.eclipse.core.resources.ResourcesPlugin.getWorkspace().getRoot()
                    .getProject(m.getProjectName())
                    .getFile(new org.eclipse.core.runtime.Path(m.getPathValue()));
        }
        if (first instanceof org.eclipse.core.runtime.IAdaptable) {
            return ((org.eclipse.core.runtime.IAdaptable) first).getAdapter(IFile.class);
        }
        return null;
    }
}

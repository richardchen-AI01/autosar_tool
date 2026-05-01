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
import org.eclipse.swt.widgets.Shell;
import org.eclipse.ui.console.MessageConsole;
import org.eclipse.ui.handlers.HandlerUtil;

import cn.com.myorg.bswbuilder.ui.Activator;
import cn.com.myorg.bswbuilder.ui.launcher.BswgenLauncher;
import cn.com.myorg.bswbuilder.ui.launcher.ConsoleAccess;

/**
 * "Update Bswmd" right-click handler — re-generates the {@code <Module>_Bswmd.arxml}
 * descriptor under {@code <project>/bswmds/}.
 *
 * <p>Runs in a separate pipeline from Generate (跟参考 V25.10 一致): the
 * Generate command updates {@code config/<Module>_Cfg.c|.h}, while Update
 * Bswmd refreshes the schema descriptor in {@code bswmds/}. Reference's
 * {@code bswmds/} timestamps (2025/10/21 — project creation time) vs
 * {@code config/} timestamps (latest user-triggered Generate) confirm the
 * two run on independent cadences.
 *
 * <p>Backed by the Python CLI flag {@code --update-bswmd <Module>}, which
 * writes to {@code <project>/bswmds/} regardless of {@code -o}.
 */
public class UpdateBswmdStubHandler extends AbstractHandler {

    @Override
    public Object execute(ExecutionEvent event) throws ExecutionException {
        Shell shell = HandlerUtil.getActiveShellChecked(event);

        IFile arxmlFile = GenerateMemIfHandler.pickIFile(event);
        if (arxmlFile == null) {
            MessageDialog.openInformation(shell, "Update Bswmd",
                    "请先在 Project Explorer 里右键一个模块 .arxml 文件。");
            return null;
        }

        File arxml = arxmlFile.getLocation() != null
                ? arxmlFile.getLocation().toFile() : null;
        if (arxml == null || !arxml.isFile()) {
            MessageDialog.openError(shell, "Update Bswmd",
                    "无法定位 ARXML 文件: " + arxmlFile.getFullPath());
            return null;
        }

        String fileName = arxml.getName();
        if (!fileName.toLowerCase().endsWith(".arxml")) return null;
        final String moduleName = fileName.substring(0, fileName.length() - ".arxml".length());

        // Workspace 推断, same rule as GenerateMemIfHandler:
        // <ws>/BSW_Builder/<MCU>/<Module>.arxml → <ws>
        File mcuDir = arxml.getParentFile();
        File bswBuilder = mcuDir == null ? null : mcuDir.getParentFile();
        if (bswBuilder == null || !"BSW_Builder".equals(bswBuilder.getName())) {
            MessageDialog.openError(shell, "Update Bswmd " + moduleName,
                    "无法从路径推断 workspace —— 期望 <workspace>/BSW_Builder/<MCU>/"
                  + moduleName + ".arxml");
            return null;
        }
        final File workspaceDir = bswBuilder.getParentFile();

        final MessageConsole console = ConsoleAccess.getConsole();
        ConsoleAccess.show(console);

        Job job = Job.create("Update Bswmd " + moduleName, (IProgressMonitor monitor) -> {
            try {
                int exit = BswgenLauncher.run(
                        BswgenLauncher.Tool.BSWGEN,
                        Arrays.asList("--update-bswmd", moduleName,
                                      "-i", workspaceDir.getAbsolutePath()),
                        console, monitor);
                if (exit != 0) {
                    return new Status(IStatus.ERROR, Activator.PLUGIN_ID,
                            "bswgen --update-bswmd returned exit code " + exit
                          + " — see BSW Builder console.");
                }
                try {
                    arxmlFile.getProject().refreshLocal(
                            org.eclipse.core.resources.IResource.DEPTH_INFINITE, monitor);
                } catch (Exception ignored) { /* not fatal */ }
                return Status.OK_STATUS;
            } catch (Exception ex) {
                return BswgenLauncher.errorStatus(Activator.PLUGIN_ID,
                        "Update Bswmd " + moduleName + " failed", ex);
            }
        });
        job.setUser(true);
        job.schedule();
        return null;
    }
}

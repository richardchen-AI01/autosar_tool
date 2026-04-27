package cn.com.myorg.bswbuilder.ui.handlers;

import java.util.List;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.core.runtime.jobs.Job;
import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.swt.widgets.DirectoryDialog;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.ui.console.MessageConsole;
import org.eclipse.ui.handlers.HandlerUtil;

import cn.com.myorg.bswbuilder.ui.Activator;
import cn.com.myorg.bswbuilder.ui.launcher.BswgenLauncher;
import cn.com.myorg.bswbuilder.ui.launcher.ConsoleAccess;

/**
 * Toolbar / menu handler: prompts for a workspace dir + an output dir, then
 * runs <code>bswgen -g MemIf -i &lt;workspace&gt; -o &lt;output&gt;</code> as a
 * background job, streaming output to the BSW Builder console.
 */
public class GenerateMemIfHandler extends AbstractHandler {

    @Override
    public Object execute(ExecutionEvent event) throws ExecutionException {
        Shell shell = HandlerUtil.getActiveShellChecked(event);

        String workspace = pickDir(shell, "Select BSW workspace (the folder containing BSW_Builder/)");
        if (workspace == null) {
            return null;
        }
        String output = pickDir(shell, "Select output directory for generated .c/.h files");
        if (output == null) {
            return null;
        }

        MessageConsole console = ConsoleAccess.getConsole();
        ConsoleAccess.show(console);

        Job job = Job.create("Generate MemIf", (IProgressMonitor monitor) -> {
            try {
                int exit = BswgenLauncher.run(
                        BswgenLauncher.Tool.BSWGEN,
                        List.of("-g", "MemIf", "-i", workspace, "-o", output),
                        console, monitor);
                if (exit != 0) {
                    return new Status(IStatus.ERROR, Activator.PLUGIN_ID,
                            "bswgen returned exit code " + exit + " — see BSW Builder console.");
                }
                return Status.OK_STATUS;
            } catch (Exception ex) {
                return BswgenLauncher.errorStatus(Activator.PLUGIN_ID,
                        "Generate MemIf failed", ex);
            }
        });
        job.setUser(true);
        job.schedule();

        // Quick non-blocking confirmation
        MessageDialog.openInformation(shell, "BSW Builder",
                "Generating MemIf… see the BSW Builder console for output.");
        return null;
    }

    private static String pickDir(Shell shell, String message) {
        DirectoryDialog d = new DirectoryDialog(shell);
        d.setMessage(message);
        d.setText("BSW Builder");
        return d.open();
    }
}

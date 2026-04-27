package cn.com.myorg.bswbuilder.ui.handlers;

import java.util.List;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.core.runtime.jobs.Job;
import org.eclipse.swt.widgets.DirectoryDialog;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.ui.console.MessageConsole;
import org.eclipse.ui.handlers.HandlerUtil;

import cn.com.myorg.bswbuilder.ui.Activator;
import cn.com.myorg.bswbuilder.ui.launcher.BswgenLauncher;
import cn.com.myorg.bswbuilder.ui.launcher.ConsoleAccess;

/**
 * Run <code>bswval -m MemIf -i &lt;workspace&gt;</code> against a chosen
 * workspace, streaming to the shared console. M3.3 will route findings into
 * the Eclipse ProblemView; for v0.1 we just print them.
 */
public class ValidateMemIfHandler extends AbstractHandler {

    @Override
    public Object execute(ExecutionEvent event) throws ExecutionException {
        Shell shell = HandlerUtil.getActiveShellChecked(event);

        DirectoryDialog d = new DirectoryDialog(shell);
        d.setMessage("Select BSW workspace to validate");
        d.setText("BSW Builder");
        String workspace = d.open();
        if (workspace == null) {
            return null;
        }

        MessageConsole console = ConsoleAccess.getConsole();
        ConsoleAccess.show(console);

        Job job = Job.create("Validate MemIf", (IProgressMonitor monitor) -> {
            try {
                int exit = BswgenLauncher.run(
                        BswgenLauncher.Tool.BSWVAL,
                        List.of("-m", "MemIf", "-i", workspace),
                        console, monitor);
                // Validator returns 1 when findings exist — that's not a failure
                // of the *tool*, so we surface it in the console only.
                if (exit < 0) {
                    return new Status(IStatus.ERROR, Activator.PLUGIN_ID,
                            "bswval terminated abnormally (exit " + exit + ").");
                }
                return Status.OK_STATUS;
            } catch (Exception ex) {
                return BswgenLauncher.errorStatus(Activator.PLUGIN_ID,
                        "Validate MemIf failed", ex);
            }
        });
        job.setUser(true);
        job.schedule();
        return null;
    }
}

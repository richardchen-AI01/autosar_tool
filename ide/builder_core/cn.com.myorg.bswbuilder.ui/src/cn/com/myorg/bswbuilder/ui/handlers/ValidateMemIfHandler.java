package cn.com.myorg.bswbuilder.ui.handlers;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.eclipse.core.commands.AbstractHandler;
import org.eclipse.core.commands.ExecutionEvent;
import org.eclipse.core.commands.ExecutionException;
import org.eclipse.core.resources.IMarker;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.resources.IWorkspaceRoot;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.core.runtime.jobs.Job;
import org.eclipse.swt.widgets.DirectoryDialog;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.console.MessageConsole;
import org.eclipse.ui.handlers.HandlerUtil;

import cn.com.myorg.bswbuilder.ui.Activator;
import cn.com.myorg.bswbuilder.ui.launcher.BswgenLauncher;
import cn.com.myorg.bswbuilder.ui.launcher.ConsoleAccess;

/**
 * Run <code>bswval -m MemIf -i &lt;workspace&gt;</code> against a chosen
 * workspace, capture the output, parse each finding, and surface it as an
 * Eclipse {@link IMarker} so the Problems View lights up.
 *
 * <p>Marker source: lines emitted by the Python validator look like
 * <pre>
 *   [4] Rule_BSW_MemIf_TCPP_2170: NvMTargetBlockReference …  @ /MemIf/MemIfGeneral/MemIfNumberOfDevices
 * </pre>
 * The number in brackets is the AUTOSAR severity level (1=critical … 4=info,
 * but for the rules we ship every fired finding is at least a configuration
 * error). We map all findings to {@link IMarker#SEVERITY_ERROR} for v0.1 and
 * stash the original level in attribute {@code memif.severity}.
 *
 * <p>Markers are attached to the {@link IWorkspaceRoot} for v0.1. v0.2 will
 * import the BSW workspace as an Eclipse project so markers can resolve to
 * the actual ARXML file.
 */
public class ValidateMemIfHandler extends AbstractHandler {

    /** Custom marker attribute key — used to identify "our" markers when
     *  clearing on re-run. */
    private static final String SOURCE_ATTR = "cn.com.myorg.bswbuilder.memif";

    /** Match a validator finding line. */
    private static final Pattern FINDING_RE = Pattern.compile(
            "^\\s*\\[(\\d+)\\]\\s+(\\w+):\\s+(.+?)\\s+@\\s+(\\S+)\\s*$");

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
                clearOldMarkers();

                List<String> lines = new ArrayList<>();
                BswgenLauncher.Result res = BswgenLauncher.runAndCapture(
                        BswgenLauncher.Tool.BSWVAL,
                        java.util.Arrays.asList("-m", "MemIf", "-i", workspace),
                        console, monitor, lines);

                int created = createMarkers(lines, workspace);
                if (created > 0) {
                    showProblemsView();
                }

                if (res.exitCode < 0) {
                    return new Status(IStatus.ERROR, Activator.PLUGIN_ID,
                            "bswval terminated abnormally (exit " + res.exitCode + ").");
                }
                if (res.exitCode == 0 && created == 0) {
                    return Status.OK_STATUS;
                }
                // exit 1 + findings → user-actionable; not a tool failure
                return new Status(IStatus.WARNING, Activator.PLUGIN_ID,
                        "MemIf validation found " + created
                                + " issue(s) — see Problems view.");
            } catch (IOException ex) {
                return BswgenLauncher.errorStatus(Activator.PLUGIN_ID,
                        "Validate MemIf failed", ex);
            }
        });
        job.setUser(true);
        job.schedule();
        return null;
    }

    /** Drop any markers we created on a previous run. */
    private static void clearOldMarkers() {
        IWorkspaceRoot root = ResourcesPlugin.getWorkspace().getRoot();
        try {
            IMarker[] all = root.findMarkers(IMarker.PROBLEM, false /* includeSubtypes */, IResource.DEPTH_ZERO);
            for (IMarker m : all) {
                if (Boolean.TRUE.equals(m.getAttribute(SOURCE_ATTR))) {
                    m.delete();
                }
            }
        } catch (CoreException e) {
            // Non-fatal — if we can't clear, new markers just append
            e.printStackTrace();
        }
    }

    /** Parse lines, create one IMarker per matching finding. Returns count. */
    private static int createMarkers(List<String> lines, String workspace) {
        IWorkspaceRoot root = ResourcesPlugin.getWorkspace().getRoot();
        int created = 0;
        for (String line : lines) {
            Matcher m = FINDING_RE.matcher(line);
            if (!m.matches()) continue;
            String level = m.group(1);
            String ruleKey = m.group(2);
            String message = m.group(3);
            String ecucPath = m.group(4);
            try {
                IMarker mk = root.createMarker(IMarker.PROBLEM);
                mk.setAttribute(IMarker.SEVERITY, IMarker.SEVERITY_ERROR);
                mk.setAttribute(IMarker.MESSAGE, ruleKey + ": " + message);
                mk.setAttribute(IMarker.LOCATION, ecucPath);
                mk.setAttribute("memif.ruleKey", ruleKey);
                mk.setAttribute("memif.severity", level);
                mk.setAttribute("memif.workspace", workspace);
                mk.setAttribute(SOURCE_ATTR, true);
                created++;
            } catch (CoreException e) {
                e.printStackTrace();
            }
        }
        return created;
    }

    private static void showProblemsView() {
        Display display = PlatformUI.getWorkbench().getDisplay();
        display.asyncExec(() -> {
            try {
                PlatformUI.getWorkbench().getActiveWorkbenchWindow().getActivePage()
                        .showView("org.eclipse.ui.views.ProblemView");
            } catch (Throwable t) {
                // Problems View ID has historically varied; fall back silently
            }
        });
    }
}

package cn.com.myorg.bswbuilder.ui.wizards;

import java.io.File;
import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.List;

import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.IProjectDescription;
import org.eclipse.core.resources.IWorkspace;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.Path;
import org.eclipse.core.runtime.SubMonitor;
import org.eclipse.jface.operation.IRunnableWithProgress;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.jface.wizard.Wizard;
import org.eclipse.jface.wizard.WizardPage;
import org.eclipse.swt.SWT;
import org.eclipse.swt.events.SelectionAdapter;
import org.eclipse.swt.events.SelectionEvent;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.DirectoryDialog;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Text;
import org.eclipse.ui.IImportWizard;
import org.eclipse.ui.IWorkbench;
import org.eclipse.ui.IWorkbenchWindow;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.WorkbenchException;

/**
 * "Existing BSW Project into Workspace" import wizard.
 *
 * <p>Walks a chosen directory recursively for {@code .project} files and
 * imports each as an Eclipse project. On finish, also switches to the
 * BSW Configurator perspective so AUTOSAR Explorer is front-and-center.
 *
 * <p>Implemented with public Eclipse API only (IProjectDescription /
 * IProject.create) — avoids the internal {@code WizardProjectsImportPage}.
 *
 * <p>Reference: V25.10 has an empty {@code cn.com.isoft.importWizards}
 * placeholder category in {@code File → Import}; we populate ours with this
 * concrete wizard so the category actually shows up (Eclipse hides
 * import-wizard categories that have zero wizards).
 */
public class BswProjectImportWizard extends Wizard implements IImportWizard {

    private static final String BSW_PERSPECTIVE_ID =
            "cn.com.myorg.bswbuilder.common.perspective";

    private DirectoryPickPage page;

    @Override
    public void init(IWorkbench workbench, IStructuredSelection selection) {
        setWindowTitle("Import BSW Project");
        setNeedsProgressMonitor(true);
    }

    @Override
    public void addPages() {
        page = new DirectoryPickPage();
        addPage(page);
    }

    @Override
    public boolean performFinish() {
        final String dir = page.getDirectory();
        if (dir == null || dir.isEmpty()) return false;

        final List<File> projectFiles = collectProjectFiles(new File(dir));
        if (projectFiles.isEmpty()) {
            page.setErrorMessage("No .project files found under " + dir);
            return false;
        }

        try {
            getContainer().run(true, false, new IRunnableWithProgress() {
                @Override
                public void run(IProgressMonitor monitor)
                        throws InvocationTargetException, InterruptedException {
                    SubMonitor sub = SubMonitor.convert(monitor,
                            "Importing projects", projectFiles.size());
                    IWorkspace ws = ResourcesPlugin.getWorkspace();
                    for (File pf : projectFiles) {
                        try {
                            IProjectDescription desc = ws.loadProjectDescription(
                                    new Path(pf.getAbsolutePath()));
                            IProject project = ws.getRoot().getProject(desc.getName());
                            if (!project.exists()) {
                                project.create(desc, sub.split(1));
                            } else {
                                sub.worked(1);
                            }
                            if (!project.isOpen()) {
                                project.open(sub.split(0));
                            }
                        } catch (CoreException ce) {
                            throw new InvocationTargetException(ce);
                        }
                    }
                }
            });
        } catch (InvocationTargetException | InterruptedException e) {
            page.setErrorMessage("Import failed: " + e.getMessage());
            return false;
        }

        switchToBswPerspective();
        return true;
    }

    /** Recursively walk {@code root} and collect every {@code .project} file. */
    private static List<File> collectProjectFiles(File root) {
        List<File> out = new ArrayList<>();
        if (root == null || !root.isDirectory()) return out;
        File dotProject = new File(root, ".project");
        if (dotProject.isFile()) {
            out.add(dotProject);
            return out; // do NOT descend into a project root
        }
        File[] children = root.listFiles();
        if (children != null) {
            for (File c : children) {
                if (c.isDirectory()) out.addAll(collectProjectFiles(c));
            }
        }
        return out;
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

    /** Single-page directory picker. */
    private static final class DirectoryPickPage extends WizardPage {
        private Text dirText;

        protected DirectoryPickPage() {
            super("BswProjectImportPage");
            setTitle("Import BSW Project");
            setDescription("Choose a directory containing one or more BSW projects "
                    + "(e.g. D:\\bswbuilderN\\workspace).");
        }

        String getDirectory() { return dirText == null ? null : dirText.getText().trim(); }

        @Override
        public void createControl(Composite parent) {
            Composite root = new Composite(parent, SWT.NONE);
            GridLayout gl = new GridLayout(3, false);
            root.setLayout(gl);

            new Label(root, SWT.NONE).setText("Root directory:");
            dirText = new Text(root, SWT.BORDER);
            dirText.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, true, false));
            dirText.addModifyListener(e -> validate());

            Button browse = new Button(root, SWT.PUSH);
            browse.setText("Browse...");
            browse.addSelectionListener(new SelectionAdapter() {
                @Override
                public void widgetSelected(SelectionEvent e) {
                    DirectoryDialog dd = new DirectoryDialog(getShell());
                    dd.setMessage("Select root directory");
                    String picked = dd.open();
                    if (picked != null) {
                        dirText.setText(picked);
                    }
                }
            });

            setControl(root);
            setPageComplete(false);
        }

        private void validate() {
            String d = dirText.getText().trim();
            if (d.isEmpty()) {
                setErrorMessage(null);
                setPageComplete(false);
                return;
            }
            File f = new File(d);
            if (!f.isDirectory()) {
                setErrorMessage("Not a directory: " + d);
                setPageComplete(false);
                return;
            }
            setErrorMessage(null);
            setPageComplete(true);
        }
    }

}

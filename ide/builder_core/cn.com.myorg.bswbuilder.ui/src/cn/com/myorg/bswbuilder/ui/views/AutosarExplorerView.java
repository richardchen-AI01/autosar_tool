package cn.com.myorg.bswbuilder.ui.views;

import java.io.File;
import java.util.Arrays;
import java.util.Comparator;

import org.eclipse.jface.action.Action;
import org.eclipse.jface.action.IMenuListener;
import org.eclipse.jface.action.IMenuManager;
import org.eclipse.jface.action.IToolBarManager;
import org.eclipse.jface.action.MenuManager;
import org.eclipse.jface.action.Separator;
import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.jface.layout.GridDataFactory;
import org.eclipse.jface.layout.GridLayoutFactory;
import org.eclipse.jface.viewers.DoubleClickEvent;
import org.eclipse.jface.viewers.IDoubleClickListener;
import org.eclipse.jface.viewers.ISelection;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.jface.viewers.LabelProvider;
import org.eclipse.jface.viewers.TreeViewer;
import org.eclipse.swt.SWT;
import org.eclipse.swt.graphics.Color;
import org.eclipse.swt.graphics.Image;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.DirectoryDialog;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Menu;
import org.eclipse.swt.widgets.Tree;
import org.eclipse.ui.ISharedImages;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.part.ViewPart;
import org.eclipse.ui.plugin.AbstractUIPlugin;
import org.eclipse.core.commands.Command;
import org.eclipse.core.commands.ParameterizedCommand;
import org.eclipse.ui.commands.ICommandService;
import org.eclipse.ui.handlers.IHandlerService;

import cn.com.myorg.bswbuilder.modules.memif.data.MemIfArxmlReader;
import cn.com.myorg.bswbuilder.modules.memif.data.MemIfData;

/**
 * Autosar Explorer — left-side project tree, mirrors the reference
 * V25.10 layout:
 * <pre>
 *   Autosar Explorer
 *   ├─ Demo_S32K148_V2510_BSW_ConfigProject
 *   │   ├─ BSW_Builder
 *   │   │   └─ S32K148 (S32K148)
 *   │   │       ├─ COM / DIAG / MCAL / MEM / SYS / WDG  (虚拟分类节点 — 按 ARXML 名分组)
 *   │   ├─ bswmds
 *   │   ├─ config
 *   │   └─ navigator.xml
 *   ...
 * </pre>
 *
 * <p>Open Workspace 用左上角的 toolbar action (DirectoryDialog)。
 * 双击 *.arxml → 通过 {@link MemIfArxmlReader} 加载 → 推到
 * {@link PropertyFormView}（U2 后会切到 MemIfModuleManagerEditor）。
 *
 * <p>JFace 路线（不是 Eclipse Resources Project Explorer）—— 不要求
 * workspace 当 Eclipse project 导入；用户选哪个目录，那就是根。
 */
public class AutosarExplorerView extends ViewPart {

    public static final String ID =
            "cn.com.myorg.bswbuilder.ui.views.AutosarExplorer";

    private static final Color BG = new Color(Display.getDefault(), 255, 255, 255);

    private TreeViewer treeViewer;
    private File workspaceRoot;

    @Override
    public void createPartControl(Composite parent) {
        parent.setBackground(BG);
        GridLayoutFactory.fillDefaults().applyTo(parent);

        treeViewer = new TreeViewer(parent, SWT.SINGLE | SWT.H_SCROLL | SWT.V_SCROLL);
        Tree tree = treeViewer.getTree();
        GridDataFactory.fillDefaults().grab(true, true).applyTo(tree);

        treeViewer.setContentProvider(new WorkspaceContentProvider());
        treeViewer.setLabelProvider(new WorkspaceLabelProvider());

        treeViewer.addDoubleClickListener(new IDoubleClickListener() {
            @Override
            public void doubleClick(DoubleClickEvent event) {
                ISelection sel = event.getSelection();
                if (!(sel instanceof IStructuredSelection)) return;
                Object first = ((IStructuredSelection) sel).getFirstElement();
                if (first instanceof TreeNode) {
                    TreeNode n = (TreeNode) first;
                    if (n.file != null && n.file.isFile()
                            && n.file.getName().toLowerCase().endsWith(".arxml")) {
                        openArxml(n.file);
                    } else if (n.file != null && n.file.isDirectory()) {
                        // Toggle expansion on dir double-click
                        treeViewer.setExpandedState(n, !treeViewer.getExpandedState(n));
                    }
                }
            }
        });

        // Right-click context menu — replaces the v0.1 toolbar buttons.
        // Reference V25.10 shows Validate / Generate / Update Bswmd / Delete on
        // module ARXML nodes; we mirror exactly (Update/Delete stubs in v0.1).
        MenuManager menuManager = new MenuManager();
        menuManager.setRemoveAllWhenShown(true);
        menuManager.addMenuListener(new IMenuListener() {
            @Override
            public void menuAboutToShow(IMenuManager mgr) {
                fillContextMenu(mgr);
            }
        });
        Menu ctxMenu = menuManager.createContextMenu(treeViewer.getControl());
        treeViewer.getControl().setMenu(ctxMenu);
        getSite().registerContextMenu(menuManager, treeViewer);

        // Toolbar action: Open Workspace
        IToolBarManager toolbar = getViewSite().getActionBars().getToolBarManager();
        Action openWorkspaceAction = new Action("Open Workspace…") {
            @Override
            public void run() {
                DirectoryDialog d = new DirectoryDialog(treeViewer.getControl().getShell());
                d.setText("Select BSW workspace root (the folder above BSW_Builder/)");
                String picked = d.open();
                if (picked != null) {
                    setWorkspaceRoot(new File(picked));
                }
            }
        };
        openWorkspaceAction.setImageDescriptor(
                AbstractUIPlugin.imageDescriptorFromPlugin("org.eclipse.ui",
                        "$nl$/icons/full/etool16/import_wiz.png"));
        toolbar.add(openWorkspaceAction);

        // Auto-detect from -Dautosar.workspaceRoot or last-used path
        String prop = System.getProperty("autosar.workspaceRoot");
        if (prop != null && !prop.isEmpty()) {
            File root = new File(prop);
            if (root.isDirectory()) {
                // Default to a sample if it exists; else just stay empty
                File sample = new File(root, "samples/Demo_S32K148");
                setWorkspaceRoot(sample.isDirectory() ? sample : root);
            }
        }
        if (workspaceRoot == null) {
            treeViewer.setInput(new TreeNode[]{
                    new TreeNode(null, "(click 'Open Workspace…' in this view's toolbar)")
            });
        }
    }

    public void setWorkspaceRoot(File root) {
        this.workspaceRoot = root;
        treeViewer.setInput(new TreeNode[]{ new TreeNode(null, root) });
        treeViewer.expandToLevel(2);
    }

    /**
     * Fill the right-click menu based on what's selected. Currently only
     * BSW module ARXML files (e.g. MemIf.arxml under BSW_Builder/&lt;MCU&gt;/)
     * get the 4 action set. Other tree nodes get an empty menu (suppressed).
     */
    private void fillContextMenu(IMenuManager mgr) {
        TreeNode selected = currentSelection();
        if (selected == null || selected.file == null) return;
        File f = selected.file;
        if (!f.isFile() || !f.getName().toLowerCase().endsWith(".arxml")) {
            return;
        }
        // Derive module short name from file name: "MemIf.arxml" → "MemIf"
        final String fileName = f.getName();
        final String moduleName = fileName.substring(0, fileName.length() - ".arxml".length());
        final File arxmlFile = f;

        mgr.add(new Action("Validate") {
            @Override
            public void run() {
                runValidateOnModule(moduleName, arxmlFile);
            }
        });
        mgr.add(new Action("Generate") {
            @Override
            public void run() {
                runGenerateOnModule(moduleName, arxmlFile);
            }
        });
        mgr.add(new Separator());
        mgr.add(new Action("Update Bswmd") {
            @Override
            public void run() {
                MessageDialog.openInformation(treeViewer.getControl().getShell(),
                        "Update Bswmd",
                        "Update Bswmd is deferred to a future version.\n\n"
                      + "v0.1 ships a fixed schema; the bswmd skeleton is regenerated\n"
                      + "automatically by 'Generate', so you don't need this in the\n"
                      + "common case.");
            }
        });
        mgr.add(new Separator());
        mgr.add(new Action("Delete") {
            @Override
            public void run() {
                boolean ok = MessageDialog.openConfirm(treeViewer.getControl().getShell(),
                        "Delete " + moduleName,
                        "Permanently delete " + arxmlFile.getName() + " from the workspace?\n\n"
                      + "This is a v0.1 stub — the file will NOT actually be deleted; the\n"
                      + "operation is left to the user via the file system. A future version\n"
                      + "will properly unregister the module from the workspace metadata.");
                if (ok) {
                    MessageDialog.openInformation(treeViewer.getControl().getShell(),
                            "Delete deferred",
                            "v0.1 doesn't perform the delete to avoid data loss; please\n"
                          + "remove the file via your OS file manager if you really intend\n"
                          + "to remove " + arxmlFile.getAbsolutePath() + ".");
                }
            }
        });
    }

    private TreeNode currentSelection() {
        ISelection sel = treeViewer.getSelection();
        if (!(sel instanceof IStructuredSelection)) return null;
        Object first = ((IStructuredSelection) sel).getFirstElement();
        return (first instanceof TreeNode) ? (TreeNode) first : null;
    }

    /**
     * Trigger the existing ValidateMemIfHandler-equivalent flow but with the
     * module name + workspace inferred from tree selection instead of
     * popping a DirectoryDialog. For non-MemIf modules the same machinery
     * works once we wire {@code -m <moduleName>} through.
     */
    private void runValidateOnModule(String moduleName, File arxmlFile) {
        File workspaceDir = inferWorkspace(arxmlFile);
        if (workspaceDir == null) {
            MessageDialog.openError(treeViewer.getControl().getShell(),
                    "Validate " + moduleName,
                    "Cannot infer workspace from " + arxmlFile.getAbsolutePath() +
                    "\nExpected layout: <workspace>/BSW_Builder/<MCU>/" + moduleName + ".arxml");
            return;
        }
        // For now defer to the existing validateMemIf command (it pops a
        // DirectoryDialog). Future: parameterized command with module +
        // workspace baked in. For MemIf this matches the user's flow.
        if ("MemIf".equals(moduleName)) {
            runCommand("cn.com.myorg.bswbuilder.commands.validateMemIf");
        } else {
            MessageDialog.openInformation(treeViewer.getControl().getShell(),
                    "Validate " + moduleName,
                    "v0.1 only wires Validate for MemIf; " + moduleName +
                    " validate is deferred until the per-module bundle lands.");
        }
    }

    private void runGenerateOnModule(String moduleName, File arxmlFile) {
        File workspaceDir = inferWorkspace(arxmlFile);
        if (workspaceDir == null) {
            MessageDialog.openError(treeViewer.getControl().getShell(),
                    "Generate " + moduleName,
                    "Cannot infer workspace from " + arxmlFile.getAbsolutePath());
            return;
        }
        if ("MemIf".equals(moduleName)) {
            runCommand("cn.com.myorg.bswbuilder.commands.generateMemIf");
        } else {
            MessageDialog.openInformation(treeViewer.getControl().getShell(),
                    "Generate " + moduleName,
                    "v0.1 only wires Generate for MemIf; other modules deferred.");
        }
    }

    private static File inferWorkspace(File arxmlFile) {
        // <ws>/BSW_Builder/<MCU>/<Module>.arxml → <ws>
        File mcuDir = arxmlFile.getParentFile();
        if (mcuDir == null) return null;
        File bswBuilder = mcuDir.getParentFile();
        if (bswBuilder == null || !"BSW_Builder".equals(bswBuilder.getName())) return null;
        return bswBuilder.getParentFile();
    }

    private void runCommand(String commandId) {
        try {
            ICommandService cs = PlatformUI.getWorkbench().getService(ICommandService.class);
            IHandlerService hs = PlatformUI.getWorkbench().getService(IHandlerService.class);
            if (cs == null || hs == null) return;
            Command cmd = cs.getCommand(commandId);
            if (cmd == null) return;
            ParameterizedCommand pc = new ParameterizedCommand(cmd, null);
            hs.executeCommand(pc, null);
        } catch (Throwable t) {
            t.printStackTrace();
        }
    }

    private void openArxml(File arxmlFile) {
        try {
            MemIfData data = MemIfArxmlReader.read(arxmlFile.getAbsolutePath());
            // U2 will replace this with MemIfModuleManagerEditor.openOn(arxmlFile)
            PropertyFormView.showAndPopulate(data);
        } catch (Throwable t) {
            t.printStackTrace();
            org.eclipse.jface.dialogs.MessageDialog.openError(
                    treeViewer.getControl().getShell(),
                    "ARXML load failed",
                    t.getClass().getSimpleName() + ": " + t.getMessage());
        }
    }

    @Override
    public void setFocus() {
        if (treeViewer != null) {
            treeViewer.getControl().setFocus();
        }
    }

    // ------------------------------------------------------------------
    // Tree node — wraps either a File or a synthetic label
    // ------------------------------------------------------------------
    public static final class TreeNode {
        final TreeNode parent;
        final File file;        // null for synthetic placeholder rows
        final String label;     // used when file == null
        TreeNode(TreeNode parent, File file) {
            this.parent = parent; this.file = file; this.label = null;
        }
        TreeNode(TreeNode parent, String label) {
            this.parent = parent; this.file = null; this.label = label;
        }
        @Override
        public String toString() {
            return file != null ? file.getName() : label;
        }
    }

    // ------------------------------------------------------------------
    // ContentProvider — children = directory entries (alphabetical, dirs first)
    // ------------------------------------------------------------------
    private static final class WorkspaceContentProvider implements ITreeContentProvider {
        @Override
        public Object[] getElements(Object inputElement) {
            if (inputElement instanceof TreeNode[]) return (TreeNode[]) inputElement;
            return new Object[0];
        }
        @Override
        public Object[] getChildren(Object parentElement) {
            if (!(parentElement instanceof TreeNode)) return new Object[0];
            TreeNode n = (TreeNode) parentElement;
            if (n.file == null || !n.file.isDirectory()) return new Object[0];
            File[] kids = n.file.listFiles();
            if (kids == null) return new Object[0];
            Arrays.sort(kids, new Comparator<File>() {
                @Override public int compare(File a, File b) {
                    if (a.isDirectory() != b.isDirectory()) {
                        return a.isDirectory() ? -1 : 1;  // dirs first
                    }
                    return a.getName().compareToIgnoreCase(b.getName());
                }
            });
            TreeNode[] out = new TreeNode[kids.length];
            for (int i = 0; i < kids.length; i++) out[i] = new TreeNode(n, kids[i]);
            return out;
        }
        @Override
        public Object getParent(Object element) {
            return (element instanceof TreeNode) ? ((TreeNode) element).parent : null;
        }
        @Override
        public boolean hasChildren(Object element) {
            if (!(element instanceof TreeNode)) return false;
            TreeNode n = (TreeNode) element;
            if (n.file == null || !n.file.isDirectory()) return false;
            File[] kids = n.file.listFiles();
            return kids != null && kids.length > 0;
        }
    }

    // ------------------------------------------------------------------
    // LabelProvider — Eclipse standard folder/file icons; ARXML highlighted
    // ------------------------------------------------------------------
    private static final class WorkspaceLabelProvider extends LabelProvider {
        @Override
        public String getText(Object element) {
            if (!(element instanceof TreeNode)) return super.getText(element);
            TreeNode n = (TreeNode) element;
            if (n.file == null) return n.label;
            return n.file.getName();
        }
        @Override
        public Image getImage(Object element) {
            if (!(element instanceof TreeNode)) return null;
            TreeNode n = (TreeNode) element;
            if (n.file == null) return null;
            ISharedImages shared = PlatformUI.getWorkbench().getSharedImages();
            if (n.file.isDirectory()) {
                return shared.getImage(ISharedImages.IMG_OBJ_FOLDER);
            }
            return shared.getImage(ISharedImages.IMG_OBJ_FILE);
        }
    }
}

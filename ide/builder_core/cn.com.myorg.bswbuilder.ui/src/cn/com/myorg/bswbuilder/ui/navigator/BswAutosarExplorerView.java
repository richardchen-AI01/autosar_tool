package cn.com.myorg.bswbuilder.ui.navigator;

import org.eclipse.jface.viewers.DoubleClickEvent;
import org.eclipse.jface.viewers.IDoubleClickListener;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.sphinx.emf.explorer.ExtendedCommonNavigator;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.ui.IFileEditorInput;
import org.eclipse.ui.PartInitException;
import org.eclipse.ui.PlatformUI;

import cn.com.myorg.mal.model.ModuleModel;

/**
 * AUTOSAR Explorer view — custom {@link ExtendedCommonNavigator} subclass.
 *
 * <p>Reference: {@code cn.com.isoft.pal.ui.explorer.AutosarNavigator}, which
 * also extends Sphinx {@link ExtendedCommonNavigator} (one level above
 * Eclipse {@code CommonNavigator}). Sphinx adds:
 * <ul>
 *   <li>SaveablesProvider integration with EMF EditingDomain dirty state</li>
 *   <li>TreeViewer state persistence via IMemento</li>
 *   <li>partListener that responds to active-editor changes</li>
 * </ul>
 *
 * <p>For E3-B-5 we keep the double-click handler we added in E3-A. Reference
 * also overrides {@code restoreState/saveState/createModelSaveablesProvider}
 * — those are deferred (no current need; tree state persistence is a v0.3
 * polish).
 */
public class BswAutosarExplorerView extends ExtendedCommonNavigator {

    public static final String VIEW_ID = "cn.com.myorg.bswbuilder.ui.bswExplorer";

    @Override
    public void createPartControl(Composite parent) {
        super.createPartControl(parent);
        getCommonViewer().addDoubleClickListener(new IDoubleClickListener() {
            @Override
            public void doubleClick(DoubleClickEvent event) {
                Object sel = ((IStructuredSelection) event.getSelection()).getFirstElement();
                if (sel instanceof ModuleModel) {
                    openModule((ModuleModel) sel);
                }
            }
        });
    }

    private void openModule(ModuleModel m) {
        try {
            PlatformUI.getWorkbench().getActiveWorkbenchWindow().getActivePage()
                    .openEditor(toEditorInput(m), pickEditorId(m), true);
        } catch (PartInitException e) {
            // surface in error log via standard workbench infrastructure
            throw new IllegalStateException(
                    "Failed to open module " + m.getKeyValue(), e);
        }
    }

    /**
     * EMF mal.model.ModuleModel doesn't have a getFile() EOperation (per
     * reference model.ecore). Compose IFile from projectName + pathValue,
     * mirroring EcuConfigurationModelImpl.getFile() pattern.
     */
    private static org.eclipse.core.resources.IFile resolveIFile(ModuleModel m) {
        return org.eclipse.core.resources.ResourcesPlugin.getWorkspace().getRoot()
                .getProject(m.getProjectName())
                .getFile(new org.eclipse.core.runtime.Path(m.getPathValue()));
    }

    private static IFileEditorInput toEditorInput(ModuleModel m) {
        return new org.eclipse.ui.part.FileEditorInput(resolveIFile(m));
    }

    /** Look up editor by .arxml filename via workbench editor registry. */
    private static String pickEditorId(ModuleModel m) {
        return PlatformUI.getWorkbench().getEditorRegistry()
                .getDefaultEditor(resolveIFile(m).getName()).getId();
    }
}

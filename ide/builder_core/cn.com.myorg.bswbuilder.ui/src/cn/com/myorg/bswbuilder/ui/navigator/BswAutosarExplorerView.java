package cn.com.myorg.bswbuilder.ui.navigator;

import org.eclipse.jface.viewers.DoubleClickEvent;
import org.eclipse.jface.viewers.IDoubleClickListener;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.ui.IFileEditorInput;
import org.eclipse.ui.PartInitException;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.navigator.CommonNavigator;

import cn.com.myorg.bswbuilder.ui.navigator.model.ModuleModel;

/**
 * AUTOSAR Explorer view — custom {@link CommonNavigator} subclass that
 * binds our mal model navigatorContent and adds double-click semantics
 * (open the matching BSW module FormEditor when a {@link ModuleModel} leaf
 * is activated).
 *
 * <p>Reference: {@code cn.com.isoft.pal.ui.explorer.AutosarNavigator}.
 *
 * <p>Editor IDs are looked up dynamically via the workbench's editor
 * registry (using the file content type / extension), so this view does
 * not hard-code a per-module editor class — same pattern as the reference,
 * which dispatches to whichever module-specific FormEditor is registered.
 */
public class BswAutosarExplorerView extends CommonNavigator {

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

    private static IFileEditorInput toEditorInput(ModuleModel m) {
        return new org.eclipse.ui.part.FileEditorInput(m.getFile());
    }

    /** Look up editor by .arxml filename via workbench editor registry. */
    private static String pickEditorId(ModuleModel m) {
        return PlatformUI.getWorkbench().getEditorRegistry()
                .getDefaultEditor(m.getFile().getName()).getId();
    }
}

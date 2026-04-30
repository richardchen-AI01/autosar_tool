package cn.com.myorg.bswbuilder.ui.navigator;

import org.eclipse.jface.viewers.LabelProvider;
import org.eclipse.swt.graphics.Image;
import org.eclipse.ui.IMemento;
import org.eclipse.ui.ISharedImages;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.navigator.ICommonContentExtensionSite;
import org.eclipse.ui.navigator.ICommonLabelProvider;

import cn.com.myorg.mal.model.BswBuilderModel;
import cn.com.myorg.mal.model.EcuConfigurationModel;
import cn.com.myorg.mal.model.ModuleKindModel;
import cn.com.myorg.mal.model.ModuleModel;

/**
 * Label provider for the AUTOSAR Explorer view's mal model nodes.
 * Paired with {@link BswExplorerContentProvider}; one entry per POJO type.
 */
public class BswExplorerLabelProvider extends LabelProvider implements ICommonLabelProvider {

    @Override public void init(ICommonContentExtensionSite cfg) { /* no-op */ }
    @Override public void restoreState(IMemento memento) { /* no-op */ }
    @Override public void saveState(IMemento memento) { /* no-op */ }
    @Override public String getDescription(Object element) { return null; }

    @Override
    public String getText(Object element) {
        if (element instanceof BswBuilderModel) {
            return ((BswBuilderModel) element).getName();
        }
        if (element instanceof EcuConfigurationModel) {
            return ((EcuConfigurationModel) element).getFileName();
        }
        if (element instanceof ModuleKindModel) {
            return ((ModuleKindModel) element).getKindName();
        }
        if (element instanceof ModuleModel) {
            return ((ModuleModel) element).getModuleName();
        }
        return null; // let downstream providers (Project Explorer default) handle IProject etc.
    }

    @Override
    public Image getImage(Object element) {
        ISharedImages shared = PlatformUI.getWorkbench().getSharedImages();
        if (element instanceof BswBuilderModel) {
            return shared.getImage(ISharedImages.IMG_OBJ_PROJECT);
        }
        if (element instanceof EcuConfigurationModel || element instanceof ModuleKindModel) {
            return shared.getImage(ISharedImages.IMG_OBJ_FOLDER);
        }
        if (element instanceof ModuleModel) {
            return shared.getImage(ISharedImages.IMG_OBJ_ELEMENT);
        }
        return null;
    }
}

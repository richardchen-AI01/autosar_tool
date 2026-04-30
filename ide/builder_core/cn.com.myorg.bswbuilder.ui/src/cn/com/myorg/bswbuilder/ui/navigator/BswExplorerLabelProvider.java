package cn.com.myorg.bswbuilder.ui.navigator;

import org.eclipse.core.resources.IFile;
import org.eclipse.jface.viewers.LabelProvider;
import org.eclipse.swt.graphics.Image;
import org.eclipse.ui.IMemento;
import org.eclipse.ui.ISharedImages;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.navigator.ICommonContentExtensionSite;
import org.eclipse.ui.navigator.ICommonLabelProvider;

/**
 * Label provider for the BSW navigatorContent extension.
 *
 * <ul>
 *   <li>{@link KindGroupNode} → kind label ("MEM" / "COM" / …) + folder icon</li>
 *   <li>BSW module {@code IFile} (under BSW_Builder/&lt;MCU&gt;/) →
 *       file name with ".arxml" stripped, IDE element/puzzle icon</li>
 *   <li>Other elements → {@code null} (let other label providers handle)</li>
 * </ul>
 *
 * <p>Reference V25.10's {@code BswExplorerLabelProvider} extends
 * {@code StyledCellLabelProvider} and renders module nodes with a
 * styled "(MCU)" suffix and font tweaks. v0.1 keeps a plain text label;
 * styling polish is a v0.2 follow-up (matches the deferred font/color
 * polish task).
 */
public class BswExplorerLabelProvider extends LabelProvider implements ICommonLabelProvider {

    @Override public void init(ICommonContentExtensionSite cfg) { /* no-op */ }
    @Override public void restoreState(IMemento memento) { /* no-op */ }
    @Override public void saveState(IMemento memento) { /* no-op */ }
    @Override public String getDescription(Object element) { return null; }

    @Override
    public String getText(Object element) {
        if (element instanceof KindGroupNode) {
            return ((KindGroupNode) element).getKind();
        }
        if (element instanceof IFile) {
            IFile f = (IFile) element;
            if (BswExplorerContentProvider.isModuleConfigArxml(f)) {
                return ModuleKindRegistry.stripArxml(f.getName());
            }
        }
        return null; // let downstream providers label it
    }

    @Override
    public Image getImage(Object element) {
        ISharedImages shared = PlatformUI.getWorkbench().getSharedImages();
        if (element instanceof KindGroupNode) {
            return shared.getImage(ISharedImages.IMG_OBJ_FOLDER);
        }
        if (element instanceof IFile) {
            IFile f = (IFile) element;
            if (BswExplorerContentProvider.isModuleConfigArxml(f)) {
                return shared.getImage(ISharedImages.IMG_OBJ_ELEMENT);
            }
        }
        return null;
    }
}

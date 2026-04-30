package cn.com.myorg.bswbuilder.ui.navigator;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IFolder;
import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.runtime.IPath;
import org.eclipse.jface.viewers.LabelProvider;
import org.eclipse.swt.graphics.Image;
import org.eclipse.ui.IMemento;
import org.eclipse.ui.ISharedImages;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.navigator.ICommonContentExtensionSite;
import org.eclipse.ui.navigator.ICommonLabelProvider;

/**
 * AUTOSAR Explorer label provider — file-system aware.
 *
 * <p>Mirrors Project Explorer's default rendering for most resources, with
 * domain-specific polish only for module-level .arxml under
 * {@code BSW_Builder/<MCU>/}: stripped suffix + module icon. Files under
 * {@code bswmds/} keep their full filename ({@code Det_Bswmd.arxml}) since
 * they are description files, not user-edited modules.
 */
public class BswExplorerLabelProvider extends LabelProvider implements ICommonLabelProvider {

    @Override public void init(ICommonContentExtensionSite cfg) { /* no-op */ }
    @Override public void restoreState(IMemento memento) { /* no-op */ }
    @Override public void saveState(IMemento memento) { /* no-op */ }
    @Override public String getDescription(Object element) { return null; }

    @Override
    public String getText(Object element) {
        if (element instanceof IFile) {
            IFile file = (IFile) element;
            if (isModuleArxml(file)) {
                String name = file.getName();
                return name.substring(0, name.length() - ".arxml".length());
            }
            return file.getName();
        }
        if (element instanceof IResource) {
            return ((IResource) element).getName();
        }
        return null;
    }

    @Override
    public Image getImage(Object element) {
        ISharedImages shared = PlatformUI.getWorkbench().getSharedImages();
        if (element instanceof IFile) {
            IFile file = (IFile) element;
            if (isModuleArxml(file)) {
                return shared.getImage(ISharedImages.IMG_OBJ_ELEMENT);
            }
            return shared.getImage(ISharedImages.IMG_OBJ_FILE);
        }
        if (element instanceof IFolder) {
            return shared.getImage(ISharedImages.IMG_OBJ_FOLDER);
        }
        if (element instanceof IProject) {
            return shared.getImage(ISharedImages.IMG_OBJ_PROJECT);
        }
        return null;
    }

    /**
     * True iff this is a module-level .arxml under BSW_Builder/&lt;MCU&gt;/.
     * bswmds/ description files keep .arxml suffix; ServiceComponents/ etc.
     * also keep full name.
     */
    private static boolean isModuleArxml(IFile file) {
        if (!"arxml".equals(file.getFileExtension())) return false;
        IPath path = file.getProjectRelativePath();
        // Need at least BSW_Builder/<MCU>/<Module>.arxml = 3 segments
        if (path.segmentCount() < 3) return false;
        return "BSW_Builder".equals(path.segment(0));
    }
}

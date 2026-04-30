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
 * domain-specific polish for module-level .arxml files:
 * <ul>
 *   <li>{@code BSW_Builder/<MCU>/<Module>.arxml} → label "<Module>" + module icon</li>
 *   <li>{@code bswmds/<Module>_Bswmd.arxml}      → label "<Module>_Bswmd" + module icon</li>
 * </ul>
 * Other resources fall through to the standard Eclipse shared images.
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
     * True iff this is a module-level .arxml under BSW_Builder/&lt;MCU&gt;/
     * or under bswmds/. Other .arxml (deep nested EMF resources, ServiceComponents/
     * etc.) keep their full filename.
     */
    private static boolean isModuleArxml(IFile file) {
        if (!"arxml".equals(file.getFileExtension())) return false;
        IPath path = file.getProjectRelativePath();
        if (path.segmentCount() < 2) return false;
        String first = path.segment(0);
        return "BSW_Builder".equals(first) || "bswmds".equals(first);
    }
}

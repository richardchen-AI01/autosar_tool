package cn.com.myorg.bswbuilder.ui.editors;

import java.io.File;

import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.Path;
import org.eclipse.core.runtime.PlatformObject;
import org.eclipse.jface.resource.ImageDescriptor;
import org.eclipse.ui.IPathEditorInput;
import org.eclipse.ui.IPersistableElement;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.ISharedImages;

/**
 * Editor input for a plain filesystem path that lives outside the Eclipse
 * workspace. The Autosar Explorer view reads ARXML files from a user-chosen
 * directory (not an imported project), so {@code IFileEditorInput} doesn't
 * apply — but {@code IPathEditorInput} does and is part of core
 * {@code org.eclipse.ui}, no IDE bundle dependency required.
 */
public final class LocalFileEditorInput extends PlatformObject implements IPathEditorInput {

    private final File file;
    private final IPath path;

    public LocalFileEditorInput(File file) {
        if (file == null) throw new IllegalArgumentException("file");
        this.file = file;
        this.path = new Path(file.getAbsolutePath());
    }

    public File getFile() { return file; }

    @Override public IPath getPath() { return path; }
    @Override public boolean exists() { return file.isFile(); }
    @Override public String getName() { return file.getName(); }
    @Override public String getToolTipText() { return file.getAbsolutePath(); }

    @Override
    public ImageDescriptor getImageDescriptor() {
        return PlatformUI.getWorkbench().getSharedImages()
                .getImageDescriptor(ISharedImages.IMG_OBJ_FILE);
    }

    @Override public IPersistableElement getPersistable() { return null; }

    @Override
    public boolean equals(Object o) {
        return o instanceof LocalFileEditorInput
                && path.equals(((LocalFileEditorInput) o).path);
    }
    @Override public int hashCode() { return path.hashCode(); }
}

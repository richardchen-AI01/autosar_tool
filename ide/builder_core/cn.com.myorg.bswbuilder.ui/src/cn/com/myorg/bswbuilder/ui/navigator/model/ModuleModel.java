package cn.com.myorg.bswbuilder.ui.navigator.model;

import java.util.Objects;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.Path;
import org.eclipse.core.runtime.PlatformObject;

/**
 * Leaf "BSW module" node — wraps a single {@code .arxml} module
 * configuration file (e.g. {@code MemIf.arxml}).
 *
 * <p>Reference: {@code cn.com.isoft.mal.model.ModuleModel}.
 * Field/operation surface mirrors model.ecore:
 * <ul>
 *   <li>{@code moduleName}: EString — display label, .arxml stripped</li>
 *   <li>{@code projectName}: EString</li>
 *   <li>{@code pathValue}: EString — workspace-relative file path</li>
 *   <li>op {@code getKeyValue()}: EString — composite identity for caches/maps</li>
 * </ul>
 *
 * <p>Per reference design, we hold no EObject reference here — Artop EMF
 * model is loaded lazily via Sphinx loadFile when the editor opens, not
 * at navigator expansion time. Tree expansion stops at this leaf in v0.2;
 * E5+ may add EObject children below (containers / parameters) if user
 * requests in-tree editing.
 */
public final class ModuleModel extends PlatformObject {

    private final ModuleKindModel parent;
    private final String pathValue;
    private final String projectName;
    private final String moduleName;

    public ModuleModel(ModuleKindModel parent, IFile arxml, String moduleName) {
        this.parent = Objects.requireNonNull(parent);
        this.pathValue = arxml.getFullPath().toString();
        this.projectName = arxml.getProject().getName();
        this.moduleName = Objects.requireNonNull(moduleName);
    }

    public ModuleKindModel getParent() { return parent; }

    public String getModuleName() { return moduleName; }
    public String getProjectName() { return projectName; }
    public String getPathValue()   { return pathValue; }

    public IPath getPath() { return new Path(pathValue); }

    /** Resolve back to live IFile via workspace lookup. */
    public IFile getFile() {
        return ResourcesPlugin.getWorkspace().getRoot().getFile(getPath());
    }

    /** ECore op: {@code getKeyValue()} — composite identity for cache keys. */
    public String getKeyValue() {
        return projectName + "::" + pathValue;
    }

    @Override
    public boolean equals(Object o) {
        return o instanceof ModuleModel
                && pathValue.equals(((ModuleModel) o).pathValue);
    }

    @Override
    public int hashCode() { return pathValue.hashCode(); }

    @Override
    public String toString() {
        return "ModuleModel(" + projectName + "/" + moduleName + ")";
    }
}

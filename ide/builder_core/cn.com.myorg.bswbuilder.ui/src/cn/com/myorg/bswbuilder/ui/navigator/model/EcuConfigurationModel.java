package cn.com.myorg.bswbuilder.ui.navigator.model;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IFolder;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.Path;
import org.eclipse.core.runtime.PlatformObject;

import cn.com.myorg.bswbuilder.ui.navigator.ModuleKindRegistry;

/**
 * Per-MCU ECU configuration container. One instance per
 * {@code <project>/BSW_Builder/&lt;MCU&gt;/} folder.
 *
 * <p>Reference: {@code cn.com.isoft.mal.model.EcuConfigurationModel}.
 * Field/operation surface mirrors model.ecore exactly:
 * <ul>
 *   <li>{@code pathValue}: EString — workspace-relative folder path</li>
 *   <li>{@code projectName}: EString</li>
 *   <li>{@code moduleKindModels}: ModuleKindModel[*] (containment)</li>
 *   <li>op {@code getFile()}: IFile — convenience IFile lookup</li>
 *   <li>op {@code getPath()}: IPath</li>
 *   <li>op {@code getFileName()}: EString</li>
 * </ul>
 *
 * <p>Why pathValue is stored as String and IFile/IPath computed lazily:
 * matches reference; IFile is workspace-state and not safe to keep across
 * workspace lifecycle events. Reference uses this pattern for EMF
 * persistence safety; we adopt same pattern for behavioral consistency.
 */
public final class EcuConfigurationModel extends PlatformObject {

    private final BswBuilderModel parent;
    private final String pathValue;
    private final String projectName;
    private List<ModuleKindModel> moduleKindModels;

    public EcuConfigurationModel(BswBuilderModel parent, IFolder mcuFolder) {
        this.parent = Objects.requireNonNull(parent);
        this.pathValue = mcuFolder.getFullPath().toString();
        this.projectName = mcuFolder.getProject().getName();
    }

    public BswBuilderModel getParent() { return parent; }

    public String getPathValue()   { return pathValue; }
    public String getProjectName() { return projectName; }

    /** mcuName = last segment of pathValue (e.g. "S32K148"). */
    public String getMcuName() {
        return new Path(pathValue).lastSegment();
    }

    /** ECore op: {@code getFile()} — but EcuConfigurationModel maps to a folder, not a file.
     *  Provided for reference parity; returns {@code null} in our IFolder-mapped case. */
    public IFile getFile() { return null; }

    /** ECore op: {@code getPath()}. */
    public IPath getPath() { return new Path(pathValue); }

    /** ECore op: {@code getFileName()}. */
    public String getFileName() { return getMcuName(); }

    /** Resolve back to the live IFolder via workspace lookup. */
    public IFolder getFolder() {
        return ResourcesPlugin.getWorkspace().getRoot().getFolder(getPath());
    }

    /**
     * Containment children — scan {@code .arxml} files under MCU folder,
     * group by {@link ModuleKindRegistry#kindOf(String)}.
     */
    public synchronized List<ModuleKindModel> getModuleKindModels() {
        if (moduleKindModels == null) {
            moduleKindModels = computeModuleKindModels();
        }
        return moduleKindModels;
    }

    private List<ModuleKindModel> computeModuleKindModels() {
        IFolder mcu = getFolder();
        if (!mcu.exists()) return new ArrayList<>();

        // Build kind -> [arxml IFile] map preserving discovery
        Map<String, List<IFile>> filesByKind = new LinkedHashMap<>();
        try {
            for (IResource r : mcu.members()) {
                if (r instanceof IFile && "arxml".equalsIgnoreCase(r.getFileExtension())) {
                    IFile f = (IFile) r;
                    String moduleName = ModuleKindRegistry.stripArxml(f.getName());
                    String kind = ModuleKindRegistry.kindOf(moduleName);
                    filesByKind.computeIfAbsent(kind, k -> new ArrayList<>()).add(f);
                }
            }
        } catch (CoreException ignored) { }

        // Emit kind nodes in registry order (stable UI), populating modules
        List<ModuleKindModel> result = new ArrayList<>();
        for (String kind : ModuleKindRegistry.KINDS) {
            List<IFile> bucket = filesByKind.get(kind);
            if (bucket == null || bucket.isEmpty()) continue;
            ModuleKindModel kindNode = new ModuleKindModel(this, kind);
            for (IFile f : bucket) {
                String moduleName = ModuleKindRegistry.stripArxml(f.getName());
                kindNode.addModule(new ModuleModel(kindNode, f, moduleName));
            }
            result.add(kindNode);
        }
        return result;
    }

    public synchronized void refresh() {
        moduleKindModels = null;
    }

    @Override
    public boolean equals(Object o) {
        return o instanceof EcuConfigurationModel
                && pathValue.equals(((EcuConfigurationModel) o).pathValue);
    }

    @Override
    public int hashCode() { return pathValue.hashCode(); }

    @Override
    public String toString() {
        return "EcuConfigurationModel(" + pathValue + ")";
    }
}

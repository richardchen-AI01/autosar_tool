package cn.com.myorg.bswbuilder.ui.navigator;

import java.util.List;
import java.util.Objects;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IFolder;
import org.eclipse.core.runtime.PlatformObject;

/**
 * Virtual node injected as a child of an MCU folder
 * ({@code <project>/BSW_Builder/&lt;MCU&gt;/}) to group BSW module .arxml
 * files by their AUTOSAR "kind" (COM / DIAG / MCAL / MEM / SYS / WDG / …).
 *
 * <p>Reference V25.10 calls this concept {@code KindTreeContainer}
 * (verified via decompiled {@code BswExplorerContentProvider} string
 * literal). iSoft's version is an EMF model element; ours is a plain POJO
 * because we work directly off file-system IResource without an EMF
 * model layer.
 *
 * <p>Equality — two KindGroupNodes are equal iff their parent MCU folder
 * AND kind label match. Eclipse navigator uses equals() to track tree
 * expansion state across refresh.
 */
public final class KindGroupNode extends PlatformObject {

    private final IFolder mcuFolder;
    private final String kind;
    private final List<IFile> arxmlFiles;

    public KindGroupNode(IFolder mcuFolder, String kind, List<IFile> arxmlFiles) {
        this.mcuFolder = Objects.requireNonNull(mcuFolder);
        this.kind = Objects.requireNonNull(kind);
        this.arxmlFiles = Objects.requireNonNull(arxmlFiles);
    }

    public IFolder getMcuFolder()      { return mcuFolder; }
    public String  getKind()           { return kind; }
    public List<IFile> getArxmlFiles() { return arxmlFiles; }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof KindGroupNode)) return false;
        KindGroupNode other = (KindGroupNode) o;
        return mcuFolder.equals(other.mcuFolder) && kind.equals(other.kind);
    }

    @Override
    public int hashCode() {
        return Objects.hash(mcuFolder, kind);
    }

    @Override
    public String toString() { return kind; }
}

package cn.com.myorg.bswbuilder.ui.navigator;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IFolder;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.jface.viewers.Viewer;
import org.eclipse.ui.IMemento;
import org.eclipse.ui.navigator.ICommonContentExtensionSite;
import org.eclipse.ui.navigator.ICommonContentProvider;
import org.eclipse.ui.navigator.IPipelinedTreeContentProvider2;
import org.eclipse.ui.navigator.PipelinedShapeModification;
import org.eclipse.ui.navigator.PipelinedViewerUpdate;

/**
 * navigatorContent provider that overlays kind-grouping on Eclipse
 * Project Explorer when the parent folder is an MCU directory
 * ({@code .../BSW_Builder/&lt;MCU&gt;/}).
 *
 * <p>Reference iSoft V25.10 implements this concept as
 * {@code BswExplorerContentProvider extends BasicExplorerContentProvider
 * (Sphinx)} — but their parent class is an EMF model browser. We work off
 * IResource directly (file-system path route, no EMF model layer in v0.1),
 * so we go via {@link IPipelinedTreeContentProvider2} instead — that's
 * Eclipse navigator's standard way to "rewrite" the children another
 * provider would have returned.
 *
 * <p>Behavior: when Project Explorer asks for children of an MCU folder,
 * we replace its raw .arxml/.xml child list with virtual
 * {@link KindGroupNode}s grouped by AUTOSAR module kind. Each KindGroupNode
 * then provides the actual IFile children when expanded. Other folders
 * are not touched (unmodified Eclipse default behavior).
 */
public class BswExplorerContentProvider
        implements ICommonContentProvider, IPipelinedTreeContentProvider2 {

    @Override public void init(ICommonContentExtensionSite config) { /* no-op */ }
    @Override public void restoreState(IMemento memento) { /* no-op */ }
    @Override public void saveState(IMemento memento) { /* no-op */ }
    @Override public void inputChanged(Viewer viewer, Object oldIn, Object newIn) { /* no-op */ }
    @Override public void dispose() { /* no-op */ }

    @Override
    public Object[] getElements(Object inputElement) {
        return new Object[0]; // we only contribute children, never roots
    }

    @Override
    public Object[] getChildren(Object parentElement) {
        if (parentElement instanceof KindGroupNode) {
            return ((KindGroupNode) parentElement).getArxmlFiles().toArray();
        }
        return new Object[0];
    }

    @Override
    public Object getParent(Object element) {
        if (element instanceof KindGroupNode) {
            return ((KindGroupNode) element).getMcuFolder();
        }
        if (element instanceof IFile) {
            IFile f = (IFile) element;
            if (isModuleConfigArxml(f)) {
                IFolder mcu = (IFolder) f.getParent();
                String kind = ModuleKindRegistry.kindOf(
                        ModuleKindRegistry.stripArxml(f.getName()));
                return new KindGroupNode(mcu, kind, java.util.Collections.singletonList(f));
            }
        }
        return null;
    }

    @Override
    public boolean hasChildren(Object element) {
        if (element instanceof KindGroupNode) {
            return !((KindGroupNode) element).getArxmlFiles().isEmpty();
        }
        return false;
    }

    /**
     * Pipelined hook: Eclipse navigator just collected the children via
     * the resource content provider; we intercept and re-bucket if the
     * parent is an MCU folder.
     */
    @Override
    public void getPipelinedChildren(Object parent, @SuppressWarnings("rawtypes") java.util.Set currentChildren) {
        if (!(parent instanceof IFolder) || !isMcuFolder((IFolder) parent)) {
            return;
        }
        IFolder mcu = (IFolder) parent;
        Map<String, List<IFile>> buckets = new LinkedHashMap<>();
        List<Object> nonGroupable = new ArrayList<>();

        for (Object child : currentChildren) {
            if (child instanceof IFile && isModuleConfigArxml((IFile) child)) {
                IFile f = (IFile) child;
                String moduleName = ModuleKindRegistry.stripArxml(f.getName());
                String kind = ModuleKindRegistry.kindOf(moduleName);
                buckets.computeIfAbsent(kind, k -> new ArrayList<>()).add(f);
            } else {
                nonGroupable.add(child);
            }
        }

        // Replace raw .arxml file children with KindGroupNodes
        currentChildren.clear();
        currentChildren.addAll(nonGroupable);
        for (String kind : ModuleKindRegistry.KINDS) {
            List<IFile> bucket = buckets.get(kind);
            if (bucket != null && !bucket.isEmpty()) {
                currentChildren.add(new KindGroupNode(mcu, kind, bucket));
            }
        }
    }

    @Override
    public void getPipelinedElements(Object input, @SuppressWarnings("rawtypes") java.util.Set currentElements) {
        // We don't override roots
    }

    @Override
    public Object getPipelinedParent(Object object, Object suggestedParent) {
        Object p = getParent(object);
        return p != null ? p : suggestedParent;
    }

    @Override
    public PipelinedShapeModification interceptAdd(PipelinedShapeModification addModification) { return addModification; }

    @Override
    public PipelinedShapeModification interceptRemove(PipelinedShapeModification removeModification) { return removeModification; }

    @Override
    public boolean interceptRefresh(PipelinedViewerUpdate refreshSynchronization) { return false; }

    @Override
    public boolean interceptUpdate(PipelinedViewerUpdate updateSynchronization) { return false; }

    @Override
    public boolean hasPipelinedChildren(Object element, boolean currentHasChildren) {
        if (element instanceof IFolder && isMcuFolder((IFolder) element)) {
            // True if any IFile children — usually yes
            try {
                for (IResource r : ((IFolder) element).members()) {
                    if (r instanceof IFile) return true;
                }
            } catch (CoreException ignored) { }
        }
        return currentHasChildren;
    }

    /** {@code .../BSW_Builder/<MCU>/} — parent named "BSW_Builder". */
    static boolean isMcuFolder(IFolder f) {
        IResource parent = f.getParent();
        return parent != null && "BSW_Builder".equals(parent.getName());
    }

    /** A file is a "BSW module config arxml" iff parent is MCU folder + ext .arxml. */
    static boolean isModuleConfigArxml(IFile f) {
        if (!"arxml".equalsIgnoreCase(f.getFileExtension())) return false;
        IResource parent = f.getParent();
        return parent instanceof IFolder && isMcuFolder((IFolder) parent);
    }
}

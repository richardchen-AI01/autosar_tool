package cn.com.myorg.bswbuilder.ui.navigator;

import org.eclipse.core.resources.IFolder;
import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.resources.IWorkspaceRoot;
import org.eclipse.core.runtime.PlatformObject;
import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.jface.viewers.Viewer;
import org.eclipse.ui.IMemento;
import org.eclipse.ui.navigator.ICommonContentExtensionSite;
import org.eclipse.ui.navigator.ICommonContentProvider;

import cn.com.myorg.bswbuilder.ui.navigator.model.BswBuilderModel;
import cn.com.myorg.bswbuilder.ui.navigator.model.EcuConfigurationModel;
import cn.com.myorg.bswbuilder.ui.navigator.model.ModuleKindModel;
import cn.com.myorg.bswbuilder.ui.navigator.model.ModuleModel;

/**
 * Tree content provider for the AUTOSAR Explorer view. Walks the mal model
 * 4-tier hierarchy:
 *
 * <pre>
 *   IWorkspaceRoot   (input)
 *     └ IProject     (Eclipse standard)
 *         └ BswBuilderModel       ← bridged from IProject (when BSW_Builder/ exists)
 *             └ EcuConfigurationModel
 *                 └ ModuleKindModel
 *                     └ ModuleModel  (leaf in v0.2)
 * </pre>
 *
 * <p>Reference: split into two providers in iSoft (pal-level
 * {@code CustomExplorerContentProvider} bridges IProject→BswBuilderModel,
 * bswbuilder.ui-level {@code BswExplorerContentProvider} expands deeper).
 * We collapse them into one class — single responsibility per provider is
 * iSoft's pattern; we have a single bundle so a single provider is simpler
 * and equivalent.
 *
 * <p>Why no Sphinx extends / no IPipelinedTreeContentProvider2: see
 * {@code feedback_reference_first} — pipelined was a wrong-route experiment
 * (E3 first attempt); reference uses a primary content provider over a
 * pure mal model tree, no EMF EObject in navigator below the leaf.
 */
public class BswExplorerContentProvider
        implements ICommonContentProvider, ITreeContentProvider {

    private static final Object[] EMPTY = new Object[0];

    @Override public void init(ICommonContentExtensionSite cfg) { /* no-op */ }
    @Override public void restoreState(IMemento memento) { /* no-op */ }
    @Override public void saveState(IMemento memento) { /* no-op */ }
    @Override public void inputChanged(Viewer viewer, Object o, Object n) { /* no-op */ }
    @Override public void dispose() { /* no-op */ }

    @Override
    public Object[] getElements(Object input) {
        return getChildren(input);
    }

    @Override
    public Object[] getChildren(Object parent) {
        if (parent instanceof IWorkspaceRoot) {
            return ((IWorkspaceRoot) parent).getProjects();
        }
        if (parent instanceof IProject) {
            IProject p = (IProject) parent;
            if (isBswProject(p)) {
                return new Object[]{ new BswBuilderModel(p) };
            }
            return EMPTY;
        }
        if (parent instanceof BswBuilderModel) {
            return ((BswBuilderModel) parent).getEcuConfigurationModels().toArray();
        }
        if (parent instanceof EcuConfigurationModel) {
            return ((EcuConfigurationModel) parent).getModuleKindModels().toArray();
        }
        if (parent instanceof ModuleKindModel) {
            return ((ModuleKindModel) parent).getModuleModels().toArray();
        }
        if (parent instanceof ModuleModel) {
            return EMPTY; // leaf in v0.2
        }
        return EMPTY;
    }

    @Override
    public Object getParent(Object element) {
        if (element instanceof PlatformObject) {
            if (element instanceof BswBuilderModel) {
                return ((BswBuilderModel) element).getProject();
            }
            if (element instanceof EcuConfigurationModel) {
                return ((EcuConfigurationModel) element).getParent();
            }
            if (element instanceof ModuleKindModel) {
                return ((ModuleKindModel) element).getParent();
            }
            if (element instanceof ModuleModel) {
                return ((ModuleModel) element).getParent();
            }
        }
        if (element instanceof IProject) {
            return ((IProject) element).getWorkspace().getRoot();
        }
        return null;
    }

    @Override
    public boolean hasChildren(Object element) {
        if (element instanceof IWorkspaceRoot) return true;
        if (element instanceof IProject) return isBswProject((IProject) element);
        if (element instanceof BswBuilderModel) {
            return !((BswBuilderModel) element).getEcuConfigurationModels().isEmpty();
        }
        if (element instanceof EcuConfigurationModel) {
            return !((EcuConfigurationModel) element).getModuleKindModels().isEmpty();
        }
        if (element instanceof ModuleKindModel) {
            return !((ModuleKindModel) element).getModuleModels().isEmpty();
        }
        return false;
    }

    /** A project counts as "BSW project" iff it contains a {@code BSW_Builder/} folder. */
    static boolean isBswProject(IProject p) {
        if (!p.isAccessible()) return false;
        IResource r = p.findMember("BSW_Builder");
        return r instanceof IFolder && r.exists();
    }
}

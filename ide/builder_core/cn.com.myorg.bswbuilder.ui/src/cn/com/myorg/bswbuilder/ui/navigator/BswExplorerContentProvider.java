package cn.com.myorg.bswbuilder.ui.navigator;

import org.eclipse.core.resources.IFolder;
import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.resources.IWorkspaceRoot;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.jface.viewers.Viewer;
import org.eclipse.ui.IMemento;
import org.eclipse.ui.navigator.ICommonContentExtensionSite;
import org.eclipse.ui.navigator.ICommonContentProvider;

import cn.com.myorg.mal.model.BswBuilderModel;
import cn.com.myorg.mal.model.EcuConfigurationModel;
import cn.com.myorg.mal.model.ModelFactory;
import cn.com.myorg.mal.model.ModuleKindModel;
import cn.com.myorg.mal.model.ModuleModel;

/**
 * Transitional content provider for the AUTOSAR Explorer view (E3-B-3).
 *
 * <p>Walks the mal model 4-tier hierarchy:
 * <pre>
 *   IWorkspaceRoot
 *     └ IProject (Eclipse standard)
 *         └ BswBuilderModel       ← created on-demand by this provider in E3-B-3
 *             └ EcuConfigurationModel    (populated empty until E3-B-4 ModelManager)
 *                 └ ModuleKindModel      (populated empty until E3-B-4)
 *                     └ ModuleModel      (leaf)
 * </pre>
 *
 * <p>Transitional caveat (will be replaced in E3-B-4/5):
 * <ul>
 *   <li>Creates BswBuilderModel directly via {@link ModelFactory#eINSTANCE} —
 *       reference uses {@code ModelManager.getBswBuilderByProject(IProject)} with a
 *       static cache. Without ModelManager (incoming in E3-B-4), every refresh
 *       creates a fresh BswBuilderModel; tree will show project node but expand to
 *       empty (children populated by ModelManager.resetBswBuildModel which doesn't
 *       exist yet).</li>
 *   <li>Reference architecture: pal-level {@code CustomExplorerContentProvider}
 *       bridges IProject → BswBuilderModel; bswbuilder.ui-level
 *       {@code BswExplorerContentProvider} expands deeper. We collapse into one
 *       (single bundle, equivalent behavior).</li>
 * </ul>
 *
 * <p>Reference E3-B-5 will: extend {@code Sphinx::BasicExplorerContentProvider},
 * call {@code ModelManager.getBswBuilderByProject(project)}, and let the EMF
 * notification chain (via Sphinx ResourceSetListener) drive viewer refresh.
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
                return new Object[]{ createBswBuilderModelFor(p) };
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
        if (element instanceof BswBuilderModel) {
            return ResourcesPlugin.getWorkspace().getRoot()
                    .getProject(((BswBuilderModel) element).getProjectName());
        }
        if (element instanceof EObject) {
            return ((EObject) element).eContainer();
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

    /** Factory-create a BswBuilderModel for the project (no caching — E3-B-4 ModelManager will). */
    private static BswBuilderModel createBswBuilderModelFor(IProject p) {
        BswBuilderModel m = ModelFactory.eINSTANCE.createBswBuilderModel();
        m.setName("BSW_Builder");
        m.setProjectName(p.getName());
        return m;
    }

    /** A project counts as "BSW project" iff it contains a {@code BSW_Builder/} folder. */
    static boolean isBswProject(IProject p) {
        if (!p.isAccessible()) return false;
        IResource r = p.findMember("BSW_Builder");
        return r instanceof IFolder && r.exists();
    }
}

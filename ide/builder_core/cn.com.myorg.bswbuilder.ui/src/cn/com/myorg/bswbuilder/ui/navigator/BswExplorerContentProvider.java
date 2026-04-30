package cn.com.myorg.bswbuilder.ui.navigator;

import java.util.ArrayList;

import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.IWorkspaceRoot;
import org.eclipse.emf.ecore.EClassifier;
import org.eclipse.emf.ecore.EcorePackage;
import org.eclipse.emf.transaction.NotificationFilter;
import org.eclipse.emf.transaction.ResourceSetChangeEvent;
import org.eclipse.emf.transaction.ResourceSetListener;
import org.eclipse.emf.transaction.ResourceSetListenerImpl;
import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.sphinx.emf.explorer.BasicExplorerContentProvider;
import org.eclipse.sphinx.platform.ui.util.ExtendedPlatformUI;

import cn.com.myorg.mal.model.BswBuilderModel;
import cn.com.myorg.mal.model.EcuConfigurationModel;
import cn.com.myorg.mal.model.ModuleKindModel;
import cn.com.myorg.mal.model.ModuleModel;
import cn.com.myorg.pal.model.ModelManager;

/**
 * AUTOSAR Explorer view content provider.
 *
 * <p>Combines the responsibilities of two reference providers:
 * <ul>
 *   <li>{@code cn.com.isoft.pal.ui.contentproviders.CustomExplorerContentProvider} —
 *       IProject → BswBuilderModel bridge via {@link ModelManager#getBswBuilderByProject}</li>
 *   <li>{@code cn.com.isoft.bswbuilder.ui.contentproviders.BswExplorerContentProvider} —
 *       mal model walk (BswBuilderModel → EcuConfigurationModel → ModuleKindModel
 *       → ModuleModel) + EMF ResourceSetListener for auto-refresh</li>
 * </ul>
 *
 * <p>We collapse them because we have a single bswbuilder.ui bundle (reference splits
 * across pal + bswbuilder.ui). External behavior is identical.
 *
 * <p>{@code createResourceChangedListener} returns a Sphinx ResourceSetListener watching
 * three EMF features (RESOURCES, CONTENTS, URI) — fires viewer.refresh() on the SWT
 * display thread when an Artop AUTOSAR Resource changes (load/save/edit). This is how
 * the navigator stays in sync with edits made via FormEditor — same exact pattern as
 * reference {@code BswExplorerContentProvider.createResourceChangedListener}.
 */
public class BswExplorerContentProvider
        extends BasicExplorerContentProvider
        implements ITreeContentProvider {

    @Override
    protected ResourceSetListener createResourceChangedListener() {
        return new ResourceSetListenerImpl(
                NotificationFilter.createFeatureFilter(
                        (EClassifier) EcorePackage.eINSTANCE.getEResourceSet(), 0)
                    .or(NotificationFilter.createFeatureFilter(
                        (EClassifier) EcorePackage.eINSTANCE.getEResource(), 4))
                    .or(NotificationFilter.createFeatureFilter(
                        (EClassifier) EcorePackage.eINSTANCE.getEResource(), 3))) {

            @Override
            public void resourceSetChanged(ResourceSetChangeEvent event) {
                ExtendedPlatformUI.getDisplay().asyncExec(
                        () -> getViewer().refresh());
            }

            @Override
            public boolean isPostcommitOnly() {
                return true;
            }
        };
    }

    @Override
    public Object[] getChildren(Object parentElement) {
        // (1) Eclipse workbench root → registered IProjects
        if (parentElement instanceof IWorkspaceRoot) {
            return ((IWorkspaceRoot) parentElement).getProjects();
        }
        // (2) IProject → BswBuilderModel bridge (reference: pal.CustomExplorerContentProvider)
        if (parentElement instanceof IProject && ((IProject) parentElement).isOpen()) {
            IProject project = (IProject) parentElement;
            BswBuilderModel model = ModelManager.getBswBuilderByProject(project);
            return model == null ? new Object[0] : new Object[]{ model };
        }
        // (3) mal model walk (reference: bswbuilder.ui.BswExplorerContentProvider)
        if (parentElement instanceof BswBuilderModel) {
            ArrayList<Object> children = new ArrayList<>();
            children.addAll(((BswBuilderModel) parentElement).getEcuConfigurationModels());
            return children.toArray();
        }
        if (parentElement instanceof EcuConfigurationModel) {
            ArrayList<Object> children = new ArrayList<>();
            children.addAll(((EcuConfigurationModel) parentElement).getModuleKindModels());
            return children.toArray();
        }
        if (parentElement instanceof ModuleKindModel) {
            ArrayList<Object> children = new ArrayList<>();
            children.addAll(((ModuleKindModel) parentElement).getModuleModels());
            return children.toArray();
        }
        if (parentElement instanceof ModuleModel) {
            return new Object[0]; // leaf
        }
        // (4) default → Sphinx super (handles IFile → EObject roots etc.)
        return super.getChildren(parentElement);
    }
}

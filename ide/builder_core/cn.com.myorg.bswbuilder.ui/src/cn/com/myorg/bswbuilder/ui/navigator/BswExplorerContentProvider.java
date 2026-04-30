package cn.com.myorg.bswbuilder.ui.navigator;

import java.util.ArrayList;

import org.eclipse.core.resources.IContainer;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.resources.IWorkspaceRoot;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.emf.ecore.EClassifier;
import org.eclipse.emf.ecore.EcorePackage;
import org.eclipse.emf.transaction.NotificationFilter;
import org.eclipse.emf.transaction.ResourceSetChangeEvent;
import org.eclipse.emf.transaction.ResourceSetListener;
import org.eclipse.emf.transaction.ResourceSetListenerImpl;
import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.sphinx.emf.explorer.BasicExplorerContentProvider;
import org.eclipse.sphinx.platform.ui.util.ExtendedPlatformUI;

/**
 * AUTOSAR Explorer content provider — file-system tree (mirrors the standard
 * Eclipse Project Explorer's IResource walk so the user sees the full project
 * layout: BSW_Builder/, bswmds/, config/, ServiceComponents/, catch.xml,
 * navigator.xml...).
 *
 * <p>2026-05-01 user pivot: AUTOSAR Explorer was previously driven off the mal
 * model + IoC chain (BswModuleManager / KindContainModule), which only surfaced
 * registered plugin modules and hid all other project content. User wanted
 * full Project-Explorer-equivalent visibility while preserving the polish
 * (module name without .arxml suffix, module icon) — that polish now lives
 * exclusively in {@link BswExplorerLabelProvider}.
 *
 * <p>The mal model + ModelManager remain alive for handler-side metadata
 * access (Generate / Validate / Update Bswmd) via AutocoreCoordinator lookup,
 * just no longer for tree rendering.
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
        try {
            if (parentElement instanceof IWorkspaceRoot) {
                ArrayList<IProject> visible = new ArrayList<>();
                for (IProject p : ((IWorkspaceRoot) parentElement).getProjects()) {
                    if (p.isOpen()) visible.add(p);
                }
                return visible.toArray();
            }
            if (parentElement instanceof IContainer) {
                IContainer c = (IContainer) parentElement;
                if (!c.isAccessible()) return new Object[0];
                ArrayList<Object> children = new ArrayList<>();
                for (IResource child : c.members()) {
                    // Hide Eclipse internals (.project / .settings / .classpath /
                    // .arxmlHashFile) — Project Explorer hides them too via filters.
                    if (!child.getName().startsWith(".")) {
                        children.add(child);
                    }
                }
                return children.toArray();
            }
            if (parentElement instanceof IFile) {
                return new Object[0];
            }
        } catch (CoreException e) {
            // Fall through to super (Sphinx EMF resource expansion etc.).
        }
        return super.getChildren(parentElement);
    }

    @Override
    public Object getParent(Object element) {
        if (element instanceof IResource) {
            return ((IResource) element).getParent();
        }
        return super.getParent(element);
    }

    @Override
    public boolean hasChildren(Object element) {
        if (element instanceof IFile) return false;
        if (element instanceof IContainer) {
            try {
                IContainer c = (IContainer) element;
                if (!c.isAccessible()) return false;
                for (IResource child : c.members()) {
                    if (!child.getName().startsWith(".")) return true;
                }
                return false;
            } catch (CoreException e) {
                return false;
            }
        }
        return super.hasChildren(element);
    }
}

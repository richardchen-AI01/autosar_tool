package cn.com.myorg.bswbuilder.common.app;

import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.IProjectNature;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.sphinx.platform.util.ExtendedPlatform;

/**
 * Project nature marking a BSW workspace project. Plays the same role as
 * iSoft V25.10's {@code cn.com.isoft.workspace.bswbuildernature} nature
 * (decompiled class {@code cn.com.isoft.pal.workspace.natures.BSWBuilderNature}).
 *
 * <p>The nature itself does no work — Sphinx + Artop look up
 * {@link IProjectNature}s on a project and use them as a discriminator
 * for which metamodel descriptor / editing-domain factory listener to
 * apply. Just having this nature on a project is enough to make Sphinx
 * recognise our BSW workspaces.
 *
 * <p>Mirrors reference impl exactly:
 * <ul>
 *   <li>{@code configure} / {@code deconfigure} are no-ops</li>
 *   <li>Static {@link #addTo(IProject, IProgressMonitor)} helper delegates to
 *       Sphinx's {@link ExtendedPlatform#addNature} (handles xml mutation
 *       of {@code .project} for you)</li>
 *   <li>Static {@link #removeFrom(IProject, IProgressMonitor)} symmetric</li>
 * </ul>
 */
public class BswBuilderNature implements IProjectNature {

    /** Must match the {@code id} of the {@code natures} extension in
     *  {@code plugin.xml}; used by external code (handlers, importers) to
     *  add/check the nature without typing the string. */
    public static final String ID = "cn.com.myorg.bswbuilder.common.bswBuilderNature";

    private IProject project;

    public BswBuilderNature() { }

    public BswBuilderNature(IProject project) {
        setProject(project);
    }

    @Override public void configure() throws CoreException { /* no-op */ }
    @Override public void deconfigure() throws CoreException { /* no-op */ }

    @Override public IProject getProject() { return project; }
    @Override public void setProject(IProject project) { this.project = project; }

    public static void addTo(IProject project, IProgressMonitor monitor) throws CoreException {
        ExtendedPlatform.addNature(project, ID, monitor);
    }

    public static void removeFrom(IProject project, IProgressMonitor monitor) throws CoreException {
        ExtendedPlatform.removeNature(project, ID, monitor);
    }
}

package cn.com.myorg.bswbuilder.ui.navigator.model;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

import org.eclipse.core.resources.IFolder;
import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.PlatformObject;

/**
 * Top-level "mal model" wrapper for a BSW Builder project (an Eclipse
 * {@link IProject} that has a {@code BSW_Builder/} folder).
 *
 * <p>Reference: {@code cn.com.isoft.mal.model.BswBuilderModel} (decompiled
 * from {@code cn.com.isoft.mal.model_1.0.0.202601300910.jar}, model.ecore
 * spec preserved at
 * {@code builder_core/cn.com.myorg.bswbuilder.ui/model/mal-model.ecore}).
 *
 * <p>Field surface mirrors the .ecore exactly:
 * <ul>
 *   <li>{@code name}: EString — display label (= project name)</li>
 *   <li>{@code projectName}: EString — IProject identifier</li>
 *   <li>{@code ecuConfigurationModels}: EcuConfigurationModel[*] (containment)</li>
 * </ul>
 *
 * <p>Differs from reference in that we use POJO ({@code extends PlatformObject})
 * rather than a generated EMF EClass; this is functional parity, not
 * structural parity (see ADR-0007 for rationale: iSoft model.ecore + impl
 * .class are encrypted, so reproducing the EMF generated code 1:1 is
 * impossible without the generator).
 */
public final class BswBuilderModel extends PlatformObject {

    private final IProject project;
    private List<EcuConfigurationModel> ecuConfigurationModels;

    public BswBuilderModel(IProject project) {
        this.project = Objects.requireNonNull(project);
    }

    /** Display label — same as project name in the reference IDE. */
    public String getName() {
        return project.getName();
    }

    /** IProject identifier. */
    public String getProjectName() {
        return project.getName();
    }

    public IProject getProject() {
        return project;
    }

    /**
     * Containment children — discovered by scanning {@code BSW_Builder/}
     * sub-folders (each a per-MCU ECU configuration).
     */
    public synchronized List<EcuConfigurationModel> getEcuConfigurationModels() {
        if (ecuConfigurationModels == null) {
            ecuConfigurationModels = new ArrayList<>();
            IFolder bswBuilder = project.getFolder("BSW_Builder");
            if (bswBuilder.exists()) {
                try {
                    for (IResource r : bswBuilder.members()) {
                        if (r instanceof IFolder) {
                            ecuConfigurationModels.add(
                                    new EcuConfigurationModel(this, (IFolder) r));
                        }
                    }
                } catch (CoreException ignored) { }
            }
        }
        return ecuConfigurationModels;
    }

    /** Force re-scan on next {@link #getEcuConfigurationModels()}. */
    public synchronized void refresh() {
        ecuConfigurationModels = null;
    }

    @Override
    public boolean equals(Object o) {
        return o instanceof BswBuilderModel
                && project.equals(((BswBuilderModel) o).project);
    }

    @Override
    public int hashCode() {
        return project.hashCode();
    }

    @Override
    public String toString() {
        return "BswBuilderModel(" + getProjectName() + ")";
    }
}

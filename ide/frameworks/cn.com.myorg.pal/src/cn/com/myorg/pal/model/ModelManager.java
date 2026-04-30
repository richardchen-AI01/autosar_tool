package cn.com.myorg.pal.model;

import java.util.HashMap;
import java.util.Map;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IFolder;
import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.runtime.CoreException;

import cn.com.myorg.mal.AutocoreModuleDefinition;
import cn.com.myorg.mal.BswModuleManager;
import cn.com.myorg.mal.coordinator.KindContainModule;
import cn.com.myorg.mal.model.BswBuilderModel;
import cn.com.myorg.mal.model.EcuConfigurationModel;
import cn.com.myorg.mal.model.ModelFactory;
import cn.com.myorg.mal.model.ModuleKindModel;
import cn.com.myorg.mal.model.ModuleModel;
import cn.com.myorg.pal.base.functionblock.FunctionBlockManager;
import cn.com.myorg.pal.base.interfaces.common.IFunctionBlock;

/**
 * Slim port of {@code cn.com.isoft.pal.model.ModelManager}.
 *
 * <p>Public API for E3-B-4 (matches reference signatures):
 * <ul>
 *   <li>{@link #getBswBuilderByProject(IProject)} — cached lookup; creates
 *       BswBuilderModel via ModelFactory if not cached, populates one
 *       EcuConfigurationModel per {@code BSW_Builder/<MCU>/} folder.</li>
 *   <li>{@link #resetBswBuildModel(IProject)} — invalidate cache + rebuild</li>
 *   <li>{@link #refreshNavigatorViewer()} — no-op stub for now (E3-B-5 wires viewer)</li>
 * </ul>
 *
 * <p>Reference also exposes 4 EMF caches (AUTOSAR / EcucValueCollection /
 * EcucModuleConfigurationValues / autosar map) — those are loaded on demand
 * by Sphinx's ModelLoadManager and not maintained here in v0.2.
 *
 * <p>Reference also has {@link #refreshNavigatorViewer()} actually finding
 * the AutosarNavigator view + calling refresh(); that wiring lands in E3-B-5
 * once BswAutosarExplorerView is registered with a known viewer ID.
 */
public final class ModelManager {

    private static final String BSW_FUNC_ID = "cn.com.myorg.bsw.funcId";

    /** Reference: same shape — Map keyed by project name. */
    private static final Map<String, BswBuilderModel> projectBswBuilderModelMap = new HashMap<>();

    /** Reference: tracks rename in ContentProvider for cache rewire. */
    public static String oldProjectName = null;

    private ModelManager() {}

    /**
     * Reference contract: returns null if project is not a BSW project
     * (no {@code BSW_Builder/} folder OR no IFunctionBlock with id
     * {@value #BSW_FUNC_ID} registered). Otherwise returns cached or
     * freshly-created model.
     */
    public static synchronized BswBuilderModel getBswBuilderByProject(IProject project) {
        if (project == null || !project.isAccessible()) return null;
        BswBuilderModel cached = projectBswBuilderModelMap.get(project.getName());
        if (cached != null) return cached;

        if (!isBSWBuilderProject(project)) return null;

        // Reference also gates on a registered IFunctionBlock with matching id.
        // We honor the same gate so future contributors must register the
        // bswbuilder FunctionBlock to make a project show up in the navigator.
        boolean hasBswFunc = false;
        for (IFunctionBlock fb : FunctionBlockManager.getRegFunctionBlock()) {
            if (BSW_FUNC_ID.equals(fb.getId())) { hasBswFunc = true; break; }
        }
        if (!hasBswFunc) return null;

        BswBuilderModel model = ModelFactory.eINSTANCE.createBswBuilderModel();
        model.setName("BSW_Builder");
        model.setProjectName(project.getName());
        populateEcuConfigurationModels(project, model);
        projectBswBuilderModelMap.put(project.getName(), model);
        return model;
    }

    /**
     * Reference's resetBswBuildModel also clears 3 other EMF caches
     * (AUTOSAR / EcucValueCollection / ModuleConfigurationValues); we
     * skip those (they don't exist yet in v0.2).
     */
    public static synchronized void resetBswBuildModel(IProject project) {
        if (project == null) return;
        BswBuilderModel model = projectBswBuilderModelMap.get(project.getName());
        if (model != null) {
            model.getEcuConfigurationModels().clear();
            populateEcuConfigurationModels(project, model);
        }
    }

    /** No-op for E3-B-4; E3-B-5 wires this to AutosarNavigator.refresh(). */
    public static void refreshNavigatorViewer() { /* no-op */ }

    /** Drop a project's cached model entry (used on project close/delete). */
    public static synchronized void clearProjectMapCache(String projectName) {
        projectBswBuilderModelMap.remove(projectName);
    }

    /** True iff project has a {@code BSW_Builder/} folder at the root. */
    public static boolean isBSWBuilderProject(IProject project) {
        if (!project.isAccessible()) return false;
        IResource r = project.findMember("BSW_Builder");
        return r instanceof IFolder && r.exists();
    }

    /**
     * Scan {@code BSW_Builder/<MCU>/} → for each MCU build full mal model subtree:
     * EcuConfigurationModel → ModuleKindModel(s) (driven by IoC: BswModuleManager
     * groups registered modules by kind) → ModuleModel(s) (one per .arxml found
     * in the MCU folder that matches a registered module's shortName).
     *
     * <p>Reference flow (CFR-confirmed):
     * <ol>
     *   <li>BswModuleManager.getInstance(mcuName) reads modulekind + module
     *       extensions, returns KindContainModule list.</li>
     *   <li>Each KindContainModule has kind name + AutocoreModuleDefinition list.</li>
     *   <li>For each AutocoreModuleDefinition, check if {@code <shortName>.arxml}
     *       exists in MCU folder; if yes → create ModuleModel.</li>
     * </ol>
     */
    private static void populateEcuConfigurationModels(IProject project, BswBuilderModel model) {
        IFolder bswFolder = project.getFolder("BSW_Builder");
        if (!bswFolder.exists()) return;
        try {
            for (IResource child : bswFolder.members()) {
                if (!(child instanceof IFolder)) continue;
                IFolder mcu = (IFolder) child;
                EcuConfigurationModel ecu = ModelFactory.eINSTANCE.createEcuConfigurationModel();
                // pathValue points at the canonical config file inside MCU folder
                // (placeholder for now; real one set per-module via ModuleModel.pathValue).
                IFile placeholder = mcu.getFile(mcu.getName() + ".arxml");
                ecu.setPathValue(placeholder.getProjectRelativePath().toString());
                ecu.setProjectName(project.getName());
                model.getEcuConfigurationModels().add(ecu);
                populateModuleKindModels(mcu, ecu);
            }
        } catch (CoreException e) {
            e.printStackTrace();
        }
    }

    /**
     * Build kind/module subtree for one MCU folder.
     * Drives off BswModuleManager (real IoC chain — modulekind + module extensions).
     */
    private static void populateModuleKindModels(IFolder mcu, EcuConfigurationModel ecu) {
        BswModuleManager mgr = BswModuleManager.getInstance(mcu.getName());
        for (KindContainModule kindContainer : mgr.getKindContainModule()) {
            ModuleKindModel kindModel = ModelFactory.eINSTANCE.createModuleKindModel();
            kindModel.setKindName(kindContainer.getKindName());
            ecu.getModuleKindModels().add(kindModel);

            for (AutocoreModuleDefinition def : kindContainer.getModules()) {
                IFile arxml = mcu.getFile(def.getModuleShortName() + ".arxml");
                if (!arxml.exists()) continue; // module registered but no config in this project

                ModuleModel modModel = ModelFactory.eINSTANCE.createModuleModel();
                modModel.setModuleName(def.getModuleShortName());
                modModel.setProjectName(mcu.getProject().getName());
                modModel.setPathValue(arxml.getProjectRelativePath().toString());
                kindModel.getModuleModels().add(modModel);
            }
        }
    }
}

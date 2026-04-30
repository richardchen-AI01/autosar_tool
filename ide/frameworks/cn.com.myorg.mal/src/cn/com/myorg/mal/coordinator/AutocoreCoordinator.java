package cn.com.myorg.mal.coordinator;

import java.util.ArrayList;
import java.util.List;

import org.eclipse.core.runtime.IConfigurationElement;
import org.eclipse.core.runtime.IExtensionRegistry;
import org.eclipse.core.runtime.Platform;

import cn.com.myorg.mal.AutocoreModuleDefinition;
import cn.com.myorg.mal.exceptions.AutocoreException;
import cn.com.myorg.mal.exceptions.ModuleDefinitionNotFoundException;

/**
 * Slim port of {@code cn.com.isoft.mal.coordinator.AutocoreCoordinator}.
 *
 * <p>Public API contract preserved (3 essential methods + 2 helpers):
 * <ul>
 *   <li>{@link #getVendorModules()} / {@link #getVendorModules(String)} —
 *       reads {@code cn.com.myorg.bswbuilder.extensionpoints.module}</li>
 *   <li>{@link #getMCUs()} — reads {@code .mcu} extension point (no license filter)</li>
 *   <li>{@link #getBswModuleKind()} — reads {@code .modulekind} extension point</li>
 *   <li>{@link #hasCompatibleMcu(AutocoreModuleDefinition, String)} — MCU match</li>
 *   <li>{@link #hasCompatibleAutosarType(AutocoreModuleDefinition, String)} — version match</li>
 * </ul>
 *
 * <p>Deliberate divergence from reference (recorded in
 * {@code docs/REFERENCE_DIVERGENCE.md}):
 * <ul>
 *   <li>No license / dongle / BitAnswer integration (research project)</li>
 *   <li>No Excel-driven MCU population (osinfo.xls not used)</li>
 *   <li>No verifyLicence / installLicenseKey / hardware fingerprinting</li>
 *   <li>No headless mode flags (ApplicationType / verbosity / generate)</li>
 *   <li>No parallel-models extension support (deferred)</li>
 * </ul>
 *
 * <p>Public method signatures match reference 1:1, so future bundles depending
 * on this can be ported byte-for-byte once stubs are filled.
 */
public final class AutocoreCoordinator {

    public static final AutocoreCoordinator INSTANCE = new AutocoreCoordinator();

    private static final String EP_MODULE     = "cn.com.myorg.bswbuilder.extensionpoints.module";
    private static final String EP_MCU        = "cn.com.myorg.bswbuilder.extensionpoints.mcu";
    private static final String EP_MODULEKIND = "cn.com.myorg.bswbuilder.extensionpoints.modulekind";

    private AutocoreCoordinator() { /* singleton */ }

    /**
     * All registered modules (no MCU filter). Mirrors reference reading-pattern:
     * {@code Platform.getExtensionRegistry().getConfigurationElementsFor(...)} +
     * 6-arg AutocoreModuleDefinition constructor passing the IConfigurationElement.
     */
    public static ArrayList<AutocoreModuleDefinition> getVendorModules() {
        IExtensionRegistry reg = Platform.getExtensionRegistry();
        ArrayList<AutocoreModuleDefinition> result = new ArrayList<>();
        IConfigurationElement[] extensions = reg.getConfigurationElementsFor(EP_MODULE);
        for (IConfigurationElement el : extensions) {
            String mcus = el.getAttribute("requiredMcus");
            ArrayList<String> requiredMcus = null;
            if (mcus != null) {
                requiredMcus = new ArrayList<>();
                for (String m : mcus.split(",")) requiredMcus.add(m.trim());
            }
            try {
                result.add(new AutocoreModuleDefinition(
                        requiredMcus,
                        el.getAttribute("version"),
                        el.getAttribute("requiredAutoSarType"),
                        el.getAttribute("moduledefinition"),
                        el.getAttribute("imageIdentifier"),
                        el));
            } catch (AutocoreException e) {
                e.printStackTrace();
            }
        }
        return result;
    }

    /** Filtered to modules compatible with the given MCU. */
    public static ArrayList<AutocoreModuleDefinition> getVendorModules(String mcu) {
        ArrayList<AutocoreModuleDefinition> result = new ArrayList<>();
        for (AutocoreModuleDefinition mod : getVendorModules()) {
            if (mod.getRequiredMcus() == null || mod.getRequiredMcus().isEmpty()) {
                result.add(mod);
                continue;
            }
            if (hasCompatibleMcu(mod, mcu)) {
                result.add(mod);
            }
        }
        return result;
    }

    /** Whether a module declares this MCU in {@code requiredMcus} (or has no restriction). */
    public static boolean hasCompatibleMcu(AutocoreModuleDefinition mod, String mcu) {
        ArrayList<String> req = mod.getRequiredMcus();
        if (req == null || req.isEmpty()) return true;
        return req.contains(mcu);
    }

    /** Whether a module declares this AUTOSAR type in {@code requiredAutoSarType}. */
    public static boolean hasCompatibleAutosarType(AutocoreModuleDefinition mod, String autosarType) {
        String req = mod.getAutosarType();
        return req == null || req.isEmpty() || req.equals(autosarType);
    }

    /**
     * MCUs declared via {@code mcu} extension point. Reference filters by
     * license whitelist; we don't.
     */
    public static ArrayList<AutocoreMCU> getMCUs() {
        IExtensionRegistry reg = Platform.getExtensionRegistry();
        ArrayList<AutocoreMCU> mcus = new ArrayList<>();
        for (IConfigurationElement el : reg.getConfigurationElementsFor(EP_MCU)) {
            String name = el.getAttribute("mcuName");
            String mfr = el.getAttribute("mcuManufacturer");
            String model = el.getAttribute("mcuModel");
            String multi = el.getAttribute("multicore");
            String numCores = el.getAttribute("numberOfCores");
            mcus.add(new AutocoreMCU(
                    name, mfr, model,
                    multi != null && !"false".equals(multi),
                    numCores == null ? 1 : Integer.parseInt(numCores)));
        }
        return mcus;
    }

    /** Kinds (categories) declared via {@code modulekind} extension point. */
    public ArrayList<BswModuleKind> getBswModuleKind() {
        IExtensionRegistry reg = Platform.getExtensionRegistry();
        ArrayList<BswModuleKind> kinds = new ArrayList<>();
        for (IConfigurationElement el : reg.getConfigurationElementsFor(EP_MODULEKIND)) {
            kinds.add(new BswModuleKind(
                    el.getAttribute("name"),
                    el.getAttribute("description")));
        }
        return kinds;
    }

    /** Look up by shortName; throws if not registered (reference contract). */
    public static AutocoreModuleDefinition getVendorModule(String shortName)
            throws ModuleDefinitionNotFoundException {
        for (AutocoreModuleDefinition mod : getVendorModules()) {
            if (shortName.equals(mod.getModuleShortName())) return mod;
        }
        throw new ModuleDefinitionNotFoundException(
                "No module definition registered with shortName=" + shortName);
    }

    /** Reference also exposes container regs; deferred (no bswbuilder.modules use it yet). */
    public List<Object> getContainerRegDefinitions() {
        return new ArrayList<>();
    }
}

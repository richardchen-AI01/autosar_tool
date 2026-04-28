package cn.com.myorg.bswbuilder.modules.memif.data;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 * Static schema metadata for the 4 MemIfGeneral parameters.
 *
 * <p>Mirrored from {@code ide/modules/cn.com.myorg.bswbuilder.modules.memif/MemIfDef.arxml}.
 * Hard-coded in v0.1 because the schema is small and stable; v0.2 will replace
 * this with a Sphinx-based schema metadata loader.
 *
 * <p>Used by {@code PropertyFormView}'s bottom Properties tabs (Phase E):
 * <ul>
 *   <li>Description tab — {@link Entry#description} + {@link Entry#introduction}</li>
 *   <li>Definition tab — {@link Entry#typeText} (incl. MIN/MAX/DEFAULT-VALUE)</li>
 *   <li>Status tab — runtime info, computed by the view (configured value,
 *       dirty flag, derived value)</li>
 * </ul>
 */
public final class MemIfParamMetadata {

    public static final class Entry {
        public final String shortName;
        public final String description;
        public final String introduction;
        public final String typeText;
        public final String origin;
        public final String defaultValue;

        Entry(String shortName, String description, String introduction,
              String typeText, String origin, String defaultValue) {
            this.shortName = shortName;
            this.description = description;
            this.introduction = introduction;
            this.typeText = typeText;
            this.origin = origin;
            this.defaultValue = defaultValue;
        }
    }

    private static final Map<String, Entry> ENTRIES = new LinkedHashMap<>();

    static {
        ENTRIES.put("MemIfDevErrorDetect", new Entry(
                "MemIfDevErrorDetect",
                "Switches the development error detection and notification on or off.",
                "* true: detection and notification is enabled. * false: detection and notification is disabled.",
                "ECUC-BOOLEAN-PARAM-DEF (default = false)",
                "AUTOSAR_ECUC",
                "false"));

        ENTRIES.put("MemIfNumberOfDevices", new Entry(
                "MemIfNumberOfDevices",
                "Concrete number of underlying memory abstraction modules.",
                "Calculation Formula: Count number of configured EA and FEE modules.",
                "ECUC-INTEGER-PARAM-DEF (MIN = 1, MAX = 2)",
                "AUTOSAR_ECUC",
                "(no default; derived from NvM EA/FEE block references)"));

        ENTRIES.put("MemIfVersionInfoApi", new Entry(
                "MemIfVersionInfoApi",
                "Pre-processor switch to enable / disable the API to read out the modules version information.",
                "true: Version info API enabled. false: Version info API disabled.",
                "ECUC-BOOLEAN-PARAM-DEF (default = false)",
                "AUTOSAR_ECUC",
                "false"));

        ENTRIES.put("MemIfModuleVersion", new Entry(
                "MemIfModuleVersion",
                "PROBE PARAMETER: experimental string to verify whether jar's MemIfDef.arxml drives the IDE form and whether the value reaches generated code.",
                "Vendor extension — kept across Phase A→F as a sanity probe (docs §15 patch).",
                "ECUC-STRING-PARAM-DEF",
                "VENDOR",
                "TEST_PROBE_42_V25_10"));
    }

    /** Look up metadata for a MemIfGeneral parameter by its short name. */
    public static Entry get(String shortName) {
        return ENTRIES.get(shortName);
    }

    /** Defensive — used by tests / debug listings. */
    public static Iterable<Entry> all() {
        return ENTRIES.values();
    }

    private MemIfParamMetadata() {}
}

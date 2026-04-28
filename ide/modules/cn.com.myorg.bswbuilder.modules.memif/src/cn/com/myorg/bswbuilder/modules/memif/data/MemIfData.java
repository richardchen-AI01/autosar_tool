package cn.com.myorg.bswbuilder.modules.memif.data;

/**
 * Plain-Java holder for the 4 MemIfGeneral parameters surfaced by Phase A.
 *
 * <p>Read-only on purpose — Phase A is "只读看". Phase B will add a mutable
 * counterpart wired through an EMF EditingDomain.
 *
 * <p>The fields are stored as String to preserve the exact textual value
 * from the ARXML (e.g. "false" / "true" for booleans, the integer literal
 * for {@code MemIfNumberOfDevices}, the raw string for the vendor probe).
 * Conversion to typed values is the consumer's responsibility.
 */
public final class MemIfData {

    private final String sourcePath;
    private final String memIfDevErrorDetect;
    private final String memIfNumberOfDevices;
    private final String memIfVersionInfoApi;
    private final String memIfModuleVersion;

    public MemIfData(String sourcePath,
                     String memIfDevErrorDetect,
                     String memIfNumberOfDevices,
                     String memIfVersionInfoApi,
                     String memIfModuleVersion) {
        this.sourcePath = sourcePath;
        this.memIfDevErrorDetect = memIfDevErrorDetect;
        this.memIfNumberOfDevices = memIfNumberOfDevices;
        this.memIfVersionInfoApi = memIfVersionInfoApi;
        this.memIfModuleVersion = memIfModuleVersion;
    }

    public String getSourcePath() { return sourcePath; }
    public String getMemIfDevErrorDetect() { return memIfDevErrorDetect; }
    public String getMemIfNumberOfDevices() { return memIfNumberOfDevices; }
    public String getMemIfVersionInfoApi() { return memIfVersionInfoApi; }
    public String getMemIfModuleVersion() { return memIfModuleVersion; }
}

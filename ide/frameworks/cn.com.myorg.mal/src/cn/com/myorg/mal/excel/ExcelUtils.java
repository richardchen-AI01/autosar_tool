package cn.com.myorg.mal.excel;

import java.util.Collections;
import java.util.Map;

/**
 * Stub — reference reads {@code osinfo.xls} (in install root) to populate
 * MCU metadata via Apache POI. v0.2 deliberate divergence: no Excel
 * dependency. Returns empty map → AutocoreCoordinator.getMCUs() falls
 * through to the {@code mcu} extension point only.
 *
 * <p>Reference: cn.com.isoft.mal.excel.ExcelUtils +
 * cn.com.isoft.mal.excel.entity.OsInfoEntity. Restoring full Excel-driven
 * MCU population is a separate phase if/when osinfo.xls becomes a useful
 * data source for our project (currently the {@code mcu} extension point
 * carries everything we need).
 */
public final class ExcelUtils {
    private ExcelUtils() {}

    /** Reference returns Map&lt;String, OsInfoEntity&gt;; we return empty Map. */
    public static Map<String, Object> getAllOsInfoEntity() {
        return Collections.emptyMap();
    }
}

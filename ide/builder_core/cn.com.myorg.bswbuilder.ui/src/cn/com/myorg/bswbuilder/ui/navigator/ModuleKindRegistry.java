package cn.com.myorg.bswbuilder.ui.navigator;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

/**
 * AUTOSAR BSW module → "kind" group mapping. Mirrors the 12 kinds iSoft
 * V25.10 declares in their {@code modulekind} extension point (verified
 * from {@code ui-extracted/plugin.xml}):
 *
 * <pre>
 *   SYS    System Service
 *   COM    Communication
 *   SEC    Security
 *   NM     Network Management
 *   DIAG   Diagnosis
 *   WDG    Wdg, WdgIf and WdgM
 *   MEM    Memory
 *   ETHER  Ethernet
 *   MCAL   Microcontroller
 *   OTHERS Others
 *   CRYPTO CRYPTO Service
 *   CDD    CDD
 * </pre>
 *
 * <p>Module-to-kind mapping is best-effort; only MemIf → MEM is
 * authoritative for v0.1. Other modules are mapped per AUTOSAR R23-11
 * naming conventions and may need correction once we cross-check against
 * iSoft's actual per-module {@code <module kind="…"/>} declarations
 * (recorded as a v0.2 follow-up task).
 */
public final class ModuleKindRegistry {

    /** Kinds in the order iSoft displays them. */
    public static final String[] KINDS = {
        "COM", "DIAG", "MCAL", "MEM", "SEC", "SYS",
        "WDG", "ETHER", "CRYPTO", "NM", "CDD", "OTHERS"
    };

    private static final Map<String, String> MAP;
    static {
        Map<String, String> m = new HashMap<>();
        // COM
        for (String n : new String[] {"CanIf","CanNm","CanSM","CanTp","Com","ComM",
                                       "EcuC","Nm","PduR","SoAd","UdpNm","SecOC","Csm",
                                       "LinIf","LinSM","LinTp","Ipdu","IpduM","J1939Nm",
                                       "J1939Tp","J1939Rm","J1939Dcm","XCP","XcpOnEth"})
            m.put(n, "COM");
        // DIAG
        for (String n : new String[] {"Dem","Dcm","FiM","Dlt"}) m.put(n, "DIAG");
        // MCAL
        for (String n : new String[] {"Mcu","Port","Spi","Adc","Can","Pwm","Gpt","Dio",
                                       "Icu","Fls","Eep","Ramt","Crc","Cry","Lin","Eth"})
            m.put(n, "MCAL");
        // WDG
        for (String n : new String[] {"Wdg","WdgIf","WdgM"}) m.put(n, "WDG");
        // MEM
        for (String n : new String[] {"MemIf","Fee","Ea","NvM","MemMap","MemLayout"})
            m.put(n, "MEM");
        // SYS
        for (String n : new String[] {"BswM","Det","EcuM","Os","Rte","StbM","Tm",
                                       "Ipdum","SchM","iRte","Xfrm"})
            m.put(n, "SYS");
        // ETHER
        for (String n : new String[] {"EthIf","EthSM","EthTSyn","TcpIp","SoAdEth","Dhcp"})
            m.put(n, "ETHER");
        MAP = Collections.unmodifiableMap(m);
    }

    private ModuleKindRegistry() {}

    /** Module name (e.g. "MemIf") → kind ("MEM"); unknown modules → "OTHERS". */
    public static String kindOf(String moduleName) {
        return MAP.getOrDefault(moduleName, "OTHERS");
    }

    /** Strip a trailing ".arxml" (case-insensitive). */
    public static String stripArxml(String fileName) {
        if (fileName == null) return "";
        String lower = fileName.toLowerCase();
        return lower.endsWith(".arxml")
                ? fileName.substring(0, fileName.length() - ".arxml".length())
                : fileName;
    }
}

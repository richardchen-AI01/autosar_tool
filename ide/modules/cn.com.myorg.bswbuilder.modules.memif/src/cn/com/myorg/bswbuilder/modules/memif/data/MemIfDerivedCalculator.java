package cn.com.myorg.bswbuilder.modules.memif.data;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Computes the derived value of {@code MemIfNumberOfDevices} from the NvM
 * configuration in a workspace.
 *
 * <p>Per AUTOSAR R23-11 ECUC TPS:
 * <pre>
 *   MemIfNumberOfDevices = (configured-EA-module-count) + (configured-FEE-module-count)
 * </pre>
 * "configured" is detected by the presence of at least one
 * {@code NvMFeeRef} / {@code NvMEaRef} sub-container under any
 * {@code NvMTargetBlockReference}. See
 * {@code docs/reference/memif-derived-truth-table.md} for the C0–C3 truth table.
 *
 * <p>Implementation: regex scan for {@code <SHORT-NAME>NvMFeeRef</SHORT-NAME>}
 * (and {@code NvMEaRef}) inside the workspace's NvM ARXML file. We don't
 * fully DOM-parse — string-presence is sufficient for the boolean flag
 * because these names don't legitimately appear elsewhere in NvM.arxml
 * outside their instance container declarations.
 *
 * <p>Mirrors the Python {@code core/Common/.../MemIf/src/MemIf.py
 * derivedNumberOfDevices} property — both must agree on every fixture.
 */
public final class MemIfDerivedCalculator {

    private static final Pattern FEE_REF_DECL =
            Pattern.compile("<SHORT-NAME>NvMFeeRef</SHORT-NAME>");
    private static final Pattern EA_REF_DECL =
            Pattern.compile("<SHORT-NAME>NvMEaRef</SHORT-NAME>");

    private MemIfDerivedCalculator() {}

    /**
     * @param workspaceDir absolute path to the workspace root (the directory
     *        that contains {@code BSW_Builder/<MCU>/}).
     * @return derived MemIfNumberOfDevices value (0, 1 or 2). Returns 0 if
     *         no NvM.arxml is found anywhere in the workspace.
     */
    public static int calculateNumberOfDevices(String workspaceDir) throws IOException {
        Path nvmFile = locateNvmArxml(Paths.get(workspaceDir));
        if (nvmFile == null) {
            return 0;
        }
        String xml = new String(Files.readAllBytes(nvmFile), StandardCharsets.UTF_8);
        return calculateFromXml(xml);
    }

    /** Pure-string version; exposed for testing. */
    public static int calculateFromXml(String nvmArxmlContent) {
        boolean hasFee = FEE_REF_DECL.matcher(nvmArxmlContent).find();
        boolean hasEa  = EA_REF_DECL.matcher(nvmArxmlContent).find();
        return (hasFee ? 1 : 0) + (hasEa ? 1 : 0);
    }

    /**
     * Walk {@code <workspace>/BSW_Builder/<any>/NvM.arxml}. Returns null if
     * the workspace doesn't contain such a file.
     */
    private static Path locateNvmArxml(Path workspaceDir) throws IOException {
        Path bswBuilder = workspaceDir.resolve("BSW_Builder");
        if (!Files.isDirectory(bswBuilder)) {
            return null;
        }
        try (java.util.stream.Stream<Path> stream = Files.list(bswBuilder)) {
            for (Path mcuDir : (Iterable<Path>) stream::iterator) {
                if (!Files.isDirectory(mcuDir)) continue;
                Path candidate = mcuDir.resolve("NvM.arxml");
                if (Files.isRegularFile(candidate)) {
                    return candidate;
                }
            }
        }
        return null;
    }

    /** Convenience: derive given a path to MemIf.arxml itself. */
    public static int calculateForMemIfFile(String memIfArxmlPath) throws IOException {
        // <…>/BSW_Builder/<MCU>/MemIf.arxml → workspace dir = <…>
        File memIfFile = new File(memIfArxmlPath);
        File mcuDir = memIfFile.getParentFile();
        if (mcuDir == null) return 0;
        File bswBuilder = mcuDir.getParentFile();
        if (bswBuilder == null) return 0;
        File workspace = bswBuilder.getParentFile();
        if (workspace == null) return 0;
        return calculateNumberOfDevices(workspace.getAbsolutePath());
    }

    /** Quick convenience for log output. */
    public static String describe(int derived) {
        switch (derived) {
            case 0: return "0 (C0 — no NV backends configured)";
            case 1: return "1 (C1 or C2 — single backend)";
            case 2: return "2 (C3 — both Fee + Ea)";
            default: return Integer.toString(derived);
        }
    }
}

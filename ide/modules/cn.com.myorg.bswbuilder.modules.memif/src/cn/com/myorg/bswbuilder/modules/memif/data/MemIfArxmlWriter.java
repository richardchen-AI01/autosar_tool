package cn.com.myorg.bswbuilder.modules.memif.data;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Surgical writer for the four MemIfGeneral parameters in an ARXML file.
 *
 * <p>Why string surgery instead of EMF/Sphinx serialization:
 * <ul>
 *   <li>Phase F's hard exit criterion is **byte-equal** ARXML round-trip
 *       between our IDE and ORIENTAIS V25.10. EMF's XMI serializer does
 *       <em>not</em> guarantee byte-level preservation of element order,
 *       indentation, namespace declarations, or comment formatting.</li>
 *   <li>String surgery only touches the {@code <VALUE>...</VALUE>} text node
 *       inside the targeted parameter; every other byte is preserved exactly.</li>
 *   <li>EditingDomain features we'd lose (undo/redo, multi-resource refactor)
 *       are not yet needed in v0.1.</li>
 * </ul>
 *
 * <p>The pattern matches an ECUC-NUMERICAL-PARAM-VALUE or
 * ECUC-TEXTUAL-PARAM-VALUE block whose DEFINITION-REF ends with the requested
 * parameter short name, then captures-and-replaces only the inner content of
 * the very next {@code <VALUE>...</VALUE>} pair. Whitespace, attributes, and
 * surrounding markup are preserved.
 */
public final class MemIfArxmlWriter {

    /**
     * Replace the &lt;VALUE&gt; payload of the named MemIfGeneral parameter
     * in-place. Reads file → regex-replaces → writes back to the same path.
     *
     * @param path           absolute filesystem path to the .arxml
     * @param paramShortName one of {@code MemIfDevErrorDetect},
     *                       {@code MemIfNumberOfDevices},
     *                       {@code MemIfVersionInfoApi},
     *                       {@code MemIfModuleVersion}
     * @param newValue       the new payload (verbatim — caller is responsible
     *                       for case / format conventions, e.g. "false" not "False")
     * @return true if exactly one matching block was found and replaced;
     *         false if zero blocks matched (no write performed)
     * @throws IllegalStateException if more than one matching block exists
     *         (we don't silently overwrite all copies — caller must disambiguate)
     */
    public static boolean writeParam(String path, String paramShortName, String newValue)
            throws IOException {
        if (isReferenceProjectPath(path)) {
            throw new IOException(
                    "拒绝写入参考项目: " + path + "\n"
                  + "ORIENTAIS_Studio / 参考工程是只读对照基准；要修改请先把工程整体复制到\n"
                  + "D:\\autosar_tool 下面或其他自有目录再操作。\n"
                  + "(防止 V25.10 验收基准被破坏 — feedback_never_modify_reference)");
        }
        Path file = Paths.get(path);
        String original = new String(Files.readAllBytes(file), StandardCharsets.UTF_8);
        String updated = replaceParamValue(original, paramShortName, newValue);
        if (updated.equals(original)) {
            return false;
        }
        Files.write(file, updated.getBytes(StandardCharsets.UTF_8));
        return true;
    }

    /**
     * Path-based safety guard: refuses to write under known reference roots
     * so a Save-from-FormEditor on an inadvertently-opened reference ARXML
     * doesn't corrupt the V25.10 byte-equal baseline. Triggers on substring
     * match (case-insensitive) for any common reference location:
     * <ul>
     *   <li>{@code ORIENTAIS_Studio} (Win install)</li>
     *   <li>{@code ORIENTAIS_Configurator} (alt install layout)</li>
     *   <li>{@code docs/reference/} (in-repo reference fixtures)</li>
     * </ul>
     * Working copies must live elsewhere (typically {@code samples/} or a
     * user-chosen workspace).
     */
    static boolean isReferenceProjectPath(String path) {
        if (path == null) return false;
        String lower = path.replace('\\', '/').toLowerCase();
        return lower.contains("/orientais_studio/")
            || lower.contains("/orientais_configurator")
            || lower.contains("/docs/reference/")
            // autosar_tool/samples/ 是 git 管的 fixture baseline。算法测试
            // (test_memif_full + pytest) 都基于这个 baseline，IDE Save 写入
            // 会污染 baseline 让 test 挂 (反复犯过, 2026-04-30 用户 D:\bswbuilder
            // IDE 改了 MemIfDevErrorDetect false→true 导致 generator 出 macros
            // 缺失)。
            // 部署专属 workspace D:\bswbuilderN\workspace\... 不会命中这条
            // (路径含 /bswbuilder<N>/ 不含 /samples/)。
            || lower.contains("/autosar_tool/samples/");
    }

    /**
     * Pure function (no I/O) — exposed for unit testing the string surgery
     * without touching the filesystem.
     */
    public static String replaceParamValue(String xml, String paramShortName, String newValue) {
        // Pattern: an ECUC-(NUMERICAL|TEXTUAL)-PARAM-VALUE block whose DEFINITION-REF
        // ends with /<paramShortName></DEFINITION-REF>, followed by a <VALUE>...</VALUE>
        // pair. Capture group 1 is the prefix up to and including <VALUE>, group 2
        // is the existing payload, group 3 is the closing </VALUE>.
        String regex =
                "(<ECUC-(?:NUMERICAL|TEXTUAL)-PARAM-VALUE>" +
                "\\s*<DEFINITION-REF[^>]*>[^<]*?/" +
                Pattern.quote(paramShortName) +
                "</DEFINITION-REF>" +
                "\\s*<VALUE>)([^<]*)(</VALUE>)";

        Pattern p = Pattern.compile(regex, Pattern.DOTALL);
        Matcher m = p.matcher(xml);

        int matchCount = 0;
        StringBuilder result = new StringBuilder();
        int last = 0;
        while (m.find()) {
            matchCount++;
            if (matchCount > 1) {
                throw new IllegalStateException(
                        "Multiple <VALUE> blocks match parameter '" + paramShortName +
                        "'. Caller must disambiguate (e.g. by container path).");
            }
            result.append(xml, last, m.start());
            result.append(m.group(1));
            result.append(escapeXmlText(newValue));
            result.append(m.group(3));
            last = m.end();
        }
        if (matchCount == 0) {
            return xml; // no match → caller decides whether to error
        }
        result.append(xml, last, xml.length());
        return result.toString();
    }

    private static String escapeXmlText(String s) {
        // Minimal XML text escaping. <VALUE> contents in our ARXML files are
        // boolean literals / integer literals / probe strings — none of which
        // contain XML metacharacters in normal use. Escape defensively anyway.
        return s.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;");
    }

    private MemIfArxmlWriter() {
        // utility class
    }
}

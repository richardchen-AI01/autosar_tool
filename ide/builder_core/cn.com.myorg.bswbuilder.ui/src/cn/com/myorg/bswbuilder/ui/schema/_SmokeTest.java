package cn.com.myorg.bswbuilder.ui.schema;

import java.io.File;

/**
 * Smoke test for {@link BswmdSchemaReader} — runs from the command line:
 *
 * <pre>
 *   javac -d /tmp/cls $(find ide/builder_core/cn.com.myorg.bswbuilder.ui/src/cn/com/myorg/bswbuilder/ui/schema -name '*.java')
 *   java -cp /tmp/cls cn.com.myorg.bswbuilder.ui.schema._SmokeTest \
 *        ide/modules/cn.com.myorg.bswbuilder.modules.memif/MemIfDef.arxml
 * </pre>
 *
 * <p>Not registered as a JUnit test in v0.1 (the {@code .ui} bundle has no
 * test sources yet); this is a quick manual smoke. M2 brings JUnit-Tycho.
 */
public final class _SmokeTest {

    public static void main(String[] args) throws Exception {
        if (args.length == 0) {
            System.err.println("usage: _SmokeTest <path-to-XxxDef.arxml> [more...]");
            System.exit(2);
        }
        for (String a : args) {
            File f = new File(a);
            System.out.println("=== " + f + " ===");
            ModuleSchema schema = BswmdSchemaReader.parse(f);
            System.out.println("module: " + schema.moduleName);
            for (ContainerSchema c : schema.containers) {
                printContainer(c, 1);
            }
        }
    }

    private static void printContainer(ContainerSchema c, int depth) {
        String ind = repeat("  ", depth);
        System.out.println(ind + "container " + c.shortName
                + " [" + c.lowerMultiplicity + ".." + (c.upperMultiplicity == -1 ? "*" : String.valueOf(c.upperMultiplicity)) + "]"
                + (c.generalFlag ? " GENERAL_FLAG" : "")
                + (c.choiceContainer ? " CHOICE" : "")
                + (c.params.size() > 0 ? "  (" + c.params.size() + " params)" : "")
                + (c.subContainers.size() > 0 ? "  (" + c.subContainers.size() + " subs)" : ""));
        for (ParamSchema p : c.params) {
            System.out.println(ind + "  param " + p);
        }
        for (ContainerSchema sc : c.subContainers) {
            printContainer(sc, depth + 1);
        }
    }

    private static String repeat(String s, int n) {
        StringBuilder sb = new StringBuilder(s.length() * n);
        for (int i = 0; i < n; i++) sb.append(s);
        return sb.toString();
    }
}

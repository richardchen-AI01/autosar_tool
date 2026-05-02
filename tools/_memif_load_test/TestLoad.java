// tools/_memif_load_test/TestLoad.java — direct integration probe for the
// A0 fix: load a real ARXML file via MemIfArxmlReader's same code path and
// assert (a) no FeatureNotFoundException, (b) the 4 expected values come
// back. Run via tools/test_memif_phase_a0.sh which constructs the right
// classpath from the built RCP launcher's plugins/.

import java.lang.reflect.Method;

public class TestLoad {
    public static void main(String[] args) throws Exception {
        if (args.length < 1) {
            System.err.println("Usage: TestLoad <path-to-MemIf.arxml>");
            System.exit(2);
        }

        String path = args[0];
        System.out.println("[TestLoad] path = " + path);

        // Load via reflection so this class doesn't have a hard import on
        // our memif bundle's package — keeps the build standalone.
        Class<?> readerCls = Class.forName(
                "cn.com.myorg.bswbuilder.modules.memif.data.MemIfArxmlReader");
        Method readM = readerCls.getMethod("read", String.class);
        Object data = null;
        try {
            data = readM.invoke(null, path);
        } catch (Throwable t) {
            Throwable cause = t.getCause() != null ? t.getCause() : t;
            System.err.println("[TestLoad] FAIL — exception during load: "
                    + cause.getClass().getName() + ": " + cause.getMessage());
            cause.printStackTrace();
            System.exit(1);
            return;  // unreachable but keeps the compiler happy
        }

        Class<?> dataCls = data.getClass();
        String dev  = (String) dataCls.getMethod("getMemIfDevErrorDetect").invoke(data);
        String num  = (String) dataCls.getMethod("getMemIfNumberOfDevices").invoke(data);
        String vapi = (String) dataCls.getMethod("getMemIfVersionInfoApi").invoke(data);
        String mver = (String) dataCls.getMethod("getMemIfModuleVersion").invoke(data);

        System.out.println("[TestLoad] DevErrorDetect      = " + dev);
        System.out.println("[TestLoad] NumberOfDevices     = " + num);
        System.out.println("[TestLoad] VersionInfoApi      = " + vapi);
        System.out.println("[TestLoad] ModuleVersion       = " + mver);

        // Demo_S32K148 expected values
        boolean ok = "false".equals(dev)
                  && "2".equals(num)
                  && "false".equals(vapi)
                  && "TEST_PROBE_42_V25_10".equals(mver);
        if (ok) {
            System.out.println("[TestLoad] PASS — 4/4 values match expected");
            System.exit(0);
        } else {
            System.err.println("[TestLoad] FAIL — value mismatch");
            System.exit(1);
        }
    }
}

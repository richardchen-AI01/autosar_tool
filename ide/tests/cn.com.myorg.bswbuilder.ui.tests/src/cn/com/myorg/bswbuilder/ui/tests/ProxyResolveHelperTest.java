package cn.com.myorg.bswbuilder.ui.tests;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;

import java.lang.reflect.Method;

import org.eclipse.emf.common.util.URI;
import org.junit.Test;

import cn.com.myorg.bswbuilder.ui.editor.utils.ProxyResolveHelper;

/**
 * Pure-function regression test for ARTOP proxy URI parsing.
 *
 * <p>Real proxy URIs seen in N=52 log:
 * {@code ar:/#/AUTOSAR/NvM/NvMBlockDescriptor?type=EcucParamConfContainerDef}.
 * If parsing of the {@code ?type=...} suffix or AR-path leaf segment breaks,
 * {@link ProxyResolveHelper#resolve} silently can't find a match and the
 * detail panel shows no parameters — root cause of "字段不显示".
 */
public class ProxyResolveHelperTest {

    @Test
    public void parseTypeQuery_extractsEClassName() throws Exception {
        URI u = URI.createURI("ar:/#/AUTOSAR/NvM/NvMBlockDescriptor?type=EcucParamConfContainerDef");
        assertEquals("EcucParamConfContainerDef", invokeParseType(u));
    }

    @Test
    public void parseTypeQuery_returnsNullWhenNoTypeQuery() throws Exception {
        URI u = URI.createURI("ar:/#/AUTOSAR/NvM/NvMBlockDescriptor");
        assertNull(invokeParseType(u));
    }

    @Test
    public void parseTypeQuery_stripsTrailingAmpersand() throws Exception {
        URI u = URI.createURI("ar:/#/AUTOSAR/NvM/NvMBlockDescriptor?type=EcucParamConfContainerDef&extra=x");
        assertEquals("EcucParamConfContainerDef", invokeParseType(u));
    }

    @Test
    public void leafSegment_returnsLastPathPart() throws Exception {
        assertEquals("NvMBlockDescriptor",
                invokeLeaf("/AUTOSAR/NvM/NvMBlockDescriptor?type=EcucParamConfContainerDef"));
    }

    @Test
    public void leafSegment_handlesNoQuery() throws Exception {
        assertEquals("NvMCommon", invokeLeaf("/AUTOSAR/NvM/NvMCommon"));
    }

    @Test
    public void leafSegment_handlesNoSlash() throws Exception {
        assertEquals("NvMBlockDescriptor", invokeLeaf("NvMBlockDescriptor"));
    }

    @Test
    public void leafSegment_returnsNullForEmpty() throws Exception {
        assertNull(invokeLeaf(""));
        assertNull(invokeLeaf(null));
    }

    private static String invokeParseType(URI u) throws Exception {
        Method m = ProxyResolveHelper.class.getDeclaredMethod("parseTypeQuery", URI.class);
        m.setAccessible(true);
        return (String) m.invoke(null, u);
    }

    private static String invokeLeaf(String fragment) throws Exception {
        Method m = ProxyResolveHelper.class.getDeclaredMethod("leafSegment", String.class);
        m.setAccessible(true);
        return (String) m.invoke(null, fragment);
    }
}

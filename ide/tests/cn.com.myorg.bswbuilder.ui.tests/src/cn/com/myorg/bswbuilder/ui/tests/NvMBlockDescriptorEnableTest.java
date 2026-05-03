package cn.com.myorg.bswbuilder.ui.tests;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

import org.eclipse.emf.ecore.EObject;
import org.junit.Test;

import cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions.NvMBlockDescriptorEnable;
import gautosar.gecucdescription.GContainer;

/**
 * Reproduce + regression test for bug "不同 NvMBlockDescriptors 显示的
 * Del/Copy/Rename 都一样".
 *
 * <p>Reference reverseuidefinition behavior — NvMBlock_ConfigID 是系统保留
 * 的 ConfigID instance, 不允许 Del/Copy/Rename. 其他 NvMBlock_* 全允许.
 */
public class NvMBlockDescriptorEnableTest {

    /**
     * Bug 1 reproduce: NvMBlock_ConfigID instance 应**禁止** Del/Copy/Rename.
     */
    @Test
    public void testConfigID_NoDelCopyRename() {
        NvMBlockDescriptorEnable enable = new NvMBlockDescriptorEnable();
        EObject configId = mockContainer("NvMBlock_ConfigID");
        assertFalse("NvMBlock_ConfigID should NOT permit Del", enable.permitDel(configId));
        assertFalse("NvMBlock_ConfigID should NOT permit Duplicate", enable.permitDuplicate(configId));
        assertFalse("NvMBlock_ConfigID should NOT permit Rename", enable.permitRename(configId));
    }

    /**
     * Bug 2 regression: NvMBlock_Primary_0 (普通 instance) 应**允许** Del/Copy/Rename.
     */
    @Test
    public void testPrimary0_AllPermitted() {
        NvMBlockDescriptorEnable enable = new NvMBlockDescriptorEnable();
        EObject primary0 = mockContainer("NvMBlock_Primary_0");
        assertTrue("NvMBlock_Primary_0 should permit Del", enable.permitDel(primary0));
        assertTrue("NvMBlock_Primary_0 should permit Duplicate", enable.permitDuplicate(primary0));
        assertTrue("NvMBlock_Primary_0 should permit Rename", enable.permitRename(primary0));
    }

    /**
     * Edge: 任何非 ConfigID 的 NvMBlock_* 都允许 (含 SecurityLevel / DIDF / Custom name).
     */
    @Test
    public void testNonConfigID_AllPermitted() {
        NvMBlockDescriptorEnable enable = new NvMBlockDescriptorEnable();
        for (String name : new String[] {
                "NvMBlock_SecurityLevel01", "NvMBlock_DIDF190", "MyCustomBlock", "" }) {
            EObject obj = mockContainer(name);
            assertTrue("'" + name + "' should permit Del", enable.permitDel(obj));
        }
    }

    /**
     * Mock GContainer + EObject dual-interface via dynamic proxy — only
     * gGetShortName is meaningful, all other methods return null/false/0.
     */
    private static EObject mockContainer(final String shortName) {
        return (EObject) Proxy.newProxyInstance(
                NvMBlockDescriptorEnableTest.class.getClassLoader(),
                new Class<?>[] { GContainer.class, EObject.class },
                new InvocationHandler() {
                    @Override
                    public Object invoke(Object proxy, Method method, Object[] args) {
                        if ("gGetShortName".equals(method.getName())) {
                            return shortName;
                        }
                        if (method.getReturnType() == boolean.class) return Boolean.FALSE;
                        if (method.getReturnType() == int.class) return Integer.valueOf(0);
                        return null;
                    }
                });
    }
}

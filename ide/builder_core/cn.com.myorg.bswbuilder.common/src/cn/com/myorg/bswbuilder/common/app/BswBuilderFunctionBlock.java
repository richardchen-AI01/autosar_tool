package cn.com.myorg.bswbuilder.common.app;

import org.eclipse.core.resources.IProject;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.swt.graphics.Image;

import cn.com.myorg.pal.base.interfaces.common.IFunctionBlock;

/**
 * Reference: registered as the BSW function block in iSoft's
 * cn.com.isoft.bswbuilder.common plugin.xml — pal.ModelManager keys off
 * its id ({@code "cn.com.isoft.bsw.funcId"} in reference) to decide whether
 * a project is a managed BSW project.
 *
 * <p>For us the gate id is {@value #FUNC_ID}; ModelManager.getBswBuilderByProject
 * returns null if no IFunctionBlock with this id is registered.
 *
 * <p>Other IFunctionBlock methods are stubs in v0.2 — drop-and-drop / image /
 * order are UI features (drag from Validation/Detail palettes etc.) that
 * we don't yet wire up.
 */
public class BswBuilderFunctionBlock implements IFunctionBlock {

    public static final String FUNC_ID = "cn.com.myorg.bsw.funcId";

    @Override
    public String getId() { return FUNC_ID; }

    @Override
    public String getName() { return "BSW Builder"; }

    @Override
    public int getOrder() { return 0; }

    @Override
    public Image getImage() { return null; }

    @Override
    public Object getFuncBlockContent(IProject project) { return null; }

    @Override
    public IStatus doDrop(IProject project, Object data) { return Status.OK_STATUS; }

    @Override
    public boolean receiveDrop() { return false; }

    @Override
    public void initialize() { /* no-op for v0.2 */ }
}

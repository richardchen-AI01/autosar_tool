package cn.com.myorg.pal.base.interfaces.common;

import org.eclipse.core.resources.IProject;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.swt.graphics.Image;

public interface IFunctionBlock {
    public String getId();

    public String getName();

    public int getOrder();

    public Image getImage();

    public Object getFuncBlockContent(IProject var1);

    public IStatus doDrop(IProject var1, Object var2);

    public boolean receiveDrop();

    public void initialize();
}

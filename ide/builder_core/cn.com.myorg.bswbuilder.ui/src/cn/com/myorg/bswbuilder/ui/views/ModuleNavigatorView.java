package cn.com.myorg.bswbuilder.ui.views;

import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.jface.viewers.LabelProvider;
import org.eclipse.jface.viewers.TreeViewer;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.ui.part.ViewPart;

/**
 * Left-hand-side BSW module navigator.
 *
 * <p>v0.1 shows a static tree:<br>
 * <code>
 *   Project<br>
 *   └── BSW<br>
 *       └── MemIf
 * </code>
 *
 * <p>v0.2 will populate from the loaded ECUC project (see
 * {@code core/Common/arxmlparse/loader.py} on the Python side; the IDE will
 * shell out via {@link cn.com.myorg.bswbuilder.ui.launcher.BswgenLauncher} to
 * a future {@code bswgen --list-modules} sub-command).
 */
public class ModuleNavigatorView extends ViewPart {

    public static final String ID = "cn.com.myorg.bswbuilder.ui.views.ModuleNavigator";

    private TreeViewer viewer;

    @Override
    public void createPartControl(Composite parent) {
        viewer = new TreeViewer(parent, SWT.H_SCROLL | SWT.V_SCROLL);
        viewer.setContentProvider(new StaticContentProvider());
        viewer.setLabelProvider(new LabelProvider() {
            @Override
            public String getText(Object element) {
                return element == null ? "" : element.toString();
            }
        });
        viewer.setInput(new String[]{"Project / BSW / MemIf"});
    }

    @Override
    public void setFocus() {
        if (viewer != null) {
            viewer.getControl().setFocus();
        }
    }

    private static final class StaticContentProvider implements ITreeContentProvider {
        @Override
        public Object[] getElements(Object input) {
            return new Object[]{"Project", "  BSW", "    MemIf  ✓ ready"};
        }

        @Override public Object[] getChildren(Object parent) { return new Object[0]; }
        @Override public Object   getParent(Object child)    { return null; }
        @Override public boolean  hasChildren(Object parent) { return false; }
    }
}

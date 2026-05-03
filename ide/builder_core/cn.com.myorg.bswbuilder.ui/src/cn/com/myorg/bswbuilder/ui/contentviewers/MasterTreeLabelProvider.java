package cn.com.myorg.bswbuilder.ui.contentviewers;

import org.eclipse.jface.viewers.LabelProvider;
import org.eclipse.swt.graphics.Image;
import org.eclipse.ui.ISharedImages;
import org.eclipse.ui.PlatformUI;

import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;

/**
 * Master tree label provider. 字面跟参考 V25.10
 * {@code MasterFormSection$TreeLabelProvider.getText} (line 71-78) 对齐:
 *
 * <ul>
 *   <li>{@link GModuleConfiguration} → {@code shortName}</li>
 *   <li>{@link GContainer}           → {@code shortName} (实例节点 NvMBlock_Primary_0)</li>
 *   <li>{@link TreeChildWrap}        → {@code defShortName + "s"} (顶层 folder NvMBlockDescriptors)</li>
 *   <li>{@link ChildContainerGroup}  → {@code defShortName + "s (" + count + ")"} (子级 folder + 子数)</li>
 *   <li>{@link TableDataContainer}   → {@code defShortName} (table 行)</li>
 * </ul>
 *
 * Image: folder vs file — 用 Eclipse 标准 ISharedImages (v0.2 不复刻 iSoft 自定义图标)。
 */
public class MasterTreeLabelProvider extends LabelProvider {

    @Override public String getText(Object element) {
        if (element instanceof GModuleConfiguration) {
            return ((GModuleConfiguration) element).gGetShortName();
        }
        if (element instanceof GContainer) {
            String n = ((GContainer) element).gGetShortName();
            return n == null || n.isEmpty() ? "<unnamed>" : n;
        }
        if (element instanceof TreeChildWrap) {
            return ((TreeChildWrap) element).getContainerDef().gGetShortName() + "s";
        }
        if (element instanceof ChildContainerGroup) {
            ChildContainerGroup g = (ChildContainerGroup) element;
            int count = g.getElementList().size();
            return g.getContainerDef().gGetShortName() + "s (" + count + ")";
        }
        if (element instanceof TableDataContainer) {
            return ((TableDataContainer) element).getContainerDef().gGetShortName();
        }
        return String.valueOf(element);
    }

    @Override public Image getImage(Object element) {
        ISharedImages shared = PlatformUI.getWorkbench().getSharedImages();
        if (element instanceof TreeChildWrap || element instanceof ChildContainerGroup) {
            return shared.getImage(ISharedImages.IMG_OBJ_FOLDER);
        }
        if (element instanceof GContainer) {
            return shared.getImage(ISharedImages.IMG_OBJ_FILE);
        }
        return null;
    }
}

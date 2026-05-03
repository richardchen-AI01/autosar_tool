package cn.com.myorg.bswbuilder.ui.contentviewers;

import java.util.ArrayList;
import java.util.List;

import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.jface.viewers.Viewer;

import gautosar.gecucdescription.GContainer;
import gautosar.gecucparameterdef.GContainerDef;
import gautosar.gecucparameterdef.GParamConfContainerDef;

/**
 * Master tree content provider. 输入是 {@link TreeChildWrap} (顶层 wrapper),
 * 子层级:
 *
 * <pre>
 * Root level     :  [TreeChildWrap]                  ("NvMBlockDescriptors")
 *  ├ TreeChildWrap children : List<GContainer>      (instance NvMBlock_Primary_0 ...)
 *      ├ GContainer children: List<ChildContainerGroup>  (per sub-def, 即使 0 实例)
 *           ├ ChildContainerGroup children: List<GContainer> (sub-instance)
 * </pre>
 *
 * 跟参考 V25.10 {@code MasterFormSection$ContentProvider.getChildren} dispatch
 * (line 54-145) 同款层级, 简化掉 ValueContainer / TableFlag / SubContainer 多分支 (v0.2 first cut)。
 */
public class MasterTreeContentProvider implements ITreeContentProvider {

    @Override public Object[] getElements(Object input) {
        if (input instanceof TreeChildWrap) {
            return new Object[] { input };
        }
        if (input instanceof List) {
            return ((List<?>) input).toArray();
        }
        return new Object[0];
    }

    @Override public Object[] getChildren(Object element) {
        if (element instanceof TreeChildWrap) {
            return ((TreeChildWrap) element).getChildItemList().toArray();
        }
        if (element instanceof GContainer) {
            // 每个 sub-def 一个 ChildContainerGroup 节点 (即使 0 实例, 跟参考一致 — folder 节点恒在)
            GContainer container = (GContainer) element;
            GContainerDef def = container.gGetDefinition();
            if (def instanceof GParamConfContainerDef) {
                List<Object> out = new ArrayList<>();
                for (GContainerDef sub : ((GParamConfContainerDef) def).gGetSubContainers()) {
                    out.add(new ChildContainerGroup(container, sub));
                }
                return out.toArray();
            }
            return new Object[0];
        }
        if (element instanceof ChildContainerGroup) {
            return ((ChildContainerGroup) element).getElementList().toArray();
        }
        return new Object[0];
    }

    @Override public Object getParent(Object element) {
        if (element instanceof GContainer) {
            org.eclipse.emf.ecore.EObject p = ((org.eclipse.emf.ecore.EObject) element).eContainer();
            return p instanceof GContainer ? p : null;
        }
        if (element instanceof ChildContainerGroup) {
            return ((ChildContainerGroup) element).getParentContainer();
        }
        return null;
    }

    @Override public boolean hasChildren(Object element) {
        if (element instanceof TreeChildWrap) {
            return !((TreeChildWrap) element).getChildItemList().isEmpty();
        }
        if (element instanceof GContainer) {
            GContainerDef def = ((GContainer) element).gGetDefinition();
            return def instanceof GParamConfContainerDef
                    && !((GParamConfContainerDef) def).gGetSubContainers().isEmpty();
        }
        if (element instanceof ChildContainerGroup) {
            return !((ChildContainerGroup) element).getElementList().isEmpty();
        }
        return false;
    }

    @Override public void inputChanged(Viewer viewer, Object oldIn, Object newIn) {}
    @Override public void dispose() {}
}

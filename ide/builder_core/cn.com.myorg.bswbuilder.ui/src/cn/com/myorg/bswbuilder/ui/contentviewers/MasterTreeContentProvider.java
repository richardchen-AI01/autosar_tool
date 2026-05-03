package cn.com.myorg.bswbuilder.ui.contentviewers;

import java.util.ArrayList;
import java.util.List;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.jface.viewers.Viewer;

import cn.com.myorg.bswbuilder.ui.Activator;
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
            TreeChildWrap w = (TreeChildWrap) element;
            Object[] arr = w.getChildItemList().toArray();
            log("getChildren TreeChildWrap[" + w.getContainerDef().gGetShortName()
                    + "] -> " + arr.length + " GContainer instance(s)");
            return arr;
        }
        if (element instanceof GContainer) {
            GContainer container = (GContainer) element;
            GContainerDef def = container.gGetDefinition();
            String shortName = container.gGetShortName();
            String defName = def == null ? "<null def>" : def.gGetShortName();
            if (def instanceof GParamConfContainerDef) {
                List<GContainerDef> subDefs = ((GParamConfContainerDef) def).gGetSubContainers();
                List<Object> out = new ArrayList<>();
                for (GContainerDef sub : subDefs) {
                    out.add(new ChildContainerGroup(container, sub));
                }
                log("getChildren GContainer[" + shortName + " def=" + defName + "] -> "
                        + out.size() + " ChildContainerGroup(s)");
                return out.toArray();
            }
            log("getChildren GContainer[" + shortName + " def=" + defName + "] -> 0 (def not PARAM-CONF)");
            return new Object[0];
        }
        if (element instanceof ChildContainerGroup) {
            ChildContainerGroup g = (ChildContainerGroup) element;
            Object[] arr = g.getElementList().toArray();
            log("getChildren ChildContainerGroup[parent=" + g.getParentContainer().gGetShortName()
                    + " def=" + g.getContainerDef().gGetShortName() + "] -> " + arr.length + " sub-instance(s)");
            return arr;
        }
        log("getChildren UNKNOWN element class=" + element.getClass().getSimpleName() + " -> 0");
        return new Object[0];
    }

    private static void log(String msg) {
        try {
            Activator a = Activator.getDefault();
            if (a != null) {
                a.getLog().log(new Status(IStatus.INFO, Activator.PLUGIN_ID,
                        "[MasterTreeCP] " + msg));
            }
        } catch (Throwable ignored) { /* fallback silent */ }
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

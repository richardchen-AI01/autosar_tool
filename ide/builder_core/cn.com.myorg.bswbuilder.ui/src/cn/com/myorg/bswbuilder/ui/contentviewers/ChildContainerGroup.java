package cn.com.myorg.bswbuilder.ui.contentviewers;

import java.util.ArrayList;
import java.util.List;

import org.eclipse.emf.ecore.EObject;

import cn.com.myorg.bswbuilder.ui.editor.utils.ProxyResolveHelper;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucparameterdef.GContainerDef;

/**
 * Sub-folder node wrapping all instances of a sub-{@link GContainerDef} under
 * a parent {@link GContainer}.
 *
 * <p>跟参考 V25.10 {@code cn.com.isoft.bswbuilder.ui.contentviewers.ChildContainerGroup}
 * 同款 (orientais_studio decompile 同名类). 截图里 "NvMSingleBlockCallbacks (1)" /
 * "NvMTargetBlockReferences (1)" 这种带 (N) 子数标记的子级 folder 节点用此类。
 *
 * <p>label 由 {@link MasterTreeLabelProvider#getText} 输出
 * {@code defShortName + "s (" + count + ")"} (跟参考
 * MasterFormSection$TreeLabelProvider line 75-78 字面对齐)。
 */
public class ChildContainerGroup {

    private final GContainer parentContainer;
    private final GContainerDef containerDef;

    public ChildContainerGroup(GContainer parentContainer, GContainerDef containerDef) {
        this.parentContainer = parentContainer;
        this.containerDef = containerDef;
    }

    public GContainer getParentContainer() { return parentContainer; }
    public GContainerDef getContainerDef() { return containerDef; }

    /**
     * 返 parentContainer 下所有 def 等于 containerDef 的 sub-container 实例。
     * sub-instance.gGetDefinition() 在 ARTOP 跨 .arxml ECUC ref 上常是 unresolved
     * proxy → proxy.gGetShortName() 返空, 直接 equals 比较 mismatch (count 0).
     * 走 ProxyResolveHelper 强制 resolve 后比较, 跟 master tree 顶层同款修法。
     */
    public List<GContainer> getElementList() {
        List<GContainer> out = new ArrayList<>();
        if (parentContainer == null || containerDef == null) return out;
        String targetName = containerDef.gGetShortName();
        if (targetName == null) return out;
        for (GContainer sub : parentContainer.gGetSubContainers()) {
            GContainerDef subDef = sub.gGetDefinition();
            if (subDef == null) continue;
            if (((EObject) subDef).eIsProxy()) {
                EObject resolved = ProxyResolveHelper.resolve((EObject) subDef, sub);
                if (resolved instanceof GContainerDef) subDef = (GContainerDef) resolved;
            }
            String subName = subDef.gGetShortName();
            if (targetName.equals(subName)) {
                out.add(sub);
            }
        }
        return out;
    }

    @Override public int hashCode() {
        int h = 31 + (containerDef == null ? 0 : containerDef.hashCode());
        return 31 * h + (parentContainer == null ? 0 : parentContainer.hashCode());
    }

    @Override public boolean equals(Object other) {
        if (this == other) return true;
        if (!(other instanceof ChildContainerGroup)) return false;
        ChildContainerGroup o = (ChildContainerGroup) other;
        if (containerDef == null ? o.containerDef != null : !containerDef.equals(o.containerDef)) return false;
        return parentContainer == null ? o.parentContainer == null : parentContainer.equals(o.parentContainer);
    }
}

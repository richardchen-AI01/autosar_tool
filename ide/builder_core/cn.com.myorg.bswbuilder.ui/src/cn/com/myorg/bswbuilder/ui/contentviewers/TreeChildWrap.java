package cn.com.myorg.bswbuilder.ui.contentviewers;

import java.util.ArrayList;
import java.util.List;

import cn.com.myorg.bswbuilder.ui.editor.utils.EcuUtils;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;
import gautosar.gecucparameterdef.GContainerDef;

/**
 * Top-level "folder" node wrapping all instances of a top-level
 * {@link GContainerDef} under a {@link GModuleConfiguration}.
 *
 * <p>跟参考 V25.10 {@code cn.com.isoft.bswbuilder.ui.editor.section.TreeChildWrap}
 * 同款 (orientais_studio decompile reference 同名类), 顶层 master tree 渲染
 * "NvMBlockDescriptors" (复数 plural) folder 节点用此类。
 *
 * <p>label 由 {@link MasterTreeLabelProvider#getText} 输出 {@code defShortName + "s"}
 * (跟参考 MasterFormSection$TreeLabelProvider line 71-73 对齐)。
 */
public class TreeChildWrap {

    private final GModuleConfiguration moduleConf;
    private final GContainerDef containerDef;
    private final List<GContainer> lstChildItem;

    public TreeChildWrap(GModuleConfiguration moduleConf, GContainerDef containerDef) {
        this.moduleConf = moduleConf;
        this.containerDef = containerDef;
        this.lstChildItem = new ArrayList<>();
        if (moduleConf != null && containerDef != null) {
            // 跟参考一致: 遍历 module.gGetContainers, 用 EcuUtils 已对齐 def 的 containers
            for (GContainer c : EcuUtils.getContainersByDef(moduleConf, containerDef)) {
                lstChildItem.add(c);
            }
        }
    }

    public GContainerDef getContainerDef() { return containerDef; }
    public GModuleConfiguration getModuleConfiguration() { return moduleConf; }
    public List<GContainer> getChildItemList() { return lstChildItem; }

    public void addChildItem(GContainer item) { lstChildItem.add(item); }

    @Override public int hashCode() {
        int h = 31 + (containerDef == null ? 0 : containerDef.hashCode());
        return 31 * h + (moduleConf == null ? 0 : moduleConf.hashCode());
    }

    @Override public boolean equals(Object other) {
        if (this == other) return true;
        if (!(other instanceof TreeChildWrap)) return false;
        TreeChildWrap o = (TreeChildWrap) other;
        if (containerDef == null ? o.containerDef != null : !containerDef.equals(o.containerDef)) return false;
        return moduleConf == null ? o.moduleConf == null : moduleConf.equals(o.moduleConf);
    }
}

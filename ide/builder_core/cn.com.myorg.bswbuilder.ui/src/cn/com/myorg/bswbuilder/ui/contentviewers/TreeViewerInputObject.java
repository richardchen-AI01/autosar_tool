package cn.com.myorg.bswbuilder.ui.contentviewers;

import gautosar.gecucdescription.GModuleConfiguration;
import gautosar.gecucparameterdef.GContainerDef;

/**
 * 99% paraphrase of cn.com.isoft.bswbuilder.ui.editor.section.MasterFormSection
 * inner class TreeViewerInputObject (line 1109-1143).
 *
 * <p>1% divergence: extracted from inner class to top-level (host page is a
 * separate FormPage class in MEN, not MasterFormSection). Class structure
 * + fields + methods + equals/hashCode preserved 1:1.
 */
public class TreeViewerInputObject {
    private GModuleConfiguration moduleConf;
    private GContainerDef containerDef;

    public TreeViewerInputObject(GModuleConfiguration moduleConf, GContainerDef containerDef) {
        this.moduleConf = moduleConf;
        this.containerDef = containerDef;
    }

    public GModuleConfiguration getModuleConfiguration() {
        return this.moduleConf;
    }

    public GContainerDef getContainerDef() {
        return this.containerDef;
    }

    @Override
    public int hashCode() {
        return 31 + (this.containerDef == null ? 0 : this.containerDef.hashCode());
    }

    @Override
    public boolean equals(Object targetObj) {
        if (this == targetObj) {
            return true;
        }
        if (targetObj == null) {
            return false;
        }
        if (this.getClass() != targetObj.getClass()) {
            return false;
        }
        TreeViewerInputObject otherObj = (TreeViewerInputObject) targetObj;
        return !(this.containerDef == null ? otherObj.containerDef != null
                : !this.containerDef.equals(otherObj.containerDef));
    }
}

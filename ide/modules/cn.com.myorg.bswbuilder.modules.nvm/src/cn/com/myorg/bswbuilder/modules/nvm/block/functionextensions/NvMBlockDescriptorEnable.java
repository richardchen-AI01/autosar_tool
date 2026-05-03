package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import cn.com.myorg.mal.uidefinition.ReserveUIDefinition;
import gautosar.gecucdescription.GContainer;
import org.eclipse.emf.ecore.EObject;

/**
 * 99% paraphrase of cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMBlockDescriptorEnable.
 *
 * <p>Controls Del/Copy/Rename action permission for NvMBlockDescriptor instances.
 * NvMBlock_ConfigID is the system-reserved ConfigID block — cannot be deleted /
 * copied / renamed. All other NvMBlockDescriptor instances permit these actions.
 */
public class NvMBlockDescriptorEnable extends ReserveUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMBlockDescriptor";
    }

    @Override
    public boolean permitDuplicate(EObject obj) {
        return this.isNvmBlockConfigIdName(obj);
    }

    @Override
    public boolean permitDel(EObject obj) {
        return this.isNvmBlockConfigIdName(obj);
    }

    @Override
    public boolean permitRename(EObject obj) {
        return this.isNvmBlockConfigIdName(obj);
    }

    private boolean isNvmBlockConfigIdName(EObject obj) {
        return !"NvMBlock_ConfigID".equals(((GContainer) obj).gGetShortName());
    }
}

package cn.com.myorg.mal.uidefinition;

import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.mal.uidefinition.ReserveUIDefinition.
 *
 * <p>Constrains container right-click menu actions (e.g. NvMBlock_ConfigID
 * cannot be deleted/renamed/duplicated). Variant 0x100000L = RESERVED_FLAG.
 */
public abstract class ReserveUIDefinition implements IUIDefinition {
    @Override
    public long getVariant() {
        return 0x100000L;
    }

    public boolean permitDuplicate(EObject obj) {
        return false;
    }

    public boolean permitDel(EObject obj) {
        return false;
    }

    public boolean permitRename(EObject obj) {
        return false;
    }

    public boolean isDisable(EObject obj) {
        return false;
    }
}

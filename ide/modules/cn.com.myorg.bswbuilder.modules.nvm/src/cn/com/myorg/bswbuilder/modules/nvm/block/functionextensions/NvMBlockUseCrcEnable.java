package cn.com.myorg.bswbuilder.modules.nvm.block.functionextensions;

import autosar40.ecucdescription.EcucNumericalParamValue;
import cn.com.myorg.mal.modelutils.EcuUtils;
import cn.com.myorg.mal.uidefinition.ComputeEnableUIDefinition;
import cn.com.myorg.mal.uidefinition.IAutoComputeUIDefinition;
import gautosar.gecucdescription.GContainer;
import java.util.ArrayList;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.bswbuilder.nvm.block.functionextensions.NvMBlockUseCrcEnable.
 *
 * <p>Field NvMBlockUseCrc enable rule:
 *  - container shortName == "NvMBlock_ConfigID" -> always disabled
 *  - NvMWriteBlockOnce == true -> disabled (CRC implied off when write-once)
 *  - else -> enabled
 *
 * <p>Auto-compute (calc) writes true back when forced-on (config block / write-once),
 * else null (leave user's value untouched).
 */
public class NvMBlockUseCrcEnable
        extends ComputeEnableUIDefinition
        implements IAutoComputeUIDefinition {

    @Override
    public String getDefElementName() {
        return "NvMBlockUseCrc";
    }

    @Override
    public boolean compute(Object parentContainer) {
        GContainer container = (GContainer) parentContainer;
        Boolean once = EcuUtils.getBooleanValue(container, "NvMWriteBlockOnce");
        String blockName = container.gGetShortName();
        return !blockName.equals("NvMBlock_ConfigID") && once == Boolean.FALSE;
    }

    @Override
    public Object calc(Object obj) {
        EObject parent = ((EcucNumericalParamValue) obj).eContainer();
        if (parent instanceof GContainer) {
            Boolean once = EcuUtils.getBooleanValue((GContainer) parent, "NvMWriteBlockOnce");
            if (((GContainer) parent).gGetShortName().equals("NvMBlock_ConfigID") || Boolean.TRUE.equals(once)) {
                return true;
            }
        }
        return null;
    }

    @Override
    public List<String> getRelatedUIElementList() {
        ArrayList<String> lstRet = new ArrayList<>();
        lstRet.add("NvMWriteBlockOnce");
        return lstRet;
    }
}

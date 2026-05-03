package cn.com.myorg.mal.modelutils;

import autosar40.ecucdescription.EcucNumericalParamValue;
import autosar40.ecucparameterdef.EcucBooleanParamDef;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GParameterValue;
import gautosar.gecucparameterdef.GConfigParameter;
import java.util.ArrayList;

/**
 * Reference: cn.com.isoft.mal.modelutils.EcuUtils (extends EcuUtilsBase).
 *
 * <p>Phase 2.5 PoC port — single helper getBooleanValue, called by
 * NvMBlockUseCrcEnable.compute. Full EcuUtilsBase port (32+ helpers including
 * getIntegerValue / getEnumerationValue / getReferenceContainerList / etc) is
 * deferred to Phase 6c when NvM 32 functionextensions need them. Kept in
 * mal.modelutils package to match reference path so subsequent ports drop in.
 */
public final class EcuUtils {

    private EcuUtils() {
    }

    public static Boolean getBooleanValue(GContainer parentContainer, String elementName) {
        ArrayList<Boolean> lstRet = new ArrayList<>();
        if (parentContainer != null) {
            for (GParameterValue parameterValue : parentContainer.gGetParameterValues()) {
                GConfigParameter def = parameterValue.gGetDefinition();
                if (!(def instanceof EcucBooleanParamDef) || !def.gGetShortName().equals(elementName)) {
                    continue;
                }
                String strBoolean = ((EcucNumericalParamValue) parameterValue).getValue().getMixedText();
                Boolean value = strBoolean.equals("true") || strBoolean.equals("1") ? Boolean.TRUE : Boolean.FALSE;
                lstRet.add(value);
            }
        }
        if (lstRet.size() > 0) {
            return lstRet.get(0);
        }
        return null;
    }
}

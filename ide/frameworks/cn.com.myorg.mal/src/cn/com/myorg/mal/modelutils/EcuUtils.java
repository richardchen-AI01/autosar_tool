package cn.com.myorg.mal.modelutils;

import autosar40.genericstructure.varianthandling.attributevaluevariationpoints.BooleanValueVariationPoint;
import autosar40.genericstructure.varianthandling.attributevaluevariationpoints.PositiveIntegerValueVariationPoint;
import autosar40.ecucdescription.EcucNumericalParamValue;
import autosar40.ecucparameterdef.EcucBooleanParamDef;
import autosar40.ecucparameterdef.EcucChoiceContainerDef;
import autosar40.ecucparameterdef.EcucDefinitionElement;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GParameterValue;
import gautosar.gecucparameterdef.GConfigParameter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

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

    /**
     * 99% paraphrase of cn.com.isoft.mal.modelutils.EcuUtilsBase.getChoiceChildContainers
     * (line 705-714).
     */
    public static List<GContainer> getChoiceChildContainers(GContainer parentContainer,
                                                            EcucChoiceContainerDef childDef) {
        LinkedList<GContainer> lstChoiceChildContainer = new LinkedList<>();
        if (parentContainer != null) {
            for (GContainer childContainer : parentContainer.gGetSubContainers()) {
                if (!childContainer.gGetDefinition().equals(childDef)) continue;
                lstChoiceChildContainer.add(childContainer);
            }
        }
        return lstChoiceChildContainer;
    }

    /**
     * 99% paraphrase of EcuUtilsBase.getUpperMultiplicity (line 215-228) +
     * parseUpperMultiplicity (line 246-258).
     */
    public static Integer getUpperMultiplicity(EObject object) {
        if (object instanceof EcucDefinitionElement) {
            EcucDefinitionElement element = (EcucDefinitionElement) object;
            BooleanValueVariationPoint booleanValueVariationPoint = element.getUpperMultiplicityInfinite();
            if (booleanValueVariationPoint != null) {
                if (booleanValueVariationPoint.getMixedText().equals("true")) {
                    return Integer.MAX_VALUE;
                }
                return -1;
            }
            return parseUpperMultiplicity(element.getUpperMultiplicity());
        }
        return -1;
    }

    private static Integer parseUpperMultiplicity(PositiveIntegerValueVariationPoint multiplicity) {
        if (multiplicity != null) {
            String mixedText = multiplicity.getMixedText();
            if (mixedText == null || mixedText.equals("*")) {
                return Integer.MAX_VALUE;
            }
            if (mixedText.equals("")) {
                return 1;
            }
            return Integer.parseInt(mixedText);
        }
        return Integer.MAX_VALUE;
    }
}

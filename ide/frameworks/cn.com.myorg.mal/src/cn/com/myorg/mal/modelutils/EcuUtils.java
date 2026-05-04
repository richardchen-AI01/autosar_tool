package cn.com.myorg.mal.modelutils;

import autosar40.genericstructure.varianthandling.attributevaluevariationpoints.BooleanValueVariationPoint;
import autosar40.genericstructure.varianthandling.attributevaluevariationpoints.PositiveIntegerValueVariationPoint;
import autosar40.ecucdescription.EcucNumericalParamValue;
import autosar40.ecucdescription.EcucTextualParamValue;
import autosar40.ecucparameterdef.EcucAbstractStringParamDef;
import autosar40.ecucparameterdef.EcucBooleanParamDef;
import autosar40.ecucparameterdef.EcucChoiceContainerDef;
import autosar40.ecucparameterdef.EcucDefinitionElement;
import autosar40.ecucparameterdef.EcucEnumerationParamDef;
import autosar40.ecucparameterdef.EcucIntegerParamDef;
import gautosar.gecucdescription.GConfigReferenceValue;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;
import gautosar.gecucdescription.GParameterValue;
import gautosar.gecucdescription.GReferenceValue;
import gautosar.gecucparameterdef.GConfigParameter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import org.eclipse.emf.ecore.EObject;

/**
 * Reference: cn.com.isoft.mal.modelutils.EcuUtils (extends EcuUtilsBase).
 * 99% paraphrase — methods needed by NvM 32 ComputeEnable hooks (M1a).
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

    public static String getEnumerationValue(GContainer parentContainer, String elementName) {
        ArrayList<String> lstRet = new ArrayList<>();
        if (parentContainer != null) {
            for (GParameterValue parameterValue : parentContainer.gGetParameterValues()) {
                GConfigParameter def = parameterValue.gGetDefinition();
                if (!(def instanceof EcucEnumerationParamDef) || !def.gGetShortName().equals(elementName)) {
                    continue;
                }
                lstRet.add(((EcucTextualParamValue) parameterValue).getValue());
            }
        }
        if (lstRet.size() > 0) {
            return lstRet.get(0);
        }
        return null;
    }

    public static Integer getIntegerValue(GContainer parentContainer, String elementName) {
        ArrayList<Integer> lstRet = new ArrayList<>();
        if (parentContainer != null) {
            for (GParameterValue parameterValue : parentContainer.gGetParameterValues()) {
                GConfigParameter def = parameterValue.gGetDefinition();
                if (!(def instanceof EcucIntegerParamDef) || !def.gGetShortName().equals(elementName)) {
                    continue;
                }
                String strInteger = ((EcucNumericalParamValue) parameterValue).getValue().getMixedText();
                if (strInteger.trim().length() <= 0) {
                    continue;
                }
                if (strInteger.length() > 2) {
                    String prefix = strInteger.substring(0, 2);
                    if (prefix.equals("0x") || prefix.equals("0X")) {
                        int val = Integer.parseInt(strInteger.substring(2), 16);
                        strInteger = String.valueOf(val);
                    }
                }
                Integer value = 0;
                try {
                    value = Integer.valueOf(strInteger);
                } catch (Exception e) {
                    e.printStackTrace();
                }
                lstRet.add(value);
            }
        }
        if (lstRet.size() > 0) {
            return lstRet.get(0);
        }
        return null;
    }

    public static String getStringValue(GContainer parentContainer, String elementName) {
        ArrayList<String> lstRet = new ArrayList<>();
        if (parentContainer != null) {
            for (GParameterValue parameterValue : parentContainer.gGetParameterValues()) {
                GConfigParameter def = parameterValue.gGetDefinition();
                if (!(def instanceof EcucAbstractStringParamDef) || !def.gGetShortName().equals(elementName)) {
                    continue;
                }
                lstRet.add(((EcucTextualParamValue) parameterValue).getValue());
            }
        }
        if (lstRet.size() > 0) {
            return lstRet.get(0);
        }
        return null;
    }

    public static GContainer getFirstChildContainer(GContainer parentContainer, String childContainerName) {
        if (parentContainer == null) {
            return null;
        }
        for (GContainer childContainer : parentContainer.gGetSubContainers()) {
            if (!childContainer.gGetDefinition().gGetShortName().equals(childContainerName)) {
                continue;
            }
            return childContainer;
        }
        return null;
    }

    public static List<GContainer> getModuleChildContainers(GModuleConfiguration moduleConf, String containerName) {
        LinkedList<GContainer> lstContainer = new LinkedList<>();
        if (moduleConf != null) {
            for (GContainer childContainer : moduleConf.gGetContainers()) {
                if (!childContainer.gGetDefinition().gGetShortName().equals(containerName)) {
                    continue;
                }
                lstContainer.add(childContainer);
            }
        }
        return lstContainer;
    }

    public static GContainer getFirstModuleContainer(GModuleConfiguration moduleConf, String containerName) {
        if (moduleConf == null) {
            return null;
        }
        for (GContainer childContainer : moduleConf.gGetContainers()) {
            if (!childContainer.gGetDefinition().gGetShortName().equals(containerName)) {
                continue;
            }
            return childContainer;
        }
        return null;
    }

    public static List<GContainer> getReferenceContainerList(GContainer parentContainer, String elementName) {
        LinkedList<GContainer> lstRet = new LinkedList<>();
        if (parentContainer != null) {
            for (GConfigReferenceValue configReferenceValue : parentContainer.gGetReferenceValues()) {
                if (!(configReferenceValue instanceof GReferenceValue)
                        || !configReferenceValue.gGetDefinition().gGetShortName().equals(elementName)) {
                    continue;
                }
                lstRet.add((GContainer) ((GReferenceValue) configReferenceValue).gGetValue());
            }
        }
        return lstRet;
    }

    public static GContainer getSingleRefValue(GContainer parentContainer, String elementName) {
        List<GContainer> lstReferenceContainer = getReferenceContainerList(parentContainer, elementName);
        if (lstReferenceContainer.size() > 0) {
            return lstReferenceContainer.get(0);
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
     * 99% paraphrase of EcuUtilsBase.getLowerMultiplicity (line 230-244).
     */
    public static Integer getLowerMultiplicity(EObject object) {
        if (object instanceof EcucDefinitionElement) {
            EcucDefinitionElement multiplicity = (EcucDefinitionElement) object;
            PositiveIntegerValueVariationPoint variationPoint = multiplicity.getLowerMultiplicity();
            if (variationPoint != null) {
                String strLowerMultiplicity = multiplicity.getLowerMultiplicity().getMixedText();
                if (strLowerMultiplicity.equals("")) {
                    return 1;
                }
                return Integer.parseInt(strLowerMultiplicity);
            }
            return 1;
        }
        return -1;
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

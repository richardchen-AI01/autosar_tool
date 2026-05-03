package cn.com.myorg.mal;

import cn.com.myorg.mal.interfaces.IFunctionExtension;
import cn.com.myorg.mal.modelutils.DebugUtils;
import cn.com.myorg.mal.uidefinition.IUIDefinition;
import cn.com.myorg.mal.uidefinition.UIDefinitionMap;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Reference: cn.com.isoft.mal.MetaModelDescriptorParser.
 *
 * <p>Central dispatcher consumed by host UI widgets to look up IUIDefinition
 * hooks contributed by each module's FunctionExtension. Indexed by element
 * name + variant flag (ENABLE / RANGE / RESERVED / etc).
 */
public class MetaModelDescriptorParser {
    public static List<IUIDefinition> getUIDefinitionList(String ecuName, String elementName) {
        List<IUIDefinition> lstRet = new ArrayList<>();
        List<AutocoreMetaModelDescriptor> lstMetaModelDescriptor =
                BswModuleManager.getInstance(ecuName).getMetaModelDescriptorList();
        if (DebugUtils.isCloseUIFuncAll()) {
            return lstRet;
        }
        for (AutocoreMetaModelDescriptor metaModelDescriptor : lstMetaModelDescriptor) {
            UIDefinitionMap uiDefinitionMap;
            IFunctionExtension funcExtension = metaModelDescriptor.getFunctionExtension();
            if (funcExtension == null
                    || (uiDefinitionMap = funcExtension.getUIDefinitionMap()) == null
                    || (lstRet = uiDefinitionMap.getUIDefinitionList(elementName)) == null
                    || lstRet.size() <= 0) {
                continue;
            }
            return lstRet;
        }
        return lstRet;
    }

    public static List<IUIDefinition> getUIDefinitionList(String ecuName, String elementName, long variant) {
        ArrayList<IUIDefinition> lstRetUIDefinition = new ArrayList<>();
        List<IUIDefinition> lstUIDefinition = getUIDefinitionList(ecuName, elementName);
        if (lstUIDefinition != null) {
            for (IUIDefinition uiDefinition : lstUIDefinition) {
                if ((uiDefinition.getVariant() & variant) <= 0L) continue;
                lstRetUIDefinition.add(uiDefinition);
            }
        }
        return lstRetUIDefinition;
    }

    public static IFunctionExtension.DataHandle getDataHandle(String ecuName, String key) {
        List<AutocoreMetaModelDescriptor> lstMetaModelDescriptor =
                BswModuleManager.getInstance(ecuName).getMetaModelDescriptorList();
        for (AutocoreMetaModelDescriptor metaModelDescriptor : lstMetaModelDescriptor) {
            Map<String, IFunctionExtension.DataHandle> mapDataHandle;
            IFunctionExtension funcExtension = metaModelDescriptor.getFunctionExtension();
            if (funcExtension == null
                    || (mapDataHandle = funcExtension.getDataHandleMap()) == null
                    || !mapDataHandle.containsKey(key)) {
                continue;
            }
            return mapDataHandle.get(key);
        }
        return null;
    }

    public static Map<String, List<IUIDefinition>> getUIDefinitionList(String ecuName, Set<String> elementNames) {
        HashMap<String, List<IUIDefinition>> mapShortNameUIDefinition = new HashMap<>();
        if (DebugUtils.isCloseUIFuncAll()) {
            return mapShortNameUIDefinition;
        }
        List<AutocoreMetaModelDescriptor> lstMetaModelDescriptor =
                BswModuleManager.getInstance(ecuName).getMetaModelDescriptorList();
        for (AutocoreMetaModelDescriptor metaModelDescriptor : lstMetaModelDescriptor) {
            UIDefinitionMap uiDefinitionMap;
            IFunctionExtension funcExtension = metaModelDescriptor.getFunctionExtension();
            if (funcExtension == null
                    || (uiDefinitionMap = funcExtension.getUIDefinitionMap()) == null) {
                continue;
            }
            for (String elementName : elementNames) {
                List<IUIDefinition> lstRet = uiDefinitionMap.getUIDefinitionList(elementName);
                if (lstRet == null || lstRet.size() <= 0) continue;
                mapShortNameUIDefinition.put(elementName, lstRet);
            }
        }
        return mapShortNameUIDefinition;
    }
}

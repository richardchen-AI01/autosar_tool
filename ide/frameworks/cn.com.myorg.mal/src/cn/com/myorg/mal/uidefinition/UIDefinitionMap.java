package cn.com.myorg.mal.uidefinition;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Reference: cn.com.isoft.mal.uidefinition.UIDefinitionMap.
 *
 * <p>Indexed container; multiple IUIDefinition entries may share the same
 * defElementName (e.g. both ENABLE and AUTO_COMPUTE on the same field).
 */
public class UIDefinitionMap {
    private Map<String, List<IUIDefinition>> mapUIDefinition = new HashMap<>();

    public void put(IUIDefinition uiDefinition) {
        String name = uiDefinition.getDefElementName();
        if (this.mapUIDefinition.containsKey(name)) {
            this.mapUIDefinition.get(name).add(uiDefinition);
        } else {
            ArrayList<IUIDefinition> lstUIDefinition = new ArrayList<>();
            lstUIDefinition.add(uiDefinition);
            this.mapUIDefinition.put(name, lstUIDefinition);
        }
    }

    public List<IUIDefinition> getUIDefinitionList(String key) {
        return this.mapUIDefinition.get(key);
    }
}

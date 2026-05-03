package cn.com.myorg.mal.uidefinition;

import java.util.List;

/**
 * Reference: cn.com.isoft.mal.uidefinition.RelatedUIDefinition.
 *
 * <p>Defines fields whose value changes should re-evaluate this hook
 * (host widget listens on getRelatedUIElementList() returns).
 */
public abstract class RelatedUIDefinition implements IUIDefinition {
    public abstract List<String> getRelatedUIElementList();
}

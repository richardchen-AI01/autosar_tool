package cn.com.myorg.mal.uidefinition;

/**
 * Reference: cn.com.isoft.mal.uidefinition.EnumValueScopeUIDefinition.
 *
 * <p>For enum fields whose candidate set varies by sibling state.
 */
public abstract class EnumValueScopeUIDefinition extends RelatedUIDefinition {
    @Override
    public long getVariant() {
        return 16384L;
    }

    public abstract String[] getValueScope(Object var1);
}

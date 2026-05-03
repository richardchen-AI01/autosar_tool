package cn.com.myorg.mal.uidefinition;

/**
 * Reference: cn.com.isoft.mal.uidefinition.ReferenceValueScopeUIDefinition.
 *
 * <p>For ref-typed fields whose drop-down candidates are computed across the
 * workspace (e.g. NvMFeeRef -> all FeeBlockConfiguration instances). Variant
 * 16384L = RANGE_FLAG. Phase 6d consumer.
 */
public abstract class ReferenceValueScopeUIDefinition extends RelatedUIDefinition {
    @Override
    public long getVariant() {
        return 16384L;
    }

    public abstract Object[] getValueScope(Object var1);
}

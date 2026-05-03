package cn.com.myorg.mal.uidefinition;

/**
 * Reference: cn.com.isoft.mal.uidefinition.ComputeEnableUIDefinition.
 *
 * <p>Concrete subclasses implement compute(parent) returning a single boolean
 * driving both isEnable (true) and isDisable (false). Variant 12296L =
 * ENABLE_FLAG (4096) | DISABLE_FLAG (8192) | FIX_FLAG (8).
 */
public abstract class ComputeEnableUIDefinition extends EnableUIDefinition {
    @Override
    public final boolean isEnable(Object parentContainer) {
        return this.compute(parentContainer);
    }

    @Override
    public final boolean isDisable(Object parentContainer) {
        return !this.compute(parentContainer);
    }

    public abstract boolean compute(Object var1);

    @Override
    public long getVariant() {
        return 12296L;
    }
}

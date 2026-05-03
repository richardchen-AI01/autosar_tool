package cn.com.myorg.mal.uidefinition;

/**
 * Reference: cn.com.isoft.mal.uidefinition.IAutoComputeUIDefinition.
 *
 * <p>Marks an IUIDefinition that auto-writes a derived value via calc().
 */
public interface IAutoComputeUIDefinition extends IUIDefinition {
    Object calc(Object var1);
}

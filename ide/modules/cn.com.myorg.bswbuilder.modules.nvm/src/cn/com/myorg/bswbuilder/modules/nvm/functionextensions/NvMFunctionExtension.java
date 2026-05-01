package cn.com.myorg.bswbuilder.modules.nvm.functionextensions;

import cn.com.myorg.mal.interfaces.IFunctionExtension;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.nvm.functionextensions.NvMFunctionExtension.
 *
 * <p>Our IFunctionExtension is a marker interface (full surface deferred), so
 * an empty impl is enough for AutocoreMetaModelDescriptor.getFunctionExtension()
 * contract. Reference also registers ComputeEnableUIDefinition entries here
 * (NvMNvramDeviceId / NvMTargetBlockReference choice) for FormEditor field
 * conditional visibility — UI condition wiring is v0.3 work.
 */
public class NvMFunctionExtension implements IFunctionExtension {
}

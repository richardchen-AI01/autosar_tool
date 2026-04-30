package cn.com.myorg.bswbuilder.modules.memif.functionextensions;

import cn.com.myorg.mal.interfaces.IFunctionExtension;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.memif.functionextensions.MemIfFunctionExtension
 * — class doesn't ship in iSoft memif jar (CFR'd 12 classes don't include it;
 * lives in a separate UI bundle in their build).
 *
 * <p>Our IFunctionExtension is a marker interface (full surface deferred),
 * so an empty impl is enough for AutocoreMetaModelDescriptor.getFunctionExtension()
 * contract.
 */
public class MemIfFunctionExtension implements IFunctionExtension {
}

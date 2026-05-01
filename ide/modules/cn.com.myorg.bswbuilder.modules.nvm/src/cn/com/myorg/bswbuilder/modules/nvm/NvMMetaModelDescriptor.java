package cn.com.myorg.bswbuilder.modules.nvm;

import org.eclipse.sphinx.emf.metamodel.MetaModelVersionData;

import cn.com.myorg.bswbuilder.modules.nvm.functionextensions.NvMFunctionExtension;
import cn.com.myorg.mal.AutocoreMetaModelDescriptor;
import cn.com.myorg.mal.interfaces.IFunctionExtension;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.nvm.NvMMetaModelDescriptor —
 * Constructor passes (identifier, baseNamespace, MetaModelVersionData(epkg,
 * namespacePattern, name)) to AutocoreMetaModelDescriptor.
 */
public class NvMMetaModelDescriptor extends AutocoreMetaModelDescriptor {

    private static final String identifier = "cn.com.myorg.bswbuilder.modules.nvm";
    private static final String baseNamespace = "cn.com.myorg.bswbuilder.modules.nvm";

    public NvMMetaModelDescriptor() {
        super(identifier, baseNamespace,
              new MetaModelVersionData("schema/r4.0", "schema/r4\\.0(/\\w+)+", "NvM"));
    }

    @Override
    public IFunctionExtension getFunctionExtension() {
        return new NvMFunctionExtension();
    }
}

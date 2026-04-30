package cn.com.myorg.bswbuilder.modules.memif;

import org.eclipse.sphinx.emf.metamodel.MetaModelVersionData;

import cn.com.myorg.bswbuilder.modules.memif.functionextensions.MemIfFunctionExtension;
import cn.com.myorg.mal.AutocoreMetaModelDescriptor;
import cn.com.myorg.mal.interfaces.IFunctionExtension;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.memif.MemIfMetaModelDescriptor
 * (Procyon-confirmed signature). Constructor passes (identifier, baseNamespace,
 * MetaModelVersionData(epkg, namespacePattern, name)) to AutocoreMetaModelDescriptor.
 */
public class MemIfMetaModelDescriptor extends AutocoreMetaModelDescriptor {

    private static final String identifier = "cn.com.myorg.bswbuilder.modules.memif";
    private static final String baseNamespace = "cn.com.myorg.bswbuilder.modules.memif";

    public MemIfMetaModelDescriptor() {
        super(identifier, baseNamespace,
              new MetaModelVersionData("schema/r4.0", "schema/r4\\.0(/\\w+)+", "MemIf"));
    }

    @Override
    public IFunctionExtension getFunctionExtension() {
        return new MemIfFunctionExtension();
    }
}

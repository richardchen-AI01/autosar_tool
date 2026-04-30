package cn.com.myorg.mal;

import cn.com.myorg.mal.interfaces.IFunctionExtension;
import org.eclipse.sphinx.emf.metamodel.AbstractMetaModelDescriptor;
import org.eclipse.sphinx.emf.metamodel.MetaModelVersionData;

public abstract class AutocoreMetaModelDescriptor
extends AbstractMetaModelDescriptor {
    protected AutocoreMetaModelDescriptor(String identifier, String baseNamespace, MetaModelVersionData versionData) {
        super(identifier, baseNamespace, versionData);
    }

    public String getDefaultContentTypeId() {
        return "cn.com.myorg.bsw.DefaultContentType";
    }

    public abstract IFunctionExtension getFunctionExtension();
}

package cn.com.myorg.mal.interfaces;

import cn.com.myorg.mal.generation.BSWModuleVersionConstraint;
import gautosar.gecucdescription.GModuleConfiguration;
import java.io.File;
import java.io.OutputStream;
import org.eclipse.core.runtime.MultiStatus;

public interface IModuleGenerator {
    public MultiStatus generate(GModuleConfiguration var1, File var2, OutputStream var3);

    public BSWModuleVersionConstraint[] getSupportedVersions();
}

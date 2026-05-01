package cn.com.myorg.bswbuilder.modules.nvm.generator;

import java.io.File;
import java.io.OutputStream;

import org.eclipse.core.runtime.MultiStatus;

import cn.com.myorg.mal.generation.BSWModuleVersionConstraint;
import cn.com.myorg.mal.interfaces.IModuleGenerator;
import gautosar.gecucdescription.GModuleConfiguration;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.nvm.generator.NvmGenerator —
 * shell class implementing IModuleGenerator contract. Reference body delegates
 * to {@code GeneratorUtils.generateExe(conf, confDir, status)} (calls
 * ORIENTAISBswGen.exe). v0.2 leaves this no-op; actual code generation runs
 * via the Python pipeline triggered by GenerateMemIfHandler-style command
 * (extensible to NvM by reusing GenerateMemIfHandler.pickIFile, since that
 * handler already passes the module name to bswgen at runtime).
 */
public class NvMGenerator implements IModuleGenerator {

    public static final String PLUGIN_ID = "cn.com.myorg.bswbuilder.modules.nvm";

    @Override
    public MultiStatus generate(GModuleConfiguration conf, File confDir, OutputStream infoStream) {
        return new MultiStatus(PLUGIN_ID, 0, null, null);
    }

    @Override
    public BSWModuleVersionConstraint[] getSupportedVersions() {
        return new BSWModuleVersionConstraint[] { new BSWModuleVersionConstraint(1, 0, null) };
    }
}

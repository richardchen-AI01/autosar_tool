package cn.com.myorg.bswbuilder.modules.memif.generator;

import java.io.File;
import java.io.OutputStream;

import org.eclipse.core.runtime.MultiStatus;

import cn.com.myorg.mal.generation.BSWModuleVersionConstraint;
import cn.com.myorg.mal.interfaces.IModuleGenerator;
import gautosar.gecucdescription.GModuleConfiguration;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.memif.generator.MemIfGenerator —
 * shell class implementing IModuleGenerator contract.
 *
 * <p>Reference body: {@code GeneratorUtils.generateExe(conf, confDir, status)}
 * — invokes ORIENTAISBswGen.exe (PyInstaller). v0.2 leaves this no-op:
 * actual code generation runs through {@code GenerateMemIfHandler} command
 * (Python jinja path), which is independent from the IoC chain.
 *
 * <p>Wiring this to call the existing Python pipeline is a v0.3 cleanup —
 * collapse two generation paths into one once we're confident the IoC
 * chain replaces the menu-handler path.
 */
public class MemIfGenerator implements IModuleGenerator {

    public static final String PLUGIN_ID = "cn.com.myorg.bswbuilder.modules.memif";

    @Override
    public MultiStatus generate(GModuleConfiguration conf, File confDir, OutputStream infoStream) {
        return new MultiStatus(PLUGIN_ID, 0, null, null);
    }

    @Override
    public BSWModuleVersionConstraint[] getSupportedVersions() {
        return new BSWModuleVersionConstraint[] { new BSWModuleVersionConstraint(1, 0, null) };
    }
}

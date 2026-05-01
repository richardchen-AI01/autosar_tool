package cn.com.myorg.bswbuilder.modules.nvm.bswmd;

import org.eclipse.core.runtime.MultiStatus;

import cn.com.myorg.mal.interfaces.IModuleUpdateBswmd;
import gautosar.gecucdescription.GModuleConfiguration;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.nvm.bswmd.NvMUpdateBswmd —
 * shell class implementing IModuleUpdateBswmd contract. Reference body delegates
 * to {@code GeneratorUtils.updateBswmdExe(conf, status)} (calls
 * ORIENTAISBswUpg.exe). v0.2 returns success unconditionally; actual Bswmd
 * regeneration runs via UpdateBswmdStubHandler → bswgen --update-bswmd CLI.
 */
public class NvMUpdateBswmd implements IModuleUpdateBswmd {

    public static final String PLUGIN_ID = "cn.com.myorg.bswbuilder.modules.nvm";

    @Override
    public MultiStatus update(GModuleConfiguration conf) {
        return new MultiStatus(PLUGIN_ID, 0, null, null);
    }
}

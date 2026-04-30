package cn.com.myorg.bswbuilder.modules.memif;

import java.util.HashMap;

import org.eclipse.jface.resource.ImageRegistry;

import cn.com.myorg.mal.modelutils.DefaultRegistry;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.memif.MemIfDefaultRegistry —
 * implements DefaultRegistry contract. Reference's intiDefaultImages
 * registers a "text_padding_left.png" icon via ISoftGraphics.mapImage;
 * we no-op for v0.2 (per-module icon polish deferred).
 *
 * <p>Method name {@code intiDefaultImages} (sic) preserved from reference
 * (CFR-confirmed typo) — see DefaultRegistry interface javadoc.
 */
public class MemIfDefaultRegistry implements DefaultRegistry {

    @Override
    public void initDefaultName(HashMap<String, String> registry) {
        // no-op — reference also has empty body
    }

    @Override
    public void intiDefaultImages(ImageRegistry reg) {
        // v0.2: no per-module icons. Reference does:
        //   ISoftGraphics.mapImage("cn.com.myorg.bswbuilder.modules.memif",
        //                          reg, "text_padding_left.png", new String[]{"MemIf"});
        // ISoftGraphics deferred to v0.3 UI polish phase.
    }
}

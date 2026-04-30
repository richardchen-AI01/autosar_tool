package cn.com.myorg.mal;

import cn.com.myorg.mal.AutocoreMetaModelDescriptor;
import cn.com.myorg.mal.AutocoreModuleDefinition;
import cn.com.myorg.mal.coordinator.AutocoreCoordinator;
import cn.com.myorg.mal.coordinator.BswModuleKind;
import cn.com.myorg.mal.coordinator.KindContainModule;
import java.util.ArrayList;
import java.util.List;
import org.eclipse.core.runtime.CoreException;

public class BswModuleManager {
    private static BswModuleManager INSTANCE;
    private ArrayList<KindContainModule> lstKindStructure = new ArrayList();
    private List<AutocoreModuleDefinition> availableModules = new ArrayList<AutocoreModuleDefinition>();
    private ArrayList<BswModuleKind> lstBswModuleKind = AutocoreCoordinator.INSTANCE.getBswModuleKind();

    public static BswModuleManager getInstance(String mcu) {
        INSTANCE = new BswModuleManager(mcu);
        return INSTANCE;
    }

    private BswModuleManager(String mcu) {
        for (BswModuleKind moduleKind : this.lstBswModuleKind) {
            this.lstKindStructure.add(new KindContainModule(moduleKind));
        }
        this.classifyModules(mcu);
        this.clearUnusedKind();
    }

    private void classifyModules(String mcuName) {
        this.availableModules = AutocoreCoordinator.getVendorModules(mcuName);
        for (AutocoreModuleDefinition module : this.availableModules) {
            for (KindContainModule obj : this.lstKindStructure) {
                if (!obj.getKindName().equals(module.getKind())) continue;
                obj.addModule(module);
                module.setParent(obj);
            }
        }
    }

    private void clearUnusedKind() {
        ArrayList<KindContainModule> unUsedKind = new ArrayList<KindContainModule>();
        for (KindContainModule obj : this.lstKindStructure) {
            if (obj.getModuleCount() != 0) continue;
            unUsedKind.add(obj);
        }
        this.lstKindStructure.removeAll(unUsedKind);
    }

    public List<AutocoreModuleDefinition> getCanUsedModule() {
        return this.availableModules;
    }

    public List<KindContainModule> getKindContainModule() {
        return this.lstKindStructure;
    }

    public List<AutocoreMetaModelDescriptor> getMetaModelDescriptorList() {
        ArrayList<AutocoreMetaModelDescriptor> lstModelDesc = new ArrayList<AutocoreMetaModelDescriptor>();
        if (this.availableModules.size() > 0) {
            for (AutocoreModuleDefinition moduleDef : this.availableModules) {
                try {
                    lstModelDesc.add((AutocoreMetaModelDescriptor)((Object)moduleDef.getModuleDescriptor()));
                }
                catch (CoreException e) {
                    System.err.println("getMetaModelDescriptor happen error : " + e.getMessage());
                }
            }
        }
        return lstModelDesc;
    }
}

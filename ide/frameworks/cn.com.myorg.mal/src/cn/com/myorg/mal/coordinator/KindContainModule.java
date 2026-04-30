package cn.com.myorg.mal.coordinator;

import cn.com.myorg.mal.AutocoreModuleDefinition;
import cn.com.myorg.mal.coordinator.BswModuleKind;
import java.util.ArrayList;
import java.util.List;

public class KindContainModule {
    private BswModuleKind bswModuleKind;
    private ArrayList<AutocoreModuleDefinition> lstModules = new ArrayList();
    private boolean shouldChecked = false;

    public KindContainModule(BswModuleKind bswModuleKind) {
        this.bswModuleKind = bswModuleKind;
    }

    public String getKindName() {
        return this.bswModuleKind.getName();
    }

    public BswModuleKind getBswModuleKind() {
        return this.bswModuleKind;
    }

    public void addModule(AutocoreModuleDefinition module) {
        this.lstModules.add(module);
    }

    public int getModuleCount() {
        return this.lstModules.size();
    }

    public List<AutocoreModuleDefinition> getModules() {
        return this.lstModules;
    }

    public void setModules(ArrayList<AutocoreModuleDefinition> list) {
        this.lstModules = list;
    }

    public boolean shouldBeChecked() {
        return this.shouldChecked;
    }

    public void setShouldBeChecked(boolean checked) {
        this.shouldChecked = checked;
    }

    public boolean isPartChecked() {
        int count = this.getCheckedCount();
        return count > 0 && count < this.lstModules.size();
    }

    public boolean isAllChecked() {
        int count = this.getCheckedCount();
        return count == this.lstModules.size();
    }

    private int getCheckedCount() {
        int count = 0;
        for (AutocoreModuleDefinition module : this.lstModules) {
            if (!module.shouldBeChecked()) continue;
            ++count;
        }
        return count;
    }

    public String toString() {
        return this.bswModuleKind.getName();
    }

    public int hashCode() {
        int hashcode = 0;
        for (AutocoreModuleDefinition module : this.getModules()) {
            hashcode += module.hashCode();
        }
        return hashcode;
    }
}

package cn.com.myorg.bswbuilder.ui.navigator.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Objects;

import org.eclipse.core.runtime.PlatformObject;

/**
 * KIND grouping virtual node ("MEM" / "COM" / "MCAL" / …) under an
 * {@link EcuConfigurationModel}.
 *
 * <p>Reference: {@code cn.com.isoft.mal.model.ModuleKindModel}.
 * Field/operation surface mirrors model.ecore:
 * <ul>
 *   <li>{@code kindName}: EString</li>
 *   <li>{@code moduleModels}: ModuleModel[*] (containment)</li>
 *   <li>op {@code hashCode()}: EInt — explicitly listed in .ecore</li>
 *   <li>op {@code toString()}: EString — explicitly listed in .ecore</li>
 * </ul>
 *
 * <p>Equality — {@code (parent EcuConfig, kindName)} pair, so navigator
 * tree state survives refresh.
 */
public final class ModuleKindModel extends PlatformObject {

    private final EcuConfigurationModel parent;
    private final String kindName;
    private final List<ModuleModel> moduleModels = new ArrayList<>();

    public ModuleKindModel(EcuConfigurationModel parent, String kindName) {
        this.parent = Objects.requireNonNull(parent);
        this.kindName = Objects.requireNonNull(kindName);
    }

    public EcuConfigurationModel getParent() { return parent; }

    public String getKindName() { return kindName; }

    public List<ModuleModel> getModuleModels() {
        return Collections.unmodifiableList(moduleModels);
    }

    void addModule(ModuleModel m) { moduleModels.add(m); }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof ModuleKindModel)) return false;
        ModuleKindModel other = (ModuleKindModel) o;
        return parent.equals(other.parent) && kindName.equals(other.kindName);
    }

    @Override
    public int hashCode() {
        return Objects.hash(parent, kindName);
    }

    @Override
    public String toString() {
        return "ModuleKindModel(" + parent.getMcuName() + "/" + kindName + ")";
    }
}

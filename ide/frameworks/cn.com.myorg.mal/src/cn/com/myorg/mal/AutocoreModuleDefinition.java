package cn.com.myorg.mal;

import cn.com.myorg.mal.coordinator.KindContainModule;
import cn.com.myorg.mal.excel.ExcelUtils;
import cn.com.myorg.mal.exceptions.AutocoreException;
import java.util.ArrayList;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IConfigurationElement;
import org.eclipse.core.runtime.IExtension;
import org.eclipse.core.runtime.IExtensionRegistry;
import org.eclipse.core.runtime.Platform;

public class AutocoreModuleDefinition
implements Cloneable {
    private final String kind;
    private final String resource;
    private final ArrayList<String> requiredMcus;
    private String version;
    private String autosarType;
    private final String imageIdentifier;
    private String moduleShortName;
    protected final IConfigurationElement vendor;
    private IConfigurationElement confElement;
    private boolean shouldChecked = false;
    private KindContainModule parent;

    public AutocoreModuleDefinition(ArrayList<String> requiredMcu, String version, String autosarType, String resource, String imageIdentifier, String moduleShortName, String kind, IConfigurationElement vendor) {
        this.resource = resource;
        this.requiredMcus = "Os".equalsIgnoreCase(moduleShortName) && requiredMcu == null ? new ArrayList<String>(ExcelUtils.getAllOsInfoEntity().keySet()) : requiredMcu;
        this.version = version;
        this.autosarType = autosarType;
        this.imageIdentifier = imageIdentifier;
        this.moduleShortName = moduleShortName;
        this.kind = kind;
        this.vendor = vendor;
    }

    public AutocoreModuleDefinition(ArrayList<String> mcus, String version, String autosarType, String resource, String imageIdentifier, IConfigurationElement confElement) throws AutocoreException {
        this(mcus, version, autosarType, resource, imageIdentifier, confElement.getAttribute("shortName"), confElement.getAttribute("kind"), AutocoreModuleDefinition.findVendor(confElement));
        this.confElement = confElement;
        if (this.vendor == null) {
            throw new AutocoreException("Vendor for module " + this.getModuleShortName() + " could not be found.");
        }
    }

    private static IConfigurationElement findVendor(IConfigurationElement moduleConfElement) {
        IConfigurationElement[] c;
        IExtensionRegistry reg = Platform.getExtensionRegistry();
        String vv = moduleConfElement.getAttribute("vendor");
        IExtension e = reg.getExtension(vv);
        IConfigurationElement v = null;
        if (e != null && (c = e.getConfigurationElements()).length > 0) {
            v = c[0];
        }
        return v;
    }

    public void setShouldBeChecked(boolean checked) {
        this.shouldChecked = checked;
    }

    public boolean shouldBeChecked() {
        if (this.parent != null) {
            return this.shouldChecked && this.getParent().shouldBeChecked();
        }
        return this.shouldChecked;
    }

    public String toString() {
        return String.valueOf(this.getModuleShortName()) + " module definition for " + this.requiredMcus;
    }

    public final String getModulePath() {
        return "/AUTOSAR/" + this.getModuleShortName();
    }

    public final String getVendorName() {
        return this.getVendor().getAttribute("shortname");
    }

    public final String getModuleShortName() {
        return this.moduleShortName;
    }

    public final void setModuleShortName(String shortName) {
        this.moduleShortName = shortName;
    }

    public final ArrayList<String> getRequiredMcus() {
        return this.requiredMcus;
    }

    public final String getVersion() {
        return this.version;
    }

    public final String getResource() {
        return this.resource;
    }

    public final String getKind() {
        return this.kind;
    }

    public final String getImageIdentifier() {
        return this.imageIdentifier;
    }

    public final IConfigurationElement getVendor() {
        return this.vendor;
    }

    public Object getGenerator() throws CoreException {
        return this.confElement.createExecutableExtension("generator");
    }

    public Object getValidator() throws CoreException {
        return this.confElement.createExecutableExtension("validator");
    }

    public Object getEditorPage() throws CoreException {
        return this.confElement.createExecutableExtension("editor");
    }

    public Object getModuleDescriptor() throws CoreException {
        return this.confElement.createExecutableExtension("moduleDescriptor");
    }

    public String getNamespaceIdentifier() {
        return this.confElement.getNamespaceIdentifier();
    }

    public void setParent(KindContainModule obj) {
        this.parent = obj;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public KindContainModule getParent() {
        return this.parent;
    }

    public String getModuleInterface() {
        return this.confElement.getAttribute("moduleInterface");
    }

    public String getModuleBswmd() {
        return this.confElement.getAttribute("bswmd");
    }

    public AutocoreModuleDefinition clone() throws CloneNotSupportedException {
        return (AutocoreModuleDefinition)super.clone();
    }

    public String getAutosarType() {
        return this.autosarType;
    }

    public void setAutosarType(String autosarType) {
        this.autosarType = autosarType;
    }

    public Object getUpdateBswmd() throws CoreException {
        return this.confElement.createExecutableExtension("updateBswmd");
    }
}

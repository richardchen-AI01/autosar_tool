package cn.com.myorg.mal;

import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IConfigurationElement;

public class ContainerRegDefinition {
    private String moduleName;
    private String containerName;
    private String requiredMcus;
    private String containerUIName;
    private IConfigurationElement confElement;

    public String getContainerUIName() {
        return this.containerUIName;
    }

    public ContainerRegDefinition(String moduleName, String containerName, String requiredMcus, IConfigurationElement confElement, String containerUIName) {
        this.moduleName = moduleName;
        this.containerName = containerName;
        this.requiredMcus = requiredMcus;
        this.confElement = confElement;
        this.containerUIName = containerUIName;
    }

    public String getModuleName() {
        return this.moduleName;
    }

    public String getContainerName() {
        return this.containerName;
    }

    public String getRequiredMcus() {
        return this.requiredMcus;
    }

    public Object getEditorPage() throws CoreException {
        return this.confElement.createExecutableExtension("editor");
    }
}

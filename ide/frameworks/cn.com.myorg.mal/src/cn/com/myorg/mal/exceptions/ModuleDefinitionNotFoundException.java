package cn.com.myorg.mal.exceptions;

/**
 * Reference: cn.com.isoft.mal.exceptions.ModuleDefinitionNotFoundException —
 * thrown by AutocoreCoordinator.getVendorModule(String) when the requested
 * shortName has no module extension registered.
 */
public class ModuleDefinitionNotFoundException extends AutocoreException {
    private static final long serialVersionUID = 1L;
    public ModuleDefinitionNotFoundException(String msg) { super(msg); }
}

package cn.com.myorg.mal.exceptions;

/**
 * Reference: cn.com.isoft.mal.exceptions.ModelObjectNotFoundException.
 *
 * <p>Thrown by ModelUtils.getEObjectByPath when a model object cannot be
 * resolved at the requested path. 99% paraphrase — collapsed into the same
 * cn.com.myorg.mal.exceptions package as AutocoreException (one bundle).
 */
public class ModelObjectNotFoundException extends AutocoreException {

    private static final long serialVersionUID = -367977841913770236L;
    protected static String packageId = "cn.com.myorg.mal.exceptions";
    protected String moduleId = "";

    public ModelObjectNotFoundException() {
    }

    public ModelObjectNotFoundException(String message) {
        super(message);
    }

    public ModelObjectNotFoundException(Throwable cause) {
        super(cause);
    }

    public ModelObjectNotFoundException(String message, Throwable cause) {
        super(packageId + ": " + message, cause);
    }

    public String getModuleId() {
        return this.moduleId;
    }
}

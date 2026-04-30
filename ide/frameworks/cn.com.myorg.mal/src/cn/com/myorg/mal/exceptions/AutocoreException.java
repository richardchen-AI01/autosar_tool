package cn.com.myorg.mal.exceptions;

/**
 * Reference: cn.com.isoft.mal.exceptions.AutocoreException — checked
 * exception thrown by AutocoreCoordinator/AutocoreModuleDefinition.
 * Reference is in cn.com.isoft.mal.exceptions bundle (separate); we collapse
 * here to avoid yet another bundle for 1 class.
 */
public class AutocoreException extends Exception {
    private static final long serialVersionUID = 1L;
    public AutocoreException()                         { super(); }
    public AutocoreException(String msg)               { super(msg); }
    public AutocoreException(String msg, Throwable t)  { super(msg, t); }
    public AutocoreException(Throwable t)              { super(t); }
}

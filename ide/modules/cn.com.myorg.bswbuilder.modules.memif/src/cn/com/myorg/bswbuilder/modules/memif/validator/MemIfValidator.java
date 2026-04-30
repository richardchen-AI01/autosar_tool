package cn.com.myorg.bswbuilder.modules.memif.validator;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.emf.validation.IValidationContext;

import cn.com.myorg.mal.interfaces.IModuleValidator;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.memif.validator.MemIfValidator —
 * shell class implementing IModuleValidator contract.
 *
 * <p>Reference body: chains 3 ValidationUtils.validate* calls + 1
 * ExteralExeValidateHandler.getValidateInfo (calls ORIENTAISBswVal.exe with
 * rules_Bsw/MemIf/*.json). v0.2 returns success unconditionally — IDE-side
 * real-time validation is deferred to v0.3+ (would need full mal.validation
 * + Python rule runner integration).
 *
 * <p>Reference also has a private validateSupport() that's never called from
 * validate() — dead code in reference, omitted here entirely.
 */
public class MemIfValidator implements IModuleValidator {

    @Override
    public IStatus validate(IValidationContext ctx) {
        return ctx.createSuccessStatus();
    }
}

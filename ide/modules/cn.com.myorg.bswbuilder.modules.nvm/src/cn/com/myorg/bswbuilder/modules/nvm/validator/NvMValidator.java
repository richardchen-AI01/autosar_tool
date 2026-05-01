package cn.com.myorg.bswbuilder.modules.nvm.validator;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.emf.validation.IValidationContext;

import cn.com.myorg.mal.interfaces.IModuleValidator;

/**
 * Reference: cn.com.isoft.bswbuilder.modules.nvm.validator.NvMValidator —
 * shell class implementing IModuleValidator contract. Reference body chains
 * ValidationUtils.validate* + ExteralExeValidateHandler.getValidateInfo
 * (calls ORIENTAISBswVal.exe with rules_Bsw/NvM/*.json). v0.2 returns
 * success unconditionally — IDE-side real-time validation deferred to
 * v0.3+ (would need full mal.validation + Python rule runner integration).
 */
public class NvMValidator implements IModuleValidator {

    @Override
    public IStatus validate(IValidationContext ctx) {
        return ctx.createSuccessStatus();
    }
}

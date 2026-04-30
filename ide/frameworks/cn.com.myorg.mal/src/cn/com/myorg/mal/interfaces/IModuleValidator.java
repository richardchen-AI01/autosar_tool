package cn.com.myorg.mal.interfaces;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.emf.validation.IValidationContext;

public interface IModuleValidator {
    public IStatus validate(IValidationContext var1);
}

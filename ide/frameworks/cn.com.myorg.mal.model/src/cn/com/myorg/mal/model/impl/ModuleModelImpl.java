/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  org.eclipse.emf.common.notify.Notification
 *  org.eclipse.emf.common.util.EList
 *  org.eclipse.emf.ecore.EClass
 *  org.eclipse.emf.ecore.InternalEObject
 *  org.eclipse.emf.ecore.impl.ENotificationImpl
 *  org.eclipse.emf.ecore.impl.MinimalEObjectImpl$Container
 */
package cn.com.myorg.mal.model.impl;

import cn.com.myorg.mal.model.ModelPackage;
import cn.com.myorg.mal.model.ModuleModel;
import java.lang.reflect.InvocationTargetException;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;

public class ModuleModelImpl
extends MinimalEObjectImpl.Container
implements ModuleModel {
    protected static final String MODULE_NAME_EDEFAULT = null;
    protected String moduleName = MODULE_NAME_EDEFAULT;
    protected static final String PROJECT_NAME_EDEFAULT = null;
    protected String projectName = PROJECT_NAME_EDEFAULT;
    protected static final String PATH_VALUE_EDEFAULT = null;
    protected String pathValue = PATH_VALUE_EDEFAULT;

    protected ModuleModelImpl() {
    }

    protected EClass eStaticClass() {
        return ModelPackage.Literals.MODULE_MODEL;
    }

    @Override
    public String getModuleName() {
        return this.moduleName;
    }

    @Override
    public void setModuleName(String newModuleName) {
        String oldModuleName = this.moduleName;
        this.moduleName = newModuleName;
        if (this.eNotificationRequired()) {
            this.eNotify((Notification)new ENotificationImpl((InternalEObject)this, 1, 0, (Object)oldModuleName, (Object)this.moduleName));
        }
    }

    @Override
    public String getProjectName() {
        return this.projectName;
    }

    @Override
    public void setProjectName(String newProjectName) {
        String oldProjectName = this.projectName;
        this.projectName = newProjectName;
        if (this.eNotificationRequired()) {
            this.eNotify((Notification)new ENotificationImpl((InternalEObject)this, 1, 1, (Object)oldProjectName, (Object)this.projectName));
        }
    }

    @Override
    public String getPathValue() {
        return this.pathValue;
    }

    @Override
    public void setPathValue(String newPathValue) {
        String oldPathValue = this.pathValue;
        this.pathValue = newPathValue;
        if (this.eNotificationRequired()) {
            this.eNotify((Notification)new ENotificationImpl((InternalEObject)this, 1, 2, (Object)oldPathValue, (Object)this.pathValue));
        }
    }

    @Override
    public String getKeyValue() {
        return String.valueOf(this.getPathValue()) + ":" + this.getModuleName();
    }

    public Object eGet(int featureID, boolean resolve, boolean coreType) {
        switch (featureID) {
            case 0: {
                return this.getModuleName();
            }
            case 1: {
                return this.getProjectName();
            }
            case 2: {
                return this.getPathValue();
            }
        }
        return super.eGet(featureID, resolve, coreType);
    }

    public void eSet(int featureID, Object newValue) {
        switch (featureID) {
            case 0: {
                this.setModuleName((String)newValue);
                return;
            }
            case 1: {
                this.setProjectName((String)newValue);
                return;
            }
            case 2: {
                this.setPathValue((String)newValue);
                return;
            }
        }
        super.eSet(featureID, newValue);
    }

    public void eUnset(int featureID) {
        switch (featureID) {
            case 0: {
                this.setModuleName(MODULE_NAME_EDEFAULT);
                return;
            }
            case 1: {
                this.setProjectName(PROJECT_NAME_EDEFAULT);
                return;
            }
            case 2: {
                this.setPathValue(PATH_VALUE_EDEFAULT);
                return;
            }
        }
        super.eUnset(featureID);
    }

    public boolean eIsSet(int featureID) {
        switch (featureID) {
            case 0: {
                return MODULE_NAME_EDEFAULT == null ? this.moduleName != null : !MODULE_NAME_EDEFAULT.equals(this.moduleName);
            }
            case 1: {
                return PROJECT_NAME_EDEFAULT == null ? this.projectName != null : !PROJECT_NAME_EDEFAULT.equals(this.projectName);
            }
            case 2: {
                return PATH_VALUE_EDEFAULT == null ? this.pathValue != null : !PATH_VALUE_EDEFAULT.equals(this.pathValue);
            }
        }
        return super.eIsSet(featureID);
    }

    public Object eInvoke(int operationID, EList<?> arguments) throws InvocationTargetException {
        switch (operationID) {
            case 0: {
                return this.getKeyValue();
            }
        }
        return super.eInvoke(operationID, arguments);
    }

    public String toString() {
        if (this.eIsProxy()) {
            return super.toString();
        }
        StringBuffer result = new StringBuffer(super.toString());
        result.append(" (moduleName: ");
        result.append(this.moduleName);
        result.append(", projectName: ");
        result.append(this.projectName);
        result.append(", pathValue: ");
        result.append(this.pathValue);
        result.append(')');
        return result.toString();
    }
}

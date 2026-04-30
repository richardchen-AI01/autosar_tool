/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  org.eclipse.core.resources.IFile
 *  org.eclipse.core.resources.ResourcesPlugin
 *  org.eclipse.core.runtime.IPath
 *  org.eclipse.core.runtime.Path
 *  org.eclipse.emf.common.notify.Notification
 *  org.eclipse.emf.common.notify.NotificationChain
 *  org.eclipse.emf.common.util.EList
 *  org.eclipse.emf.ecore.EClass
 *  org.eclipse.emf.ecore.InternalEObject
 *  org.eclipse.emf.ecore.impl.ENotificationImpl
 *  org.eclipse.emf.ecore.impl.MinimalEObjectImpl$Container
 *  org.eclipse.emf.ecore.util.EObjectContainmentEList
 *  org.eclipse.emf.ecore.util.InternalEList
 */
package cn.com.myorg.mal.model.impl;

import cn.com.myorg.mal.model.EcuConfigurationModel;
import cn.com.myorg.mal.model.ModelPackage;
import cn.com.myorg.mal.model.ModuleKindModel;
import java.lang.reflect.InvocationTargetException;
import java.util.Collection;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.Path;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.notify.NotificationChain;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;
import org.eclipse.emf.ecore.util.EObjectContainmentEList;
import org.eclipse.emf.ecore.util.InternalEList;

public class EcuConfigurationModelImpl
extends MinimalEObjectImpl.Container
implements EcuConfigurationModel {
    protected static final String PATH_VALUE_EDEFAULT = null;
    protected String pathValue = PATH_VALUE_EDEFAULT;
    protected static final String PROJECT_NAME_EDEFAULT = null;
    protected String projectName = PROJECT_NAME_EDEFAULT;
    protected EList<ModuleKindModel> moduleKindModels;

    protected EcuConfigurationModelImpl() {
    }

    protected EClass eStaticClass() {
        return ModelPackage.Literals.ECU_CONFIGURATION_MODEL;
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
            this.eNotify((Notification)new ENotificationImpl((InternalEObject)this, 1, 0, (Object)oldPathValue, (Object)this.pathValue));
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
    public EList<ModuleKindModel> getModuleKindModels() {
        if (this.moduleKindModels == null) {
            this.moduleKindModels = new EObjectContainmentEList(ModuleKindModel.class, (InternalEObject)this, 2);
        }
        return this.moduleKindModels;
    }

    @Override
    public IFile getFile() {
        return ResourcesPlugin.getWorkspace().getRoot().getProject(this.projectName).getFile(this.getPath());
    }

    @Override
    public IPath getPath() {
        return new Path(this.pathValue);
    }

    @Override
    public String getFileName() {
        return this.getFile().getParent().getName();
    }

    public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
        switch (featureID) {
            case 2: {
                return ((InternalEList)this.getModuleKindModels()).basicRemove((Object)otherEnd, msgs);
            }
        }
        return super.eInverseRemove(otherEnd, featureID, msgs);
    }

    public Object eGet(int featureID, boolean resolve, boolean coreType) {
        switch (featureID) {
            case 0: {
                return this.getPathValue();
            }
            case 1: {
                return this.getProjectName();
            }
            case 2: {
                return this.getModuleKindModels();
            }
        }
        return super.eGet(featureID, resolve, coreType);
    }

    public void eSet(int featureID, Object newValue) {
        switch (featureID) {
            case 0: {
                this.setPathValue((String)newValue);
                return;
            }
            case 1: {
                this.setProjectName((String)newValue);
                return;
            }
            case 2: {
                this.getModuleKindModels().clear();
                this.getModuleKindModels().addAll((Collection)newValue);
                return;
            }
        }
        super.eSet(featureID, newValue);
    }

    public void eUnset(int featureID) {
        switch (featureID) {
            case 0: {
                this.setPathValue(PATH_VALUE_EDEFAULT);
                return;
            }
            case 1: {
                this.setProjectName(PROJECT_NAME_EDEFAULT);
                return;
            }
            case 2: {
                this.getModuleKindModels().clear();
                return;
            }
        }
        super.eUnset(featureID);
    }

    public boolean eIsSet(int featureID) {
        switch (featureID) {
            case 0: {
                return PATH_VALUE_EDEFAULT == null ? this.pathValue != null : !PATH_VALUE_EDEFAULT.equals(this.pathValue);
            }
            case 1: {
                return PROJECT_NAME_EDEFAULT == null ? this.projectName != null : !PROJECT_NAME_EDEFAULT.equals(this.projectName);
            }
            case 2: {
                return this.moduleKindModels != null && !this.moduleKindModels.isEmpty();
            }
        }
        return super.eIsSet(featureID);
    }

    public Object eInvoke(int operationID, EList<?> arguments) throws InvocationTargetException {
        switch (operationID) {
            case 0: {
                return this.getFile();
            }
            case 1: {
                return this.getPath();
            }
            case 2: {
                return this.getFileName();
            }
        }
        return super.eInvoke(operationID, arguments);
    }

    public String toString() {
        if (this.eIsProxy()) {
            return super.toString();
        }
        StringBuffer result = new StringBuffer(super.toString());
        result.append(" (pathValue: ");
        result.append(this.pathValue);
        result.append(", projectName: ");
        result.append(this.projectName);
        result.append(')');
        return result.toString();
    }
}

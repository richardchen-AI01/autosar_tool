/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
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

import cn.com.myorg.mal.model.ModelPackage;
import cn.com.myorg.mal.model.ModuleKindModel;
import cn.com.myorg.mal.model.ModuleModel;
import java.lang.reflect.InvocationTargetException;
import java.util.Collection;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.notify.NotificationChain;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;
import org.eclipse.emf.ecore.util.EObjectContainmentEList;
import org.eclipse.emf.ecore.util.InternalEList;

public class ModuleKindModelImpl
extends MinimalEObjectImpl.Container
implements ModuleKindModel {
    protected static final String KIND_NAME_EDEFAULT = null;
    protected String kindName = KIND_NAME_EDEFAULT;
    protected EList<ModuleModel> moduleModels;

    protected ModuleKindModelImpl() {
    }

    protected EClass eStaticClass() {
        return ModelPackage.Literals.MODULE_KIND_MODEL;
    }

    @Override
    public String getKindName() {
        return this.kindName;
    }

    @Override
    public void setKindName(String newKindName) {
        String oldKindName = this.kindName;
        this.kindName = newKindName;
        if (this.eNotificationRequired()) {
            this.eNotify((Notification)new ENotificationImpl((InternalEObject)this, 1, 0, (Object)oldKindName, (Object)this.kindName));
        }
    }

    @Override
    public EList<ModuleModel> getModuleModels() {
        if (this.moduleModels == null) {
            this.moduleModels = new EObjectContainmentEList(ModuleModel.class, (InternalEObject)this, 1);
        }
        return this.moduleModels;
    }

    @Override
    public int hashCode() {
        int code = 0;
        for (ModuleModel config : this.getModuleModels()) {
            code += config.hashCode();
        }
        return code;
    }

    @Override
    public String toString() {
        String strToString = String.valueOf(this.kindName) + "[";
        for (ModuleModel configWrap : this.getModuleModels()) {
            strToString = String.valueOf(strToString) + configWrap.toString() + ", ";
        }
        strToString = String.valueOf(strToString) + "]";
        return strToString;
    }

    public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
        switch (featureID) {
            case 1: {
                return ((InternalEList)this.getModuleModels()).basicRemove((Object)otherEnd, msgs);
            }
        }
        return super.eInverseRemove(otherEnd, featureID, msgs);
    }

    public Object eGet(int featureID, boolean resolve, boolean coreType) {
        switch (featureID) {
            case 0: {
                return this.getKindName();
            }
            case 1: {
                return this.getModuleModels();
            }
        }
        return super.eGet(featureID, resolve, coreType);
    }

    public void eSet(int featureID, Object newValue) {
        switch (featureID) {
            case 0: {
                this.setKindName((String)newValue);
                return;
            }
            case 1: {
                this.getModuleModels().clear();
                this.getModuleModels().addAll((Collection)newValue);
                return;
            }
        }
        super.eSet(featureID, newValue);
    }

    public void eUnset(int featureID) {
        switch (featureID) {
            case 0: {
                this.setKindName(KIND_NAME_EDEFAULT);
                return;
            }
            case 1: {
                this.getModuleModels().clear();
                return;
            }
        }
        super.eUnset(featureID);
    }

    public boolean eIsSet(int featureID) {
        switch (featureID) {
            case 0: {
                return KIND_NAME_EDEFAULT == null ? this.kindName != null : !KIND_NAME_EDEFAULT.equals(this.kindName);
            }
            case 1: {
                return this.moduleModels != null && !this.moduleModels.isEmpty();
            }
        }
        return super.eIsSet(featureID);
    }

    public Object eInvoke(int operationID, EList<?> arguments) throws InvocationTargetException {
        switch (operationID) {
            case 0: {
                return this.hashCode();
            }
            case 1: {
                return this.toString();
            }
        }
        return super.eInvoke(operationID, arguments);
    }
}

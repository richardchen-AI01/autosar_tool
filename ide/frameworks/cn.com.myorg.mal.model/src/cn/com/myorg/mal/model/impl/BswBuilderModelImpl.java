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

import cn.com.myorg.mal.model.BswBuilderModel;
import cn.com.myorg.mal.model.EcuConfigurationModel;
import cn.com.myorg.mal.model.ModelPackage;
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

public class BswBuilderModelImpl
extends MinimalEObjectImpl.Container
implements BswBuilderModel {
    protected static final String NAME_EDEFAULT = null;
    protected String name = NAME_EDEFAULT;
    protected static final String PROJECT_NAME_EDEFAULT = null;
    protected String projectName = PROJECT_NAME_EDEFAULT;
    protected EList<EcuConfigurationModel> ecuConfigurationModels;

    protected BswBuilderModelImpl() {
    }

    protected EClass eStaticClass() {
        return ModelPackage.Literals.BSW_BUILDER_MODEL;
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public void setName(String newName) {
        String oldName = this.name;
        this.name = newName;
        if (this.eNotificationRequired()) {
            this.eNotify((Notification)new ENotificationImpl((InternalEObject)this, 1, 0, (Object)oldName, (Object)this.name));
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
    public EList<EcuConfigurationModel> getEcuConfigurationModels() {
        if (this.ecuConfigurationModels == null) {
            this.ecuConfigurationModels = new EObjectContainmentEList(EcuConfigurationModel.class, (InternalEObject)this, 2);
        }
        return this.ecuConfigurationModels;
    }

    public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
        switch (featureID) {
            case 2: {
                return ((InternalEList)this.getEcuConfigurationModels()).basicRemove((Object)otherEnd, msgs);
            }
        }
        return super.eInverseRemove(otherEnd, featureID, msgs);
    }

    public Object eGet(int featureID, boolean resolve, boolean coreType) {
        switch (featureID) {
            case 0: {
                return this.getName();
            }
            case 1: {
                return this.getProjectName();
            }
            case 2: {
                return this.getEcuConfigurationModels();
            }
        }
        return super.eGet(featureID, resolve, coreType);
    }

    public void eSet(int featureID, Object newValue) {
        switch (featureID) {
            case 0: {
                this.setName((String)newValue);
                return;
            }
            case 1: {
                this.setProjectName((String)newValue);
                return;
            }
            case 2: {
                this.getEcuConfigurationModels().clear();
                this.getEcuConfigurationModels().addAll((Collection)newValue);
                return;
            }
        }
        super.eSet(featureID, newValue);
    }

    public void eUnset(int featureID) {
        switch (featureID) {
            case 0: {
                this.setName(NAME_EDEFAULT);
                return;
            }
            case 1: {
                this.setProjectName(PROJECT_NAME_EDEFAULT);
                return;
            }
            case 2: {
                this.getEcuConfigurationModels().clear();
                return;
            }
        }
        super.eUnset(featureID);
    }

    public boolean eIsSet(int featureID) {
        switch (featureID) {
            case 0: {
                return NAME_EDEFAULT == null ? this.name != null : !NAME_EDEFAULT.equals(this.name);
            }
            case 1: {
                return PROJECT_NAME_EDEFAULT == null ? this.projectName != null : !PROJECT_NAME_EDEFAULT.equals(this.projectName);
            }
            case 2: {
                return this.ecuConfigurationModels != null && !this.ecuConfigurationModels.isEmpty();
            }
        }
        return super.eIsSet(featureID);
    }

    public String toString() {
        if (this.eIsProxy()) {
            return super.toString();
        }
        StringBuffer result = new StringBuffer(super.toString());
        result.append(" (name: ");
        result.append(this.name);
        result.append(", projectName: ");
        result.append(this.projectName);
        result.append(')');
        return result.toString();
    }
}

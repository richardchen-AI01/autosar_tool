/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  org.eclipse.emf.ecore.EObject
 *  org.eclipse.emf.ecore.EPackage
 *  org.eclipse.emf.ecore.util.Switch
 */
package cn.com.myorg.mal.model.util;

import cn.com.myorg.mal.model.BswBuilderModel;
import cn.com.myorg.mal.model.EcuConfigurationModel;
import cn.com.myorg.mal.model.ModelPackage;
import cn.com.myorg.mal.model.ModuleKindModel;
import cn.com.myorg.mal.model.ModuleModel;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.util.Switch;

public class ModelSwitch<T>
extends Switch<T> {
    protected static ModelPackage modelPackage;

    public ModelSwitch() {
        if (modelPackage == null) {
            modelPackage = ModelPackage.eINSTANCE;
        }
    }

    protected boolean isSwitchFor(EPackage ePackage) {
        return ePackage == modelPackage;
    }

    protected T doSwitch(int classifierID, EObject theEObject) {
        switch (classifierID) {
            case 0: {
                BswBuilderModel bswBuilderModel = (BswBuilderModel)theEObject;
                T result = this.caseBswBuilderModel(bswBuilderModel);
                if (result == null) {
                    result = this.defaultCase(theEObject);
                }
                return result;
            }
            case 1: {
                EcuConfigurationModel ecuConfigurationModel = (EcuConfigurationModel)theEObject;
                T result = this.caseEcuConfigurationModel(ecuConfigurationModel);
                if (result == null) {
                    result = this.defaultCase(theEObject);
                }
                return result;
            }
            case 2: {
                ModuleKindModel moduleKindModel = (ModuleKindModel)theEObject;
                T result = this.caseModuleKindModel(moduleKindModel);
                if (result == null) {
                    result = this.defaultCase(theEObject);
                }
                return result;
            }
            case 3: {
                ModuleModel moduleModel = (ModuleModel)theEObject;
                T result = this.caseModuleModel(moduleModel);
                if (result == null) {
                    result = this.defaultCase(theEObject);
                }
                return result;
            }
        }
        return this.defaultCase(theEObject);
    }

    public T caseBswBuilderModel(BswBuilderModel object) {
        return null;
    }

    public T caseEcuConfigurationModel(EcuConfigurationModel object) {
        return null;
    }

    public T caseModuleKindModel(ModuleKindModel object) {
        return null;
    }

    public T caseModuleModel(ModuleModel object) {
        return null;
    }

    public T defaultCase(EObject object) {
        return null;
    }
}

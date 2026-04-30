/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  org.eclipse.core.resources.IFile
 *  org.eclipse.core.runtime.IPath
 *  org.eclipse.emf.ecore.EClass
 *  org.eclipse.emf.ecore.EDataType
 *  org.eclipse.emf.ecore.EObject
 *  org.eclipse.emf.ecore.EPackage$Registry
 *  org.eclipse.emf.ecore.impl.EFactoryImpl
 *  org.eclipse.emf.ecore.plugin.EcorePlugin
 */
package cn.com.myorg.mal.model.impl;

import cn.com.myorg.mal.model.BswBuilderModel;
import cn.com.myorg.mal.model.EcuConfigurationModel;
import cn.com.myorg.mal.model.ModelFactory;
import cn.com.myorg.mal.model.ModelPackage;
import cn.com.myorg.mal.model.ModuleKindModel;
import cn.com.myorg.mal.model.ModuleModel;
import cn.com.myorg.mal.model.impl.BswBuilderModelImpl;
import cn.com.myorg.mal.model.impl.EcuConfigurationModelImpl;
import cn.com.myorg.mal.model.impl.ModuleKindModelImpl;
import cn.com.myorg.mal.model.impl.ModuleModelImpl;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.runtime.IPath;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EDataType;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.impl.EFactoryImpl;
import org.eclipse.emf.ecore.plugin.EcorePlugin;

public class ModelFactoryImpl
extends EFactoryImpl
implements ModelFactory {
    public static ModelFactory init() {
        try {
            ModelFactory theModelFactory = (ModelFactory)EPackage.Registry.INSTANCE.getEFactory("http:///cn/com/myorg/mal/model.ecore");
            if (theModelFactory != null) {
                return theModelFactory;
            }
        }
        catch (Exception exception) {
            EcorePlugin.INSTANCE.log((Object)exception);
        }
        return new ModelFactoryImpl();
    }

    public EObject create(EClass eClass) {
        switch (eClass.getClassifierID()) {
            case 0: {
                return this.createBswBuilderModel();
            }
            case 1: {
                return this.createEcuConfigurationModel();
            }
            case 2: {
                return this.createModuleKindModel();
            }
            case 3: {
                return this.createModuleModel();
            }
        }
        throw new IllegalArgumentException("The class '" + eClass.getName() + "' is not a valid classifier");
    }

    public Object createFromString(EDataType eDataType, String initialValue) {
        switch (eDataType.getClassifierID()) {
            case 4: {
                return this.createIFileFromString(eDataType, initialValue);
            }
            case 5: {
                return this.createIPathFromString(eDataType, initialValue);
            }
        }
        throw new IllegalArgumentException("The datatype '" + eDataType.getName() + "' is not a valid classifier");
    }

    public String convertToString(EDataType eDataType, Object instanceValue) {
        switch (eDataType.getClassifierID()) {
            case 4: {
                return this.convertIFileToString(eDataType, instanceValue);
            }
            case 5: {
                return this.convertIPathToString(eDataType, instanceValue);
            }
        }
        throw new IllegalArgumentException("The datatype '" + eDataType.getName() + "' is not a valid classifier");
    }

    @Override
    public BswBuilderModel createBswBuilderModel() {
        BswBuilderModelImpl bswBuilderModel = new BswBuilderModelImpl();
        return bswBuilderModel;
    }

    @Override
    public EcuConfigurationModel createEcuConfigurationModel() {
        EcuConfigurationModelImpl ecuConfigurationModel = new EcuConfigurationModelImpl();
        return ecuConfigurationModel;
    }

    @Override
    public ModuleKindModel createModuleKindModel() {
        ModuleKindModelImpl moduleKindModel = new ModuleKindModelImpl();
        return moduleKindModel;
    }

    @Override
    public ModuleModel createModuleModel() {
        ModuleModelImpl moduleModel = new ModuleModelImpl();
        return moduleModel;
    }

    public IFile createIFileFromString(EDataType eDataType, String initialValue) {
        return (IFile)super.createFromString(eDataType, initialValue);
    }

    public String convertIFileToString(EDataType eDataType, Object instanceValue) {
        return super.convertToString(eDataType, instanceValue);
    }

    public IPath createIPathFromString(EDataType eDataType, String initialValue) {
        return (IPath)super.createFromString(eDataType, initialValue);
    }

    public String convertIPathToString(EDataType eDataType, Object instanceValue) {
        return super.convertToString(eDataType, instanceValue);
    }

    @Override
    public ModelPackage getModelPackage() {
        return (ModelPackage)this.getEPackage();
    }

    @Deprecated
    public static ModelPackage getPackage() {
        return ModelPackage.eINSTANCE;
    }
}

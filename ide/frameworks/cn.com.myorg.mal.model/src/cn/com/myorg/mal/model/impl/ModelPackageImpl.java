/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  org.eclipse.core.resources.IFile
 *  org.eclipse.core.runtime.IPath
 *  org.eclipse.emf.ecore.EAttribute
 *  org.eclipse.emf.ecore.EClass
 *  org.eclipse.emf.ecore.EClassifier
 *  org.eclipse.emf.ecore.EDataType
 *  org.eclipse.emf.ecore.EFactory
 *  org.eclipse.emf.ecore.EOperation
 *  org.eclipse.emf.ecore.EPackage$Registry
 *  org.eclipse.emf.ecore.EReference
 *  org.eclipse.emf.ecore.impl.EPackageImpl
 */
package cn.com.myorg.mal.model.impl;

import cn.com.myorg.mal.model.BswBuilderModel;
import cn.com.myorg.mal.model.EcuConfigurationModel;
import cn.com.myorg.mal.model.ModelFactory;
import cn.com.myorg.mal.model.ModelPackage;
import cn.com.myorg.mal.model.ModuleKindModel;
import cn.com.myorg.mal.model.ModuleModel;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.runtime.IPath;
import org.eclipse.emf.ecore.EAttribute;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EClassifier;
import org.eclipse.emf.ecore.EDataType;
import org.eclipse.emf.ecore.EFactory;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EReference;
import org.eclipse.emf.ecore.impl.EPackageImpl;

public class ModelPackageImpl
extends EPackageImpl
implements ModelPackage {
    private EClass bswBuilderModelEClass = null;
    private EClass ecuConfigurationModelEClass = null;
    private EClass moduleKindModelEClass = null;
    private EClass moduleModelEClass = null;
    private EDataType iFileEDataType = null;
    private EDataType iPathEDataType = null;
    private static boolean isInited = false;
    private boolean isCreated = false;
    private boolean isInitialized = false;

    private ModelPackageImpl() {
        super("http:///cn/com/myorg/mal/model.ecore", (EFactory)ModelFactory.eINSTANCE);
    }

    public static ModelPackage init() {
        if (isInited) {
            return (ModelPackage)EPackage.Registry.INSTANCE.getEPackage("http:///cn/com/myorg/mal/model.ecore");
        }
        ModelPackageImpl theModelPackage = (ModelPackageImpl)(EPackage.Registry.INSTANCE.get("http:///cn/com/myorg/mal/model.ecore") instanceof ModelPackageImpl ? EPackage.Registry.INSTANCE.get("http:///cn/com/myorg/mal/model.ecore") : new ModelPackageImpl());
        isInited = true;
        theModelPackage.createPackageContents();
        theModelPackage.initializePackageContents();
        theModelPackage.freeze();
        EPackage.Registry.INSTANCE.put("http:///cn/com/myorg/mal/model.ecore", (Object)theModelPackage);
        return theModelPackage;
    }

    @Override
    public EClass getBswBuilderModel() {
        return this.bswBuilderModelEClass;
    }

    @Override
    public EAttribute getBswBuilderModel_Name() {
        return (EAttribute)this.bswBuilderModelEClass.getEStructuralFeatures().get(0);
    }

    @Override
    public EAttribute getBswBuilderModel_ProjectName() {
        return (EAttribute)this.bswBuilderModelEClass.getEStructuralFeatures().get(1);
    }

    @Override
    public EReference getBswBuilderModel_EcuConfigurationModels() {
        return (EReference)this.bswBuilderModelEClass.getEStructuralFeatures().get(2);
    }

    @Override
    public EClass getEcuConfigurationModel() {
        return this.ecuConfigurationModelEClass;
    }

    @Override
    public EAttribute getEcuConfigurationModel_PathValue() {
        return (EAttribute)this.ecuConfigurationModelEClass.getEStructuralFeatures().get(0);
    }

    @Override
    public EAttribute getEcuConfigurationModel_ProjectName() {
        return (EAttribute)this.ecuConfigurationModelEClass.getEStructuralFeatures().get(1);
    }

    @Override
    public EReference getEcuConfigurationModel_ModuleKindModels() {
        return (EReference)this.ecuConfigurationModelEClass.getEStructuralFeatures().get(2);
    }

    @Override
    public EOperation getEcuConfigurationModel__GetFile() {
        return (EOperation)this.ecuConfigurationModelEClass.getEOperations().get(0);
    }

    @Override
    public EOperation getEcuConfigurationModel__GetPath() {
        return (EOperation)this.ecuConfigurationModelEClass.getEOperations().get(1);
    }

    @Override
    public EOperation getEcuConfigurationModel__GetFileName() {
        return (EOperation)this.ecuConfigurationModelEClass.getEOperations().get(2);
    }

    @Override
    public EClass getModuleKindModel() {
        return this.moduleKindModelEClass;
    }

    @Override
    public EAttribute getModuleKindModel_KindName() {
        return (EAttribute)this.moduleKindModelEClass.getEStructuralFeatures().get(0);
    }

    @Override
    public EReference getModuleKindModel_ModuleModels() {
        return (EReference)this.moduleKindModelEClass.getEStructuralFeatures().get(1);
    }

    @Override
    public EOperation getModuleKindModel__HashCode() {
        return (EOperation)this.moduleKindModelEClass.getEOperations().get(0);
    }

    @Override
    public EOperation getModuleKindModel__ToString() {
        return (EOperation)this.moduleKindModelEClass.getEOperations().get(1);
    }

    @Override
    public EClass getModuleModel() {
        return this.moduleModelEClass;
    }

    @Override
    public EAttribute getModuleModel_ModuleName() {
        return (EAttribute)this.moduleModelEClass.getEStructuralFeatures().get(0);
    }

    @Override
    public EAttribute getModuleModel_ProjectName() {
        return (EAttribute)this.moduleModelEClass.getEStructuralFeatures().get(1);
    }

    @Override
    public EAttribute getModuleModel_PathValue() {
        return (EAttribute)this.moduleModelEClass.getEStructuralFeatures().get(2);
    }

    @Override
    public EOperation getModuleModel__GetKeyValue() {
        return (EOperation)this.moduleModelEClass.getEOperations().get(0);
    }

    @Override
    public EDataType getIFile() {
        return this.iFileEDataType;
    }

    @Override
    public EDataType getIPath() {
        return this.iPathEDataType;
    }

    @Override
    public ModelFactory getModelFactory() {
        return (ModelFactory)this.getEFactoryInstance();
    }

    public void createPackageContents() {
        if (this.isCreated) {
            return;
        }
        this.isCreated = true;
        this.bswBuilderModelEClass = this.createEClass(0);
        this.createEAttribute(this.bswBuilderModelEClass, 0);
        this.createEAttribute(this.bswBuilderModelEClass, 1);
        this.createEReference(this.bswBuilderModelEClass, 2);
        this.ecuConfigurationModelEClass = this.createEClass(1);
        this.createEAttribute(this.ecuConfigurationModelEClass, 0);
        this.createEAttribute(this.ecuConfigurationModelEClass, 1);
        this.createEReference(this.ecuConfigurationModelEClass, 2);
        this.createEOperation(this.ecuConfigurationModelEClass, 0);
        this.createEOperation(this.ecuConfigurationModelEClass, 1);
        this.createEOperation(this.ecuConfigurationModelEClass, 2);
        this.moduleKindModelEClass = this.createEClass(2);
        this.createEAttribute(this.moduleKindModelEClass, 0);
        this.createEReference(this.moduleKindModelEClass, 1);
        this.createEOperation(this.moduleKindModelEClass, 0);
        this.createEOperation(this.moduleKindModelEClass, 1);
        this.moduleModelEClass = this.createEClass(3);
        this.createEAttribute(this.moduleModelEClass, 0);
        this.createEAttribute(this.moduleModelEClass, 1);
        this.createEAttribute(this.moduleModelEClass, 2);
        this.createEOperation(this.moduleModelEClass, 0);
        this.iFileEDataType = this.createEDataType(4);
        this.iPathEDataType = this.createEDataType(5);
    }

    public void initializePackageContents() {
        if (this.isInitialized) {
            return;
        }
        this.isInitialized = true;
        this.setName("model");
        this.setNsPrefix("cn.com.myorg.mal.model");
        this.setNsURI("http:///cn/com/myorg/mal/model.ecore");
        this.initEClass(this.bswBuilderModelEClass, BswBuilderModel.class, "BswBuilderModel", false, false, true);
        this.initEAttribute(this.getBswBuilderModel_Name(), (EClassifier)this.ecorePackage.getEString(), "name", null, 1, 1, BswBuilderModel.class, false, false, true, false, false, true, false, true);
        this.initEAttribute(this.getBswBuilderModel_ProjectName(), (EClassifier)this.ecorePackage.getEString(), "projectName", null, 1, 1, BswBuilderModel.class, false, false, true, false, false, true, false, true);
        this.initEReference(this.getBswBuilderModel_EcuConfigurationModels(), (EClassifier)this.getEcuConfigurationModel(), null, "ecuConfigurationModels", null, 0, -1, BswBuilderModel.class, false, false, true, true, false, false, true, false, true);
        this.initEClass(this.ecuConfigurationModelEClass, EcuConfigurationModel.class, "EcuConfigurationModel", false, false, true);
        this.initEAttribute(this.getEcuConfigurationModel_PathValue(), (EClassifier)this.ecorePackage.getEString(), "pathValue", null, 1, 1, EcuConfigurationModel.class, false, false, true, false, false, true, false, true);
        this.initEAttribute(this.getEcuConfigurationModel_ProjectName(), (EClassifier)this.ecorePackage.getEString(), "projectName", null, 1, 1, EcuConfigurationModel.class, false, false, true, false, false, true, false, true);
        this.initEReference(this.getEcuConfigurationModel_ModuleKindModels(), (EClassifier)this.getModuleKindModel(), null, "moduleKindModels", null, 0, -1, EcuConfigurationModel.class, false, false, true, true, false, false, true, false, true);
        this.initEOperation(this.getEcuConfigurationModel__GetFile(), (EClassifier)this.getIFile(), "getFile", 0, 1, true, true);
        this.initEOperation(this.getEcuConfigurationModel__GetPath(), (EClassifier)this.getIPath(), "getPath", 0, 1, true, true);
        this.initEOperation(this.getEcuConfigurationModel__GetFileName(), (EClassifier)this.ecorePackage.getEString(), "getFileName", 0, 1, true, true);
        this.initEClass(this.moduleKindModelEClass, ModuleKindModel.class, "ModuleKindModel", false, false, true);
        this.initEAttribute(this.getModuleKindModel_KindName(), (EClassifier)this.ecorePackage.getEString(), "kindName", null, 1, 1, ModuleKindModel.class, false, false, true, false, false, true, false, true);
        this.initEReference(this.getModuleKindModel_ModuleModels(), (EClassifier)this.getModuleModel(), null, "moduleModels", null, 0, -1, ModuleKindModel.class, false, false, true, true, false, false, true, false, true);
        this.initEOperation(this.getModuleKindModel__HashCode(), (EClassifier)this.ecorePackage.getEInt(), "hashCode", 0, 1, true, true);
        this.initEOperation(this.getModuleKindModel__ToString(), (EClassifier)this.ecorePackage.getEString(), "toString", 0, 1, true, true);
        this.initEClass(this.moduleModelEClass, ModuleModel.class, "ModuleModel", false, false, true);
        this.initEAttribute(this.getModuleModel_ModuleName(), (EClassifier)this.ecorePackage.getEString(), "moduleName", null, 1, 1, ModuleModel.class, false, false, true, false, false, true, false, true);
        this.initEAttribute(this.getModuleModel_ProjectName(), (EClassifier)this.ecorePackage.getEString(), "projectName", null, 1, 1, ModuleModel.class, false, false, true, false, false, true, false, true);
        this.initEAttribute(this.getModuleModel_PathValue(), (EClassifier)this.ecorePackage.getEString(), "pathValue", null, 1, 1, ModuleModel.class, false, false, true, false, false, true, false, true);
        this.initEOperation(this.getModuleModel__GetKeyValue(), (EClassifier)this.ecorePackage.getEString(), "getKeyValue", 0, 1, true, true);
        this.initEDataType(this.iFileEDataType, IFile.class, "IFile", true, false);
        this.initEDataType(this.iPathEDataType, IPath.class, "IPath", true, false);
        this.createResource("http:///cn/com/myorg/mal/model.ecore");
    }
}

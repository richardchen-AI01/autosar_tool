/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  org.eclipse.emf.ecore.EAttribute
 *  org.eclipse.emf.ecore.EClass
 *  org.eclipse.emf.ecore.EDataType
 *  org.eclipse.emf.ecore.EOperation
 *  org.eclipse.emf.ecore.EPackage
 *  org.eclipse.emf.ecore.EReference
 */
package cn.com.myorg.mal.model;

import cn.com.myorg.mal.model.ModelFactory;
import cn.com.myorg.mal.model.impl.ModelPackageImpl;
import org.eclipse.emf.ecore.EAttribute;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EDataType;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EReference;

public interface ModelPackage
extends EPackage {
    public static final String eNAME = "model";
    public static final String eNS_URI = "http:///cn/com/myorg/mal/model.ecore";
    public static final String eNS_PREFIX = "cn.com.myorg.mal.model";
    public static final ModelPackage eINSTANCE = ModelPackageImpl.init();
    public static final int BSW_BUILDER_MODEL = 0;
    public static final int BSW_BUILDER_MODEL__NAME = 0;
    public static final int BSW_BUILDER_MODEL__PROJECT_NAME = 1;
    public static final int BSW_BUILDER_MODEL__ECU_CONFIGURATION_MODELS = 2;
    public static final int BSW_BUILDER_MODEL_FEATURE_COUNT = 3;
    public static final int BSW_BUILDER_MODEL_OPERATION_COUNT = 0;
    public static final int ECU_CONFIGURATION_MODEL = 1;
    public static final int ECU_CONFIGURATION_MODEL__PATH_VALUE = 0;
    public static final int ECU_CONFIGURATION_MODEL__PROJECT_NAME = 1;
    public static final int ECU_CONFIGURATION_MODEL__MODULE_KIND_MODELS = 2;
    public static final int ECU_CONFIGURATION_MODEL_FEATURE_COUNT = 3;
    public static final int ECU_CONFIGURATION_MODEL___GET_FILE = 0;
    public static final int ECU_CONFIGURATION_MODEL___GET_PATH = 1;
    public static final int ECU_CONFIGURATION_MODEL___GET_FILE_NAME = 2;
    public static final int ECU_CONFIGURATION_MODEL_OPERATION_COUNT = 3;
    public static final int MODULE_KIND_MODEL = 2;
    public static final int MODULE_KIND_MODEL__KIND_NAME = 0;
    public static final int MODULE_KIND_MODEL__MODULE_MODELS = 1;
    public static final int MODULE_KIND_MODEL_FEATURE_COUNT = 2;
    public static final int MODULE_KIND_MODEL___HASH_CODE = 0;
    public static final int MODULE_KIND_MODEL___TO_STRING = 1;
    public static final int MODULE_KIND_MODEL_OPERATION_COUNT = 2;
    public static final int MODULE_MODEL = 3;
    public static final int MODULE_MODEL__MODULE_NAME = 0;
    public static final int MODULE_MODEL__PROJECT_NAME = 1;
    public static final int MODULE_MODEL__PATH_VALUE = 2;
    public static final int MODULE_MODEL_FEATURE_COUNT = 3;
    public static final int MODULE_MODEL___GET_KEY_VALUE = 0;
    public static final int MODULE_MODEL_OPERATION_COUNT = 1;
    public static final int IFILE = 4;
    public static final int IPATH = 5;

    public EClass getBswBuilderModel();

    public EAttribute getBswBuilderModel_Name();

    public EAttribute getBswBuilderModel_ProjectName();

    public EReference getBswBuilderModel_EcuConfigurationModels();

    public EClass getEcuConfigurationModel();

    public EAttribute getEcuConfigurationModel_PathValue();

    public EAttribute getEcuConfigurationModel_ProjectName();

    public EReference getEcuConfigurationModel_ModuleKindModels();

    public EOperation getEcuConfigurationModel__GetFile();

    public EOperation getEcuConfigurationModel__GetPath();

    public EOperation getEcuConfigurationModel__GetFileName();

    public EClass getModuleKindModel();

    public EAttribute getModuleKindModel_KindName();

    public EReference getModuleKindModel_ModuleModels();

    public EOperation getModuleKindModel__HashCode();

    public EOperation getModuleKindModel__ToString();

    public EClass getModuleModel();

    public EAttribute getModuleModel_ModuleName();

    public EAttribute getModuleModel_ProjectName();

    public EAttribute getModuleModel_PathValue();

    public EOperation getModuleModel__GetKeyValue();

    public EDataType getIFile();

    public EDataType getIPath();

    public ModelFactory getModelFactory();

    public static interface Literals {
        public static final EClass BSW_BUILDER_MODEL = eINSTANCE.getBswBuilderModel();
        public static final EAttribute BSW_BUILDER_MODEL__NAME = eINSTANCE.getBswBuilderModel_Name();
        public static final EAttribute BSW_BUILDER_MODEL__PROJECT_NAME = eINSTANCE.getBswBuilderModel_ProjectName();
        public static final EReference BSW_BUILDER_MODEL__ECU_CONFIGURATION_MODELS = eINSTANCE.getBswBuilderModel_EcuConfigurationModels();
        public static final EClass ECU_CONFIGURATION_MODEL = eINSTANCE.getEcuConfigurationModel();
        public static final EAttribute ECU_CONFIGURATION_MODEL__PATH_VALUE = eINSTANCE.getEcuConfigurationModel_PathValue();
        public static final EAttribute ECU_CONFIGURATION_MODEL__PROJECT_NAME = eINSTANCE.getEcuConfigurationModel_ProjectName();
        public static final EReference ECU_CONFIGURATION_MODEL__MODULE_KIND_MODELS = eINSTANCE.getEcuConfigurationModel_ModuleKindModels();
        public static final EOperation ECU_CONFIGURATION_MODEL___GET_FILE = eINSTANCE.getEcuConfigurationModel__GetFile();
        public static final EOperation ECU_CONFIGURATION_MODEL___GET_PATH = eINSTANCE.getEcuConfigurationModel__GetPath();
        public static final EOperation ECU_CONFIGURATION_MODEL___GET_FILE_NAME = eINSTANCE.getEcuConfigurationModel__GetFileName();
        public static final EClass MODULE_KIND_MODEL = eINSTANCE.getModuleKindModel();
        public static final EAttribute MODULE_KIND_MODEL__KIND_NAME = eINSTANCE.getModuleKindModel_KindName();
        public static final EReference MODULE_KIND_MODEL__MODULE_MODELS = eINSTANCE.getModuleKindModel_ModuleModels();
        public static final EOperation MODULE_KIND_MODEL___HASH_CODE = eINSTANCE.getModuleKindModel__HashCode();
        public static final EOperation MODULE_KIND_MODEL___TO_STRING = eINSTANCE.getModuleKindModel__ToString();
        public static final EClass MODULE_MODEL = eINSTANCE.getModuleModel();
        public static final EAttribute MODULE_MODEL__MODULE_NAME = eINSTANCE.getModuleModel_ModuleName();
        public static final EAttribute MODULE_MODEL__PROJECT_NAME = eINSTANCE.getModuleModel_ProjectName();
        public static final EAttribute MODULE_MODEL__PATH_VALUE = eINSTANCE.getModuleModel_PathValue();
        public static final EOperation MODULE_MODEL___GET_KEY_VALUE = eINSTANCE.getModuleModel__GetKeyValue();
        public static final EDataType IFILE = eINSTANCE.getIFile();
        public static final EDataType IPATH = eINSTANCE.getIPath();
    }
}

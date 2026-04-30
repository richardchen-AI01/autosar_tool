/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  org.eclipse.emf.common.notify.Adapter
 *  org.eclipse.emf.common.notify.Notifier
 *  org.eclipse.emf.common.notify.impl.AdapterFactoryImpl
 *  org.eclipse.emf.ecore.EObject
 */
package cn.com.myorg.mal.model.util;

import cn.com.myorg.mal.model.BswBuilderModel;
import cn.com.myorg.mal.model.EcuConfigurationModel;
import cn.com.myorg.mal.model.ModelPackage;
import cn.com.myorg.mal.model.ModuleKindModel;
import cn.com.myorg.mal.model.ModuleModel;
import cn.com.myorg.mal.model.util.ModelSwitch;
import org.eclipse.emf.common.notify.Adapter;
import org.eclipse.emf.common.notify.Notifier;
import org.eclipse.emf.common.notify.impl.AdapterFactoryImpl;
import org.eclipse.emf.ecore.EObject;

public class ModelAdapterFactory
extends AdapterFactoryImpl {
    protected static ModelPackage modelPackage;
    protected ModelSwitch<Adapter> modelSwitch = new ModelSwitch<Adapter>(){

        @Override
        public Adapter caseBswBuilderModel(BswBuilderModel object) {
            return ModelAdapterFactory.this.createBswBuilderModelAdapter();
        }

        @Override
        public Adapter caseEcuConfigurationModel(EcuConfigurationModel object) {
            return ModelAdapterFactory.this.createEcuConfigurationModelAdapter();
        }

        @Override
        public Adapter caseModuleKindModel(ModuleKindModel object) {
            return ModelAdapterFactory.this.createModuleKindModelAdapter();
        }

        @Override
        public Adapter caseModuleModel(ModuleModel object) {
            return ModelAdapterFactory.this.createModuleModelAdapter();
        }

        @Override
        public Adapter defaultCase(EObject object) {
            return ModelAdapterFactory.this.createEObjectAdapter();
        }
    };

    public ModelAdapterFactory() {
        if (modelPackage == null) {
            modelPackage = ModelPackage.eINSTANCE;
        }
    }

    public boolean isFactoryForType(Object object) {
        if (object == modelPackage) {
            return true;
        }
        if (object instanceof EObject) {
            return ((EObject)object).eClass().getEPackage() == modelPackage;
        }
        return false;
    }

    public Adapter createAdapter(Notifier target) {
        return (Adapter)this.modelSwitch.doSwitch((EObject)target);
    }

    public Adapter createBswBuilderModelAdapter() {
        return null;
    }

    public Adapter createEcuConfigurationModelAdapter() {
        return null;
    }

    public Adapter createModuleKindModelAdapter() {
        return null;
    }

    public Adapter createModuleModelAdapter() {
        return null;
    }

    public Adapter createEObjectAdapter() {
        return null;
    }
}

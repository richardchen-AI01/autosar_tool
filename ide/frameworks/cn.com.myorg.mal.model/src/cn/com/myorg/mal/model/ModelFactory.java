/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  org.eclipse.emf.ecore.EFactory
 */
package cn.com.myorg.mal.model;

import cn.com.myorg.mal.model.BswBuilderModel;
import cn.com.myorg.mal.model.EcuConfigurationModel;
import cn.com.myorg.mal.model.ModelPackage;
import cn.com.myorg.mal.model.ModuleKindModel;
import cn.com.myorg.mal.model.ModuleModel;
import cn.com.myorg.mal.model.impl.ModelFactoryImpl;
import org.eclipse.emf.ecore.EFactory;

public interface ModelFactory
extends EFactory {
    public static final ModelFactory eINSTANCE = ModelFactoryImpl.init();

    public BswBuilderModel createBswBuilderModel();

    public EcuConfigurationModel createEcuConfigurationModel();

    public ModuleKindModel createModuleKindModel();

    public ModuleModel createModuleModel();

    public ModelPackage getModelPackage();
}

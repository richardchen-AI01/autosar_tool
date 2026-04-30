/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  org.eclipse.emf.common.util.EList
 *  org.eclipse.emf.ecore.EObject
 */
package cn.com.myorg.mal.model;

import cn.com.myorg.mal.model.EcuConfigurationModel;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EObject;

public interface BswBuilderModel
extends EObject {
    public String getName();

    public void setName(String var1);

    public String getProjectName();

    public void setProjectName(String var1);

    public EList<EcuConfigurationModel> getEcuConfigurationModels();
}

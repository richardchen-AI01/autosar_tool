/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  org.eclipse.emf.common.util.EList
 *  org.eclipse.emf.ecore.EObject
 */
package cn.com.myorg.mal.model;

import cn.com.myorg.mal.model.ModuleModel;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EObject;

public interface ModuleKindModel
extends EObject {
    public String getKindName();

    public void setKindName(String var1);

    public EList<ModuleModel> getModuleModels();

    public int hashCode();

    public String toString();
}

/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  org.eclipse.emf.ecore.EObject
 */
package cn.com.myorg.mal.model;

import org.eclipse.emf.ecore.EObject;

public interface ModuleModel
extends EObject {
    public String getModuleName();

    public void setModuleName(String var1);

    public String getProjectName();

    public void setProjectName(String var1);

    public String getPathValue();

    public void setPathValue(String var1);

    public String getKeyValue();
}

/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  org.eclipse.core.resources.IFile
 *  org.eclipse.core.runtime.IPath
 *  org.eclipse.emf.common.util.EList
 *  org.eclipse.emf.ecore.EObject
 */
package cn.com.myorg.mal.model;

import cn.com.myorg.mal.model.ModuleKindModel;
import org.eclipse.core.resources.IFile;
import org.eclipse.core.runtime.IPath;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EObject;

public interface EcuConfigurationModel
extends EObject {
    public String getPathValue();

    public void setPathValue(String var1);

    public String getProjectName();

    public void setProjectName(String var1);

    public EList<ModuleKindModel> getModuleKindModels();

    public IFile getFile();

    public IPath getPath();

    public String getFileName();
}

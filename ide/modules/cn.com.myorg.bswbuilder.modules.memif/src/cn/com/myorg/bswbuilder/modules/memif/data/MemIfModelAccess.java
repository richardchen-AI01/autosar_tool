package cn.com.myorg.bswbuilder.modules.memif.data;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.NullProgressMonitor;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.transaction.TransactionalEditingDomain;
import org.eclipse.sphinx.emf.util.EcorePlatformUtil;
import org.eclipse.sphinx.emf.util.WorkspaceEditingDomainUtil;
import org.eclipse.sphinx.emf.workspace.loading.ModelLoadManager;

/**
 * EMF model facade — replaces v0.1's regex-based {@link MemIfArxmlReader}.
 *
 * <p>v0.2 切到 EMF 路线 (REFERENCE_STACK §7 决定的 Q1 = 全 EMF)。读路径
 * 从字符串解析切到 Sphinx ResourceSet load, 取 typed
 * {@code EcucModuleConfigurationValues} EObject。
 *
 * <p>三步加载模式 — **照搬参考 iSoft `cn.com.isoft.pal.model.ModelManager`
 * 反编结果**:
 * <pre>
 *   1. ModelLoadManager.INSTANCE.loadFile(iFile, false, monitor)
 *   2. WorkspaceEditingDomainUtil.getEditingDomain(iFile) -> TransactionalEditingDomain
 *   3. EcorePlatformUtil.getModelRoot(domain, iFile) -> EObject
 * </pre>
 *
 * <p>v0.1 旧 {@link MemIfArxmlReader} 暂保留作回归对照, v0.2 完整切完后会删。
 */
public final class MemIfModelAccess {

    private MemIfModelAccess() {}

    /**
     * Load an .arxml file via Sphinx and return its root EObject.
     * Returns {@code null} if the file is not loaded into any
     * Sphinx-managed editing domain (most likely the project doesn't
     * have an AUTOSAR nature or the metamodel descriptor isn't matched).
     */
    public static EObject loadModelRoot(IFile arxml) {
        return loadModelRoot(arxml, new NullProgressMonitor());
    }

    public static EObject loadModelRoot(IFile arxml, IProgressMonitor monitor) {
        if (arxml == null || !arxml.exists()) return null;

        // 1. load (synchronous — async=false for predictable behaviour in
        //    spike / inline calls; iSoft does the same in ModelManager).
        ModelLoadManager.INSTANCE.loadFile(arxml, false, monitor);

        // 2. resolve editing domain
        TransactionalEditingDomain domain =
                WorkspaceEditingDomainUtil.getEditingDomain(arxml);
        if (domain == null) return null;

        // 3. fetch root EObject from the resource attached to that domain
        return EcorePlatformUtil.getModelRoot(domain, arxml);
    }
}

package cn.com.myorg.bswbuilder.ui.editors;

import java.io.File;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.ui.IEditorInput;
import org.eclipse.ui.IEditorSite;
import org.eclipse.ui.IFileEditorInput;
import org.eclipse.ui.IPathEditorInput;
import org.eclipse.ui.PartInitException;
import org.eclipse.ui.forms.editor.FormEditor;

import cn.com.myorg.bswbuilder.modules.memif.data.MemIfModelAccess;
import cn.com.myorg.bswbuilder.ui.editor.pages.GenericGeneralFormPage;
import cn.com.myorg.bswbuilder.ui.editor.pages.GenericMasterDetailFormPage;
import cn.com.myorg.bswbuilder.ui.schema.BswSchemaLoader;
import gautosar.gecucdescription.GModuleConfiguration;
import gautosar.gecucparameterdef.GContainerDef;
import gautosar.gecucparameterdef.GModuleDef;

/**
 * Generic multi-page form editor for any BSW module's ECUC ARXML.
 *
 * <p>跟参考 V25.10 cn.com.isoft.bswbuilder.ui.editor.NewBswBuilderEditor 同
 * pattern (反编 addPages 的 GModuleDef.gGetContainers() 循环 1:1 对齐):
 * <ol>
 *   <li>从 IEditorInput 解析 .arxml 文件 → Sphinx EditingDomain 加载得到
 *       {@link GModuleConfiguration} 实例 (instance side, EObject)</li>
 *   <li>{@link BswSchemaLoader#resolveDef} 拿到 {@link GModuleDef} (schema)
 *       — Def.arxml 自动从 module bundle load 进同 ResourceSet</li>
 *   <li>遍历 def.gGetContainers() → 单实例容器加 GenericGeneralFormPage,
 *       多实例加 GenericMasterDetailFormPage</li>
 * </ol>
 *
 * <p>替代之前 MemIf 专用的 MemIfModuleManagerEditor: 一个类服务所有模块, 加
 * 新模块只要 plugin.xml 注册 + 写 BSWMD/Def, 0 行 UI 代码。
 *
 * <p>v0.2 first cut 不做的:
 * <ul>
 *   <li>Save / dirty 跟踪 (本类 doSave 现在 no-op, page collectChangedParams
 *       只输出 delta 没写回, E5-4 v2 接 EcucArxmlWriter generalize 后实现)</li>
 *   <li>Cross-module REF chooser dialog (留 v0.3)</li>
 *   <li>BSWMD descriptor file 拒打开守卫 (跟参考 V25.10 一致 — bswmds/
 *       走 navigator filter 路径, editor 端不再特殊检测)</li>
 * </ul>
 */
public class GenericModuleEditor extends FormEditor {

    public static final String ID =
            "cn.com.myorg.bswbuilder.ui.editors.GenericModuleEditor";

    private File arxmlFile;
    private IFile arxmlIFile;
    private GModuleConfiguration module;
    private GModuleDef moduleDef;
    private boolean dirty;

    @Override
    public void init(IEditorSite site, IEditorInput input) throws PartInitException {
        if (input instanceof IFileEditorInput) {
            this.arxmlIFile = ((IFileEditorInput) input).getFile();
        }
        File f = resolveFile(input);
        if (f == null) {
            throw new PartInitException(
                    "Unsupported editor input: " + input.getClass().getName());
        }
        if (!f.isFile()) {
            throw new PartInitException("ARXML file not found: " + f.getAbsolutePath());
        }
        this.arxmlFile = f;

        // Load instance via Sphinx — reuses existing MemIfModelAccess
        // (despite name, it's module-agnostic — just calls Sphinx
        // ModelLoadManager + WorkspaceEditingDomainUtil to get the EObject).
        if (this.arxmlIFile != null) {
            EObject root = MemIfModelAccess.loadModelRoot(this.arxmlIFile);
            this.module = findModuleConfiguration(root);
        }
        if (this.module == null) {
            throw new PartInitException(
                    "Could not load GModuleConfiguration from " + f.getName()
                  + ". Ensure the file has AUTOSAR nature + Sphinx EditingDomain wired.");
        }
        // E5-1: resolve schema (loads <Module>Def.arxml from module bundle if needed).
        this.moduleDef = BswSchemaLoader.resolveDef(this.module);

        super.init(site, input);
        setPartName(f.getName());
    }

    /** Walk the loaded EObject tree for the first GModuleConfiguration. */
    private static GModuleConfiguration findModuleConfiguration(EObject root) {
        if (root == null) return null;
        if (root instanceof GModuleConfiguration) return (GModuleConfiguration) root;
        org.eclipse.emf.common.util.TreeIterator<EObject> it = root.eAllContents();
        while (it.hasNext()) {
            EObject obj = it.next();
            if (obj instanceof GModuleConfiguration) return (GModuleConfiguration) obj;
        }
        return null;
    }

    @Override
    protected void addPages() {
        if (module == null) return;
        if (moduleDef == null) {
            // No schema — fall back to a single empty placeholder so the editor
            // still opens (user sees empty form rather than crash).
            return;
        }
        // Mirrors reference V25.10 NewBswBuilderEditor.addPages():
        for (GContainerDef cdef : moduleDef.gGetContainers()) {
            try {
                if (useGeneralPage(cdef)) {
                    addPage(new GenericGeneralFormPage(this, module, cdef));
                } else {
                    addPage(new GenericMasterDetailFormPage(this, module, cdef));
                }
            } catch (PartInitException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * Page-picker decision: single-instance container → General page; multi
     * → MasterDetail. Reference V25.10 only checks GENERAL_FLAG SDG option
     * (not present in our Def files); we fall back to multiplicity check via
     * {@link gautosar.gecucparameterdef.GParamConfMultiplicity}.
     */
    private static boolean useGeneralPage(GContainerDef cdef) {
        // gGetUpperMultiplicityInfinite — true means unbounded (* = multi)
        Boolean infinite = cdef.gGetUpperMultiplicityInfinite();
        if (Boolean.TRUE.equals(infinite)) return false;

        // gGetUpperMultiplicityAsString — null/empty defaults to 1, ">1" multi
        String upperStr = cdef.gGetUpperMultiplicityAsString();
        if (upperStr == null || upperStr.isEmpty()) return true;  // default 1
        try {
            return Long.parseLong(upperStr.trim()) <= 1;
        } catch (NumberFormatException nfe) {
            return true;  // unparseable → assume general (safer than master-detail)
        }
    }

    private static File resolveFile(IEditorInput input) {
        if (input instanceof IFileEditorInput) {
            IFile rf = ((IFileEditorInput) input).getFile();
            if (rf != null) {
                org.eclipse.core.runtime.IPath loc = rf.getLocation();
                if (loc != null) return loc.toFile();
            }
            return null;
        }
        if (input instanceof IPathEditorInput) {
            return ((IPathEditorInput) input).getPath().toFile();
        }
        return null;
    }

    // ============================================================ save / dirty

    public void setDirty(boolean d) {
        if (this.dirty == d) return;
        this.dirty = d;
        org.eclipse.swt.widgets.Display.getDefault().asyncExec(new Runnable() {
            @Override public void run() { firePropertyChange(PROP_DIRTY); }
        });
    }

    @Override public boolean isDirty() { return dirty; }
    @Override public boolean isSaveAsAllowed() { return false; }

    @Override
    public void doSave(IProgressMonitor monitor) {
        // E5-4 v2 接 EcucArxmlWriter generalize → 收 page.collectChangedParams() 写回。
        // 本版只把 dirty=false, 让 editor 关闭流程不弹保存 prompt。
        // (Save 实际写盘逻辑 v0.3 接 EMF transactional)
        setDirty(false);
    }

    @Override public void doSaveAs() { /* not supported */ }

    public File getArxmlFile() { return arxmlFile; }
    public GModuleConfiguration getModule() { return module; }
    public GModuleDef getModuleDef() { return moduleDef; }
}

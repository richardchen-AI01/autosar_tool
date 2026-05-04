package cn.com.myorg.bswbuilder.ui.editors;

import java.io.File;

import org.eclipse.core.resources.IFile;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.sphinx.emf.editors.forms.BasicTransactionalFormEditor;
import org.eclipse.ui.IEditorInput;
import org.eclipse.ui.IEditorSite;
import org.eclipse.ui.IFileEditorInput;
import org.eclipse.ui.IPathEditorInput;
import org.eclipse.ui.PartInitException;

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
 * pattern (反编 NewBswBuilderEditor 的继承链):
 * <pre>
 *   Sphinx.BasicTransactionalFormEditor
 *     └─ AbstractBuilderEditor (pal jar)
 *         └─ EcuConfigurationEditor (pal jar)
 *             └─ NewBswBuilderEditor
 * </pre>
 * 我们直接继承 {@link BasicTransactionalFormEditor} 拿到 Sphinx 的:
 * <ul>
 *   <li>EditingDomain 自动绑定 (init 流程里查 ResourceSet → TransactionalEditingDomain)</li>
 *   <li>dirty tracking (CommandStack 监听 → setDirty 自动 fire PROP_DIRTY)</li>
 *   <li>doSave 写盘 (Resource.save via transactional, 不需要我们 string-surgery)</li>
 *   <li>undo/redo (CommandStack)</li>
 *   <li>外部修改检测 (BasicTransactionalFormEditorInputChangeHandler)</li>
 * </ul>
 *
 * <p>E5-6 整顿前 (E5-4 ~ E5-5) 直接 extends FormEditor + 手撸 dirty 字段 + doSave no-op,
 * 是 U2 commit 9bb216e 的路线债泛化结果 — 见 memory feedback_align_reference_three_layers.md。
 */
public class GenericModuleEditor extends BasicTransactionalFormEditor {

    public static final String ID =
            "cn.com.myorg.bswbuilder.ui.editors.GenericModuleEditor";

    private File arxmlFile;
    private IFile arxmlIFile;
    private GModuleConfiguration module;
    private GModuleDef moduleDef;
    /** init 失败原因; addPages 时降级到 fallback page 展示给用户. */
    private String initFailure;

    @Override
    public void init(IEditorSite site, IEditorInput input) {
        // BTFE.init 不抛 PartInitException (Sphinx 收紧了 throws 子句),
        // 我们只能内部 catch + 把错记到 initFailure, 由 addPages 走 fallback。
        try {
            if (input instanceof IFileEditorInput) {
                this.arxmlIFile = ((IFileEditorInput) input).getFile();
            }
            File f = resolveFile(input);
            if (f == null) {
                this.initFailure = "Unsupported editor input: " + input.getClass().getName();
            } else if (!f.isFile()) {
                this.initFailure = "ARXML file not found: " + f.getAbsolutePath();
            } else {
                this.arxmlFile = f;
                setPartName(f.getName());
            }
        } catch (Throwable t) {
            this.initFailure = "init: " + t.getClass().getSimpleName() + ": " + t.getMessage();
        }

        // Sphinx super.init 接管 EditingDomain / dirty / save 接驳
        super.init(site, input);

        // 加载 instance EObject — 复用现有 MemIfModelAccess (实际是 module-agnostic
        // 包装 Sphinx ModelLoadManager + WorkspaceEditingDomainUtil).
        if (this.arxmlFile != null && this.arxmlIFile != null) {
            try {
                EObject root = MemIfModelAccess.loadModelRoot(this.arxmlIFile);
                this.module = findModuleConfiguration(root);
                if (this.module == null) {
                    this.initFailure = "Could not load GModuleConfiguration from " + arxmlFile.getName()
                            + ". Ensure the file has AUTOSAR nature + Sphinx EditingDomain wired.";
                } else {
                    this.moduleDef = BswSchemaLoader.resolveDef(this.module);
                }
            } catch (Throwable t) {
                this.initFailure = "model load: " + t.getClass().getSimpleName() + ": " + t.getMessage();
            }
        }
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
        // S2 探针: 验证 super.init 是否接管成功 (super.getEditingDomain / getModelRoot 不空)。
        cn.com.myorg.bswbuilder.ui.editor.utils.EcucWriteActions.probeBindings(this,
                "addPages " + (module == null ? "<no module>" : module.gGetShortName()));

        // Mirrors reference V25.10 NewBswBuilderEditor.addPages().
        int added = 0;
        if (module != null && moduleDef != null) {
            for (GContainerDef cdef : moduleDef.gGetContainers()) {
                try {
                    // 99% 复刻 — 参考 V25.10 单实例 / 多实例 def 都走 3 栏
                    // master-detail 布局 (reference/ui MemIfGeneral 截图实证).
                    // GenericGeneralFormPage 现遗留, 删派发, 全走 master-detail.
                    addPage(new GenericMasterDetailFormPage(this, module, cdef));
                    added++;
                } catch (PartInitException e) {
                    System.err.println("[GenericModuleEditor] addPage(" + cdef.gGetShortName()
                            + ") failed: " + e);
                }
            }
        }

        // CRITICAL: MultiPageEditorPart.createPartControl ends with
        // setActivePage(0), which Assert.isTrue(pageIndex < pageCount). Adding
        // 0 pages here → assertion fail → editor open craters with
        // "Failed to create the part's controls". 任何 normal-path 0-page 情况
        // 必须降级到 fallback page, 让 editor 至少能开起来报错.
        if (added == 0) {
            addFallbackPage();
        }
    }

    /**
     * Empty form page used when normal page enumeration would produce 0 pages
     * (module not loaded / schema not resolved / def has 0 containers). Avoids
     * MultiPageEditorPart's 0-page assertion failure.
     */
    private void addFallbackPage() {
        try {
            StringBuilder reason = new StringBuilder();
            if (initFailure != null) {
                reason.append(initFailure).append('\n');
            }
            if (module == null) {
                reason.append("GModuleConfiguration could not be loaded from ")
                      .append(arxmlFile == null ? "<no file>" : arxmlFile.getName())
                      .append(".\nSphinx EditingDomain may not be wired (project nature missing?).");
            } else if (moduleDef == null) {
                reason.append("Module schema (<Module>Def.arxml) could not be resolved for module '")
                      .append(module.gGetShortName()).append("'.\n");
            } else {
                reason.append("Module '").append(module.gGetShortName())
                      .append("' schema has 0 containers — empty Def.arxml?");
            }
            java.util.List<String> diags = cn.com.myorg.bswbuilder.ui.schema.BswSchemaLoader.drainDiagnostics();
            if (!diags.isEmpty()) {
                reason.append("\n\nDiagnostics:");
                for (String d : diags) reason.append('\n').append(d);
            }
            addPage(new EditorOpenFailurePage(this, "BSW Module Editor", reason.toString()));
        } catch (PartInitException e) {
            e.printStackTrace();
        }
    }

    /**
     * Page-picker decision: single-instance container → General page; multi
     * → MasterDetail. Reference V25.10 only checks GENERAL_FLAG SDG option
     * (not present in our Def files); we fall back to multiplicity check via
     * {@link gautosar.gecucparameterdef.GParamConfMultiplicity}.
     */
    private static boolean useGeneralPage(GContainerDef cdef) {
        Boolean infinite = cdef.gGetUpperMultiplicityInfinite();
        if (Boolean.TRUE.equals(infinite)) return false;

        String upperStr = cdef.gGetUpperMultiplicityAsString();
        if (upperStr == null || upperStr.isEmpty()) return true;
        try {
            return Long.parseLong(upperStr.trim()) <= 1;
        } catch (NumberFormatException nfe) {
            return true;
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

    // Save/dirty 全部由 Sphinx BasicTransactionalFormEditor 接管, 不再 override:
    //   - isDirty() 由 CommandStack 监听器自动维护
    //   - doSave(monitor) 由 Sphinx 调 Resource.save via transactional
    //   - doSaveAs() 默认 not allowed (super.isSaveAsAllowed() 返 false)

    public File getArxmlFile() { return arxmlFile; }
    public GModuleConfiguration getModule() { return module; }
    public GModuleDef getModuleDef() { return moduleDef; }
}

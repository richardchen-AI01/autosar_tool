package cn.com.myorg.bswbuilder.ui.editor.utils;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.emf.common.command.Command;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.edit.command.SetCommand;
import org.eclipse.emf.edit.domain.EditingDomain;
import org.eclipse.emf.transaction.TransactionalEditingDomain;
import org.eclipse.sphinx.emf.editors.forms.BasicTransactionalFormEditor;
import org.eclipse.sphinx.emf.util.WorkspaceEditingDomainUtil;

import autosar40.ecucdescription.EcucNumericalParamValue;
import autosar40.ecucdescription.EcucTextualParamValue;
import autosar40.genericstructure.varianthandling.attributevaluevariationpoints.NumericalValueVariationPoint;
import cn.com.myorg.bswbuilder.ui.Activator;

/**
 * Write-back helpers wrapping ECUC value mutations as EMF
 * {@link SetCommand}s executed on the editor's
 * {@link TransactionalEditingDomain}. Mirrors the reference V25.10 pattern:
 *
 * <pre>
 *   TransactionalEditingDomain d = WorkspaceEditingDomainUtil.getEditingDomain(eObj);
 *   d.getCommandStack().execute(SetCommand.create(d, owner, feature, newValue));
 * </pre>
 *
 * <p>跟参考 (RenameBswContainerAction line 270-273 / DeleteBswContainerAction
 * line 96) 同款写入路径。我们这层只暴露 ECUC 价值常用面 (Numerical / Textual);
 * S5 加 add/remove/rename container helper。
 *
 * <p>Going through CommandStack is what gives us:
 * <ul>
 *   <li>Sphinx 自动 dirty tracking (CommandStack 监听器 fire PROP_DIRTY)</li>
 *   <li>Save 写盘 (Sphinx Resource.save 序列化整个 ResourceSet)</li>
 *   <li>Undo/Redo</li>
 * </ul>
 * 直接 {@code pv.setValue(...)} 不走 CommandStack — Sphinx 探测不到 → 仍然 dirty
 * 不亮 + Save 写不出。
 */
public final class EcucWriteActions {

    private EcucWriteActions() {}

    /**
     * Editor 持有的 TransactionalEditingDomain; null 表示 BTFE.init 没接管成功
     * (input 类型不匹配 / model 没 load 进 Sphinx ResourceSet)。
     */
    public static TransactionalEditingDomain getDomain(BasicTransactionalFormEditor editor) {
        if (editor == null) return null;
        EditingDomain ed = editor.getEditingDomain();
        return (ed instanceof TransactionalEditingDomain) ? (TransactionalEditingDomain) ed : null;
    }

    /**
     * Fallback 路径: 直接从 EObject 的 ResourceSet 走 Sphinx WorkspaceEditingDomainUtil
     * 反查 domain (跟参考 RenameBswContainerAction line 270 同款)。
     */
    public static TransactionalEditingDomain getDomainFromEObject(EObject obj) {
        if (obj == null) return null;
        return WorkspaceEditingDomainUtil.getEditingDomain(obj);
    }

    /**
     * 给 {@link EcucNumericalParamValue} 包装的 {@link NumericalValueVariationPoint}
     * 的 {@code mixedText} feature (从 FormulaExpression 继承) 写新值, via
     * SetCommand。返 false 时调用方应记录失败 (domain 缺 / feature 缺 / wrapper 缺)。
     */
    public static boolean setNumericalText(BasicTransactionalFormEditor editor,
                                           EcucNumericalParamValue pv,
                                           String newText) {
        if (pv == null) {
            log("setNumericalText: pv==null");
            return false;
        }
        NumericalValueVariationPoint vp = pv.getValue();
        if (vp == null) {
            // S3.5 TODO: pv.value wrapper 不存在 → 用 CompoundCommand 先 SetCommand 创 wrapper
            // 再 SetCommand 设 mixedText。当前 Demo arxml 所有参数都已实例化, vp 不会 null。
            log("setNumericalText: pv.getValue() returned null (wrapper missing)");
            return false;
        }
        TransactionalEditingDomain d = pickDomain(editor, vp);
        if (d == null) {
            log("setNumericalText: no TransactionalEditingDomain for " + describe(vp));
            return false;
        }
        EStructuralFeature feature = vp.eClass().getEStructuralFeature("mixedText");
        if (feature == null) {
            log("setNumericalText: no feature 'mixedText' on " + vp.eClass().getName());
            return false;
        }
        Command cmd = SetCommand.create(d, vp, feature, newText);
        d.getCommandStack().execute(cmd);
        return true;
    }

    /**
     * 给 {@link EcucTextualParamValue} 的 {@code value} feature 写新值, via SetCommand。
     */
    public static boolean setTextualValue(BasicTransactionalFormEditor editor,
                                          EcucTextualParamValue pv,
                                          String newValue) {
        if (pv == null) {
            log("setTextualValue: pv==null");
            return false;
        }
        TransactionalEditingDomain d = pickDomain(editor, pv);
        if (d == null) {
            log("setTextualValue: no TransactionalEditingDomain for " + describe(pv));
            return false;
        }
        EStructuralFeature feature = pv.eClass().getEStructuralFeature("value");
        if (feature == null) {
            log("setTextualValue: no feature 'value' on " + pv.eClass().getName());
            return false;
        }
        Command cmd = SetCommand.create(d, pv, feature, newValue);
        d.getCommandStack().execute(cmd);
        return true;
    }

    /**
     * S2 探针: 把 super.getEditingDomain() / super.getModelRoot() 状态打到 ILog,
     * 让 S2 验收阶段判断 super.init 是否接管成功。
     * S3 / S5 落地后可以改成 assert 形式。
     */
    public static void probeBindings(BasicTransactionalFormEditor editor, String contextLabel) {
        EditingDomain ed = editor == null ? null : editor.getEditingDomain();
        Object root = editor == null ? null : editor.getModelRoot();
        StringBuilder sb = new StringBuilder("[probe] ").append(contextLabel)
                .append(": editingDomain=")
                .append(ed == null ? "null" : ed.getClass().getSimpleName())
                .append(", isTransactional=").append(ed instanceof TransactionalEditingDomain)
                .append(", modelRoot=")
                .append(root == null ? "null" : root.getClass().getSimpleName());
        if (root instanceof EObject) {
            EObject e = (EObject) root;
            sb.append(", rootResource=")
              .append(e.eResource() == null ? "null" : e.eResource().getURI());
        }
        log(sb.toString());
    }

    private static TransactionalEditingDomain pickDomain(BasicTransactionalFormEditor editor, EObject obj) {
        TransactionalEditingDomain d = getDomain(editor);
        if (d != null) return d;
        return getDomainFromEObject(obj);
    }

    private static String describe(EObject obj) {
        if (obj == null) return "null";
        return obj.eClass().getName() + "@" + Integer.toHexString(System.identityHashCode(obj));
    }

    private static void log(String msg) {
        try {
            Activator a = Activator.getDefault();
            if (a != null) {
                a.getLog().log(new Status(IStatus.INFO, Activator.PLUGIN_ID,
                        "[EcucWriteActions] " + msg));
            }
        } catch (Throwable ignored) {
            /* fallback silent */
        }
    }
}

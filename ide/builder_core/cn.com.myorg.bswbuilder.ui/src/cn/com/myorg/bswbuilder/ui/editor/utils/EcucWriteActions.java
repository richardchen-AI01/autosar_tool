package cn.com.myorg.bswbuilder.ui.editor.utils;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.util.EcoreUtil;
import org.eclipse.emf.edit.domain.EditingDomain;
import org.eclipse.emf.transaction.RecordingCommand;
import org.eclipse.emf.transaction.TransactionalEditingDomain;
import org.eclipse.sphinx.emf.editors.forms.BasicTransactionalFormEditor;
import org.eclipse.sphinx.emf.util.WorkspaceEditingDomainUtil;

import autosar40.ecucdescription.EcucContainerValue;
import autosar40.ecucdescription.EcucModuleConfigurationValues;
import autosar40.ecucdescription.EcucNumericalParamValue;
import autosar40.ecucdescription.EcucTextualParamValue;
import autosar40.ecucdescription.EcucdescriptionFactory;
import autosar40.ecucparameterdef.EcucContainerDef;
import autosar40.genericstructure.varianthandling.attributevaluevariationpoints.NumericalValueVariationPoint;
import cn.com.myorg.bswbuilder.ui.Activator;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;
import gautosar.gecucparameterdef.GContainerDef;

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
     * 的 mixedText 写新值, via {@link RecordingCommand}。
     *
     * <p>注意 mixedText 是 FormulaExpression 的 Java 派生 setter (内部把 String 写进
     * 真正的 {@code mixed} FeatureMap), **不是 Ecore EAttribute** — 直接
     * {@code getEStructuralFeature("mixedText")} 返 null。所以这里不用 SetCommand,
     * 改用 RecordingCommand 包裹 typed setter, 它录制 doExecute() 内的所有 EMF
     * 通知 + 自动支持 undo + 进 CommandStack 触发 dirty。
     */
    public static boolean setNumericalText(BasicTransactionalFormEditor editor,
                                           EcucNumericalParamValue pv,
                                           final String newText) {
        if (pv == null) {
            log("setNumericalText: pv==null");
            return false;
        }
        final NumericalValueVariationPoint vp = pv.getValue();
        if (vp == null) {
            // S3.5 TODO: pv.value wrapper 不存在 → CompoundCommand 创 wrapper 再设 mixedText。
            log("setNumericalText: pv.getValue() returned null (wrapper missing)");
            return false;
        }
        TransactionalEditingDomain d = pickDomain(editor, vp);
        if (d == null) {
            log("setNumericalText: no TransactionalEditingDomain for " + describe(vp));
            return false;
        }
        d.getCommandStack().execute(new RecordingCommand(d, "Set numerical value") {
            @Override protected void doExecute() {
                vp.setMixedText(newText);
            }
        });
        return true;
    }

    /**
     * 给 {@link EcucTextualParamValue} 的 value 写新值, via {@link RecordingCommand}。
     * 用 RecordingCommand 跟 numerical 路径保持一致 (SetCommand 也行, 但 textual
     * params 的 value feature 同样是 typed accessor 派生, 直接 typed setter + record 最稳)。
     */
    public static boolean setTextualValue(BasicTransactionalFormEditor editor,
                                          final EcucTextualParamValue pv,
                                          final String newValue) {
        if (pv == null) {
            log("setTextualValue: pv==null");
            return false;
        }
        TransactionalEditingDomain d = pickDomain(editor, pv);
        if (d == null) {
            log("setTextualValue: no TransactionalEditingDomain for " + describe(pv));
            return false;
        }
        d.getCommandStack().execute(new RecordingCommand(d, "Set textual value") {
            @Override protected void doExecute() {
                pv.setValue(newValue);
            }
        });
        return true;
    }

    /**
     * S5: 在 module 下创建一个新 EcucContainerValue, 设 shortName + definition,
     * 加进 module.gGetContainers()。用 RecordingCommand 包裹整段, dirty 自动亮。
     *
     * <p>跟参考 V25.10 CreateContainerActionProvider + MetaModelDescriptorParser
     * 的"创新容器"路径同款 EMF 写入: 创实例 → 设引用 → append 到 parent's containers。
     * 我们 v0.2 不复刻 reference 的 UIDefinition 默认值填充层 — 创空容器, 用户用
     * detail form 自己填; 后续 S5.5 polish 可以加 schema-driven default value 自动
     * 填充。
     *
     * @return 新建容器 (写入完成后, 可用于 viewer 重选)，或 null 表示失败。
     */
    public static GContainer addContainer(BasicTransactionalFormEditor editor,
                                          final GModuleConfiguration parent,
                                          final GContainerDef def,
                                          final String shortName) {
        if (parent == null || def == null) {
            log("addContainer: parent/def null");
            return null;
        }
        TransactionalEditingDomain d = pickDomain(editor, (EObject) parent);
        if (d == null) {
            log("addContainer: no TransactionalEditingDomain");
            return null;
        }
        if (!(parent instanceof EcucModuleConfigurationValues)) {
            log("addContainer: parent is not EcucModuleConfigurationValues, got "
                    + ((EObject) parent).eClass().getName());
            return null;
        }
        if (!(def instanceof EcucContainerDef)) {
            log("addContainer: def is not EcucContainerDef, got "
                    + ((EObject) def).eClass().getName());
            return null;
        }
        final EcucModuleConfigurationValues moduleVal = (EcucModuleConfigurationValues) parent;
        final EcucContainerDef containerDef = (EcucContainerDef) def;
        final EcucContainerValue[] holder = new EcucContainerValue[1];
        d.getCommandStack().execute(new RecordingCommand(d, "Add " + def.gGetShortName()) {
            @Override protected void doExecute() {
                EcucContainerValue cv = EcucdescriptionFactory.eINSTANCE.createEcucContainerValue();
                cv.setShortName(shortName);
                cv.setDefinition(containerDef);
                moduleVal.getContainers().add(cv);
                holder[0] = cv;
            }
        });
        return holder[0];
    }

    /**
     * S5: 删一个容器 — 从其 eContainer 的 containers/subContainers 列表 remove。
     * 跟参考 V25.10 DeleteBswContainerAction:96 同款 (eContainer 类型分支:
     * EcucModuleConfigurationValues.getContainers() vs GContainer.gGetSubContainers())。
     * 我们 v0.2 跳过 reference 的 ModelUtils.getEObjectByCompleteURI 联动清引用 —
     * 留 v0.3 polish (用户删一个 block 后可能其他 block 还在 ref 它, 暂时 EMF 让它指向
     * 死引用 — 后续 ResourceImpl save 序列化时 EMF 自动清 dangling ref)。
     */
    public static boolean removeContainer(BasicTransactionalFormEditor editor,
                                           final GContainer container) {
        if (container == null) {
            log("removeContainer: container null");
            return false;
        }
        TransactionalEditingDomain d = pickDomain(editor, (EObject) container);
        if (d == null) {
            log("removeContainer: no TransactionalEditingDomain");
            return false;
        }
        final EObject parent = ((EObject) container).eContainer();
        if (parent == null) {
            log("removeContainer: container has no eContainer (already detached?)");
            return false;
        }
        d.getCommandStack().execute(new RecordingCommand(d, "Delete " + container.gGetShortName()) {
            @Override protected void doExecute() {
                if (parent instanceof EcucModuleConfigurationValues) {
                    ((EcucModuleConfigurationValues) parent).getContainers().remove(container);
                } else if (parent instanceof GContainer) {
                    ((GContainer) parent).gGetSubContainers().remove(container);
                } else {
                    EcoreUtil.remove((EObject) container);
                }
            }
        });
        return true;
    }

    /**
     * S5: 重命名 container. 走 typed gSetShortName (跟参考 V25.10
     * RenameBswContainerAction:271-273 同款 SetCommand 写 nameFeature, 我们用
     * RecordingCommand 包 typed setter 跟 numerical/textual 路径统一)。
     */
    public static boolean renameContainer(BasicTransactionalFormEditor editor,
                                           final GContainer container,
                                           final String newShortName) {
        if (container == null || newShortName == null || newShortName.isEmpty()) {
            log("renameContainer: container/newName null/empty");
            return false;
        }
        TransactionalEditingDomain d = pickDomain(editor, (EObject) container);
        if (d == null) {
            log("renameContainer: no TransactionalEditingDomain");
            return false;
        }
        d.getCommandStack().execute(new RecordingCommand(d, "Rename") {
            @Override protected void doExecute() {
                container.gSetShortName(newShortName);
            }
        });
        return true;
    }

    /**
     * S5: 复制一个容器到同 parent — EcoreUtil.copy 深拷贝, append "_copy" 到 shortName,
     * append 到 parent containers 列表。Sphinx CommandStack 自动 dirty。
     */
    public static GContainer duplicateContainer(BasicTransactionalFormEditor editor,
                                                 final GContainer src) {
        if (src == null) {
            log("duplicateContainer: src null");
            return null;
        }
        TransactionalEditingDomain d = pickDomain(editor, (EObject) src);
        if (d == null) {
            log("duplicateContainer: no TransactionalEditingDomain");
            return null;
        }
        final EObject parent = ((EObject) src).eContainer();
        if (parent == null) {
            log("duplicateContainer: src has no eContainer");
            return null;
        }
        final GContainer[] holder = new GContainer[1];
        d.getCommandStack().execute(new RecordingCommand(d, "Duplicate " + src.gGetShortName()) {
            @SuppressWarnings("unchecked")
            @Override protected void doExecute() {
                EObject copy = EcoreUtil.copy((EObject) src);
                if (!(copy instanceof GContainer)) return;
                GContainer cc = (GContainer) copy;
                cc.gSetShortName(uniqueSiblingName(parent, src.gGetShortName() + "_copy"));
                if (parent instanceof EcucModuleConfigurationValues) {
                    ((EcucModuleConfigurationValues) parent).getContainers().add((EcucContainerValue) cc);
                } else if (parent instanceof GContainer) {
                    ((GContainer) parent).gGetSubContainers().add(cc);
                }
                holder[0] = cc;
            }
        });
        return holder[0];
    }

    /** 找一个不冲突的 shortName: name, name_1, name_2, ... 直到 sibling 中没出现。 */
    private static String uniqueSiblingName(EObject parent, String base) {
        java.util.Set<String> existing = new java.util.HashSet<>();
        if (parent instanceof EcucModuleConfigurationValues) {
            for (Object c : ((EcucModuleConfigurationValues) parent).getContainers()) {
                if (c instanceof GContainer) existing.add(((GContainer) c).gGetShortName());
            }
        } else if (parent instanceof GContainer) {
            for (Object c : ((GContainer) parent).gGetSubContainers()) {
                if (c instanceof GContainer) existing.add(((GContainer) c).gGetShortName());
            }
        }
        if (!existing.contains(base)) return base;
        int i = 1;
        while (existing.contains(base + "_" + i)) i++;
        return base + "_" + i;
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

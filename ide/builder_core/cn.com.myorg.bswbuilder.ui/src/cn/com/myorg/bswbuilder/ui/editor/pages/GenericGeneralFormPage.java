package cn.com.myorg.bswbuilder.ui.editor.pages;

import java.util.LinkedHashMap;
import java.util.Map;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.jface.layout.GridDataFactory;
import org.eclipse.jface.layout.GridLayoutFactory;
import org.eclipse.sphinx.emf.editors.forms.BasicTransactionalFormEditor;
import org.eclipse.swt.SWT;
import org.eclipse.swt.events.ModifyEvent;
import org.eclipse.swt.events.ModifyListener;
import org.eclipse.swt.events.SelectionAdapter;
import org.eclipse.swt.events.SelectionEvent;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Combo;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Spinner;
import org.eclipse.swt.widgets.Text;
import org.eclipse.ui.forms.IManagedForm;
import org.eclipse.ui.forms.editor.FormEditor;
import org.eclipse.ui.forms.editor.FormPage;
import org.eclipse.ui.forms.widgets.FormToolkit;
import org.eclipse.ui.forms.widgets.ScrolledForm;
import org.eclipse.ui.forms.widgets.Section;

import autosar40.ecucdescription.EcucNumericalParamValue;
import autosar40.ecucdescription.EcucTextualParamValue;
import cn.com.myorg.bswbuilder.ui.Activator;
import cn.com.myorg.bswbuilder.ui.editor.utils.EcuUtils;
import cn.com.myorg.bswbuilder.ui.editor.utils.EcucWriteActions;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;
import gautosar.gecucdescription.GParameterValue;
import gautosar.gecucparameterdef.GBooleanParamDef;
import gautosar.gecucparameterdef.GConfigParameter;
import gautosar.gecucparameterdef.GContainerDef;
import gautosar.gecucparameterdef.GEnumerationLiteralDef;
import gautosar.gecucparameterdef.GEnumerationParamDef;
import gautosar.gecucparameterdef.GFloatParamDef;
import gautosar.gecucparameterdef.GIntegerParamDef;
import gautosar.gecucparameterdef.GParamConfContainerDef;
import gautosar.gecucparameterdef.GStringParamDef;

/**
 * Generic single-instance ('General') form page — auto-renders widgets from
 * an ECUC {@link GContainerDef} schema and binds them to the matching
 * {@link GContainer} instance.
 *
 * <p>Reference V25.10 path:
 * {@code cn.com.isoft.bswbuilder.ui.editor.pages.BswModuleGeneralFormPage}.
 *
 * <p>Widget mapping (跟参考 V25.10 一致):
 * <ul>
 *   <li>{@link GBooleanParamDef} → {@link Button} {@code SWT.CHECK} (numerical)</li>
 *   <li>{@link GIntegerParamDef} → {@link Spinner} (numerical)</li>
 *   <li>{@link GFloatParamDef}   → {@link Text} (numerical)</li>
 *   <li>{@link GStringParamDef}  → {@link Text} (textual)</li>
 *   <li>{@link GEnumerationParamDef} → {@link Combo} (textual)</li>
 * </ul>
 *
 * <p>E5-6 S3 起 widget 改值经 {@link EcucWriteActions} 包装成 EMF
 * {@code SetCommand} 写入 Sphinx {@code TransactionalEditingDomain.getCommandStack()}。
 * Sphinx CommandStack 监听器自动 fire {@code PROP_DIRTY} → 标题小星亮 + Save 按钮亮 +
 * 撑 undo/redo + Save 时自动 {@code Resource.save}。
 *
 * <p>之前 (E5-2 ~ E5-5) 直接 {@code recheckDirty()} no-op + 留了 collectChangedParams
 * 给手撸 writer — E5-6 S3 删掉, 全归 Sphinx 框架管。
 */
public class GenericGeneralFormPage extends FormPage {

    private final GModuleConfiguration module;
    private final GContainerDef containerDef;

    /** Resolved instance container ([1..1] container's single instance), or null. */
    private GContainer instanceContainer;

    /** Schema-defined param → backing widget. Iteration order matters (UI flow). */
    private final Map<GConfigParameter, Control> widgets = new LinkedHashMap<>();

    public GenericGeneralFormPage(FormEditor editor,
                                  GModuleConfiguration module,
                                  GContainerDef containerDef) {
        super(editor, containerDef.gGetShortName() + "Page", containerDef.gGetShortName());
        this.module = module;
        this.containerDef = containerDef;
    }

    @Override
    protected void createFormContent(IManagedForm managedForm) {
        FormToolkit toolkit = managedForm.getToolkit();
        ScrolledForm form = managedForm.getForm();
        String moduleName = module.gGetShortName();
        String containerName = containerDef.gGetShortName();
        form.setText(moduleName + " — " + containerName);

        Composite body = form.getBody();
        GridLayoutFactory.fillDefaults().margins(5, 5).applyTo(body);

        // Locate the instance container ([1..1] expected for general containers).
        instanceContainer = EcuUtils.getSingleContainerByDef(module, containerDef);

        Section section = toolkit.createSection(body,
                Section.TITLE_BAR | Section.DESCRIPTION | Section.EXPANDED);
        section.setText(containerName);
        String desc = "Edit parameters of " + containerName + " (" + moduleName + " module).";
        section.setDescription(desc);
        GridDataFactory.fillDefaults().grab(true, true).applyTo(section);

        Composite client = toolkit.createComposite(section);
        GridLayout grid = new GridLayout(3, false);
        grid.marginTop = 6;
        grid.horizontalSpacing = 10;
        grid.verticalSpacing = 6;
        client.setLayout(grid);
        section.setClient(client);

        if (instanceContainer == null) {
            Label note = toolkit.createLabel(client,
                    "(no '" + containerName + "' container instance in this module — defaults shown read-only)",
                    SWT.WRAP);
            GridDataFactory.fillDefaults().span(3, 1).applyTo(note);
        }

        if (containerDef instanceof GParamConfContainerDef) {
            GParamConfContainerDef pdef = (GParamConfContainerDef) containerDef;
            for (GConfigParameter param : pdef.gGetParameters()) {
                addRow(client, toolkit, param);
            }
        }
    }

    private void addRow(Composite parent, FormToolkit toolkit, final GConfigParameter param) {
        Label label = toolkit.createLabel(parent, param.gGetShortName() + ":", SWT.NONE);
        GridDataFactory.fillDefaults().align(SWT.END, SWT.CENTER).applyTo(label);

        Control widget;

        if (param instanceof GBooleanParamDef) {
            String currentVal = readParamValue(param);
            final Button check = toolkit.createButton(parent, "", SWT.CHECK);
            check.setSelection("true".equalsIgnoreCase(currentVal));
            check.addSelectionListener(new SelectionAdapter() {
                @Override public void widgetSelected(SelectionEvent e) {
                    writeNumericalParam(param, check.getSelection() ? "true" : "false");
                }
            });
            widget = check;
        } else if (param instanceof GIntegerParamDef) {
            String currentVal = readParamValue(param);
            final Spinner spin = new Spinner(parent, SWT.BORDER);
            spin.setMinimum(Integer.MIN_VALUE);
            spin.setMaximum(Integer.MAX_VALUE);
            try { if (currentVal != null) spin.setSelection(Integer.parseInt(currentVal.trim())); }
            catch (NumberFormatException nfe) { /* leave default 0 */ }
            spin.addModifyListener(new ModifyListener() {
                @Override public void modifyText(ModifyEvent e) {
                    writeNumericalParam(param, String.valueOf(spin.getSelection()));
                }
            });
            GridDataFactory.fillDefaults().hint(120, SWT.DEFAULT).applyTo(spin);
            widget = spin;
        } else if (param instanceof GEnumerationParamDef) {
            String currentVal = readParamValue(param);
            final Combo combo = new Combo(parent, SWT.READ_ONLY | SWT.BORDER);
            for (GEnumerationLiteralDef lit : ((GEnumerationParamDef) param).gGetLiterals()) {
                combo.add(lit.gGetShortName());
            }
            int idx = currentVal == null ? -1 : combo.indexOf(currentVal);
            if (idx >= 0) combo.select(idx);
            combo.addSelectionListener(new SelectionAdapter() {
                @Override public void widgetSelected(SelectionEvent e) {
                    writeTextualParam(param, combo.getText());
                }
            });
            GridDataFactory.fillDefaults().hint(180, SWT.DEFAULT).applyTo(combo);
            widget = combo;
        } else if (param instanceof GFloatParamDef) {
            String currentVal = readParamValue(param);
            final Text text = toolkit.createText(parent, currentVal == null ? "" : currentVal, SWT.BORDER);
            GridDataFactory.fillDefaults().hint(180, SWT.DEFAULT).applyTo(text);
            text.addModifyListener(new ModifyListener() {
                @Override public void modifyText(ModifyEvent e) {
                    writeNumericalParam(param, text.getText());
                }
            });
            widget = text;
        } else if (param instanceof GStringParamDef) {
            String currentVal = readParamValue(param);
            final Text text = toolkit.createText(parent, currentVal == null ? "" : currentVal, SWT.BORDER);
            GridDataFactory.fillDefaults().hint(180, SWT.DEFAULT).applyTo(text);
            text.addModifyListener(new ModifyListener() {
                @Override public void modifyText(ModifyEvent e) {
                    writeTextualParam(param, text.getText());
                }
            });
            widget = text;
        } else {
            Label note = toolkit.createLabel(parent, "(unsupported type)", SWT.NONE);
            widget = note;
        }

        // Disable widget if no instance container — display informational only.
        if (instanceContainer == null) {
            widget.setEnabled(false);
        }

        // 3rd column reserved for future per-row [D] reset / browse buttons.
        toolkit.createLabel(parent, "", SWT.NONE);

        widgets.put(param, widget);
    }

    /**
     * Read a parameter's current value from the instance container, if any.
     * Returns null when not configured (caller falls back to schema default
     * via separate code path or just shows widget's intrinsic default).
     */
    private String readParamValue(GConfigParameter paramDef) {
        if (instanceContainer == null) return null;
        GParameterValue pv = EcuUtils.getParameterValue(instanceContainer, paramDef);
        if (pv == null) return null;
        if (pv instanceof EcucNumericalParamValue) {
            EcucNumericalParamValue n = (EcucNumericalParamValue) pv;
            return n.getValue() == null ? null : n.getValue().getMixedText();
        }
        if (pv instanceof EcucTextualParamValue) {
            return ((EcucTextualParamValue) pv).getValue();
        }
        return null;
    }

    /**
     * 把 numerical (boolean / integer / float) 参数的新值经 SetCommand 写到
     * NumericalValueVariationPoint.mixedText。Sphinx CommandStack 自动 fire dirty。
     */
    private void writeNumericalParam(GConfigParameter param, String newText) {
        if (instanceContainer == null) return;
        GParameterValue pv = EcuUtils.getParameterValue(instanceContainer, param);
        if (pv instanceof EcucNumericalParamValue) {
            EcucWriteActions.setNumericalText(editor(), (EcucNumericalParamValue) pv, newText);
        } else if (pv == null) {
            // S3.5: 当前 Demo arxml 所有参数都已实例化, 这条不该触发。撞了说明
            // schema 派的参数没初始化 — 走 CompoundCommand 创 pv + 设 wrapper + 设 mixedText。
            log("writeNumericalParam: pv missing for " + param.gGetShortName()
                    + " — skip (S3.5 will create pv via CompoundCommand)");
        } else {
            log("writeNumericalParam: pv has unexpected type " + pv.eClass().getName()
                    + " for " + param.gGetShortName());
        }
    }

    /**
     * 把 textual (string / enum) 参数的新值经 SetCommand 写到 EcucTextualParamValue.value。
     */
    private void writeTextualParam(GConfigParameter param, String newValue) {
        if (instanceContainer == null) return;
        GParameterValue pv = EcuUtils.getParameterValue(instanceContainer, param);
        if (pv instanceof EcucTextualParamValue) {
            EcucWriteActions.setTextualValue(editor(), (EcucTextualParamValue) pv, newValue);
        } else if (pv == null) {
            log("writeTextualParam: pv missing for " + param.gGetShortName()
                    + " — skip (S3.5 will create pv via CompoundCommand)");
        } else {
            log("writeTextualParam: pv has unexpected type " + pv.eClass().getName()
                    + " for " + param.gGetShortName());
        }
    }

    private BasicTransactionalFormEditor editor() {
        FormEditor e = getEditor();
        return (e instanceof BasicTransactionalFormEditor) ? (BasicTransactionalFormEditor) e : null;
    }

    private static void log(String msg) {
        try {
            Activator a = Activator.getDefault();
            if (a != null) {
                a.getLog().log(new Status(IStatus.INFO, Activator.PLUGIN_ID,
                        "[GenericGeneralFormPage] " + msg));
            }
        } catch (Throwable ignored) { /* fallback silent */ }
    }

    public GContainerDef getContainerDef() { return containerDef; }
    public GContainer getInstanceContainer() { return instanceContainer; }
}

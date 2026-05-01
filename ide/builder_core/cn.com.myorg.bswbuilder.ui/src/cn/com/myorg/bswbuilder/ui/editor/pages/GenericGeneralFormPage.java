package cn.com.myorg.bswbuilder.ui.editor.pages;

import java.util.LinkedHashMap;
import java.util.Map;

import org.eclipse.jface.layout.GridDataFactory;
import org.eclipse.jface.layout.GridLayoutFactory;
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

import cn.com.myorg.bswbuilder.ui.editor.utils.EcuUtils;
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
 * Same role: one form page per single-instance container in the module
 * (e.g. MemIfGeneral / NvMCommon). All modules share this one class — no
 * per-module hand-coded FormPage.
 *
 * <p>Widget mapping (跟参考 V25.10 一致):
 * <ul>
 *   <li>{@link GBooleanParamDef} → {@link Button} {@code SWT.CHECK}</li>
 *   <li>{@link GIntegerParamDef} → {@link Spinner} (with min/max from def)</li>
 *   <li>{@link GFloatParamDef}   → {@link Text}</li>
 *   <li>{@link GStringParamDef}  → {@link Text}</li>
 *   <li>{@link GEnumerationParamDef} → {@link Combo} (literals from
 *       {@code gGetLiterals()})</li>
 * </ul>
 *
 * <p>Read happens once on page-create. Save commits dirty values back via
 * the parent FormEditor's {@code doSave} (E5-4 wires this in). v0.2 first
 * cut: read-only display + dirty tracking + commit hook (write path
 * implemented in E5-4 + writer generalization in parallel).
 */
public class GenericGeneralFormPage extends FormPage {

    private final GModuleConfiguration module;
    private final GContainerDef containerDef;

    /** Resolved instance container ([1..1] container's single instance), or null. */
    private GContainer instanceContainer;

    /** Schema-defined param → backing widget. Iteration order matters (UI flow). */
    private final Map<GConfigParameter, Control> widgets = new LinkedHashMap<>();

    /** Schema-defined param → string snapshot of widget value at page-create.
     *  Used for dirty detection (跟参考 originalValues 同思路). */
    private final Map<GConfigParameter, String> originalValues = new LinkedHashMap<>();

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

        // Walk schema. CHOICE container has a different shape (sub-container choice);
        // E5-2 first cut handles GParamConfContainerDef only — the typical 'general'
        // page case. Choice containers route through master-detail (E5-3 will pick up
        // those at the parent's master level).
        if (containerDef instanceof GParamConfContainerDef) {
            GParamConfContainerDef pdef = (GParamConfContainerDef) containerDef;
            for (GConfigParameter param : pdef.gGetParameters()) {
                addRow(client, toolkit, param);
            }
            // GConfigReference 行先不在 v0.2 General page 渲染 (一般 reference
            // 出现在 master-detail 的 sub-container 而非顶层 single-instance
            // container)。如果出现, 留 E5-3 chooser dialog 时统一处理。
        }
    }

    private void addRow(Composite parent, FormToolkit toolkit, GConfigParameter param) {
        Label label = toolkit.createLabel(parent, param.gGetShortName() + ":", SWT.NONE);
        GridDataFactory.fillDefaults().align(SWT.END, SWT.CENTER).applyTo(label);

        Control widget;
        String originalText;

        if (param instanceof GBooleanParamDef) {
            String currentVal = readParamValue(param);
            Button check = toolkit.createButton(parent, "", SWT.CHECK);
            check.setSelection("true".equalsIgnoreCase(currentVal));
            check.addSelectionListener(new SelectionAdapter() {
                @Override public void widgetSelected(SelectionEvent e) { recheckDirty(); }
            });
            widget = check;
            originalText = check.getSelection() ? "true" : "false";
        } else if (param instanceof GIntegerParamDef) {
            String currentVal = readParamValue(param);
            Spinner spin = new Spinner(parent, SWT.BORDER);
            // ARTOP G* param defs don't expose min/max — that's typed on
            // autosar40.ecucparameterdef.EcucIntegerParamDef. v0.2 cut: use
            // wide bounds; E5-3 polish will read typed bounds.
            spin.setMinimum(Integer.MIN_VALUE);
            spin.setMaximum(Integer.MAX_VALUE);
            try { if (currentVal != null) spin.setSelection(Integer.parseInt(currentVal.trim())); }
            catch (NumberFormatException nfe) { /* leave default 0 */ }
            spin.addModifyListener(new ModifyListener() {
                @Override public void modifyText(ModifyEvent e) { recheckDirty(); }
            });
            GridDataFactory.fillDefaults().hint(120, SWT.DEFAULT).applyTo(spin);
            widget = spin;
            originalText = String.valueOf(spin.getSelection());
        } else if (param instanceof GEnumerationParamDef) {
            String currentVal = readParamValue(param);
            Combo combo = new Combo(parent, SWT.READ_ONLY | SWT.BORDER);
            for (GEnumerationLiteralDef lit : ((GEnumerationParamDef) param).gGetLiterals()) {
                combo.add(lit.gGetShortName());
            }
            int idx = currentVal == null ? -1 : combo.indexOf(currentVal);
            if (idx >= 0) combo.select(idx);
            combo.addSelectionListener(new SelectionAdapter() {
                @Override public void widgetSelected(SelectionEvent e) { recheckDirty(); }
            });
            GridDataFactory.fillDefaults().hint(180, SWT.DEFAULT).applyTo(combo);
            widget = combo;
            originalText = combo.getText();
        } else if (param instanceof GFloatParamDef || param instanceof GStringParamDef) {
            String currentVal = readParamValue(param);
            Text text = toolkit.createText(parent, currentVal == null ? "" : currentVal, SWT.BORDER);
            GridDataFactory.fillDefaults().hint(180, SWT.DEFAULT).applyTo(text);
            text.addModifyListener(new ModifyListener() {
                @Override public void modifyText(ModifyEvent e) { recheckDirty(); }
            });
            widget = text;
            originalText = text.getText();
        } else {
            Label note = toolkit.createLabel(parent, "(unsupported type)", SWT.NONE);
            widget = note;
            originalText = "";
        }

        // Disable widget if no instance container — display is informational only.
        if (instanceContainer == null) {
            widget.setEnabled(false);
        }

        // 3rd column reserved for future per-row [D] reset / browse buttons.
        toolkit.createLabel(parent, "", SWT.NONE);

        widgets.put(param, widget);
        originalValues.put(param, originalText);
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
        // Numerical (boolean / integer / float) → mixed-text via VariationPoint;
        // textual (string / enum) → typed getValue().
        if (pv instanceof autosar40.ecucdescription.EcucNumericalParamValue) {
            autosar40.ecucdescription.EcucNumericalParamValue n =
                    (autosar40.ecucdescription.EcucNumericalParamValue) pv;
            return n.getValue() == null ? null : n.getValue().getMixedText();
        }
        if (pv instanceof autosar40.ecucdescription.EcucTextualParamValue) {
            return ((autosar40.ecucdescription.EcucTextualParamValue) pv).getValue();
        }
        return null;
    }

    /**
     * Compare each widget's current value against snapshot at page-create;
     * mark editor dirty if any differ. Editor's {@code firePropertyChange}
     * picks up via {@code isDirty()} override (E5-4 wires the link).
     */
    private void recheckDirty() {
        // For now just compute, don't fire — wiring to FormEditor happens at E5-4.
        // (Hook reserved so logic is ready.)
        for (Map.Entry<GConfigParameter, Control> e : widgets.entrySet()) {
            String now = widgetValue(e.getValue());
            String orig = originalValues.getOrDefault(e.getKey(), "");
            if (!now.equals(orig)) {
                // Dirty. E5-4: editor.setDirty(true);
                return;
            }
        }
        // Clean. E5-4: editor.setDirty(false);
    }

    /** Read a widget's current value as a string suitable for dirty compare / save. */
    private static String widgetValue(Control w) {
        if (w instanceof Button) return ((Button) w).getSelection() ? "true" : "false";
        if (w instanceof Spinner) return String.valueOf(((Spinner) w).getSelection());
        if (w instanceof Combo) return ((Combo) w).getText();
        if (w instanceof Text) return ((Text) w).getText();
        return "";
    }

    /**
     * Iterate widgets and surface every (paramShortName, newValue) tuple that
     * differs from snapshot — caller persists via {@link
     * cn.com.myorg.bswbuilder.modules.memif.data.MemIfArxmlWriter#writeParam}
     * (or the generalized writer in E5-4).
     *
     * @return number of changed entries; 0 if clean.
     */
    public int collectChangedParams(Map<String, String> outDeltaByParamShortName) {
        int n = 0;
        for (Map.Entry<GConfigParameter, Control> e : widgets.entrySet()) {
            String now = widgetValue(e.getValue());
            String orig = originalValues.getOrDefault(e.getKey(), "");
            if (!now.equals(orig)) {
                outDeltaByParamShortName.put(e.getKey().gGetShortName(), now);
                n++;
            }
        }
        return n;
    }

    public GContainerDef getContainerDef() { return containerDef; }
    public GContainer getInstanceContainer() { return instanceContainer; }
}

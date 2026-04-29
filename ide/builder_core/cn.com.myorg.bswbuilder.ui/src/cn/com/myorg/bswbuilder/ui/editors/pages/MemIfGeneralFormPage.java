package cn.com.myorg.bswbuilder.ui.editors.pages;

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
import org.eclipse.swt.widgets.Combo;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Text;
import org.eclipse.ui.forms.IManagedForm;
import org.eclipse.ui.forms.editor.FormEditor;
import org.eclipse.ui.forms.editor.FormPage;
import org.eclipse.ui.forms.widgets.FormToolkit;
import org.eclipse.ui.forms.widgets.ScrolledForm;
import org.eclipse.ui.forms.widgets.Section;

import cn.com.myorg.bswbuilder.modules.memif.data.MemIfArxmlWriter;
import cn.com.myorg.bswbuilder.modules.memif.data.MemIfData;
import cn.com.myorg.bswbuilder.modules.memif.data.MemIfDerivedCalculator;
import cn.com.myorg.bswbuilder.ui.editors.MemIfModuleManagerEditor;

/**
 * General configuration page for the MemIf module — analogue of the
 * reference V25.10 {@code BswModuleGeneralFormPage}, which renders a single
 * "General" section under the page title:
 *
 * <pre>
 *   Page title :   MemIf - MemIfGeneral Module Manager
 *   Section    :   "MemIfGeneral General"
 *                  "This container contains the global parameters of the MemIfGeneral."
 *   Layout     :   GridLayout(1, false), marginTop = 10
 *   Per-row    :   label (~230) | value-widget (~150),  vSpacing = 10
 *   Fields     :   MemIfDevErrorDetect (Combo)
 *                  MemIfNumberOfDevices (Text + derived hint)
 *                  MemIfVersionInfoApi (Combo)
 *                  MemIfModuleVersion (Text)
 * </pre>
 *
 * Reference uses Sphinx auto-rendering driven by EcucContainerDef +
 * EcucModuleConfigurationValues (see
 * {@code BswModuleGeneralFormPage.createGeneralOptionsSection}). v0.1
 * doesn't have a working EMF EditingDomain pipeline — we hand-build
 * the same widgets and write back via {@code MemIfArxmlWriter} string
 * surgery (Phase F). Visual result matches; the persistence path differs.
 */
public class MemIfGeneralFormPage extends FormPage {

    public static final String ID = "cn.com.myorg.bswbuilder.ui.editors.pages.MemIfGeneral";

    /** Reference label-width / value-width / vertical-spacing — matches
     *  iSoft GridLayoutAdapter(230, 150, 10) in
     *  BswModuleGeneralFormPage.createGeneralOptionsSection. */
    private static final int LABEL_WIDTH = 230;
    private static final int VALUE_WIDTH = 150;
    private static final int V_SPACING = 10;

    private static final String CONTAINER_NAME = "MemIfGeneral";
    private static final String MODULE_NAME = "MemIf";

    private enum Param {
        DEV_ERROR_DETECT("MemIfDevErrorDetect", "Memif Dev Error Detect:", Type.BOOLEAN),
        NUMBER_OF_DEVICES("MemIfNumberOfDevices", "Memif Number Of Devices:", Type.INTEGER),
        VERSION_INFO_API("MemIfVersionInfoApi", "Memif Version Info Api:", Type.BOOLEAN),
        MODULE_VERSION("MemIfModuleVersion", "Memif Module Version:", Type.STRING);

        final String shortName;
        final String label;
        final Type type;
        Param(String shortName, String label, Type type) {
            this.shortName = shortName; this.label = label; this.type = type;
        }
    }
    private enum Type { BOOLEAN, INTEGER, STRING }

    private MemIfData data;
    private FormToolkit toolkit;
    private final Map<Param, Control> editors = new LinkedHashMap<>();
    private final Map<Param, String> originalValues = new LinkedHashMap<>();
    private Label derivedHint;

    public MemIfGeneralFormPage(FormEditor editor, MemIfData data) {
        super(editor, ID, MODULE_NAME);
        this.data = data;
    }

    @Override
    protected void createFormContent(IManagedForm managedForm) {
        toolkit = managedForm.getToolkit();
        ScrolledForm form = managedForm.getForm();
        // Page title — reference: "<module> - <container> Module Manager"
        form.setText(MODULE_NAME + " - " + CONTAINER_NAME + " Module Manager");

        Composite body = form.getBody();
        body.setLayout(new GridLayout(1, false));

        Section section = toolkit.createSection(body,
                Section.TITLE_BAR | Section.DESCRIPTION | Section.EXPANDED);
        // Reference: "<container> General" + "This container contains the global parameters of the <container>."
        section.setText(CONTAINER_NAME + " General");
        section.setDescription("This container contains the global parameters of the "
                + CONTAINER_NAME + ".");
        GridDataFactory.fillDefaults().grab(true, false).applyTo(section);

        Composite client = toolkit.createComposite(section);
        GridLayout cl = new GridLayout(2, false);
        cl.marginTop = V_SPACING;
        cl.verticalSpacing = V_SPACING;
        cl.horizontalSpacing = 16;
        cl.marginWidth = 14;
        client.setLayout(cl);
        section.setClient(client);

        addRow(client, Param.DEV_ERROR_DETECT,  data.getMemIfDevErrorDetect());
        addRow(client, Param.NUMBER_OF_DEVICES, data.getMemIfNumberOfDevices());
        addRow(client, Param.VERSION_INFO_API,  data.getMemIfVersionInfoApi());
        addRow(client, Param.MODULE_VERSION,    data.getMemIfModuleVersion());

        Label src = toolkit.createLabel(body,
                "source: " + data.getSourcePath(), SWT.NONE);
        GridDataFactory.fillDefaults().grab(true, false).indent(0, 14).applyTo(src);

        updateDerivedHint();
    }

    /**
     * One reference row: 230-wide label on the left, 150-wide editor in
     * the middle. We render the derived hint inline next to the value
     * widget for NumberOfDevices instead of as a separate column — the
     * reference puts auto-fill notes in the validate output rather than
     * the form, but inline keeps it visible at edit time.
     */
    private void addRow(Composite parent, final Param p, String value) {
        Label l = toolkit.createLabel(parent, p.label, SWT.NONE);
        GridDataFactory.fillDefaults()
                .align(SWT.END, SWT.CENTER)
                .hint(LABEL_WIDTH, SWT.DEFAULT)
                .applyTo(l);

        Composite valueCell = toolkit.createComposite(parent);
        GridLayoutFactory.fillDefaults().numColumns(2).spacing(8, 0).applyTo(valueCell);
        GridDataFactory.fillDefaults().grab(true, false).applyTo(valueCell);

        String display = (value == null) ? "" : value;
        originalValues.put(p, display);

        Control widget;
        switch (p.type) {
            case BOOLEAN: {
                Combo combo = new Combo(valueCell, SWT.READ_ONLY);
                combo.setItems(new String[] { "false", "true" });
                combo.setText(display.isEmpty() ? "false" : display);
                toolkit.adapt(combo);
                GridDataFactory.fillDefaults().hint(VALUE_WIDTH, SWT.DEFAULT).applyTo(combo);
                combo.addSelectionListener(new SelectionAdapter() {
                    @Override public void widgetSelected(SelectionEvent e) { recheckDirty(); }
                });
                widget = combo;
                break;
            }
            default: {
                Text text = toolkit.createText(valueCell, display, SWT.BORDER);
                GridDataFactory.fillDefaults().hint(VALUE_WIDTH, SWT.DEFAULT).applyTo(text);
                text.addModifyListener(new ModifyListener() {
                    @Override public void modifyText(ModifyEvent e) { recheckDirty(); }
                });
                widget = text;
                break;
            }
        }
        editors.put(p, widget);

        Label hint = toolkit.createLabel(valueCell, "", SWT.NONE);
        GridDataFactory.fillDefaults().grab(true, false).applyTo(hint);
        if (p == Param.NUMBER_OF_DEVICES) this.derivedHint = hint;
    }

    private void recheckDirty() {
        boolean dirty = false;
        for (Map.Entry<Param, Control> e : editors.entrySet()) {
            String now = widgetValue(e.getValue());
            String orig = originalValues.getOrDefault(e.getKey(), "");
            if (!now.equals(orig)) { dirty = true; break; }
        }
        ((MemIfModuleManagerEditor) getEditor()).setDirty(dirty);
        updateDerivedHint();
    }

    private static String widgetValue(Control w) {
        if (w instanceof Combo) return ((Combo) w).getText();
        if (w instanceof Text)  return ((Text)  w).getText();
        return "";
    }

    private void updateDerivedHint() {
        if (derivedHint == null || derivedHint.isDisposed()) return;
        String src = data == null ? null : data.getSourcePath();
        if (src == null) { derivedHint.setText(""); return; }
        try {
            int derived = MemIfDerivedCalculator.calculateForMemIfFile(src);
            String configuredStr = widgetValue(editors.get(Param.NUMBER_OF_DEVICES));
            int configured;
            try { configured = Integer.parseInt(configuredStr.trim()); }
            catch (NumberFormatException nfe) { configured = -1; }
            String tag = (configured == derived)
                    ? String.format("(derived from NvM: %d ✓)", derived)
                    : String.format("(derived from NvM: %d — configured value differs)", derived);
            derivedHint.setText(tag);
        } catch (Throwable t) {
            derivedHint.setText("(derived: " + t.getClass().getSimpleName() + ")");
        }
        derivedHint.getParent().layout();
    }

    /** Called by the editor's doSave. Returns count written, or -1 on error. */
    public int commit() {
        String sourcePath = data.getSourcePath();
        if (sourcePath == null) return -1;
        int count = 0;
        for (Map.Entry<Param, Control> e : editors.entrySet()) {
            Param p = e.getKey();
            String now = widgetValue(e.getValue());
            String orig = originalValues.getOrDefault(p, "");
            if (now.equals(orig)) continue;
            try {
                if (MemIfArxmlWriter.writeParam(sourcePath, p.shortName, now)) {
                    count++;
                }
            } catch (Throwable t) {
                t.printStackTrace();
                return -1;
            }
        }
        return count;
    }

    public void reload(MemIfData fresh) {
        if (fresh == null) return;
        this.data = fresh;
        Display.getDefault().asyncExec(new Runnable() {
            @Override public void run() {
                applyValues();
            }
        });
    }

    private void applyValues() {
        applyOne(Param.DEV_ERROR_DETECT,  data.getMemIfDevErrorDetect());
        applyOne(Param.NUMBER_OF_DEVICES, data.getMemIfNumberOfDevices());
        applyOne(Param.VERSION_INFO_API,  data.getMemIfVersionInfoApi());
        applyOne(Param.MODULE_VERSION,    data.getMemIfModuleVersion());
        updateDerivedHint();
    }

    private void applyOne(Param p, String value) {
        Control w = editors.get(p);
        if (w == null || w.isDisposed()) return;
        String s = value == null ? "" : value;
        if (w instanceof Combo) ((Combo) w).setText(s);
        else if (w instanceof Text) ((Text) w).setText(s);
        originalValues.put(p, s);
    }
}

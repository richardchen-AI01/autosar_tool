package cn.com.myorg.bswbuilder.ui.views;

import java.util.LinkedHashMap;
import java.util.Map;

import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.jface.layout.GridDataFactory;
import org.eclipse.jface.layout.GridLayoutFactory;
import org.eclipse.swt.SWT;
import org.eclipse.swt.events.FocusAdapter;
import org.eclipse.swt.events.FocusEvent;
import org.eclipse.swt.events.SelectionAdapter;
import org.eclipse.swt.events.SelectionEvent;
import org.eclipse.swt.graphics.Color;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Combo;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.TabFolder;
import org.eclipse.swt.widgets.TabItem;
import org.eclipse.swt.widgets.Text;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.part.ViewPart;

import cn.com.myorg.bswbuilder.modules.memif.data.MemIfArxmlReader;
import cn.com.myorg.bswbuilder.modules.memif.data.MemIfArxmlWriter;
import cn.com.myorg.bswbuilder.modules.memif.data.MemIfData;
import cn.com.myorg.bswbuilder.modules.memif.data.MemIfDerivedCalculator;
import cn.com.myorg.bswbuilder.modules.memif.data.MemIfParamMetadata;

/**
 * Property form view — right-hand side of the EB-tresos style perspective.
 *
 * <p>Phase A (read) + Phase B (write): each of the four MemIfGeneral
 * parameters becomes an editable widget (Combo for booleans, Text for
 * the integer / string). A Save button calls
 * {@link MemIfArxmlWriter#writeParam(String, String, String)} per changed
 * field, then reloads via {@link MemIfArxmlReader#read(String)} to refresh
 * the form (defensive — proves the round-trip).
 *
 * <p>The chosen write-back is **byte-equal string surgery** (no EMF
 * EditingDomain). See ADR rationale in MemIfArxmlWriter Javadoc and
 * docs/MEMIF_REPLICA_PLAN.md §3.
 */
public class PropertyFormView extends ViewPart {

    public static final String ID =
            "cn.com.myorg.bswbuilder.ui.views.PropertyForm";

    private static final Color BG = new Color(Display.getDefault(), 255, 255, 255);
    private static final Color LABEL_FG = new Color(Display.getDefault(), 70, 70, 70);
    private static final Color SUBTLE = new Color(Display.getDefault(), 120, 120, 120);
    private static final Color VALUE_FG = new Color(Display.getDefault(), 25, 25, 25);
    private static final Color PLACEHOLDER_FG = new Color(Display.getDefault(), 160, 160, 160);

    /** Param shortName → (display label, schema type) */
    private enum Param {
        DEV_ERROR_DETECT("MemIfDevErrorDetect", "Memif Dev Error Detect:", Type.BOOLEAN),
        NUMBER_OF_DEVICES("MemIfNumberOfDevices", "Memif Number Of Devices:", Type.INTEGER),
        VERSION_INFO_API("MemIfVersionInfoApi", "Memif Version Info Api:", Type.BOOLEAN),
        MODULE_VERSION("MemIfModuleVersion", "Memif Module Version:", Type.STRING);

        final String shortName;
        final String label;
        final Type type;
        Param(String shortName, String label, Type type) {
            this.shortName = shortName;
            this.label = label;
            this.type = type;
        }
    }

    private enum Type { BOOLEAN, INTEGER, STRING }

    private Composite breadcrumbArea;
    private Composite formArea;
    private Label breadcrumbModule;
    private Label breadcrumbContainer;

    /** Set on showMemIf; null when nothing loaded. */
    private String currentSourcePath;

    /** Per-Param: the widget whose user-edited value we'll write back. */
    private final Map<Param, Control> editors = new LinkedHashMap<>();

    /** Per-Param: the original value loaded from disk (used to skip no-op writes). */
    private final Map<Param, String> originalValues = new LinkedHashMap<>();

    private Button saveButton;
    private Button recomputeButton;
    private Label statusLabel;
    private Label derivedHint;  // shown next to NumberOfDevices widget

    // Phase E — bottom Properties tabs
    private Text descriptionText;
    private Text definitionText;
    private Text statusTabText;
    private Param focusedParam;

    @Override
    public void createPartControl(Composite parent) {
        parent.setBackground(BG);
        GridLayoutFactory.fillDefaults().margins(0, 0).spacing(0, 0).applyTo(parent);

        // Breadcrumb row (mutable)
        breadcrumbArea = new Composite(parent, SWT.NONE);
        breadcrumbArea.setBackground(BG);
        GridLayoutFactory.fillDefaults().numColumns(5).margins(12, 8).spacing(6, 0)
                .applyTo(breadcrumbArea);
        GridDataFactory.fillDefaults().grab(true, false).applyTo(breadcrumbArea);

        Label home = new Label(breadcrumbArea, SWT.NONE);
        home.setText("◀ ▸ ");
        home.setBackground(BG);
        home.setForeground(SUBTLE);

        breadcrumbModule = new Label(breadcrumbArea, SWT.NONE);
        breadcrumbModule.setText("(no module)");
        breadcrumbModule.setBackground(BG);
        breadcrumbModule.setForeground(LABEL_FG);

        Label arrow = new Label(breadcrumbArea, SWT.NONE);
        arrow.setText(" ▸ ");
        arrow.setBackground(BG);
        arrow.setForeground(SUBTLE);

        breadcrumbContainer = new Label(breadcrumbArea, SWT.NONE);
        breadcrumbContainer.setText("");
        breadcrumbContainer.setBackground(BG);
        breadcrumbContainer.setForeground(LABEL_FG);

        // Form area (mutable). 3 columns: label | widget | derived-hint.
        // Most rows leave the hint column empty.
        formArea = new Composite(parent, SWT.NONE);
        formArea.setBackground(BG);
        GridLayoutFactory.fillDefaults()
                .numColumns(3)
                .margins(20, 10)
                .spacing(8, 8)
                .applyTo(formArea);
        GridDataFactory.fillDefaults().grab(true, true).applyTo(formArea);

        // Phase E — bottom Properties tabs (Description / Definition / Status)
        TabFolder tabs = new TabFolder(parent, SWT.BOTTOM);
        GridDataFactory.fillDefaults().grab(true, false).hint(SWT.DEFAULT, 130).applyTo(tabs);

        descriptionText = makeTabText(tabs, "Description");
        definitionText  = makeTabText(tabs, "Definition");
        statusTabText   = makeTabText(tabs, "Status");

        showPlaceholder();
        setPropertyTabsFor(null);
    }

    private static Text makeTabText(TabFolder parent, String title) {
        TabItem item = new TabItem(parent, SWT.NONE);
        item.setText(title);
        Text t = new Text(parent, SWT.MULTI | SWT.WRAP | SWT.READ_ONLY | SWT.V_SCROLL);
        t.setBackground(BG);
        t.setForeground(VALUE_FG);
        item.setControl(t);
        return t;
    }

    private void showPlaceholder() {
        clearForm();
        currentSourcePath = null;
        editors.clear();
        originalValues.clear();

        Label placeholder = new Label(formArea, SWT.NONE);
        placeholder.setText("Select a module from the left to view its parameters.");
        placeholder.setForeground(PLACEHOLDER_FG);
        placeholder.setBackground(BG);
        GridDataFactory.fillDefaults().span(3, 1).grab(true, false).applyTo(placeholder);
        formArea.layout(true, true);
    }

    private void clearForm() {
        if (formArea == null || formArea.isDisposed()) return;
        for (Control c : formArea.getChildren()) {
            c.dispose();
        }
    }

    /**
     * Populate the form with the four MemIfGeneral parameters and arm Save.
     */
    public void showMemIf(MemIfData data) {
        if (formArea == null || formArea.isDisposed()) return;

        breadcrumbModule.setText("MemIf");
        breadcrumbContainer.setText("MemIfGeneral");
        breadcrumbArea.layout(true, true);

        clearForm();
        editors.clear();
        originalValues.clear();
        currentSourcePath = data.getSourcePath();

        addEditableRow(Param.DEV_ERROR_DETECT,    data.getMemIfDevErrorDetect());
        addEditableRow(Param.NUMBER_OF_DEVICES,   data.getMemIfNumberOfDevices());
        addEditableRow(Param.VERSION_INFO_API,    data.getMemIfVersionInfoApi());
        addEditableRow(Param.MODULE_VERSION,      data.getMemIfModuleVersion());

        // Action row: Save + Recompute from NvM
        saveButton = new Button(formArea, SWT.PUSH);
        saveButton.setText("Save");
        GridDataFactory.fillDefaults()
                .align(SWT.END, SWT.CENTER)
                .indent(0, 12)
                .applyTo(saveButton);
        saveButton.addSelectionListener(new SelectionAdapter() {
            @Override public void widgetSelected(SelectionEvent e) {
                onSave();
            }
        });

        recomputeButton = new Button(formArea, SWT.PUSH);
        recomputeButton.setText("Recompute from NvM");
        GridDataFactory.fillDefaults()
                .align(SWT.BEGINNING, SWT.CENTER)
                .indent(0, 12)
                .applyTo(recomputeButton);
        recomputeButton.addSelectionListener(new SelectionAdapter() {
            @Override public void widgetSelected(SelectionEvent e) {
                onRecomputeFromNvM();
            }
        });

        statusLabel = new Label(formArea, SWT.NONE);
        statusLabel.setText("");
        statusLabel.setForeground(SUBTLE);
        statusLabel.setBackground(BG);
        GridDataFactory.fillDefaults().grab(true, false).indent(0, 12).applyTo(statusLabel);

        Label src = new Label(formArea, SWT.NONE);
        src.setText("source: " + data.getSourcePath());
        src.setForeground(SUBTLE);
        src.setBackground(BG);
        GridDataFactory.fillDefaults().span(3, 1).grab(true, false).indent(0, 12).applyTo(src);

        // Auto-compute the NvM-derived NumberOfDevices once on initial show.
        updateDerivedHint();

        formArea.layout(true, true);
    }

    private void addEditableRow(Param param, String currentValue) {
        Label l = new Label(formArea, SWT.NONE);
        l.setText(param.label);
        l.setForeground(LABEL_FG);
        l.setBackground(BG);
        GridDataFactory.fillDefaults().align(SWT.END, SWT.CENTER).applyTo(l);

        String display = (currentValue == null) ? "" : currentValue;
        originalValues.put(param, display);

        Control widget;
        switch (param.type) {
            case BOOLEAN:
                Combo combo = new Combo(formArea, SWT.READ_ONLY);
                combo.setItems("false", "true");
                combo.setText(display.isEmpty() ? "false" : display);
                combo.setBackground(BG);
                GridDataFactory.fillDefaults().hint(120, SWT.DEFAULT).applyTo(combo);
                widget = combo;
                break;
            case INTEGER:
            case STRING:
            default:
                Text text = new Text(formArea, SWT.BORDER);
                text.setText(display);
                GridDataFactory.fillDefaults().hint(220, SWT.DEFAULT).applyTo(text);
                widget = text;
                break;
        }
        editors.put(param, widget);

        // Phase E: focus listener — updates bottom Property tabs when this
        // widget becomes the input focus.
        widget.addFocusListener(new FocusAdapter() {
            @Override public void focusGained(FocusEvent e) {
                setPropertyTabsFor(param);
            }
        });

        // 3rd column: derived hint or empty filler. For NumberOfDevices we
        // stash the Label so updateDerivedHint() can rewrite it later.
        Label hint = new Label(formArea, SWT.NONE);
        hint.setText("");
        hint.setForeground(SUBTLE);
        hint.setBackground(BG);
        GridDataFactory.fillDefaults().grab(true, false).applyTo(hint);
        if (param == Param.NUMBER_OF_DEVICES) {
            this.derivedHint = hint;
        }
    }

    /**
     * Phase E: update the bottom 3 tabs to show metadata for the given
     * parameter. {@code null} resets all tabs to empty placeholder text.
     */
    private void setPropertyTabsFor(Param param) {
        focusedParam = param;
        if (descriptionText == null || descriptionText.isDisposed()) return;

        if (param == null) {
            descriptionText.setText("(focus a parameter widget to see its description)");
            definitionText.setText("(focus a parameter widget to see its schema definition)");
            statusTabText.setText("(focus a parameter widget to see its current value / dirty flag)");
            return;
        }

        MemIfParamMetadata.Entry meta = MemIfParamMetadata.get(param.shortName);
        if (meta == null) {
            descriptionText.setText("(no metadata for " + param.shortName + ")");
            definitionText.setText("");
            statusTabText.setText("");
            return;
        }

        descriptionText.setText(
                meta.description + "\n\n" + meta.introduction);

        StringBuilder def = new StringBuilder();
        def.append("Parameter: ").append(meta.shortName).append("\n");
        def.append("Type:      ").append(meta.typeText).append("\n");
        def.append("Origin:    ").append(meta.origin).append("\n");
        def.append("Default:   ").append(meta.defaultValue);
        definitionText.setText(def.toString());

        StringBuilder st = new StringBuilder();
        Control widget = editors.get(param);
        String currentValue = widget != null ? widgetValue(widget) : "(unset)";
        String origValue = originalValues.getOrDefault(param, "");
        boolean dirty = !currentValue.equals(origValue);
        st.append("Current value: ").append(currentValue).append("\n");
        st.append("Original:      ").append(origValue).append("\n");
        st.append("Dirty:         ").append(dirty ? "yes (unsaved)" : "no").append("\n");
        if (param == Param.NUMBER_OF_DEVICES && currentSourcePath != null) {
            try {
                int derived = MemIfDerivedCalculator.calculateForMemIfFile(currentSourcePath);
                st.append("Derived:       ").append(derived)
                        .append(" ").append(MemIfDerivedCalculator.describe(derived));
            } catch (Throwable ignored) {
                st.append("Derived:       (error)");
            }
        }
        statusTabText.setText(st.toString());
    }

    private String widgetValue(Control w) {
        if (w instanceof Combo) return ((Combo) w).getText();
        if (w instanceof Text)  return ((Text)  w).getText();
        return "";
    }

    private void onSave() {
        if (currentSourcePath == null) {
            return;
        }

        int writeCount = 0;
        StringBuilder errors = new StringBuilder();

        for (Map.Entry<Param, Control> e : editors.entrySet()) {
            Param param = e.getKey();
            String newVal = widgetValue(e.getValue());
            String origVal = originalValues.getOrDefault(param, "");
            if (newVal.equals(origVal)) {
                continue;
            }
            try {
                boolean wrote = MemIfArxmlWriter.writeParam(
                        currentSourcePath, param.shortName, newVal);
                if (wrote) {
                    writeCount++;
                }
            } catch (Throwable t) {
                errors.append(param.shortName).append(": ").append(t.getMessage()).append("\n");
            }
        }

        if (errors.length() > 0) {
            MessageDialog.openError(saveButton.getShell(),
                    "Save failed (some fields)", errors.toString());
        } else if (writeCount == 0) {
            statusLabel.setText("No changes to save.");
        } else {
            statusLabel.setText(String.format("Saved %d field(s) — reloading …", writeCount));
            // Reload from disk so display + originalValues realign
            try {
                MemIfData fresh = MemIfArxmlReader.read(currentSourcePath);
                showMemIf(fresh);
                statusLabel.setText(String.format("Saved %d field(s); form reloaded.", writeCount));
            } catch (Throwable t) {
                statusLabel.setText("Saved but reload failed: " + t.getMessage());
            }
        }
    }

    /**
     * Re-read the workspace's NvM.arxml and update the derived-hint label
     * next to the NumberOfDevices widget. Called once on showMemIf, and
     * each time the user clicks "Recompute from NvM".
     */
    private void updateDerivedHint() {
        if (derivedHint == null || derivedHint.isDisposed() || currentSourcePath == null) {
            return;
        }
        try {
            int derived = MemIfDerivedCalculator.calculateForMemIfFile(currentSourcePath);
            String configuredStr = widgetValue(editors.get(Param.NUMBER_OF_DEVICES));
            int configured;
            try { configured = Integer.parseInt(configuredStr.trim()); }
            catch (NumberFormatException nfe) { configured = -1; }

            String tag = (configured == derived)
                    ? String.format("(derived from NvM: %d ✓)", derived)
                    : String.format("(derived from NvM: %d  — configured value differs)", derived);
            derivedHint.setText(tag);
        } catch (Throwable t) {
            derivedHint.setText("(derived: error " + t.getClass().getSimpleName() + ")");
        }
        derivedHint.getParent().layout();
    }

    private void onRecomputeFromNvM() {
        if (currentSourcePath == null) {
            return;
        }
        updateDerivedHint();
        if (statusLabel != null && !statusLabel.isDisposed()) {
            statusLabel.setText("Recomputed derived NumberOfDevices from NvM.");
        }
    }

    @Override
    public void setFocus() {
        // no-op
    }

    /**
     * Convenience: locate the singleton PropertyFormView in the active
     * workbench page, opening it if necessary, and push the given MemIfData.
     */
    public static PropertyFormView showAndPopulate(MemIfData data) {
        try {
            org.eclipse.ui.IWorkbenchPage page = PlatformUI.getWorkbench()
                    .getActiveWorkbenchWindow().getActivePage();
            org.eclipse.ui.IViewPart view = page.showView(ID);
            if (view instanceof PropertyFormView) {
                PropertyFormView v = (PropertyFormView) view;
                v.showMemIf(data);
                return v;
            }
        } catch (Throwable t) {
            t.printStackTrace();
        }
        return null;
    }
}

package cn.com.myorg.bswbuilder.ui.views;

import java.util.LinkedHashMap;
import java.util.Map;

import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.jface.layout.GridDataFactory;
import org.eclipse.jface.layout.GridLayoutFactory;
import org.eclipse.swt.SWT;
import org.eclipse.swt.events.SelectionAdapter;
import org.eclipse.swt.events.SelectionEvent;
import org.eclipse.swt.graphics.Color;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Combo;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Text;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.part.ViewPart;

import cn.com.myorg.bswbuilder.modules.memif.data.MemIfArxmlReader;
import cn.com.myorg.bswbuilder.modules.memif.data.MemIfArxmlWriter;
import cn.com.myorg.bswbuilder.modules.memif.data.MemIfData;

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
    private Label statusLabel;

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

        // Form area (mutable)
        formArea = new Composite(parent, SWT.NONE);
        formArea.setBackground(BG);
        GridLayoutFactory.fillDefaults()
                .numColumns(2)
                .margins(20, 10)
                .spacing(8, 8)
                .applyTo(formArea);
        GridDataFactory.fillDefaults().grab(true, true).applyTo(formArea);

        showPlaceholder();
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
        GridDataFactory.fillDefaults().span(2, 1).grab(true, false).applyTo(placeholder);
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

        // Save row
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

        statusLabel = new Label(formArea, SWT.NONE);
        statusLabel.setText("");
        statusLabel.setForeground(SUBTLE);
        statusLabel.setBackground(BG);
        GridDataFactory.fillDefaults().grab(true, false).indent(0, 12).applyTo(statusLabel);

        Label src = new Label(formArea, SWT.NONE);
        src.setText("source: " + data.getSourcePath());
        src.setForeground(SUBTLE);
        src.setBackground(BG);
        GridDataFactory.fillDefaults().span(2, 1).grab(true, false).indent(0, 12).applyTo(src);

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

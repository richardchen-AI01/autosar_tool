package cn.com.myorg.bswbuilder.ui.views;

import org.eclipse.jface.layout.GridDataFactory;
import org.eclipse.jface.layout.GridLayoutFactory;
import org.eclipse.swt.SWT;
import org.eclipse.swt.graphics.Color;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Label;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.part.ViewPart;

import cn.com.myorg.bswbuilder.modules.memif.data.MemIfData;

/**
 * Property form view — right-hand side of the EB-tresos style perspective.
 *
 * <p>Phase A delivery: data-driven, read-only. Default state shows a
 * placeholder; {@link #showMemIf(MemIfData)} repopulates the form with the
 * four MemIfGeneral parameters from a loaded ARXML.
 *
 * <p>Sphinx auto-render of an EMF Forms editor is the longer-term path
 * (Phase B+); for read-only Phase A we manually render the four rows so
 * we don't need a TransactionalEditingDomain yet.
 */
public class PropertyFormView extends ViewPart {

    public static final String ID =
            "cn.com.myorg.bswbuilder.ui.views.PropertyForm";

    private static final Color BG = new Color(Display.getDefault(), 255, 255, 255);
    private static final Color LABEL_FG = new Color(Display.getDefault(), 70, 70, 70);
    private static final Color SUBTLE = new Color(Display.getDefault(), 120, 120, 120);
    private static final Color VALUE_FG = new Color(Display.getDefault(), 25, 25, 25);
    private static final Color PLACEHOLDER_FG = new Color(Display.getDefault(), 160, 160, 160);

    private Composite breadcrumbArea;
    private Composite formArea;
    private Label breadcrumbModule;
    private Label breadcrumbContainer;

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
     * Populate the form with the four MemIfGeneral parameters from a loaded
     * ARXML. Phase A delivery — read-only labels.
     */
    public void showMemIf(MemIfData data) {
        if (formArea == null || formArea.isDisposed()) return;

        breadcrumbModule.setText("MemIf");
        breadcrumbContainer.setText("MemIfGeneral");
        breadcrumbArea.layout(true, true);

        clearForm();
        addReadOnlyRow(formArea, "Memif Dev Error Detect:",  formatValue(data.getMemIfDevErrorDetect()));
        addReadOnlyRow(formArea, "Memif Number Of Devices:", formatValue(data.getMemIfNumberOfDevices()));
        addReadOnlyRow(formArea, "Memif Version Info Api:",  formatValue(data.getMemIfVersionInfoApi()));
        addReadOnlyRow(formArea, "Memif Module Version:",    formatValue(data.getMemIfModuleVersion()));

        Label src = new Label(formArea, SWT.NONE);
        src.setText("source: " + data.getSourcePath());
        src.setForeground(SUBTLE);
        src.setBackground(BG);
        GridDataFactory.fillDefaults().span(2, 1).grab(true, false).indent(0, 12).applyTo(src);

        formArea.layout(true, true);
    }

    private static String formatValue(String raw) {
        return (raw == null || raw.isEmpty()) ? "(unset)" : raw;
    }

    private void addReadOnlyRow(Composite parent, String label, String value) {
        Label l = new Label(parent, SWT.NONE);
        l.setText(label);
        l.setForeground(LABEL_FG);
        l.setBackground(BG);
        GridDataFactory.fillDefaults().align(SWT.END, SWT.CENTER).applyTo(l);

        Label v = new Label(parent, SWT.NONE);
        v.setText(value);
        v.setForeground(VALUE_FG);
        v.setBackground(BG);
        GridDataFactory.fillDefaults().grab(true, false).applyTo(v);
    }

    @Override
    public void setFocus() {
        // no-op
    }

    /**
     * Convenience: locate the singleton PropertyFormView in the active
     * workbench page, opening it (creating if necessary) and pushing the
     * given MemIfData. Returns null if no active workbench window exists.
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

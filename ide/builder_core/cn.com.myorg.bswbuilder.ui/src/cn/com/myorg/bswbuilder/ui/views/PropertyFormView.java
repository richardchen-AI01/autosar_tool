package cn.com.myorg.bswbuilder.ui.views;

import org.eclipse.jface.layout.GridDataFactory;
import org.eclipse.jface.layout.GridLayoutFactory;
import org.eclipse.swt.SWT;
import org.eclipse.swt.graphics.Color;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Text;
import org.eclipse.ui.part.ViewPart;

/**
 * Property form view — right-hand side of the EB-tresos style perspective.
 *
 * <p>Shows a sample container's parameter form (Label + widget + required '*'),
 * mirroring the reference UI's "Safe Bsw Checks: ☑ *" pattern. v0.1 ships
 * a static mock-up so the layout polish is visible without needing ARTOP
 * integration; v0.2 will wire to the actual selected ECUC container.
 */
public class PropertyFormView extends ViewPart {

    public static final String ID =
            "cn.com.myorg.bswbuilder.ui.views.PropertyForm";

    private static final Color BG = new Color(Display.getDefault(), 255, 255, 255);
    private static final Color LABEL_FG = new Color(Display.getDefault(), 70, 70, 70);
    private static final Color SUBTLE = new Color(Display.getDefault(), 120, 120, 120);
    private static final Color REQUIRED_RED = new Color(Display.getDefault(), 200, 80, 80);

    @Override
    public void createPartControl(Composite parent) {
        parent.setBackground(BG);
        GridLayoutFactory.fillDefaults().margins(0, 0).spacing(0, 0).applyTo(parent);

        // Breadcrumb row
        Composite breadcrumb = new Composite(parent, SWT.NONE);
        breadcrumb.setBackground(BG);
        GridLayoutFactory.fillDefaults().numColumns(5).margins(12, 8).spacing(6, 0)
                .applyTo(breadcrumb);
        GridDataFactory.fillDefaults().grab(true, false).applyTo(breadcrumb);

        Label home = new Label(breadcrumb, SWT.NONE);
        home.setText("◀ ▸ ");
        home.setBackground(BG);
        home.setForeground(SUBTLE);
        Label memif = makeBreadcrumbLink(breadcrumb, "MemIf");
        Label arrow = new Label(breadcrumb, SWT.NONE);
        arrow.setText(" ▸ ");
        arrow.setBackground(BG);
        arrow.setForeground(SUBTLE);
        Label memifGen = makeBreadcrumbLink(breadcrumb, "MemIfGeneral");

        // Form rows
        Composite form = new Composite(parent, SWT.NONE);
        form.setBackground(BG);
        GridLayoutFactory.fillDefaults()
                .numColumns(3)
                .margins(20, 10)
                .spacing(8, 8)
                .applyTo(form);
        GridDataFactory.fillDefaults().grab(true, true).applyTo(form);

        // Sample: real MemIfGeneral parameter set (from MemIfDef.arxml)
        addCheckRow(form, "Memif Dev Error Detect:",         true,  true);
        addCheckRow(form, "Memif Number Of Devices:",        false, false);
        addCheckRow(form, "Memif Version Info Api:",         false, true);
        addCheckRow(form, "Memif Module Version:",           false, false);
        addTextRow (form, "User Config File:",               "",    false);
        addCheckRow(form, "Safe Bsw Checks:",                true,  false);
        addCheckRow(form, "Single Rx Buffer Optimization:",  false, false);
        addCheckRow(form, "Split Main Function:",            false, false);
        addCheckRow(form, "Synchronous Transmission:",       true,  false);
        addCheckRow(form, "Transmit Cancellation:",          false, false);
        addCheckRow(form, "Transmit Queue:",                 false, false);
    }

    private Label makeBreadcrumbLink(Composite parent, String text) {
        Label l = new Label(parent, SWT.NONE);
        l.setText(text);
        l.setBackground(BG);
        l.setForeground(LABEL_FG);
        return l;
    }

    private void addCheckRow(Composite form, String label, boolean checked, boolean required) {
        Label l = new Label(form, SWT.NONE);
        l.setText(label);
        l.setForeground(LABEL_FG);
        l.setBackground(BG);
        GridDataFactory.fillDefaults().grab(true, false).align(SWT.END, SWT.CENTER).applyTo(l);

        Button cb = new Button(form, SWT.CHECK);
        cb.setBackground(BG);
        cb.setSelection(checked);
        GridDataFactory.fillDefaults().hint(80, SWT.DEFAULT).applyTo(cb);

        Label req = new Label(form, SWT.NONE);
        req.setText(required ? "*" : "");
        req.setForeground(REQUIRED_RED);
        req.setBackground(BG);
        GridDataFactory.fillDefaults().hint(10, SWT.DEFAULT).applyTo(req);
    }

    private void addTextRow(Composite form, String label, String value, boolean required) {
        Label l = new Label(form, SWT.NONE);
        l.setText(label);
        l.setForeground(LABEL_FG);
        l.setBackground(BG);
        GridDataFactory.fillDefaults().grab(true, false).align(SWT.END, SWT.CENTER).applyTo(l);

        Text t = new Text(form, SWT.BORDER);
        t.setText(value);
        GridDataFactory.fillDefaults().hint(180, SWT.DEFAULT).applyTo(t);

        Label req = new Label(form, SWT.NONE);
        req.setText(required ? "*" : "");
        req.setForeground(REQUIRED_RED);
        req.setBackground(BG);
        GridDataFactory.fillDefaults().hint(10, SWT.DEFAULT).applyTo(req);
    }

    @Override
    public void setFocus() {
        // no-op
    }
}

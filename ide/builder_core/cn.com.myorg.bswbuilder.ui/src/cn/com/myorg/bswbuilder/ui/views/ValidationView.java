package cn.com.myorg.bswbuilder.ui.views;

import org.eclipse.jface.layout.GridDataFactory;
import org.eclipse.jface.layout.GridLayoutFactory;
import org.eclipse.swt.SWT;
import org.eclipse.swt.graphics.Color;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Table;
import org.eclipse.swt.widgets.TableColumn;
import org.eclipse.swt.widgets.TableItem;
import org.eclipse.ui.part.ViewPart;

/**
 * Validation findings view — bottom-right of the EB-tresos style perspective.
 *
 * <p>Surfaces bswval JSON output as a 3-column table. v0.1 ships a small
 * mock-up; v0.2 will wire to the validator JSON output and Eclipse marker
 * framework so findings appear in the standard ProblemView too.
 */
public class ValidationView extends ViewPart {

    public static final String ID =
            "cn.com.myorg.bswbuilder.ui.views.Validation";

    private static final Color BG = new Color(Display.getDefault(), 255, 255, 255);

    @Override
    public void createPartControl(Composite parent) {
        parent.setBackground(BG);
        GridLayoutFactory.fillDefaults().margins(0, 0).spacing(0, 4).applyTo(parent);

        Label header = new Label(parent, SWT.NONE);
        header.setText("  Validation");
        header.setBackground(BG);
        header.setForeground(new Color(Display.getDefault(), 33, 91, 152));
        GridDataFactory.fillDefaults().grab(true, false).indent(0, 4).applyTo(header);

        Table table = new Table(parent, SWT.BORDER | SWT.FULL_SELECTION | SWT.V_SCROLL);
        table.setHeaderVisible(true);
        table.setLinesVisible(true);
        GridDataFactory.fillDefaults().grab(true, true).applyTo(table);

        TableColumn level = new TableColumn(table, SWT.NONE);
        level.setText("Level");
        level.setWidth(80);
        TableColumn rule = new TableColumn(table, SWT.NONE);
        rule.setText("Rule");
        rule.setWidth(220);
        TableColumn descr = new TableColumn(table, SWT.NONE);
        descr.setText("Description");
        descr.setWidth(500);

        // Mock findings (matches what bswval produces on Demo_S32K148_BAD_2170)
        addRow(table, "INFO",  "—",
                "Click 'Validate MemIf' on the BSW menu to populate this view.");
        addRow(table, "INFO",  "—",
                "Findings load from bswval's JSON output (see validator/Bsw/MemIf/MemIfMessages.json).");

        // dummy spacer
        new TableItem(table, SWT.NONE);
    }

    private void addRow(Table table, String level, String rule, String description) {
        TableItem item = new TableItem(table, SWT.NONE);
        item.setText(new String[]{level, rule, description});
    }

    @Override
    public void setFocus() {
        // no-op
    }
}

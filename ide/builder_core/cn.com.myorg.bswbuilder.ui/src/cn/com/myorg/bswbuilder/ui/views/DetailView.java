package cn.com.myorg.bswbuilder.ui.views;

import org.eclipse.jface.layout.GridDataFactory;
import org.eclipse.jface.layout.GridLayoutFactory;
import org.eclipse.jface.viewers.ISelection;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.swt.SWT;
import org.eclipse.swt.graphics.Color;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Text;
import org.eclipse.ui.ISelectionListener;
import org.eclipse.ui.IWorkbenchPart;
import org.eclipse.ui.part.ViewPart;

/**
 * Detail view — bottom-right tab in the perspective. Mirrors iSoft V25.10's
 * {@code cn.com.isoft.bswbuilder.ui.detailview} (icons/page_white_edit.png),
 * which shows the description of whatever's selected in the editor /
 * Autosar Explorer.
 *
 * <p>v0.1 minimum: a single multi-line read-only Text that shows the
 * selected ECUC parameter / container's description, sourced from
 * {@code MemIfParamMetadata} when the selection is one of MemIf's params.
 * Expanded later as more modules wire in.
 */
public class DetailView extends ViewPart implements ISelectionListener {

    public static final String ID = "cn.com.myorg.bswbuilder.ui.views.Detail";

    private static final Color BG = new Color(Display.getDefault(), 255, 255, 255);
    private static final Color TITLE_FG = new Color(Display.getDefault(), 33, 91, 152);
    private static final Color BODY_FG  = new Color(Display.getDefault(), 50, 50, 50);

    private Label titleLabel;
    private Text bodyText;

    @Override
    public void createPartControl(Composite parent) {
        parent.setBackground(BG);
        GridLayoutFactory.fillDefaults().margins(8, 8).spacing(0, 4).applyTo(parent);

        titleLabel = new Label(parent, SWT.NONE);
        titleLabel.setText("(no selection)");
        titleLabel.setForeground(TITLE_FG);
        titleLabel.setBackground(BG);
        GridDataFactory.fillDefaults().grab(true, false).applyTo(titleLabel);

        bodyText = new Text(parent, SWT.MULTI | SWT.WRAP | SWT.READ_ONLY | SWT.V_SCROLL);
        bodyText.setText("Select a parameter or container to see its description here.");
        bodyText.setForeground(BODY_FG);
        bodyText.setBackground(BG);
        GridDataFactory.fillDefaults().grab(true, true).applyTo(bodyText);

        getSite().getWorkbenchWindow().getSelectionService().addPostSelectionListener(this);
    }

    @Override
    public void selectionChanged(IWorkbenchPart part, ISelection selection) {
        if (!(selection instanceof IStructuredSelection)) return;
        Object first = ((IStructuredSelection) selection).getFirstElement();
        if (first == null) {
            setContent("(no selection)", "");
            return;
        }
        // v0.1: just show the toString of the selected element. v0.2 will dispatch
        // by element type into proper schema metadata (Description / Definition / Status).
        setContent(first.getClass().getSimpleName(), first.toString());
    }

    private void setContent(String title, String body) {
        if (titleLabel != null && !titleLabel.isDisposed()) {
            titleLabel.setText(title);
        }
        if (bodyText != null && !bodyText.isDisposed()) {
            bodyText.setText(body == null ? "" : body);
        }
    }

    @Override
    public void dispose() {
        getSite().getWorkbenchWindow().getSelectionService().removePostSelectionListener(this);
        super.dispose();
    }

    @Override
    public void setFocus() {
        if (bodyText != null) bodyText.setFocus();
    }
}

package cn.com.myorg.bswbuilder.ui.editors;

import org.eclipse.jface.layout.GridDataFactory;
import org.eclipse.jface.layout.GridLayoutFactory;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Label;
import org.eclipse.ui.forms.IManagedForm;
import org.eclipse.ui.forms.editor.FormEditor;
import org.eclipse.ui.forms.editor.FormPage;
import org.eclipse.ui.forms.widgets.ScrolledForm;

/**
 * Trivial fallback page — used by {@link GenericModuleEditor} when normal
 * page enumeration would produce 0 pages (which crashes
 * {@link org.eclipse.ui.part.MultiPageEditorPart#setActivePage(int)}'s
 * assertion). Shows a single error message so the user sees what went wrong
 * instead of "Failed to create the part's controls".
 */
public class EditorOpenFailurePage extends FormPage {

    private final String reason;

    public EditorOpenFailurePage(FormEditor editor, String title, String reason) {
        super(editor, "errorPage", title);
        this.reason = reason;
    }

    @Override
    protected void createFormContent(IManagedForm managedForm) {
        ScrolledForm form = managedForm.getForm();
        form.setText("Editor could not open — see message");
        Composite body = form.getBody();
        GridLayoutFactory.fillDefaults().margins(20, 20).applyTo(body);

        Label l = new Label(body, SWT.WRAP);
        l.setText(reason == null ? "Unknown error." : reason);
        GridDataFactory.fillDefaults().grab(true, false).applyTo(l);
    }
}

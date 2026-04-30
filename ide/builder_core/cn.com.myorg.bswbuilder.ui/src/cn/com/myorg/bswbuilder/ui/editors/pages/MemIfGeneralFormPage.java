package cn.com.myorg.bswbuilder.ui.editors.pages;

import java.util.LinkedHashMap;
import java.util.Map;

import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.jface.layout.GridDataFactory;
import org.eclipse.jface.layout.GridLayoutFactory;
import org.eclipse.jface.viewers.ISelectionChangedListener;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.jface.viewers.LabelProvider;
import org.eclipse.jface.viewers.SelectionChangedEvent;
import org.eclipse.jface.viewers.StructuredSelection;
import org.eclipse.jface.viewers.TreeViewer;
import org.eclipse.swt.SWT;
import org.eclipse.swt.custom.SashForm;
import org.eclipse.swt.custom.StackLayout;
import org.eclipse.swt.events.ModifyEvent;
import org.eclipse.swt.events.ModifyListener;
import org.eclipse.swt.events.SelectionAdapter;
import org.eclipse.swt.events.SelectionEvent;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Text;
import org.eclipse.swt.widgets.Tree;
import org.eclipse.ui.forms.IManagedForm;
import org.eclipse.ui.forms.editor.FormEditor;
import org.eclipse.ui.forms.editor.FormPage;
import org.eclipse.ui.forms.events.HyperlinkAdapter;
import org.eclipse.ui.forms.events.HyperlinkEvent;
import org.eclipse.ui.forms.widgets.FormToolkit;
import org.eclipse.ui.forms.widgets.Hyperlink;
import org.eclipse.ui.forms.widgets.ScrolledForm;
import org.eclipse.ui.forms.widgets.Section;

import cn.com.myorg.bswbuilder.modules.memif.data.MemIfArxmlWriter;
import cn.com.myorg.bswbuilder.modules.memif.data.MemIfData;
import cn.com.myorg.bswbuilder.ui.editors.MemIfModuleManagerEditor;

/**
 * Master/detail page for MemIf module manager. Mirrors the reference V25.10
 * 3-column layout (verified by user 2026-04-29 on running ORIENTAIS IDE):
 *
 * <pre>
 *   form title :  MemIf - MemIf Module Manager
 *   section    :  MemIfGeneral details
 *                 "This container contains the MemIf module specific
 *                  parameters of each MemIfGeneral."
 *   ┌──────────────────────────┬──────────────┬─────────────────────────┐
 *   │ Container Hierarchical   │ ReName       │ MemIfGeneral            │
 *   │ information:             │ Element      │   MemIfDevErrorDetect:☐ │
 *   │ [filter] [⤓][⤒]          │              │   MemIfNumberOfDevices: │
 *   │                          │              │     [text  ] [D]        │
 *   │   ☑ MemIfGenerals        │              │   MemIfVersionInfoApi:☐ │
 *   │     └ ✏ MemIfGeneral     │              │                         │
 *   │                          │              │                         │
 *   │ (Right click to add or   │              │                         │
 *   │  remove items)           │              │                         │
 *   └──────────────────────────┴──────────────┴─────────────────────────┘
 * </pre>
 *
 * Field rules (also from reference):
 * <ul>
 *   <li>Booleans → SWT Checkbox (not Combo).</li>
 *   <li>NumberOfDevices integer → Text + [D] button (sets the
 *       NvM-derived default value).</li>
 *   <li>MemIfModuleVersion is hidden — it's @published-information,
 *       computed by the generator, never user-editable.</li>
 * </ul>
 */
public class MemIfGeneralFormPage extends FormPage {

    public static final String ID = "cn.com.myorg.bswbuilder.ui.editors.pages.MemIfGeneral";

    private static final String MODULE_NAME = "MemIf";

    private enum Param {
        DEV_ERROR_DETECT("MemIfDevErrorDetect", Type.BOOLEAN),
        NUMBER_OF_DEVICES("MemIfNumberOfDevices", Type.INTEGER),
        VERSION_INFO_API("MemIfVersionInfoApi", Type.BOOLEAN);
        // MemIfModuleVersion intentionally omitted — published-information,
        // not user-editable. Reference IDE doesn't show it either.

        final String shortName;
        final Type type;
        Param(String shortName, Type type) {
            this.shortName = shortName; this.type = type;
        }
        String label() { return shortName + " :"; }
    }
    private enum Type { BOOLEAN, INTEGER, STRING }

    private static final class TNode {
        final String name;
        final TNode[] children;
        TNode(String n, TNode... kids) { name = n; children = kids; }
        @Override public String toString() { return name; }
    }
    private static final TNode LEAF = new TNode("MemIfGeneral");
    private static final TNode ROOT = new TNode("MemIfGenerals", LEAF);

    private MemIfData data;
    private FormToolkit toolkit;

    private Section detailSection;
    private Composite detailHost;
    private StackLayout detailStack;
    private Composite generalForm;
    private Composite emptyForm;

    private TreeViewer master;

    private final Map<Param, Control> editors = new LinkedHashMap<>();
    private final Map<Param, String> originalValues = new LinkedHashMap<>();

    public MemIfGeneralFormPage(FormEditor editor, MemIfData data) {
        super(editor, ID, MODULE_NAME);
        this.data = data;
    }

    @Override
    protected void createFormContent(IManagedForm managedForm) {
        toolkit = managedForm.getToolkit();
        ScrolledForm form = managedForm.getForm();
        form.setText(MODULE_NAME + " - " + MODULE_NAME + " Module Manager");

        // 颜色 / 头部装饰对齐参考 V25.10 (反编 AutosarFormToolkit.decorateFormHeading):
        //   1. toolkit.decorateFormHeading(form) 加 Eclipse 标准 gradient + 底部 keyline
        //   2. 字体改 Verdana 15 (iSoft 字面常量 "Verdana" / size 15)
        //   3. 前景色 RGB(33,33,33) (iSoft 字面常量 bipush 33,33,33)
        toolkit.decorateFormHeading(form.getForm());
        org.eclipse.swt.widgets.Display display = form.getDisplay();
        org.eclipse.swt.graphics.FontData[] base = form.getFont().getFontData();
        if (base != null && base.length > 0) {
            org.eclipse.swt.graphics.FontData fd =
                    new org.eclipse.swt.graphics.FontData(base[0].toString());
            fd.setName("Verdana");
            fd.setHeight(15);
            org.eclipse.swt.graphics.Font verdana = new org.eclipse.swt.graphics.Font(display, fd);
            form.setFont(verdana);
            form.addDisposeListener(e -> verdana.dispose());
        }
        form.setForeground(new org.eclipse.swt.graphics.Color(display, 33, 33, 33));

        Composite body = form.getBody();
        GridLayoutFactory.fillDefaults().applyTo(body);

        // Outer "MemIfGeneral details" section (always shown, wraps the 3 cols)
        detailSection = toolkit.createSection(body,
                Section.TITLE_BAR | Section.DESCRIPTION | Section.EXPANDED);
        detailSection.setText("MemIfGeneral details");
        detailSection.setDescription(
                "This container contains the MemIf module specific parameters "
              + "of each MemIfGeneral.");
        GridDataFactory.fillDefaults().grab(true, true).applyTo(detailSection);

        Composite outer = toolkit.createComposite(detailSection);
        outer.setLayout(new GridLayout(3, false));
        detailSection.setClient(outer);

        // ====== COL 1: Container Hierarchical information ======
        Composite col1 = toolkit.createComposite(outer);
        GridLayoutFactory.fillDefaults().margins(0, 0).applyTo(col1);
        GridDataFactory.fillDefaults().grab(true, true).hint(280, SWT.DEFAULT).applyTo(col1);

        Section masterSection = toolkit.createSection(col1,
                Section.TITLE_BAR | Section.EXPANDED);
        masterSection.setText("Container Hierarchical information:");
        GridDataFactory.fillDefaults().grab(true, true).applyTo(masterSection);

        Composite masterBody = toolkit.createComposite(masterSection);
        GridLayoutFactory.fillDefaults().margins(2, 4).applyTo(masterBody);
        masterSection.setClient(masterBody);

        // Filter + collapse/expand row
        Composite filterRow = toolkit.createComposite(masterBody);
        GridLayoutFactory.fillDefaults().numColumns(3).spacing(4, 0).applyTo(filterRow);
        GridDataFactory.fillDefaults().grab(true, false).applyTo(filterRow);
        final Text filter = toolkit.createText(filterRow, "", SWT.BORDER | SWT.SEARCH);
        filter.setMessage("filter");
        GridDataFactory.fillDefaults().grab(true, false).applyTo(filter);
        Button collapseAll = toolkit.createButton(filterRow, "", SWT.PUSH | SWT.FLAT);
        collapseAll.setText("⊟");
        collapseAll.setToolTipText("Collapse all");
        collapseAll.addSelectionListener(new SelectionAdapter() {
            @Override public void widgetSelected(SelectionEvent e) {
                if (master != null) master.collapseAll();
            }
        });
        Button expandAll = toolkit.createButton(filterRow, "", SWT.PUSH | SWT.FLAT);
        expandAll.setText("⊞");
        expandAll.setToolTipText("Expand all");
        expandAll.addSelectionListener(new SelectionAdapter() {
            @Override public void widgetSelected(SelectionEvent e) {
                if (master != null) master.expandAll();
            }
        });

        // Tree
        master = new TreeViewer(masterBody, SWT.SINGLE | SWT.H_SCROLL | SWT.V_SCROLL);
        Tree tree = master.getTree();
        GridDataFactory.fillDefaults().grab(true, true).applyTo(tree);
        master.setContentProvider(new HierarchyContentProvider());
        master.setLabelProvider(new LabelProvider());
        master.setInput(new TNode[] { ROOT });
        master.expandAll();

        // Footer hint
        Label hint = toolkit.createLabel(masterBody,
                "(Right click to add or remove items)", SWT.NONE);
        GridDataFactory.fillDefaults().grab(true, false).align(SWT.CENTER, SWT.END).applyTo(hint);

        // ====== COL 2: action column (ReName Element link) ======
        Composite col2 = toolkit.createComposite(outer);
        GridLayoutFactory.fillDefaults().margins(8, 8).applyTo(col2);
        GridDataFactory.fillDefaults().align(SWT.BEGINNING, SWT.BEGINNING).hint(120, SWT.DEFAULT).applyTo(col2);

        Hyperlink rename = toolkit.createHyperlink(col2, "ReName Element", SWT.NONE);
        rename.addHyperlinkListener(new HyperlinkAdapter() {
            @Override public void linkActivated(HyperlinkEvent e) {
                MessageDialog.openInformation(getEditorSite().getShell(),
                        "ReName Element",
                        "Rename 在 v0.2 落地。v0.1 schema 容器名固定 (MemIfGeneral)，"
                      + "重命名既不会反向改 ARXML 也不会影响 byte-equal round-trip，"
                      + "保留这条 link 只是跟参考菜单形状对齐。");
            }
        });

        // ====== COL 3: detail panel (per-container form) ======
        Composite col3 = toolkit.createComposite(outer);
        GridLayoutFactory.fillDefaults().margins(8, 8).applyTo(col3);
        GridDataFactory.fillDefaults().grab(true, true).applyTo(col3);

        Label header = toolkit.createLabel(col3, "MemIfGeneral", SWT.NONE);
        header.setFont(org.eclipse.jface.resource.JFaceResources.getBannerFont());
        GridDataFactory.fillDefaults().grab(true, false).applyTo(header);

        detailHost = toolkit.createComposite(col3);
        detailStack = new StackLayout();
        detailHost.setLayout(detailStack);
        GridDataFactory.fillDefaults().grab(true, true).applyTo(detailHost);

        emptyForm = buildEmptyForm(detailHost);
        generalForm = buildGeneralForm(detailHost);
        detailStack.topControl = generalForm; // default = MemIfGeneral selected

        master.addSelectionChangedListener(new ISelectionChangedListener() {
            @Override
            public void selectionChanged(SelectionChangedEvent event) {
                Object first = ((IStructuredSelection) event.getSelection()).getFirstElement();
                if (!(first instanceof TNode)) return;
                TNode n = (TNode) first;
                detailStack.topControl = (n == LEAF) ? generalForm : emptyForm;
                detailHost.layout(true, true);
            }
        });
        master.setSelection(new StructuredSelection(LEAF), true);
    }

    private Composite buildEmptyForm(Composite parent) {
        Composite c = toolkit.createComposite(parent);
        GridLayoutFactory.fillDefaults().margins(20, 20).applyTo(c);
        toolkit.createLabel(c,
                "Pick MemIfGeneral in the left tree to view its parameters.",
                SWT.WRAP);
        return c;
    }

    private Composite buildGeneralForm(Composite parent) {
        Composite c = toolkit.createComposite(parent);
        GridLayout gl = new GridLayout(3, false);  // label | widget | extra (D button)
        gl.marginWidth = 8;
        gl.marginTop = 6;
        gl.verticalSpacing = 8;
        gl.horizontalSpacing = 8;
        c.setLayout(gl);

        addRow(c, Param.DEV_ERROR_DETECT,  data.getMemIfDevErrorDetect());
        addRow(c, Param.NUMBER_OF_DEVICES, data.getMemIfNumberOfDevices());
        addRow(c, Param.VERSION_INFO_API,  data.getMemIfVersionInfoApi());

        Label src = toolkit.createLabel(c,
                "source: " + data.getSourcePath(), SWT.NONE);
        GridDataFactory.fillDefaults().span(3, 1).indent(0, 14).applyTo(src);
        return c;
    }

    private void addRow(Composite parent, final Param p, String value) {
        Label l = toolkit.createLabel(parent, p.label(), SWT.NONE);
        GridDataFactory.fillDefaults().align(SWT.END, SWT.CENTER).applyTo(l);

        String display = (value == null) ? "" : value;
        originalValues.put(p, display);

        Control widget;
        boolean placeholder = false;
        switch (p.type) {
            case BOOLEAN: {
                // Reference uses a plain Checkbox here (not a Combo).
                Button check = toolkit.createButton(parent, "", SWT.CHECK);
                check.setSelection("true".equalsIgnoreCase(display));
                check.addSelectionListener(new SelectionAdapter() {
                    @Override public void widgetSelected(SelectionEvent e) { recheckDirty(); }
                });
                widget = check;
                break;
            }
            default: {
                Text text = toolkit.createText(parent, display, SWT.BORDER);
                GridDataFactory.fillDefaults().hint(100, SWT.DEFAULT).applyTo(text);
                text.addModifyListener(new ModifyListener() {
                    @Override public void modifyText(ModifyEvent e) { recheckDirty(); }
                });
                widget = text;
                break;
            }
        }
        editors.put(p, widget);

        // 3rd-column placeholder. Reference V25.10 has a [D] button next
        // to NumberOfDevices but the click semantic isn't clear from the
        // screenshot alone (could be "Default" / "Decimal" / "Derived" / …).
        // Per "don't blindly copy, understand first" rule (memory:
        // feedback_reference_first), shipping the visual without the
        // correct behavior is worse than not shipping it. The button
        // returns once we javap the actual click handler in v0.2.
        Label filler = toolkit.createLabel(parent, "", SWT.NONE);
        GridDataFactory.fillDefaults().hint(28, SWT.DEFAULT).applyTo(filler);
        if (placeholder) widget.setEnabled(false);
    }

    private void recheckDirty() {
        boolean dirty = false;
        for (Map.Entry<Param, Control> e : editors.entrySet()) {
            String now = widgetValue(e.getValue());
            String orig = originalValues.getOrDefault(e.getKey(), "");
            if (!now.equals(orig)) { dirty = true; break; }
        }
        ((MemIfModuleManagerEditor) getEditor()).setDirty(dirty);
    }

    private static String widgetValue(Control w) {
        if (w instanceof Button) {
            return ((Button) w).getSelection() ? "true" : "false";
        }
        if (w instanceof Text) return ((Text) w).getText();
        return "";
    }

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
    }

    private void applyOne(Param p, String value) {
        Control w = editors.get(p);
        if (w == null || w.isDisposed()) return;
        String s = value == null ? "" : value;
        if (w instanceof Button) ((Button) w).setSelection("true".equalsIgnoreCase(s));
        else if (w instanceof Text) ((Text) w).setText(s);
        originalValues.put(p, s);
    }

    private static final class HierarchyContentProvider implements ITreeContentProvider {
        @Override public Object[] getElements(Object input) {
            return (input instanceof Object[]) ? (Object[]) input : new Object[0];
        }
        @Override public Object[] getChildren(Object e) {
            return (e instanceof TNode) ? ((TNode) e).children : new Object[0];
        }
        @Override public Object getParent(Object e) { return null; }
        @Override public boolean hasChildren(Object e) {
            return e instanceof TNode && ((TNode) e).children.length > 0;
        }
    }
}

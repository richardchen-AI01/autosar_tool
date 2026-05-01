package cn.com.myorg.bswbuilder.ui.editor.pages;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.eclipse.jface.layout.GridDataFactory;
import org.eclipse.jface.layout.GridLayoutFactory;
import org.eclipse.jface.viewers.ISelectionChangedListener;
import org.eclipse.jface.viewers.IStructuredContentProvider;
import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.jface.viewers.LabelProvider;
import org.eclipse.jface.viewers.SelectionChangedEvent;
import org.eclipse.jface.viewers.StructuredSelection;
import org.eclipse.jface.viewers.TreeViewer;
import org.eclipse.jface.viewers.Viewer;
import org.eclipse.swt.SWT;
import org.eclipse.swt.custom.SashForm;
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
import org.eclipse.swt.widgets.ToolBar;
import org.eclipse.swt.widgets.ToolItem;
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
 * Generic master-detail form page — multi-instance container UI.
 *
 * <p>Layout (跟参考 V25.10 cn.com.isoft.bswbuilder.ui.editor.pages.BswMasterDetailFormPage 一致):
 * <pre>
 *   [Add] [Remove] [Duplicate]
 *   ─────────────────────────────────────────────
 *   ┌─────────────────┬─────────────────────────┐
 *   │ NvMBlock_Pri_0  │ NvMBlockJobPriority: 1  │
 *   │ NvMBlock_Pri_1  │ NvMBlockUseCrc:    [✓]  │
 *   │ NvMBlock_Pri_2  │ NvMNvBlockLength:  2    │
 *   │ ... (24)        │ ...                     │
 *   └─────────────────┴─────────────────────────┘
 *      master tree           detail form (per-instance)
 * </pre>
 *
 * <p>Reference V25.10 splits this into 3 classes (NewAutosarMasterDetailBlock +
 * MasterFormSection + DetailFormSection); we collapse into one class for v0.2.
 * Behavior matches: schema-driven widget rendering on the right, EMF instance
 * selection on the left.
 *
 * <p>v0.2 first cut scope:
 * <ul>
 *   <li>✓ Master tree shows all GContainer instances</li>
 *   <li>✓ Detail form re-renders on selection change (uses same widget logic
 *       as {@link GenericGeneralFormPage})</li>
 *   <li>✗ Add / Remove / Duplicate buttons (rendered disabled — E5-4 wires)</li>
 *   <li>✗ Cross-module REF chooser dialog (留 v0.3)</li>
 *   <li>✗ Sub-container nested forms (e.g. NvMTargetBlockReference) — first
 *       cut shows top-level params only, sub-containers come in E5-3 v2</li>
 * </ul>
 */
public class GenericMasterDetailFormPage extends FormPage {

    private final GModuleConfiguration module;
    private final GContainerDef containerDef;

    /** All instance containers matching containerDef. Refreshed when add/remove. */
    private List<GContainer> instances = new ArrayList<>();

    private TreeViewer masterViewer;
    private Composite detailParent;
    private FormToolkit toolkit;

    /** Currently selected instance — drives detail form. */
    private GContainer selectedInstance;

    /** Per-selected-instance widget map (rebuilt on each selection change). */
    private final Map<GConfigParameter, Control> detailWidgets = new LinkedHashMap<>();

    public GenericMasterDetailFormPage(FormEditor editor,
                                       GModuleConfiguration module,
                                       GContainerDef containerDef) {
        super(editor, containerDef.gGetShortName() + "MdPage", containerDef.gGetShortName());
        this.module = module;
        this.containerDef = containerDef;
    }

    @Override
    protected void createFormContent(IManagedForm managedForm) {
        toolkit = managedForm.getToolkit();
        ScrolledForm form = managedForm.getForm();
        String moduleName = module.gGetShortName();
        String containerName = containerDef.gGetShortName();
        form.setText(moduleName + " — " + containerName);

        Composite body = form.getBody();
        GridLayoutFactory.fillDefaults().margins(5, 5).applyTo(body);

        // Top toolbar (Add / Remove / Duplicate). Disabled for v0.2 — E5-4 wires.
        createToolbar(body);

        // SashForm splits master (left ~30%) + detail (right ~70%).
        SashForm sash = new SashForm(body, SWT.HORIZONTAL);
        GridDataFactory.fillDefaults().grab(true, true).applyTo(sash);
        toolkit.adapt(sash);

        createMaster(sash);
        createDetail(sash);
        sash.setWeights(new int[] { 30, 70 });

        // Initial selection — first instance, if any.
        instances = EcuUtils.getContainersByDef(module, containerDef);
        masterViewer.setInput(instances);
        if (!instances.isEmpty()) {
            masterViewer.setSelection(new StructuredSelection(instances.get(0)), true);
        } else {
            renderEmptyDetail("(no '" + containerName + "' instances configured)");
        }
    }

    // ============================================================ master side

    private void createToolbar(Composite parent) {
        ToolBar tb = new ToolBar(parent, SWT.FLAT | SWT.HORIZONTAL);
        ToolItem add = new ToolItem(tb, SWT.PUSH);
        add.setText("Add");
        add.setEnabled(false);   // E5-4 wires
        ToolItem rm = new ToolItem(tb, SWT.PUSH);
        rm.setText("Remove");
        rm.setEnabled(false);    // E5-4 wires
        ToolItem dup = new ToolItem(tb, SWT.PUSH);
        dup.setText("Duplicate");
        dup.setEnabled(false);   // E5-4 wires
        toolkit.adapt(tb);
    }

    private void createMaster(Composite parent) {
        Composite master = toolkit.createComposite(parent);
        GridLayoutFactory.fillDefaults().applyTo(master);

        Section section = toolkit.createSection(master, Section.TITLE_BAR);
        section.setText(containerDef.gGetShortName() + " instances");
        GridDataFactory.fillDefaults().grab(true, true).applyTo(section);

        Composite client = toolkit.createComposite(section);
        GridLayoutFactory.fillDefaults().applyTo(client);
        section.setClient(client);

        masterViewer = new TreeViewer(client, SWT.BORDER | SWT.SINGLE | SWT.V_SCROLL);
        GridDataFactory.fillDefaults().grab(true, true).applyTo(masterViewer.getTree());

        masterViewer.setContentProvider(new MasterContentProvider());
        masterViewer.setLabelProvider(new LabelProvider() {
            @Override
            public String getText(Object element) {
                if (element instanceof GContainer) {
                    String n = ((GContainer) element).gGetShortName();
                    return n == null || n.isEmpty() ? "<unnamed>" : n;
                }
                return String.valueOf(element);
            }
        });

        masterViewer.addSelectionChangedListener(new ISelectionChangedListener() {
            @Override public void selectionChanged(SelectionChangedEvent event) {
                Object first = event.getStructuredSelection().getFirstElement();
                if (first instanceof GContainer) {
                    onInstanceSelected((GContainer) first);
                }
            }
        });
    }

    /** TreeViewer content provider — flat list of GContainer instances. */
    private static final class MasterContentProvider
            implements IStructuredContentProvider, ITreeContentProvider {
        @SuppressWarnings("unchecked")
        @Override public Object[] getElements(Object input) {
            if (input instanceof List) return ((List<Object>) input).toArray();
            return new Object[0];
        }
        @Override public Object[] getChildren(Object element) { return new Object[0]; }
        @Override public Object getParent(Object element) { return null; }
        @Override public boolean hasChildren(Object element) { return false; }
        @Override public void inputChanged(Viewer viewer, Object oldIn, Object newIn) {}
        @Override public void dispose() {}
    }

    // ============================================================ detail side

    private void createDetail(Composite parent) {
        detailParent = toolkit.createComposite(parent);
        GridLayoutFactory.fillDefaults().applyTo(detailParent);
    }

    /** Re-render detail form for the selected instance. */
    private void onInstanceSelected(GContainer instance) {
        this.selectedInstance = instance;
        for (Control c : detailParent.getChildren()) c.dispose();
        detailWidgets.clear();

        Section section = toolkit.createSection(detailParent,
                Section.TITLE_BAR | Section.DESCRIPTION);
        section.setText(instance.gGetShortName());
        section.setDescription("Edit parameters of this " + containerDef.gGetShortName() + " instance.");
        GridDataFactory.fillDefaults().grab(true, true).applyTo(section);

        Composite client = toolkit.createComposite(section);
        GridLayout grid = new GridLayout(3, false);
        grid.marginTop = 6;
        grid.horizontalSpacing = 10;
        grid.verticalSpacing = 6;
        client.setLayout(grid);
        section.setClient(client);

        if (containerDef instanceof GParamConfContainerDef) {
            GParamConfContainerDef pdef = (GParamConfContainerDef) containerDef;
            for (GConfigParameter param : pdef.gGetParameters()) {
                addRow(client, param, instance);
            }
            // Sub-containers (e.g. NvMTargetBlockReference inside NvMBlockDescriptor)
            // 待 E5-3 v2 nest 渲染 — 先只展平第一层。
        }

        detailParent.layout(true, true);
    }

    private void renderEmptyDetail(String message) {
        for (Control c : detailParent.getChildren()) c.dispose();
        Label l = toolkit.createLabel(detailParent, message, SWT.WRAP);
        GridDataFactory.fillDefaults().align(SWT.CENTER, SWT.CENTER).applyTo(l);
        detailParent.layout(true, true);
    }

    private void addRow(Composite parent, GConfigParameter param, GContainer instance) {
        Label label = toolkit.createLabel(parent, param.gGetShortName() + ":", SWT.NONE);
        GridDataFactory.fillDefaults().align(SWT.END, SWT.CENTER).applyTo(label);

        Control widget;
        String currentVal = readParamValue(instance, param);

        if (param instanceof GBooleanParamDef) {
            Button check = toolkit.createButton(parent, "", SWT.CHECK);
            check.setSelection("true".equalsIgnoreCase(currentVal));
            check.addSelectionListener(new SelectionAdapter() {
                @Override public void widgetSelected(SelectionEvent e) { /* dirty: E5-4 wires */ }
            });
            widget = check;
        } else if (param instanceof GIntegerParamDef) {
            Spinner spin = new Spinner(parent, SWT.BORDER);
            spin.setMinimum(Integer.MIN_VALUE);
            spin.setMaximum(Integer.MAX_VALUE);
            try { if (currentVal != null) spin.setSelection(Integer.parseInt(currentVal.trim())); }
            catch (NumberFormatException nfe) { /* leave 0 */ }
            spin.addModifyListener(new ModifyListener() {
                @Override public void modifyText(ModifyEvent e) { /* dirty */ }
            });
            GridDataFactory.fillDefaults().hint(120, SWT.DEFAULT).applyTo(spin);
            widget = spin;
        } else if (param instanceof GEnumerationParamDef) {
            Combo combo = new Combo(parent, SWT.READ_ONLY | SWT.BORDER);
            for (GEnumerationLiteralDef lit : ((GEnumerationParamDef) param).gGetLiterals()) {
                combo.add(lit.gGetShortName());
            }
            int idx = currentVal == null ? -1 : combo.indexOf(currentVal);
            if (idx >= 0) combo.select(idx);
            combo.addSelectionListener(new SelectionAdapter() {
                @Override public void widgetSelected(SelectionEvent e) { /* dirty */ }
            });
            GridDataFactory.fillDefaults().hint(180, SWT.DEFAULT).applyTo(combo);
            widget = combo;
        } else if (param instanceof GFloatParamDef || param instanceof GStringParamDef) {
            Text text = toolkit.createText(parent, currentVal == null ? "" : currentVal, SWT.BORDER);
            GridDataFactory.fillDefaults().hint(180, SWT.DEFAULT).applyTo(text);
            text.addModifyListener(new ModifyListener() {
                @Override public void modifyText(ModifyEvent e) { /* dirty */ }
            });
            widget = text;
        } else {
            Label note = toolkit.createLabel(parent, "(unsupported type)", SWT.NONE);
            widget = note;
        }

        toolkit.createLabel(parent, "", SWT.NONE);   // 3rd col placeholder (D button etc.)
        detailWidgets.put(param, widget);
    }

    /** Mirror {@link GenericGeneralFormPage#readParamValue} — typed instance read. */
    private static String readParamValue(GContainer container, GConfigParameter paramDef) {
        if (container == null) return null;
        GParameterValue pv = EcuUtils.getParameterValue(container, paramDef);
        if (pv == null) return null;
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

    // ============================================================ accessors

    public GContainerDef getContainerDef() { return containerDef; }
    public GContainer getSelectedInstance()  { return selectedInstance; }
}

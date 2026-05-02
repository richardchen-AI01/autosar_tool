package cn.com.myorg.bswbuilder.ui.editor.pages;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.jface.action.Action;
import org.eclipse.jface.action.IMenuListener;
import org.eclipse.jface.action.IMenuManager;
import org.eclipse.jface.action.MenuManager;
import org.eclipse.jface.dialogs.InputDialog;
import org.eclipse.jface.dialogs.MessageDialog;
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
import org.eclipse.sphinx.emf.editors.forms.BasicTransactionalFormEditor;
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
import org.eclipse.swt.widgets.Menu;
import org.eclipse.swt.widgets.Spinner;
import org.eclipse.swt.widgets.Text;
import org.eclipse.swt.widgets.Tree;
import org.eclipse.ui.forms.IManagedForm;
import org.eclipse.ui.forms.editor.FormEditor;
import org.eclipse.ui.forms.editor.FormPage;
import org.eclipse.ui.forms.widgets.FormToolkit;
import org.eclipse.ui.forms.widgets.ScrolledForm;
import org.eclipse.ui.forms.widgets.Section;

import autosar40.ecucdescription.EcucNumericalParamValue;
import autosar40.ecucdescription.EcucTextualParamValue;
import cn.com.myorg.bswbuilder.ui.Activator;
import cn.com.myorg.bswbuilder.ui.editor.utils.EcuUtils;
import cn.com.myorg.bswbuilder.ui.editor.utils.EcucWriteActions;
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
 *   ┌─────────────────┬─────────────────────────┐
 *   │ NvMBlock_Pri_0  │ NvMBlockJobPriority: 1  │
 *   │ NvMBlock_Pri_1  │ NvMBlockUseCrc:    [✓]  │
 *   │ NvMBlock_Pri_2  │ NvMNvBlockLength:  2    │
 *   │ ... (24)        │ ...                     │
 *   └─────────────────┴─────────────────────────┘
 *      master tree           detail form (per-instance)
 *      (右键菜单: New / Delete / Rename / Duplicate)
 * </pre>
 *
 * <p>E5-6 S5 修订:
 * <ul>
 *   <li>删 toolbar Add/Remove/Duplicate 占位 — 参考 V25.10 用右键菜单 (MasterFormSection
 *       line 444 MenuManager("#PopupMenu"))</li>
 *   <li>右键菜单加 Action: New &lt;ContainerName&gt;, Delete, Rename..., Duplicate</li>
 *   <li>所有写入经 EcucWriteActions → EMF RecordingCommand → Sphinx CommandStack →
 *       自动 dirty + 撑 undo + Save 时自动写盘 (BTFE.doSave 框架接管)</li>
 *   <li>detail-side widget listeners 接 EcucWriteActions, 跟 GenericGeneralFormPage 同款</li>
 * </ul>
 */
public class GenericMasterDetailFormPage extends FormPage {

    private final GModuleConfiguration module;
    private final GContainerDef containerDef;

    /** All instance containers matching containerDef. Refreshed on Add/Delete. */
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
        form.setText(moduleName + " — " + containerName + " (右键 New / Delete / Rename)");

        Composite body = form.getBody();
        GridLayoutFactory.fillDefaults().margins(5, 5).applyTo(body);

        SashForm sash = new SashForm(body, SWT.HORIZONTAL);
        GridDataFactory.fillDefaults().grab(true, true).applyTo(sash);
        toolkit.adapt(sash);

        createMaster(sash);
        createDetail(sash);
        sash.setWeights(new int[] { 30, 70 });

        refreshInstancesAndSelectFirst();
    }

    /** 重新从 module 抽 containerDef 对应的实例列表, masterViewer.setInput, 默认选第一个。 */
    private void refreshInstancesAndSelectFirst() {
        instances = EcuUtils.getContainersByDef(module, containerDef);
        if (masterViewer != null && !masterViewer.getTree().isDisposed()) {
            masterViewer.setInput(instances);
        }
        if (!instances.isEmpty()) {
            masterViewer.setSelection(new StructuredSelection(instances.get(0)), true);
        } else {
            renderEmptyDetail("(no '" + containerDef.gGetShortName() + "' instances configured — 右键 → New)");
        }
    }

    // ============================================================ master side

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
            @Override public String getText(Object element) {
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

        // 右键菜单 (跟参考 MasterFormSection line 444 同款 MenuManager("#PopupMenu") pattern)
        installContextMenu();
    }

    /**
     * 装右键菜单到 master tree 控件。menuAboutToShow 动态 fill action,
     * action 走 EcucWriteActions → CommandStack → Sphinx 自动 dirty。
     */
    private void installContextMenu() {
        MenuManager menuManager = new MenuManager("#PopupMenu");
        menuManager.setRemoveAllWhenShown(true);
        menuManager.addMenuListener(new IMenuListener() {
            @Override public void menuAboutToShow(IMenuManager mm) {
                fillContextMenu(mm);
            }
        });
        Tree tree = masterViewer.getTree();
        Menu menu = menuManager.createContextMenu(tree);
        tree.setMenu(menu);
    }

    /** 动态填充右键菜单 — selection 决定哪些 action 启用。 */
    private void fillContextMenu(IMenuManager mm) {
        final GContainer selected = currentSelection();

        // New <ContainerName> — 总是启用
        mm.add(new Action("New " + containerDef.gGetShortName()) {
            @Override public void run() { runNew(); }
        });

        if (selected != null) {
            mm.add(new Action("Delete") {
                @Override public void run() { runDelete(selected); }
            });
            mm.add(new Action("Rename...") {
                @Override public void run() { runRename(selected); }
            });
            mm.add(new Action("Duplicate") {
                @Override public void run() { runDuplicate(selected); }
            });
        }
    }

    private GContainer currentSelection() {
        if (masterViewer == null) return null;
        Object first = masterViewer.getStructuredSelection().getFirstElement();
        return first instanceof GContainer ? (GContainer) first : null;
    }

    // ============================================================ Action runners

    private void runNew() {
        String defaultName = uniqueDefaultName(containerDef.gGetShortName());
        InputDialog dlg = new InputDialog(masterViewer.getControl().getShell(),
                "New " + containerDef.gGetShortName(),
                "Enter shortName for the new " + containerDef.gGetShortName() + ":",
                defaultName, null);
        if (dlg.open() != InputDialog.OK) return;
        String name = dlg.getValue();
        if (name == null || name.isEmpty()) return;

        GContainer created = EcucWriteActions.addContainer(editor(), module, containerDef, name);
        if (created == null) {
            warn("Add failed", "Could not create new " + containerDef.gGetShortName()
                    + " — see .metadata/.log for details.");
            return;
        }
        refreshInstancesAndSelect(created);
    }

    private void runDelete(final GContainer victim) {
        if (!MessageDialog.openConfirm(masterViewer.getControl().getShell(),
                "Delete", "Delete '" + victim.gGetShortName() + "'?")) return;
        if (!EcucWriteActions.removeContainer(editor(), victim)) {
            warn("Delete failed", "Could not delete '" + victim.gGetShortName() + "'.");
            return;
        }
        refreshInstancesAndSelectFirst();
    }

    private void runRename(final GContainer target) {
        InputDialog dlg = new InputDialog(masterViewer.getControl().getShell(),
                "Rename " + target.gGetShortName(),
                "Enter new shortName:",
                target.gGetShortName(), null);
        if (dlg.open() != InputDialog.OK) return;
        String name = dlg.getValue();
        if (name == null || name.isEmpty() || name.equals(target.gGetShortName())) return;
        if (!EcucWriteActions.renameContainer(editor(), target, name)) {
            warn("Rename failed", "Could not rename '" + target.gGetShortName() + "'.");
            return;
        }
        refreshInstancesAndSelect(target);
    }

    private void runDuplicate(final GContainer src) {
        GContainer copy = EcucWriteActions.duplicateContainer(editor(), src);
        if (copy == null) {
            warn("Duplicate failed", "Could not duplicate '" + src.gGetShortName() + "'.");
            return;
        }
        refreshInstancesAndSelect(copy);
    }

    private void refreshInstancesAndSelect(GContainer toSelect) {
        instances = EcuUtils.getContainersByDef(module, containerDef);
        masterViewer.setInput(instances);
        if (toSelect != null && instances.contains(toSelect)) {
            masterViewer.setSelection(new StructuredSelection(toSelect), true);
        } else if (!instances.isEmpty()) {
            masterViewer.setSelection(new StructuredSelection(instances.get(0)), true);
        } else {
            renderEmptyDetail("(no instances)");
        }
    }

    private String uniqueDefaultName(String base) {
        String prefix = base + "_";
        int i = instances.size();
        while (true) {
            String candidate = prefix + i;
            boolean clash = false;
            for (GContainer c : instances) {
                if (candidate.equals(c.gGetShortName())) { clash = true; break; }
            }
            if (!clash) return candidate;
            i++;
        }
    }

    private void warn(String title, String msg) {
        MessageDialog.openWarning(masterViewer.getControl().getShell(), title, msg);
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
        }

        detailParent.layout(true, true);
    }

    private void renderEmptyDetail(String message) {
        for (Control c : detailParent.getChildren()) c.dispose();
        Label l = toolkit.createLabel(detailParent, message, SWT.WRAP);
        GridDataFactory.fillDefaults().align(SWT.CENTER, SWT.CENTER).applyTo(l);
        detailParent.layout(true, true);
    }

    /** detail-side widget listeners 走 EcucWriteActions, 同 GenericGeneralFormPage 模式。 */
    private void addRow(Composite parent, final GConfigParameter param, final GContainer instance) {
        Label label = toolkit.createLabel(parent, param.gGetShortName() + ":", SWT.NONE);
        GridDataFactory.fillDefaults().align(SWT.END, SWT.CENTER).applyTo(label);

        Control widget;
        String currentVal = readParamValue(instance, param);

        if (param instanceof GBooleanParamDef) {
            final Button check = toolkit.createButton(parent, "", SWT.CHECK);
            check.setSelection("true".equalsIgnoreCase(currentVal));
            check.addSelectionListener(new SelectionAdapter() {
                @Override public void widgetSelected(SelectionEvent e) {
                    writeNumericalParam(instance, param, check.getSelection() ? "true" : "false");
                }
            });
            widget = check;
        } else if (param instanceof GIntegerParamDef) {
            final Spinner spin = new Spinner(parent, SWT.BORDER);
            spin.setMinimum(Integer.MIN_VALUE);
            spin.setMaximum(Integer.MAX_VALUE);
            try { if (currentVal != null) spin.setSelection(Integer.parseInt(currentVal.trim())); }
            catch (NumberFormatException nfe) { /* leave 0 */ }
            spin.addModifyListener(new ModifyListener() {
                @Override public void modifyText(ModifyEvent e) {
                    writeNumericalParam(instance, param, String.valueOf(spin.getSelection()));
                }
            });
            GridDataFactory.fillDefaults().hint(120, SWT.DEFAULT).applyTo(spin);
            widget = spin;
        } else if (param instanceof GEnumerationParamDef) {
            final Combo combo = new Combo(parent, SWT.READ_ONLY | SWT.BORDER);
            for (GEnumerationLiteralDef lit : ((GEnumerationParamDef) param).gGetLiterals()) {
                combo.add(lit.gGetShortName());
            }
            int idx = currentVal == null ? -1 : combo.indexOf(currentVal);
            if (idx >= 0) combo.select(idx);
            combo.addSelectionListener(new SelectionAdapter() {
                @Override public void widgetSelected(SelectionEvent e) {
                    writeTextualParam(instance, param, combo.getText());
                }
            });
            GridDataFactory.fillDefaults().hint(180, SWT.DEFAULT).applyTo(combo);
            widget = combo;
        } else if (param instanceof GFloatParamDef) {
            final Text text = toolkit.createText(parent, currentVal == null ? "" : currentVal, SWT.BORDER);
            GridDataFactory.fillDefaults().hint(180, SWT.DEFAULT).applyTo(text);
            text.addModifyListener(new ModifyListener() {
                @Override public void modifyText(ModifyEvent e) {
                    writeNumericalParam(instance, param, text.getText());
                }
            });
            widget = text;
        } else if (param instanceof GStringParamDef) {
            final Text text = toolkit.createText(parent, currentVal == null ? "" : currentVal, SWT.BORDER);
            GridDataFactory.fillDefaults().hint(180, SWT.DEFAULT).applyTo(text);
            text.addModifyListener(new ModifyListener() {
                @Override public void modifyText(ModifyEvent e) {
                    writeTextualParam(instance, param, text.getText());
                }
            });
            widget = text;
        } else {
            Label note = toolkit.createLabel(parent, "(unsupported type)", SWT.NONE);
            widget = note;
        }

        toolkit.createLabel(parent, "", SWT.NONE);   // 3rd col placeholder
        detailWidgets.put(param, widget);
    }

    private void writeNumericalParam(GContainer instance, GConfigParameter param, String newText) {
        GParameterValue pv = EcuUtils.getParameterValue(instance, param);
        if (pv instanceof EcucNumericalParamValue) {
            EcucWriteActions.setNumericalText(editor(), (EcucNumericalParamValue) pv, newText);
        } else if (pv == null) {
            log("writeNumericalParam: pv missing for " + param.gGetShortName() + " on "
                    + instance.gGetShortName() + " — skip (S5.5 will create pv)");
        }
    }

    private void writeTextualParam(GContainer instance, GConfigParameter param, String newValue) {
        GParameterValue pv = EcuUtils.getParameterValue(instance, param);
        if (pv instanceof EcucTextualParamValue) {
            EcucWriteActions.setTextualValue(editor(), (EcucTextualParamValue) pv, newValue);
        } else if (pv == null) {
            log("writeTextualParam: pv missing for " + param.gGetShortName() + " on "
                    + instance.gGetShortName() + " — skip (S5.5 will create pv)");
        }
    }

    /** Mirror {@link GenericGeneralFormPage#readParamValue} — typed instance read. */
    private static String readParamValue(GContainer container, GConfigParameter paramDef) {
        if (container == null) return null;
        GParameterValue pv = EcuUtils.getParameterValue(container, paramDef);
        if (pv == null) return null;
        if (pv instanceof EcucNumericalParamValue) {
            EcucNumericalParamValue n = (EcucNumericalParamValue) pv;
            return n.getValue() == null ? null : n.getValue().getMixedText();
        }
        if (pv instanceof EcucTextualParamValue) {
            return ((EcucTextualParamValue) pv).getValue();
        }
        return null;
    }

    private BasicTransactionalFormEditor editor() {
        FormEditor e = getEditor();
        return (e instanceof BasicTransactionalFormEditor) ? (BasicTransactionalFormEditor) e : null;
    }

    private static void log(String msg) {
        try {
            Activator a = Activator.getDefault();
            if (a != null) {
                a.getLog().log(new Status(IStatus.INFO, Activator.PLUGIN_ID,
                        "[GenericMasterDetailFormPage] " + msg));
            }
        } catch (Throwable ignored) { /* fallback silent */ }
    }

    // ============================================================ accessors

    public GContainerDef getContainerDef() { return containerDef; }
    public GContainer getSelectedInstance()  { return selectedInstance; }
}

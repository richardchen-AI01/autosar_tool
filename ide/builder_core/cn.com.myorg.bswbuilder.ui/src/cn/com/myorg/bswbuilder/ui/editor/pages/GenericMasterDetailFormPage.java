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
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Combo;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Link;
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
 * <p>跟参考 V25.10 cn.com.isoft.bswbuilder.ui.editor.section.NewAutosarMasterDetailBlock
 * 的 createMasterPart (line 102-145) 同款 3 栏布局:
 * <pre>
 *   ┌─ master tree ──┬─ action panel ─┬─── detail form ───┐
 *   │ NvMBlock_Pri_0 │ &lt;a&gt;New NvMInit  │ NvMBlockJobPri: 1 │
 *   │  ▾NvMInit...   │   BlockCallback&lt;/a&gt;  NvMBlockUseCrc:[v]│
 *   │  ▾NvMSingle..  │ &lt;a&gt;New NvMSingle│ NvMNvBlockLength:2│
 *   │ NvMBlock_Pri_1 │   BlockCallback&lt;/a&gt;  ...               │
 *   │ ...            │ &lt;a&gt;Del Element&lt;/a&gt;│                   │
 *   │                │ &lt;a&gt;Copy Element&lt;/a&gt;│                  │
 *   │                │ &lt;a&gt;ReName Element&lt;/a&gt;                  │
 *   └────────────────┴─────────────────┴───────────────────┘
 * </pre>
 * 跟参考一致:
 * <ul>
 *   <li>SashForm horizontal weights={10,15} 切 master+action 部分 vs detail 部分</li>
 *   <li>master+action 部分内部 GridLayout numColumns=2 (master 占左, action 占右)</li>
 *   <li>action panel 用 SWT {@link Link} "&lt;a&gt;label&lt;/a&gt;" 链接,
 *       跟参考 NewAutosarMasterDetailBlockActionManager.addActionLink (line 144-148) 同款</li>
 *   <li>tree 可展开看 sub-containers (NvMBlockDescriptor → NvMInitBlockCallback /
 *       NvMSingleBlockCallback) — getChildren = {@link GContainer#gGetSubContainers}</li>
 *   <li>右键菜单 + action panel 内容一致 (参考也保留 right-click)</li>
 *   <li>底部提示 "(Right click to add or remove items)" — 参考 line 142 同 label</li>
 *   <li>label "Del Element" / "Copy Element" / "ReName Element" / "New &lt;subDef&gt;"
 *       字面对齐参考</li>
 * </ul>
 */
public class GenericMasterDetailFormPage extends FormPage {

    private final GModuleConfiguration module;
    private final GContainerDef containerDef;

    /** Top-level instance containers matching containerDef. */
    private List<GContainer> instances = new ArrayList<>();

    private TreeViewer masterViewer;
    private Composite actionPanel;
    private Composite detailParent;
    private FormToolkit toolkit;

    /** Currently selected instance — drives detail form + action panel. */
    private GContainer selectedInstance;

    /** Per-selected-instance widget map (rebuilt on each selection change). */
    private final Map<GConfigParameter, Control> detailWidgets = new LinkedHashMap<>();

    /** Currently rendered action links — disposed + rebuilt on selection change. */
    private final List<Link> actionLinks = new ArrayList<>();

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

        // SashForm 跟参考 NewAutosarAbstractMasterDetailsBlock.createContent line 51-52 同款
        // weights {10, 15} (master+action 部分 : detail 部分).
        SashForm sash = new SashForm(body, SWT.HORIZONTAL);
        GridDataFactory.fillDefaults().grab(true, true).applyTo(sash);
        toolkit.adapt(sash);

        // 左半 master + action panel (内部 GridLayout 2 col, 跟参考 createMasterPart line 109).
        Composite leftSide = toolkit.createComposite(sash);
        GridLayout leftGrid = new GridLayout(2, false);
        leftGrid.marginWidth = 0;
        leftGrid.marginHeight = 0;
        leftGrid.horizontalSpacing = 5;
        leftSide.setLayout(leftGrid);

        createMaster(leftSide);
        createActionPanel(leftSide);

        // Hint label, 跟参考 createMasterPart line 142 同款.
        Label hint = toolkit.createLabel(leftSide, "(Right click to add or remove items)");
        GridData hintGd = new GridData(SWT.FILL, SWT.BEGINNING, true, false, 2, 1);
        hint.setLayoutData(hintGd);

        createDetail(sash);
        sash.setWeights(new int[] { 10, 15 });

        refreshInstancesAndSelectFirst();
    }

    /** 重新拉 module 对应 containerDef 的实例列表, viewer.setInput, 默认选第一个。 */
    private void refreshInstancesAndSelectFirst() {
        instances = EcuUtils.getContainersByDef(module, containerDef);
        if (masterViewer != null && !masterViewer.getTree().isDisposed()) {
            masterViewer.setInput(instances);
        }
        if (!instances.isEmpty()) {
            masterViewer.setSelection(new StructuredSelection(instances.get(0)), true);
        } else {
            renderEmptyDetail("(no '" + containerDef.gGetShortName() + "' instances configured — 右键 → New)");
            updateActionPanel(null);
        }
    }

    // ============================================================ master side

    private void createMaster(Composite parent) {
        Composite master = toolkit.createComposite(parent);
        GridLayoutFactory.fillDefaults().applyTo(master);
        // master 占左侧主要空间.
        GridDataFactory.fillDefaults().grab(true, true).applyTo(master);

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
                } else {
                    updateActionPanel(null);
                }
            }
        });

        installContextMenu();
    }

    /**
     * Tree content provider — 顶层是 instances 列表, 每个 GContainer 的 children 是
     * gGetSubContainers (跟参考 NewAutosarMasterDetailBlock master tree 同款,
     * 让 NvMBlockDescriptor 可以展开看 NvMInitBlockCallback / NvMSingleBlockCallback)。
     */
    private static final class MasterContentProvider
            implements IStructuredContentProvider, ITreeContentProvider {
        @SuppressWarnings("unchecked")
        @Override public Object[] getElements(Object input) {
            if (input instanceof List) return ((List<Object>) input).toArray();
            return new Object[0];
        }
        @Override public Object[] getChildren(Object element) {
            if (element instanceof GContainer) {
                List<GContainer> subs = ((GContainer) element).gGetSubContainers();
                return subs == null ? new Object[0] : subs.toArray();
            }
            return new Object[0];
        }
        @Override public Object getParent(Object element) {
            if (element instanceof GContainer) {
                org.eclipse.emf.ecore.EObject p = ((org.eclipse.emf.ecore.EObject) element).eContainer();
                return p instanceof GContainer ? p : null;
            }
            return null;
        }
        @Override public boolean hasChildren(Object element) {
            if (element instanceof GContainer) {
                List<GContainer> subs = ((GContainer) element).gGetSubContainers();
                return subs != null && !subs.isEmpty();
            }
            return false;
        }
        @Override public void inputChanged(Viewer viewer, Object oldIn, Object newIn) {}
        @Override public void dispose() {}
    }

    // ============================================================ action panel (中间一栏)

    /**
     * 创建中间 action panel 容器, 内容由 {@link #updateActionPanel} 在 selectionChanged
     * 时动态填充 (跟参考 NewAutosarMasterDetailBlockActionManager 同款生命周期)。
     */
    private void createActionPanel(Composite parent) {
        actionPanel = toolkit.createComposite(parent);
        GridLayout gl = new GridLayout(1, true);
        gl.marginWidth = 8;
        gl.marginHeight = 8;
        gl.verticalSpacing = 4;
        actionPanel.setLayout(gl);
        // 固定窗口宽度让 action panel 不被压缩.
        GridData gd = new GridData(SWT.FILL, SWT.FILL, false, true);
        gd.widthHint = 200;
        actionPanel.setLayoutData(gd);
    }

    /**
     * 根据当前选中的 GContainer 重建 action panel 链接列表 — 跟右键菜单 (fillContextMenu)
     * 的 action 集合一致, 仅渲染形态不同 (Link "&lt;a&gt;label&lt;/a&gt;" vs MenuItem)。
     * 跟参考 NewAutosarMasterDetailBlockActionManager.fillComposite (line 118) +
     * addActionLink (line 144) 同 pattern。
     */
    private void updateActionPanel(final GContainer selected) {
        if (actionPanel == null || actionPanel.isDisposed()) return;
        // clear 旧链接
        for (Link l : actionLinks) {
            if (!l.isDisposed()) l.dispose();
        }
        actionLinks.clear();

        if (selected == null) {
            // 空白选 — 只显示顶层 New 链接 (v0.2 便利项)
            addActionLink("New " + containerDef.gGetShortName(), new Runnable() {
                @Override public void run() { runNewTopLevel(); }
            });
        } else {
            // selected 的 sub-container defs 各加一条 "New <subDef>"
            for (final GContainerDef subDef : collectSubContainerDefs(selected)) {
                final String linkText = "New " + subDef.gGetShortName();
                addActionLink(linkText, new Runnable() {
                    @Override public void run() { runNewChild(selected, subDef); }
                });
            }
            // 跟参考 MasterFormSection:567-573 顺序: Del / Copy / ReName.
            addActionLink("Del Element", new Runnable() {
                @Override public void run() { runDelete(selected); }
            });
            addActionLink("Copy Element", new Runnable() {
                @Override public void run() { runDuplicate(selected); }
            });
            addActionLink("ReName Element", new Runnable() {
                @Override public void run() { runRename(selected); }
            });
        }
        actionPanel.layout(true, true);
    }

    /** Add a Link with "&lt;a&gt;text&lt;/a&gt;" — 跟参考 ActionManager.addActionLink line 146 同 markup。 */
    private void addActionLink(String text, final Runnable onClick) {
        Link link = new Link(actionPanel, SWT.NONE);
        link.setText("<a>" + text + "</a>");
        link.setLayoutData(new GridData(SWT.FILL, SWT.BEGINNING, true, false));
        link.addSelectionListener(new SelectionAdapter() {
            @Override public void widgetSelected(SelectionEvent e) { onClick.run(); }
        });
        toolkit.adapt(link, true, true);
        actionLinks.add(link);
    }

    // ============================================================ right-click menu (跟 action panel 内容一致)

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

    /**
     * 跟 {@link #updateActionPanel} 内容一致, 仅 Action vs Link 渲染差。
     * 跟参考 V25.10 MasterFormSection.createContextMenu (line 547-577) 字面对齐:
     * "New" submenu (CreateContainerActionProvider) + "Del Element" /
     * "Copy Element" / "ReName Element"。
     */
    private void fillContextMenu(IMenuManager mm) {
        final GContainer selected = currentSelection();

        if (selected == null) {
            mm.add(new Action("New " + containerDef.gGetShortName()) {
                @Override public void run() { runNewTopLevel(); }
            });
            return;
        }

        List<GContainerDef> subDefs = collectSubContainerDefs(selected);
        if (!subDefs.isEmpty()) {
            MenuManager newSub = new MenuManager("New");
            for (final GContainerDef subDef : subDefs) {
                newSub.add(new Action("New " + subDef.gGetShortName()) {
                    @Override public void run() { runNewChild(selected, subDef); }
                });
            }
            mm.add(newSub);
        }
        mm.add(new Action("Del Element") {
            @Override public void run() { runDelete(selected); }
        });
        mm.add(new Action("Copy Element") {
            @Override public void run() { runDuplicate(selected); }
        });
        mm.add(new Action("ReName Element") {
            @Override public void run() { runRename(selected); }
        });
    }

    private GContainer currentSelection() {
        if (masterViewer == null) return null;
        Object first = masterViewer.getStructuredSelection().getFirstElement();
        return first instanceof GContainer ? (GContainer) first : null;
    }

    /**
     * 跟参考 CreateContainerActionProvider.getSubContainerDefArray 同 dispatch:
     * GParamConfContainerDef → gGetSubContainers,
     * GChoiceContainerDef → gGetChoices (v0.2 暂不接 — 当前 ECUC 模块没用 choice)。
     */
    private static List<GContainerDef> collectSubContainerDefs(GContainer container) {
        List<GContainerDef> out = new ArrayList<>();
        if (container == null) return out;
        GContainerDef def = container.gGetDefinition();
        if (def instanceof GParamConfContainerDef) {
            for (GContainerDef sub : ((GParamConfContainerDef) def).gGetSubContainers()) {
                out.add(sub);
            }
        }
        return out;
    }

    // ============================================================ Action runners

    /** 顶层 create — 在 module 下加 containerDef 实例 (空白处右键 / Action panel)。 */
    private void runNewTopLevel() {
        String defaultName = uniqueDefaultName(containerDef.gGetShortName());
        InputDialog dlg = new InputDialog(masterViewer.getControl().getShell(),
                "New " + containerDef.gGetShortName(),
                "Enter shortName for the new " + containerDef.gGetShortName() + ":",
                defaultName, null);
        if (dlg.open() != InputDialog.OK) return;
        String name = dlg.getValue();
        if (name == null || name.isEmpty()) return;

        GContainer created = EcucWriteActions.addContainerUnder(editor(),
                (org.eclipse.emf.ecore.EObject) module, containerDef, name);
        if (created == null) {
            warn("Add failed", "Could not create new " + containerDef.gGetShortName());
            return;
        }
        refreshInstancesAndSelect(created);
    }

    /** 子级 create — 在 selected 下加 subDef 实例。 */
    private void runNewChild(GContainer parent, GContainerDef subDef) {
        String defaultName = subDef.gGetShortName() + "_0";
        InputDialog dlg = new InputDialog(masterViewer.getControl().getShell(),
                "New " + subDef.gGetShortName(),
                "Enter shortName for the new " + subDef.gGetShortName()
                        + " under " + parent.gGetShortName() + ":",
                defaultName, null);
        if (dlg.open() != InputDialog.OK) return;
        String name = dlg.getValue();
        if (name == null || name.isEmpty()) return;

        GContainer created = EcucWriteActions.addContainerUnder(editor(),
                (org.eclipse.emf.ecore.EObject) parent, subDef, name);
        if (created == null) {
            warn("Add failed", "Could not create child " + subDef.gGetShortName()
                    + " under " + parent.gGetShortName());
            return;
        }
        // Tree 展开 parent 节点让用户立刻看到新建的 sub-container
        masterViewer.refresh(parent);
        masterViewer.setExpandedState(parent, true);
        masterViewer.setSelection(new StructuredSelection(created), true);
    }

    private void runDelete(final GContainer victim) {
        if (!MessageDialog.openConfirm(masterViewer.getControl().getShell(),
                "Del Element", "Delete '" + victim.gGetShortName() + "'?")) return;
        if (!EcucWriteActions.removeContainer(editor(), victim)) {
            warn("Del Element failed", "Could not delete '" + victim.gGetShortName() + "'.");
            return;
        }
        refreshInstancesAndSelectFirst();
    }

    private void runRename(final GContainer target) {
        InputDialog dlg = new InputDialog(masterViewer.getControl().getShell(),
                "ReName Element",
                "Enter new shortName for '" + target.gGetShortName() + "':",
                target.gGetShortName(), null);
        if (dlg.open() != InputDialog.OK) return;
        String name = dlg.getValue();
        if (name == null || name.isEmpty() || name.equals(target.gGetShortName())) return;
        if (!EcucWriteActions.renameContainer(editor(), target, name)) {
            warn("ReName Element failed", "Could not rename '" + target.gGetShortName() + "'.");
            return;
        }
        masterViewer.refresh(target);
        masterViewer.setSelection(new StructuredSelection(target), true);
    }

    private void runDuplicate(final GContainer src) {
        GContainer copy = EcucWriteActions.duplicateContainer(editor(), src);
        if (copy == null) {
            warn("Copy Element failed", "Could not duplicate '" + src.gGetShortName() + "'.");
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

        // 渲染 instance 自己 def 的 parameters (顶层 def 可能跟 selected 实际 def 不一样,
        // 例如展开后选中 sub-container 时, 用 sub-container 自己的 def 渲染参数)
        GContainerDef instanceDef = instance.gGetDefinition();
        if (instanceDef instanceof GParamConfContainerDef) {
            GParamConfContainerDef pdef = (GParamConfContainerDef) instanceDef;
            for (GConfigParameter param : pdef.gGetParameters()) {
                addRow(client, param, instance);
            }
        }

        detailParent.layout(true, true);
        updateActionPanel(instance);
    }

    private void renderEmptyDetail(String message) {
        for (Control c : detailParent.getChildren()) c.dispose();
        Label l = toolkit.createLabel(detailParent, message, SWT.WRAP);
        GridDataFactory.fillDefaults().align(SWT.CENTER, SWT.CENTER).applyTo(l);
        detailParent.layout(true, true);
    }

    /** detail-side widget listeners 走 EcucWriteActions, 跟 GenericGeneralFormPage 同款。 */
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

        toolkit.createLabel(parent, "", SWT.NONE);
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

    public GContainerDef getContainerDef() { return containerDef; }
    public GContainer getSelectedInstance()  { return selectedInstance; }
}

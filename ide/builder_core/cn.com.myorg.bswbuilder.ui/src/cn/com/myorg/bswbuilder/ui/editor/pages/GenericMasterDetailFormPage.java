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
import org.eclipse.jface.viewers.ArrayContentProvider;
import org.eclipse.jface.viewers.ColumnLabelProvider;
import org.eclipse.jface.viewers.DoubleClickEvent;
import org.eclipse.jface.viewers.IDoubleClickListener;
import org.eclipse.jface.viewers.ISelectionChangedListener;
import org.eclipse.jface.viewers.SelectionChangedEvent;
import org.eclipse.jface.viewers.StructuredSelection;
import org.eclipse.jface.viewers.TableViewer;
import org.eclipse.jface.viewers.TableViewerColumn;
import org.eclipse.jface.viewers.TreeViewer;
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
import cn.com.myorg.bswbuilder.ui.contentviewers.ChildContainerGroup;
import cn.com.myorg.bswbuilder.ui.contentviewers.MasterTreeContentProvider;
import cn.com.myorg.bswbuilder.ui.contentviewers.MasterTreeLabelProvider;
import cn.com.myorg.bswbuilder.ui.contentviewers.TableDataContainer;
import cn.com.myorg.bswbuilder.ui.contentviewers.TreeChildWrap;
import cn.com.myorg.bswbuilder.ui.contentviewers.TreeViewerInputObject;
import cn.com.myorg.bswbuilder.ui.editor.utils.EcuUtils;
import cn.com.myorg.bswbuilder.ui.editor.utils.EcucWriteActions;
import cn.com.myorg.bswbuilder.ui.editor.utils.ProxyResolveHelper;
import cn.com.myorg.bswbuilder.ui.editor.utils.UIDefinitionDispatcher;
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

    /** Top-level wrapper "NvMBlockDescriptors" folder node (跟参考截图一致). */
    private TreeChildWrap rootWrap;

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
        // 标题格式跟 reference/ui 截图字面对齐: "<Module> - <Module> Module Manager"
        form.setText(moduleName + " - " + moduleName + " Module Manager");

        Composite body = form.getBody();
        GridLayoutFactory.fillDefaults().margins(5, 5).applyTo(body);

        // 顶部 Section: "<containerDef> details" 蓝色 + 描述行
        // (跟参考截图 reference/ui/C58BE21BCDABFA396FC0C5BAB0BEEF01.png 一致)
        Section topSection = toolkit.createSection(body, Section.TITLE_BAR | Section.DESCRIPTION);
        topSection.setText(containerName + " details");
        topSection.setDescription("This container containers the " + moduleName
                + " module specific parameters of each " + containerName + ".");
        GridDataFactory.fillDefaults().grab(true, false).applyTo(topSection);
        toolkit.createComposite(topSection);  // 占位 client (空)

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
        // 99% 配色复刻 reference NewAutosarMasterDetailBlock.java line 144-147:
        //   l.setForeground(new Color(null, 100, 100, 100));   -> 深灰 RGB(100,100,100)
        //   fd[0].setStyle(3); l.setFont(new Font(null, fd));   -> SWT.BOLD | SWT.ITALIC
        hint.setForeground(new org.eclipse.swt.graphics.Color(null, 100, 100, 100));
        org.eclipse.swt.graphics.FontData[] hintFd = hint.getFont().getFontData();
        hintFd[0].setStyle(SWT.BOLD | SWT.ITALIC);
        hint.setFont(new org.eclipse.swt.graphics.Font(null, hintFd));

        createDetail(sash);
        sash.setWeights(new int[] { 10, 15 });

        refreshInstancesAndSelectFirst();
    }

    /**
     * 跟参考 MasterFormSection.createSectionClientContent line 437 一致:
     * setInput(new TreeViewerInputObject(moduleConfig, containerDef)).
     * ContentProvider.getElements 内部 new TreeChildWrap, 不让我们自己 hold.
     */
    private void refreshInstancesAndSelectFirst() {
        instances = EcuUtils.getContainersByDef(module, containerDef);
        TreeViewerInputObject input = new TreeViewerInputObject(module, containerDef);
        if (masterViewer != null && !masterViewer.getTree().isDisposed()) {
            masterViewer.setInput(input);
            masterViewer.refresh();
            // 不强制 expandToLevel — 让用户手动展开
        }
        // 默认选 TreeChildWrap (顶层 folder) — 跟参考截图 2 NvMBlockDescriptors 根选中一致.
        // ContentProvider.getElements 已构造 TreeChildWrap, 取 viewer 第一行作 selection.
        Object[] roots = ((MasterTreeContentProvider) masterViewer.getContentProvider()).getElements(input);
        if (instances.size() == 1) {
            // 单实例 case (e.g., MemIfGeneral) — 默认选 instance 直接进 form view, 跟
            // reference/ui/C58BE21BCDABFA396FC0C5BAB0BEEF01.png 截图一致.
            masterViewer.expandToLevel(2);
            masterViewer.setSelection(new StructuredSelection(instances.get(0)), true);
        } else if (roots.length > 0) {
            // 多实例 case — 默认选 root folder → table view (横向所有 instance).
            masterViewer.setSelection(new StructuredSelection(roots[0]), true);
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
        section.setText("Container Hierarchical information:");
        GridDataFactory.fillDefaults().grab(true, true).applyTo(section);

        Composite client = toolkit.createComposite(section);
        GridLayoutFactory.fillDefaults().applyTo(client);
        section.setClient(client);

        masterViewer = new TreeViewer(client, SWT.BORDER | SWT.SINGLE | SWT.V_SCROLL);
        masterViewer.setUseHashlookup(true);  // 跟参考 MasterFormSection line 433 一致
        GridDataFactory.fillDefaults().grab(true, true).applyTo(masterViewer.getTree());

        // 三层 content provider 跟 MasterFormSection.ContentProvider 99% paraphrase
        masterViewer.setContentProvider(new MasterTreeContentProvider());
        masterViewer.setLabelProvider(new MasterTreeLabelProvider());

        masterViewer.addSelectionChangedListener(new ISelectionChangedListener() {
            @Override public void selectionChanged(SelectionChangedEvent event) {
                Object first = event.getStructuredSelection().getFirstElement();
                if (first instanceof GContainer) {
                    // 单实例选中 → form view
                    onInstanceSelected((GContainer) first);
                } else if (first instanceof TreeChildWrap) {
                    // 顶层根选中 → table view (跟参考截图 2)
                    TreeChildWrap w = (TreeChildWrap) first;
                    renderTableView(w.getContainerDef(), w.getChildItemList());
                    updateActionPanel(null);
                } else if (first instanceof ChildContainerGroup) {
                    // 子级 folder 选中 → table view 列出该 folder 内 sub-instance
                    ChildContainerGroup g = (ChildContainerGroup) first;
                    renderTableView(g.getContainerDef(), g.getElementList());
                    updateActionPanel(g.getParentContainer());
                } else if (first instanceof TableDataContainer) {
                    // table-row wrapper 选中 — 跟参考一致, 不进 form
                    updateActionPanel(((TableDataContainer) first).getParentContainer());
                } else {
                    updateActionPanel(null);
                }
            }
        });

        installContextMenu();
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
            // selected 的 sub-container defs 各加一条 "New <subDef>" — 按 upper-multiplicity 过滤,
            // 已达 upper 的 sub-def 不允许 New (跟参考 fillComposite isEnabled 一致).
            for (final GContainerDef subDef : collectSubContainerDefs(selected)) {
                int currentCount = countSubInstancesOfDef(selected, subDef);
                int upper = cn.com.myorg.mal.modelutils.EcuUtils.getUpperMultiplicity(
                        (org.eclipse.emf.ecore.EObject) subDef);
                if (upper > 0 && currentCount >= upper) continue;  // 已达上限不显示 New
                final String linkText = "New " + subDef.gGetShortName();
                addActionLink(linkText, new Runnable() {
                    @Override public void run() { runNewChild(selected, subDef); }
                });
            }
            // Del/Copy/Rename — multiplicity + ReserveUIDefinition 双层过滤.
            // MemIfGeneral [1..1] singleton 应只剩 ReName (countSiblings=1=lower, 不能 Del/Copy).
            int siblingCount = countSiblingsOfSameDef(selected);
            int lower = cn.com.myorg.mal.modelutils.EcuUtils.getLowerMultiplicity(
                    (org.eclipse.emf.ecore.EObject) selected.gGetDefinition());
            int selfDefUpper = cn.com.myorg.mal.modelutils.EcuUtils.getUpperMultiplicity(
                    (org.eclipse.emf.ecore.EObject) selected.gGetDefinition());
            boolean canRemove = siblingCount > Math.max(lower, 0);
            boolean canDuplicate = selfDefUpper <= 0 || siblingCount < selfDefUpper;
            boolean permitDel = checkReservePermit(selected, ReservePermit.DEL);
            boolean permitDup = checkReservePermit(selected, ReservePermit.DUPLICATE);
            boolean permitRen = checkReservePermit(selected, ReservePermit.RENAME);
            if (permitDel && canRemove) {
                addActionLink("Del Element", new Runnable() {
                    @Override public void run() { runDelete(selected); }
                });
            }
            if (permitDup && canDuplicate) {
                addActionLink("Copy Element", new Runnable() {
                    @Override public void run() { runDuplicate(selected); }
                });
            }
            if (permitRen) {
                addActionLink("ReName Element", new Runnable() {
                    @Override public void run() { runRename(selected); }
                });
            }
        }
        actionPanel.layout(true, true);
    }

    private enum ReservePermit { DEL, DUPLICATE, RENAME }

    /** Count sub-instances under {@code parent} whose def shortName == subDef.shortName. */
    private static int countSubInstancesOfDef(GContainer parent, GContainerDef subDef) {
        if (parent == null || subDef == null) return 0;
        String subDefName = subDef.gGetShortName();
        if (subDefName == null) return 0;
        int n = 0;
        for (GContainer sub : parent.gGetSubContainers()) {
            GContainerDef d = sub.gGetDefinition();
            if (d != null && subDefName.equals(d.gGetShortName())) n++;
        }
        return n;
    }

    /** Count siblings of {@code selected} under same eContainer with same def. */
    private int countSiblingsOfSameDef(GContainer selected) {
        if (selected == null) return 0;
        org.eclipse.emf.ecore.EObject parent = ((org.eclipse.emf.ecore.EObject) selected).eContainer();
        if (parent == null) return 1;
        GContainerDef def = selected.gGetDefinition();
        String defName = def == null ? null : def.gGetShortName();
        int n = 0;
        if (parent instanceof GModuleConfiguration) {
            for (GContainer c : ((GModuleConfiguration) parent).gGetContainers()) {
                GContainerDef d = c.gGetDefinition();
                if (d != null && defName != null && defName.equals(d.gGetShortName())) n++;
            }
        } else if (parent instanceof GContainer) {
            for (GContainer c : ((GContainer) parent).gGetSubContainers()) {
                GContainerDef d = c.gGetDefinition();
                if (d != null && defName != null && defName.equals(d.gGetShortName())) n++;
            }
        }
        return n == 0 ? 1 : n;
    }

    /**
     * 调 MetaModelDescriptorParser.getUIDefinitionList(ecuName, def.shortName, RESERVED_FLAG)
     * 拿 ReserveUIDefinition list, 调 permit{Del,Duplicate,Rename}(selected) 决定 link 是否 show.
     * 跟参考 BswContainerUtil.java:55+ 同 pattern (3 处 RESERVED_FLAG 分别 dispatch).
     */
    private boolean checkReservePermit(GContainer selected, ReservePermit kind) {
        try {
            GContainerDef def = selected.gGetDefinition();
            if (def == null) return true;
            String defShortName = def.gGetShortName();
            if (defShortName == null || defShortName.isEmpty()) return true;
            java.util.List<cn.com.myorg.mal.uidefinition.IUIDefinition> defs =
                    cn.com.myorg.mal.MetaModelDescriptorParser.getUIDefinitionList(
                            "", defShortName, cn.com.myorg.mal.uidefinition.IUIDefinition.RESERVED_FLAG);
            if (defs == null || defs.isEmpty()) return true;
            for (cn.com.myorg.mal.uidefinition.IUIDefinition d : defs) {
                if (!(d instanceof cn.com.myorg.mal.uidefinition.ReserveUIDefinition)) continue;
                cn.com.myorg.mal.uidefinition.ReserveUIDefinition r =
                        (cn.com.myorg.mal.uidefinition.ReserveUIDefinition) d;
                switch (kind) {
                    case DEL:       if (!r.permitDel(selected))       return false; break;
                    case DUPLICATE: if (!r.permitDuplicate(selected)) return false; break;
                    case RENAME:    if (!r.permitRename(selected))    return false; break;
                }
            }
            return true;
        } catch (Throwable t) {
            return true;
        }
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
        GContainerDef def = resolveDef(container);
        if (def instanceof GParamConfContainerDef) {
            for (GContainerDef sub : ((GParamConfContainerDef) def).gGetSubContainers()) {
                out.add(sub);
            }
        }
        return out;
    }

    /** Shared proxy-aware def resolution — see {@link ProxyResolveHelper}. */
    private static GContainerDef resolveDef(GContainer container) {
        if (container == null) return null;
        GContainerDef def = container.gGetDefinition();
        if (def == null) return null;
        if (!((org.eclipse.emf.ecore.EObject) def).eIsProxy()) return def;
        org.eclipse.emf.ecore.EObject resolved = ProxyResolveHelper.resolve(
                (org.eclipse.emf.ecore.EObject) def, container);
        return (resolved instanceof GContainerDef) ? (GContainerDef) resolved : def;
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
        // 必须 TreeViewerInputObject (跟 refreshInstancesAndSelectFirst 一致),
        // 否则新 ContentProvider.getElements 不认 List 直接返空 → tree 全空,
        // 用户报 "New 后所有 NvMBlockDescriptor 都消失了" 的根因.
        TreeViewerInputObject input = new TreeViewerInputObject(module, containerDef);
        masterViewer.setInput(input);
        masterViewer.refresh();
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
        // 2 列简洁: label | widget (checkbox/D 按钮先去掉等读懂 ECUC SDG 再加)
        GridLayout grid = new GridLayout(2, false);
        grid.marginTop = 6;
        grid.horizontalSpacing = 8;
        grid.verticalSpacing = 6;
        client.setLayout(grid);
        section.setClient(client);

        // Resolve possibly-proxied def via ProxyResolveHelper (handles ar:/?type=
        // URIs that standard EcoreUtil.resolve can't decode). Without resolution
        // the instanceof check returns false → 0 params → 用户报 "不显示配置".
        GContainerDef instanceDef = resolveDef(instance);
        if (instanceDef instanceof GParamConfContainerDef) {
            GParamConfContainerDef pdef = (GParamConfContainerDef) instanceDef;
            for (GConfigParameter param : pdef.gGetParameters()) {
                addRow(client, param, instance);
            }
        }

        detailParent.layout(true, true);
        updateActionPanel(instance);
    }

    /**
     * Render a table view listing all instances of {@code def} as rows × all parameters
     * of {@code def} as columns. 跟 reference/ui/截图 2 (NvMBlockDescriptors 根选中)
     * 一致 — 横向列出 25 个 NvMBlock_* 实例 + 各字段值. 双击 row 切到 form view.
     */
    private void renderTableView(GContainerDef def, List<GContainer> rows) {
        for (Control c : detailParent.getChildren()) c.dispose();
        detailWidgets.clear();

        Section section = toolkit.createSection(detailParent, Section.TITLE_BAR | Section.DESCRIPTION);
        section.setText(def.gGetShortName() + "s");
        section.setDescription(rows.size() + " instance(s) of " + def.gGetShortName()
                + ". Double-click a row to edit in form view.");
        GridDataFactory.fillDefaults().grab(true, true).applyTo(section);

        Composite client = toolkit.createComposite(section);
        GridLayoutFactory.fillDefaults().applyTo(client);
        section.setClient(client);

        final TableViewer tv = new TableViewer(client,
                SWT.BORDER | SWT.FULL_SELECTION | SWT.H_SCROLL | SWT.V_SCROLL);
        tv.getTable().setHeaderVisible(true);
        tv.getTable().setLinesVisible(true);
        GridDataFactory.fillDefaults().grab(true, true).applyTo(tv.getTable());

        // Name column (固定首列)
        TableViewerColumn nameCol = new TableViewerColumn(tv, SWT.NONE);
        nameCol.getColumn().setText("Name");
        nameCol.getColumn().setWidth(200);
        nameCol.setLabelProvider(new ColumnLabelProvider() {
            @Override public String getText(Object e) {
                return e instanceof GContainer ? ((GContainer) e).gGetShortName() : String.valueOf(e);
            }
        });

        // 每个 GConfigParameter 一列
        if (def instanceof GParamConfContainerDef) {
            for (final GConfigParameter param : ((GParamConfContainerDef) def).gGetParameters()) {
                TableViewerColumn col = new TableViewerColumn(tv, SWT.NONE);
                col.getColumn().setText(param.gGetShortName());
                col.getColumn().setWidth(140);
                col.setLabelProvider(new ColumnLabelProvider() {
                    @Override public String getText(Object e) {
                        if (!(e instanceof GContainer)) return "";
                        String v = readParamValue((GContainer) e, param);
                        return v == null ? "N/A" : v;
                    }
                });
            }
        }

        tv.setContentProvider(ArrayContentProvider.getInstance());
        tv.setInput(rows.toArray());

        // 双击 row → master tree 选中该 GContainer → 触发 form view
        tv.addDoubleClickListener(new IDoubleClickListener() {
            @Override public void doubleClick(DoubleClickEvent ev) {
                Object first = ((StructuredSelection) ev.getSelection()).getFirstElement();
                if (first instanceof GContainer && masterViewer != null) {
                    masterViewer.setSelection(new StructuredSelection(first), true);
                }
            }
        });

        detailParent.layout(true, true);
    }

    private void renderEmptyDetail(String message) {
        for (Control c : detailParent.getChildren()) c.dispose();
        Label l = toolkit.createLabel(detailParent, message, SWT.WRAP);
        GridDataFactory.fillDefaults().align(SWT.CENTER, SWT.CENTER).applyTo(l);
        detailParent.layout(true, true);
    }

    /**
     * detail-side widget listeners 走 EcucWriteActions, 跟 GenericGeneralFormPage 同款.
     * 当前 2 列布局: label | widget. 参考截图里"checkbox / D 按钮"不是每行都有,
     * 是按 ECUC SDG (origin / required / hide flag) 决定的 — 没读懂 SDG 元数据
     * 之前不机械照搬, 等 Phase 6c 反完 IdentifiableOption.getOption("HIDE_FLAG"
     * / "TABLE_FLAG" / 等) 再准确加。
     */
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

        detailWidgets.put(param, widget);

        // Apply field-enable hooks contributed by the module's FunctionExtension
        // (Phase 2.5 PoC: NvMBlockUseCrcEnable). Static apply on widget creation.
        UIDefinitionDispatcher.applyEnableHooks(instance, param.gGetShortName(), widget);
    }

    private void writeNumericalParam(GContainer instance, GConfigParameter param, String newText) {
        GParameterValue pv = EcuUtils.getParameterValue(instance, param);
        if (pv instanceof EcucNumericalParamValue) {
            EcucWriteActions.setNumericalText(editor(), (EcucNumericalParamValue) pv, newText);
            UIDefinitionDispatcher.reapplyForRelated(instance, param.gGetShortName(), detailWidgets);
        } else if (pv == null) {
            log("writeNumericalParam: pv missing for " + param.gGetShortName() + " on "
                    + instance.gGetShortName() + " — skip (S5.5 will create pv)");
        }
    }

    private void writeTextualParam(GContainer instance, GConfigParameter param, String newValue) {
        GParameterValue pv = EcuUtils.getParameterValue(instance, param);
        if (pv instanceof EcucTextualParamValue) {
            EcucWriteActions.setTextualValue(editor(), (EcucTextualParamValue) pv, newValue);
            UIDefinitionDispatcher.reapplyForRelated(instance, param.gGetShortName(), detailWidgets);
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

package cn.com.myorg.bswbuilder.ui.contentviewers;

import java.util.ArrayList;
import java.util.List;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.jface.viewers.Viewer;

import autosar40.ecucparameterdef.EcucChoiceContainerDef;
import autosar40.ecucparameterdef.EcucContainerDef;
import autosar40.ecucparameterdef.EcucParamConfContainerDef;
import autosar40.ecucparameterdef.EcucParameterDef;
import autosar40.genericstructure.generaltemplateclasses.identifiable.Identifiable;
import cn.com.myorg.bswbuilder.ui.Activator;
import cn.com.myorg.bswbuilder.ui.editor.utils.ProxyResolveHelper;
import cn.com.myorg.mal.admindata.IdentifiableOption;
import cn.com.myorg.mal.modelutils.EcuUtils;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucparameterdef.GContainerDef;

/**
 * 99% paraphrase of cn.com.isoft.bswbuilder.ui.editor.section.MasterFormSection
 * inner class ContentProvider (line 819-970, ~150 lines).
 *
 * <p>分支结构 + IdentifiableOption SDG flag 全部 1:1 保留:
 * <ul>
 *   <li>TreeChildWrap → return getChildItemList</li>
 *   <li>GContainer + EcucParamConfContainerDef → isDisplay 过滤 + sub-defs.size {@code > 1} / == 1 / 0 三分支
 *       + 5 SDG flag (TABLE_FLAG / UPPER_LAYER_FLAG / NEW_CHOICE_CONTAINER_FLAG / TABLE_SPC_FLAG)</li>
 *   <li>GContainer + EcucChoiceContainerDef → NEW_CHOICE_CONTAINER_FLAG 决定走 sub-containers vs flatten</li>
 *   <li>TableDataContainer → 0 children</li>
 *   <li>ChildContainerGroup → getElementList</li>
 * </ul>
 *
 * <p>1% divergence: variant filter (getVariantValue + getActiveVariant) 在 MEN
 * 不实装 — getSubContainers 直返所有 sub-instance, 不按 variant 过滤. variant
 * 体系是另一独立 feature (PostBuildVariant 整套), Phase 6 后期 port. 当前
 * Demo 不用 variant, 不影响 master tree 渲染.
 */
public class MasterTreeContentProvider extends org.eclipse.ui.navigator.CommonActionProvider
        implements ITreeContentProvider {

    @Override
    public Object[] getChildren(Object parentElement) {
        if (parentElement instanceof TreeChildWrap) {
            List<GContainer> lstContainer = ((TreeChildWrap) parentElement).getChildItemList();
            log("getChildren TreeChildWrap[" + ((TreeChildWrap) parentElement).getContainerDef().gGetShortName()
                    + "] -> " + lstContainer.size() + " GContainer instance(s)");
            return lstContainer.toArray(new GContainer[lstContainer.size()]);
        }
        if (parentElement instanceof GContainer) {
            GContainer container = (GContainer) parentElement;
            GContainerDef containerDef = resolveDef(container);
            if (containerDef instanceof EcucParamConfContainerDef) {
                EcucParamConfContainerDef paramConfContainerDef = (EcucParamConfContainerDef) containerDef;
                if (!this.isDisplay(paramConfContainerDef)) {
                    log("getChildren GContainer[" + container.gGetShortName() + "] isDisplay=false -> 0");
                    return new Object[0];
                }
                ArrayList<Object> lstRet = new ArrayList<>();
                ArrayList<TableDataContainer> lstTableDataContainer = new ArrayList<>();
                ArrayList<ChildContainerGroup> lstChildContainerGroup = new ArrayList<>();
                ArrayList<GContainer> lstContainer = new ArrayList<>();
                EList<? extends GContainerDef> lstGContainerDef = paramConfContainerDef.gGetSubContainers();
                if (lstGContainerDef.size() > 1) {
                    for (GContainerDef def : lstGContainerDef) {
                        if (!(def instanceof EcucChoiceContainerDef)) {
                            IdentifiableOption identifiableOption = new IdentifiableOption((Identifiable) def);
                            String table = identifiableOption.getOption("TABLE_FLAG");
                            if (table.equals("true")) {
                                lstTableDataContainer.add(new TableDataContainer(container, (EcucContainerDef) def));
                                continue;
                            }
                            String upper_layer = identifiableOption.getOption("UPPER_LAYER_FLAG");
                            if (upper_layer.equals("true")) continue;
                            lstChildContainerGroup.add(new ChildContainerGroup(container, (EcucContainerDef) def));
                            continue;
                        }
                        if (!(def instanceof EcucChoiceContainerDef)) continue;
                        IdentifiableOption identifiableOption = new IdentifiableOption((Identifiable) def);
                        String showChoice = identifiableOption.getOption("NEW_CHOICE_CONTAINER_FLAG");
                        if ("true".equals(showChoice)) {
                            String upper_layer = identifiableOption.getOption("UPPER_LAYER_FLAG");
                            if (upper_layer.equals("true")) continue;
                            lstContainer.addAll(EcuUtils.getChoiceChildContainers(container,
                                    (EcucChoiceContainerDef) def));
                            continue;
                        }
                        lstChildContainerGroup.add(new ChildContainerGroup(container, (EcucContainerDef) def));
                    }
                } else if (lstGContainerDef.size() == 1) {
                    GContainerDef def = lstGContainerDef.get(0);
                    if (!(def instanceof EcucChoiceContainerDef)) {
                        IdentifiableOption identifiableOption = new IdentifiableOption((Identifiable) def);
                        String table = identifiableOption.getOption("TABLE_FLAG");
                        if (table.equals("true")) {
                            lstTableDataContainer.add(new TableDataContainer(container, (EcucContainerDef) def));
                        } else {
                            String upper_layer = identifiableOption.getOption("UPPER_LAYER_FLAG");
                            if (!upper_layer.equals("true")) {
                                lstChildContainerGroup.add(new ChildContainerGroup(container, (EcucContainerDef) def));
                            }
                        }
                    } else if (def instanceof EcucChoiceContainerDef) {
                        IdentifiableOption identifiableOption = new IdentifiableOption((Identifiable) def);
                        String showChoice = identifiableOption.getOption("NEW_CHOICE_CONTAINER_FLAG");
                        if ("true".equals(showChoice)) {
                            String upper_layer = identifiableOption.getOption("UPPER_LAYER_FLAG");
                            if (!upper_layer.equals("true")) {
                                lstContainer.addAll(EcuUtils.getChoiceChildContainers(container,
                                        (EcucChoiceContainerDef) def));
                            }
                        } else {
                            lstChildContainerGroup.add(new ChildContainerGroup(container, (EcucContainerDef) def));
                        }
                    }
                }
                lstRet.addAll(lstContainer);
                lstRet.addAll(lstTableDataContainer);
                lstRet.addAll(lstChildContainerGroup);
                log("getChildren GContainer[" + container.gGetShortName() + " def=" + containerDef.gGetShortName()
                        + "] -> " + lstRet.size() + " (instance=" + lstContainer.size()
                        + " table=" + lstTableDataContainer.size()
                        + " group=" + lstChildContainerGroup.size() + ")");
                if (lstRet.size() != 1 || lstTableDataContainer.size() != 1) return lstRet.toArray();
                IdentifiableOption identifiableOption = new IdentifiableOption(
                        (Identifiable) lstTableDataContainer.get(0).getContainerDef());
                String table = identifiableOption.getOption("TABLE_SPC_FLAG");
                if (!table.equals("true")) return new Object[0];
                return lstRet.toArray();
            }
            if (!(containerDef instanceof EcucChoiceContainerDef)) {
                log("getChildren GContainer[" + container.gGetShortName() + "] non-PARAM-CONF non-CHOICE -> 0");
                return new Object[0];
            }
            IdentifiableOption identifiableOption = new IdentifiableOption((Identifiable) containerDef);
            String showChoice = identifiableOption.getOption("NEW_CHOICE_CONTAINER_FLAG");
            if (!"true".equals(showChoice)) return this.getSubContainers(container);
            return ((GContainer) container.gGetSubContainers().get(0)).gGetSubContainers().toArray();
        }
        if (parentElement instanceof TableDataContainer) {
            return new Object[0];
        }
        if (!(parentElement instanceof ChildContainerGroup)) {
            log("getChildren UNKNOWN class=" + parentElement.getClass().getSimpleName() + " -> 0");
            return new Object[0];
        }
        if (((ChildContainerGroup) parentElement).getElementList().size() <= 0) return new Object[0];
        return ((ChildContainerGroup) parentElement).getElementList().toArray();
    }

    private boolean isDisplay(EcucParamConfContainerDef paramConfiContainerDef) {
        IdentifiableOption identifiableOption;
        String table;
        for (EcucParameterDef p : paramConfiContainerDef.getParameters()) {
            IdentifiableOption identifiableOption2 = new IdentifiableOption((Identifiable) p);
            String hide = identifiableOption2.getOption("HIDE_FLAG");
            if (!hide.equals("")) continue;
            return true;
        }
        if (paramConfiContainerDef.getReferences().size() > 1) {
            return true;
        }
        return paramConfiContainerDef.getSubContainers().size() != 1
                || !(table = (identifiableOption = new IdentifiableOption((Identifiable) paramConfiContainerDef))
                        .getOption("TABLE_FLAG")).equals("true");
    }

    @Override
    public Object getParent(Object element) {
        return null;
    }

    @Override
    public boolean hasChildren(Object element) {
        return this.getChildren(element).length > 0;
    }

    @Override
    public Object[] getElements(Object inputElement) {
        if (inputElement instanceof TreeViewerInputObject) {
            TreeViewerInputObject root = (TreeViewerInputObject) inputElement;
            return new Object[] {
                new TreeChildWrap(root.getModuleConfiguration(), root.getContainerDef())
            };
        }
        return new Object[0];
    }

    @Override
    public void inputChanged(Viewer viewer, Object oldInput, Object newInput) {
        viewer.refresh();
    }

    /**
     * 99% paraphrase of MasterFormSection.ContentProvider.getSubContainers (line 960-969).
     * 1% divergence: variant filter (getVariantValue + getActiveVariant) 在 MEN 不实装,
     * 直返所有 sub-instance.
     */
    private Object[] getSubContainers(GContainer container) {
        ArrayList<GContainer> subCotainers = new ArrayList<>();
        for (GContainer subContainer : container.gGetSubContainers()) {
            subCotainers.add(subContainer);
        }
        return subCotainers.toArray();
    }

    /**
     * Resolve possibly-proxied container definition. ARTOP encodes def
     * cross-refs as {@code ar:/#/...?type=...} URIs which standard
     * {@link org.eclipse.emf.ecore.util.EcoreUtil#resolve} can't decode without
     * full Sphinx wiring. Delegate to {@link ProxyResolveHelper} which scans
     * loaded resources for a matching Identifiable.
     */
    private static GContainerDef resolveDef(GContainer container) {
        GContainerDef def = container.gGetDefinition();
        if (def == null) return null;
        if (!((EObject) def).eIsProxy()) return def;
        EObject resolved = ProxyResolveHelper.resolve((EObject) def, container);
        return (resolved instanceof GContainerDef) ? (GContainerDef) resolved : def;
    }

    private static void log(String msg) {
        try {
            Activator a = Activator.getDefault();
            if (a != null) {
                a.getLog().log(new Status(IStatus.INFO, Activator.PLUGIN_ID, "[MasterTreeCP] " + msg));
            }
        } catch (Throwable ignored) { /* fall back silent */ }
    }
}

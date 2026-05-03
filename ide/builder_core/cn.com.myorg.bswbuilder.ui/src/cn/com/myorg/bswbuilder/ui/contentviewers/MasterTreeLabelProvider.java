package cn.com.myorg.bswbuilder.ui.contentviewers;

import org.eclipse.jface.viewers.ILabelProvider;
import org.eclipse.jface.viewers.StyledCellLabelProvider;
import org.eclipse.jface.viewers.StyledString;
import org.eclipse.jface.viewers.ViewerCell;
import org.eclipse.swt.graphics.Image;
import org.eclipse.swt.graphics.TextStyle;
import org.eclipse.swt.widgets.Display;
import org.eclipse.ui.ISharedImages;
import org.eclipse.ui.PlatformUI;

import autosar40.ecucparameterdef.EcucParamConfContainerDef;
import autosar40.ecucparameterdef.EcucParameterDef;
import autosar40.genericstructure.generaltemplateclasses.identifiable.Identifiable;
import cn.com.myorg.mal.admindata.IdentifiableOption;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucdescription.GModuleConfiguration;
import gautosar.gecucparameterdef.GContainerDef;
import gautosar.gecucparameterdef.GConfigParameter;
import gautosar.gecucparameterdef.GParamConfContainerDef;

/**
 * 99% paraphrase of cn.com.isoft.bswbuilder.ui.editor.section.MasterFormSection
 * inner class TreeLabelProvider (line 987-1107).
 *
 * <p>1% divergences:
 * <ul>
 *   <li>ISoftGraphics images → Eclipse ISharedImages (folder/file standard icons).
 *       图标提供方等价替换, 截图视觉略有差异但语义一致.</li>
 *   <li>isVariantPoint always returns false — VariationPoint 体系不实装 (跟
 *       ContentProvider.getSubContainers 一致).</li>
 * </ul>
 */
public class MasterTreeLabelProvider extends StyledCellLabelProvider implements ILabelProvider {

    StyledString.Styler style = new StyledString.Styler() {
        @Override
        public void applyStyles(TextStyle textStyle) {
            textStyle.foreground = Display.getDefault().getSystemColor(3);
        }
    };

    private boolean isVariantPoint(Object element) {
        // 1% divergence: variant 体系不实装, 始终返 false.
        return false;
    }

    @Override
    public void update(ViewerCell cell) {
        Object element = cell.getElement();
        StyledString styledString = new StyledString();
        styledString.append(this.getText(element));
        if (this.isVariantPoint(element)) {
            styledString.append(" [V]", this.style);
        }
        cell.setText(styledString.toString());
        cell.setStyleRanges(styledString.getStyleRanges());
        cell.setImage(this.getImage(element));
        super.update(cell);
    }

    @Override
    public Image getImage(Object element) {
        ISharedImages shared = PlatformUI.getWorkbench().getSharedImages();
        if (element instanceof GContainer) {
            GContainer container = (GContainer) element;
            if (!this.isDisplay(container)) {
                return shared.getImage(ISharedImages.IMG_OBJ_FOLDER);
            }
            if (container.eContainer() instanceof GModuleConfiguration) {
                return shared.getImage(ISharedImages.IMG_OBJ_FOLDER);
            }
            return shared.getImage(ISharedImages.IMG_OBJ_FILE);
        }
        if (element instanceof TreeChildWrap) {
            return shared.getImage(ISharedImages.IMG_OBJ_FOLDER);
        }
        if (element instanceof GModuleConfiguration) {
            return shared.getImage(ISharedImages.IMG_OBJ_FOLDER);
        }
        if (element instanceof ChildContainerGroup) {
            return shared.getImage(ISharedImages.IMG_OBJ_FOLDER);
        }
        return shared.getImage(ISharedImages.IMG_OBJ_FILE);
    }

    @Override
    public String getText(Object element) {
        if (element instanceof GModuleConfiguration) {
            return ((GModuleConfiguration) element).gGetShortName();
        }
        if (element instanceof GContainer) {
            return ((GContainer) element).gGetShortName();
        }
        if (element instanceof TreeChildWrap) {
            return ((TreeChildWrap) element).getContainerDef().gGetShortName() + "s";
        }
        if (element instanceof TableDataContainer) {
            GContainerDef def = ((TableDataContainer) element).getContainerDef();
            String control_name = new IdentifiableOption((Identifiable) def).getOption("CONTROL_NAME");
            if (!control_name.equals("")) {
                return control_name;
            }
            return def.gGetShortName();
        }
        if (element instanceof ChildContainerGroup) {
            String defShortName = ((ChildContainerGroup) element).getContainerDef().gGetShortName();
            int subContainerNum = ((ChildContainerGroup) element).getElementList().size();
            return defShortName + "s (" + subContainerNum + ")";
        }
        return "no definition";
    }

    private boolean isDisplay(GContainer container) {
        GContainerDef containerDef = container.gGetDefinition();
        if (containerDef instanceof EcucParamConfContainerDef) {
            IdentifiableOption identifiableOption;
            GParamConfContainerDef paramConfContainerDef = (GParamConfContainerDef) containerDef;
            for (GConfigParameter configParameter : paramConfContainerDef.gGetParameters()) {
                identifiableOption = new IdentifiableOption((Identifiable) configParameter);
                String hide = identifiableOption.getOption("HIDE_FLAG");
                if (!hide.equals("true")) continue;
                return true;
            }
            if (paramConfContainerDef.gGetReferences().size() > 1) {
                return true;
            }
            if (paramConfContainerDef.gGetSubContainers().size() > 1) {
                for (GContainerDef def : paramConfContainerDef.gGetSubContainers()) {
                    identifiableOption = new IdentifiableOption((Identifiable) def);
                    String upper_layer = identifiableOption.getOption("UPPER_LAYER_FLAG");
                    if (!upper_layer.equals("true")) continue;
                    return true;
                }
                return false;
            }
            if (paramConfContainerDef.gGetSubContainers().size() == 1) {
                IdentifiableOption identifiableOption2 = new IdentifiableOption(
                        (Identifiable) paramConfContainerDef.gGetSubContainers().get(0));
                String table = identifiableOption2.getOption("TABLE_FLAG");
                if (table.equals("true")) {
                    return true;
                }
                if (cn.com.myorg.mal.modelutils.EcuUtils.getUpperMultiplicity(
                        (org.eclipse.emf.ecore.EObject) paramConfContainerDef) > 1) {
                    return false;
                }
                if (cn.com.myorg.mal.modelutils.EcuUtils.getUpperMultiplicity(
                        (org.eclipse.emf.ecore.EObject) paramConfContainerDef.gGetSubContainers().get(0)) > 1) {
                    return false;
                }
            }
        }
        return true;
    }
}

package cn.com.myorg.bswbuilder.ui.editor.utils;

import java.util.List;
import java.util.Map;

import org.eclipse.swt.widgets.Control;

import cn.com.myorg.mal.MetaModelDescriptorParser;
import cn.com.myorg.mal.uidefinition.EnableUIDefinition;
import cn.com.myorg.mal.uidefinition.IUIDefinition;
import cn.com.myorg.mal.uidefinition.RelatedUIDefinition;
import gautosar.gecucdescription.GContainer;
import gautosar.gecucparameterdef.GConfigParameter;

/**
 * Phase 2.5 PoC dispatcher — bridges form-page widgets to module-contributed
 * IUIDefinition hooks via MetaModelDescriptorParser. Pattern mirrors reference
 * V25.10 cn.com.isoft.bswbuilder.ui.units.BaseEditUnit.enableHandle.
 *
 * <p>Reference passes mcuName from the surrounding McuModuleManagerEditor /
 * BswModuleManagerEditor; for the PoC we pass an empty string — MEN's
 * AutocoreCoordinator returns all modules when none declares requiredMcus
 * (NvM/MemIf/etc don't, so the dispatcher sees every registered module's
 * FunctionExtension regardless). Phase 6c will plumb the real mcu identifier
 * through the editor input once cross-module flow is exercised.
 *
 * <p>PoC scope: ENABLE_FLAG / ComputeEnableUIDefinition only. RANGE_FLAG
 * (drop-down value scope), CHANGE_MODEL_FLAG, RESERVED_FLAG (right-click
 * constraints), AUTO_COMPUTE (write-back) are wired in 6c/6d.
 */
public final class UIDefinitionDispatcher {

    /** PoC: no mcu filter (MEN modules don't declare requiredMcus). */
    private static final String POC_MCU_NAME = "";

    private UIDefinitionDispatcher() {
    }

    /**
     * Apply enable/disable hooks to {@code widget} for the field
     * {@code elementName} on container {@code parent}. ComputeEnableUIDefinition
     * variant (12296L = ENABLE | DISABLE | FIX) drives a single setEnabled call.
     */
    public static void applyEnableHooks(GContainer parent, String elementName, Control widget) {
        if (widget == null || widget.isDisposed()) return;
        List<IUIDefinition> defs =
                MetaModelDescriptorParser.getUIDefinitionList(POC_MCU_NAME, elementName, IUIDefinition.ENABLE_FLAG);
        if (defs == null || defs.isEmpty()) return;
        for (IUIDefinition d : defs) {
            if (!(d instanceof EnableUIDefinition)) continue;
            EnableUIDefinition ed = (EnableUIDefinition) d;
            boolean enabled = ed.isEnable(parent);
            widget.setEnabled(enabled);
            // First matching ENABLE hook wins (mirrors reference enableHandle which
            // applies sequentially; PoC only registers one per element).
            return;
        }
    }

    /**
     * After {@code changedElement} on {@code parent} was written, re-evaluate
     * any widget whose hook lists {@code changedElement} in its
     * getRelatedUIElementList — equivalent to reference notifyValueChanged
     * cascade.
     */
    public static void reapplyForRelated(GContainer parent,
                                         String changedElement,
                                         Map<GConfigParameter, Control> widgets) {
        if (widgets == null || widgets.isEmpty()) return;
        for (Map.Entry<GConfigParameter, Control> e : widgets.entrySet()) {
            String element = e.getKey().gGetShortName();
            if (element.equals(changedElement)) continue; // self
            List<IUIDefinition> defs = MetaModelDescriptorParser.getUIDefinitionList(POC_MCU_NAME, element);
            if (defs == null) continue;
            for (IUIDefinition d : defs) {
                if (!(d instanceof RelatedUIDefinition)) continue;
                List<String> related = ((RelatedUIDefinition) d).getRelatedUIElementList();
                if (related != null && related.contains(changedElement)) {
                    applyEnableHooks(parent, element, e.getValue());
                    break;
                }
            }
        }
    }
}

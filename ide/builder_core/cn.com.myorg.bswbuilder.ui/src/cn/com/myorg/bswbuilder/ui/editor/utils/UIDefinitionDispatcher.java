package cn.com.myorg.bswbuilder.ui.editor.utils;

import java.util.List;
import java.util.Map;

import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.swt.widgets.Control;

import cn.com.myorg.bswbuilder.ui.Activator;
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
 */
public final class UIDefinitionDispatcher {

    /** PoC: no mcu filter (MEN modules don't declare requiredMcus). */
    private static final String POC_MCU_NAME = "";

    private UIDefinitionDispatcher() {
    }

    public static void applyEnableHooks(GContainer parent, String elementName, Control widget) {
        if (widget == null || widget.isDisposed()) {
            log("applyEnableHooks SKIP: widget null/disposed for element=" + elementName);
            return;
        }
        if (parent == null) {
            log("applyEnableHooks SKIP: parent null for element=" + elementName);
            return;
        }
        try {
            List<IUIDefinition> defs = MetaModelDescriptorParser.getUIDefinitionList(
                    POC_MCU_NAME, elementName, IUIDefinition.ENABLE_FLAG);
            int count = defs == null ? 0 : defs.size();
            log("applyEnableHooks parent=" + parent.gGetShortName() + " element=" + elementName
                    + " hits=" + count);
            if (defs == null || defs.isEmpty()) return;
            for (IUIDefinition d : defs) {
                if (!(d instanceof EnableUIDefinition)) {
                    log("  skip non-EnableUIDefinition class=" + d.getClass().getSimpleName());
                    continue;
                }
                EnableUIDefinition ed = (EnableUIDefinition) d;
                boolean enabled = ed.isEnable(parent);
                widget.setEnabled(enabled);
                log("  hook " + ed.getClass().getSimpleName() + ".isEnable(" + parent.gGetShortName()
                        + ") -> " + enabled + ", widget.setEnabled(" + enabled + ")");
                return;
            }
        } catch (Throwable t) {
            log("applyEnableHooks THROW element=" + elementName + " : " + t);
            for (StackTraceElement ste : t.getStackTrace()) {
                log("    at " + ste);
                if (ste.getClassName().contains("Dispatcher")) break;
            }
        }
    }

    public static void reapplyForRelated(GContainer parent,
                                         String changedElement,
                                         Map<GConfigParameter, Control> widgets) {
        if (widgets == null || widgets.isEmpty()) return;
        try {
            int reapplied = 0;
            for (Map.Entry<GConfigParameter, Control> e : widgets.entrySet()) {
                String element = e.getKey().gGetShortName();
                if (element.equals(changedElement)) continue;
                List<IUIDefinition> defs = MetaModelDescriptorParser.getUIDefinitionList(POC_MCU_NAME, element);
                if (defs == null) continue;
                for (IUIDefinition d : defs) {
                    if (!(d instanceof RelatedUIDefinition)) continue;
                    List<String> related = ((RelatedUIDefinition) d).getRelatedUIElementList();
                    if (related != null && related.contains(changedElement)) {
                        applyEnableHooks(parent, element, e.getValue());
                        reapplied++;
                        break;
                    }
                }
            }
            log("reapplyForRelated changed=" + changedElement + " reapplied=" + reapplied);
        } catch (Throwable t) {
            log("reapplyForRelated THROW changed=" + changedElement + " : " + t);
        }
    }

    private static void log(String msg) {
        try {
            Activator a = Activator.getDefault();
            if (a != null) {
                a.getLog().log(new Status(IStatus.INFO, Activator.PLUGIN_ID,
                        "[UIDefinitionDispatcher] " + msg));
            } else {
                System.err.println("[UIDefinitionDispatcher] " + msg);
            }
        } catch (Throwable ignored) {
            System.err.println("[UIDefinitionDispatcher] " + msg);
        }
    }
}

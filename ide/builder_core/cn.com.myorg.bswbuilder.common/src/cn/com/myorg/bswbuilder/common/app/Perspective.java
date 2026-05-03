package cn.com.myorg.bswbuilder.common.app;

import org.eclipse.ui.IFolderLayout;
import org.eclipse.ui.IPageLayout;
import org.eclipse.ui.IPerspectiveFactory;

/**
 * BSW Configurator perspective — overlays Eclipse IDE's standard workbench
 * with a 4-zone layout matching the reference V25.10 (ORIENTAIS) IDE:
 *
 * <pre>
 * +-------------------+--------------------------+
 * | Project Explorer  |   Editor area            |
 * | (Eclipse standard)|   (MemIfModuleManager /  |
 * | (left, ~22%)      |    text editors / etc.)  |
 * |                   |                          |
 * +-------------------+--------------------------+
 * |  Console (BSW Builder)  |  Validation/Detail |
 * |  bottom-left (~25%)     |  bottom-right tabs |
 * +-------------------------+--------------------+
 * </pre>
 *
 * IDE pivot phase 2 (2026-04-30) — replaced our self-rolled
 * {@code AutosarExplorerView} with Eclipse's standard Project Explorer
 * {@code org.eclipse.ui.navigator.ProjectExplorer}; dropped PropertyForm
 * (legacy ViewPart, replaced by MemIfModuleManagerEditor FormEditor).
 */
public class Perspective implements IPerspectiveFactory {

    public static final String PROJECT_EXPLORER_VIEW =
            "org.eclipse.ui.navigator.ProjectExplorer";

    public static final String VALIDATION_VIEW =
            "cn.com.myorg.bswbuilder.ui.views.Validation";

    public static final String DETAIL_VIEW =
            "cn.com.myorg.bswbuilder.ui.views.Detail";

    public static final String CONSOLE_VIEW = "org.eclipse.ui.console.ConsoleView";

    public static final String OUTLINE_VIEW = "org.eclipse.ui.views.ContentOutline";

    public static final String PROPERTIES_VIEW = "org.eclipse.ui.views.PropertySheet";

    @Override
    public void createInitialLayout(IPageLayout layout) {
        String editorArea = layout.getEditorArea();
        layout.setEditorAreaVisible(true);

        // LEFT: Project Explorer (Eclipse 标准 navigator, AUTOSAR-aware via
        // commonNavigator content extensions). 04-30 删了自撸 bswExplorer view
        // 后这里的 AUTOSAR_EXPLORER_VIEW addView 抛 e4 invalid-bundleclass,
        // 整个 perspective layout 退化 — 53 launch 用户看到空白根因.
        IFolderLayout left = layout.createFolder(
                "left", IPageLayout.LEFT, 0.22f, editorArea);
        left.addView(PROJECT_EXPLORER_VIEW);

        // BOTTOM-LEFT: BSW Builder console + Properties (Eclipse standard)
        IFolderLayout bottomLeft = layout.createFolder(
                "bottom-left", IPageLayout.BOTTOM, 0.7f, editorArea);
        bottomLeft.addView(CONSOLE_VIEW);
        bottomLeft.addView(PROPERTIES_VIEW);

        // BOTTOM-RIGHT: Autosar Validation + Detail + Outline
        IFolderLayout bottomRight = layout.createFolder(
                "bottom-right", IPageLayout.RIGHT, 0.55f, "bottom-left");
        bottomRight.addView(VALIDATION_VIEW);
        bottomRight.addView(DETAIL_VIEW);
        bottomRight.addView(OUTLINE_VIEW);

        // Make all views available in Window → Show View
        layout.addShowViewShortcut(PROJECT_EXPLORER_VIEW);
        layout.addShowViewShortcut(VALIDATION_VIEW);
        layout.addShowViewShortcut(DETAIL_VIEW);
        layout.addShowViewShortcut(OUTLINE_VIEW);
        layout.addShowViewShortcut(PROPERTIES_VIEW);
        layout.addShowViewShortcut(CONSOLE_VIEW);
    }
}

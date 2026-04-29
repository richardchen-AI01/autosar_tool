package cn.com.myorg.bswbuilder.common.app;

import org.eclipse.ui.IFolderLayout;
import org.eclipse.ui.IPageLayout;
import org.eclipse.ui.IPerspectiveFactory;

/**
 * EB-tresos / ORIENTAIS V25.10-style 4-zone perspective:
 *
 * <pre>
 * +-------------------+--------------------------+
 * |                   |                          |
 * | Configuration     |   Editor area            |
 * | Editors           |   (Basic Editor /        |
 * | (left, ~22%)      |    Project Settings)     |
 * |                   |                          |
 * |                   +--------------------------+
 * |                   |  Properties (right       |
 * |                   |   ~30% of right zone)    |
 * +-------------------+--------------------------+
 * |  Console (BSW Builder)  |  Validation        |
 * |  bottom (~25% of total) |                    |
 * +-------------------------+--------------------+
 * </pre>
 *
 * View IDs are intentionally referenced as constants here so a single rename
 * in one of the contributing plugins doesn't silently break the layout.
 */
public class Perspective implements IPerspectiveFactory {

    public static final String AUTOSAR_EXPLORER_VIEW =
            "cn.com.myorg.bswbuilder.ui.views.AutosarExplorer";

    public static final String PROPERTY_FORM_VIEW =
            "cn.com.myorg.bswbuilder.ui.views.PropertyForm";

    public static final String VALIDATION_VIEW =
            "cn.com.myorg.bswbuilder.ui.views.Validation";

    public static final String CONSOLE_VIEW = "org.eclipse.ui.console.ConsoleView";

    @Override
    public void createInitialLayout(IPageLayout layout) {
        String editorArea = layout.getEditorArea();
        layout.setEditorAreaVisible(true);

        // LEFT: Configuration Editors (~22%)
        IFolderLayout left = layout.createFolder(
                "left", IPageLayout.LEFT, 0.22f, editorArea);
        left.addView(AUTOSAR_EXPLORER_VIEW);

        // RIGHT: Property form attached to the editor area (~30% of remainder)
        IFolderLayout right = layout.createFolder(
                "right", IPageLayout.RIGHT, 0.65f, editorArea);
        right.addView(PROPERTY_FORM_VIEW);

        // BOTTOM-LEFT: Console (BSW Builder console for bswgen / bswval output)
        IFolderLayout bottomLeft = layout.createFolder(
                "bottom-left", IPageLayout.BOTTOM, 0.7f, editorArea);
        bottomLeft.addView(CONSOLE_VIEW);

        // BOTTOM-RIGHT: Validation
        IFolderLayout bottomRight = layout.createFolder(
                "bottom-right", IPageLayout.RIGHT, 0.55f, "bottom-left");
        bottomRight.addView(VALIDATION_VIEW);

        // Make all views available in Window → Show View
        layout.addShowViewShortcut(AUTOSAR_EXPLORER_VIEW);
        layout.addShowViewShortcut(PROPERTY_FORM_VIEW);
        layout.addShowViewShortcut(VALIDATION_VIEW);
        layout.addShowViewShortcut(CONSOLE_VIEW);
    }
}

package cn.com.myorg.bswbuilder.common.app;

import org.eclipse.ui.IFolderLayout;
import org.eclipse.ui.IPageLayout;
import org.eclipse.ui.IPerspectiveFactory;

public class Perspective implements IPerspectiveFactory {

    public static final String MODULE_NAVIGATOR_VIEW =
            "cn.com.myorg.bswbuilder.ui.views.ModuleNavigator";

    public static final String CONSOLE_VIEW = "org.eclipse.ui.console.ConsoleView";

    @Override
    public void createInitialLayout(IPageLayout layout) {
        String editorArea = layout.getEditorArea();
        layout.setEditorAreaVisible(true);

        // Left: BSW module navigator
        IFolderLayout left = layout.createFolder(
                "left", IPageLayout.LEFT, 0.25f, editorArea);
        left.addView(MODULE_NAVIGATOR_VIEW);

        // Bottom: bswgen / bswval console
        IFolderLayout bottom = layout.createFolder(
                "bottom", IPageLayout.BOTTOM, 0.7f, editorArea);
        bottom.addView(CONSOLE_VIEW);

        // Make views available in Window → Show View
        layout.addShowViewShortcut(MODULE_NAVIGATOR_VIEW);
        layout.addShowViewShortcut(CONSOLE_VIEW);
    }
}

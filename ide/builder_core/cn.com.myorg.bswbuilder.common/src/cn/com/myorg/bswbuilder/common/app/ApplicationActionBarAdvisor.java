package cn.com.myorg.bswbuilder.common.app;

import org.eclipse.jface.action.GroupMarker;
import org.eclipse.jface.action.IMenuManager;
import org.eclipse.jface.action.MenuManager;
import org.eclipse.jface.action.Separator;
import org.eclipse.ui.IWorkbenchActionConstants;
import org.eclipse.ui.IWorkbenchWindow;
import org.eclipse.ui.actions.ActionFactory;
import org.eclipse.ui.actions.ActionFactory.IWorkbenchAction;
import org.eclipse.ui.application.ActionBarAdvisor;
import org.eclipse.ui.application.IActionBarConfigurer;

public class ApplicationActionBarAdvisor extends ActionBarAdvisor {

    private IWorkbenchAction exitAction;
    private IWorkbenchAction aboutAction;

    public ApplicationActionBarAdvisor(IActionBarConfigurer configurer) {
        super(configurer);
    }

    @Override
    protected void makeActions(IWorkbenchWindow window) {
        exitAction = ActionFactory.QUIT.create(window);
        register(exitAction);

        aboutAction = ActionFactory.ABOUT.create(window);
        register(aboutAction);
    }

    @Override
    protected void fillMenuBar(IMenuManager menuBar) {
        // File menu
        MenuManager fileMenu = new MenuManager(
                "&File", IWorkbenchActionConstants.M_FILE);
        fileMenu.add(new Separator());
        fileMenu.add(exitAction);
        menuBar.add(fileMenu);

        // BSW menu — populated by handler extensions in the .ui plugin
        MenuManager bswMenu = new MenuManager(
                "&BSW", "cn.com.myorg.bswbuilder.menu");
        bswMenu.add(new GroupMarker("generators"));
        bswMenu.add(new GroupMarker("validators"));
        bswMenu.add(new GroupMarker(IWorkbenchActionConstants.MB_ADDITIONS));
        menuBar.add(bswMenu);

        // Help menu
        MenuManager helpMenu = new MenuManager(
                "&Help", IWorkbenchActionConstants.M_HELP);
        helpMenu.add(aboutAction);
        menuBar.add(helpMenu);
    }
}

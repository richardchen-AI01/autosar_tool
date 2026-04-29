package cn.com.myorg.bswbuilder.common.app;

import org.eclipse.jface.action.GroupMarker;
import org.eclipse.jface.action.IMenuManager;
import org.eclipse.jface.action.MenuManager;
import org.eclipse.jface.action.Separator;
import org.eclipse.ui.IWorkbenchActionConstants;
import org.eclipse.ui.IWorkbenchWindow;
import org.eclipse.ui.actions.ActionFactory;
import org.eclipse.ui.actions.ActionFactory.IWorkbenchAction;
import org.eclipse.ui.actions.ContributionItemFactory;
import org.eclipse.ui.application.ActionBarAdvisor;
import org.eclipse.ui.application.IActionBarConfigurer;

/**
 * Top menu bar — mirrors ORIENTAIS V25.10 layout
 * (File / Edit / Search / Project / Window / Help) so users with that mental
 * model find the standard Eclipse actions where they expect.
 *
 * <p>Each menu uses Eclipse's {@link ActionFactory} entries (cut / copy /
 * paste / undo / redo / save / save as / quit / about / preferences /
 * find / showView ...) — these are the platform's defaults, no custom
 * implementations needed.
 *
 * <p>The {@code BSW} menu is contributed dynamically by the .ui bundle's
 * plugin.xml {@code menuContribution}, attaching to the
 * {@code cn.com.myorg.bswbuilder.menu} location-URI declared here.
 */
public class ApplicationActionBarAdvisor extends ActionBarAdvisor {

    // File
    private IWorkbenchAction newAction;
    private IWorkbenchAction saveAction;
    private IWorkbenchAction saveAsAction;
    private IWorkbenchAction saveAllAction;
    private IWorkbenchAction closeAction;
    private IWorkbenchAction closeAllAction;
    private IWorkbenchAction exitAction;

    // Edit
    private IWorkbenchAction undoAction;
    private IWorkbenchAction redoAction;
    private IWorkbenchAction cutAction;
    private IWorkbenchAction copyAction;
    private IWorkbenchAction pasteAction;
    private IWorkbenchAction selectAllAction;
    private IWorkbenchAction deleteAction;
    private IWorkbenchAction findAction;
    private IWorkbenchAction prefsAction;

    // Window
    private IWorkbenchAction openPerspectiveAction;
    private IWorkbenchAction maximizeAction;
    private IWorkbenchAction minimizeAction;

    // Help
    private IWorkbenchAction aboutAction;
    private IWorkbenchAction helpContentsAction;

    public ApplicationActionBarAdvisor(IActionBarConfigurer configurer) {
        super(configurer);
    }

    @Override
    protected void makeActions(IWorkbenchWindow window) {
        // File
        newAction      = ActionFactory.NEW.create(window);              register(newAction);
        saveAction     = ActionFactory.SAVE.create(window);             register(saveAction);
        saveAsAction   = ActionFactory.SAVE_AS.create(window);          register(saveAsAction);
        saveAllAction  = ActionFactory.SAVE_ALL.create(window);         register(saveAllAction);
        closeAction    = ActionFactory.CLOSE.create(window);            register(closeAction);
        closeAllAction = ActionFactory.CLOSE_ALL.create(window);        register(closeAllAction);
        exitAction     = ActionFactory.QUIT.create(window);             register(exitAction);

        // Edit
        undoAction      = ActionFactory.UNDO.create(window);            register(undoAction);
        redoAction      = ActionFactory.REDO.create(window);            register(redoAction);
        cutAction       = ActionFactory.CUT.create(window);             register(cutAction);
        copyAction      = ActionFactory.COPY.create(window);            register(copyAction);
        pasteAction     = ActionFactory.PASTE.create(window);           register(pasteAction);
        selectAllAction = ActionFactory.SELECT_ALL.create(window);      register(selectAllAction);
        deleteAction    = ActionFactory.DELETE.create(window);          register(deleteAction);
        findAction      = ActionFactory.FIND.create(window);            register(findAction);
        prefsAction     = ActionFactory.PREFERENCES.create(window);     register(prefsAction);

        // Window
        openPerspectiveAction = ActionFactory.OPEN_PERSPECTIVE_DIALOG.create(window);
        register(openPerspectiveAction);
        maximizeAction = ActionFactory.MAXIMIZE.create(window);         register(maximizeAction);
        minimizeAction = ActionFactory.MINIMIZE.create(window);         register(minimizeAction);

        // Help
        aboutAction         = ActionFactory.ABOUT.create(window);       register(aboutAction);
        helpContentsAction  = ActionFactory.HELP_CONTENTS.create(window); register(helpContentsAction);
    }

    @Override
    protected void fillMenuBar(IMenuManager menuBar) {
        menuBar.add(buildFileMenu());
        menuBar.add(buildEditMenu());
        menuBar.add(buildSearchMenu());
        menuBar.add(buildProjectMenu());
        menuBar.add(buildBswMenu());
        menuBar.add(buildWindowMenu());
        menuBar.add(buildHelpMenu());
    }

    private MenuManager buildFileMenu() {
        MenuManager m = new MenuManager("&File", IWorkbenchActionConstants.M_FILE);
        m.add(newAction);
        m.add(new Separator());
        m.add(saveAction);
        m.add(saveAsAction);
        m.add(saveAllAction);
        m.add(new Separator());
        m.add(closeAction);
        m.add(closeAllAction);
        m.add(new Separator());
        m.add(new GroupMarker(IWorkbenchActionConstants.MB_ADDITIONS));
        m.add(new Separator());
        m.add(exitAction);
        return m;
    }

    private MenuManager buildEditMenu() {
        MenuManager m = new MenuManager("&Edit", IWorkbenchActionConstants.M_EDIT);
        m.add(undoAction);
        m.add(redoAction);
        m.add(new Separator());
        m.add(cutAction);
        m.add(copyAction);
        m.add(pasteAction);
        m.add(new Separator());
        m.add(deleteAction);
        m.add(selectAllAction);
        m.add(new Separator());
        m.add(findAction);
        m.add(new Separator());
        m.add(new GroupMarker(IWorkbenchActionConstants.MB_ADDITIONS));
        m.add(new Separator());
        m.add(prefsAction);
        return m;
    }

    private MenuManager buildSearchMenu() {
        MenuManager m = new MenuManager("&Search", IWorkbenchActionConstants.M_NAVIGATE);
        m.add(new GroupMarker(IWorkbenchActionConstants.MB_ADDITIONS));
        return m;
    }

    private MenuManager buildProjectMenu() {
        MenuManager m = new MenuManager("&Project", "project");
        m.add(new GroupMarker(IWorkbenchActionConstants.MB_ADDITIONS));
        return m;
    }

    private MenuManager buildBswMenu() {
        MenuManager m = new MenuManager("&BSW", "cn.com.myorg.bswbuilder.menu");
        m.add(new GroupMarker("generators"));
        m.add(new GroupMarker("validators"));
        m.add(new Separator());
        m.add(new GroupMarker(IWorkbenchActionConstants.MB_ADDITIONS));
        return m;
    }

    private MenuManager buildWindowMenu() {
        MenuManager m = new MenuManager("&Window", IWorkbenchActionConstants.M_WINDOW);
        m.add(openPerspectiveAction);

        MenuManager showViewSubmenu = new MenuManager("Show &View", "showView");
        showViewSubmenu.add(ContributionItemFactory.VIEWS_SHORTLIST.create(
                getActionBarConfigurer().getWindowConfigurer().getWindow()));
        m.add(showViewSubmenu);

        m.add(new Separator());
        m.add(maximizeAction);
        m.add(minimizeAction);
        m.add(new Separator());
        m.add(new GroupMarker(IWorkbenchActionConstants.MB_ADDITIONS));
        m.add(new Separator());
        m.add(prefsAction);
        return m;
    }

    private MenuManager buildHelpMenu() {
        MenuManager m = new MenuManager("&Help", IWorkbenchActionConstants.M_HELP);
        m.add(helpContentsAction);
        m.add(new Separator());
        m.add(new GroupMarker(IWorkbenchActionConstants.MB_ADDITIONS));
        m.add(new Separator());
        m.add(aboutAction);
        return m;
    }
}

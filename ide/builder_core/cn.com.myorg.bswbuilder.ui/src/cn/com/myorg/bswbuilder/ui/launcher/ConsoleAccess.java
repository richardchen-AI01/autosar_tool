package cn.com.myorg.bswbuilder.ui.launcher;

import org.eclipse.ui.console.ConsolePlugin;
import org.eclipse.ui.console.IConsole;
import org.eclipse.ui.console.IConsoleManager;
import org.eclipse.ui.console.MessageConsole;

/**
 * Shared accessor for the "BSW Builder" output console — finds-or-creates a
 * single MessageConsole so generator and validator runs interleave in the
 * same view.
 */
public final class ConsoleAccess {

    public static final String CONSOLE_NAME = "BSW Builder";

    private ConsoleAccess() {}

    public static MessageConsole getConsole() {
        IConsoleManager manager = ConsolePlugin.getDefault().getConsoleManager();
        for (IConsole c : manager.getConsoles()) {
            if (CONSOLE_NAME.equals(c.getName()) && c instanceof MessageConsole mc) {
                return mc;
            }
        }
        MessageConsole created = new MessageConsole(CONSOLE_NAME, null);
        manager.addConsoles(new IConsole[]{created});
        return created;
    }

    /** Bring the console view forward and select our console. */
    public static void show(MessageConsole console) {
        ConsolePlugin.getDefault().getConsoleManager().showConsoleView(console);
    }
}

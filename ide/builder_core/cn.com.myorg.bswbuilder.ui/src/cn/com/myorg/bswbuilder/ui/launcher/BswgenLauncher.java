package cn.com.myorg.bswbuilder.ui.launcher;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.ui.console.MessageConsole;
import org.eclipse.ui.console.MessageConsoleStream;

/**
 * Glue between the Eclipse IDE and the Python bswgen / bswval CLIs.
 *
 * <p>Invocation strategy (in priority order):
 * <ol>
 *   <li>{@code build/dist/bswgen} or {@code build/dist/bswgen.exe} if PyInstaller
 *       has been run.
 *   <li>Otherwise {@code python3 -m generator …} from source against the repo
 *       root, with {@code PYTHONPATH=core}.
 * </ol>
 *
 * <p>The repo root is found by walking up from the running plugin's
 * {@code Bundle-RootPath} until a {@code generator/__main__.py} is sighted.
 * For dev launches the repo root is the cwd of the Eclipse process.
 */
public final class BswgenLauncher {

    public enum Tool {
        BSWGEN("bswgen", "generator"),
        BSWVAL("bswval", "validator");

        final String binaryName;
        final String pythonModule;

        Tool(String binaryName, String pythonModule) {
            this.binaryName = binaryName;
            this.pythonModule = pythonModule;
        }
    }

    private BswgenLauncher() {}

    /**
     * Run the requested CLI synchronously, streaming combined stdout+stderr
     * into the supplied console stream.
     *
     * @return the process exit code (0 on success).
     */
    public static int run(Tool tool, List<String> extraArgs,
                          MessageConsole console,
                          IProgressMonitor monitor) throws IOException {
        Path repoRoot = locateRepoRoot();
        List<String> command = buildCommand(tool, repoRoot, extraArgs);

        try (MessageConsoleStream out = console.newMessageStream()) {
            out.println("$ " + String.join(" ", command));
            out.println("(working directory: " + repoRoot + ")");
            ProcessBuilder pb = new ProcessBuilder(command);
            pb.directory(repoRoot.toFile());
            pb.redirectErrorStream(true);
            // For source-mode: PYTHONPATH=core
            pb.environment().merge("PYTHONPATH", repoRoot.resolve("core").toString(),
                    (existing, ours) -> ours + File.pathSeparator + existing);

            Process p = pb.start();
            try (BufferedReader r = new BufferedReader(
                    new InputStreamReader(p.getInputStream(), StandardCharsets.UTF_8))) {
                String line;
                while ((line = r.readLine()) != null) {
                    if (monitor != null && monitor.isCanceled()) {
                        p.destroy();
                        out.println("[CANCELLED]");
                        return -1;
                    }
                    out.println(line);
                }
            }
            try {
                int exit = p.waitFor();
                out.println("[exit " + exit + "]");
                return exit;
            } catch (InterruptedException ie) {
                Thread.currentThread().interrupt();
                out.println("[INTERRUPTED]");
                return -2;
            }
        }
    }

    /** Build the command line, preferring the PyInstaller bundle if present. */
    private static List<String> buildCommand(Tool tool, Path repoRoot, List<String> extraArgs) {
        List<String> cmd = new ArrayList<>();
        Path binary = pickBinary(repoRoot, tool);
        if (binary != null) {
            cmd.add(binary.toString());
        } else {
            // Source mode
            cmd.add(System.getProperty("os.name").toLowerCase().contains("win")
                    ? "python" : "python3");
            cmd.add("-m");
            cmd.add(tool.pythonModule);
        }
        cmd.addAll(extraArgs);
        return cmd;
    }

    private static Path pickBinary(Path repoRoot, Tool tool) {
        boolean win = System.getProperty("os.name").toLowerCase().contains("win");
        String name = win ? tool.binaryName + ".exe" : tool.binaryName;
        Path candidate = repoRoot.resolve("build").resolve("dist").resolve(name);
        return Files.isExecutable(candidate) ? candidate : null;
    }

    /**
     * Walk up from the Eclipse process cwd until a directory containing both
     * {@code generator/__main__.py} and {@code core/Common/} is found. That is
     * the autosar_tool repo root.
     */
    private static Path locateRepoRoot() throws IOException {
        Path cwd = Paths.get(System.getProperty("user.dir")).toAbsolutePath();
        Path probe = cwd;
        while (probe != null) {
            if (Files.isRegularFile(probe.resolve("generator/__main__.py"))
                    && Files.isDirectory(probe.resolve("core/Common"))) {
                return probe;
            }
            probe = probe.getParent();
        }
        // Fallback to cwd; user can override via -Dautosar.repoRoot=…
        String override = System.getProperty("autosar.repoRoot");
        if (override != null) {
            return Paths.get(override);
        }
        throw new IOException("Cannot locate autosar_tool repo root from cwd=" + cwd
                + ". Pass -Dautosar.repoRoot=<path> in the launch config.");
    }

    public static IStatus errorStatus(String pluginId, String msg, Throwable t) {
        return new Status(IStatus.ERROR, pluginId, msg, t);
    }
}

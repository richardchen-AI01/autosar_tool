package cn.com.myorg.bswbuilder.ui.views;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

import org.eclipse.jface.layout.GridDataFactory;
import org.eclipse.jface.layout.GridLayoutFactory;
import org.eclipse.jface.resource.JFaceResources;
import org.eclipse.swt.SWT;
import org.eclipse.swt.events.ModifyListener;
import org.eclipse.swt.events.MouseAdapter;
import org.eclipse.swt.events.MouseEvent;
import org.eclipse.swt.events.MouseListener;
import org.eclipse.swt.events.MouseTrackAdapter;
import org.eclipse.swt.events.MouseTrackListener;
import org.eclipse.swt.graphics.Color;
import org.eclipse.swt.graphics.Font;
import org.eclipse.swt.graphics.FontData;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Control;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.FileDialog;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.swt.widgets.Text;
import org.eclipse.ui.part.ViewPart;
import org.eclipse.jface.dialogs.MessageDialog;

import cn.com.myorg.bswbuilder.modules.memif.data.MemIfArxmlReader;
import cn.com.myorg.bswbuilder.modules.memif.data.MemIfData;

/**
 * Configuration Editors view — EB tresos / ORIENTAIS V25.10-style left panel.
 *
 * <p>Layout (top to bottom):
 * <ol>
 *   <li>Filter input field
 *   <li>Categorised, collapsible list of BSW modules:
 *       <ul>
 *         <li>Base Services</li>
 *         <li>Communication</li>
 *         <li>Diagnostics</li>
 *         <li>I/O</li>
 *         <li>Memory</li>
 *         <li>Mode Management</li>
 *         <li>Network Management</li>
 *         <li>Runtime System</li>
 *       </ul>
 *   <li>Bottom tabs: "Basic Editor" / "Properties" (placeholder for v0.2)
 * </ol>
 *
 * <p>v0.1: static category map (mirrors AUTOSAR R23-11 BSW partition).
 * v0.2 will build the list dynamically from a workspace's loaded ECUC modules.
 */
public class ConfigurationEditorsView extends ViewPart {

    public static final String ID =
            "cn.com.myorg.bswbuilder.ui.views.ConfigurationEditors";

    private static final Color BG_WHITE = new Color(Display.getDefault(), 255, 255, 255);
    private static final Color CATEGORY_BLUE = new Color(Display.getDefault(), 33, 91, 152);
    private static final Color CATEGORY_HOVER = new Color(Display.getDefault(), 230, 240, 250);
    private static final Color SEPARATOR = new Color(Display.getDefault(), 220, 220, 220);
    private static final Color MODULE_FG = new Color(Display.getDefault(), 50, 50, 50);

    private Text filterText;
    private Composite categoryArea;
    private final List<CategorySection> sections = new ArrayList<>();

    /** AUTOSAR R23-11 BSW module → category map (mirrors the reference UI). */
    private static final Map<String, String[]> CATEGORIES = new LinkedHashMap<>();
    static {
        CATEGORIES.put("Base Services",
                new String[]{"Det", "EcuM", "BswM", "Os", "MemMap"});
        CATEGORIES.put("Communication",
                new String[]{"Com", "ComM", "PduR", "CanIf", "CanTp", "CanSM",
                             "CanNm", "Nm", "Can", "Xfrm"});
        CATEGORIES.put("Diagnostics",
                new String[]{"Dem", "Dcm", "Crc"});
        CATEGORIES.put("I/O",
                new String[]{"Dio", "Port", "Mcu", "Gpt", "Wdg", "WdgIf"});
        CATEGORIES.put("Memory",
                new String[]{"MemIf ✓", "Fee", "NvM", "Ea"});
        CATEGORIES.put("Mode Management",
                new String[]{"BswM (Modes)"});
        CATEGORIES.put("Network Management",
                new String[]{"Nm", "CanNm"});
        CATEGORIES.put("Runtime System",
                new String[]{"iRte"});
    }

    @Override
    public void createPartControl(Composite parent) {
        parent.setBackground(BG_WHITE);
        GridLayoutFactory.fillDefaults().margins(0, 0).spacing(0, 0).applyTo(parent);

        // ---- Header strip ----
        Label header = new Label(parent, SWT.NONE);
        header.setText("  Configuration Editors");
        header.setBackground(BG_WHITE);
        header.setForeground(CATEGORY_BLUE);
        header.setFont(boldFont(parent, 11));
        GridDataFactory.fillDefaults()
                .grab(true, false)
                .indent(0, 6)
                .applyTo(header);

        // ---- Filter field ----
        filterText = new Text(parent, SWT.BORDER | SWT.SEARCH | SWT.ICON_SEARCH);
        filterText.setMessage("<Filter>");
        filterText.setBackground(BG_WHITE);
        GridDataFactory.fillDefaults()
                .grab(true, false)
                .indent(6, 4)
                .hint(SWT.DEFAULT, 22)
                .applyTo(filterText);

        // ---- Scrollable category area ----
        categoryArea = new Composite(parent, SWT.NONE);
        categoryArea.setBackground(BG_WHITE);
        GridLayoutFactory.fillDefaults().numColumns(1).margins(0, 0).spacing(0, 0)
                .applyTo(categoryArea);
        GridDataFactory.fillDefaults().grab(true, true).applyTo(categoryArea);

        for (Map.Entry<String, String[]> e : CATEGORIES.entrySet()) {
            sections.add(new CategorySection(categoryArea, e.getKey(), e.getValue()));
        }

        // ---- Bottom: tab strip (placeholder) ----
        Composite tabStrip = new Composite(parent, SWT.NONE);
        tabStrip.setBackground(BG_WHITE);
        GridLayoutFactory.fillDefaults().numColumns(2).margins(8, 4).spacing(12, 0)
                .applyTo(tabStrip);
        GridDataFactory.fillDefaults().grab(true, false).applyTo(tabStrip);

        Label basicTab = new Label(tabStrip, SWT.NONE);
        basicTab.setText("Basic Editor");
        basicTab.setForeground(CATEGORY_BLUE);
        basicTab.setFont(JFaceResources.getFontRegistry().getBold(JFaceResources.DEFAULT_FONT));
        basicTab.setBackground(BG_WHITE);

        Label propsTab = new Label(tabStrip, SWT.NONE);
        propsTab.setText("Properties");
        propsTab.setForeground(MODULE_FG);
        propsTab.setBackground(BG_WHITE);

        // Wire filter
        ModifyListener applyFilter = e -> applyFilter(filterText.getText());
        filterText.addModifyListener(applyFilter);
    }

    private void applyFilter(String query) {
        String q = (query == null) ? "" : query.trim().toLowerCase(Locale.ROOT);
        for (CategorySection s : sections) {
            s.applyFilter(q);
        }
        categoryArea.layout(true, true);
    }

    @Override
    public void setFocus() {
        if (filterText != null) {
            filterText.setFocus();
        }
    }

    private static Font boldFont(Control widget, int size) {
        FontData[] data = widget.getFont().getFontData();
        for (FontData fd : data) {
            fd.setHeight(size);
            fd.setStyle(SWT.BOLD);
        }
        return new Font(widget.getDisplay(), data);
    }

    /**
     * One collapsible category. Header (bold blue) + chevron + N module rows.
     * Click header → toggles expanded state.
     */
    private static final class CategorySection {
        private final Composite root;
        private final Composite headerRow;
        private final Label chevron;
        private final Label title;
        private final Composite moduleArea;
        private final List<Label> moduleLabels = new ArrayList<>();
        private boolean expanded;

        CategorySection(Composite parent, String categoryName, String[] modules) {
            root = new Composite(parent, SWT.NONE);
            root.setBackground(BG_WHITE);
            GridLayoutFactory.fillDefaults().margins(0, 0).spacing(0, 0).applyTo(root);
            GridDataFactory.fillDefaults().grab(true, false).applyTo(root);

            // Header row: chevron + bold name
            headerRow = new Composite(root, SWT.NONE);
            headerRow.setBackground(BG_WHITE);
            GridLayoutFactory.fillDefaults().numColumns(2).margins(8, 4).spacing(4, 0)
                    .applyTo(headerRow);
            GridDataFactory.fillDefaults().grab(true, false).applyTo(headerRow);

            chevron = new Label(headerRow, SWT.NONE);
            chevron.setText("▸"); // right-pointing triangle ▸
            chevron.setForeground(CATEGORY_BLUE);
            chevron.setBackground(BG_WHITE);

            title = new Label(headerRow, SWT.NONE);
            title.setText(categoryName);
            title.setForeground(CATEGORY_BLUE);
            title.setBackground(BG_WHITE);
            title.setFont(JFaceResources.getFontRegistry()
                    .getBold(JFaceResources.DEFAULT_FONT));
            GridDataFactory.fillDefaults().grab(true, false).applyTo(title);

            // Hover effect (mouseEnter/Exit are on MouseTrackListener, not
            // MouseListener). Apply to all 3 header sub-widgets so dragging
            // across them keeps the hover-on color.
            MouseTrackListener hover = new MouseTrackAdapter() {
                @Override public void mouseEnter(MouseEvent e) {
                    headerRow.setBackground(CATEGORY_HOVER);
                    chevron.setBackground(CATEGORY_HOVER);
                    title.setBackground(CATEGORY_HOVER);
                }
                @Override public void mouseExit(MouseEvent e) {
                    headerRow.setBackground(BG_WHITE);
                    chevron.setBackground(BG_WHITE);
                    title.setBackground(BG_WHITE);
                }
            };
            headerRow.addMouseTrackListener(hover);
            chevron.addMouseTrackListener(hover);
            title.addMouseTrackListener(hover);

            // Click toggles expansion
            MouseListener click = new MouseAdapter() {
                @Override public void mouseUp(MouseEvent e) {
                    setExpanded(!expanded);
                }
            };
            headerRow.addMouseListener(click);
            chevron.addMouseListener(click);
            title.addMouseListener(click);

            // Separator under header
            Label sep = new Label(root, SWT.SEPARATOR | SWT.HORIZONTAL);
            sep.setBackground(SEPARATOR);
            GridDataFactory.fillDefaults().grab(true, false).applyTo(sep);

            // Module list (initially collapsed → exclude from layout)
            moduleArea = new Composite(root, SWT.NONE);
            moduleArea.setBackground(BG_WHITE);
            GridLayoutFactory.fillDefaults().numColumns(1).margins(24, 4).spacing(0, 4)
                    .applyTo(moduleArea);
            GridData moduleAreaLD = new GridData(SWT.FILL, SWT.TOP, true, false);
            moduleAreaLD.exclude = true;
            moduleArea.setLayoutData(moduleAreaLD);

            for (String m : modules) {
                Label l = new Label(moduleArea, SWT.NONE);
                l.setText("• " + m);
                l.setForeground(MODULE_FG);
                l.setBackground(BG_WHITE);
                // Each module label gets its own GridData so we can flip
                // .exclude on it during filter.
                GridDataFactory.fillDefaults().grab(true, false).applyTo(l);
                moduleLabels.add(l);

                // Phase A: only MemIf is wired. Click → file dialog → load
                // ARXML → populate PropertyFormView. Other modules ignore
                // clicks until each gets its own data layer.
                if (m.startsWith("MemIf")) {
                    l.addMouseListener(new MouseAdapter() {
                        @Override public void mouseUp(MouseEvent e) {
                            openMemIfFromUser(l.getShell());
                        }
                    });
                    l.addMouseTrackListener(new MouseTrackAdapter() {
                        @Override public void mouseEnter(MouseEvent e) {
                            l.setBackground(CATEGORY_HOVER);
                        }
                        @Override public void mouseExit(MouseEvent e) {
                            l.setBackground(BG_WHITE);
                        }
                    });
                }
            }

            expanded = false;
        }

        /**
         * Phase A flow: ask the user for an ARXML file via {@link FileDialog},
         * load it via {@link MemIfArxmlReader}, push the result into
         * {@link PropertyFormView#showAndPopulate(MemIfData)}.
         */
        private static void openMemIfFromUser(Shell shell) {
            FileDialog dialog = new FileDialog(shell, SWT.OPEN);
            dialog.setFilterExtensions(new String[] { "*.arxml" });
            dialog.setText("Select a MemIf ARXML (e.g. samples/Demo_S32K148/.../MemIf.arxml)");
            String path = dialog.open();
            if (path == null) {
                return;
            }
            try {
                MemIfData data = MemIfArxmlReader.read(path);
                PropertyFormView.showAndPopulate(data);
            } catch (Throwable t) {
                t.printStackTrace();
                MessageDialog.openError(shell, "MemIf ARXML load failed",
                        t.getClass().getSimpleName() + ": " + t.getMessage());
            }
        }

        void setExpanded(boolean exp) {
            this.expanded = exp;
            chevron.setText(exp ? "▾" /* ▾ */ : "▸" /* ▸ */);
            ((GridData) moduleArea.getLayoutData()).exclude = !exp;
            moduleArea.setVisible(exp);
            root.requestLayout();
        }

        void applyFilter(String q) {
            boolean anyMatch = false;
            for (Label l : moduleLabels) {
                String text = l.getText().toLowerCase(Locale.ROOT);
                boolean match = q.isEmpty() || text.contains(q);
                Object ld = l.getLayoutData();
                if (ld instanceof GridData gd) {
                    gd.exclude = !match;
                }
                l.setVisible(match);
                if (match) anyMatch = true;
            }
            // Auto-expand category when filter has hits
            if (!q.isEmpty() && anyMatch) {
                setExpanded(true);
            }
        }
    }
}

package cn.com.myorg.bswbuilder.ui.views;

import org.eclipse.ui.navigator.CommonNavigator;

/**
 * AUTOSAR Explorer view, registered as
 * {@code cn.com.myorg.bswbuilder.ui.bswExplorer}. Thin subclass of Eclipse's
 * public {@link CommonNavigator} — all rendering comes from navigator content
 * extensions wired via {@code org.eclipse.ui.navigator.viewer} in
 * {@code plugin.xml}:
 * <ul>
 *   <li>{@code org.eclipse.ui.navigator.resourceContent} — standard workspace
 *       project / file tree (Eclipse public)</li>
 *   <li>{@code cn.com.myorg.bswbuilder.ui.arxmlContent} — drill into .arxml
 *       file's AR-PACKAGE / Identifiable hierarchy via Sphinx
 *       {@code BasicExplorerContentProvider} + {@code BasicExplorerLabelProvider}
 *       (org.eclipse.sphinx.emf.explorer, Eclipse-licensed open source)</li>
 * </ul>
 */
public class BswExplorerView extends CommonNavigator {
}

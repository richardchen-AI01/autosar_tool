package cn.com.myorg.bswbuilder.ui.navigator;

import org.eclipse.jface.viewers.ITreeContentProvider;
import org.eclipse.sphinx.emf.explorer.BasicExplorerContentProvider;

/**
 * AUTOSAR Explorer content provider — placeholder.
 *
 * <p>2026-05-01: AUTOSAR Explorer's content (IResource walk) is now provided
 * by Eclipse's standard {@code org.eclipse.ui.navigator.resourceContent}
 * (bound as {@code isRoot="true"} in viewerContentBinding) — same arrangement
 * as reference V25.10 ({@code cn.com.isoft.pal.views.autosarexplorer}).
 *
 * <p>This class survives so the {@code bswNavigatorContent} extension still
 * has a content provider class (CommonNavigator framework requires one).
 * It contributes no children — children come from resourceContent. The
 * value-add of our navigatorContent is purely the {@link BswExplorerLabelProvider}
 * (strip {@code .arxml}, module icon, etc.).
 *
 * <p>Reference's CustomExplorerContentProvider DID contribute children
 * (IProject → BswBuilderModel bridge) for model overlay; we don't currently
 * need that since the file system already shows everything.
 */
public class BswExplorerContentProvider
        extends BasicExplorerContentProvider
        implements ITreeContentProvider {

    @Override
    public Object[] getChildren(Object parentElement) {
        return new Object[0];
    }

    @Override
    public Object[] getElements(Object inputElement) {
        return new Object[0];
    }

    @Override
    public boolean hasChildren(Object element) {
        return false;
    }

    @Override
    public Object getParent(Object element) {
        return null;
    }
}

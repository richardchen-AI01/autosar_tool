package cn.com.myorg.bswbuilder.ui.contentviewers;

import gautosar.gecucdescription.GContainer;
import gautosar.gecucparameterdef.GContainerDef;

/**
 * Table-row data wrapper used by detail-side TableViewer to represent a single
 * row when the master selection is a folder ({@link TreeChildWrap} or
 * {@link ChildContainerGroup}).
 *
 * <p>跟参考 V25.10 {@code cn.com.isoft.bswbuilder.ui.contentviewers.TableDataContainer}
 * 同款 — table 行行项 element, 含 row 对应的 instance container + def。
 *
 * <p>用途: detail TableViewer.setInput(group); group.getElementList() →
 * 给每个 GContainer 包一个 TableDataContainer 作 row element, 让
 * SelectionChangedListener 能区分 "selected a row in table" vs
 * "selected a node in master tree"。
 */
public class TableDataContainer {

    private final GContainer parentContainer;
    private final GContainerDef containerDef;

    public TableDataContainer(GContainer parentContainer, GContainerDef containerDef) {
        this.parentContainer = parentContainer;
        this.containerDef = containerDef;
    }

    public GContainer getParentContainer() { return parentContainer; }
    public GContainerDef getContainerDef() { return containerDef; }

    @Override public int hashCode() {
        int h = 31 + (containerDef == null ? 0 : containerDef.hashCode());
        return 31 * h + (parentContainer == null ? 0 : parentContainer.hashCode());
    }

    @Override public boolean equals(Object other) {
        if (this == other) return true;
        if (!(other instanceof TableDataContainer)) return false;
        TableDataContainer o = (TableDataContainer) other;
        if (containerDef == null ? o.containerDef != null : !containerDef.equals(o.containerDef)) return false;
        return parentContainer == null ? o.parentContainer == null : parentContainer.equals(o.parentContainer);
    }
}

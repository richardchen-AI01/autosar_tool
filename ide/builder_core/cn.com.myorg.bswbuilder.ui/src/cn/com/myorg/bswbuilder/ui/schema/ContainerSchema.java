package cn.com.myorg.bswbuilder.ui.schema;

import java.util.Collections;
import java.util.List;

/**
 * ECUC container definition — read from {@code <Module>Def.arxml}.
 *
 * <p>Drives editor page selection (跟参考 V25.10 NewBswBuilderEditor.addPages
 * 同思路):
 * <ul>
 *   <li>{@link #generalFlag} == true → 单实例容器, 用 GenericGeneralFormPage
 *   <li>{@link #generalFlag} == false → 多实例容器, 用 GenericMasterDetailFormPage
 * </ul>
 *
 * <p>Container 嵌套 (subContainers) 在 NvMBlockDescriptor 这种里很常见 — 比如
 * NvMBlockDescriptor 下有 NvMTargetBlockReference (CHOICE-CONTAINER) 嵌套
 * NvMFeeRef / NvMEaRef。
 */
public final class ContainerSchema {

    public final String shortName;        // SHORT-NAME (e.g. "NvMBlockDescriptor")
    public final String description;      // DESC/L-2 (may be null)
    public final long lowerMultiplicity;
    public final long upperMultiplicity;  // * → -1

    /** GENERAL_FLAG iSoft option (跟参考 V25.10 同 driving signal). */
    public final boolean generalFlag;

    /** True for ECUC-CHOICE-CONTAINER-DEF (e.g. NvMTargetBlockReference 二选一). */
    public final boolean choiceContainer;

    public final List<ParamSchema> params;
    public final List<ContainerSchema> subContainers;

    public ContainerSchema(String shortName, String description,
                           long lowerMultiplicity, long upperMultiplicity,
                           boolean generalFlag, boolean choiceContainer,
                           List<ParamSchema> params, List<ContainerSchema> subContainers) {
        this.shortName = shortName;
        this.description = description;
        this.lowerMultiplicity = lowerMultiplicity;
        this.upperMultiplicity = upperMultiplicity;
        this.generalFlag = generalFlag;
        this.choiceContainer = choiceContainer;
        this.params = params == null
                ? Collections.<ParamSchema>emptyList()
                : Collections.unmodifiableList(params);
        this.subContainers = subContainers == null
                ? Collections.<ContainerSchema>emptyList()
                : Collections.unmodifiableList(subContainers);
    }

    /** True iff this container can have multiple instances (upperMultiplicity > 1 or unbounded). */
    public boolean isMultiInstance() {
        return upperMultiplicity == -1 || upperMultiplicity > 1;
    }

    /**
     * Page-picker decision: single-instance (or explicit GENERAL_FLAG) → General page;
     * multi-instance → Master-Detail. Reference V25.10 only checks GENERAL_FLAG SDG;
     * our def files don't carry that option so we fall back to {@code !isMultiInstance()}
     * which gives equivalent behavior on the modules we ship (MemIfGeneral / NvMCommon
     * 都是 [1..1], NvMBlockDescriptor [1..65536] 跑 master-detail).
     */
    public boolean useGeneralPage() {
        return generalFlag || !isMultiInstance();
    }
}

package cn.com.myorg.bswbuilder.ui.schema;

import java.util.Collections;
import java.util.List;

/**
 * Single ECUC parameter definition — read from {@code <Module>Def.arxml}.
 * Drives widget rendering in {@code GenericGeneralFormPage} (E5-2).
 */
public final class ParamSchema {

    public final String shortName;          // SHORT-NAME (e.g. "NvMBlockUseCrc")
    public final ParamType type;
    public final String description;        // DESC/L-2 (English text, may be null)
    public final String defaultValue;       // DEFAULT-VALUE (may be null)
    public final long lowerMultiplicity;    // LOWER-MULTIPLICITY (default 1)
    public final long upperMultiplicity;    // UPPER-MULTIPLICITY (default 1, * = -1)

    // Numeric only: MIN / MAX literal text. null when N/A.
    public final String minValue;
    public final String maxValue;

    // ENUMERATION only: literal short-names. Empty list otherwise.
    public final List<String> enumLiterals;

    // REFERENCE / FOREIGN_REFERENCE / CHOICE_REFERENCE only:
    //   destination param def path, e.g. "/AUTOSAR/Fee/FeeBlockConfiguration".
    public final String destinationRef;

    public ParamSchema(String shortName, ParamType type, String description,
                       String defaultValue, long lowerMultiplicity, long upperMultiplicity,
                       String minValue, String maxValue,
                       List<String> enumLiterals, String destinationRef) {
        this.shortName = shortName;
        this.type = type;
        this.description = description;
        this.defaultValue = defaultValue;
        this.lowerMultiplicity = lowerMultiplicity;
        this.upperMultiplicity = upperMultiplicity;
        this.minValue = minValue;
        this.maxValue = maxValue;
        this.enumLiterals = enumLiterals == null
                ? Collections.<String>emptyList()
                : Collections.unmodifiableList(enumLiterals);
        this.destinationRef = destinationRef;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder()
                .append(shortName)
                .append(": ")
                .append(type);
        if (defaultValue != null) sb.append(" =").append(defaultValue);
        if (minValue != null || maxValue != null)
            sb.append(" [").append(minValue).append("..").append(maxValue).append(']');
        if (!enumLiterals.isEmpty())
            sb.append(" {").append(String.join(",", enumLiterals)).append('}');
        if (destinationRef != null) sb.append(" → ").append(destinationRef);
        return sb.toString();
    }
}

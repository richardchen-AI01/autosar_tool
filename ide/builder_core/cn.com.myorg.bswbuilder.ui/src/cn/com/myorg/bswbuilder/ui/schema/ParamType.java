package cn.com.myorg.bswbuilder.ui.schema;

/**
 * ECUC parameter primitive type (one per AUTOSAR parameter definition).
 * Reference: standard {@code ECUC-*-PARAM-DEF} elements in AUTOSAR ECUC schema.
 */
public enum ParamType {
    BOOLEAN,           // ECUC-BOOLEAN-PARAM-DEF       → checkbox widget
    INTEGER,           // ECUC-INTEGER-PARAM-DEF       → text + spinner (with min/max)
    FLOAT,             // ECUC-FLOAT-PARAM-DEF         → text (with min/max)
    STRING,            // ECUC-STRING-PARAM-DEF        → text
    ENUMERATION,       // ECUC-ENUMERATION-PARAM-DEF   → combo (literals from schema)
    REFERENCE,         // ECUC-REFERENCE-DEF           → browse button + chooser dialog
    FOREIGN_REFERENCE, // ECUC-FOREIGN-REFERENCE-DEF   → 同 reference 但跨模块
    CHOICE_REFERENCE   // ECUC-CHOICE-REFERENCE-DEF    → 选 N 中之一类型的 ref
}

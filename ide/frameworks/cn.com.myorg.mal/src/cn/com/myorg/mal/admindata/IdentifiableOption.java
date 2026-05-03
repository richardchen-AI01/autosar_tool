package cn.com.myorg.mal.admindata;

import autosar40.genericstructure.generaltemplateclasses.identifiable.Identifiable;

/**
 * 99% paraphrase of cn.com.isoft.mal.admindata.IdentifiableOption (53 lines).
 * Reads/writes "iSoft::IdentifiableOptions" SDG on Identifiable's AdminData.
 *
 * <p>SDG GID kept as "iSoft::IdentifiableOptions" because MEN NvMDef.arxml
 * already contains SDGs with this GID (33 grep matches) — changing it would
 * break loading existing .arxml.
 */
public class IdentifiableOption extends ArccoreOption {
    public static final String GID_IdentifiableOption = "iSoft::IdentifiableOptions";
    public static final String OPT_ISOFT_COMMENT = "@ISOFT_COMMENT";
    public static final String GENERAL_FLAG = "GENERAL_FLAG";
    public static final String HIDE_FLAG = "HIDE_FLAG";
    public static final String DISABLE_FLAG = "DISABLE_FLAG";
    public static final String TWISTIE_FLAG = "TWISTIE_FLAG";
    public static final String UPPER_LAYER_FLAG = "UPPER_LAYER_FLAG";
    public static final String DERIVED_FLAG = "DERIVED_FLAG";
    public static final String HEX_DISPLAY_FLAG = "HEX_DISPLAY_FLAG";
    public static final String FIX_FLAG = "FIX_FLAG";
    public static final String TRIGGER_FLAG = "TRIGGER_FLAG";
    public static final String ENABLE_EXCEPTION_FLAG = "ENABLE_EXCEPTION_FLAG";
    public static final String TABLE_FLAG = "TABLE_FLAG";
    public static final String TABLE_SPC_FLAG = "TABLE_SPC_FLAG";
    public static final String REPET_FLAG = "REPET_FLAG";
    public static final String RESERVED_FLAG = "RESERVED_FLAG";
    public static final String CONTROL_NAME = "CONTROL_NAME";
    public static final String PARENT_LEVEL = "PARENT_LEVEL";
    public static final String ORDER_NO = "ORDER_NO";
    public static final String USER_SELFDEFINEd = "USER_SELFDEFINEd";
    public static final String GROUP_NAME = "GROUP_NAME";
    public static final String CONACTION_FLAG = "CONACTION_FLAG";
    public static final String ACTION_FLAG = "ACTION_FLAG";
    public static final String NEW_CHOICE_CONTAINER_FLAG = "NEW_CHOICE_CONTAINER_FLAG";
    public static final String ACTION_NAME = "ACTION_NAME";
    public static final String USER_DEFINED_FLAG = "USER_DEFINED_FLAG";
    public static final String SYNC_FLAG = "SYNC_FLAG";
    public static final String IMPORT_EXCEL_FLAG = "IMPORT_EXCEL_FLAG";
    public static final String UPDOWN_FLAG = "UPDOWN_FLAG";

    public IdentifiableOption(Identifiable identifiable) {
        super(identifiable);
    }

    @Override
    public String getSdgId() {
        return GID_IdentifiableOption;
    }
}

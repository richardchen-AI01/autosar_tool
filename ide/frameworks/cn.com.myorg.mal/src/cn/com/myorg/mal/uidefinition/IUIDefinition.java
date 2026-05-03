package cn.com.myorg.mal.uidefinition;

/**
 * Reference: cn.com.isoft.mal.uidefinition.IUIDefinition.
 *
 * <p>Top-level marker for UI behavior hooks (field enable/disable, value scope,
 * reserve container actions). Variant flags map to families of behavior consumed
 * by host widgets via MetaModelDescriptorParser.getUIDefinitionList(.., flag).
 */
public interface IUIDefinition {
    long REPLACE_FLAG = 1L;
    long FIX_FLAG = 8L;
    long VIEWER_FLAG = 128L;
    long TRIGGER_FLAG = 32768L;
    long ENABLE_FLAG = 4096L;
    long DISABLE_FLAG = 8192L;
    long RANGE_FLAG = 16384L;
    long CHANGE_MODEL_FLAG = 65536L;
    long RADIO_FLAG = 131072L;
    long RESERVED_FLAG = 0x100000L;
    long DELETEREFVALUE_FLAG = 0x200000L;
    long ADDVALUE_FLAG = 0x40000000L;

    String getDefElementName();

    long getVariant();
}

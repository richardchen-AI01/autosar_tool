# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\constant\BswConstant.py
MODULE_NAME_ECUM = "EcuM"
MODULE_NAME_RTE = "Rte"
MODULE_NAME_OS = "Os"
MODULE_NAME_COM = "Com"
MODULE_NAME_LDCOM = "LdCom"
MODULE_NAME_XFRM = "Xfrm"
MODULE_NAME_XCP = "Xcp"
MODULE_NAME_ECUC = "EcuC"
MODULE_NAME_BSWM = "BswM"
BSWMD_PG_NAME_DESC = "BswModuleDescriptions"
BSWMD_PG_NAME_ENTRY = "BswModuleEntrys"
BSWMD_PG_NAME_IMP = "BswImplementations"
BOOLEAN = "BL"
UINT8 = "U8"
UINT16 = "U16"
UINT32 = "U32"
UINT64 = "U64"
SINT8 = "S8"
SINT16 = "S16"
SINT32 = "S32"
SINT64 = "S64"
UINT8_N = "U8N"
FLOAT32 = "F32"
FLOAT64 = "F64"
LITTLE_ENDIAN = "LE"
BIG_ENDIAN = "BE"
OPAQUE = "OP"

def get_bsw_constant_value(key):
    return globals().get(key)

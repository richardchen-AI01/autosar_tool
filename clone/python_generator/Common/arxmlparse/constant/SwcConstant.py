# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\constant\SwcConstant.py
from Common import logger
dict_name_to_event = {
 'datasendcompletedevent': '"DATA_SEND_COMPLETED_EVENT"', 
 'asynchronousservercallreturnsevent': '"ASYNCHRONOUS_SERVER_CALL_RETURNS_EVENT"', 
 'transformerharderrorevent': '"TRANSFORMER_HARD_ERROR_EVENT"', 
 'swcmodemanagererrorevent': '"SWC_MODE_MANAGER_ERROR_EVENT"', 
 'internaltriggeroccurredevent': '"INTERNAL_TRIGGER_OCCURRED_EVENT"', 
 'initevent': '"INIT_EVENT"', 
 'externaltriggeroccurredevent': '"EXTERNAL_TRIGGER_OCCURRED_EVENT"', 
 'datawritecompletedevent': '"DATA_WRITE_COMPLETED_EVENT"', 
 'timingevent': '"TIMING_EVENT"', 
 'swcmodeswitchevent': '"SWC_MODE_SWITCH_EVENT"', 
 'operationinvokedevent': '"OPERATION_INVOKED_EVENT"', 
 'datareceiveerrorevent': '"DATA_RECEIVE_ERROR_EVENT"', 
 'datareceivedevent': '"DATA_RECEIVED_EVENT"', 
 'backgroundevent': '"BACKGROUND_EVENT"', 
 'modeswitchedackevent': '"MODE_SWITCHED_ACK_EVENT"'}

class SwcConstants:
    BASE_TYPE = {
     'boolean': 1, 
     'uint8': 1, 
     'unsigned char': 1, 
     'utf-8': 1, 
     'sint8': 1, 
     'signed char': 1, 
     'uint16': 2, 
     'unsigned short': 2, 
     'sint16': 2, 
     'signed short': 2, 
     'utf-16': 2, 
     'uint32': 4, 
     'unsigned long': 4, 
     'sint32': 4, 
     'signed long': 4, 
     'float32': 4, 
     'float': 4, 
     'uint64': 8, 
     'unsigned long long': 8, 
     'sint64': 8, 
     'signed long long': 8, 
     'float64': 8, 
     'double': 8}
    MACRO_DEFINE = {
     'SOMEIPXF_DATA_ELEMENT_CONFIG_START': 8, 
     'SOMEIPXF_DATA_ELEMENT_STOP': 1, 
     'SOMEIPXF_BASIC_DATA_TYPE_START': 1, 
     'SOMEIPXF_BASIC_DATA_TYPE_STOP': 1, 
     'SOMEIPXF_FSA_OF_BASIC_TYPE_START': 1, 
     'SOMEIPXF_FSA_OF_BASIC_TYPE_STOP': 1, 
     'SOMEIPXF_FSA_OF_STRUCT_START': 1, 
     'SOMEIPXF_FSA_OF_STRUCT_STOP': 1, 
     'SOMEIPXF_STRUCT_WITH_LF_START': 1, 
     'SOMEIPXF_STRUCT_WITH_LF_STOP': 1, 
     'SOMEIPXF_FSA_WITH_LF_START': 1, 
     'SOMEIPXF_FSA_WITH_LF_STOP': 1, 
     'SOMEIPXF_VSA_START': 1, 
     'SOMEIPXF_VSA_STOP': 1, 
     'SOMEIPXF_VSA_ELEMENT_CHECK_POINT': 1, 
     'SOMEIPXF_VSA_ELEMENT_ENTER': 1, 
     'SOMEIPXF_FSA_WITH_BOM_START': 1, 
     'SOMEIPXF_FSA_WITH_BOM_STOP': 1, 
     'SOMEIPXF_VSA_WITH_BOM_START': 1, 
     'SOMEIPXF_VSA_WITH_BOM_STOP': 1, 
     'SOMEIPXF_SET_INTEGER_CONFIG_NW_1B': 1, 
     'SOMEIPXF_SET_INTEGER_CONFIG_NW_2B': 2, 
     'SOMEIPXF_SET_INTEGER_CONFIG_NW_4B': 4, 
     'SOMEIPXF_SET_INTEGER_CONFIG_NW_8B': 8, 
     'SOMEIPXF_SET_STRUCT_CONFIG_NW_1B': 1, 
     'SOMEIPXF_SET_STRUCT_CONFIG_NW_2B': 2, 
     'SOMEIPXF_SET_STRUCT_CONFIG_NW_4B': 4, 
     'SOMEIPXF_SET_STRUCT_CONFIG_NW_8B': 8, 
     'SOMEIPXF_SET_FSA_CONFIG': 2, 
     'SOMEIPXF_SET_FSA_WITH_LF_CONFIG': 2, 
     'SOMEIPXF_SET_FSA_WITH_LF_DIM_CONFIG': 3, 
     'SOMEIPXF_SET_STRUCT_LENGTH_FIELD_CONFIG': 2, 
     'SOMEIPXF_SET_VSA_CONFIG': 4, 
     'SOMEIPXF_SET_VSA_DIM_CONFIG': 3, 
     'SOMEIPXF_VSA_STOP_INDEX': 1, 
     'SOMEIPXF_SET_FSA_BOM_CONFIG': 1, 
     'SOMEIPXF_SET_VSA_BOM_CONFIG': 2}

    @staticmethod
    def get_swc_base_type_value(key):
        return SwcConstants.BASE_TYPE.get(key)

    @staticmethod
    def get_swc_macro_define_value(key):
        if "/*" in key:
            return 0
        if "(" in key:
            key = key[None[:key.index("(")]]
        result = SwcConstants.MACRO_DEFINE.get(key)
        if isinstance(result, int):
            return result
        logger.error("Cost calculation failed：" + key)
        return 0


if __name__ == "__main__":
    print(SwcConstants.get_swc_base_type_value("sint16"))
    print(SwcConstants.get_swc_macro_define_value("SOMEIPXF_DATA_ELEMENT_CONFIG_START"))

# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ParameterSwComponentType.py
from .SwComponentType import SwComponentType

class ParameterSwComponentType(SwComponentType):

    def __init__(self):
        super().__init__()
        from .ConstantSpecificationMappingSet import ConstantSpecificationMappingSet
        from .DataTypeMappingSet import DataTypeMappingSet
        from .InstantiationDataDefProps import InstantiationDataDefProps
        self._artop_constantMappingRef = []
        self._artop_dataTypeMappingRef = []
        self._artop_instantiationDataDefProps = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_constantMappingRef':"CONSTANT-SPECIFICATION-MAPPING-SET", 
         '_artop_dataTypeMappingRef':"DATA-TYPE-MAPPING-SET", 
         '_artop_instantiationDataDefProps':"INSTANTIATION-DATA-DEF-PROPS"})

    @property
    def ref_constantMappings_(self):
        return self._artop_constantMappingRef

    @property
    def constantMappings_(self):
        return self._artop_constantMappingRef

    @property
    def ref_dataTypeMappings_(self):
        return self._artop_dataTypeMappingRef

    @property
    def dataTypeMappings_(self):
        return self._artop_dataTypeMappingRef

    @property
    def instantiationDataDefProps_InstantiationDataDefProps(self):
        return self._artop_instantiationDataDefProps

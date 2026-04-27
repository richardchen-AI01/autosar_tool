# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\InternalBehavior.py
from .AtpStructureElement import AtpStructureElement

class InternalBehavior(AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .ParameterDataPrototype import ParameterDataPrototype
        from .ConstantSpecificationMappingSet import ConstantSpecificationMappingSet
        from .DataTypeMappingSet import DataTypeMappingSet
        from .ExclusiveArea import ExclusiveArea
        from .ExclusiveAreaNestingOrder import ExclusiveAreaNestingOrder
        from .VariableDataPrototype import VariableDataPrototype
        self._artop_constantMemory = []
        self._artop_constantValueMappingRef = []
        self._artop_dataTypeMappingRef = []
        self._artop_exclusiveArea = []
        self._artop_exclusiveAreaNestingOrder = []
        self._artop_staticMemory = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_constantMemory': '"PARAMETER-DATA-PROTOTYPE"', 
         '_artop_constantValueMappingRef': '"CONSTANT-SPECIFICATION-MAPPING-SET"', 
         '_artop_dataTypeMappingRef': '"DATA-TYPE-MAPPING-SET"', 
         '_artop_exclusiveArea': '"EXCLUSIVE-AREA"', 
         '_artop_exclusiveAreaNestingOrder': '"EXCLUSIVE-AREA-NESTING-ORDER"', 
         '_artop_staticMemory': '"VARIABLE-DATA-PROTOTYPE"'})

    @property
    def constantMemories_ParameterDataPrototype(self):
        return self._artop_constantMemory

    @property
    def ref_constantValueMappings_(self):
        return self._artop_constantValueMappingRef

    @property
    def constantValueMappings_(self):
        return self._artop_constantValueMappingRef

    @property
    def ref_dataTypeMappings_(self):
        return self._artop_dataTypeMappingRef

    @property
    def dataTypeMappings_(self):
        return self._artop_dataTypeMappingRef

    @property
    def exclusiveAreas_ExclusiveArea(self):
        return self._artop_exclusiveArea

    @property
    def exclusiveAreaNestingOrders_ExclusiveAreaNestingOrder(self):
        return self._artop_exclusiveAreaNestingOrder

    @property
    def staticMemories_VariableDataPrototype(self):
        return self._artop_staticMemory

# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompositionSwComponentType.py
from .SwComponentType import SwComponentType

class CompositionSwComponentType(SwComponentType):

    def __init__(self):
        super().__init__()
        from .SwComponentPrototype import SwComponentPrototype
        from .SwConnector import SwConnector
        from .ConstantSpecificationMappingSet import ConstantSpecificationMappingSet
        from .DataTypeMappingSet import DataTypeMappingSet
        from .InstantiationRTEEventProps import InstantiationRTEEventProps
        self._artop_component = []
        self._artop_connector = []
        self._artop_constantValueMappingRef = []
        self._artop_dataTypeMappingRef = []
        self._artop_instantiationRteEventProps = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_component': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_connector': '"SW-CONNECTOR"', 
         '_artop_constantValueMappingRef': '"CONSTANT-SPECIFICATION-MAPPING-SET"', 
         '_artop_dataTypeMappingRef': '"DATA-TYPE-MAPPING-SET"', 
         '_artop_instantiationRteEventProps': '"INSTANTIATION-RTE-EVENT-PROPS"'})

    @property
    def components_SwComponentPrototype(self):
        return self._artop_component

    @property
    def connectors_SwConnector(self):
        return self._artop_connector

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
    def instantiationRTEEventProps_InstantiationRTEEventProps(self):
        return self._artop_instantiationRteEventProps

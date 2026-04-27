# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\InterfaceMapping.py
from .Identifiable import Identifiable

class InterfaceMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .InterfaceMappingSet import InterfaceMappingSet
        from .EventMapping import EventMapping
        from .FieldMapping import FieldMapping
        from .FireAndForgetMapping import FireAndForgetMapping
        from .MethodMapping import MethodMapping
        from .VariationPoint import VariationPoint
        self._artop_interfaceMappingSet = None
        self._artop_eventMapping = []
        self._artop_fieldMapping = []
        self._artop_fireAndForgetMapping = []
        self._artop_methodMapping = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_interfaceMappingSet': '"INTERFACE-MAPPING-SET"', 
         '_artop_eventMapping': '"EVENT-MAPPING"', 
         '_artop_fieldMapping': '"FIELD-MAPPING"', 
         '_artop_fireAndForgetMapping': '"FIRE-AND-FORGET-MAPPING"', 
         '_artop_methodMapping': '"METHOD-MAPPING"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_interfaceMappingSet_(self):
        return self._artop_interfaceMappingSet

    @property
    def interfaceMappingSet_(self):
        if self._artop_interfaceMappingSet is not None:
            if hasattr(self._artop_interfaceMappingSet, "uuid"):
                return self._artop_interfaceMappingSet.uuid
        return

    @property
    def eventMappings_EventMapping(self):
        return self._artop_eventMapping

    @property
    def fieldMappings_FieldMapping(self):
        return self._artop_fieldMapping

    @property
    def fireAndForgetMappings_FireAndForgetMapping(self):
        return self._artop_fireAndForgetMapping

    @property
    def methodMappings_MethodMapping(self):
        return self._artop_methodMapping

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return

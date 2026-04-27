# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwComponentType.py
from .AtpType import AtpType
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint
from .ARElement import ARElement

class SwComponentType(ARElement, AtpBlueprint, AtpBlueprintable, AtpType):

    def __init__(self):
        super().__init__()
        from .SwComponentDocumentation import SwComponentDocumentation
        from .ConsistencyNeeds import ConsistencyNeeds
        from .PortPrototype import PortPrototype
        from .PortGroup import PortGroup
        from .UnitGroup import UnitGroup
        self._artop_swComponentDocumentation = []
        self._artop_consistencyNeeds = []
        self._artop_port = []
        self._artop_portGroup = []
        self._artop_unitGroupRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swComponentDocumentation': '"SW-COMPONENT-DOCUMENTATION"', 
         '_artop_consistencyNeeds': '"CONSISTENCY-NEEDS"', 
         '_artop_port': '"PORT-PROTOTYPE"', 
         '_artop_portGroup': '"PORT-GROUP"', 
         '_artop_unitGroupRef': '"UNIT-GROUP"'})

    @property
    def swComponentDocumentations_SwComponentDocumentation(self):
        return self._artop_swComponentDocumentation

    @property
    def consistencyNeeds_ConsistencyNeeds(self):
        return self._artop_consistencyNeeds

    @property
    def ports_PortPrototype(self):
        return self._artop_port

    @property
    def portGroups_PortGroup(self):
        return self._artop_portGroup

    @property
    def ref_unitGroups_(self):
        return self._artop_unitGroupRef

    @property
    def unitGroups_(self):
        return self._artop_unitGroupRef

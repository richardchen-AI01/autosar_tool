# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeDeclarationGroupPrototypeMapping.py
from .ARObject import ARObject

class ModeDeclarationGroupPrototypeMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .ModeInterfaceMapping import ModeInterfaceMapping
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        from .ModeDeclarationMappingSet import ModeDeclarationMappingSet
        self._artop_modeInterfaceMapping = None
        self._artop_firstModeGroupRef = None
        self._artop_modeDeclarationMappingSetRef = None
        self._artop_secondModeGroupRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_modeInterfaceMapping': '"MODE-INTERFACE-MAPPING"', 
         '_artop_firstModeGroupRef': '"MODE-DECLARATION-GROUP-PROTOTYPE"', 
         '_artop_modeDeclarationMappingSetRef': '"MODE-DECLARATION-MAPPING-SET"', 
         '_artop_secondModeGroupRef': '"MODE-DECLARATION-GROUP-PROTOTYPE"'})

    @property
    def ref_modeInterfaceMapping_(self):
        return self._artop_modeInterfaceMapping

    @property
    def modeInterfaceMapping_(self):
        if self._artop_modeInterfaceMapping is not None:
            if hasattr(self._artop_modeInterfaceMapping, "uuid"):
                return self._artop_modeInterfaceMapping.uuid
        return

    @property
    def ref_firstModeGroup_(self):
        return self._artop_firstModeGroupRef

    @property
    def firstModeGroup_(self):
        if self._artop_firstModeGroupRef is not None:
            if hasattr(self._artop_firstModeGroupRef, "uuid"):
                return self._artop_firstModeGroupRef.uuid
        return

    @property
    def ref_modeDeclarationMappingSet_(self):
        return self._artop_modeDeclarationMappingSetRef

    @property
    def modeDeclarationMappingSet_(self):
        if self._artop_modeDeclarationMappingSetRef is not None:
            if hasattr(self._artop_modeDeclarationMappingSetRef, "uuid"):
                return self._artop_modeDeclarationMappingSetRef.uuid
        return

    @property
    def ref_secondModeGroup_(self):
        return self._artop_secondModeGroupRef

    @property
    def secondModeGroup_(self):
        if self._artop_secondModeGroupRef is not None:
            if hasattr(self._artop_secondModeGroupRef, "uuid"):
                return self._artop_secondModeGroupRef.uuid
        return

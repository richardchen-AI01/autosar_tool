# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PortPrototypeBlueprint.py
from .AtpStructureElement import AtpStructureElement
from .AtpBlueprint import AtpBlueprint
from .ARElement import ARElement

class PortPrototypeBlueprint(ARElement, AtpBlueprint, AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .PortPrototypeBlueprintInitValue import PortPrototypeBlueprintInitValue
        from .PortInterface import PortInterface
        from .PPortComSpec import PPortComSpec
        from .RPortComSpec import RPortComSpec
        self._artop_initValue = []
        self._artop_interfaceRef = None
        self._artop_providedComSpec = []
        self._artop_requiredComSpec = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_initValue': '"PORT-PROTOTYPE-BLUEPRINT-INIT-VALUE"', 
         '_artop_interfaceRef': '"PORT-INTERFACE"', 
         '_artop_providedComSpec': '"P-PORT-COM-SPEC"', 
         '_artop_requiredComSpec': '"R-PORT-COM-SPEC"'})

    @property
    def initValues_PortPrototypeBlueprintInitValue(self):
        return self._artop_initValue

    @property
    def ref_interface_(self):
        return self._artop_interfaceRef

    @property
    def interface_(self):
        if self._artop_interfaceRef is not None:
            if hasattr(self._artop_interfaceRef, "uuid"):
                return self._artop_interfaceRef.uuid
        return

    @property
    def providedComSpecs_PPortComSpec(self):
        return self._artop_providedComSpec

    @property
    def requiredComSpecs_RPortComSpec(self):
        return self._artop_requiredComSpec

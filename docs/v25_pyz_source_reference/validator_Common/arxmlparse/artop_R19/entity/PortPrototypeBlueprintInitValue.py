# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PortPrototypeBlueprintInitValue.py
from .ARObject import ARObject

class PortPrototypeBlueprintInitValue(ARObject):

    def __init__(self):
        super().__init__()
        from .PortPrototypeBlueprint import PortPrototypeBlueprint
        from .AutosarDataPrototype import AutosarDataPrototype
        from .ValueSpecification import ValueSpecification
        self._artop_portPrototypeBlueprint = None
        self._artop_dataPrototypeRef = None
        self._artop_value = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_portPrototypeBlueprint':"PORT-PROTOTYPE-BLUEPRINT", 
         '_artop_dataPrototypeRef':"AUTOSAR-DATA-PROTOTYPE", 
         '_artop_value':"VALUE-SPECIFICATION"})

    @property
    def ref_portPrototypeBlueprint_(self):
        return self._artop_portPrototypeBlueprint

    @property
    def portPrototypeBlueprint_(self):
        if self._artop_portPrototypeBlueprint is not None:
            if hasattr(self._artop_portPrototypeBlueprint, "uuid"):
                return self._artop_portPrototypeBlueprint.uuid
        return

    @property
    def ref_dataPrototype_(self):
        return self._artop_dataPrototypeRef

    @property
    def dataPrototype_(self):
        if self._artop_dataPrototypeRef is not None:
            if hasattr(self._artop_dataPrototypeRef, "uuid"):
                return self._artop_dataPrototypeRef.uuid
        return

    @property
    def ref_value_(self):
        return self._artop_value

    @property
    def value_(self):
        if self._artop_value is not None:
            if hasattr(self._artop_value, "uuid"):
                return self._artop_value.uuid
        return

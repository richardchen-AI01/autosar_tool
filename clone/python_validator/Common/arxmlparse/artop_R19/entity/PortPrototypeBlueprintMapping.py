# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PortPrototypeBlueprintMapping.py
from .AtpBlueprintMapping import AtpBlueprintMapping

class PortPrototypeBlueprintMapping(AtpBlueprintMapping):

    def __init__(self):
        super().__init__()
        from .PortPrototypeBlueprint import PortPrototypeBlueprint
        from .PortPrototype import PortPrototype
        self._artop_portPrototypeBlueprintRef = None
        self._artop_derivedPortPrototypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_portPrototypeBlueprintRef':"PORT-PROTOTYPE-BLUEPRINT", 
         '_artop_derivedPortPrototypeRef':"PORT-PROTOTYPE"})

    @property
    def ref_portPrototypeBlueprint_(self):
        return self._artop_portPrototypeBlueprintRef

    @property
    def portPrototypeBlueprint_(self):
        if self._artop_portPrototypeBlueprintRef is not None:
            if hasattr(self._artop_portPrototypeBlueprintRef, "uuid"):
                return self._artop_portPrototypeBlueprintRef.uuid
        return

    @property
    def ref_derivedPortPrototype_(self):
        return self._artop_derivedPortPrototypeRef

    @property
    def derivedPortPrototype_(self):
        if self._artop_derivedPortPrototypeRef is not None:
            if hasattr(self._artop_derivedPortPrototypeRef, "uuid"):
                return self._artop_derivedPortPrototypeRef.uuid
        return

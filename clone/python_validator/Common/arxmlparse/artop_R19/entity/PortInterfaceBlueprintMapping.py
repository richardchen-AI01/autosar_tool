# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PortInterfaceBlueprintMapping.py
from .AtpBlueprintMapping import AtpBlueprintMapping

class PortInterfaceBlueprintMapping(AtpBlueprintMapping):

    def __init__(self):
        super().__init__()
        from .PortInterface import PortInterface
        self._artop_portInterfaceBlueprintRef = None
        self._artop_derivedPortInterfaceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_portInterfaceBlueprintRef':"PORT-INTERFACE", 
         '_artop_derivedPortInterfaceRef':"PORT-INTERFACE"})

    @property
    def ref_portInterfaceBlueprint_(self):
        return self._artop_portInterfaceBlueprintRef

    @property
    def portInterfaceBlueprint_(self):
        if self._artop_portInterfaceBlueprintRef is not None:
            if hasattr(self._artop_portInterfaceBlueprintRef, "uuid"):
                return self._artop_portInterfaceBlueprintRef.uuid
        return

    @property
    def ref_derivedPortInterface_(self):
        return self._artop_derivedPortInterfaceRef

    @property
    def derivedPortInterface_(self):
        if self._artop_derivedPortInterfaceRef is not None:
            if hasattr(self._artop_derivedPortInterfaceRef, "uuid"):
                return self._artop_derivedPortInterfaceRef.uuid
        return

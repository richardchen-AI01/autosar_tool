# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventVfbPort.py
from .TDEventVfb import TDEventVfb

class TDEventVfbPort(TDEventVfb):

    def __init__(self):
        super().__init__()
        from .PortPrototypeBlueprint import PortPrototypeBlueprint
        from .PortPrototype import PortPrototype
        self._artop_isExternal = None
        self._artop_portPrototypeBlueprintRef = None
        self._artop_portRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_portPrototypeBlueprintRef':"PORT-PROTOTYPE-BLUEPRINT", 
         '_artop_portRef':"PORT-PROTOTYPE"})

    @property
    def isExternal_(self):
        if self._artop_isExternal:
            if self._artop_isExternal == "true":
                return True
            return False
        else:
            return self._artop_isExternal

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
    def ref_port_(self):
        return self._artop_portRef

    @property
    def port_(self):
        if self._artop_portRef is not None:
            if hasattr(self._artop_portRef, "uuid"):
                return self._artop_portRef.uuid
        return

# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompuMethod.py
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint
from .ARElement import ARElement

class CompuMethod(ARElement, AtpBlueprint, AtpBlueprintable):

    def __init__(self):
        super().__init__()
        from .Unit import Unit
        from .Compu import Compu
        self._artop_displayFormat = None
        self._artop_unitRef = None
        self._artop_compuInternalToPhys = None
        self._artop_compuPhysToInternal = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_unitRef':"UNIT", 
         '_artop_compuInternalToPhys':"COMPU", 
         '_artop_compuPhysToInternal':"COMPU"})

    @property
    def displayFormat_(self):
        return self._artop_displayFormat

    @property
    def ref_unit_(self):
        return self._artop_unitRef

    @property
    def unit_(self):
        if self._artop_unitRef is not None:
            if hasattr(self._artop_unitRef, "uuid"):
                return self._artop_unitRef.uuid
        return

    @property
    def ref_compuInternalToPhys_(self):
        return self._artop_compuInternalToPhys

    @property
    def compuInternalToPhys_(self):
        if self._artop_compuInternalToPhys is not None:
            if hasattr(self._artop_compuInternalToPhys, "uuid"):
                return self._artop_compuInternalToPhys.uuid
        return

    @property
    def ref_compuPhysToInternal_(self):
        return self._artop_compuPhysToInternal

    @property
    def compuPhysToInternal_(self):
        if self._artop_compuPhysToInternal is not None:
            if hasattr(self._artop_compuPhysToInternal, "uuid"):
                return self._artop_compuPhysToInternal.uuid
        return

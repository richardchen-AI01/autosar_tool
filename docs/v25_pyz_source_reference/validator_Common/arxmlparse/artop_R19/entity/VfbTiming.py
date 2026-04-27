# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\VfbTiming.py
from .TimingExtension import TimingExtension
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint

class VfbTiming(AtpBlueprint, AtpBlueprintable, TimingExtension):

    def __init__(self):
        super().__init__()
        from .SwComponentType import SwComponentType
        self._artop_componentRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_componentRef": "SW-COMPONENT-TYPE"})

    @property
    def ref_component_(self):
        return self._artop_componentRef

    @property
    def component_(self):
        if self._artop_componentRef is not None:
            if hasattr(self._artop_componentRef, "uuid"):
                return self._artop_componentRef.uuid
        return

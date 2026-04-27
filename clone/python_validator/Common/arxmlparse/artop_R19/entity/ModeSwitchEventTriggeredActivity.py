# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeSwitchEventTriggeredActivity.py
from .ARObject import ARObject

class ModeSwitchEventTriggeredActivity(ARObject):

    def __init__(self):
        super().__init__()
        from .NvBlockDescriptor import NvBlockDescriptor
        from .SwcModeSwitchEvent import SwcModeSwitchEvent
        from .VariationPoint import VariationPoint
        self._artop_role = None
        self._artop_nvBlockDescriptor = None
        self._artop_swcModeSwitchEventRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_nvBlockDescriptor':"NV-BLOCK-DESCRIPTOR", 
         '_artop_swcModeSwitchEventRef':"SWC-MODE-SWITCH-EVENT", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def role_(self):
        return self._artop_role

    @property
    def ref_nvBlockDescriptor_(self):
        return self._artop_nvBlockDescriptor

    @property
    def nvBlockDescriptor_(self):
        if self._artop_nvBlockDescriptor is not None:
            if hasattr(self._artop_nvBlockDescriptor, "uuid"):
                return self._artop_nvBlockDescriptor.uuid
        return

    @property
    def ref_swcModeSwitchEvent_(self):
        return self._artop_swcModeSwitchEventRef

    @property
    def swcModeSwitchEvent_(self):
        if self._artop_swcModeSwitchEventRef is not None:
            if hasattr(self._artop_swcModeSwitchEventRef, "uuid"):
                return self._artop_swcModeSwitchEventRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return

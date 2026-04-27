# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HwPinGroupContent.py
from .ARObject import ARObject

class HwPinGroupContent(ARObject):

    def __init__(self):
        super().__init__()
        from .HwPinGroup import HwPinGroup
        from .HwPin import HwPin
        self._artop_mixed = None
        self._artop_hwPinGroup = None
        self._artop_hwPin = []
        self._artop_hwPinGroup = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_hwPinGroup':"HW-PIN-GROUP", 
         '_artop_hwPin':"HW-PIN", 
         '_artop_hwPinGroup':"HW-PIN-GROUP"})

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def ref_hwPinGroup_(self):
        return self._artop_hwPinGroup

    @property
    def hwPinGroup_(self):
        if self._artop_hwPinGroup is not None:
            if hasattr(self._artop_hwPinGroup, "uuid"):
                return self._artop_hwPinGroup.uuid
        return

    @property
    def hwPins_HwPin(self):
        return self._artop_hwPin

    @property
    def hwPinGroups_HwPinGroup(self):
        return self._artop_hwPinGroup

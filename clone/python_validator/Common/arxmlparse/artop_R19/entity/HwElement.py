# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HwElement.py
from .HwDescriptionEntity import HwDescriptionEntity
from .ARElement import ARElement

class HwElement(ARElement, HwDescriptionEntity):

    def __init__(self):
        super().__init__()
        from .HwElementRefConditional import HwElementRefConditional
        from .HwPinGroup import HwPinGroup
        from .HwElementConnector import HwElementConnector
        self._artop_nestedElement = []
        self._artop_hwPinGroup = []
        self._artop_hwElementConnection = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_nestedElement':"HW-ELEMENT-REF-CONDITIONAL", 
         '_artop_hwPinGroup':"HW-PIN-GROUP", 
         '_artop_hwElementConnection':"HW-ELEMENT-CONNECTOR"})

    @property
    def nestedElements_HwElementRefConditional(self):
        return self._artop_nestedElement

    @property
    def hwPinGroups_HwPinGroup(self):
        return self._artop_hwPinGroup

    @property
    def hwElementConnections_HwElementConnector(self):
        return self._artop_hwElementConnection

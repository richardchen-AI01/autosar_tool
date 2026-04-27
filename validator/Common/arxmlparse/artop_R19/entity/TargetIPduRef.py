# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TargetIPduRef.py
from .ARObject import ARObject

class TargetIPduRef(ARObject):

    def __init__(self):
        super().__init__()
        from .IPduMapping import IPduMapping
        from .PduMappingDefaultValue import PduMappingDefaultValue
        from .PduTriggering import PduTriggering
        self._artop_iPduMapping = None
        self._artop_defaultValue = None
        self._artop_targetIPduRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_iPduMapping':"I-PDU-MAPPING", 
         '_artop_defaultValue':"PDU-MAPPING-DEFAULT-VALUE", 
         '_artop_targetIPduRef':"PDU-TRIGGERING"})

    @property
    def ref_iPduMapping_(self):
        return self._artop_iPduMapping

    @property
    def iPduMapping_(self):
        if self._artop_iPduMapping is not None:
            if hasattr(self._artop_iPduMapping, "uuid"):
                return self._artop_iPduMapping.uuid
        return

    @property
    def ref_defaultValue_(self):
        return self._artop_defaultValue

    @property
    def defaultValue_(self):
        if self._artop_defaultValue is not None:
            if hasattr(self._artop_defaultValue, "uuid"):
                return self._artop_defaultValue.uuid
        return

    @property
    def ref_targetIPdu_(self):
        return self._artop_targetIPduRef

    @property
    def targetIPdu_(self):
        if self._artop_targetIPduRef is not None:
            if hasattr(self._artop_targetIPduRef, "uuid"):
                return self._artop_targetIPduRef.uuid
        return

# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PduMappingDefaultValue.py
from .ARObject import ARObject

class PduMappingDefaultValue(ARObject):

    def __init__(self):
        super().__init__()
        from .TargetIPduRef import TargetIPduRef
        from .DefaultValueElement import DefaultValueElement
        self._artop_targetIPduRef = None
        self._artop_defaultValueElement = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_targetIPduRef':"TARGET-I-PDU-REF", 
         '_artop_defaultValueElement':"DEFAULT-VALUE-ELEMENT"})

    @property
    def ref_targetIPduRef_(self):
        return self._artop_targetIPduRef

    @property
    def targetIPduRef_(self):
        if self._artop_targetIPduRef is not None:
            if hasattr(self._artop_targetIPduRef, "uuid"):
                return self._artop_targetIPduRef.uuid
        return

    @property
    def defaultValueElements_DefaultValueElement(self):
        return self._artop_defaultValueElement

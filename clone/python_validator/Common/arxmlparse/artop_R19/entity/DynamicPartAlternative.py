# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DynamicPartAlternative.py
from .ARObject import ARObject

class DynamicPartAlternative(ARObject):

    def __init__(self):
        super().__init__()
        from .DynamicPart import DynamicPart
        from .ISignalIPdu import ISignalIPdu
        self._artop_initialDynamicPart = None
        self._artop_selectorFieldCode = None
        self._artop_dynamicPart = None
        self._artop_iPduRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dynamicPart':"DYNAMIC-PART", 
         '_artop_iPduRef':"I-SIGNAL-I-PDU"})

    @property
    def initialDynamicPart_(self):
        if self._artop_initialDynamicPart:
            if self._artop_initialDynamicPart == "true":
                return True
            return False
        else:
            return self._artop_initialDynamicPart

    @property
    def selectorFieldCode_(self):
        if self._artop_selectorFieldCode:
            return int(self._artop_selectorFieldCode)
        return self._artop_selectorFieldCode

    @property
    def ref_dynamicPart_(self):
        return self._artop_dynamicPart

    @property
    def dynamicPart_(self):
        if self._artop_dynamicPart is not None:
            if hasattr(self._artop_dynamicPart, "uuid"):
                return self._artop_dynamicPart.uuid
        return

    @property
    def ref_iPdu_(self):
        return self._artop_iPduRef

    @property
    def iPdu_(self):
        if self._artop_iPduRef is not None:
            if hasattr(self._artop_iPduRef, "uuid"):
                return self._artop_iPduRef.uuid
        return

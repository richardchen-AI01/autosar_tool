# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SenderRecArrayElementMapping.py
from .ARObject import ARObject

class SenderRecArrayElementMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .SenderRecArrayTypeMapping import SenderRecArrayTypeMapping
        from .SenderRecCompositeTypeMapping import SenderRecCompositeTypeMapping
        from .IndexedArrayElement import IndexedArrayElement
        from .SystemSignal import SystemSignal
        self._artop_senderRecArrayTypeMapping = None
        self._artop_complexTypeMapping = None
        self._artop_indexedArrayElement = None
        self._artop_systemSignalRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_senderRecArrayTypeMapping': '"SENDER-REC-ARRAY-TYPE-MAPPING"', 
         '_artop_complexTypeMapping': '"SENDER-REC-COMPOSITE-TYPE-MAPPING"', 
         '_artop_indexedArrayElement': '"INDEXED-ARRAY-ELEMENT"', 
         '_artop_systemSignalRef': '"SYSTEM-SIGNAL"'})

    @property
    def ref_senderRecArrayTypeMapping_(self):
        return self._artop_senderRecArrayTypeMapping

    @property
    def senderRecArrayTypeMapping_(self):
        if self._artop_senderRecArrayTypeMapping is not None:
            if hasattr(self._artop_senderRecArrayTypeMapping, "uuid"):
                return self._artop_senderRecArrayTypeMapping.uuid
        return

    @property
    def ref_complexTypeMapping_(self):
        return self._artop_complexTypeMapping

    @property
    def complexTypeMapping_(self):
        if self._artop_complexTypeMapping is not None:
            if hasattr(self._artop_complexTypeMapping, "uuid"):
                return self._artop_complexTypeMapping.uuid
        return

    @property
    def ref_indexedArrayElement_(self):
        return self._artop_indexedArrayElement

    @property
    def indexedArrayElement_(self):
        if self._artop_indexedArrayElement is not None:
            if hasattr(self._artop_indexedArrayElement, "uuid"):
                return self._artop_indexedArrayElement.uuid
        return

    @property
    def ref_systemSignal_(self):
        return self._artop_systemSignalRef

    @property
    def systemSignal_(self):
        if self._artop_systemSignalRef is not None:
            if hasattr(self._artop_systemSignalRef, "uuid"):
                return self._artop_systemSignalRef.uuid
        return

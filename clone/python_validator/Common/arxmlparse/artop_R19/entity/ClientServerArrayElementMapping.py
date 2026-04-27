# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ClientServerArrayElementMapping.py
from .ARObject import ARObject

class ClientServerArrayElementMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .ClientServerArrayTypeMapping import ClientServerArrayTypeMapping
        from .ClientServerCompositeTypeMapping import ClientServerCompositeTypeMapping
        from .IndexedArrayElement import IndexedArrayElement
        from .SystemSignal import SystemSignal
        self._artop_clientServerArrayTypeMapping = None
        self._artop_complexTypeMapping = None
        self._artop_indexedArrayElement = None
        self._artop_systemSignalRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_clientServerArrayTypeMapping': '"CLIENT-SERVER-ARRAY-TYPE-MAPPING"', 
         '_artop_complexTypeMapping': '"CLIENT-SERVER-COMPOSITE-TYPE-MAPPING"', 
         '_artop_indexedArrayElement': '"INDEXED-ARRAY-ELEMENT"', 
         '_artop_systemSignalRef': '"SYSTEM-SIGNAL"'})

    @property
    def ref_clientServerArrayTypeMapping_(self):
        return self._artop_clientServerArrayTypeMapping

    @property
    def clientServerArrayTypeMapping_(self):
        if self._artop_clientServerArrayTypeMapping is not None:
            if hasattr(self._artop_clientServerArrayTypeMapping, "uuid"):
                return self._artop_clientServerArrayTypeMapping.uuid
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

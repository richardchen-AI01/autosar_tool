# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\IndexedArrayElement.py
from .ARObject import ARObject

class IndexedArrayElement(ARObject):

    def __init__(self):
        super().__init__()
        from .ApplicationArrayElement import ApplicationArrayElement
        from .ImplementationDataTypeElement import ImplementationDataTypeElement
        self._artop_index = None
        self._artop_applicationArrayElementRef = None
        self._artop_implementationArrayElementRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_applicationArrayElementRef':"APPLICATION-ARRAY-ELEMENT", 
         '_artop_implementationArrayElementRef':"IMPLEMENTATION-DATA-TYPE-ELEMENT"})

    @property
    def index_(self):
        if self._artop_index:
            return int(self._artop_index)
        return self._artop_index

    @property
    def ref_applicationArrayElement_(self):
        return self._artop_applicationArrayElementRef

    @property
    def applicationArrayElement_(self):
        if self._artop_applicationArrayElementRef is not None:
            if hasattr(self._artop_applicationArrayElementRef, "uuid"):
                return self._artop_applicationArrayElementRef.uuid
        return

    @property
    def ref_implementationArrayElement_(self):
        return self._artop_implementationArrayElementRef

    @property
    def implementationArrayElement_(self):
        if self._artop_implementationArrayElementRef is not None:
            if hasattr(self._artop_implementationArrayElementRef, "uuid"):
                return self._artop_implementationArrayElementRef.uuid
        return

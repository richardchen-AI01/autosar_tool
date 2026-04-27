# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ClientServerCompositeTypeMapping.py
from .ARObject import ARObject

class ClientServerCompositeTypeMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .ArgumentDataPrototype import ArgumentDataPrototype
        self._artop_argumentRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_argumentRef": "ARGUMENT-DATA-PROTOTYPE"})

    @property
    def ref_argument_(self):
        return self._artop_argumentRef

    @property
    def argument_(self):
        if self._artop_argumentRef is not None:
            if hasattr(self._artop_argumentRef, "uuid"):
                return self._artop_argumentRef.uuid
        return

# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucInstanceReferenceValue.py
from .EcucAbstractReferenceValue import EcucAbstractReferenceValue

class EcucInstanceReferenceValue(EcucAbstractReferenceValue):

    def __init__(self):
        super().__init__()
        from .AnyInstanceRef import AnyInstanceRef
        self._artop_valueIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_valueIref": "ANY-INSTANCE-REF-IREF"})

    @property
    def ref_value_(self):
        return self._artop_valueIref

    @property
    def value_(self):
        if self._artop_valueIref is not None:
            if hasattr(self._artop_valueIref, "uuid"):
                return self._artop_valueIref.uuid
        return

# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ConstantReference.py
from .ValueSpecification import ValueSpecification

class ConstantReference(ValueSpecification):

    def __init__(self):
        super().__init__()
        from .ConstantSpecification import ConstantSpecification
        self._artop_constantRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_constantRef": "CONSTANT-SPECIFICATION"})

    @property
    def ref_constant_(self):
        return self._artop_constantRef

    @property
    def constant_(self):
        if self._artop_constantRef is not None:
            if hasattr(self._artop_constantRef, "uuid"):
                return self._artop_constantRef.uuid
        return

# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ReferenceValueSpecification.py
from .ValueSpecification import ValueSpecification

class ReferenceValueSpecification(ValueSpecification):

    def __init__(self):
        super().__init__()
        from .DataPrototype import DataPrototype
        self._artop_referenceValueRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_referenceValueRef": "DATA-PROTOTYPE"})

    @property
    def ref_referenceValue_(self):
        return self._artop_referenceValueRef

    @property
    def referenceValue_(self):
        if self._artop_referenceValueRef is not None:
            if hasattr(self._artop_referenceValueRef, "uuid"):
                return self._artop_referenceValueRef.uuid
        return

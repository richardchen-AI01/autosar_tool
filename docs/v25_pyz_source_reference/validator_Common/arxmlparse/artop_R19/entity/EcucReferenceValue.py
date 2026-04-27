# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucReferenceValue.py
from .EcucAbstractReferenceValue import EcucAbstractReferenceValue

class EcucReferenceValue(EcucAbstractReferenceValue):

    def __init__(self):
        super().__init__()
        from .Referrable import Referrable
        self._artop_valueRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_valueRef": "REFERRABLE"})

    @property
    def ref_value_(self):
        return self._artop_valueRef

    @property
    def value_(self):
        if self._artop_valueRef is not None:
            if hasattr(self._artop_valueRef, "uuid"):
                return self._artop_valueRef.uuid
        return

    def getAttrValue(self, enum_path, variant_value=None):
        from ..artop_util import get_attribute_value
        return get_attribute_value(self, enum_path, variant_value)

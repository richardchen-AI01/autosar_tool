# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventVariableDataPrototype.py
from .TDEventVfbPort import TDEventVfbPort

class TDEventVariableDataPrototype(TDEventVfbPort):

    def __init__(self):
        super().__init__()
        from .VariableDataPrototype import VariableDataPrototype
        self._artop_tdEventVariableDataPrototypeType = None
        self._artop_dataElementRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_dataElementRef": "VARIABLE-DATA-PROTOTYPE"})

    @property
    def tdEventVariableDataPrototypeType_(self):
        return self._artop_tdEventVariableDataPrototypeType

    @property
    def ref_dataElement_(self):
        return self._artop_dataElementRef

    @property
    def dataElement_(self):
        if self._artop_dataElementRef is not None:
            if hasattr(self._artop_dataElementRef, "uuid"):
                return self._artop_dataElementRef.uuid
        return

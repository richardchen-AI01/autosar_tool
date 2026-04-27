# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AutosarDataPrototype.py
from .DataPrototype import DataPrototype

class AutosarDataPrototype(DataPrototype):

    def __init__(self):
        super().__init__()
        from .AutosarDataType import AutosarDataType
        self._artop_typeTref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_typeTref": "AUTOSAR-DATA-TYPE"})

    @property
    def ref_type_(self):
        return self._artop_typeTref

    @property
    def type_(self):
        if self._artop_typeTref is not None:
            if hasattr(self._artop_typeTref, "uuid"):
                return self._artop_typeTref.uuid
        return

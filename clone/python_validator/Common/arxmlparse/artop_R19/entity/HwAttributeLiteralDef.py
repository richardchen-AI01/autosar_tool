# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HwAttributeLiteralDef.py
from .Identifiable import Identifiable

class HwAttributeLiteralDef(Identifiable):

    def __init__(self):
        super().__init__()
        from .HwAttributeDef import HwAttributeDef
        self._artop_hwAttributeDef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_hwAttributeDef": "HW-ATTRIBUTE-DEF"})

    @property
    def ref_hwAttributeDef_(self):
        return self._artop_hwAttributeDef

    @property
    def hwAttributeDef_(self):
        if self._artop_hwAttributeDef is not None:
            if hasattr(self._artop_hwAttributeDef, "uuid"):
                return self._artop_hwAttributeDef.uuid
        return

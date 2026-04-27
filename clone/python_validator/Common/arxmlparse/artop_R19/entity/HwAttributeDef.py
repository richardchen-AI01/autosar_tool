# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HwAttributeDef.py
from .Identifiable import Identifiable

class HwAttributeDef(Identifiable):

    def __init__(self):
        super().__init__()
        from .HwCategory import HwCategory
        from .HwAttributeLiteralDef import HwAttributeLiteralDef
        from .Unit import Unit
        self._artop_isRequired = None
        self._artop_hwCategory = None
        self._artop_hwAttributeLiteral = []
        self._artop_unitRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_hwCategory':"HW-CATEGORY", 
         '_artop_hwAttributeLiteral':"HW-ATTRIBUTE-LITERAL-DEF", 
         '_artop_unitRef':"UNIT"})

    @property
    def isRequired_(self):
        if self._artop_isRequired:
            if self._artop_isRequired == "true":
                return True
            return False
        else:
            return self._artop_isRequired

    @property
    def ref_hwCategory_(self):
        return self._artop_hwCategory

    @property
    def hwCategory_(self):
        if self._artop_hwCategory is not None:
            if hasattr(self._artop_hwCategory, "uuid"):
                return self._artop_hwCategory.uuid
        return

    @property
    def hwAttributeLiterals_HwAttributeLiteralDef(self):
        return self._artop_hwAttributeLiteral

    @property
    def ref_unit_(self):
        return self._artop_unitRef

    @property
    def unit_(self):
        if self._artop_unitRef is not None:
            if hasattr(self._artop_unitRef, "uuid"):
                return self._artop_unitRef.uuid
        return

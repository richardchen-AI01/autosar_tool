# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucIntegerParamDef.py
from .EcucParameterDef import EcucParameterDef

class EcucIntegerParamDef(EcucParameterDef):

    def __init__(self):
        super().__init__()
        from .UnlimitedIntegerValueVariationPoint import UnlimitedIntegerValueVariationPoint
        self._artop_defaultValue = None
        self._artop_max = None
        self._artop_min = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_defaultValue':"UNLIMITED-INTEGER-VALUE-VARIATION-POINT", 
         '_artop_max':"UNLIMITED-INTEGER-VALUE-VARIATION-POINT", 
         '_artop_min':"UNLIMITED-INTEGER-VALUE-VARIATION-POINT"})

    @property
    def ref_defaultValue_(self):
        return self._artop_defaultValue

    @property
    def defaultValue_(self):
        if self._artop_defaultValue is not None:
            if hasattr(self._artop_defaultValue, "uuid"):
                return self._artop_defaultValue.uuid
        return

    @property
    def ref_max_(self):
        return self._artop_max

    @property
    def max_(self):
        if self._artop_max is not None:
            if hasattr(self._artop_max, "uuid"):
                return self._artop_max.uuid
        return

    @property
    def ref_min_(self):
        return self._artop_min

    @property
    def min_(self):
        if self._artop_min is not None:
            if hasattr(self._artop_min, "uuid"):
                return self._artop_min.uuid
        return

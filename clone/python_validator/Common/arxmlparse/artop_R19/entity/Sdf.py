# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Sdf.py
from .ARObject import ARObject

class Sdf(ARObject):

    def __init__(self):
        super().__init__()
        from .SdgContents import SdgContents
        from .NumericalValueVariationPoint import NumericalValueVariationPoint
        self._artop_gid = None
        self._artop_sdgContents = None
        self._artop_value = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_sdgContents':"SDG-CONTENTS", 
         '_artop_value':"NUMERICAL-VALUE-VARIATION-POINT"})

    @property
    def gid_(self):
        return self._artop_gid

    @property
    def ref_sdgContents_(self):
        return self._artop_sdgContents

    @property
    def sdgContents_(self):
        if self._artop_sdgContents is not None:
            if hasattr(self._artop_sdgContents, "uuid"):
                return self._artop_sdgContents.uuid
        return

    @property
    def ref_value_(self):
        return self._artop_value

    @property
    def value_(self):
        if self._artop_value is not None:
            if hasattr(self._artop_value, "uuid"):
                return self._artop_value.uuid
        return

# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MultiLanguageVerbatim.py
from .Paginateable import Paginateable

class MultiLanguageVerbatim(Paginateable):

    def __init__(self):
        super().__init__()
        from .LVerbatim import LVerbatim
        from .VariationPoint import VariationPoint
        self._artop_allowBreak = None
        self._artop_float = None
        self._artop_helpEntry = None
        self._artop_pgwide = None
        self._artop_l5 = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_l5':"L-VERBATIM", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def allowBreak_(self):
        return self._artop_allowBreak

    @property
    def float_(self):
        return self._artop_float

    @property
    def helpEntry_(self):
        return self._artop_helpEntry

    @property
    def pgwide_(self):
        return self._artop_pgwide

    @property
    def l5s_LVerbatim(self):
        return self._artop_l5

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return

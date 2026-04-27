# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ScaleConstr.py
from .ARObject import ARObject

class ScaleConstr(ARObject):

    def __init__(self):
        super().__init__()
        from .MultiLanguageOverviewParagraph import MultiLanguageOverviewParagraph
        from .LimitValueVariationPoint import LimitValueVariationPoint
        self._artop_validity = None
        self._artop_shortLabel = None
        self._artop_desc = None
        self._artop_lowerLimit = None
        self._artop_upperLimit = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_desc':"MULTI-LANGUAGE-OVERVIEW-PARAGRAPH", 
         '_artop_lowerLimit':"LIMIT", 
         '_artop_upperLimit':"LIMIT"})

    @property
    def validity_(self):
        return self._artop_validity

    @property
    def shortLabel_(self):
        return self._artop_shortLabel

    @property
    def ref_desc_(self):
        return self._artop_desc

    @property
    def desc_(self):
        if self._artop_desc is not None:
            if hasattr(self._artop_desc, "uuid"):
                return self._artop_desc.uuid
        return

    @property
    def ref_lowerLimit_(self):
        return self._artop_lowerLimit

    @property
    def lowerLimit_(self):
        if self._artop_lowerLimit is not None:
            if hasattr(self._artop_lowerLimit, "uuid"):
                return self._artop_lowerLimit.uuid
        return

    @property
    def ref_upperLimit_(self):
        return self._artop_upperLimit

    @property
    def upperLimit_(self):
        if self._artop_upperLimit is not None:
            if hasattr(self._artop_upperLimit, "uuid"):
                return self._artop_upperLimit.uuid
        return

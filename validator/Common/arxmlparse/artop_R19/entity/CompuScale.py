# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompuScale.py
from .ARObject import ARObject

class CompuScale(ARObject):

    def __init__(self):
        super().__init__()
        from .MultiLanguageOverviewParagraph import MultiLanguageOverviewParagraph
        from .LimitValueVariationPoint import LimitValueVariationPoint
        from .CompuConst import CompuConst
        from .CompuScaleContents import CompuScaleContents
        from .VariationPoint import VariationPoint
        self._artop_shortLabel = None
        self._artop_symbol = None
        self._artop_mask = None
        self._artop_desc = None
        self._artop_lowerLimit = None
        self._artop_upperLimit = None
        self._artop_compuInverseValue = None
        self._artop_compuScaleContents = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_desc': '"MULTI-LANGUAGE-OVERVIEW-PARAGRAPH"', 
         '_artop_lowerLimit': '"LIMIT"', 
         '_artop_upperLimit': '"LIMIT"', 
         '_artop_compuInverseValue': '"COMPU-CONST"', 
         '_artop_compuScaleContents': '"COMPU-SCALE-CONTENTS"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def shortLabel_(self):
        return self._artop_shortLabel

    @property
    def symbol_(self):
        return self._artop_symbol

    @property
    def mask_(self):
        return self._artop_mask

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

    @property
    def ref_compuInverseValue_(self):
        return self._artop_compuInverseValue

    @property
    def compuInverseValue_(self):
        if self._artop_compuInverseValue is not None:
            if hasattr(self._artop_compuInverseValue, "uuid"):
                return self._artop_compuInverseValue.uuid
        return

    @property
    def ref_compuScaleContents_(self):
        return self._artop_compuScaleContents

    @property
    def compuScaleContents_(self):
        if self._artop_compuScaleContents is not None:
            if hasattr(self._artop_compuScaleContents, "uuid"):
                return self._artop_compuScaleContents.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return

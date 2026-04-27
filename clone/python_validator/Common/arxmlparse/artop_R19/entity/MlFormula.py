# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MlFormula.py
from .Paginateable import Paginateable

class MlFormula(Paginateable):

    def __init__(self):
        super().__init__()
        from .Caption import Caption
        from .LGraphic import LGraphic
        from .MultiLanguageVerbatim import MultiLanguageVerbatim
        from .MultiLanguagePlainText import MultiLanguagePlainText
        from .VariationPoint import VariationPoint
        self._artop_formulaCaption = None
        self._artop_lGraphic = []
        self._artop_verbatim = None
        self._artop_texMath = None
        self._artop_genericMath = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_formulaCaption': '"CAPTION"', 
         '_artop_lGraphic': '"L-GRAPHIC"', 
         '_artop_verbatim': '"MULTI-LANGUAGE-VERBATIM"', 
         '_artop_texMath': '"MULTI-LANGUAGE-PLAIN-TEXT"', 
         '_artop_genericMath': '"MULTI-LANGUAGE-PLAIN-TEXT"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_formulaCaption_(self):
        return self._artop_formulaCaption

    @property
    def formulaCaption_(self):
        if self._artop_formulaCaption is not None:
            if hasattr(self._artop_formulaCaption, "uuid"):
                return self._artop_formulaCaption.uuid
        return

    @property
    def lGraphics_LGraphic(self):
        return self._artop_lGraphic

    @property
    def ref_verbatim_(self):
        return self._artop_verbatim

    @property
    def verbatim_(self):
        if self._artop_verbatim is not None:
            if hasattr(self._artop_verbatim, "uuid"):
                return self._artop_verbatim.uuid
        return

    @property
    def ref_texMath_(self):
        return self._artop_texMath

    @property
    def texMath_(self):
        if self._artop_texMath is not None:
            if hasattr(self._artop_texMath, "uuid"):
                return self._artop_texMath.uuid
        return

    @property
    def ref_genericMath_(self):
        return self._artop_genericMath

    @property
    def genericMath_(self):
        if self._artop_genericMath is not None:
            if hasattr(self._artop_genericMath, "uuid"):
                return self._artop_genericMath.uuid
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
